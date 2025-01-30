import subprocess

# Your target
target = 'example.com'

def bug_hunter(comm):
    try:
        result = subprocess.run(comm, shell=True, capture_output=True, text=True)
        return result.stdout.strip() if result.stdout else result.stderr.strip()
    except Exception as e:
        return f'Error: {e}'

def main():
    # wafw00f -> check if your target is behind Cloudflare
    print('[*] wafw00f processing...')
    waf_w00f = bug_hunter(f'wafw00f {target}')
    print(waf_w00f)

    # ping -> wait for ICMP response from the target.
    print('[*] Running ping...')
    ping = bug_hunter(f"ping -c 4 {target}")
    print(ping)

    # nslookup -> Get DNS information
    print('[*] Running nslookup...')
    nslook = bug_hunter(f'nslookup {target}')
    print(nslook)

    # dig -> More DNS details
    print('[*] Running dig...')
    dig = bug_hunter(f'dig {target}')
    print(dig)

    # Run an Nmap scan
    print("\n[*] Running Nmap scan...")
    nmap_output = bug_hunter(f"nmap -Pn -sC -sV {target}")
    print(nmap_output)

if __name__ == "__main__":
    main()
