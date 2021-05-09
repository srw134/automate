import requests
import json
import yaml

import urllib3 ##These lines used to avoid Self Signed Warnings
urllib3.disable_warnings()

#response = requests.post("https://192.168.1.239/api/auth/login", data = {"username":"admin", "password":"eve"}, verify=False)

##payload_tuples = [('username', 'admin'), ('password', 'eve'), ("html5", "0")]i


testcookie=requests.cookies.RequestsCookieJar()


##FIRST

data_call='{"username": "admin","password": "eve", "html5": "0"}'

print ("Login")

response = requests.post('https://192.168.1.239/api/auth/login', data=data_call, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(response.json())
    testcookie = response.cookies

elif response.status_code == 404:
    print("Unable to reach URL.")
elif response.status_code == 400:
    print("User Session Timeout")

    print(response.json())


elif response.status_code == 401:
    print("User Should Login")
elif response.status_code == 403:
    print("User Not Allowed")
else:
    print("Unable to connect API or retrieve data.")
    print(response.status_code)





##Second

print ("Status")

response = requests.get('https://192.168.1.239/api/status', cookies=testcookie, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 404:
    print("Unable to reach URL.")
elif response.status_code == 400:
    print("User Session Timeout")

    print(response.json())


elif response.status_code == 401:
    print("User Should Login")
elif response.status_code == 403:
    print("User Not Allowed")
else:
    print("Unable to connect API or retrieve data.")
    print(response.status_code)
    print(response.json())
    print(record['name'])













print ("Template")

response = requests.get('https://192.168.1.239/api/list/templates/', cookies=testcookie, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 404:
    print("Unable to reach URL.")
elif response.status_code == 400:
    print("User Session Timeout")

    print(response.json())


elif response.status_code == 401:
    print("User Should Login")
elif response.status_code == 403:
    print("User Not Allowed")
else:
    print("Unable to connect API or retrieve data.")
    print(response.status_code)
    print(response.json())
    print(record['name'])




print ("List Content")

response = requests.get('https://192.168.1.239/api/folders/', cookies=testcookie, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 404:
    print("Unable to reach URL.")
elif response.status_code == 400:
    print("User Session Timeout")

    print(response.json())


elif response.status_code == 401:
    print("User Should Login")
elif response.status_code == 403:
    print("User Not Allowed")
else:
    print("Unable to connect API or retrieve data.")
    print(response.status_code)
    print(response.json())
    print(record['name'])




##
##POST -d '{"path":"/User1/Folder 3","name":"New
#Lab","version":"1","author":"User1 Lastname","description":"A new demo
#lab","body":"Lab usage and guide"}' -H 'Content-type: application/json'
##http://127.0.0.1/api/labs


print ("Create Lab")

data_call='{"path": "/","name": "API_Lab_1"}'

response = requests.post('https://192.168.1.239/api/labs', data=data_call, cookies=testcookie, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 404:
    print("Unable to reach URL.")
elif response.status_code == 400:
    print("User Session Timeout")

    print(response.json())


elif response.status_code == 401:
    print("User Should Login")
elif response.status_code == 403:
    print("User Not Allowed")
else:
    print("Unable to connect API or retrieve data.")
    print(response.status_code)
    print(response.json())
    print(record['name'])



##ADD Node

##      <node id="1" name="vIOS1" type="qemu" template="vios" image="vios-adventerprisek9-m.vmdk.SPA.157-3.M3" console="telnet" cpu="1" cpulimit="0" ram="1024" ethernet="4" uuid="78cafd2c-bb43-4ead-9e0a-8ada11b54894" firstmac="50:00:00:01:00:00" qemu_options="-machine type=pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host" qemu_version="2.12.0" qemu_arch="x86_64" delay="0" sat="0" icon="Router.png" config="0" left="63" top="45"/>
#      <node id="2" name="vIOS2" type="qemu" template="vios" image="vios-adventerprisek9-m.vmdk.SPA.157-3.M3" console="telnet" cpu="1" cpulimit="0" ram="1024" ethernet="4" uuid="725fe3f9-8d5d-47f1-a0c2-04c05f5a9b02" firstmac="50:00:00:02:00:00" qemu_options="-machine type=pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host" qemu_version="2.12.0" qemu_arch="x86_64" delay="0" sat="0" icon="Router.png" config="0" left="240" top="45"/>
#      <node id="3" name="vIOS3" type="qemu" template="vios" image="vios-adventerprisek9-m.vmdk.SPA.157-3.M3" console="telnet" cpu="1" cpulimit="0" ram="1024" ethernet="4" uuid="7c4366b4-050d-46cc-b15d-4109483fb072" firstmac="50:00:00:03:00:00" qemu_options="-machine type=pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host" qemu_version="2.12.0" qemu_arch="x86_64" delay="0" sat="0" icon="Router.png" config="0" left="63" top="207"/>
##      <node id="4" name="vIOS4" type="qemu" template="vios" image="vios-adventerprisek9-m.vmdk.SPA.157-3.M3" console="telnet" cpu="1" cpulimit="0" ram="1024" ethernet="4" uuid="901eaf7c-c147-47b1-89c5-1f3851d427f4" firstmac="50:00:00:04:00:00" qemu_options="-machine type=pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host" qemu_version="2.12.0" qemu_arch="x86_64" delay="0" sat="0" icon="Router.png" config="0" left="240" top="207"/>


#POST -d '{"type":"qemu","template":"vios","config":"Unconfigured","delay":0,"icon":"Router.png","image":"vios-adventerprisek9-m-15.5.3M","name":"Core Router 1","left":"35%","top":"25%","ram":"1024","console":"telnet","cpu":1,"ethernet":2,"uuid":"641a4800-1b19-427c-ae87-4a8ee90b7790"}' -H 'Content-type: application/json' http://127.0.0.1/api/labs/User1/Folder%202/Different%20Lab.unl/nodes

print ("Create Node")

##Duplicate node names ARE allowed

data_call='{"name": "Router1","type": "qemu","template": "vios","icon": "Router.png","image": "vios-adventerprisek9-m.vmdk.SPA.157-3.M3","ram": "1024","ethernet": "4","firstmac": "50:00:00:04:00:00","qemu_options": "-machine type=pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host","left": "63","top": "45"}'


response = requests.post('https://192.168.1.239/api/labs/API_Lab_1.unl/nodes', data=data_call, cookies=testcookie, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 201:
    print("Lab has been saved - Node Added")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 404:
    print("Unable to reach URL.")
elif response.status_code == 400:
    print("User Session Timeout")

    print(response.json())


elif response.status_code == 401:
    print("User Should Login")
elif response.status_code == 403:
    print("User Not Allowed")
else:
    print("Unable to connect API or retrieve data.")
    print(response.status_code)
    print(response.json())
    print(record['name'])






print ("Node Info")

response = requests.get('https://192.168.1.239/api/labs/API_Lab_1.unl/nodes', cookies=testcookie, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    print(response.status_code)
    
    print("Parse Attempt")

    parse = response.json()
    

    ##Work here
    print("HERE")
 

    ##Here it is, this can be used to determine start or not. 0 for no, 2 for yes (type - int)
    print(type(parse["data"]["2"]["status"]))


    data = response.json()
    #print ("YAML")
    #print(yaml.dump(data))
else:
     print(response.status_code)
     print(yaml.dump(response.json()))






print ("Start Node")


data_call='{"username": "admin","password": "eve", "html5": "0"}'

print ("Login-Again")

response = requests.post('https://192.168.1.239/api/auth/login', data=data_call, verify=False)

if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(response.json())
    testcookie = response.cookies 


response = requests.get('https://192.168.1.239/api/labs/API_Lab_1.unl/nodes/1/start', cookies=testcookie, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 201:
    print("Lab has been saved - Not used here I don't believe")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 404:
    print("Unable to reach URL.")
elif response.status_code == 400:
    print("User Session Timeout")


    print(response.json())

elif response.status_code == 401:
    print("User Should Login")
elif response.status_code == 403:
    print("User Not Allowed")
else:
    print("Unable to connect API or retrieve data.")
    print(response.status_code)
    print(response.json())
    print(record['name'])









input("Press any key to Delete Node")


##Delete Node

#Nodes must be stopped before removal, needs to be a check first.





print ("Delete Node")


data_call='{"username": "admin","password": "eve", "html5": "0"}'

print ("Login-Again")

response = requests.post('https://192.168.1.239/api/auth/login', data=data_call, verify=False)

if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(response.json())
    testcookie = response.cookies 


response = requests.delete('https://192.168.1.239/api/labs/API_Lab_1.unl/nodes/1', cookies=testcookie, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 201:
    print("Lab has been saved - Node Added")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 404:
    print("Unable to reach URL.")
elif response.status_code == 400:
    print("User Session Timeout")


    print(response.json())

elif response.status_code == 401:
    print("User Should Login")
elif response.status_code == 403:
    print("User Not Allowed")
else:
    print("Unable to connect API or retrieve data.")
    print(response.status_code)
    print(response.json())
    print(record['name'])





input("Press any key to Delete lab")


data_call='{"username": "admin","password": "eve", "html5": "0"}'

print ("Login-Again")

response = requests.post('https://192.168.1.239/api/auth/login', data=data_call, verify=False)

if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(response.json())
    testcookie = response.cookies 


#http://127.0.0.1/api/labs/

print ("Delete Lab")


response = requests.delete('https://192.168.1.239/api/labs/API_Lab_1.unl', cookies=testcookie, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(yaml.dump(data))

elif response.status_code == 404:
    print("Unable to reach URL.")
elif response.status_code == 400:
    print("User Session Timeout")

    print(response.json())


elif response.status_code == 401:
    print("User Should Login")
elif response.status_code == 403:
    print("User Not Allowed")
else:
    print("Unable to connect API or retrieve data.")
    print(response.status_code)
    print(response.json())
    print(record['name'])



##Third

#data_call='{"username": "admin","password": "eve", "html5": "0"}'

print ("Logout")
#print (data_call)

response = requests.get('https://192.168.1.239/api/auth/logout', cookies=testcookie, verify=False)


if response.status_code == 200:
    print("Succesful connection with API.")
    data = response.json()

    print(response.json())

elif response.status_code == 404:
    print("Unable to reach URL.")
elif response.status_code == 400:
    print("User Session Timeout")

    print(response.json())


elif response.status_code == 401:
    print("User Should Login")
elif response.status_code == 403:
    print("User Not Allowed")
else:
    print("Unable to connect API or retrieve data.")
    print(response.status_code)


##print(testcookie)
