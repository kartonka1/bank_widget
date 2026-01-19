from src.external_api.currency import convert_to_rub


def test_convert_to_rub_stub():
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "RUB"},
        }
    }

    assert convert_to_rub(transaction) == 0.0
