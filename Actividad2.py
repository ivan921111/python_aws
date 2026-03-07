import os
import subprocess
iOrR = "install"
defaultPackages = "htop curl git"
print ("Enter a list of packages to install")
print("The list should be separated by spaces. for example")
print("numpy pandas matplotlib")
print("Otherwise, input 'default' "+ iOrR + " the default packages listed in this program")
packages = input().lower()
if packages == "default":
    packages = defaultpackages
if iOrR == "install":
    try:
        subprocess.run(["pip3", "install"] + packages.split(), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar el packages: {e}")
   
   

    #subprocess.run(["sudo", "apt-get", "install"] + packages.split())
    #os.system("sudo apt-get install " + packages)

