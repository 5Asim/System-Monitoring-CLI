# dashboard.py
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from datetime import datetime
from .metrics import SystemMetricsCollector
from .process_manager import ProcessManager
from rich.live import Live
import time

class Dashboard:
    def __init__(self, metrics_collector: SystemMetricsCollector):
        self.console = Console()
        self.metrics_collector = metrics_collector
        self.process_manager = ProcessManager()

    def generate_cpu_panel(self, metrics: dict) -> Panel:
        config = self.metrics_collector.config
        cpu_usage = metrics['cpu']
        border_style = "red" if cpu_usage > config.cpu_threshold else "green"
        return Panel(
            f"CPU Usage: {cpu_usage}%",
            title="CPU",
            border_style=border_style
        )

    def generate_memory_panel(self, metrics: dict) -> Panel:
        config = self.metrics_collector.config
        memory = metrics['memory']
        mem_usage = memory['percent']
        border_style = "red" if mem_usage > config.memory_threshold else "blue"
        
        content = f"""
Total: {memory['total'] / (1024**3):.2f} GB
Used: {memory['used'] / (1024**3):.2f} GB
Free: {memory['free'] / (1024**3):.2f} GB
Usage: {mem_usage}%
        """.strip()
        
        return Panel(content, title="Memory", border_style=border_style)

    def generate_process_table(self) -> Table:
        table = Table(title="Top Processes", show_header=True, header_style="bold magenta")
        table.add_column("PID", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("CPU %", justify="right")
        table.add_column("Memory %", justify="right")
        
        processes = sorted(
            self.process_manager.list_processes(),
            key=lambda x: x.get('cpu_percent', 0),
            reverse=True
        )[:5]
        
        for proc in processes:
            table.add_row(
                str(proc['pid']),
                proc['name'][:20],
                f"{proc.get('cpu_percent', 0):.1f}",
                f"{proc.get('memory_percent', 0):.1f}"
            )
        
        return table

    def generate_layout(self) -> Layout:
        metrics = self.metrics_collector.get_system_metrics()
        
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main"),
            Layout(name="footer", size=8)
        )
        
        # Header with timestamp
        layout["header"].update(
            Panel(
                f"System Monitor - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                style="bold white",
                subtitle="Press Ctrl+C to exit"
            )
        )
        
        # Main metrics panels
        main_layout = Layout()
        main_layout.split_row(
            Layout(self.generate_cpu_panel(metrics), name="cpu"),
            Layout(self.generate_memory_panel(metrics), name="memory")
        )
        layout["main"].update(main_layout)
        
        # Footer with process table
        layout["footer"].update(self.generate_process_table())
        
        return layout

def run_dashboard():
    """Run the dashboard interface"""
    collector = SystemMetricsCollector()
    dashboard = Dashboard(collector)
    console = Console()
    
    refresh_period = collector.config.dashboard_refresh_rate
    
    try:
        with Live(console=console, screen=True, refresh_per_second=4) as live:
            while True:
                live.update(dashboard.generate_layout())
                time.sleep(refresh_period)
    except KeyboardInterrupt:
        console.print("\n[yellow]Dashboard closed successfully[/]")

if __name__ == "__main__":
    run_dashboard()