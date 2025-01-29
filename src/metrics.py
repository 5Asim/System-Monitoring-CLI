import psutil
import logging
from datetime import datetime
from typing import Dict, Any
from pathlib import Path
from .config import MonitoringConfig

class SystemMetricsCollector:
    def __init__(self):
        self.config = MonitoringConfig.from_yaml("config.yaml")
        self._setup_logging()
        
    def _setup_logging(self):
        logging.basicConfig(
            filename=self.config.log_file,  # Use config value
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def cpu_usage(self) -> float:
        return psutil.cpu_percent(interval=1)
    
    def memory_usage(self) -> Dict[str, Any]:
        mem = psutil.virtual_memory()
        return {
            'total': mem.total,
            'available': mem.available,
            'percent': mem.percent,
            'used': mem.used,
            'free': mem.free
        }
    
    def disk_usage(self) -> Dict[str, Any]:
        disk = psutil.disk_usage('/')
        return {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
            'percent': disk.percent
        }
    
    def network_usage(self) -> Dict[str, Any]:
        net = psutil.net_io_counters()
        return {
            'bytes_sent': net.bytes_sent,
            'bytes_recv': net.bytes_recv,
            'packets_sent': net.packets_sent,
            'packets_recv': net.packets_recv
        }

    def get_system_metrics(self) -> Dict[str, Any]:
        return {
            'timestamp': datetime.now().isoformat(),
            'cpu': self.cpu_usage(),
            'memory': self.memory_usage(),
            'disk': self.disk_usage(),
            'network': self.network_usage()
        }