# Amaan Muhammad
# PSID: 1607608

# Create class
class ItemToPurchase:
    # Default constructor
    def __init__(self):
        # Initializing variables
        # with default values
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    # print the items
    def print_item_cost(self):
        # Display the item name, quantity and price
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(
            self.item_price * self.item_quantity))

# Main
if __name__ == "__main__":
    # Print item1
    print("Item 1")

    item1 = ItemToPurchase()

    item2 = ItemToPurchase()

    # Prompt user for input on Item1
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    print("\nItem 2")

    # Prompt user for input on Item2
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")

    # Call method to print
    item1.print_item_cost()
    item2.print_item_cost()

    # Calculate the cost of items
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    # Display the total cost
    print("\nTotal: $" + str(total))
