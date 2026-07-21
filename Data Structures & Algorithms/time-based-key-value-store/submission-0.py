class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.table.keys():
            self.table[key] = [[timestamp, value]]
        else:
            self.table[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        currans = ""
        if not key in self.table.keys():
            return ""
        else:
            currlist = self.table[key]
            if timestamp > currlist[-1][0]:
                return self.table[key][-1][-1]
            else:
                left = 0
                right = len(currlist) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if currlist[mid][0] == timestamp:
                        return currlist[mid][1]
                    else:
                        if currlist[mid][0] < timestamp:
                            currans = currlist[mid][1]
                            left = mid + 1
                        else:
                            right = mid - 1
        return currans
