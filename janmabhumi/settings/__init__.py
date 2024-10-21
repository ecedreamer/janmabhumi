from decouple import config


mode = config("MODE")
if mode == "PROD":
    from .prod_settings import *
else:
    from .dev_setttings import *
