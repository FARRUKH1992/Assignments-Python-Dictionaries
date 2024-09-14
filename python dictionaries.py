# Initial menu
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
# adding categories updating steak price removing brushcetta

# Add a new category called "Beverages" with at least two items
restaurant_menu["Beverages"] = {"Soda": 2.49, "Coffee": 3.99}

# Update the price of "Steak" to 17.99
restaurant_menu["Main Course"]["Steak"] = 17.99

# Remove "Bruschetta" from "Starters"
del restaurant_menu["Starters"]["Bruschetta"]

# Print the updated menu to verify changes
print(restaurant_menu)



# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.



service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Function to open a new service ticket
def open_ticket(ticket_id, customer_name, issue_description):
    if ticket_id in service_tickets:
        print(f"Ticket ID {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {
            "Customer": customer_name,
            "Issue": issue_description,
            "Status": "open"
        }
        print(f"Ticket {ticket_id} opened for {customer_name}.")

# Function to update the status of an existing ticket
def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        if new_status in ["open", "closed"]:
            service_tickets[ticket_id]["Status"] = new_status
            print(f"Ticket {ticket_id} status updated to {new_status}.")
        else:
            print("Invalid status. Please use 'open' or 'closed'.")
    else:
        print(f"Ticket ID {ticket_id} does not exist.")

# Function to display all tickets or filter by status
def display_tickets(status_filter=None):
    for ticket_id, ticket_info in service_tickets.items():
        if status_filter is None or ticket_info["Status"] == status_filter:
            print(f"ID: {ticket_id}")
            print(f"  Customer: {ticket_info['Customer']}")
            print(f"  Issue: {ticket_info['Issue']}")
            print(f"  Status: {ticket_info['Status']}")
            print()

# Test the functions
print("Initial tickets:")
display_tickets()

print("Opening a new ticket...")
open_ticket("Ticket003", "Charlie", "Feature request")

print("Updating ticket status...")
update_ticket_status("Ticket001", "closed")

print("Displaying all tickets after updates:")
display_tickets()

print("Displaying only 'closed' tickets:")
display_tickets("closed")
