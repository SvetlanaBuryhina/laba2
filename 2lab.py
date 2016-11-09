import re
f1= open('access.log' , 'r')
unique=set()
for line in f1.readlines():
    pattern = '\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[‌​0-5]|2[0-4][0-9]|[01‌​]?[0-9][0-9]?)\\b'
    ips = re.findall(pattern, line)
    for i in range (len(ips)):
        if ips[i] in unique:
            pass
        else:
            unique.add(ips[i])
subnet=set()
for item in unique:
    pattern = '(\d{1,3}\.\d{1,3}\.\d{1,3}\.)\d{1,3}'
    result = re.findall(pattern, item)
    for i in range (len(result)):
        subnet.add(result[i])
for element in subnet:
    for ip in unique:
        if ip.startswith(element):
            print(ip)
    print(" ")  
