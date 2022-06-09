# A simple example of a singly-linked list. Is not a totally OOP approach
# as list traversal and manipulation is handled with global variables and functions
# as opposed to a LinkedList class.

# Individual node in linked list
class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None

  def set_next_node(self, next):
    self.next_node = next

# node_a is the 'head' of our list
node_a = Node('Hello')
#node_b = Node('World')
#node_c = Node('!')

# Connect nodes 
#node_a.set_next_node(node_b)
#node_b.set_next_node(node_c)

# Iterate thru list
pointer = node_a
while(pointer):
  #print(pointer.value)
  pointer = pointer.next_node

# Pass in the head of a linked list, and a value --
# this function will append a new node at the end of the list
# with desired value.
def add_to_list(head, new_value):
  new_node = Node(new_value)

  # Get to the end of the list
  # So I can append (add on) the new node
  pointer = head
  while(pointer):
    # End of list, add new the node & exit loop
    if(pointer.next_node == None):
      pointer.next_node = new_node
      break

    # Otherwise move on to the next node in the list
    else:
      pointer = pointer.next_node

# Adding some nodes to our list 
add_to_list(node_a, 'World')
add_to_list(node_a, '!')
add_to_list(node_a, ' It is sunny')
add_to_list(node_a, ' and the weather is good.')

# Traverse through list and print value of each node
def print_list(head):
  pointer = head
  while(pointer):
    print(pointer.value)
    pointer = pointer.next_node

print_list(node_a)