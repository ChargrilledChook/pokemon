class Pokemon:

  def __init__(self,name):
    self.name = name

  def speak(self):
    print('Hi!')

bulby = Pokemon('Bulby')

print(bulby.name)

bulby.speak()
