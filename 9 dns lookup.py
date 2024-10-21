import socket
def main():
print("1.Enter Host Name \n2.Enter IP address")
 choice = int(input("Choice="))
if choice == 1:
 host = input("\nEnter host name: ")
try:
 address = socket.gethostbyname(host)
print("IP address: ", address)
print("Host name : ", host)
print("Host name and IP address: ", f"{host}/{address}")
except socket.gaierror:
print("Could not find ", host)
elif choice == 2:
 host = input("\nEnter IP address: ")
try:
 address = socket.gethostbyaddr(host)
print("Host name : ", address[0])
print("IP address: ", host)
print("Host name and IP address: ", f"{address[0]}/{host}")
except socket.herror:
print("Could not find ", host)
else:
print("Invalid choice")
if __name__ == "__main__":
 main()
