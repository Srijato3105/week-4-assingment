class Solution:
    def delete_node(self, head, x):
        # If list is empty
        if not head:
            return head
        
        # If the node to delete is the head
        if x == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            head.next = None  # disconnect the old head
            return new_head
        
        current = head
        count = 1
        
        # Traverse to the node at position x
        while current and count < x:
            current = current.next
            count += 1
        
        # If node at position x exists
        if current:
            # Update next node's prev pointer if next node exists
            if current.next:
                current.next.prev = current.prev
            
            # Update previous node's next pointer
            if current.prev:
                current.prev.next = current.next
            
            # Disconnect current node
            current.prev = None
            current.next = None
        
        return head
