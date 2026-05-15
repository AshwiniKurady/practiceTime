class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def makeLinkedList(self,list):
        dummy = ListNode()
        current = dummy
        for each_value in list:
            dummy.next = ListNode(each_value)
            dummy = dummy.next
        return current.next

    def printLinkedList(self,head):
        print("Printing LinkedList")
        cur = head
        while cur!=None:
            print(cur.val, " --> ")
            cur = cur.next
        
    def reorderLinkedList(self, head):

        # Find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # cut the list
        second = slow.next
        slow.next = None 
        
        #reverse second half
        prev = None
        while second:
            next_item = second.next
            second.next = prev
            prev = second
            second = next_item
        
        #Merge two halves
        first = head
        second = prev










        reorderedList = ListNode()
        finalreturn = reorderedList

        while dummy1!=None and dummy2!=None:
            reorderedList.next = dummy1
            reorderedList.next.next=dummy2
            dummy1 = dummy1.next
            dummy2 = dummy2.next

        return finalreturn.next


if __name__ == "__main__":
    insSolution = Solution()
    head = insSolution.makeLinkedList([1,2,3,4])
    finalreturn = insSolution.reorderLinkedList(head)
    insSolution.printLinkedList(finalreturn)