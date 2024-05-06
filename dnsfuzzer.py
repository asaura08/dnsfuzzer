#!/bin/python

import os
import argparse
import argcomplete
from tqdm import tqdm
import sys
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor
import dns.resolver
import dns.exception

init(autoreset=True)

def resolve_subdomain(subdomain, domain, resolver=None):
    try:
        timeout = 5  # You can adjust this timeout value as needed

        if resolver:
            my_resolver = dns.resolver.Resolver(configure=False)
            my_resolver.nameservers = [resolver]
            my_resolver.timeout = timeout
            my_resolver.lifetime = timeout
            answer = my_resolver.resolve(f"{subdomain}.{domain}")
        else:
            answer = dns.resolver.resolve(f"{subdomain}.{domain}", lifetime=timeout)

        ip_address = answer[0]
        output = f"{Fore.GREEN}[+] Subdomain:{Style.RESET_ALL} {subdomain}.{domain} {Fore.CYAN}IP:{Style.RESET_ALL} {ip_address}"
        sys.stdout.write(output + '\n')
        return output

    except dns.exception.DNSException as dns_exception:
        error_message = f"{Fore.RED}Error resolving {subdomain}.{domain}:{Style.RESET_ALL} {dns_exception}"
        # sys.stdout.write(error_message + '\n')
        return error_message
    except Exception as e:
        error_message = f"{Fore.RED}Error resolving {subdomain}.{domain}:{Style.RESET_ALL} {e}"
        # sys.stdout.write(error_message + '\n')
        return error_message

def main(args):
    domain = args.domain
    wordlist = args.wordlist
    resolver = args.resolver
    threads = args.threads
    if not os.path.exists(wordlist):
        print(f"{Fore.RED}[-] The wordlist file {wordlist} does not exist.{Style.RESET_ALL}")
        sys.exit(1)

    with open(wordlist, 'r') as file:
        subdomains = file.readlines()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        list(tqdm(executor.map(lambda subdomain: resolve_subdomain(subdomain.strip(), domain, resolver), subdomains),
            total=len(subdomains), desc="Progress", unit=" Word", position=0, leave=True))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is a simple DNS subdomain discovery tool")
    parser.add_argument('-d', '--domain', help='Domain to enumerate subdomains of', required=True)
    parser.add_argument('-w', '--wordlist', help='Wordlist file to use for subdomain discovery', required=True)
    parser.add_argument('-r', '--resolver', help='IP address of a DNS resolver to use', required=False)
    parser.add_argument('-t', '--threads', help='Number of threads for concurrent resolution (default=10)', type=int, default=50)
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    main(args)
