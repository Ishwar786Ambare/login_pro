# d = {'a': 1, 'b': 2, 'c': 3}
# for n in d.keys():
#     print(n)
# str='ISHWAR'
# print(str)
# print(str[:3].lower()+str[3:])

# a = [i ** 2 for i in range(11)]
# print(a)

# s=input("Enter ubou:")
# print(s)
# print(len(s))

# def counter(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n]+=1
#         else:
#             dict[n]=1
#     return dict
#
# print(counter("googgle.com"))


'''
def addstring(str1):
    length = len(str1)
    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    return str1


print(addstring('ab'))
print(addstring('abcd'))
print(addstring('abcding'))

'''

'''
def char_mix_up(a, b):
    new_a=a[:2]+b[-1]
    new_b=b[:2]+a[-1]
    return new_a + "   " + new_b

print(char_mix_up('abc', 'xyz'))

'''

'''
def changr_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '@')
    str1 = char + str1[1:]
    return str1


print(changr_char("restart"))

'''

'''
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1

'''

# print(change_char('restart'))


'''
def counnt(str1):
    if len(str1) < 2:
        return "at least two"
    return str1[:2] + str1[-2:]


print(counnt('hgkz'))
'''

# def counter(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(counter("google.com"))

# print(counter('ishwar pururshottam ambare'))

# print(counter("google.com"))

# s = input("enter a string:")
# count=0
# for i in range(len(s)):
#     count+=i
# print(i)


# import textwrap

# s = input("Input a string: ")
# w = int(input("Input the width of the paragraph: ").strip())
# print(textwrap.fill(s, w))
# textwrap.fill()
# def test(str):
#     result = ""
#     for item in str:
#         if item.islower():
#             result += item.upper()
#         else:
#             result += item.lower()
#     return result
#
#
# print(test('iSJwar'))


# def swp_case(str1):
#     result = ""
#     for item in str1:
#         if item.isupper():
#             result += item.lower()
#         else:
#             result += item.upper()
#     return result
# 
# 
# print(swp_case("Ishwar"))
