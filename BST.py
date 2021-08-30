# ADRIAN CHING LIANSHENG 18063865
# NG WEI JINN 18064154
# ROGER JIA SIEN BOON 18046847

import time

def print_command(msg='', value=''):
    print('\n---------------------\n')
    print(msg, value)
    return

def print_menu():
    print(' __________________________________________')
    print('|       Please select an action:           |')
    print('|__________________________________________|')
    print('| 1: Insert node into BST                  |')
    print('| 2: Remove node from BST                  |')
    print('| 3: Check if value exists in BST          |')
    print('| 4: Get largest & smallest value in BST   |')
    print('| 5: Get max depth/height of BST           |')
    print('| 6: Print BST & traversal orders          |')
    print('| 0: Exit program                          |')
    print('|__________________________________________|\n')
    return input('Action: ')

def value_type_converter(value):

    # User input will always be in String.
    # If user enters Int or Float,
    # the data needs conversion.
    try:
        float(value)
        if '.' in value:
            value = float(value)
        else:
            value = int(value)
    except:
        if type(value) is str:
            value = value.upper()
            if not value.isalpha():
                    return False
    return value


class BinarySearchTree:
    
    #=====Main Program=====
    def __init__(self, value=None):
        self.left_node = None
        self.right_node = None
        self.value = value
        
        
    #=====Edit BST Functions=====
    def insert(self, value):
        
        value = value_type_converter(value)

        if value == False:
            print_command('Not a valid alphabet.')
            return False

        if not self.value:
            self.value = value
            return
    
        #Validate data types based on the 1st value inserted / root node
        if (type(self.value) is str and type(value) is str) or (type(self.value) is int or type(self.value) is float) and (type(value) is int or type(value) is float):
                
            if self.value == value:
                print_command('Failed to add, already exists:', value)
                return False
            
            if value < self.value:
                print(f'Value {value} is lesser than {self.value}, moved left.')
                if self.left_node:
                    outcome = self.left_node.insert(value)
                    if outcome != False:
                        return
                    else:
                        return False
                self.left_node = BinarySearchTree(value)
                return
    
            if self.right_node:
                outcome = self.right_node.insert(value)
                if outcome != False:
                    return
                else:
                    return False
            print(f'Value {value} is more than {self.value}, moved right.')
            self.right_node = BinarySearchTree(value)
        else:
            print_command('Invalid DataType:', str(type(value)))
            return False


    def delete(self, value):

        value = value_type_converter(value)

        if value == False:
            print_command('Not a valid alphabet.')
            return False

        if self == None:
            return self
        
        # Validation of data type, according to root node.
        if (type(self.value) is str and type(value) is str) or (type(self.value) is int or type(self.value) is float) and (type(value) is int or type(value) is float):
            if self.exists(value):
                if value < self.value:
                    if self.left_node:
                        self.left_node = self.left_node.delete(value)
                    return self
                if value > self.value:
                    if self.right_node:
                        self.right_node = self.right_node.delete(value)
                    return self
                if self.right_node == None:
                    return self.left_node
                if self.left_node == None:
                    return self.right_node
                min_larger_node = self.right_node
                while min_larger_node.left_node:
                    min_larger_node = min_larger_node.left_node
                self.value = min_larger_node.value
                self.right_node = self.right_node.delete(min_larger_node.value)
                return self
            else:
                print_command('Failed to remove, no such value in tree:', value)
                return False
        else:
            print_command('Invalid DataType:', str(type(value)))
            return False

    def exists(self, value):

        value = value_type_converter(value)

        if value == False:
            print_command('Not a valid alphabet.')
            return False

        if (type(self.value) is str and type(value) is str) or (type(self.value) is int or type(self.value) is float) and (type(value) is int or type(value) is float):
            if value == self.value:
                return True
    
            if value < self.value:
                if self.left_node == None:
                    return False
                return self.left_node.exists(value)
    
            if self.right_node == None:
                return False
            return self.right_node.exists(value)
        else:
            print_command('Invalid DataType:', str(type(value)))
            return False

    #=====Tree Traversal Functions=====
    def preorder(self, values):
        if self.value is not None:
            values.append(self.value)
        if self.left_node is not None:
            self.left_node.preorder(values)
        if self.right_node is not None:
            self.right_node.preorder(values)
        return values

    def inorder(self, values):
        if self.left_node is not None:
            self.left_node.inorder(values)
        if self.value is not None:
            values.append(self.value)
        if self.right_node is not None:
            self.right_node.inorder(values)
        return values

    def postorder(self, values):
        if self.left_node is not None:
            self.left_node.postorder(values)
        if self.right_node is not None:
            self.right_node.postorder(values)
        if self.value is not None:
            values.append(self.value)
        return values
    
    #=====Display Functions=====
    def add(self, value):
        outcome = self.insert(value)
        return outcome
        
    def remove(self, value):
        outcome = self.delete(value)
        return outcome
            
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
        
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right_node is None and self.left_node is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_node is None:
            lines, n, p, x = self.left_node._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_node is None:
            lines, n, p, x = self.right_node._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left_node, n, p, x = self.left_node._display_aux()
        right_node, m, q, y = self.right_node._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left_node += [n * ' '] * (q - p)
        elif q < p:
            right_node += [m * ' '] * (p - q)
        zipped_lines = zip(left_node, right_node)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    
#=====Get Depth / Height of Tree=====
def maxDepth(node):
    if node is None:
        return 0
    else:
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left_node)
        rDepth = maxDepth(node.right_node)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

def get_max(bst):
    return bst.inorder([])[-1]

def get_min(bst):
    return bst.inorder([])[0]

if __name__ == '__main__':
    
    #Create new BST
    bst = BinarySearchTree()

    user_input = print_menu()

    while user_input != '0':
        if user_input == '1':
            value = input('Please enter value/values (i.e.: \'5 10 2 13 1\') to be added into BST: ')
            for i in value.split(' '):
                outcome = bst.add(i)
                if outcome != False:
                    print(f'Successfully added {i} into BST.')
                    bst.display()
                    print_command()

        elif user_input == '2':
            value = input('Please enter the value to be removed from BST: ')
            for i in value.split(' '):
                outcome = bst.remove(i)
                if outcome != False:
                    print(f'\nSuccessfully removed {value} from BST.')
                    bst.display()
                    print_command()

        elif user_input == '3':
            value = input('\nPlease enter a value to check for: ')
            if bst.exists(value):
                print(f'Yes, value \'{value}\' exists in BST.')
            else:
                print(f'No, value \'{value}\' does not exist in BST.')

        elif user_input == '4':
            print('\nLargest value in BST:', get_max(bst))
            print('Smallest value in BST:', get_min(bst))
            
        elif user_input == '5':
            print('\nMax depth of BST:', maxDepth(bst))

        elif user_input == '6':
            bst.display()
            print('\nPreorder Traversal:', bst.preorder([]))
            print('Postorder Traversal:', bst.postorder([]))
            print('Inorder Traversal:', bst.inorder([]))

        else:
            print('Not a valid input. Please try again')

        for delay in range(44):
            print('.', end='', flush=True)
            time.sleep(0.04)
        print('\n')
        user_input = print_menu()

    
    print('Exited program... Have a nice day! :)')
    bst.display()