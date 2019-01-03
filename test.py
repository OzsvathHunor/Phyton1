from calculations import numbers_sum, main   #ha "import *" irsz az osszes fuggvenyt lefuttassa


def testing_numbers_sum1():
    assert numbers_sum(num1=2, num2=3) == 5
    return "testing_numbers_sum1() passed successfully"


def testing_numbers_sum2():
    assert numbers_sum(num1=3, num2=3) == 6
    return "testing_numbers_sum2() passed successfully"


print testing_numbers_sum1()
print testing_numbers_sum2()
main()
