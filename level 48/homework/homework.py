def double_char(s):
    return "".join([i*2 for i in s])

def get_age(age):
    return int(age[0])

def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)

def check_for_factor(base, factor):
    return base % factor == 0