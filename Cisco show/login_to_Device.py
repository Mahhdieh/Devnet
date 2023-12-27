from netmiko import ConnectHandler

connect = ConnectHandler(host="192.168.98.102", device_type ="cisco_ios" ,username ="test" ,password = "test")
show_ver = connect.send_command("show ver")


print(show_ver)