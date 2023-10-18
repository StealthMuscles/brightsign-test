# brightsign-test

Hello,
Thank you for the little test project.  Here are instructions to build and run:

- Clone repo
- `bin/build`
- Define the shell variable LOCATEIP_API_KEY set to the value of your ipscan.com API key - `export LOCATEIP_API_KEY=<your key>`
- `bin/locateip <ipaddress>`

The program should output the latitude and longitude values, space-separated, to stdout on success and return 0.  On any failure, a relevant error message should be output to stderr and the return value should be non-zero.

Dev builds:
Reqs: python 3.10, pipenv (although the only 3rd party package in use is requests)
- `pipenv install`
- `pipenv run python3 locateip.py <ipaddress>`

Notes:
I was in a bit of a rush, so I would probably wrap this in scripts or use docker-compose before distributing this as an actual command line tool.

Security considerations:
The program currently expects the API key to be set in an environment variable, whose values is passed in via the docker run --env command line argument.  A more robust method would be to use a proper secure store such as HashiCorp Vault or Mozilla SOPS and manage this as part of whatever larger set of secrets used in an enterprise environment.  Beyond that, the api itself runs on http, which is a no-no.  I also do have the docker build creating and using a user other than root.
