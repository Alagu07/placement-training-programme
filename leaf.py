class Tree_structure:
 def __init__(self, data=None):
 self.key = data
 self.children = []
 def set_root_node(self, data):
 self.key = data
 def add_vals(self, node):
 self.children.append(node)
 def search_val(self, key):
 if self.key == key:
 return self
 for child in self.children:
 temp = child.search(key)
 if temp is not None:
 return temp
 return None
 def count_leaf_node(self):
 leaf_nodes = []
 self.count_leaf_node_helper_fun(leaf_nodes)
 return len(leaf_nodes)
 def count_leaf_node_helper_fun(self, leaf_nodes):
 if self.children == []:
 leaf_nodes.append(self)
 else:
 for child in self.children:
 child.count_leaf_node_helper_fun(leaf_nodes)
tree = None
print('Menu (this assumes no duplicate keys)')
print('add <data> at root')
print('add <data> below <data>')
print('count')
print('quit')
while True:
 my_input = input('What operation would you like to perform ? ').split()
 operation = my_input[0].strip().lower()
 if operation == 'add':
 data = int(my_input[1])
 newNode = Tree_structure(data)
 sub_op = my_input[2].strip().lower()
 if sub_op == 'at':
 tree = newNode
 elif sub_op == 'below':
 my_pos = my_input[3].strip().lower()
 key = int(my_pos)
 ref_node = None
 if tree is not None:
 ref_node = tree.search_val(key)
 if ref_node is None:
 print('No such key.')
 continue
 ref_node.add_vals(newNode)
 elif operation == 'count':
 if tree is None:
 print('The tree is empty')
 else:
 count = tree.count_leaf_node()
 print('The number of leaf nodes are : {}'.format(count))
 elif operation == 'quit':
 break
