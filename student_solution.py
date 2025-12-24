# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1(s):
    s=input()
first, second=s.split(',')
print(len(first)>len(second))
print(first==second)
print(second in first)

# ---------- ЗАДАНИЕ 2 ----------
def task2(s):
    s=input()
stripped=s.strip()
print(stripped)
print(len(s))
print(s.count('a'))
print(s.replace('a', '@'))
print(s.istitle())


# ---------- ЗАДАНИЕ 3 ----------
def task3(s):
    s=input()
result1=s[1:-1]
print(result1)
result2=s[::2]
print(result2)
result3=s[::-1].lower()
print(result3)

# ---------- ЗАДАНИЕ 4 ----------
def task4(nums):
    numbers=list(map(int, input().split()))
print(sum(numbers))
print(min(numbers), max(numbers))


# ---------- ЗАДАНИЕ 5 ----------
def task6(s):
    s=input()
print(s.lower()==s.lower()[::-1] and ' ' not in s)

# ---------- ЗАДАНИЕ 6 ----------
def task7(n):
    s=input()
print(s.lower()==s.lower()[::-1] and ' ' not in s)
n=int(input())
h=hex(n)[2:]
print(h)
print(len(h))
print('a' in h)


# ---------- ЗАДАНИЕ 7 ----------
def task8(month_num):
    months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print(months[int(input()) - 1])
