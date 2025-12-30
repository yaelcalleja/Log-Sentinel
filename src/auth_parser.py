"""
Class for log files such as auth.log (Linux server)
"""

import log_parser  # The father class and engine of the research for the code.


class AuthParser(log_parser.LogEntry):  # Inherated the methods from the father class

    _Regexs = {  # We only incorporate the regex because the research methods becomes from the father class.
        "_Date": r"^[A-Z]{1}[a-z]{2} \d{2} \d{2}:\d{2}:\d{2}",
        "_User": r"user ([a-z]+)|([a-z]+) from",
        "_Ip": r"((?:\d{1,3}\.){3}\d{1,3})",
        "_Port": r"port (\d+)",
        "_Service": r"([a-z]{1,6}[1-9]{1,5})$",
    }
