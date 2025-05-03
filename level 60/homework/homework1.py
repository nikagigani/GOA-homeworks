def mouth_size(animal):
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"

def nth_even(n):
    return (n - 1) * 2

def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)

def unusual_five():
    return len("world")

def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()]
