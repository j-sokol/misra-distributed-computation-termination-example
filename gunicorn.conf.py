# import json
# import multiprocessing
# import os
# workers = os.getenv("WORKERS", "1")
# host = os.getenv("HOST", "0.0.0.0")
# port = os.getenv("PORT", "5049")
# bind_env = os.getenv("BIND", None)

# use_loglevel = os.getenv("LOG_LEVEL", "INFO")
# if bind_env:
#     use_bind = bind_env
# else:
#     use_bind = f"{host}:{port}"

# # Gunicorn config variables
# loglevel = use_loglevel
# bind = use_bind
# keepalive = 120
# errorlog = "-"
# timeout = 120

# # For debugging and testing
# log_data = {
#     "loglevel": loglevel,
#     "workers": workers,
#     "bind": bind,
#     # Additional, non-gunicorn variables
#     "host": host,
#     "port": port,
# }
# print(json.dumps(log_data))
