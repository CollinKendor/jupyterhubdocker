# Jupyterhub Implementation with Docker Spawner
This implementation is base on the following guide:
https://opendreamkit.org/2018/10/17/jupyterhub-docker/#:~:text=%E2%80%9CThe%20littlest%20JupyterHub%E2%80%9D%20adheres%20to,and%20users%20can%20share%20data.

# What's Different.
1.  There is no https as I could not det domain in my server.
2.  LDAPAuthenticator is installed from git.
3.  Special characters in username is replaced with _ for data persistance.
