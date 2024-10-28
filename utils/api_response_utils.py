# api_response_utils.py

from rich import print as rprint
from rich.panel import Panel
from rich.json import JSON
from rich.table import Table
import traceback
import json


def beautify_response(api_response):
    rprint(f"[bold green]Status Code:[/bold green] {api_response.status_code}")
    rprint("\n[bold cyan]Headers:[/bold cyan]")
    rprint(api_response.headers)
    
    rprint("\n[bold cyan]Data:[/bold cyan]")
    if api_response.data:
        try:
            data_json = json.loads(api_response.data.to_json())
            rprint(JSON(json.dumps(data_json, indent=2)))
        except (TypeError, ValueError):
            rprint(api_response.data)
    else:
        rprint("No data available")

    rprint("\n[bold cyan]Raw Data (if JSON):[/bold cyan]")
    try:
        raw_json = json.loads(api_response.raw_data)
        rprint(JSON(json.dumps(raw_json, indent=2)))
    except (TypeError, ValueError):
        rprint(api_response.raw_data)



def handle_exception(e):
    # Display the main exception message
    rprint(Panel(f"[bold red]Exception Occurred:[/bold red] {e}", title="Error"))

    # Display HTTP status
    rprint(Panel(f"[bold cyan]HTTP Status Code:[/bold cyan] {e.status}", title="Status"))

    headers_dict=dict(e)
    headers_json=json.dumps(headers_dict, indent=2)
    rprint(headers_json)

    # Display headers in a table format for clarity
    headers_table = Table(title="HTTP Headers", show_header=True, header_style="bold magenta")
    headers_table.add_column("Header", style="cyan")
    headers_table.add_column("Value", style="green")
    for header, value in e.headers.items():
        headers_table.add_row(header, value)
    rprint(headers_table)

    # Display the full traceback for deeper debugging
    rprint(Panel("[bold cyan]Traceback:[/bold cyan]"))
    rprint(traceback.format_exc())