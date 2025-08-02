class Item:
    def __init__(self, name: str, price: int):
        # name and price are stored as given — price may be reused multiple times
        self.name = name
        self.price = price

    # stored as attributes only; no custom __str__ needed for this problem
    # accessing `item.name` directly will return its name

class ShoppingCart:
    def __init__(self):
        # we keep items in a list; duplicates are allowed
        self._items: list[Item] = []

    def add(self, item: Item):
        """Adds *one* instance of the given item."""
        self._items.append(item)

    def total(self) -> int:
        """Returns the sum of prices of all items currently in the cart."""
        return sum(it.price for it in self._items)

    def __len__(self) -> int:
        """Makes len(cart) return the number of items added."""
        return len(self._items)

def main():
    import sys

    data = sys.stdin.read().strip().split()
    it = iter(data)

    n = int(next(it))        # number of distinct items
    items = {}

    for _ in range(n):
        name = next(it)
        price = int(next(it))
        items[name] = Item(name, price)

    cart = ShoppingCart()
    q = int(next(it))        # number of operations

    for _ in range(q):
        op = next(it)
        if op == "add":
            # next token is the item name
            name = next(it)
            if name in items:
                cart.add(items[name])
            else:
                raise ValueError(f"Unknown item name: '{name}'")
        elif op == "total":
            print(cart.total())
        elif op == "len":
            print(len(cart))
        else:
            raise ValueError(f"Unknown operation: '{op}'")


if __name__ == "__main__":
    main()
