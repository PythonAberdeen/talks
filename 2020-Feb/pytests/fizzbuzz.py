class FizzBuzz():
    fizz, buzz = 'Fizz', 'Buzz'

    @staticmethod
    def is_mod_three_true(number):
        return number % 3 == 0

    @staticmethod
    def is_mod_five_true(number):
        return number % 5 == 0

    def is_mod_three_and_five_true(self, number):
        return self.is_mod_five_true(number) and self.is_mod_three_true(number)

    def evaluate(self, number):
        if not isinstance(number, int):
            raise OurCustomException

        if self.is_mod_three_and_five_true(number):
            return "{}{}".format(self.fizz, self.buzz)
        if self.is_mod_three_true(number):
            return self.fizz
        elif self.is_mod_five_true(number):
            return self.buzz
        else:
            return number


class OurCustomException(Exception):
    print("Custom Exception")
