# remember that Item is a generic variable, you declare it
# when making an object
#
# For example:
# d = Deque[int]()
#
class Deque[Item]:
    # construct an empty deque
    def __init__(self):
        self.deque: list[Item] = []

    # is the deque empty?
    def is_empty(self) -> bool:
        return len(self.deque) == 0

    # return the number of items on the deque
    def size(self) -> int:
        return len(self.deque)

    # add the item to the front
    def add_first(self, item: Item) -> None:
        self.deque.insert(0, item)

    # add the item to the back
    def add_last(self, item: Item) -> None:
        self.deque.append(item)

    # remove and return the item from the front
    def remove_first(self) -> Item:
        return self.deque.pop(0)

    # remove and return the item from the back
    def remove_last(self) -> Item:
        return self.deque.pop()

    def __iter__(self):
        pass

    # return the current item and tick the current item to the next
    # otherwise, raise StopIteration
    def __next__(self) -> Item:
        pass

    # unit testing (required)
    @staticmethod
    def main():
        pass


if __name__ == "__main__":
    Deque.main()
