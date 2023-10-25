#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Oct. 25, 2023
# This is program will tell you if your at the age to date there grandchild.


def main():
    user_age = str(input("Enter your age:\n"))
    try:
        user_age = int(user_age)
    except ValueError:
        print("Your age wasn't valid")
    else:
        if user_age > 25 and user_age < 40:
            print("You are able to date the grandchild")
        else:
            print("You cannot date the grandchild")
    finally:
        print("End")


if __name__ == "__main__":
    main()
