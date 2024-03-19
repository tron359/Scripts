def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ipsplit=ip.split(".")
    #check if all strings in the list are digits, and if only 3 periods are used (ip4 address only has 3)
    if all(number.isdigit() for number in ipsplit) and sum(1 for period in ip if period == ".")==3:
        #return if all values are between 0 to 255.
        return all(0 <= int(number) <= 255 for number in ipsplit)
    else:
        return False


if __name__ == "__main__":
    main()