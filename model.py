class Batch:

    def __init__(self, ref, sku, quantity, eta):
        self.ref = ref
        self.sku = sku
        self.quantity = quantity
        self.eta = eta

    def allocate(self, line):
        self.quantity = self.quantity - line.quantity
        return self


class OrderLine:

    def __init__(self, order_ref, sku, quantity):
        self.order_ref = order_ref
        self.sku = sku
        self.quantity = quantity
