def create_cubes(n):
  for x in range(n):
    yield x**3

#print(list(create_cubes(10)))

def gen_fib(n):
  a = 1
  b = 1
  for i in range(n):
    yield a
    a, b = b, a+b

#for number in gen_fib(10):
 # print(number)

def simple_gen():
  for x in range(3):
    yield x

#for num in simple_gen():
#  print(num)

g = simple_gen()

print(next(g), 'one')
print(next(g), 'two')
print(next(g), 'threee')
