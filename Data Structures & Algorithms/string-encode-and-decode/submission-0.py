class Solution:

    def encode(self, strs: List[str]) -> str:
        builder = ""
        for string in strs:
            builder = builder + f"{len(string)}" + "#" + string
        return builder
            

    def decode(self, s: str) -> List[str]:
        pointer = 0
        finallist = []
        while pointer < len(s):
            number = ""
            while s[pointer] != "#":
                number = number + s[pointer]
                pointer += 1
            actualnumber = int(number)
            pointer += 1
            finallist.append(s[pointer:(pointer+actualnumber)])
            pointer += actualnumber
        return finallist

