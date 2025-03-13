#Reversed sequence
def reverse_seq(n):
    return list(range(n, 0, -1))

#Rock Paper Scissors!
def rps(p1, p2):
    if p1 == p2: return "Draw!"
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        return "Player 1 won!"
    return "Player 2 won!"

#Is n divisible by x and y?
def is_divisible(n,x,y):
    if n % x != 0 or n % y != 0: return False
    return True

#def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n+1))

#Grade book
def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) // 3
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    return "F"