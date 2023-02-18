my_queue = __import__('4_queue')

class Order:
    # Constructor, Time O(1), Space O(1)
    def __init__(self, id, items, price):
        self.order_id = id
        self.order_items = items
        self.order_price = price

    # Override the print format, Time O(1), Space O(1)
    def __str__(self):
        return  str(self.order_id) + " , "+ str(self.order_items)+\
             ", $"+str(self.order_price)

# Use queue to track the delivery order
if __name__ == '__main__':
    queue = my_queue.Queue()
    queue.enqueue(Order(1, "Burrito bowl", 15))
    queue.enqueue(Order(2, "Salad", 8))
    queue.enqueue(Order(3, "Veggie bowl", 7.5))
    queue.enqueue(Order(4, "Kids's Quesadilla", 5))
    while (queue.is_empty() == False):
        order = queue.dequeue()
        print("order: " + str(order))