# Do not forget to pin down the version
FROM jupyterhub/jupyterhub:1.0.0

# Copy the JupyterHub configuration in the container
COPY jupyterhub_config.py .

# Download script to automatically stop idle single-user servers
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install wget
RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/1.0.0/examples/cull-idle/cull_idle_servers.py

# Install dependencies (for advanced authentication and spawning)
RUN pip install --upgrade pip
RUN apt-get -y install git
RUN pip install \
    dockerspawner==0.10.0 \
    git+https://github.com/jupyterhub/ldapauthenticator.git
