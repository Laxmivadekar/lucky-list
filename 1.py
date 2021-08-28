def expanded_form(num):
    i = 10**(len(str(num))-1)
    print(i)
    ans = ''
    while num:
        if (num//i)*i != 0:
            ans += str((num//i)*i) + ' + '
        num = num % i
        i //= 10
    return ans[0:len(ans)-3]

# Test Cases

print(expanded_form(42))
# print(expanded_form(12))
# print(expanded_form(70304))