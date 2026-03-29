# enumerate
# zip

# servers = ["web-01", "web-02", "web-03"]
# [(0, "web-01"), (1, "web-02"),(2, "web-03")]
# for server in enumerate(servers):
#     print(type(server))
#     print(server)
#     print(f"this is tuple {server}")
    

servers = ["web-01", "web-02", "web-03"]
# [(0, "web-01"), (1, "web-02"),(2, "web-03")]
for index, server in enumerate(servers, start=100):
    # print(type(server))
    # print(server)
    # print(server[0]) # index
    # print(server[1]) # item
    print(f"{index} Proccessing server {server}")