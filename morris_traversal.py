import random

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def generate_random_binary_tree(n, values):
	"""
	Generate a random binary tree of n nodes. The values of each node will be the unique
	integers form k to k+n-1, also random.

	This is a simplified version that doesn't ensure uniformity.
	"""
	if n == 0:
		return None

	n_left = random.randint(0, n - 1)
	root = Node(values[0])
	root.left = generate_random_binary_tree(n_left, values[1:1 + n_left])
	root.right = generate_random_binary_tree(n - 1 - n_left, values[1 + n_left:])
	return root

def binary_tree_to_string(root):
	if root is None:
		return '()'

	return f'({root.value}, {binary_tree_to_string(root.left)}, {binary_tree_to_string(root.right)})'

def inorder_traversal_recursion(root, proccess_function):
	"""
	Simple inorder traversal using recursion.
	"""
	if root is None:
		return

	inorder_traversal_recursion(root.left, proccess_function)
	proccess_function(root)
	inorder_traversal_recursion(root.right, proccess_function)

def inorder_traversal_morris(root, proccess_function):
	"""
	Morris traversal (inorder). Doesn't use stack or recursion and is constant space.
	"""
	curr = root;
	while curr is not None:
		if curr.left is None:
			proccess_function(curr)
			curr = curr.right
		else:
			prev = curr.left
			while (prev.right is not None) and (prev.right is not curr):
				prev = prev.right
			if prev.right is None:
				prev.right = curr
				curr = curr.left
			else:
				prev.right = None
				proccess_function(curr)
				curr = curr.right

def main():
	n = 20
	values = list(range(1, n + 1))
	random.shuffle(values)
	root = generate_random_binary_tree(n, values)

	# Generate a random binary tree of n nodes and prints the string representation.
	print('Binary tree string representation')
	print(binary_tree_to_string(root))
	print()

	# Use recursive traversal to print out the values of the binary tree.
	print('Inorder traversal using recursion')
	inorder_traversal_recursion(root, lambda node: print(node.value, end = ', '))
	print()

	# Use morris traversal to print out the values of the binary tree.
	# Compare this result with the previous one, to verify correctiness.
	print('Inorder traversal using morris traversal')
	inorder_traversal_morris(root, lambda node: print(node.value, end = ', '))
	print()

if __name__=="__main__": 
    main() 