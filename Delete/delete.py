import inspect


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self, initial_values=None):
        self.head = None
        self.tail = None
        self.length = 0

        self.debug_data = []  # add/remove nodes you use

        if initial_values:
            for value in initial_values:
                self.insert_end(value)

    
    def __repr__(self):
        represent = ''
        temp_head = self.head

        while temp_head is not None:
            represent += str(temp_head.data)
            temp_head = temp_head.next
            if temp_head:
                represent += ', '

        return represent
    
    def _add_node(self, node):
        self.debug_data.append(node)
        self.length += 1
        
    def insert_end(self, value):
        
        node = Node(value)
        self._add_node(node)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.debug_verify_data_integrity()  # ** verify as possible
    
    def _delete_node(self, node):
        if node in self.debug_data:
            self.debug_data.remove(node)
        else:
            print("Node does't exist!!")
            return

        self.length -= 1
    
    def debug_verify_data_integrity(self):
        if self.length == 0:
            assert self.head is None
            assert self.tail is None
            return

        assert self.head is not None
        assert self.tail is not None
        assert self.tail.next is None

        if self.length == 1:
            assert self.head == self.tail
        elif self.length == 2:
            assert self.head.next == self.tail
        else:
            actual_lst_len = 0
            temp_head = self.head

            while temp_head is not None:
                temp_head = temp_head.next
                actual_lst_len += 1
                assert actual_lst_len < 1000  # Consider infinite cycle

            assert self.length == actual_lst_len
            assert self.length == len(self.debug_data)
    
    def debug_print_node(self, node):
        if node is None:
            print('None')
            return

        print(str(node.data).ljust(5), end=' -> ')
        next_value = 'None' if node.next is None else str(node.next.data)
        print(next_value.ljust(5), end='\t')

        if node == self.head:
            print("head")
        elif node == self.tail:
            print("tail")
        else:
            print("")
        
    def debug_print_existing_nodes(self, msg=None):
        if msg:
            print(msg)

        for node in self.debug_data:
            self.debug_print_node(node)

        print('*******************')

        self.debug_verify_data_integrity()
        
        
    def delete_front(self): # without depend on  Length
        
        # Time Complexity ==> O(1)
        # Space Complexity ==> O(1)
        
        if not self.head: # Empty List
            return "Linked List is Empty"
        
        elif self.head == self.tail: # One Node
            self.head = self.tail = None
            
        elif self.head.next == self.tail: # Two Nodes

            self.head = self.tail
            
        else: # Multiple Nodes
            self.head = self.head.next
            
        self._delete_node(self.head)
    
    def delete_last(self): # without depend on  Length
        
        # Time Complexity ==> O(1)
        # Space Complexity ==> O(1)
        
        if not self.head: # Empty List
            return "Linked List is Empty"
        
        elif self.head == self.tail: # One Node
            self.head = self.tail = None
        
        elif self.head.next == self.tail: # Two Nodes
            self.tail = self.head
            self.tail.next = None
        
        else: # Multiple Nodes
            temp = self.head
            prev = None
            
            while temp.next:
                prev = temp
                temp = temp.next
            
            self.tail = prev
            self.tail.next = None
            
        self._delete_node(self.head)

    def delete_node_nth(self, node):
        # Time Complexity ==> O(n)
        # Space Complexity ==> O(1)
        
        if node < 0 or node > self.length:
            return "Invalid Node"
        
        elif node == 0:
            self.delete_front()
            return "First Item Deleted"
            
        elif node == self.length -1:
            self.delete_last()
            return "Last Item Deleted"
            
        else:
            temp=self.head
            prev=None
            steps= 0
            
            while steps != node:
                prev = temp
                temp = temp.next
                prev.next = temp.next
                self._delete_node(temp)
                steps += 1
                    
            return f"Node {steps} with value {temp} Deleted"
        
        
    
    
def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([])

    lst.debug_print_existing_nodes()
    result = str(lst.delete_front())
    expected = 'Linked List is Empty'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10])

    lst.debug_print_existing_nodes()
    result = str(lst.delete_front())
    expected = "None"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test3():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20])

    lst.debug_print_existing_nodes()
    lst.delete_front()
    result = str(lst)
    expected = "20"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test4():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20, 30, 40])

    lst.debug_print_existing_nodes()
    lst.delete_front()
    result = str(lst)
    expected = "20, 30, 40"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test5():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20, 30, 40])

    lst.debug_print_existing_nodes()
    lst.delete_front()
    lst.delete_front()
    result = str(lst)
    expected = "30, 40"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test6():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([])

    lst.debug_print_existing_nodes()
    result = str(lst.delete_last())
    expected = 'Linked List is Empty'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test7():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10])

    lst.debug_print_existing_nodes()
    
    result = str(lst.delete_last())
    expected = "None"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test8():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20])

    lst.debug_print_existing_nodes()
    lst.delete_last()
    result = str(lst)
    expected = "10"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test9():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20, 30, 40])

    lst.debug_print_existing_nodes()
    lst.delete_last()
    result = str(lst)
    expected = "10, 20, 30"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test10():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20, 30, 40])

    lst.debug_print_existing_nodes()
    lst.delete_last()
    lst.delete_last()
    result = str(lst)
    expected = "10, 20"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test11():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20, 30, 40])

    lst.debug_print_existing_nodes()
    
    result = str(lst.delete_node_nth(-1))
    expected = "Invalid Node"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test12():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20, 30, 40])

    lst.debug_print_existing_nodes()
    
    result = str(lst.delete_node_nth(0))
    expected = "First Item Deleted"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test13():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20, 30, 40])

    lst.debug_print_existing_nodes()
    
    result = str(lst.delete_node_nth(lst.length - 1))
    expected = "Last Item Deleted"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test14():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20, 30, 40])

    lst.debug_print_existing_nodes()
    
    result = str(lst.delete_node_nth(1))
    expected = "Node 1 with value 20 Deleted"
    lst.debug_print_existing_nodes()
    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test15():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20, 30, 40])

    lst.debug_print_existing_nodes()
    
    lst.delete_node_nth(1)
    result = str(lst.delete_node_nth(1))
    expected = "Node 1 with value 30 Deleted"
    lst.debug_print_existing_nodes()
    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
if __name__ == '__main__':
    # Delete Front
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    
    # Delete Last
    # test6()
    # test7()
    # test8()
    # test9()
    # test10()
    
    # Delete nth
    test11()
    test12()
    test13()
    test14()
    test15()
    
    

    # Must see to insure no RTE
    print('ALL CASES PASSED')

