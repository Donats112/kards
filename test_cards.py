from numuri import check_card_type

def test_check_card_type():
    assert check_card_type("4003600000000014") == "VISA"
    assert check_card_type("6176292929") == "INVALID"
    assert check_card_type("371449635398431") == "AMEX"
    assert check_card_type("5555555555554444") == "MasterCard"
    assert check_card_type("4111111111111111") == "VISA"
