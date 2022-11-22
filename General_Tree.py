# Implementation of General Tree

# object of the Tree
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.childs = []
        self.parent = None
    

    #method to return the level of the tree
    def level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

    #method with adds a child to the parent node
    def add_child(self,child):
        child.parent = self
        self.childs.append(child)

    #method to print the data
    def print_tree(self):
        spaces = ' ' * self.level() * 3
        prefix = spaces + '|--' if self.parent else ""
        print(prefix + self.data)
        for child in self.childs:
            child.print_tree()
    
# Creating an object
root = TreeNode("Narayana Swammy Thatha")

sibiling1 = TreeNode("Govindamma")
damu = TreeNode("Damu")
damu.add_child(TreeNode("Nishanth"))
sibiling1.add_child(damu)
mona = TreeNode("Mona")
mona.add_child(TreeNode("Vetri"))
sibiling1.add_child(mona)
dini = TreeNode("Dini")
dini.add_child(TreeNode("Vishnu"))
sibiling1.add_child(dini)

sibiling2 = TreeNode("Kanthaamma")
sibiling2.add_child(TreeNode("Anil"))
sibiling2.add_child(TreeNode("Devi"))
sibiling2.add_child(TreeNode("Sharan"))

sibiling3 = TreeNode("Navneetha")
sibiling3.add_child(TreeNode("Chinntu"))
sibiling3.add_child(TreeNode("Manu"))

root.add_child(sibiling1)
root.add_child(sibiling2)
root.add_child(sibiling3)

root.print_tree()
