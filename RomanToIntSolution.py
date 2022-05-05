class RomanToIntSolution:
    def romanToInt(self, s: str) -> int:
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000
        dictionary={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        temp = []
        num = 0
        for c in s:
            temp.append(dictionary[c])

        for i, v in enumerate(temp):
            try:
                if v < temp[i+1]:
                    num -= v
                else:
                    num += v
            except:
                num += v
        return num
