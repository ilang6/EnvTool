import subprocess

def install(package):
    try:
        subprocess.check_call([f'pip install {package}'], shell=True)
    except subprocess.CalledProcessError:
        pass
    print(f'Successfully installed {package}')

with open('available_packages.txt') as f:
    packages = f.readlines()

for package in packages:
    install(package.strip())
