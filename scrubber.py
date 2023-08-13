import re

def scrub_ip_addresses(log):
    with open("scrubbed_log.txt","a") as scrubb_log:
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        for line in log:
            scrubb_log.write(re.sub(ip_pattern, 'X.X.X.X', line))
    return


with open("kubelet_service.log", "r") as log:
    scrub_ip_addresses(log)

