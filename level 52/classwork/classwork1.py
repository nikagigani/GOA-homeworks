#Get the mean of an array
def get_average(marks):
    raise NotImplementedError("TODO: get_average")
def get_average(marks):
    return int(sum(marks) / len(marks))


#Keep up the hoop
def hoop_count(n):
    if n < 10: return "Keep at it until you get it"
    return "Great, now move on to tricks"

#Reversed Words
def reverse_words(s):
    return " ".join(s.split(' ')[::-1])

#Beginner Series #4 Cockroach
def cockroach_speed(s):
    return int(s*27.777778)

#Switch it Up!
def switch_it_up(number):
    res = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return res[number]

#Function 2 - squaring an argument
def square(n):
    return n*n

#Removing Elements
def remove_every_other(my_list):
    return my_list[::2]
def remove_every_other(my_list):
    new_list = []

    for i in range(len(my_list)):
        if i%2 == 0: new_list.append(my_list[i])

    return new_list

#Twice as old
def twice_as_old(dad_years_old, son_years_old):
    res = (dad_years_old - 2 * son_years_old)

    if res < 0: return res*-1
    return res

#All Star Code Challenge #18
def str_count(strng, letter):
    return strng.count(letter)

#is it even?
def is_even(n): 
    return n % 2 == 0

#
def move(position, roll):
    return position + roll*2

#
def get_planet_name(id):
    if id == 1: return "Mercury"
    elif id == 2: return "Venus"
    elif id == 3: return "Earth"
    elif id == 4: return "Mars"
    elif id == 5: return "Jupiter"
    elif id == 6: return "Saturn"
    elif id == 7: return "Uranus"
    elif id == 8: return "Neptune"

#
def enough(cap, on, wait):
    available = cap - on
    
    if available >= wait: return 0
    return wait - available

#
def between(a,b):
    return list(range(a, b+1))

#
def is_uppercase(inp):
    return inp == inp.upper()

#
def say_hello(name):
    return f"Hello, {name}"

#
def monkey_count(n):
    return list(range(1, n+1))

#
def powers_of_two(n):
    return [2**i for i in range(n+1)]

#
def human_years_cat_years_dog_years(human_years):
    cat_years = 15 + (human_years > 1) * 9 + max(0, human_years - 2) * 4
    dog_years = 15 + (human_years > 1) * 9 + max(0, human_years - 2) * 5
    return [human_years, cat_years, dog_years]