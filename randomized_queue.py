import random

class RandomizedQueue[Item]:
    # construct an empty randomized queue
    def __init__(self):
        self.radQ: list[Item] = []

    # is the randomized queue empty?
    def is_empty(self) -> bool:
        return len(self.radQ) == 0

    # return the number of items on the randomized queue
    def size(self) -> int:
        return len(self.radQ)

    # add the item
    def enqueue(self, item: Item) -> None:
        self.deque.append(item)

    # remove and return a random item
    def dequeue(self) -> Item:
        return self.radQ.pop(random.choice(self.radQ))

    # return a random item (but do not remove it)
    def sample(self) -> Item:
        return random.choice(self.radQ)

    # for looping this object will loop over the items in a random order
    def __iter__(self):
        pass

    # return the current item and tick the current item to the next
    # otherwise, raise StopIteration
    def __next__(self) -> Item:
        old_current = self.radQ(0)
        self.radQ.remove(old_current)  # Remove the element
        self.radQ.append(1, old_current)  # Append it to the next index
        return self.radQ(1)
        

    # unit testing (required)
    @staticmethod
    def main():
        pass

if __name__ == "__main__":
    RandomizedQueue.main()