hosts = [
    "host-A", 
    "host-B", 
    "host-C"
]

ips = [
    "10.0.0.1",
    "10.0.0.2",
    "10.0.0.3"
]

azs = [
    "us-east-1a",
    "us-east-1b",
    "us-east-1c"
]

all_servers = zip(hosts, ips, azs)
print(list(all_servers))

for host, ip, az in zip(hosts, ips, azs):
    # Print a stsus of " "Scanning " " specific server each time
    # "Scanning server Host-A located at us-east-1a with ip 10.0.0.1"
    print(f"Scanning server {host} located at {az} with ip {ip}")
    
    
# dummy_list = [("niv", "bar"), ("mike", "nogh"), ("yoni", 93)]

# for first_name, last_name in dummy_list:
#     print(f"First Name: {first_name} | Last Name: {last_name}")