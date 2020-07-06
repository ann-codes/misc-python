

# Data -------- Ordered - Mutable	- Constructor --- Example
# List	        Yes	      Yes	      [ ] or list()	  [5.7, 4, 'yes', 5.7]
# Tuple	        Yes	      No	      ( ) or tuple()	(5.7, 4, 'yes', 5.7)
# Set	          No	      Yes	      {}* or set()	  {5.7, 4, 'yes'}
# Dictionary	  No	      No**	    { } or dict()	  {'Jun': 75, 'Jul': 89}

# multiple assignments w/ multiple values
size, color, quirk = "skinny", "chocolate", "pukes a lot"
print(size, color, quirk) # skinny chocolate pukes a lot

# multiple assignments
cat = ["hairy", "Zues", "unknown"]
hair_length, name, age = cat
print(hair_length, name, age) ## hairy Zues unknown

# augmented operators (works similarly to JS)
answer = 42
answer = answer + 1
# is same as 
answer += 1
# note: it does not have ++ or --
print(answer) # 44


# note: python is particular about lists, excep for when you indent inside lists/dicts or if you use "+ \ in order to separate lines inside strings"
print("itsy bitsy spider" + \
      "went up a water spout")