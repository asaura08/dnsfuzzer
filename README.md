# DNS Subdomain Discovery Tool

This is a simple Python script for DNS subdomain discovery. It enumerates subdomains of a given domain using a wordlist file and DNS resolution.

## Features

- Multi-threaded DNS resolution for faster discovery.
- Customizable DNS resolver.
- Utilizes a wordlist file to discover subdomains.
- Timeout value for DNS resolution.

## Requirements

- Python 3.x
- `argparse`, `argcomplete`, `tqdm`, and `colorama` Python libraries. You can install them using pip:

```bash
pip install argparse argcomplete tqdm colorama
```

## Usage

```bash
python dnsfuzzer.py -d <domain> -w <wordlist> [-r <resolver>] [-t <threads>] [-T <timeout>]
```

### Options

- `-d`, `--domain`: Domain to enumerate subdomains of (required).
- `-w`, `--wordlist`: Wordlist file to use for subdomain discovery (required).
- `-r`, `--resolver`: IP address of a DNS resolver to use (optional).
- `-t`, `--threads`: Number of threads for concurrent resolution (default=50).
- `-T`, `--timeout`: Timeout value for DNS resolution (default=5).

## Example

```bash
python dnsfuzzer.py -d example.com -w wordlist.txt -r 8.8.8.8 -t 20 -T 3
```

This will enumerate subdomains of `example.com` using the wordlist in `wordlist.txt` file, utilizing `8.8.8.8` as the DNS resolver with 20 threads for concurrent resolution and a timeout of 3 seconds.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
