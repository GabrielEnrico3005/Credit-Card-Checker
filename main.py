def isValid(number):
    step2_result = sumOfDoubleEvenPlace(number)
    step3_result = sumOfOddPlace(number)
    final_sum = step2_result + step3_result
    return final_sum % 10 == 0


def sumOfDoubleEvenPlace(number):
    number_str = str(number)
    sum_result = 0
    for i in range(len(number_str) - 2, -1, -2):
        sum_result += getDigit(int(number_str[i]) * 2)
    return sum_result


def getDigit(number):
    if number < 10:
        return number
    else:
        return (number % 10) + (number // 10)


def sumOfOddPlace(number):
    number_str = str(number)
    sum_result = 0
    for i in range(len(number_str) - 1, -1, -2):
        sum_result += int(number_str[i])
    
    return sum_result

credit_card_number = int(input("Enter credit card number: "))

if isValid(credit_card_number):
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")