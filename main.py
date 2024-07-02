import subprocess
import requests
domfull =[]
hashcat_command = r"wsl hashcat --force --opencl-device-type=1 list.txt -r /usr/share/hashcat/rules/best64.rule --stdout > maybedom.txt"
process = subprocess.Popen(str(hashcat_command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Get the output and error messages
output, error = process.communicate()

# Print the output and error messages
print(output.decode('utf-8', errors='replace'))
print(error.decode('utf-8', errors='replace'))
with open('maybedom.txt' , 'r') as f :
    maybedom_list = [line.strip() for line in f.readlines()]
with open('domain_names_extensions.txt', 'r') as ext :
    domain_names_extensions = [line.strip() for line in ext.readlines()]
for i in maybedom_list :
    for x in domain_names_extensions:
        domfull.append(str(i) + '.' + str(x))
print (domfull)
#def is_domain_up(domain):
#    try:
#        response = requests.get(f'http://{domain}')
#        print( str(domain) , 'IS UP')
#        return response.status_code == 200
#        
#    except requests.exceptions.RequestException:
#        print('Pas de soucis')
#        return False