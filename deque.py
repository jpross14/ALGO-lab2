# remember that Item is a generic variable, you declare it
# when making an object
#
# For example:
# d = Deque[int]()


from typing import Generic, TypeVar, Iterator

Item = TypeVar("Item")

class Deque(Generic[Item]):
    def __init__(self):
        """Construct an empty deque."""
        self.deque: list[Item] = []

    def is_empty(self) -> bool:
        """Check if the deque is empty."""
        return len(self.deque) == 0

    def size(self) -> int:
        """Return the number of items in the deque."""
        return len(self.deque)

    def add_first(self, item: Item) -> None:
        """Add an item to the front of the deque."""
        self.deque.insert(0, item)  

    def add_last(self, item: Item) -> None:
        """Add an item to the back of the deque."""
        self.deque.append(item)  

    def remove_first(self) -> Item:
        """Remove and return the item from the front of the deque."""
        if self.is_empty():
            raise IndexError("Cannot remove from an empty deque")
        return self.deque.pop(0)  

    def remove_last(self) -> Item:
        """Remove and return the item from the back of the deque."""
        if self.is_empty():
            raise IndexError("Cannot remove from an empty deque")
        return self.deque.pop()  

    def __iter__(self) -> Iterator[Item]:
        """Return an iterator for the deque."""
        self.index = 0  
        return self

    def __next__(self) -> Item:
        """Return the next item in the deque, or raise StopIteration."""
        if self.index >= len(self.deque):
            raise StopIteration  
        item = self.deque[self.index]
        self.index += 1
        return item

    @staticmethod
    def main():
        d = Deque[int]()  

        d.add_first(10)
        d.add_last(20)
        d.add_first(5)

        print("Deque contents:", list(d))  

        print("Removed first:", d.remove_first())  
        print("Removed last:", d.remove_last())   

        print("Final deque contents:", list(d)) 

if __name__ == "__main__":
    Deque.main()
