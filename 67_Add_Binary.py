# https://leetcode.com/problems/add-binary/description/
# Easy
# Math
# String
# Bit Manipulation
# Simulation


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # [x,y] = sorted([a,b], key=len, reverse=True)
        # resultBinary = ""
        # carry = 0
        # result = 0
        # for i in range(1, len(x)+1):
        #     if(i>len(y)):
        #         result = carry + int(x[-i]) + 0
        #     else:
        #       result = carry + int(x[-i]) +int(y[-i])          
        #     if(result == 0):
        #         resultBinary = "0" + resultBinary
        #         carry = 0
        #     elif(result == 1):
        #         resultBinary = "1" + resultBinary
        #         carry = 0
        #     elif(result == 2):
        #         resultBinary = "0" + resultBinary
        #         carry = 1
        #     elif(result == 3):
        #         resultBinary = "1" + resultBinary
        #         carry = 1
        # if( result ==  3 or 2):
        #     resultBinary = "1" + resultBinary
        # return resultBinary
# ==============================================================================================================================================================
        # i, j = len(a) - 1, len(b) - 1
        # carry = 0
        # result = ""

        # while i >= 0 or j >= 0:
        #     bit_a = int(a[i]) if i >= 0 else 0
        #     bit_b = int(b[j]) if j >= 0 else 0

        #     total = bit_a + bit_b + carry
        #     carry = total // 2
        #     result = str(total % 2) + result

        #     i -= 1
        #     j -= 1

        # if carry:
        #     result = "1" + result

        # return result
# ==============================================================================================================================================================
        carry = 0
        res = []
        
        idxA, idxB = len(a) - 1, len(b) - 1
        
        while idxA >= 0 or idxB >= 0 or carry == 1:
            if idxA >= 0:
                carry += int(a[idxA])
                idxA -= 1            
            if idxB >= 0:
                carry += int(b[idxB])
                idxB -= 1            

            res.append(str(carry % 2))
            carry = carry // 2

        return "".join(res[::-1])

bin = Solution()
bin.addBinary("111","111") 
bin.addBinary("111","11") 
bin.addBinary("1010","1011")
