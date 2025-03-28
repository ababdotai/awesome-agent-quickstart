import os

def get_servers_dir():
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "servers")