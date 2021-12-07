def corrupt_disperse(a,size):
 n = size*size
 b = a.copy()
 max = np.amax(b)
 min = np.amin(b)
 for p in range(n):
   i = np.random.choice(range(0, 199))
   j = np.random.choice(range(0, 199))
   try:
     b[i][j] = np.random.randint(np.amin(b), np.amax(b))
   except IndexError:
     continue
 return b
