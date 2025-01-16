"""This module provides the what-llm-can-i-run CLI."""
from typing import Optional
import typer
from whatllm import __app_name__, __version__, VRAM_ERROR
from .ram import get_total_ram
from .vram import get_machine_spec
from .llm_list import get_llm_list, list_to_excel
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
    """
    """
    typer.echo(f"Total RAM: {get_total_ram()} GiB")

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

# get a list of recommended LLMs to run based on hardware spec
@app.command(name="list")
def get_llm_list_wrapper(precision: str = typer.Argument("fp16", help="Precision of the model. Lower means more overhead.")):
    """
    
    """
    # check if user given precision is valid
    if precision.lower() not in ['int4', 'int8', 'fp16', 'fp32']:
        typer.echo("Precision should be: 'int4', 'int8', 'fp16', or 'fp32'.")
        raise typer.Exit()
    
    # retrieve hardware specs first
    capacity = get_total_ram() # default to cpu inference
    # check gpu availability
    if (vram := get_machine_spec()[2]):
        capacity = vram # gpu inference should be faster than cpu, even if vram < ram

    llm_list = get_llm_list(precision, capacity) 
    typer.echo(llm_list)


@app.command("fetch")
def fetch_new_leaderboard():
    """
    
    """
    try:
        list_to_excel()
        typer.echo("Successfully fetched from Open LLM Leaderboard.")
    except Exception as e:
        typer.echo(f"Error fetching from Open LLM Leaderboard: {e}")
        logging.error(e)