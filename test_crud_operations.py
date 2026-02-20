import unittest

from crud_operations import CRUDStore


class CRUDStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = CRUDStore()

    def test_create_and_read(self) -> None:
        record = self.store.create("Alice", "alice@example.com")
        loaded = self.store.read_one(record.id)
        self.assertEqual(loaded.name, "Alice")
        self.assertEqual(loaded.email, "alice@example.com")

    def test_update(self) -> None:
        record = self.store.create("Bob", "bob@example.com")
        updated = self.store.update(record.id, name="Robert")
        self.assertEqual(updated.name, "Robert")
        self.assertEqual(updated.email, "bob@example.com")

    def test_delete(self) -> None:
        record = self.store.create("Eve", "eve@example.com")
        self.store.delete(record.id)
        with self.assertRaises(KeyError):
            self.store.read_one(record.id)


if __name__ == "__main__":
    unittest.main()
