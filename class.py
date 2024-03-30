class Artwork:
    """
    Represents an artwork with title, artist, date created, and significance.
    """
    def __init__(self, title="", artist="", date_created=None, significance=""):
        """
        Initialize Artwork object with provided attributes.

        Args:
            title (str): Title of the artwork.
            artist (str): Artist of the artwork.
            date_created (Date): Date when the artwork was created.
            significance (str): Significance of the artwork.
        """
        self.title = title
        self.artist = artist
        self.date_created = date_created
        self.significance = significance

    def setTitle(self, title):
        """
        Set the title of the artwork.

        Args:
            title (str): Title of the artwork.
        """
        self.title = title

    def getTitle(self):
        """
        Get the title of the artwork.

        Returns:
            str: Title of the artwork.
        """
        return self.title

    # Similar setter and getter methods for other attributes
