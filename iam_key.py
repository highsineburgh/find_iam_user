"""
A module to return the user associated with the specified aws_access_key_id.
AWS credentials for IAM access can either be provided via the command line or placed in a credentials file.

Usage:
    iam_key.py <key_id> [--region=<reg> --key_id=<key> --secret_key=<secret_key>]


    Options:
        -h --help                       Show this screen.
        -v --version                    Print the version number
        --region=<reg>                  AWS region to connect to [default: us-west-2]
        --key_id=<key>                  AWS access_key_id
        --secret_key=<secret_key>       AWS secret_access_key
"""
__author__ = 'tfield'


try:
    from docopt import docopt
except ImportError:
    exit("This script requires the use of the docopt argument parsing package\n"
         "pip install docopts\n"
         "http://docopt.org/")


if __name__ == '__main__':
    arguments = docopt(__doc__, version="0.1.0")