class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1,num2='',''
        while l1:
            num1=str(l1.val)+num1
            l1=l1.next 
        while l2:
            num2=str(l2.val)+num2 
            l2=l2.next 
        num3=str(int(num1)+int(num2))
        ans=None
        while num3:
            node=ListNode(num3[0],ans)
            ans=node
            num3=num3[1:]
        return ans
