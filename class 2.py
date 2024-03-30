class Ticket:
    """
    Represents a ticket with ticket ID, price, type, and availability.
    """
    def __init__(self, ticketID=0, price=0.0, ticket_type="", availability=False):
        """
        Initialize Ticket object with provided attributes.

        Args:
            ticketID (int): Unique identifier for the ticket.
            price (float): Price of the ticket.
            ticket_type (str): Type of the ticket.
            availability (bool): Availability status of the ticket.
        """
        self.ticketID = ticketID
        self.price = price
        self.ticket_type = ticket_type
        self.availability = availability

    # Define setter and getter methods for each attribute
