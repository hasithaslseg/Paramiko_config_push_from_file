import paramiko
import time

"""
Please enter your credentials to log in to the router
"""

username = input("Please Enter Your User Name: ")
password = input("Please Enter Your Password: ")


"""
node_list.txt: contains the list of the MGT IPs/Hostnames
commands_list: contains the list of commands in order of execution
"""

with open("node_list.txt") as f1:
    node_list=f1.readlines()

with open("command_list.txt") as f2:
    command=f2.readlines()



#command = ["enable\n","\n","test\n","\n","ter len 0\n","\n","config t\n","\n","hostname DR-3\n","do show ip int br","\n"]

for hostname1 in node_list:

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname1.strip('\n'), port=22, username=username,
                password=password,
                look_for_keys=False, allow_agent=False)

    except Exception as e:
        print(f"{e} Please check the issue in {hostname1.strip()}")
        pass

    else:
        remote_conn = ssh.invoke_shell()
        for y in command:

            remote_conn.send(y)
            time.sleep(0.6)
        output = remote_conn.recv(65535)
        filename=hostname1.strip('\n')+".txt"
        with open(filename,'w') as f3:
            f3.write(output.decode().strip())
        print(f"Connection to {hostname1.strip()} is successful...Output is saved in {filename}")



