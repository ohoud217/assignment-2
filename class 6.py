class Tour:
    """
    Represents a tour with tour ID, date, group size, and guide.
    """
    def __init__(self, tourID=0, date=None, group_size=0, guide=""):
        """
        Initialize Tour object with provided attributes.

        Args:
            tourID (int): Unique identifier for the tour.
            date (Date): Date of the tour.
            group_size (int): Size of the tour group.
            guide (str): Guide for the tour.
        """
        self.tourID = tourID
        self.date = date
        self.group_size = group_size
        self.guide = guide

    # Define setter and getter methods for each attribute








