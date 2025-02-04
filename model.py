from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    order_ref: str
    sku: str
    quantity: int


class Batch:

    def __init__(self, ref, sku, quantity, eta):
        self.ref = ref
        self.sku = sku
        self._purchased_quantity = quantity
        self._allocations = set()
        self.eta = eta

    def allocate(self, line):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line):
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.quantity for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line):
        return self.available_quantity >= line.quantity and self.sku == line.sku
