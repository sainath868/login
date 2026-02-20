"""Simple in-memory CRUD operations example."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class Record:
    id: int
    name: str
    email: str


class CRUDStore:
    """A small in-memory store with CRUD operations."""

    def __init__(self) -> None:
        self._records: Dict[int, Record] = {}
        self._next_id = 1

    def create(self, name: str, email: str) -> Record:
        record = Record(id=self._next_id, name=name, email=email)
        self._records[self._next_id] = record
        self._next_id += 1
        return record

    def read_one(self, record_id: int) -> Record:
        if record_id not in self._records:
            raise KeyError(f"Record {record_id} does not exist")
        return self._records[record_id]

    def read_all(self) -> List[Record]:
        return [self._records[key] for key in sorted(self._records)]

    def update(self, record_id: int, *, name: str | None = None, email: str | None = None) -> Record:
        record = self.read_one(record_id)

        if name is not None:
            record.name = name
        if email is not None:
            record.email = email

        return record

    def delete(self, record_id: int) -> None:
        if record_id not in self._records:
            raise KeyError(f"Record {record_id} does not exist")
        del self._records[record_id]


if __name__ == "__main__":
    store = CRUDStore()
    alice = store.create("Alice", "alice@example.com")
    bob = store.create("Bob", "bob@example.com")

    print("Created:", asdict(alice), asdict(bob))
    print("Read one:", asdict(store.read_one(1)))
    updated = store.update(2, email="robert@example.com")
    print("Updated:", asdict(updated))
    store.delete(1)
    print("Remaining:", [asdict(record) for record in store.read_all()])
