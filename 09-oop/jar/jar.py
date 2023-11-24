# capacity is the cookie jar’s capacity
# size is the number of cookies actually in the cookie jar

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be over 0")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        total = self.size + n
        if total > self.capacity:
            raise ValueError(f"Cannot deposity this value of cookies. You can add to {self.capacity - self.size} cookies")
        else:
            self._size = total


    def withdraw(self, n):
        total = self.size - n
        if total < 0:
            raise ValueError(f"Cannot remove this value of cookies. You can remove up to {self.size} cookies")
        else:
            self._size = total

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    myJar = Jar()
    myJar.deposit(2)
    myJar.withdraw(1)
    print(myJar)

if __name__ == "__main__":
    main()
