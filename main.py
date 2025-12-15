"""
Using the tools from the src folders, we build the behavior of the
script. Now it can provide some relevant information of the log file
researching under any resultant object using the classes and they
methods.
"""

from src.log_parser import LogEntry  # This will be changed for a dynamic class

OpenFile = "assets/auth.log"  # Test file maded as probe (later will be also dynamic)
ip_frequency = {}  # Dictionary maded to count the intrust attempt for each IP

try:
    with open(OpenFile, "r") as log:
        for line in log:  # For each line on the text:

            entry = LogEntry(line)  # Using the class and saving it on a variable

            ip = entry.get_ip()  # Search for the ip on the line

            if (
                ip == "0.0.0.0" or ip == "Default" or ip == "Empty"
            ):  # In case the IP has no value, dont register it on the report
                continue

            """
            We create a histogram for each ip so we can count them
            """
            ip_frequency[ip] = ip_frequency.get(ip, 0) + 1


except FileNotFoundError:
    print("[!] The file must be in the same folder [!]")


def IpReport():  # Report of each IP intrusion attempt
    print("-" * 30)
    print("[i] IP intrution report [i]")
    print("-" * 30)
    for ip, count in ip_frequency.items():
        print(f"[+]IP:{ip} \t -> {count} attempts.")


if __name__ == "__main__":
    IpReport()
