import re


class LogEntry:  # The father class maded to search for every important data on the file.

    _Regexs = {}  # This will be filled by the polimorphism on each class

    def __init__(self, raw_line_text):
        # In case the parser failes, getting the default settings:
        self._Date = "Jan 01 00:01:01"
        self._User = "Default"
        self._Status = "No-status"
        self._Ip = "0.0.0.0"
        self._Port = "0"
        self._Service = "No reachable"
        # Calling the method who fills all the data
        self.__parse_the_line(raw_line_text)

    # The main method that builds the values from the text
    def __parse_the_line(self, line):
        """
        Iterating on every attribute and changing the default values for the regexs results
        """
        for key, regex in self._Regexs.items():
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

    """
    Defining the getter methods, so we can obtain the data without
    leaving the encapsulated data open.
    """

    # Get the date.
    def get_date(self):
        return self._Date

    # Get the user.
    def get_user(self):
        return self._User

    # Get the status.
    def get_status(self):
        return self._Status

    # Get the ip.
    def get_ip(self):
        return self._Ip

    # Get the port.
    def get_port(self):
        return self._Port

    # Get the service.
    def get_service(self):
        return self._Service

    # Get all attributes
    def get_all_attributes(self):
        return (
            self._Logn,
            self._Date,
            self._User,
            self._Status,
            self._Ip,
            self._Port,
            self._Service,
        )
