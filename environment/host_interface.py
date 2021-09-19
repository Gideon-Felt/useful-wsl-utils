def get_resolvers(default: str = "127.0.0.1") -> str:
    """
    if using WSL will access /etc/resolv.conf and parse the host address, may access service provided on host machine.
    (WSL must have the Windows Firewall open).
    :return: str ip address default 127.0.0.1
    """
    resolvers: List = []
    try:
        with open("/etc/resolv.conf", encoding='utf-8') as resolve_conf:
            line: str
            for line in resolve_conf.readlines():
                line = line.split('#', 1)[0].rstrip()
        if 'nameserver' in line:
            resolvers.append(line.split()[1])
        return resolvers[0] if len(resolvers) > 0 else default
    except Exception as err:
        return default
