import requests

API_URL = "http://numbersapi.com/{}/{}"

class Number:
    def __init__(self, number):
        """
        Initializes the Number instance with a given number.
        """
        self.number = int(number)
        self.abs_num = abs(self.number)

    def is_prime(self):
        """
        Check if the number is a prime number.
        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if self.number < 2:
            return False
        for i in range(2, int(self.abs_num ** 0.5) + 1):
            if self.abs_num % i == 0:
                return False
        return True

    def is_perfect(self):
        """
        Determine if the number is a perfect number.
        A perfect number is a positive integer that is equal to the sum of its proper divisors,
        excluding itself. For example, 6 is a perfect number because its divisors are 1, 2, and 3,
        and 1 + 2 + 3 = 6.
        Returns:
            bool: True if the number is perfect, False otherwise.
        """

        divisors = []
        for i in range(1, self.abs_num // 2 + 1):
            if self.abs_num % i == 0:
                divisors.append(i)
        if sum(divisors) == self.abs_num:
            return True
        return False
    
    def properties(self):
        """
        Get the properties of the number.
        This method checks if the number is an Armstrong number and determines its parity (even or odd).
        It returns a list of properties that the number satisfies.
        Returns:
            list: A list containing the properties of the number. Possible values are "armstrong" and "even"/"odd".
        """
        result = []
        if self.is_armstrong():
            result.append("armstrong")
        result.append(self.get_parity())
        return result

    def is_armstrong(self):
        """
        Check if the number is an Armstrong number.
        An Armstrong number (also known as a narcissistic number) is a
        number that is equal to the sum of its own digits each raised
        to the power of the number of digits.

        Returns:
            bool: True if the number is an Armstrong number, False otherwise.
        """

        pow = len(str(self.abs_num))
        num = sum((int(x) ** pow) for x in str(self.abs_num))
        if num == self.abs_num:
            return True
        return False

    def get_parity(self):
        """
        Determine the parity (even or odd) of a given number.
        Returns:
            str: "even" if the number is even, "odd" if the number is odd.
        """
        if self.abs_num % 2 == 0:
            return "even"
        return "odd"

    def digit_sum(self):
        """
        Calculate the sum of the digits of the number.
        Returns:
            int: The sum of the digits of the number.
        """
        return sum(int(digit) for digit in str(self.abs_num))
    
    def fun_fact(self):
        """
        Fetch a fun fact about the number from an external API.
        Returns:
            str: A fun fact about the number if the request is successful, None otherwise.
        """
        url = API_URL.format(self.number,"math")
        response = requests.get(url, headers={"Content-Type": "application/json"})
        data = response.json()
        if response.status_code == 200:
            return data.get("text")
        return None
