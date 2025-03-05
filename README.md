# NetProbe

**NetProbe** is a simple yet powerful network scanning tool designed to detect open ports and identify vulnerabilities on networked devices. It helps network administrators monitor and secure their networks efficiently.

---

## Requirements

Before running **NetProbe**, you need to have **Python 3** installed on your system. 

To install Python 3, follow the instructions for your operating system:

- **Ubuntu/Debian**: `sudo apt install python3`
- **Fedora**: `sudo dnf install python3`
- **CentOS/RHEL**: `sudo yum install python3`
- **Arch Linux**: `sudo pacman -S python`

---

## Files

### 1. `port_scanner.py`
This Python script contains the core logic of the **NetProbe** tool. It scans the specified network for open ports and vulnerabilities.

### 2. `run.sh`
This is a shell script that automates running the `port_scanner.py` Python script. It provides an easy way to execute the port scanner without manually entering Python commands.

---

## How to Run NetProbe

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/NetProbe.git
   cd NetProbe
   ```
2. **Make the shell script executable**:
   ```bash
   chmod +x run
   ```
## Contributing
If you have any ideas for improvements or if you've found a bug, please open an issue or submit a pull request. Contributions are always welcome!

## License
This project is licensed under the MIT License. See the [Apache-2.0 license](LICENSE) file for more details.
