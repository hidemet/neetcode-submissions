# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev: ListNode | None = None 
        curr: ListNode | None = head

        while curr is not None:
            nxt = curr.next #1. Salva il riferimento al nodo successivo.
            curr.next = prev #2. Inverte la freccia del nodo corrente.
            prev = curr #3. Sposta prev sul nodo appena processato
            curr = nxt #4. Sposta curr al nodo successivo
        
        return prev # prev punta alla nuova testa (l'ex ultimo nodo)
