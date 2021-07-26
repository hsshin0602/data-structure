addressBook = {'kim' : 'Seoul', 'james' : 'NewYork', 'ami' : 'Tokyo', 'karm' : 'Paris',
'yami' : 'Busan', 'lee' : 'Incheon',
'park' : 'London', 'potter' : 'Madrid',
'kuda' : 'Rome', 'euna' : 'Seoul',
}
class node:
    def __init__(self, data):
        self.data=data
        self.next=None

class myHashTable:
  def __init__(self):
    self.size = 17
    self.count = 0
    self.hashArray = [None for _ in range(self.size)]
    
  def hashFunction(self, strData, mod):
    hf = 0
    for s in strData:
      hf = hf * 137 + ord(s) #임의의 소수 , ord():아스키코드 변환
    return hf % mod
  
  def add(self, key, value):
    if self.count >= self.size:
      return
    hf = self.hashFunction(key, self.size)
    
    # Chaining 방법:linked_list
    if self.hashArray[hf] is None:
      self.hashArray[hf] = node((key, value))
    else:
      self.hashArray[hf].next = node((key, value))
    self.count += 1
  
  def showTable(self):
    print('개수 : ', self.count)
    for data in self.hashArray:
      if data is not None:
        horse = data
        while horse.next:
          print(horse.data, end = '->')
          horse = horse.next
        print(horse.data)
      else: 
        print(data)    

ht = myHashTable()
for name, address in addressBook.items():
  ht.add(name, address)

ht.showTable()