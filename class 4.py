
class Visitor:
    """
    Represents a visitor with visitor ID, name, age, and nationality.
    """
    def __init__(self, visitorID=0, name="", age=0, nationality=""):
        """
        Initialize Visitor object with provided attributes.

        Args:
            visitorID (int): Unique identifier for the visitor.
            name (str): Name of the visitor.
            age (int): Age of the visitor.
            nationality (str): Nationality of the visitor.
        """
        self.visitorID = visitorID
        self.name = name
        self.age = age
        self.nationality = nationality

    # Define setter and getter methods for each attribute

