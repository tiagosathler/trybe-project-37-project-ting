from collections import deque


class Queue:
    def __init__(self) -> None:
        self._data = deque()

    def __len__(self) -> int:
        return len(self._data)

    def enqueue(self, value: dict) -> None:
        self._data.append(value)

    def dequeue(self) -> dict:
        return self._data.popleft()

    def search(self, index: int) -> dict:
        if (0 <= index < len(self)):
            return self._data[index]
        else:
            raise IndexError("Index out of bounds")
