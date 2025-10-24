from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    card_number = 1234567812345678
    account_number = 9876543210

    masked_card = get_mask_card_number(card_number)
    masked_account = get_mask_account(account_number)

    print(f"Маскированная карта: {masked_card}")
    print(f"Маскированный счёт: {masked_account}")


if __name__ == "__main__":
    main()
