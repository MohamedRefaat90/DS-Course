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

    def _add_node(self, node):
        self.debug_data.append(node)
        self.length += 1

    def _delete_node(self, node):
        if node in self.debug_data:
            self.debug_data.remove(node)
        else:
            print("Node does't exist!!")
            return

        self.length -= 1

    def debug_print_address(self):
        temp_head = self.head

        while temp_head is not None:
            print(f'{temp_head.data}@{id(temp_head)}', end='\t->\t')
            temp_head = temp_head.next
        print('None')

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

    ##############################################

    def insert_end(self, value):
        
        node = Node(value)
        self._add_node(node)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.debug_verify_data_integrity()  # ** verify as possible

    def print(self):
        temp_head = self.head

        while temp_head is not None:
            print(temp_head.data, end='->')
            temp_head = temp_head.next
        print('None')

    def __iter__(self):
        temp_head = self.head
        while temp_head is not None:
            yield temp_head
            temp_head = temp_head.next

    def __repr__(self):
        represent = ''
        temp_head = self.head

        while temp_head is not None:
            represent += str(temp_head.data)
            temp_head = temp_head.next
            if temp_head:
                represent += ', '

        return represent
    ##############################################
    
    def insert_front(self, value):
        
        # Time Complexity ==> O(1)
        # Space Complexity ==> O(1)
        
        newNode = Node(value)
        
        if self.length == 0:
            self.head = self.tail = newNode
            
        elif self.length == 1 :
            self.head = newNode
            self.head.next = self.tail
        else:
            prevHead = self.head
            self.head = newNode
            self.head.next = prevHead
                
        self._add_node(newNode)
        self.debug_verify_data_integrity()
    
    def delete_front(self):
        
        # Time Complexity ==> O(1)
        # Space Complexity ==> O(1)
        
        if self.length == 0:
            print("Your List is Already Empty")
            return
        
        elif self.length == 1:
            self._delete_node(self.head)
            self.head = self.tail = None
        
        else:
            self._delete_node(self.head)
            self.head = self.head.next
        
        self.debug_verify_data_integrity()

    def get_nth_back(self, n):
        
        steps = self.length - n 
        temp = self.head
        
        if n > self.length or n < 0:
            return None

        i = 0 
        while i < steps:
            temp = temp.next
            i += 1
            
        
        return temp
    
    def delete_node_with_key(self, value):
        # Time Complexity ==> O(n)
        # Space Complexity ==> O(1)
        
        if self.length == 0:
            return "Empty List"
        
        elif self.head.data == value:
            deletedValue = self.head.data
            self.delete_front()
            return deletedValue
        else:
            curr , prev = self.head , None
            
            while curr : 
                
                if curr.data == value:
                    prev.next = curr.next
                    self._delete_node(curr)
                    
                    if curr == self.tail:
                        self.tail = prev
                    return curr.data
                    
                prev, curr = curr , curr.next
        self.debug_verify_data_integrity()

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        curr = self.head
        
        if not self.head or not self.head.next:
            return ''
        
        while curr and curr.next :
            first= curr
            seconde = curr.next
            
            # Swapping
            prev.next = seconde         # dummy => 2
            first.next = seconde.next   # 1 => 3
            seconde.next = first        # 2 => 1
            
            # Move Pointers
            prev = first
            curr = first.next
        
        # reset the head
        self.head = dummy.next
        self.tail = prev if self.length % 2 == 0 else curr
            
            


def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([])
    # lst.delete_node_with_key(1)

    result = str(lst.delete_node_with_key(2))
    lst.debug_print_existing_nodes()
    expected = 'Empty List'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10, 20])
    

    result = str(lst.delete_node_with_key(20))
    lst.debug_print_existing_nodes()
    expected = '20'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test3():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([10, 20])
    

    result = str(lst.delete_node_with_key(10))
    lst.debug_print_existing_nodes()
    expected = '10'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test4():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10, 20, 30, 40])
    

    result = str(lst.delete_node_with_key(40))
    lst.debug_print_existing_nodes()
    expected = '40'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test5():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10, 20, 30, 40])
    

    result = str(lst.delete_node_with_key(30))
    lst.debug_print_existing_nodes()
    expected = '30'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test6():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10, 20, 30, 40])
    

    result = str(lst.delete_node_with_key(3000))
    lst.debug_print_existing_nodes()
    expected = 'None'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test7():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10, 20, 30, 40, 20])
    

    result = str(lst.delete_node_with_key(20))
    lst.debug_print_existing_nodes()
    expected = '20'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test8():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10, 20, 30, 40])
    
    lst.swap_pairs()
    result = str(lst)
    lst.debug_print_existing_nodes()
    expected = '20, 10, 40, 30'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test9():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10, 20])
    
    lst.swap_pairs()
    result = str(lst)
    lst.debug_print_existing_nodes()
    expected = '20, 10'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test10():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10, 20, 30])
    
    lst.swap_pairs()
    result = str(lst)
    lst.debug_print_existing_nodes()
    expected = '20, 10, 30'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test11():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([])
    
    lst.swap_pairs()
    result = str(lst)
    lst.debug_print_existing_nodes()
    expected = ''

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


if __name__ == '__main__':
    
    # ========= delete with value =========
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    
    # ========= swap pairs =========
    test8()
    test9()
    test10()
    test11()

    # Must see to insure no RTE
    print('ALL CASES PASSED')