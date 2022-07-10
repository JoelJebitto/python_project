class Utility(object):
        class String():
                @staticmethod
                def rearrangeAList(a):
                        result = []
                        for i in range(1, len(a)):
                                result.append(a[len(a) - i])
                        return result

                @staticmethod
                def vowelsToCapsIfSmallAndSmallIfCaps(string=""):
                        result = ""
                        for i in string:
                                if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                                        if i.upper() == i:
                                                result += i.lower()
                                        elif i.lower() == i:
                                                result += i.upper()
                                else:
                                        result += i
                        return result

                @staticmethod
                def capsToSmallAmdSmallToCaps(string=""):
                        result = ""
                        for i in range(len(string)):
                                if  str(string[i].upper) == str(i):
                                        result += string[i].lower()
                                if string[i].lower == i:
                                        result += string[i].upper()
                                else:
                                        result += string[i]
                        return result


if __name__ == '__main__':
        i = Utility()
        print(i.capsToSmallAmdSmallToCaps("Hello, World"))
