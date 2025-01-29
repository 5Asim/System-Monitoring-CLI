# System Performance Monitor

A Python-based system monitoring tool that provides real-time insights into system performance metrics and process management.

## Features

- **Real-time System Monitoring**
  - CPU usage tracking
  - Memory utilization
  - Disk usage statistics
  - Network traffic monitoring

- **Process Management**
  - List all running processes
  - Detailed process information
  - Process termination capabilities
  - Resource usage by process

- **Interactive CLI**
  - Rich text interface
  - Real-time updates
  - Easy-to-use commands
  - Colorized output

## Prerequisites

- Python 3.7 or higher
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/5Asim/System-Monitoring-CLI
cd System-Monitoring-CLI
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

The tool provides several commands through its CLI interface:

### Monitor System Metrics
```bash
python src/cli.py monitor
```
Shows real-time system metrics including CPU, memory, disk, and network usage.

### List All Processes
```bash
python src/cli.py processes
```
Displays a list of all running processes with basic information.

### Get Process Details
```bash
python src/cli.py process-info <PID>
```
Shows detailed information about a specific process.

### Terminate a Process
```bash
python src/cli.py kill <PID>
```
Terminates a specific process. Use with caution.

### Help
```bash
python src/cli.py --help
```
Shows all available commands and their usage.

## Project Structure
```
System-Monitoring-CLI/
├── requirements.txt
├── README.md
└── src/
    ├── __init__.py
    ├── metrics.py         # System metrics collection
    ├── process_manager.py # Process management functionality
    └── cli.py            # Command line interface
```

## Metrics Collected

- **CPU**: Usage percentage
- **Memory**: 
  - Total memory
  - Used memory
  - Available memory
  - Usage percentage
- **Disk**:
  - Total space
  - Used space
  - Free space
  - Usage percentage
- **Network**:
  - Bytes sent
  - Bytes received
  - Packets sent
  - Packets received

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- Web interface for monitoring
- Historical data tracking and graphs
- Alert system for metric thresholds
- Export capabilities for metrics data
- System resource predictions
- Docker container monitoring
- Custom plugin support

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [psutil](https://github.com/giampaolo/psutil)
- CLI interface powered by [Typer](https://typer.tiangolo.com/)
- Terminal UI enhanced by [Rich](https://github.com/Textualize/rich)

## Author

Your Name
- GitHub: [@5Asim](https://github.com/5Asim)
- Email: ashim.shrestha.55@gmail.com