# Amaan Muhammad
# PSID: 1607608

import csv
from datetime import datetime


class OutputInventory:
    # Class for methods used to create output inventory files from provided input
    def __init__(self, item_list):
        self.item_list = item_list

    def fullinventory(self):
        # Create a csv file that outputs the full inventory
        # Each row should contain item ID,
        # manufacturer name, item type, price, service date, and list if it is damaged. The item
        # attributes must appear in this order.
        with open('./FullInventory.csv', 'w') as file:
            items = self.item_list
            # get order of keys to write to file based on manufacturer
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))

    def inventory_by_type(self):
        # Create a csv file that outputs the items based on type
        # there should be a file for each item
        # type and the item type needs to be in the file name. Each row of the file should contain
        # item ID, manufacturer name, price, service date, and list if it is damaged. The items
        # should be sorted by their item ID.
        items = self.item_list
        types = []
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open('./' + file_name, 'w') as file:
                for item in keys:
                    id = item
                    man_name = items[item]['manufacturer']
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']
                    if type == item_type:
                        file.write('{},{},{},{},{}\n'.format(id, man_name, price, service_date, damaged))

    def past_service_inventory(self):
        # Create a csv file that outputs the items which are past their service date
        # all the items that are past the service date on the day
        # the program is actually executed. Each row should contain: item ID, manufacturer
        # name, item type, price, service date, and list if it is damaged. The items must appear in
        # the order of service date from oldest to most recent.
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date(),
                      reverse=True)
        with open('./PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                expired = service_expiration < today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))

    def damaged_inventory(self):
        # Create a csv file that outputs all damaged items
        # all items that are damaged. Each row should contain : item ID,
        # manufacturer name, item type, price, and service date. The items must appear in the
        # order of most expensive to least expensive.
        items = self.item_list
        # Get order of keys to write to file based on price
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('./DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date))

if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = man_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    inventory = OutputInventory(items)
    # Create all the output files
    # Calling each function to run
    inventory.fullinventory()
    inventory.inventory_by_type()
    inventory.past_service_inventory()
    inventory.damaged_inventory()

    # Get the different manufacturers and types in a list
    types = []
    manufacturers = []
    for item in items:
        checked_manufacturer = items[item]['manufacturer']
        checked_type = items[item]['item_type']
        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)
        if checked_type not in types:
            types.append(checked_type)