# 1. Function Example
def greet(name):
    print(f"Hello {name}! Welcome ")

# calling the function
greet("Fatima")


# 2. Local Variable
def show_number():
    num = 50
    print(num)

show_number()

def show_number2():
    num = 100
    print(num)




show_number2()


# 3. Global Variable
x = "Pakistan"

def display_country():
    print(x)

display_country()

def change_country():
    global x
    x = "Canada"

change_country()
print(x)


# 4. Mutable Example (List)
def add_color(colors):
    colors.append("Blue")

my_colors = ["Red", "Green"]
add_color(my_colors)
print(my_colors)

def add_number(nums):
    nums.append(10)

numbers = [1, 2]
add_number(numbers)
print(numbers)


# 5. Immutable Example (String)
def change_text(text):
    text = "New Text"

msg = "Old Text"
change_text(msg)
print(msg)

def change_name(name):
    name = "Ahmed"

person = "Ali"
change_name(person)
print(person)


# 6. Default Arguments

# Wrong way
def add_fruit_wrong(fruit, basket=[]):
    basket.append(fruit)
    return basket

print(add_fruit_wrong("Apple"))
print(add_fruit_wrong("Banana"))

# Correct way
def add_fruit_correct(fruit, basket=None):
    if basket is None:
        basket = []
    basket.append(fruit)
    return basket

print(add_fruit_correct("Apple"))
print(add_fruit_correct("Banana"))


# 7. Closure Example
def create_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))
print(triple(5))


# 8. Mixed Example
def process_data(name, marks):
    print(f"Student: {name}")
    print(f"Marks: {marks}")
    if marks >= 50:
        print("Status: Pass")
    else:
        print("Status: Fail")

process_data("Ali", 75)
process_data("Sara", 45)