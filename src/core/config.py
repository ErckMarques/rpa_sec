"Módulo responsável por carregar e armazenar as configurações do aplicativo."
from pathlib import Path

from dynaconf import Dynaconf


settings = Dynaconf(
    envvar_prefix="RPA",
    settings_files=[Path().cwd().joinpath('settings.toml').absolute(), Path().cwd().joinpath('.secrets.toml').absolute()],
    load_dotenv=True
)
