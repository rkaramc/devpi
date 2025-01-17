#!/usr/bin/env bash

# Creates PyPI user and an index for uploading packages to

devpi use http://localhost:3141
devpi login root --password=
devpi user -c pypi email= password=${PYPI_PASSWORD:-}
devpi index -c pypi/stable bases=root/pypi volatile=True mirror_whitelist=*
devpi user -c packages email= password=${PYPI_PASSWORD:-}
devpi index -c packages/stable bases=pypi/stable volatile=True mirror_whitelist=*
devpi index -c packages/staging bases=packages/stable volatile=True mirror_whitelist=*
