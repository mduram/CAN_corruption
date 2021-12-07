
def drug_alcohol(a,size):
  b = a.copy()
  b = np.where(b <0, b*size, b)
  return b

def drug_NMDA(a,size):
  b = a.copy()
  b = np.where(b >0, b*size, b)
  return b
