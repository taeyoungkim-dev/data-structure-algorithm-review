#From decimal to binary
def decimal_to_binary(decimal):
    temp = ""
    while decimal!=1 :
        temp += str(decimal%2)
        decimal = decimal//2
    temp += "1"
    return temp[::-1]

#reversing bits
def bit_reverse(bits):
    for x in range(len(bits)) :
        if  bits[x] == '0' :
            bits = bits[:x] + '1' + bits[x+1:]
        else :
            bits = bits[:x] + '0' + bits[x+1:]
    return bits

#binary +1
def binary_add_one(binary_string):
    decimal_value = int(binary_string, 2)
    decimal_value += 1
    new_binary = bin(decimal_value)
    new_binary = new_binary[2:]
    return new_binary.zfill(8)

#Represent 101, -123 by binary(char)

#Sign-magnitude format
#Fixed first bit to represent positive or negative

#101
#represent positive
_101 = "0"
temp = decimal_to_binary(101)
_101 = _101 + "0"*(7-len(temp))
_101 += temp
print("101 with Sign-magnitude format : "+_101)
print()

#-123
#represent negative
_123 = "1"
temp = decimal_to_binary(123)
_123 = _123 + "0"*(7-len(temp))
_123 += temp
print("-123 with Sign-magnitude format : "+_123)
print()

#One's complement format
#Reversing all bits is negative

#101
__101 = decimal_to_binary(101)
__101 = "0"*(8-len(__101)) + __101
print("101 with One's complement format : "+__101)
print()

#-123
__123 = decimal_to_binary(123)
__123 = "0"*(8-len(__123)) + __123
#Represent negative by reversing
__123 = bit_reverse(__123)
print("-123 with One's complement format : "+__123)
print()

#Two's complement format
#Reversing all bits and +1 is negative

#101
___101 = decimal_to_binary(101)
___101 = "0"*(8-len(___101)) + ___101
print("101 with Two's complement format : "+___101)
print()

#-123
___123 = decimal_to_binary(123)
___123 = "0"*(8-len(___123)) + ___123
#Represent negative by reversing and +1
___123 = bit_reverse(___123)
___123 = binary_add_one(___123)
print("-123 with Two's complement format : "+___123)
print()

