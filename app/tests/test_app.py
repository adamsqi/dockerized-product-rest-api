import json


def test_availability_register_product(client):
    res = client.get('/product/1')
    assert res.status_code == 200


def test_availability_get_all_available_products(client):
    res = client.get('/products/available')
    assert res.status_code == 200


def test_availability_get_all_sold_products(client):
    res = client.get('/products/sold_out')
    assert res.status_code == 200


def test_register_product(client):
    rv = client.post('/product/register', json={
        "sku": "1",
        "name": "prod1",
        "qty": 1,
        "price": 100
    })
    assert rv.status_code == 200


def test_register_quantity_change(client):
    res1 = client.post('/product/register', json={
        "sku": "2",
        "name": "prod1",
        "qty": 1,
        "price": 100
    })

    assert res1.status_code == 200
    res2 = client.put('/product/2/set_new_qty/2')
    expected = {
        "sku": "2",
        "name": "prod1",
        "qty": 2,
        "price": 100
    }
    assert res2.status_code == 200
    assert expected == json.loads(res2.get_data(as_text=True))
