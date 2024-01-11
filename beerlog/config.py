import os

from dynaconf import Dynaconf  # coversa nativamente com VAULT


settings = Dynaconf(
    envvar_prefix="BEERLOG",
    root_path=os.path.dirname(__file__),
    settings_files=["settings.toml"],
)

# export BEERLOG_DATABASE__url="sqlite:///testing.db"
