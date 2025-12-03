from src.log_parser import LogEntry

objects = []

OpenFile = "assets/auth.log"

try:
    with open(OpenFile, "r") as logType:
        for line in logType:
            ObjectToAppend = LogEntry(line)
            objects.append(ObjectToAppend)
except FileNotFoundError:
    print("[!] The file must be in the same folder")

for obj in objects:
    print(f"[+] Object: {obj.get_all_attributes()}")
