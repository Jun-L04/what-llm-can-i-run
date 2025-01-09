"""This module provides the what-llm-can-i-run CLI."""
from typing import Optional
import typer
from whatllm import __app_name__, __version__
from .ram import get_total_ram
from .vram import get_machine_spec
import logging


app = typer.Typer()


def _version_callback(value: bool) -> None:

    if value:

        typer.echo(f"{__app_name__} v{__version__}")

        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


# gets hardware spec (or throws an error) and then exits
@app.command(name="spec")
def get_hardware_info():
    print(f"Total RAM: {get_total_ram()} GiB")

    try:
        spec = get_machine_spec()
        typer.echo(f'Platform: {spec[0]}')
        typer.echo(f'Device: {spec[1]}')
        typer.echo(f'Total VRAM: {spec[2]} GiB')
    except Exception as e:
        typer.echo(f"Error: {e}")
        logging.error(e)
    finally:
        typer.Exit()
