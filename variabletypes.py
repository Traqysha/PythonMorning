# Local variable
def car():
    x = "volvo"
    print(x)

car()

# Global variable
y = "Phone"

def device():
    global y
    print(y)

device()