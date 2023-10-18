# brightsign-test

Hello,
Thank you for the little test project.  Here are instructions to build and run:

- Clone the repo
- `bin/build`
- Define a shell variable `LOCATEIP_API_KEY` set to the value of your ipstack.com API key - `export LOCATEIP_API_KEY=<key>`
- `bin/locateip <ipaddress>`

The program should output the latitude and longitude values, space-separated, to stdout on success and return 0.  On any failure, a relevant error message should be output to stderr and the return value should be non-zero.

Dev builds:
Reqs: python 3.10, pipenv (although the only 3rd party package in use is requests)
- `pipenv install`
- `pipenv run python3 locateip.py <ipaddress>`

Security considerations:
The program currently expects the API key to be set in an environment variable, whose values is passed in via the docker run --env command line argument.  A more robust method would be to use a proper secure store such as HashiCorp Vault or Mozilla SOPS and manage this as part of whatever larger set of secrets used in an enterprise environment.  Beyond that, the api itself runs on http, which is a no-no.  I also do have the docker build creating and using a user other than root.
