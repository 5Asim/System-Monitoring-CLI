import psutil
from datetime import datetime
import logging
from typing import Dict, List, Any, Optional

class ProcessManager:
    @staticmethod
    def list_processes() -> List[Dict[str, Any]]:
        """List all running processes with basic information"""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return processes

    @staticmethod
    def get_process_details(pid: int) -> Optional[Dict[str, Any]]:
        """Get detailed information about a specific process"""
        try:
            process = psutil.Process(pid)
            return {
                'pid': pid,
                'name': process.name(),
                'status': process.status(),
                'cpu_percent': process.cpu_percent(),
                'memory_percent': process.memory_percent(),
                'create_time': datetime.fromtimestamp(process.create_time()).isoformat(),
                'username': process.username(),
                'cmdline': process.cmdline()
            }
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            logging.error(f"Error getting process details for PID {pid}: {str(e)}")
            return None

    @staticmethod
    def kill_process(pid: int, force: bool = False) -> bool:
        try:
                process = psutil.Process(pid)
                if force:
                        process.kill()
                else:
                        process.terminate()
                return True
        except Exception as e:
                logging.error(f"Error killing process {pid}: {str(e)}")
                return False