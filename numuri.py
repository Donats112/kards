# Koda paraugs
# returns True if checksum is valid, otherwise returns False
def Luhn_checks_my_card(card_number):
    card_number=input()
    x=len(card_number)-1
    extra_num=[]
    reiz_num = []
    while x >= 0:
        n=int(card_number[x-1])*2
        reiz_num.append(n)
        extra_num.append(card_number[x])
        x-=2
    print(extra_num)
    print(reiz_num)



    
    return ...

# returns name of card if digits are valid, otherwise returns "INVALID"
def check_card_type(card_number):
    card_type = ""
    if card_number[0] == 4:
        if len(card_number)==13 or len(card_number)==16:
            card_type="VISA"
        else:
            card_type="INVALID"

    elif card_number[0] == 3 and card_number[1] == 4:
        if len(card_number)==15:
            card_type="AMEX"
        else:
            card_type="INVALID"
    elif card_number[0] == 3 and card_number[1] == 7:
        if len(card_number)==15:
            card_type="AMEX"
        else:
            card_type="INVALID"

    elif card_number[0]==5:
        if card_number[1] == 1 or card_number[1] == 2 or card_number[1] == 3 or card_number[1] == 4 or card_number[1] == 5:
            if len(card_number) == 16:
                card_type="MasterCard"
            else:
                card_type="INVALID"
        else:
            card_type="INVALID"

    else:
        card_type="INVALID"
    return card_type

# main logic
def main():
    card_number = input("Card number: ")
    if Luhn_checks_my_card():
        print(check_card_type())
    else:
        print("INVALID")
    return card_number

if __name__ == "__main__":
    main()