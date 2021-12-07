def corrupt(a,size):
 b = a.copy()
 i = np.random.choice(range(0, 199))
 j = np.random.choice(range(0, 199))
 max = np.amax(b)
 min = np.amin(b)
 for p in range(-size,size):
   for t in range(-size,size):
     try:
       b[i+p][j+t] = np.random.randint(np.amin(b), np.amax(b))
     except IndexError:
       continue
 return b
