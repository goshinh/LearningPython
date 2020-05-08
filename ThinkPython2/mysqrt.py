import math
def mysqrt(a):
  x = 3
  while True:
#    print(x)
    y = (x + a/x) / 2
    if y == x:
      break
    x = y
  return y

def test_square_root(a):
#  print(a,math.sqrt(a),math.sqrt(a)-mysqrt(a))
  print('{:<4}{:<20}{:<20}{:<20}'.format(a,mysqrt(a),math.sqrt(a),math.sqrt(a) - mysqrt(a)))

print('{:<4}{:<20}{:<20}{:<20}'.format('a','mysqrt(a)','math.sqrt(a)','diff'))
print('{:<4}{:<20}{:<20}{:<20}'.format('-','---------','------------','----'))
for i in range(1,100):
  test_square_root(i)
