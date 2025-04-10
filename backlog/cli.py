#!/usr/bin/env python3

import click

@click.group()
def cli():
    """Backlog - AI-Directed Task Backlog Manager"""
    pass

@cli.command()
def hello():
    """Prints a friendly hello message"""
    click.echo("👋 Hello from Backlog! Let's manage some tasks.")


if __name__ == "__main__":
    cli()
