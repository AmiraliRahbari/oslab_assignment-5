import csv

class Shop:
    def __init__(self):
        self.items = list()
        self.buy = list()


    def add_item(self):
        name = input("Enter name of item : ")
        id = input("Enter id of item : ")
        price = input("Enter price of item : ")
        self.items.append({"name": name, "id": id, "price": price})


    def show_items(self):
       for item in self.items:
            return f"name: {item['name']}\t\tid: {item['id']}\t\tprice: {item['price']}"

    def delete_item(self):
        delete_id =  input("Enter id of item that you want delete it : ")

        for item in self.items:
            if delete_id == item['id']:
                self.items.remove(item)
                print(f"item {item['name']} deleted!!!")
                return
        print("not found")


    def edit_item(self, id):
        index = 1
        for item in self.items:
            if id == item['id']:

                new_id = input("Enter new id: ")
                new_name = input("Edit item name: ")
                new_price = input("Enter new price: ")
                new_item = {"name": new_name, "id": new_id, "price": new_price}
                self.items.insert(index, new_item)
                self.delete_item(id)
                index += 1


    def search_by_name(self, name):
        for item in self.items:
            if name == item["name"]:
                print(f"item found!!!\t\tid: {item['id']}\t\tprice: {item['price']}")
                return

        print("item not found!!!")

    def buying(self):
        buy_item_name = input("Enter name of item that you want to buy : ")
        buy_item_id = input("Enter id of item that you want to buy : ")
        buy_item_price = float()

        for item in self.items:
            if buy_item_id == item['id']:
                buy_item_price = item['price']

        self.buy.append({"name": buy_item_name, "id": buy_item_id, "price": buy_item_price})

    def show_buy_items(self):
        for buy in self.buy:
            print(f"item : {buy['name']}\t\tid : {buy['id']}\t\tprice:{buy['price']}")


    def purchase(self):
        all_price = float()
        all_data = list()
        for b in self.buy:
            all_price += float(b['price'])

        result = input(f"you should pay {all_price}\nare you shore?(y/n)\t")
        if(result == 'y'):
            print("payed successfuly. have a good day.")
            for b in self.buy:
                all_data.append([b['name'], b['id'],  b['price']])

            self.save_data(all_data)



    def save_data(self, data):
        with open("data.csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerow("purchase\n")
            writer.writerow(data)
            writer.writerow([self.show_items()])




if __name__ == "__main__":
    shop = Shop()

    while(True):
        result = int(
            input("Enter a choice :\n1.add item\n2.delete item\n3.show items\n"
                  "4.add item to buy\n5.show item in your buy basket\n6.buy items in your buy basket\n7.exit\n"))
        if result == 1:
            shop.add_item()
            print("\n\n****************************\n\n")

        elif result == 2:
            shop.delete_item()
            print("\n\n****************************\n\n")

        elif result == 3:
            shop.show_items()
            print("\n\n****************************\n\n")

        elif result == 4:
            shop.buying()
            print("\n\n****************************\n\n")

        elif result == 5:
            shop.show_buy_items()
            print("\n\n****************************\n\n")

        elif result == 6:
            shop.purchase()
            print("\n\n****************************\n\n")

        elif result == 7:
            break
