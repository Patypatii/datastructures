# =========================
# DATA STRUCTURES
# =========================

# 1. Stack (LIFO)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if not self.is_empty() else None
    def peek(self): return self.items[-1] if not self.is_empty() else None
    def is_empty(self): return len(self.items) == 0

# 2. Queue (FIFO)
from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.popleft() if not self.is_empty() else None
    def is_empty(self): return len(self.items) == 0

# 3. Linked List
class Node:
    def __init__(self, value): self.value = value; self.next = None

class LinkedList:
    def __init__(self): self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = Node(value)

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

# 4. Binary Tree with Traversal
class TreeNode:
    def __init__(self, value): self.value = value; self.left = None; self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# =========================
# ALGORITHMS
# =========================

# 1. Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

# 2. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 3. Depth First Search (DFS) in Graph
def dfs(graph, start, visited=None):
    if visited is None: visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 4. Breadth First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

# =========================
# EXAMPLES
# =========================
if __name__ == "__main__":
    # Stack
    print("Stack:")
    s = Stack()
    s.push(10)
    s.push(20)
    print("Pop:", s.pop())

    # Queue
    print("\nQueue:")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Dequeue:", q.dequeue())

    # Linked List
    print("\nLinked List:")
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.print_list()

    # Binary Search
    print("\nBinary Search:")
    arr = [1, 3, 5, 7, 9]
    print("Index of 7:", binary_search(arr, 7))

    # Bubble Sort
    print("\nBubble Sort:")
    print("Sorted:", bubble_sort([5, 3, 8, 4, 2]))

    # DFS and BFS
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("\nDFS:")
    dfs(graph, 'A')
    print("\nBFS:")
    bfs(graph, 'A')

    # Binary Tree
    print("\n\nBinary Tree Inorder Traversal:")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    inorder(root)
