# LAND TRADING APPLICATION
def display_details():
    print("******************************************************************")
    print("OWNER 1:")
    print("LAND OWNER ID: ", Owner1.land_owner_id)
    print("Land Owner Name: ", Owner1.land_owner_name)
    print("Land in Acres: ", Owner1.acres_of_land)
    print("Amount: ", Owner1.amount)
    print("------------------------------------------------------------------")
    print("Owner 2:")
    print("LAND OWNER ID: ", Owner2.land_owner_id)
    print("Land Owner Name: ", Owner2.land_owner_name)
    print("Land in Acres: ", Owner2.acres_of_land)
    print("Amount: ", Owner2.amount)
    print("******************************************************************")


class TradeLand:
    def __init__(self, land_owner_id=0, land_owner_name="", acres_of_land=0, amt=0):
        self.land_owner_id = land_owner_id
        self.land_owner_name = land_owner_name
        self.acres_of_land = acres_of_land
        self.amount = amt

    def get_land_owner_id(self):
        return self.land_owner_id

    def set_land_owner_id(self, land_owner_id):
        self.land_owner_id = land_owner_id

    def get_land_owner_name(self):
        return self.land_owner_name

    def set_land_owner_name(self, land_owner_name):
        self.land_owner_name = land_owner_name

    def get_acres_of_land(self):
        return self.acres_of_land

    def set_acres_of_land(self, acres):
        self.acres_of_land = acres

    def get_amount(self):
        return self.amount

    def set_amount(self, amt):
        self.amount = amt

    def sell_land_to(self, quantity_of_land, price_per_acre, selling_to):
        if self.acres_of_land < quantity_of_land:
            print("Owner Doesn't have that much Land to sell")
        elif Owner2.amount < quantity_of_land * price_per_acre:
            print("Owner Doesn't have enough money")
        else:
            self.acres_of_land -= quantity_of_land
            selling_to.acres_of_land += quantity_of_land
            self.amount += quantity_of_land * price_per_acre
            selling_to.amount -= quantity_of_land * price_per_acre
            print("After Transaction: ")
            display_details()


# driver code
if __name__ == "__main__":
    while True:
        print("For Owner 1:")
        owner_id = int(input("Enter Land Owner ID:"))
        name = input("Enter Land Owner Name:")
        land_in_acres = int(input("Enter the Land in Acres:"))
        amount = int(input("Enter Amount:"))
        Owner1 = TradeLand(owner_id, name, land_in_acres, amount)

        Owner2 = TradeLand()
        print("For Owner2:")
        Owner2.set_land_owner_id(int(input("Enter Land Owner ID:")))
        Owner2.set_land_owner_name(input("Enter Land Owner Name:"))
        Owner2.set_acres_of_land(int(input("Enter the Land in Acres:")))
        Owner2.set_amount(int(input("Enter Amount:")))

        # DETAILS BEFORE TRANSACTION
        print("Before Transaction: ")
        display_details()

        who_is_selling = int(input("who wants to sell to whom? 1 for Owner1 and 2 for owner2: "))
        how_much = int(input("How much land is being sold: "))
        price_for_each_acre = int(input("What is the price per acre: "))

        if who_is_selling == 1:
            Owner1.sell_land_to(how_much, price_for_each_acre, Owner2)
            break
        else:
            Owner2.sell_land_to(how_much, price_for_each_acre, Owner1)
            break
