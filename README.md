# find_iam_user
A simple script to identify the the IAM user associated with an aws_access_key.

## Installation
This script was designed to be used from the command line, ideally in a virtual environment. To install 
the depdendancies navigate to the root folder of the project and use pip. 

```bash
git clone git@github.com:highsineburgh/find_iam_user.git
cd find_iam_user
pip install -r requirements.txt
```

## Use 
From the command line, if you have a credentials file located in the default position (~/.aws/credentials 
for Linux/Mac): 

```bash
python iam_key.py <target_key> 
```

Alternatively you may pass the your aws_access_key_id and aws_secret_key_id as parameters

```bash
python iam_key.py <target_key> --key_id=<aws_access_key_id> --secret_key=<aws_secret_key_id>
```
