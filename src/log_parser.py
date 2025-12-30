from abc import ABC, abstractmethod
import re


class LogEntry(ABC):
    """
    Base class designed to be the engine for research on each subclass.
    It is indispensable for any subclass derived from this class to have
    its own regexs; otherwise, the code won't work.
    """

    @property
    @abstractmethod
    def _Regexs(self):
        pass  # This will be filled by the polimorphism on each class

    def __init__(self, raw_line_text):
        self.data = {}  # Later will be filled with the data for each class
        self.__parse_the_line(  # Calling the method who fills all the data
            raw_line_text
        )

    # The main method that builds the values from the text
    def __parse_the_line(self, line):
        """
        Iterating on every regex and setting the values of the attributes to the regexs results.
        """
        for key, regex in self._Regexs.items():
            match = re.search(regex, line)
            if match:
                if (
                    match.lastindex
                ):  # We try to set only the last capture group of the regex on the value for the key
                    found_value = match.group(match.lastindex)
                else:  # In case there was no capture group but it have a match
                    found_value = match.group(0)

                self.data[key] = found_value
            else:
                # If there was no match, fill the field as empty
                self.data[key] = "Empty"

    """
    Defining the getter method, so we can obtain the data without
    leaving the encapsulated data open.
    """

    def get_value(self, key):
        return self.data.get(key)
