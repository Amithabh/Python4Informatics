##import string
##stringIn = "string.with.punctuation!"
##out = stringIn.translate(stringIn.maketrans("",""), string.punctuation)

# Make a translation table.
# ... Map a to d, b to e, and c to f.
##dict = str.maketrans("abc", "def")
##print(dict)
##
### Translate this value.
##value = "aabbcc"
##result = value.translate(dict)
##print(result)

import string

words = "Dave, Laura, Maddy, Dave, Laura, Maddy, Dave,#$^^@! Laura, Dave";
translation = str.maketrans("","", string.punctuation);
new = words.translate(translation);
lower = new.lower();
print (lower)
