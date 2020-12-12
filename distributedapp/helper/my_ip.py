import socket


def get_my_ip() -> str:

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip: str = s.getsockname()[0]
    except Exception:
        ip: str = '127.0.0.1'
    finally:
        s.close()

    return ip
