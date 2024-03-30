class ExhibitionLocation:
    """
    Represents a location for an exhibition with location ID, name, and type.
    """
    def __init__(self, locationID=0, name="", type=""):
        """
        Initialize ExhibitionLocation object with provided attributes.

        Args:
            locationID (int): Unique identifier for the location.
            name (str): Name of the location.
            type (str): Type of the location.
        """
        self.locationID = locationID
        self.name = name
        self.type = type

    # Define setter and getter methods for each attribute
