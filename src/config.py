from dataclasses import dataclass
from typing import Dict, Optional
import yaml
from pathlib import Path

@dataclass
class MonitoringConfig:
    cpu_threshold: float = 80.0
    memory_threshold: float = 80.0
    disk_threshold: float = 80.0
    network_threshold: float = 1000000
    monitoring_interval: int = 5
    log_file: str = 'monitor.log'
    alert_email: Optional[str] = None
    dashboard_refresh_rate: int = 2

    @classmethod
    def from_yaml(cls, file_path: str = "config.yaml") -> 'MonitoringConfig':
        abs_path = Path(__file__).parent.parent / file_path  # Proper path resolution
        if not abs_path.exists():
            return cls()
        with open(abs_path, 'r') as f:
            config_dict = yaml.safe_load(f)
        return cls(**config_dict)