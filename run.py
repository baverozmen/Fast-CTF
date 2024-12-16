import argparse
import subprocess as sb
import os
import threading

sdor = ["sqlmap", "nmap", "dirsearch", "hydra", "nikto", "john", "hashcat"]

def tool_download():
    try:
        for ad in sdor:
            sb.check_output(f"which {ad}", shell=True)
            print(f"{ad} : Installed")
    except Exception:
        for ad in sdor:
            sb.run(f"apt-get install -y {ad}", shell=True, check=True)

def tool_start(ip_address, tools, verbose, url, username, wordlist, port_name, hash_file):
    print(f"Running tool: {tools}")

    tool_commands = {
        "nmap": f"nmap -v -A -T5 -Pn {ip_address} -oN nmap_scan",
        "dirsearch": f"dirsearch -u {ip_address} -e php,html,js,txt --threads 20",
        "hydra": f"hydra -l {username} -P {wordlist} {port_name}://{ip_address}",
        "nikto": f"nikto -h {url} -ssl -o nikto-results.txt",
        "sqlmap": f"sqlmap -u '{url}' --batch --dump",
        "john": f"john {hash_file} --wordlist={wordlist}",
        "hashcat": f"hashcat -m 0 {hash_file} {wordlist}"
    }

    if tools in tool_commands:
        os.system(tool_commands[tools])

    if verbose:
        print("Verbose mode enabled.")

def run_in_thread(ip_address, tools, verbose, url, username, wordlist, port_name, hash_file):
    """Helper function to run each tool in its own thread."""
    threading.Thread(
        target=tool_start,
        args=(ip_address, tools, verbose, url, username, wordlist, port_name, hash_file)
    ).start()

parser = argparse.ArgumentParser(description="Fast CTF Automation Tool")
parser.add_argument("-l", "--username", help="Username for Hydra", type=str)
parser.add_argument("-p", "--portname", help="Port name for Hydra (e.g., http, ssh)", type=str)
parser.add_argument("-w", "--wordlist", help="Path to the wordlist file", type=str)
parser.add_argument("-ui", "--url_ip", metavar="url_ip", help="Target IP address or URL", type=str, required=True)
parser.add_argument("-t", "--tools", metavar="tools", help="Comma-separated tools to use", type=str, required=True)
parser.add_argument("-v", "--verbose", help="Enable verbose output", action="store_true")
parser.add_argument("-s", "--skiptool", help="Skip tool downloading", action="store_true")
parser.add_argument("-hf", "--hashfile", help="Hash file for john or hashcat", type=str)

args = parser.parse_args()

tools = args.tools.split(',')

if args.skiptool:
    for tool in tools:
        run_in_thread(
            ip_address=args.url_ip,
            tools=tool,
            verbose=args.verbose,
            url=args.url_ip,
            username=args.username,
            wordlist=args.wordlist,
            port_name=args.portname,
            hash_file=args.hashfile
        )
else:
    print("Start downloading tools...")
    tool_download()

    for tool in tools:
        run_in_thread(
            ip_address=args.url_ip,
            tools=tool,
            verbose=args.verbose,
            url=args.url_ip,
            username=args.username,
            wordlist=args.wordlist,
            port_name=args.portname,
            hash_file=args.hashfile
        )
