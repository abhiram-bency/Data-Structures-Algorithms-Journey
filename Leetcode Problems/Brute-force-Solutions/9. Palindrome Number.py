def palindrome_number(n):
    original = n
    if n<0:
        return False
    ans=0
    while n!=0:
        rem = n%10
        ans = ans*10+rem
        n=n//10
    if original == ans:
        return True
    else:
        return False
n=121
palindrome_number(n)
if n:
    print("palindrome")
else:
    print("no")