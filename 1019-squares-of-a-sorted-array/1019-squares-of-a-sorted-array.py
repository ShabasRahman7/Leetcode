class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length=len(nums)
        left_pos=0
        right_pos=length-1
        insert_pos=-1
        result = [0]*length
        while(left_pos<=right_pos):
            left_element,right_element =abs(nums[left_pos]),abs(nums[right_pos])
            if(left_element>right_element):
                result[insert_pos]=left_element**2
                left_pos+=1
            else:
                result[insert_pos]=right_element**2
                right_pos-=1
            insert_pos-=1
        return result