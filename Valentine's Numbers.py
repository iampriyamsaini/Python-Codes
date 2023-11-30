# It’s January end at the time of this writing, and Valentine’s week is coming very soon. Personally, I believe love should be celebrated every day of the year – not just on a designated date. But that’s just me.
# Mr. Mandeep Singh is 27 years old and yet he had no luck in his love life so far. He has lost all hope about this. Thinking that he will never have any love in his life he started to think about love between numbers. According to him two numbers are in love with each other if their bitwise-xor and sum are equal. For example: bitwise-xor of 160 and 75 is 235 and their sum is also 235. Hence 160 and 75 are in love with each other. On the other hand the bitwise-xor of 32 and 63 is 31 but their sum is 95. Hence 32 and 63 are not lovers.
# In this problem Mr. Mandeep Singh will ask you question. In each question he will give you a numbers X and Y. Your task is to find out numbers are in love or not(Valentine or not). If any of the answer doesn’t exist simply print None.
# Note: for bitwise-xor python use ^ symbol
# Input Format:
# two integers in separate lines

# Output Format:

# Sample Input 0
# 160
# 75
# Sample Output 0
# 'Valentine Match'

# Sample Input 1
# 56
# 87
# Sample Output 1
# None

# Sample Input 2
# 27
# 64
# Sample Output 2
# 'Valentine Match'


a=eval(input())
b=eval(input())
if (a^b==a+b):
    print("'Valentine Match'")
else:
    print("None")








