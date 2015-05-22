"""
A module to return the user associated with the specified aws_access_key_id.
AWS credentials for IAM access can either be provided via the command line or placed in a credentials file.

Usage:
    iam_key.py <target_key> [--key_id=<key> --secret_key=<secret_key>]


    Options:
        -h --help                       Show this screen.
        -v --version                    Print the version number
        --key_id=<key>                  AWS access_key_id
        --secret_key=<secret_key>       AWS secret_access_key
"""
__author__ = 'tfield'


import os

try:
    from docopt import docopt
except ImportError:
    exit("This script requires the use of the `docopt` argument parsing package\n"
         "pip install docopts\n"
         "http://docopt.org/")

try:
    from schema import Schema, And, Or, SchemaError, Use
except ImportError:
    exit("This script requires that `schema` data-validation library is installed: \n"
         "pip install schema\n"
         "https://github.com/halst/schema")

try:
    from boto import iam
except ImportError:
    exit("This script requires the `boto` package for access AWS\n"
         "pip install boto\n"
         "http://docs.pythonboto.org/en/latest/")


def validate_keys(key, length):
    if key:
        return len(key) == length
    else:
        return os.path.exists(os.path.expanduser('~/.aws/credentials'))


if __name__ == '__main__':
    arguments = docopt(__doc__, version="0.1.0")

    schema = Schema({
        '<target_key>': lambda x: len(x) == 20,
        '--key_id': lambda x: validate_keys(x, 20),
        '--secret_key': lambda x: validate_keys(x, 40)
    })

    try:
        args = schema.validate(arguments)
    except SchemaError as e:
        exit('Error validating inputs please ensure that the target key is in the correct format and that an AWS '
             'credentials file exists at the default location or the access key and secret key are provided as parameters')
