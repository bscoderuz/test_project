import re
from collections import Counter

def analyze_apache_logs(log_file):
    ip_addresses = []
    requests = []
    errors = []

    with open(log_file, 'r') as file:
        for line in file:
            # IP manzilini izlash
            match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if match:
                ip_addresses.append(match.group(0))

            # So'rovlarni izlash
            request_match = re.search(r'\"(.+?)\"', line)
            if request_match:
                request = request_match.group(1).split()[1]
                requests.append(request)

            # Xatolarni izlash
            error_match = re.search(r'\[(.*?)\]', line)
            if error_match:
                error = error_match.group(1)
                errors.append(error)

    # Unikal IP manzillarini aniqlash
    unique_ips = set(ip_addresses)

    # Eng ko'p uchraydigan so'rovlarni topish
    most_common_requests = Counter(requests).most_common(5)

    # Eng ko'p uchraydigan server xatolarni topish
    most_common_errors = Counter(errors).most_common(5)

    return unique_ips, most_common_requests, most_common_errors

# Log-faylni ko'rsatish
log_file_path = '../path/to/your/logfile.log'

# Log-faylni tahlil qilish
unique_ips, most_common_requests, most_common_errors = analyze_apache_logs(log_file_path)

# Natijalarni chiqarish
print("Unikal IP manzillar:")
for ip in unique_ips:
    print(ip)

print("\nEng ko'p uchraydigan so'rovlari:")
for request, count in most_common_requests:
    print(f"{request}: {count}")

print("\nEng ko'p uchraydigan server xatolari:")
for error, count in most_common_errors:
    print(f"{error}: {count}")
