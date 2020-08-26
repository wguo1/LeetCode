class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        if (num >= 1000):
            result = ("M" * (num // 1000)) + self.intToRoman(num % 1000)
        else:
            half = ""
            full = ""
            exception = ""
            place = -1

            if (num > 100):
                half = "D"
                full = "M"
                exception = "C"
                place = 100
            elif (num > 10):
                half = "L"
                full = "C"
                exception = "X"
                place = 10
            else:
                half = "V"
                full = "X"
                exception = "I"
                place = 1

            if (num != 0):
                if (num >= 9 * place):
                    if (num < 10 * place):
                        result = exception
                    result = result + full
                elif (num >= 6 * place):
                    result = result + half + (((num // place) - 5) * exception)
                elif (4 * place <= num < 6 * place):
                    if (num < 5 * place):
                        result = exception
                    result = result + half
                else:
                    result = result + ((num // place) * exception)

                result = result + self.intToRoman(num % place)
            
        return result