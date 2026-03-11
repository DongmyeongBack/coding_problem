import sys
input = sys.stdin.readline

N = int(input())

tree = [['.', '.'] for _ in range(N)]

for _ in range(N):
  ordA = ord('A')

  node, left, right = map(str, input().split())

  tree[ord(node)-ordA][0] = ord(left)-ordA 
  tree[ord(node)-ordA][1] = ord(right)-ordA 

answers = [[],[],[]]
def preorder(now):
  if now < 0:
    return

  answers[0].append(chr(now+ordA))
  preorder(tree[now][0])
  preorder(tree[now][1])

def inorder(now):
  if now < 0:
    return

  inorder(tree[now][0])
  answers[1].append(chr(now+ordA))
  inorder(tree[now][1])

def postorder(now):
  if now < 0:
    return

  postorder(tree[now][0])
  postorder(tree[now][1])
  answers[2].append(chr(now+ordA))

preorder(0)
inorder(0)
postorder(0)

for answer in answers:
  print(''.join(answer))