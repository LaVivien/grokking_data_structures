my_array = __import__('1_array')

class Flower:
    # Constructor, Time O(1), Space O(1)
    def __init__(self, name, num, price):
        self.name = name
        self.supply = num
        self.sold = 0
        self.price = price

    # override to check equality, Time O(1), Space O(1)
    def __eq__(self, other):
        if isinstance(other, Flower):
            return other.name == self.name
        return False

    # make the object hashable when adding to set, Time O(1), Space O(1) 
    def __hash__(self):
        return hash(id(self))

    # override for sorting by name alphabetically, Time O(1), Space O(1) 
    def __gt__(self, a):
        return self.name > a.name

    # override to print item, Time O(1), Space O(1)
    def __str__(self):
        return "flower name: " + self.name + \
                ", supply: "+ str(self.supply) +\
                ", sold: " + str(self.sold) +\
                ", price: " + str(self.price)

class FlowerShopApplication:
    #constructor, Time O(1), Space O(1)
    def __init__(self, size):
        self.flower_array = my_array.Array(size)

    # add flower, Time O(1), Space O(1)
    def add_flower(self, flower):
        self.flower_array.add(flower)

    # update flower supply number, Time O(n), Space O(1)
    def update_supply(self, flower, number):
        index = self.flower_array.search(flower)
        if index < 0:
            print("cannot find flower " + flower.name)
            return
        flower = self.flower_array.get(index)
        flower.supply += number

    # update flower sold number, Time O(n), Space O(1)
    def update_sold(self, flower, number):
        index = self.flower_array.search(flower)
        if index < 0:
            print("cannot find flower " + flower.name)
            return
        flower = self.flower_array.get(index)
        sold = flower.sold
        supply = flower.supply
        if sold + number > supply:
            print("not enough '" + flower.name + "' to sell.")
            return
        flower.sold += number
        flower.supply -= number
    
    # calculate total sales, Time O(n), Space O(1)
    def sales(self):
        total = 0
        for i in range(0, self.flower_array.num_of_items()):
            x = self.flower_array.get(i)
            total += x.price* x.sold
        return total
    
    # delete, Time O(n), Space O(1)
    def delete_flower(self, flower):
        self.flower_array.delete(flower)

    # print all flowers, Time O(n), Space O(1)
    def display_all_flowers(self):
        self.flower_array.print()
        print("flowers: " + str(app.flower_array.num_of_items()))
        print()

    # remove duplicates using set, Time O(n), Space O(n)
    def remove_dup_flowers(self):
        new_set = set()
        for i in range(0, self.flower_array.num_of_items()):
            x = self.flower_array.get(i)
            new_set.add(x)
        max_size = self.flower_array.max_size
        self.flower_array = my_array.Array(max_size)
        i = 0
        for x in new_set:
            self.flower_array.add(x)
            i += 1

    # remove duplicates by calling method in Array, Time O(n^2), Space O(1)       
    def remove_dup_in_place(self) :
        self.flower_array.remove_dup_in_place()

# test
if __name__ == "__main__":
    app = FlowerShopApplication(12)
    rose = Flower("Rose", 20, 1)
    app.add_flower(rose)

    sunflower = Flower("Sunflower", 40, 1.25)
    app.add_flower(sunflower)

    daisy = Flower("Daisy", 50, 0.5)
    app.add_flower(daisy)

    tulip = Flower("Tulip", 12, 2)
    app.add_flower(tulip)

    lily = Flower("Lily", 15, 1)
    app.add_flower(lily)

    carnation = Flower("Carnation", 30, 0.25)
    app.add_flower(carnation)

    app.display_all_flowers()

    # add duplicates 
    print("add duplicates")
    app.add_flower(daisy)
    app.add_flower(sunflower)
    app.display_all_flowers()

    # remove dup by set
    print("remove duplicates")
    app.remove_dup_flowers()
    app.display_all_flowers()
    
    # update sales
    app.update_sold(sunflower, 12)
    app.update_sold(rose, 22) # not enough
    app.update_sold(lily, 3)
    print("Total sales:" + str(app.sales()))
    app.display_all_flowers()
    
    # delete
    print("delete item")
    app.delete_flower(lily)
    app.display_all_flowers()

    # update 
    print("update supply")
    app.update_supply(sunflower, 10)
    app.display_all_flowers()
