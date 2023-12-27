
from ncclient import manager
from jinja2 import Environment,FileSystemLoader,Template
import yaml
from yaml import safe_load

# Create a template for the rpc_request to config router bgp
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("BGP-Template.j2")

# Load the data for configuring bgp neighborship
with open ("BGP-Data.yml" , "r") as data:
   bgp_data = yaml.safe_load(data)

# render template with the data
bgp_config = template.render(bgp_data)


# netconf to the device and push the configs
with manager.connect(host="192.168.24.188",port="830", username="devnet", password="devnet", hostkey_verify=False) as device:
    config = device.edit_config(target="running", config=bgp_config)

# Just to print something on end of code execution
print("New BGP neighborship is configured")




    
