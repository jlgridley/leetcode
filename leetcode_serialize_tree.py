#!/usr/bin/env python3

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:


    def print_tree(self, root):
        queue = [root]
        for node in queue:
            print(node.val, ":", end=" ")
            if node.left:
                print(node.left.val, end=", ")
                queue.append(node.left)
            else:
                print("None", end=", ")
            if node.right:
                print(node.right.val)
                queue.append(node.right)
            else:
                print("None")

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        serialized_tree = ""
        queue = [root]
        hm = {}  # keep a hashmap of nodes to IDs
        hm[root] = str(1)
        id = 2
        for node in queue:
            serialized_tree += str(hm[node]) + ',' + str(node.val)
            if node.left:
                queue.append(node.left)
                serialized_tree += ',' + str(id) + ','
                hm[node.left] = str(id)
                id += 1
                if node.right:
                    queue.append(node.right)
                    serialized_tree += str(id)
                    hm[node.right] = str(id)
                    id += 1
                else:
                    serialized_tree += 'N'
            elif node.right:
                queue.append(node.right)
                hm[node.right] = str(id)
                serialized_tree += ',N,' + str(id)
                id += 1
            serialized_tree += '/'
        return serialized_tree[:-1]

        # Do BFS and concatenate a string with the serialized data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == None or data == "":
            return None
        nodes = data.split('/')
        if len(nodes) == 0:
            return None
        hm = {} # Create all the nodes and add to a hashmap indexed by their IDs (effectively an adjacency list)
        for node in nodes:
            curr = node.split(',')
            if len(curr) == 2:
                id, val = curr
                hm[id] = (TreeNode(int(val)), [])
            elif len(curr) == 4:
                id, val, left, right = curr
                hm[id] = (TreeNode(int(val)), [left, right])
            else:
                assert False, "Invalid serialization"
        # go through the items in the hashmap and connect all the nodes
        root = hm['1'][0]
        for id, info in hm.items():
            node, children = info
            if children:
                l, r = children
                if l != 'N':
                    node.left = hm[l][0]
                if r != 'N':
                    node.right = hm[r][0]
        return root

# Your Codec object will be instantiated and called as such:
codec = Codec()
# Serialized format: ID,val,leftID (if any),rightID (if any)/...
serialized_tree = "1,1,2,3/2,2/3,3,4,5/4,4/5,5"
root = TreeNode(1)
child = TreeNode(2)
root.left = child
print(codec.serialize(root))
# (codec.deserialize(serialized_tree))

# codec.deserialize(codec.serialize(root))
