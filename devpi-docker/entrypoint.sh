#!/usr/bin/env bash
if ! [ -f /root/.devpi/server ]; then
    devpi-init
fi

exec "$@"
