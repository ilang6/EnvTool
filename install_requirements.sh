# install_requirements.sh
#!/bin/bash

set -e

echo "Installing requirements"
/opt/conda/bin/python install_requirements.py || true
