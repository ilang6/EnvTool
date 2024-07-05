import re
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import json
import requests
from decouple import config

# API keys Config

OPENAI_KEY = config('OPENAI_KEY')
SERPER_KEY = config('SERPER_KEY')


def get_latest_release_github(repo):
    """Get the latest release tag from a GitHub repository."""
    """
    Fetch the latest release tag from a specified GitHub repository.

    Args:
        repo (str): The GitHub repository in the format 'owner/repo'.
    
    Returns:
        str: The tag name of the latest release.

    Raises:
        requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
    
    Example:
        >>> get_latest_release_github('octocat/Hello-World')
        'v1.0.1'
    """
    url = f'https://api.github.com/repos/{repo}/releases/latest'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['tag_name']

def get_latest_anaconda_version():
    """Get the latest Anaconda version from the Anaconda website."""
    url = 'https://repo.anaconda.com/archive/'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    versions = [a.text for a in soup.find_all('a') if 'Anaconda3' in a.text and 'Linux-x86_64.sh' in a.text]
    latest_version = versions[0].split('-')[1]
    return latest_version

def get_latest_pycharm_rstudio_version(prompt,site):
    url = "https://google.serper.dev/search"
    payload = json.dumps({
        "q": f"latest {prompt} version site:{site}"
    })
    headers = {
        'X-API-KEY': SERPER_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    search_results = response.json()
    client = OpenAI(
    # This is the default and can be omitted
    api_key=OPENAI_KEY)

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"what is the latest {prompt} version from this text {search_results} respond only with version number",
        }
    ],
    model="gpt-4o",
    )
    # Regular expression to extract the content value from the provided string
    content_pattern = re.compile(r"content='([^']*)'")
    match = content_pattern.search(str(chat_completion))
    latest_version = match.group(1)
    return latest_version

def get_latest_rstudio_version():
    """Get the latest RStudio version from the RStudio website."""
    url = 'https://posit.co/download/rstudio-server/'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the download link for the RStudio Server .deb file
    link = soup.find('a', href=re.compile(r'.*rstudio-server.*-'))
    if not link:
        raise ValueError('Could not find the RStudio version link.')

    # Log the found link for debugging
    print(f"Found link: {link['href']}")

    version = re.search(r'rstudio-server-(\d+\.\d+\.\d+)-amd64\.deb', link['href']).group(1)
    return version
     

def update_dockerfile(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Update VSCodium version
    codium_version = get_latest_release_github('VSCodium/vscodium')
    content = re.sub(r'codium_\d+\.\d+\.\d+\.\d+_amd64\.deb', f'codium_{codium_version}_amd64.deb', content)
    content = re.sub(r'VSCodium/vscodium/releases/download/\d+\.\d+\.\d+\.\d+', f'VSCodium/vscodium/releases/download/{codium_version}', content)
    print(content)

    # Update Quarto version
    quarto_version = get_latest_release_github('quarto-dev/quarto-cli')
    content = re.sub(r'quarto-\d+\.\d+\.\d+-linux-amd64\.deb', f'quarto-{quarto_version[1:]}-linux-amd64.deb', content)
    content = re.sub(r'quarto-cli/releases/download/\d+\.\d+\.\d+', f'quarto-cli/releases/download/{quarto_version[1:]}', content)
    print(content)

    # Update Anaconda version
    anaconda_version = get_latest_anaconda_version()
    content = re.sub(r'Anaconda3-\d+\.\d+-Linux-x86_64\.sh', f'Anaconda3-{anaconda_version}-Linux-x86_64.sh', content)
    print(content)

    # Update PyCharm version
    pycharm_version = get_latest_pycharm_rstudio_version('pycharm','jetbrains.com')
    content = re.sub(r'pycharm-community-\d+\.\d+\.tar\.gz', f'pycharm-community-{pycharm_version}.tar.gz', content)
    print(content)

    
    # Update RStudio version
    rstudio_version = rstudio_version.replace('+','-')
    content = re.sub(r'rstudio-server-\d+\.\d+\.\d+-amd64\.deb', f'rstudio-server-{rstudio_version}-amd64.deb', content)


    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    dockerfile_path = '/Users/ilangofer/EnvTool/Dockerfile_V2 copy'
    update_dockerfile(dockerfile_path)
    print(f'Dockerfile updated with the latest versions of the tools.')



