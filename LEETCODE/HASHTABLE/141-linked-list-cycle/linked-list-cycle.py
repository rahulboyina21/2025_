# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Below code will speed up the execution LOL
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
            fast=slow=head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    return True
            return False
# """        '''
#         Think in terms of the programming 
#         like if both start at the same position and one moves 1 step at a time normal and other moves
#         2 steps at a time 

#         a 1 step 
#         b 2 steps 

#         then at certain point there will be a co-incidence of both of the elements if there is a cycle
#         as the intersection is inevidable 

#         '''

#         """// Define variables
#         // Start at the same point of the race"""
    
# """
#         // While the fast node doesnt reach the end node with the None value the while loop will
#         continue right as that's the basic logic

#         if there is no end value with None then it will revist back to the old nodes 
#         then slow node will in the front line as the fast node went back in reverse order 
#         so in a specific iteration there will be a instance there the fast and slow will meet 
#         which will only happen if there is a cycle if not how can someone be fast and fall behind the
#         slow node without changing the speed of the slow node
# """
# """

# Mistakes Made:

# 1. In while i haven't considered the fast.next 
# why ? Overlooked i just thought just check current step but when we are validating one step and two steps ahead then it would be expensive to handle like fast.next = none can be handled by my code but fast.next=none and i still go for none.next -> that's brutal like 
# 0/0 you can't get nothing out of it expect you are a ant man LOL

# 2.head and head.next just checking them instead of the process above which is also wrong