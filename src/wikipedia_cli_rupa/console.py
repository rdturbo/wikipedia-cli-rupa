# src/wikipedia_cli_rupa/console.py
import textwrap
import click

from . import __version__, wikipedia


@click.command()
@click.version_option(version=__version__)
def main():
    """The Wikipedia Command Line Interface project."""
    data = wikipedia.random_page()
    
    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
