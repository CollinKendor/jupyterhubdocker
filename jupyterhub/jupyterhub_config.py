import os,re

def create_dir_hook(spawner):
    """ Create directory """
    username = spawner.user.name  # get the username
    c.DockerSpawner.volumes = { 'jupyterhub-user-'+re.sub('[^a-zA-Z0-9_.-]','_',username): notebook_dir }

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.Spawner.pre_spawn_hook = create_dir_hook

c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.server_address = '13.250.1.38'
c.LDAPAuthenticator.server_port = 10389
c.LDAPAuthenticator.bind_dn_template = [
    'uid={username},ou=user,dc=kewmann,dc=com'
]
c.LDAPAuthenticator.lookup_dn = True
c.LDAPAuthenticator.lookup_dn_search_filter = '({login_attr}={login})'
c.LDAPAuthenticator.user_search_base = 'ou=user,dc=kewmann,dc=com'
c.LDAPAuthenticator.user_attribute = 'uid'
c.LDAPAuthenticator.lookup_dn_user_dn_attribute = 'uid'
c.LDAPAuthenticator.valid_username_regex = '.+'
c.Authenticator.admin_users = {'deric.dominic@kewmann.com'}
