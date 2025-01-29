from datetime import date, timedelta
import pytest

from model import Batch, OrderLine

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch(ref="batch-001", sku=sku, quantity=batch_qty, eta=today),
        OrderLine(order_ref="order-123", sku=sku, quantity=line_qty)
    )


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch, line = make_batch_and_line(
        sku="FANCY-LAMP", batch_qty=20, line_qty=2
    )
    batch.allocate(line)

    assert batch.quantity == 18


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line(
        sku="FANCY-LAMP", batch_qty=20, line_qty=2
    )
    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = make_batch_and_line(
        sku="FANCY-LAMP", batch_qty=20, line_qty=40
    )
    assert small_batch.can_allocate(large_line) is False


def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line(
        sku="FANCY-LAMP", batch_qty=20, line_qty=20
    )
    assert batch.can_allocate(line)




# def test_prefers_warehouse_batches_to_shipments():
#     pytest.fail("todo")


# def test_prefers_earlier_batches():
#     pytest.fail("todo")
