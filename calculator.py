class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            result = self.add(result, abs(a))
        if (a < 0) ^ (b < 0):
            result = -result
        return result

    def divide(self, a, b):
        if b == 0:
            return None 
        abs_a, abs_b = abs(a), abs(b)
        result = 0
        while abs_a >= abs_b:
            abs_a = self.subtract(abs_a, abs_b)
            result += 1
        if (a < 0) ^ (b < 0):  
            result = -result
        return result

    def modulo(self, a, b):
        if b == 0:
            return None 
        abs_a, abs_b = abs(a), abs(b)
        while abs_a >= abs_b:
            abs_a -= abs_b
        return abs_a if a >= 0 else -abs_a  


# Testing the methods
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(5, 2))
    print("Example: multiplication: ", calc.multiply(3, 7))
    print("Example: division: ", calc.divide(5, 2))
    print("Example: modulo: ", calc.modulo(5, 2)) 