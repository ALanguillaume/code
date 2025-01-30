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
        self.quantity = quantity
        self.eta = eta

    def can_allocate(self, line):
        return self.quantity >= line.quantity and self.sku == line.sku

    def allocate(self, line):
        if self.can_allocate(line):
            self.quantity = self.quantity - line.quantity
            return self
        else:
            raise ValueError("Cannot allocate more than available quantity")
