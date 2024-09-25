class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0
        
    
    def __str__(self):
        return self.size * "🍪 "

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies for the jar")
        self.size += n
    
    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies in the jar")
        print("Nom nom nom")
        return self.size - n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity can't be a negative number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size can't be greater then capacity")
        self._size = size
        

# def main():
#     cookie_jar = Jar()
#     cookie_jar.deposit(5)
#     print(cookie_jar)

# if __name__ == "__main__":
#     main()
    