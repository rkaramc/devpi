# Using `devpi`[^devpi] as a local mirror

Using `devpi` as a local mirror for `https://pypi.org`, and as a private index for Python packages.

Install `devpi` in `docker` following instructions at (Mphego, 2021)[^Mphego2021]:

```bash
# install devpi using docker in project c:\users\rkara\cascadeprojects\devpi
docker-compose --env-file ./.env -f docker-compose-dev.yaml up --build -d
docker exec -ti devpi-devpi-1 /bin/bash -c "/data/create_pypi_index.sh"

# create user packages
devpi user -c packages email=packaging@company.com

# login as user packages
devpi login packages

# create indexes packages/stable and packages/staging
devpi index -c packages/stable bases=root/pypi volatile=False
devpi index -c packages/staging bases=packages/stable volatile=True
```

Configure your project to use `devpi`:

```bash
# activate devpi packages/staging index
devpi use packages/staging

# update pyproject.toml to use packages/staging
#
#  [[tool.uv.index]]
#  name = "devpi-staging"
#  url = "http://localhost:3141/packages/staging"
#  publish-url = "http://localhost:3141/packages/staging/+simple/"
#  default = true
#
# run ./show-index.py to verify these keys are set in pyproject.toml

# make changes, update version, build package
uv build

# remove package from current index on devpi
devpi use packages/staging
devpi upload --from-dir dist
devpi remove devpi-config==0.1.0

# upload to and remove from a specific index (packages/stable) on devpi
devpi upload --from-dir dist --index packages/stable
devpi remove devpi-config==0.1.0 --index packages/stable

```

[^Mphego2021]: Mphego, M. (2021) 'How I setup a private local PYPI server using Docker and Ansible,' Mpho Mphego, 15 June. https://blog.mphomphego.co.za/blog/2021/06/15/How-I-setup-a-private-PyPI-server-using-Docker-and-Ansible.html.

[^devpi]: devpi: PyPI server and packaging/testing/release tool — devpi server-6.13, client-7.1, web-4.2 documentation (no date). https://devpi.net/docs/devpi/devpi/latest/+doc/index.html#.
