# Jupyterhub Implementation with Docker Spawner
This implementation is base on the following guide:
https://opendreamkit.org/2018/10/17/jupyterhub-docker/#:~:text=%E2%80%9CThe%20littlest%20JupyterHub%E2%80%9D%20adheres%20to,and%20users%20can%20share%20data.

# Extra Information
1.  Installed in a single Ubuntu 20.04 server.
2.  Install Docker Engine and Docker Compose in server before starting.

# What's Different.
1.  There is no https as I could not det domain in my server.
2.  Using LDAP authentication instead of OAuth. LDAPAuthenticator is installed from git.
3.  Special characters in username is replaced with _ using bootstrap method for data persistance.

# Information Needed Before Starting Engines.
1.  HOST in .env file. Please enter the IP or Hostname of reverse proxy.
2.  jupyterhub/jupyterhub_config.py:
    -  c.LDAPAuthenticator.server_address - Put LDAP server hostname or IP
    -  c.LDAPAuthenticator.server_port    - LDAP port. Set to 389 at the moment.
    -  c.Authenticator.admin_users        - Set an admin user from LDAP
