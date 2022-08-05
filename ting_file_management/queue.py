from collections import deque


class Queue:
    def __init__(self) -> None:
        self._data = deque()

    def __len__(self) -> int:
        return len(self._data)

    def enqueue(self, value: dict) -> None:
        self._data.append(value)

    def dequeue(self) -> int:
        return self._data.popleft()

    def search(self, index: int) -> dict:
        if (index < 0 or index > len(self)):
            raise IndexError("Index out of bounds")
        else:
            return self._data[index]
