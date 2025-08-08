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
        
        # Time Complexity ==> O(n)
        # Space Complexity ==> O(1)
        
        steps = self.length - n 
        temp = self.head
        
        if n > self.length or n < 0:
            return None

        i = 0 
        while i < steps:
            temp = temp.next
            i += 1
            
        
        return temp
        
    def is_identical_to(self, lst):
        # Time Complexity ==> O(n)
        # Space Complexity ==> O(1)
        
        len1,len2 = 0, 0
        
        temp1,temp2 = self.head, lst.head
        
        while temp1 is not None:
            len1 += 1
            temp1 = temp1.next
        
        while temp2 is not None:
            len2 += 1
            temp2 = temp2.next
            
        temp1,temp2 = self.head, lst.head   
        
        if len1 == len2:
            while temp2 is not None:
                if temp1.data == temp2.data:
                    temp1 = temp1.next
                    temp2 = temp2.next
                    
                else :
                    return False
                
            return True
        else:
            return False
        
    def add_element(self, value):
        # Time Complexity ==> O(n)
        # Space Complexity ==> O(1)
        
        # Empty List
        if not self.head:
            self.head = Node(value)
            return
        
        temp = self.head
        
        # Traverse in next has data
        while temp.next: temp = temp.next
        
        temp.next = Node(value)
            
    def get_tail(self):
        if not self.head : return "None"
        
        temp = self.head
        
        while temp.next : temp = temp.next
        
        return temp
        
        
def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([])

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = ''

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([6])

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '6'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test3():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([6, 10, 8, 15])
    lst.debug_print_existing_nodes()

    result = str(lst)
    expected = '6, 10, 8, 15'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'

    print('PASSED\n')

def test4():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([])
    lst.debug_print_existing_nodes()
    lst.insert_front(10)
    result = str(lst)
    expected = '10'
    
    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test5():
    func_name = inspect.currentframe().f_code.co_name
    print(f"Testing {func_name}")
    lst = LinkedList([10])
    lst.debug_print_existing_nodes()
    
    lst.insert_front(20)
    
    result = str(lst)
    expected = "20, 10"
    
    lst.debug_print_existing_nodes()

    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test6():
    func_name = inspect.currentframe().f_code.co_name
    print(f"Testing {func_name}")
    lst = LinkedList([10,20])
    lst.debug_print_existing_nodes()
    
    lst.insert_front(30)
    
    result = str(lst)
    expected = "30, 10, 20"
    
    lst.debug_print_existing_nodes()
    
    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test7():
    func_name = inspect.currentframe().f_code.co_name
    print(f"Testing {func_name}")
    lst = LinkedList([10,20,30])
    lst.debug_print_existing_nodes()
    
    lst.insert_front(40)
    
    result = str(lst)
    expected = "40, 10, 20, 30"
    
    lst.debug_print_existing_nodes()
    
    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    
    lst.debug_verify_data_integrity()
    print('PASSED\n')

def test8():
    func_name = inspect.currentframe().f_code.co_name
    print(f"Testing {func_name}")
    lst = LinkedList([])
    lst.debug_print_existing_nodes()
    
    lst.delete_front()
    
    result = str(lst)
    expected = ""
    
    lst.debug_print_existing_nodes()
    
    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    
    lst.debug_verify_data_integrity()
    print('PASSED\n')
    
def test9():
    func_name = inspect.currentframe().f_code.co_name
    print(f"Testing {func_name}")
    lst = LinkedList([10])
    lst.debug_print_existing_nodes()
    
    lst.delete_front()
    
    result = str(lst)
    expected = ""
    
    # lst.debug_print_existing_nodes()
    
    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    
    print('PASSED\n')
    
def test10():
    func_name = inspect.currentframe().f_code.co_name
    print(f"Testing {func_name}")
    lst = LinkedList([10, 20])
    lst.debug_print_existing_nodes()
    
    lst.delete_front()
    
    result = str(lst)
    expected = "20"
        
    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    
    print('PASSED\n')
    
def test11():
    func_name = inspect.currentframe().f_code.co_name
    print(f"Testing {func_name}")
    lst = LinkedList([10, 20, 30])
    lst.debug_print_existing_nodes()
    
    lst.delete_front()
    
    result = str(lst)
    expected = "20, 30"
    
    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'

    print('PASSED\n')
    
def test12():
    func_name = inspect.currentframe().f_code.co_name
    print(f"Testing {func_name}")
    lst = LinkedList([10, 20, 30,40,50,60])
    lst.debug_print_existing_nodes()
    
    lst.delete_front()
    lst.delete_front()
    lst.delete_front()
    lst.delete_front()
    
    result = str(lst)
    expected = "50, 60"
    
    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'

    print('PASSED\n')

def test13():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([6, 10, 8, 15])

    lst.debug_print_existing_nodes()
    result = str(lst.get_nth_back(5))
    
    expected = "None"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test14():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([6, 10, 8, 15])

    lst.debug_print_existing_nodes()
    result = str(lst.get_nth_back(2))
    
    expected = "8"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test15():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([6])

    lst.debug_print_existing_nodes()
    result = str(lst.get_nth_back(1))
    
    expected = "6"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test16():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    lst = LinkedList([])

    lst.debug_print_existing_nodes()
    result = str(lst.get_nth_back(1))
    
    expected = "None"

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test17():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    
    lst1 = LinkedList([1,2,3])
    lst2 = LinkedList([1,2,3,5,5,5])
    
    result = str(lst1.is_identical_to(lst2))
    expected = "False"
    
    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test18():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    
    lst1 = LinkedList([1,2,3])
    lst2 = LinkedList([1,2,4])
    
    result = str(lst1.is_identical_to(lst2))
    expected = "False"
    
    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test19():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    
    lst1 = LinkedList([1,2,3])
    lst2 = LinkedList([1,2,3])
    
    result = str(lst1.is_identical_to(lst2))
    expected = "True"
    
    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test20():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    
    lst = LinkedList([])
    lst.add_element(10)
    
    result = str(lst)
    expected = "10"
    print(result)
    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test21():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    
    lst = LinkedList([10])
    lst.add_element(20)
    
    result = str(lst)
    expected = "10, 20"
    print(result)
    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test22():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    
    lst = LinkedList([10, 20])
    lst.add_element(30)
    
    result = str(lst)
    expected = "10, 20, 30"
    print(result)
    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')

def test23():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    
    lst = LinkedList([])
    
    result = str(lst.get_tail())
    expected = "None"

    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test24():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    
    lst = LinkedList([10])
    
    result = str(lst.get_tail())
    expected = "10"

    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    
def test25():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')
    
    lst = LinkedList([10, 20])
    
    result = str(lst.get_tail())
    expected = "20"

    assert result == expected , f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')
    

if __name__ == '__main__':
    # test1()  # empty
    # test2()  # one element
    # test3()  # 6, 10, 8, 15
    
    # # ========= Insert Front =========
    # test4()  # empty
    # test5()  # one element
    # test6()  # two element
    # test7()  # N elements
    
    # # ========= Delete Front =========
    # test8()  # empty
    # test9()  # one element
    # test10()  # two element
    # test11()  # N elements
    # test12()  # N elements with N deletion
    
    # test13()  # None if such position doesn’t exist
    # test14()  # N elements
    # test15()  # one element
    # test16()  # empty
    
    # test17() # different length
    # test18() # same length with different values
    # test19() # same length with same values
    
    # test20() # empty list
    # test21() # one element in list
    # test22() # two element in list
    
    test23() # empty list
    test24() # one element
    test25() # two element in list
    
    # Must see to insure no RTE
    print('ALL CASES PASSED')

