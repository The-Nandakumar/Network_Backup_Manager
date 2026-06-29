from netmiko import ConnectHandler
import paramiko
import logging

class ConnectionManager:

    def __init__(self, jump_host, jump_user, jump_password):
        self.jump_host = jump_host
        self.jump_user = jump_user
        self.jump_password = jump_password
        self.jump_client = None

    def _connect_jump_host(self):
        try:
            self.jump_client = paramiko.SSHClient()
            self.jump_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            self.jump_client.connect(
                hostname=self.jump_host,
                username=self.jump_user,
                password=self.jump_password,
                timeout=20
            )

            return self.jump_client

        except Exception as e:
            logging.error(f"Failed to connect to jump host: {e}")
            return None

    def connect(self, device_ip, username, password, device_type):
        try:
            # Step 1: Connect to jump host
            jump = self._connect_jump_host()
            if not jump:
                return None

            # Step 2: Create tunnel (channel) to device
            jump_transport = jump.get_transport()
            dest_addr = (device_ip, 22)
            local_addr = ("", 0)

            channel = jump_transport.open_channel(
                "direct-tcpip",
                dest_addr,
                local_addr
            )

            # Step 3: Connect to device via Netmiko using socket
            device = {
                "device_type": device_type,
                "host": device_ip,
                "username": username,
                "password": password,
                "sock": channel,

                "conn_timeout": 20,
                "banner_timeout": 20,
                "auth_timeout": 20,
                "global_delay_factor": 2,
            }

            ssh = ConnectHandler(**device)
            return ssh

        except Exception as e:
            logging.error(f"Failed to connect to {device_ip} via jump host: {e}")
            return None

    def disconnect(self, ssh):
        try:
            if ssh:
                ssh.disconnect()
        except Exception as e:
            logging.error(f"Disconnect error: {e}")

    def close_jump(self):
        try:
            if self.jump_client:
                self.jump_client.close()
        except Exception as e:
            logging.error(f"Jump host disconnect error: {e}")