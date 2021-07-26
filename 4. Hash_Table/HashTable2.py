addressBook = {'kim' : 'Seoul', 'james' : 'NewYork', 'ami' : 'Tokyo', 'karm' : 'Paris',
'yami' : 'Busan', 'lee' : 'Incheon',
'park' : 'London', 'potter' : 'Madrid',
'kuda' : 'Rome', 'euna' : 'Seoul',
}
class myHashTable:
  def __init__(self):
    self.size = 17
    self.count = 0
    self.hashArray = [None for _ in range(self.size)]
    
  def hashFunction(self, strData, mod):
    hf = 0
    for s in strData:
      hf = hf * 137 + ord(s)
    return hf % mod
  
  def add(self, key, value):
    if self.count >= self.size:
      return
    hf = self.hashFunction(key, self.size)
    while self.hashArray[hf] is not None:
      # Linear Probing
      hf += 1

      # Quadratic Probing
      # cnt = 1
      # hf += cnt * cnt
      # cnt += 1

      # Double Hashing:해쉬값을 증가시키는것도 해쉬함수로 계산
      #hf += self.hashFunction(key, 7)
      #hf = hf % self.size

    self.hashArray[hf] = (key, value)
    self.count += 1
  
  def showTable(self):
    print('개수 : ', self.count)
    for data in self.hashArray:
      if data is not None:
        print(data, end=' ')
    

ht = myHashTable()
for name, address in addressBook.items():
  ht.add(name, address)

ht.showTable()
print()
print(ht.hashArray)
