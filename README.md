# brightsign-test

Hello,
Thank you for the little test project.  Here are instructions to build and run:

- `docker build -t locateip https://github.com/StealthMuscles/brightsign-test.git#main`
- `docker run locateip <ipaddress>`

(or you can clone this and run `docker build -t locateip .` to build instead)

The program should output the latitude and longitude values, space-separated, to stdout on success and return 0.  On any failure, a relevant error message should be output to stderr and the return value should be non-zero.

Dev builds:
Reqs: python 3.10, pipenv (although the only 3rd party package in use is requests)
- `pipenv install`
- `pipenv run python3 locateip.py <ipaddress>`

Notes:
I was in a bit of a rush, so I would probably wrap this in scripts or use docker-compose before distributing this as an actual command line tool.

Security considerations:
Currently the ipstack API key is defined in the Dockerfile as an environment variable and read by the program from the executing shell environment.  This is obviously bad as the key is now exposed to the world in my currently public github repo.  A more secure method would be to use some secrets management tool like AWS Secrets Manager or HashiCorp vault to distribute the secret to this program setup to run as an endpoint service in some cloud.  If the program is inteded to be distributed locally as is, then some method for adding and storing the API key would need to be created (the simplest method being make the user get their own key and import into the environment somehow via shell profile or sourced .env file, etc.)
