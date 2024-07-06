import requests

def check_package_on_pypi(package_name):
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    if response.status_code == 200:
        data = response.json()
        if 'releases' in data:
            for release in data['releases']:
                if any(file['python_version'] == 'py3' or file['python_version'].startswith('cp39') for file in data['releases'][release]):
                    return True
    return False

def main():
    available_packages = []
    unavailable_packages = []

    with open('requirements.txt', 'r') as file:
        packages = [line.strip() for line in file.readlines()]

    for package in packages:
        if check_package_on_pypi(package):
            available_packages.append(package)
        else:
            unavailable_packages.append(package)

    with open('available_packages.txt', 'w') as file:
        file.write("\n".join(available_packages))

    with open('unavailable_packages.txt', 'w') as file:
        file.write("\n".join(unavailable_packages))

    print(f"Check completed. {len(available_packages)} packages are available for Python 3.9 on PyPI, {len(unavailable_packages)} packages are not.")
    print("Results are saved to available_packages.txt and unavailable_packages.txt")

if __name__ == "__main__":
    main()
