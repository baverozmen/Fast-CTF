# Fast CTF Automation Tool

## Description

Fast CTF is a Python-based tool designed for Capture The Flag (CTF) competitions and penetration testing tasks. It automates the execution of popular security tools, reducing setup time and enabling faster results. The script also handles the downloading and installation of required tools when needed.

## Tools Supported

- **sqlmap**: Automated SQL injection tool.
- **nmap**: Network scanner for discovering hosts and services.
- **dirsearch**: Web directory brute-forcing tool.
- **hydra**: Password-cracking tool supporting multiple protocols.
- **nikto**: Web server vulnerability scanner.
- **john**: Password cracker for hash files.
- **hashcat**: Advanced password recovery tool for hashes.

---

## Features

- **Tool Installation**: Automatically checks and installs missing tools.
- **Multi-Threading**: Executes tools in separate threads for efficiency.
- **Customizable Parameters**: Supports various arguments for user-defined configurations.
- **Verbose Mode**: Enables detailed output for debugging.
- **Hash Cracking**: Includes support for `john` and `hashcat` with hash file input.

---

## Requirements

- Python 3.6 or higher
- Root privileges for installing and running tools
- Ensure the following tools are installed or installable via `apt-get`:
  - sqlmap
  - nmap
  - dirsearch
  - hydra
  - nikto
  - john
  - hashcat

---

## Installation

1. Save the script as `run.py`.
2. Grant execution permission to the script:
   ```bash
   chmod +x run.py
   ```

   ```bash
   python3 setup.py sdist bdist_wheel                                      
   pip install .
   ```

3. Ensure required Python packages are installed:
   ```bash
   pip install argparse
   ```

---

## Usage

### Command-Line Arguments

| Parameter          | Description                                                   | Type   | Required |
|--------------------|---------------------------------------------------------------|--------|----------|
| `-l`, `--username` | Username for Hydra.                                           | String | No       |
| `-p`, `--portname` | Port name for Hydra (e.g., `http`, `ssh`).                    | String | No       |
| `-w`, `--wordlist` | Path to the wordlist file.                                    | String | No       |
| `-ui`, `--url_ip`  | Target IP address or URL.                                     | String | Yes      |
| `-t`, `--tools`    | Comma-separated list of tools to use.                         | String | Yes      |
| `-v`, `--verbose`  | Enables verbose output mode.                                  | Flag   | No       |
| `-s`, `--skiptool` | Skips tool installation and runs the specified tools directly.| Flag   | No       |
| `-hf`, `--hashfile`| Hash file path for use with `john` or `hashcat`.              | String | No       |

---

### Examples

#### Running `nmap` and `dirsearch` with verbose output
```bash
sudo fastctf -ui 192.168.1.1 -t nmap,dirsearch -v
```

#### Running `hydra` with a username and wordlist
```bash
sudo fastctf -ui 192.168.1.1 -t hydra -l admin -w /path/to/wordlist -p http -s
```

#### Running `sqlmap` on a URL
```bash
sudo fastctf -ui http://example.com -t sqlmap
```

#### Cracking a hash with `john`
```bash
sudo fastctf -t john -w /path/to/wordlist -hf /path/to/hashfile
```

#### Cracking a hash with `hashcat`
```bash
sudo fastctf -t hashcat -w /path/to/wordlist -hf /path/to/hashfile
```

---

## Functions

### `tool_download()`

- Checks if required tools are installed.
- Downloads and installs missing tools using `apt-get`.

### `tool_start(ip_address, tools, verbose, url, username, wordlist, port_name, hash_file)`

- Executes the selected tools with appropriate parameters.

### `run_in_thread(ip_address, tools, verbose, url, username, wordlist, port_name, hash_file)`

- Runs each tool in its own thread for concurrent execution.

---

## Notes

- Ensure all required tools are in the system's `PATH` or installable via `apt-get`.
- Use verbose mode for detailed output and debugging information.

---

## License

This project is licensed under the MIT License. For more details, refer to the `LICENSE` file.

