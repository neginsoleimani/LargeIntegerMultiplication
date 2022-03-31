# Large Integer Multiplication
# Negin Soleimani
# https://github.com/neginsoleimani

# Functions used in this algorithm
# ord(character)



# Multiplies str1 and str2, and prints result.
def multiply(num1, num2):
    len1 = len(num1)
    len2 = len(num2)
    if len1 == 0 or len2 == 0:
        return "0"
 
    # will keep the result number in vector
    # in reverse order
    result = [0] * (len1 + len2)
     
    # Below two indexes are used to
    # find positions in result.
    i_n1 = 0
    i_n2 = 0
 
    # Go from right to left in num1
    for i in range(len1 - 1, -1, -1):
        carry = 0
        n1 = ord(num1[i]) - 48
 
        # To shift position to left after every
        # multiplication of a digit in num2
        i_n2 = 0
 
        # Go from right to left in num2
        for j in range(len2 - 1, -1, -1):
             
            # Take current digit of second number
            n2 = ord(num2[j]) - 48
         
            # Multiply with current digit of first number
            # and add result to previously stored result
            # at current position.
            summ = n1 * n2 + result[i_n1 + i_n2] + carry
 
            # Carry for next iteration
            carry = summ // 10
 
            # Store result
            result[i_n1 + i_n2] = summ % 10
 
            i_n2 += 1
 
            # store carry in next cell
        if (carry > 0):
            result[i_n1 + i_n2] += carry
 
            # To shift position to left after every
            # multiplication of a digit in num1.
        i_n1 += 1
         
        # print(result)
 
    # ignore '0's from the right
    i = len(result) - 1
    while (i >= 0 and result[i] == 0):
        i -= 1
 
    # If all were '0's - means either both or
    # one of num1 or num2 were '0'
    if (i == -1):
        return "0"
 
    # generate the result string
    s = ""
    while (i >= 0):
        s += chr(result[i] + 48)
        i -= 1
 
    return s
 
# Driver code
str1 = "1235421415454545454545454544"
str2 = "1714546546546545454544548544544545"
 
if((str1[0] == '-' or str2[0] == '-') and
   (str1[0] != '-' or str2[0] != '-')):
    print("-", end = '')
 
 
if(str1[0] == '-' and str2[0] != '-'):
    str1 = str1[1:]
elif(str1[0] != '-' and str2[0] == '-'):
    str2 = str2[1:]
elif(str1[0] == '-' and str2[0] == '-'):
    str1 = str1[1:]
    str2 = str2[1:]
print(multiply(str1, str2))