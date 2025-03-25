
from netmiko import ConnectHandler
from datetime import datetime

def run_commands():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    
    for device in config["devices"]:
        try:
            connection = ConnectHandler(
                host=device["host"],
                device_type=device["device_type"],
                username=device["username"],
                password=device["password"]
            )
            
            print(f"\n=== {device['host']} ===")
            for cmd in device["commands"]:
                output = connection.send_command(cmd)
                print(f"\n{cmd}:\n{output}")
                
                # Extract key details (example for show version)
                if "show version" in cmd:
                    hostname = connection.find_prompt()[:-1]
                    uptime = output.split("uptime is")[1].split("\n")[0]
                    print(f"\nHostname: {hostname}\nUptime: {uptime}")
            
            connection.disconnect()
            
        except Exception as e:
            print(f"Failed on {device['host']}: {str(e)}")
            log_error(device["host"], str(e))

if __name__ == "__main__":
    run_commands()
