from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from beerlog.core import add_beer_to_database, get_beers_from_database

main = typer.Typer(help="Beer Management Application")
console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Add a new beer to database"""
    if add_beer_to_database(name, style, flavor, image, cost):
        print('🍺 beer added to database')


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists a beers in database"""
    beers = get_beers_from_database()
    table = Table(title="Beerlog")
    headers = ['id', 'name', 'style', 'flavor', 'image', 'cost', 'rate', 'date']
    for header in headers:
        table.add_column(header, style='magenta')

    for beer in beers:
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
