import typer
from rich.console import Console
from rich.panel import Panel
import time
from rich.live import Live

# Use relative imports
from .metrics import SystemMetricsCollector
from .process_manager import ProcessManager
from .dashboard import Dashboard

app = typer.Typer()
console = Console()

@app.command()
def monitor():
    """Monitor system metrics in real-time"""
    collector = SystemMetricsCollector()
    console.print("[green]Starting system monitoring...[/]")
    try:
        while True:
            metrics = collector.get_system_metrics()
            console.clear()
            console.print(Panel(
                f"""
CPU Usage: {metrics['cpu']}%
Memory: {metrics['memory']['percent']}%
Disk: {metrics['disk']['percent']}%
Network:
    Sent: {metrics['network']['bytes_sent'] / 1024:.2f} KB
    Received: {metrics['network']['bytes_recv'] / 1024:.2f} KB
                """.strip(),
                title="System Metrics",
                border_style="green"
            ))
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Monitoring stopped by user[/]")

@app.command()
def processes():
    """List all running processes"""
    process_list = ProcessManager.list_processes()
    for proc in process_list:
        console.print(f"PID: {proc['pid']} - Name: {proc['name']} - User: {proc['username']}")

@app.command()
def process_info(pid: int):
    """Get detailed information about a specific process"""
    details = ProcessManager.get_process_details(pid)
    if details:
        console.print(Panel.fit(
            "\n".join(f"{k}: {v}" for k, v in details.items()),
            title=f"Process Details (PID: {pid})"
        ))
    else:
        console.print(f"[red]Process with PID {pid} not found[/]")

@app.command()
def kill(pid: int, force: bool = False):
    """Kill a process by PID"""
    if not force:
        confirm = typer.confirm(f"Really kill process {pid}?")
        if not confirm:
            raise typer.Abort()
    
    if ProcessManager.kill_process(pid, force):
        console.print(f"[green]Process {pid} terminated successfully[/]")
    else:
        console.print(f"[red]Failed to terminate process {pid}[/]")



# Add this new command
@app.command()
def dashboard():
    """Launch the rich terminal dashboard"""
    collector = SystemMetricsCollector()
    dashboard = Dashboard(collector)
    console = Console()
    
    try:
        with Live(console=console, screen=True, refresh_per_second=4) as live:
            while True:
                live.update(dashboard.generate_layout())
                time.sleep(0.5)  # Refresh rate
    except KeyboardInterrupt:
        console.print("\n[yellow]Dashboard closed[/]")

if __name__ == "__main__":
    app()