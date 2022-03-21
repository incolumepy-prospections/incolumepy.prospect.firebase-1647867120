"""
Principal Module.

Update metadata from version by semver
"""
import toml
from pathlib import Path

configfile = Path(__file__).parents[3].joinpath("pyproject.toml")
versionfile = Path(__file__).parent.joinpath("version.txt")

versionfile.write_text(f"{toml.load(configfile)['tool']['poetry']['version']}\n")

__version__ = versionfile.read_text().strip()
