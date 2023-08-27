"""Configuration for DP - NF"""
from pathlib import Path
from dynaconf import Dynaconf

relative_path = 'DP/nf/scripts'
project = 'config.py'
config_path = Path.cwd() / relative_path / project

settings = Dynaconf(
    root_path = config_path,
    settings_files = ['settings.toml']
)
