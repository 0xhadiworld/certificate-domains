# certificate-domains
A tool for extracting domains based on SSL/TLS certificates from the Crt.sh website

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation
```bash
git clone https://github.com/0xhadiworld/certificate-domains.git
cd certificate-domains
pip install -r requirements.txt  # Corrected typo in requirements
python3 main.py -h

# Usage
# Basic Usage
python3 main.py -o Example
# Save Results to a File
python3 main.py -o Example -f output.txt

