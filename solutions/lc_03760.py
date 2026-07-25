# hash_table string
class Solution:
    def maxDistinct(self, s: str) -> int:
        return len( set(s) )
    
    def maxDistinct_v1(self, s: str) -> int:
        table = [0] * 26
        result = 0

        for c in s:
            char = ord(c) - 97
            table[char] += 1

        for val in table:
            result = result + 1 if val > 0 else result
        return result

solution = Solution()


tests = ["abab", "abcd", "aaaa"]

for string in tests:
    result = solution.maxDistinct(s=string)
    print(result)

