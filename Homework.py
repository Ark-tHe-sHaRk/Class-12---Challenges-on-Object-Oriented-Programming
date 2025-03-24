class IntegerToRoman:
    def __init__(self):
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def convert(self, num):
        roman_numeral = ''
        for value, numeral in self.value_map:
            while num >= value:
                roman_numeral += numeral
                num -= value
        return roman_numeral

converter = IntegerToRoman()
print(converter.convert(4))  