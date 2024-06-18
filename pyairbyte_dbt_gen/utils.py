def create_file_path(*parts: str) -> str:
    """
    create a file path with the give str list
    """
    file_path = "/".join(p for p in parts)
    return file_path

def create_clickhouse_profile(project_name:str, profile: str, username:str, password: str, host: str, port: str, driver: str,secure: bool)-> list[str] :
    """
    create profile for clickhouse database
    """
    return [
            f"{project_name}:\n",
            f"  target: {profile}\n",
            f"  outputs:\n",
            f"    {profile}:\n",
            f"      type: clickhouse\n",
            f"      schema: default\n",
            f'      host: {host}\n',
            f'      port: {port}\n',
            f"      driver: {driver}\n",
            f'      user: {username}\n',
            f'      password: {password}\n',
            f'      secure: {secure}\n',
    ]