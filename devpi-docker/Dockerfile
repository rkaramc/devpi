FROM python:3-slim

RUN pip install --no-cache-dir \
    devpi-client \
    devpi-server \
    devpi-web

# ENV PYPI_PASSWORD
EXPOSE 3141
WORKDIR /root
VOLUME /root/.devpi

COPY create_pypi_index.sh /data/create_pypi_index.sh
RUN chmod a+x /data/create_pypi_index.sh

COPY entrypoint.sh /data/entrypoint.sh
ENTRYPOINT ["bash", "/data/entrypoint.sh"]

COPY config.yml /data/config.yml
CMD ["devpi-server", "-c", "/data/config.yml"]
