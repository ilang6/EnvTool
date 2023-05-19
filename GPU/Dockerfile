FROM nvcr.io/nvidia/pytorch:23.04-py3

WORKDIR /workspace/
COPY . .

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y tzdata krb5-kdc krb5-admin-server krb5-config krb5-user 
RUN pip install -r requirements.txt
RUN apt --allow-unauthenticated --allow-insecure-repositories update 
RUN apt install -y apt-transport-https
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y \
                    apt-utils \
                    git \
                    build-essential \
                    wget \
                    htop \
                    nano \
                    openssl libssl-dev \
                    libcairo2 \
                    libcairo2-dev \
                    libcurl4-openssl-dev \
                    unixodbc* \
                    unixodbc-dev \
                    r-cran-rodbc \
                    freetds-bin \
                    freetds-common \
                    tdsodbc \
                    libxt-dev libgtk2.0-dev xvfb xauth xfonts-base \
                    libxml2-dev \
                    default-jre \
                    openjdk-8-jdk \
                    default-jdk \
                    r-cran-rjava \
                    freetds-dev \
                    libudunits2-dev \
                    gfortran \
                     wget \
                    libxtst6 \
                    default-jre \
                    curl \
                    openssh-client \
                    openssh-server \
                    openssh-sftp-server \
                    librsvg2-dev \
                    samba \
                    perl \
                    libv8-dev \
                    libnode-dev \
                    libnet-ssleay-perl \
                    libauthen-pam-perl \
                    libpam-runtime \
                    libio-pty-perl  \
                    cifs-utils \
                    zsh \
                    powerline \
                    fonts-powerline \
                    gedit\
                    msktutil  \
                    libgit2-dev \
                    libpq-dev \
                    libfreetype6-dev\
                    libfreetype6\
                    libpng-dev\ 
                    libtiff5-dev\
                    libjpeg-dev\
                    nodejs\
                    npm\
                    cmake\
                    graphviz
RUN  curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN  curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN  apt update
RUN  apt-get update \
    && ACCEPT_EULA=Y apt-get -y install msodbcsql18
RUN  ACCEPT_EULA=Y apt-get install -y mssql-tools18
RUN  echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bash_profile
RUN  echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
RUN  apt-get install -y unixodbc-dev
RUN  wget https://github.com/VSCodium/vscodium/releases/download/1.76.2.23074/codium_1.76.2.23074_amd64.deb
RUN  dpkg -i codium_1.76.2.23074_amd64.deb
RUN  wget https://download.jetbrains.com/python/pycharm-community-2022.3.tar.gz
RUN  tar -xzf pycharm-community-2022.3.tar.gz
RUN  rm pycharm-community-2022.3.tar.gz
RUN  curl -fsSL https://code-server.dev/install.sh | sh
RUN  mkdir -p ~/.local/share/code-server/ \
    && mkdir -p ~/.local/share/code-server/User 
RUN  code-server --force --install-extension ms-python.python \
    && code-server --force --install-extension Ikuyadeu.r \
    && code-server --force --install-extension REditorSupport.r-lsp \
    && code-server --force --install-extension ms-toolsai.jupyter \
    && code-server --force --install-extension hdg.live-html-previewer-0.3.0.vsix \
    && code-server --force --install-extension ms-python.vscode-pylance \
    && code-server --force --install-extension neuron.neuron-IPE-1.0.4.vsix \
    && code-server --force --install-extension quarto.quarto \
    && code-server --force --install-extension ms-toolsai.jupyter-keymap \
    && code-server --force --install-extension njpwerner.autodocstring \
    && code-server --force --install-extension eamodio.gitlens \
    && code-server --force --install-extension bierner.markdown-mermaid 