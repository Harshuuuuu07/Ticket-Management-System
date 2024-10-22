import random
from collections import deque


class Ticket:
    def __init__(self, ticket_type, price, quantity):
        self.ticket_type = ticket_type  # Type of ticket (e.g., VIP, Regular, General)
        self.price = price  # Price of the ticket
        self.quantity = quantity  # Number of available tickets

    def __str__(self):
        return f"Type: {self.ticket_type}, Price: {self.price}, Quantity: {self.quantity}"


class TicketManagementSystem:
    def __init__(self):
        self.ticket_types = []
        self.request_queue = deque()

    # Add a new ticket type
    def add_ticket_type(self, ticket_type, price, quantity):
        ticket = Ticket(ticket_type, price, quantity)
        self.ticket_types.append(ticket)
        print(f"Ticket type {ticket_type} added with {quantity} tickets.")

    def request_ticket(self, person_name, requested_type, requested_quantity):
        self.request_queue.append((person_name, requested_type, requested_quantity))
        print(f"{person_name} requested {requested_quantity} tickets of type {requested_type}.")

    def allocate_tickets(self):
        while self.request_queue:
            person_name, requested_type, requested_quantity = self.request_queue.popleft()

            available_tickets = [ticket for ticket in self.ticket_types if
                                 ticket.ticket_type == requested_type and ticket.quantity >= requested_quantity]

            if not available_tickets:
                print(f"Sorry, {person_name}. Requested {requested_quantity} tickets of type {requested_type} are not available.")
                continue

            allocated_ticket = random.choice(available_tickets)

            allocated_ticket.quantity -= requested_quantity
            print(f"Allocated {requested_quantity} {requested_type} tickets to {person_name}. {allocated_ticket.quantity} remaining.")

    def display_available_tickets(self):
        print("Available Tickets:")
        for ticket in self.ticket_types:
            print(ticket)


ticket_system = TicketManagementSystem()

# Adding different ticket types
ticket_system.add_ticket_type("VIP", 200, 10)  # 10 VIP tickets available
ticket_system.add_ticket_type("Regular", 100, 50)  # 50 Regular tickets available
ticket_system.add_ticket_type("General", 50, 100)  # 100 General tickets available

ticket_system.display_available_tickets()

ticket_system.request_ticket("Harsh", "VIP", 2)  # Alice requests 2 VIP tickets
ticket_system.request_ticket("Gagan", "General", 5)  # Bob requests 5 General tickets
ticket_system.request_ticket("Prince", "Regular", 20)  # Charlie requests 20 Regular tickets
ticket_system.request_ticket("lakshya", "VIP", 12)  # Dave requests 12 VIP tickets (which will exceed available tickets)

ticket_system.allocate_tickets()
ticket_system.display_available_tickets()
