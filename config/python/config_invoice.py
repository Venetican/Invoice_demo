"""Configuration for DP - NF"""
from pathlib import Path
from dynaconf import Dynaconf

relative_path = 'config/python'
config = 'config_invoice.py'
config_path = Path.cwd() / relative_path / config

settings = Dynaconf(
    root_path = config_path,
    settings_files = ['settings.toml']
)
