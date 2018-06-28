#ABCDE --> BADCE

def manipulateString(MyString):
    retString = ''
    i = 0
    try:
        for letter in MyString:
            if i % 2 == 0:
                retString += MyString[i + 1]
                retString += MyString[i]                
            i += 1
    except IndexError:
        retString += MyString[i] #the lenght of the str is odd, grap the last letter
    finally:
        pass
    return retString


print('The new string is %s' % manipulateString(''))            #return ''
print('The new string is %s' % manipulateString('A'))           #return 'A'
print('The new string is %s' % manipulateString('AB'))          #return 'BA'
print('The new string is %s' % manipulateString('ABC'))         #return 'BAC'
print('The new string is %s' % manipulateString('ABCDE'))       #return 'BADCE'
print('The new string is %s' % manipulateString('ABCDEF'))      #return 'BADCFE'
print('The new string is %s' % manipulateString('ABCDEFG'))     #return 'BADCFEG'

