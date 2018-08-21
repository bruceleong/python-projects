#one.py
print('hello')
def myfunc():
  print('running myfunc stuff - one.py')

print('top level in one.py')

if __name__ == "__main__":
  myfunc()
  print('one.py is running')
else:
  print('one.py has been imported')
