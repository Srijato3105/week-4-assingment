class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)
        
        # Case 1: Empty list
        if not head:
            new_node.next = new_node
            return new_node
        
        current = head
        
        while True:
            # Case 2: Insert between two nodes where data fits
            if current.data <= data <= current.next.data:
                break
            
            # Case 3: At the boundary where list wraps from max to min
            if current.data > current.next.data:
                # Insert if data is max or min
                if data >= current.data or data <= current.next.data:
                    break
            
            current = current.next
            
            # If we completed a full circle, insert here
            if current == head:
                break
        
        # Insert new_node after current
        new_node.next = current.next
        current.next = new_node
        
        # If new node data is smaller than head's data, new node becomes new head
        if data < head.data:
            return new_node
        
        return head
