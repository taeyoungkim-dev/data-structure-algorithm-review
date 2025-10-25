#Lets describe 987, -123
# The concept here is saving the number's *representation* (each digit)
# instead of its *binary value*.
#zone deciaml format
zone_portion = ('','','','')
decimal_portion = ('','','','')
#987
#make 9 
zone_portion = "1111" #1111 means number
decimal_portion = "1001" # 9
_987 = list(zone_portion + decimal_portion)
#make 8
zone_portion = "1111"
decimal_portion = "1000" # 8
_987.extend(list(zone_portion + decimal_portion))
#make 7
#The zone portion of the last byte indicates 
#the number's sign: 1100 for positive and 1101 for negative
zone_portion = "1100" #positive
decimal_portion = "0111" # 7
_987.extend(list(zone_portion + decimal_portion))

print("987 in zone decimal format : " + "".join(_987))
print()

#-123
#make 1
zone_portion = "1111" 
decimal_portion = "0001" # 1
_123 = list(zone_portion + decimal_portion)
#make 2
zone_portion = "1111"
decimal_portion = "0010" # 2
_123.extend(list(zone_portion + decimal_portion))
#make 7
zone_portion = "1101" #negative
decimal_portion = "0011" # 3
_123.extend(list(zone_portion + decimal_portion))

print("123 in zone decimal format : "+"".join(_123))
print()


#pack decimal format
#pack decimal format is similar as zone but it only use pack portion only one time
pack_portion = ('','','','')
deciaml_portion = ('','','','')

#987
#9
deciaml_portion = "1001"
__987 = list(decimal_portion)
#8
decimal_portion = "1000"
__987.extend(deciaml_portion)
#7
decimal_portion = "0111"
__987.extend(deciaml_portion)

#represent 987 is positive
pack_portion = "1100"
__987.extend(pack_portion)

print("987 in pack decimal format : " + "".join(__987))
print()

#-123
#1
deciaml_portion = "0001"
__123 = list(decimal_portion)
#2
decimal_portion = "0010"
__123.extend(decimal_portion)
#3
decimal_portion = "0011"
__123.extend(decimal_portion)

#represent 123 is negative
pack_portion = "1101"
__123.extend(pack_portion)

print("-123 in pack decimal format : " + "".join(__123))
print()
