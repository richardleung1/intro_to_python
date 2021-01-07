# comment

"""Welcome to Python"""

"""Data Types"""
name = 'Richard'
age = 5
is_old = False
sei_1019 = True

print(name)

"""String Methods"""
sentence = 'Today is Nicole birthday'

nicole_birthday = sentence.split(' ')

new_sentence = ' '.join(nicole_birthday)

# find index
print(new_sentence.index('N'))

# Upper and lower case
name.upper()
name.lower()

# replace
day_sentence = sentence.replace('birthday', 'Day')
print(day_sentence)

# in keyword
is_day = 'Day' in day_sentence
print(is_day)

# ranges
"""
str[index] choose one letter at index
str[-index] choose letter at index counting backwards from the end.
str[start:end] get a range of letters from a start to end.
str[start:end:step] get a range of letters taking step sized steps between.
str[:end] omit the start index and grab letters from zero up to end.
str[start:] omit the end index and grab letters from start up to the end of the string.
str[::-1] reverses a string by going backwards with a step of -1 from start to end.
"""
last_letter = day_sentence[-1]
nicole_range = day_sentence[9:15]
print(day_sentence[15])
print(nicole_range)

# length
print(len(nicole_range))

equal_to = 5 == 5
not_equal = 5 != 5

not True
not False

true_story = 5 <= 5
this_should_be_true = 6 >= 5

print(9 < 30)
print('Richard' == 'richard' or 'Richard' == 'Richard')
print('Richard' == 'richard' and 'Richard' == 'richard')

print('' or 'Richard')
print(0 or 5)

print(5 < age < 6)

real_name = name or False

# list (array)
numbers = [3, 4, 5, 6]
print(len(numbers))

(numbers[1])
print(numbers[-1])
numbers[len(numbers) - 1]

five_name = [name] * 5
print(five_name)

one_through_five = list(range(5))
print(one_through_five)

for i in range(len(one_through_five)):
    num = one_through_five[i]
    print(num)

animals = ['tiger', 'bear', 'monkey', 'wolf', 'penguin']
for i in range(len(animals)):
    animal = animals[i]
    print(animal)

random_numbers = [45, 34, 9, 17]
random_numbers.sort()
print(random_numbers)

random_numbers.append(33)
print(random_numbers)

reverse_random_numbers = random_numbers[::-1]
print(reverse_random_numbers)

thirty_three = random_numbers.pop()
print(thirty_three)

random_numbers.insert(1, 77)
print(random_numbers)

print(random_numbers.count(45))

# dictionaries
car = {
    "color": "White",
    "make": "Tesla",
    "model": "S",
    "all_colors": ["Red", "White", "Black"],
    "cool": True,
    "other_products": {
        "product": "Model 3",
        "product": "Model X",
        "product": "Cybertruck"
    }
}

print(car["make"])
car["speed"] = 200
print(car)

print(car.get("color"))
print(car.items())
print(car.keys())

# type conversion
int('33')
str(33)
float(33)
bool(0)
bool(3)

# string interpolation
print('Hello my name is ' + name)
print(f"Hello my name is {name}")

phrase = 'This {} is a phrase {}'
print(phrase.format('sentence', name))
print(phrase)

# functions
def print_name(someone):
    return someone

print(print_name(name))

def old_enough(age):
    if age < 21:
        return 'Not old enough'
    elif age == 21:
        return 'You made it to adulthood'
    else:
        return 'You older, nice'

print(old_enough(21))

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

print(is_prime(3))
print(is_prime(1))
