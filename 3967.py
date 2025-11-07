class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        power_of_ten = 1
    
        while n > 0:
            digit = n % 10
      
            if digit > 0:
                component = digit * power_of_ten
                result.append(component)
        
            n = n // 10
            power_of_ten *= 10

        return result[::-1]