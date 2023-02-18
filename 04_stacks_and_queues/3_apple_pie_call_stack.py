# func1, Time O(1), Space O(1)
def make_pie():
    print("Bob makes a pie")
    bring_apples()
    print("Bob made an apple pie")

# func2, Time O(1), Space O(1)
def bring_apples():
    print("Jane goes to bring some apples")
    gather_apples()
    print("Jane brought back some apples")

# func3, Time O(1), Space O(1)
def gather_apples():
    print("Ben gathers apples in orchard\n")
    print("Ben gathered some apples")

# start call stack
make_pie()