import re

#******************************************************
# Find a pattern in a sentence using re
#******************************************************

# List of patterns to search for
patterns = [ 'term1', 'term2' ]

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print('Searching for "%s" in: \n"%s"' % (pattern, text),)
    
    #Check for match
    if re.search(pattern,  text):
        print ('\n')
        print ('Match was found. \n')
    else:
        print ('\n')
        print ('No Match was found.\n')

match = re.search(patterns[0], text)
print(match)
print(match.start())
print(match.end())


#******************************************************
# Split string using re
#******************************************************

# Term to split on
split_term = '@'
phrase = 'What is the domain name of someone with the email: hello@gmail.com'
# Split the phrase at the '@' sign in a list of element
print(re.split(split_term,phrase))

# Returns a list of all matches. This will find all match including the matches
print(re.findall('match','test phrase match is in middle of all possible matches'))

#******************************************************
# Repetition Syntax
#******************************************************
#Function to find what I want in a string
def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %pattern)
        print(re.findall(pattern,phrase))
        print('\n')

#here is what I am looking for
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',         # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)

#******************************************************
# Character Sets
#******************************************************
test_patterns = ['[sd]',    # either s or d
                 's[sd]+']  # s followed by one or more s or d
            
multi_re_find(test_patterns,test_phrase)

#******************************************************
# Exclusion
#******************************************************
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^!.? ]+',test_phrase)) #remove all punctuation in this sentence

#******************************************************
# Character Ranges
#******************************************************
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'
test_patterns=[ '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
print(multi_re_find(test_patterns,test_phrase))

#******************************************************
# Escape code
#******************************************************
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

# note the r before the escape code tells Python the following is a escape code

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

print(multi_re_find(test_patterns,test_phrase))


