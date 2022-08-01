class TreeNode:

    right = None
    left = None

    def __init__(self, val):
        self.val = val


def mergeTrees(t1, t2):
    """
    Create a new tree
    DFS (?) through the old two trees
    base case:
        no nodes at all: just return None
        just one node: create a node with that value and return it

    keep track of where one tree left off and check if you've caught up to it
        but how do you know if you've caught up to it?
        just a special thing on the stack with a boolean flag??

    create a stack for each old tree and one for the new tree
    for the new tree, create the new nodes for the children, then put on the stack
    put all the roots on the stack
    tree1 = True
    tree2 = True
    while at least one of the old stacks:
        if tree1 and tree2:
            pop something from each stack
            # if the thing from the stack is an X:
            #     this should never happen if both trees are operational
            if node.right (then node.left) from both trees, create a new node for the new tree with the sum of the values
                push this new node to the new tree's stack and push the old node.rights to the stacks for the old tree
            elif node.right (or node.left) only for tree_i:
                create a new node for the new tree with only the existing value
                push this new node to the stack for the new tree
                set tree_j to False
                push X to the stack for tree_i
                push node.right (or node.left) to the stack for tree_i
        if only tree1 or tree2:
            
        if neither tree:
            this should never happen o____o
    """
