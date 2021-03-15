import getpass

if getpass.getuser() in ["ubuntu", "root", "www-data"]:
	from .prod import *
else:
	from .dev import *
