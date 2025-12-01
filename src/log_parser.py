import re


# A general class for the login attempt.
class LogEntry:
    # Defining the log-in class
    def __init__(self, raw_line_text):
        # In case the parser failes, default settings
        self._Logn = "Log 0"
        self._Date = "Jan 01 00:01:01"
        self._User = "Default"
        self._Status = "No-status"
        self._Ip = "0.0.0.0"
        self._Port = "0"
        self._Service = "No reachable"
        # This build the values on every field
        self.__parse_the_line(raw_line_text)

    # The main function to build the values from the text
    def __parse_the_line(self, line):
        self._Logn = "Log"
        # Dictionary to iterate for the searched value
        regexs = {
            '_Date': r'^[A-Z]{1}[a-z]{2} [0-9]{2} (?:[0-9]{2}.){2}[0-9]{2}',
            '_User': r'user ([a-z]+)|([a-z]+) from',
            '_Status': r'.( [A-Z][a-z]{1,15} [a-z]{1,})',
            '_Ip': r'(([0-9]{1,3}\.){3}[0-9]{1,3})',
            '_Port': r'port ([0-9]{1,5})',
            '_Service': r'([a-z]{1,6}[1-9]{1,5})$'
        }
        # Iterating on every attribute
        # and changing it values for the regexs search results
        for key, regex in regexs.items():
            match = re.search(regex, line)
            if match:
                # We try to get only the capture group of the regex
                try:
                    if match.group(2):
                        found_value = match.group(2)
                    elif match.group(1):
                        found_value = match.group(1)
                # If there was no capture group, then get all the line
                except IndexError:
                    found_value = match.group(0)
                setattr(self, key, found_value)
            else:
                # If there was no value, put the field as empty
                setattr(self, key, "Empty")

    # A safe way to get the attributes.

    # Get the date.
    def get_date(self):
        return self._Date

    # Get the user.
    def get_user(self):
        return self._User

    # Get the status.
    def get_status(self):
        return self._Status

    # Get the ipu.
    def get_ip(self):
        return self._Ip

    # Get the port.
    def get_port(self):
        return self._Port

    # Get the service.
    def get_service(self):
        return self._Service

    def get_all_attributes(self):
        return self._Logn, self._Date, self._User, self._Status, self._Ip, self._Port, self._Service
