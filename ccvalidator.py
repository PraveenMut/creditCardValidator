def validator(n):
  cc_n = []   # credit card number splitted into list for easier operations on ints
  count = 0   # counter that increments to determine true index of list
  if isinstance(n, int):
    n = str(n)
  if len(n) < 16:     # immediately reject non-conforming visa/mastercards
    return "Invalid Credit Card Number"
  for e in n:
    cc_n.append(e)
  cc_n = list(map(lambda e: int(e), cc_n))
  odd = cc_n[-1::-2]
  even = cc_n[-2::-2]
  for i in even:
    t = i * 2        # temp store var to be replaced with the doubled value in even list 
    if t > 9:
      even[count] = t - 9
      count += 1
    else:
      even[count] = t
      count += 1
  if (sum(even) + sum(odd)) % 10 == 0:
    return "Valid Credit Card Number"
  else:
    return "Invalid Credit Card Number"

print validator('5456091364750692')