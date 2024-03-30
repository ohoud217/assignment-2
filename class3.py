
class Exhibition:
    """
    Represents an exhibition with name, start date, end date, and location.
    """
    def __init__(self, name="", start_date=None, end_date=None, location=""):
        """
        Initialize Exhibition object with provided attributes.

        Args:
            name (str): Name of the exhibition.
            start_date (Date): Start date of the exhibition.
            end_date (Date): End date of the exhibition.
            location (str): Location of the exhibition.
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

    # Define setter and getter methods for each attribute
