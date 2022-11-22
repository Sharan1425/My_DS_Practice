#Get the Levels

class Treenode:
    def __init__(self,data):
        self.data = data
        self.childs = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level

    def add_child(self,child):
        child.parent = self
        self.childs.append(child)

    def print_tree_bylevels(self,level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() *3
        prefix = spaces + '|--' if self.parent else ""
        print(prefix + self.data)
        for child in self.childs:
            child.print_tree_bylevels(level)


def helper_method():
    root = Treenode("Technologies")
    BE = Treenode("BackEnd")
    BE.add_child(Treenode("Python"))
    BE.add_child(Treenode("Ruby"))
    BE.add_child(Treenode("Java"))
    root.add_child(BE)
    FE = Treenode("FrontEnd")
    FE.add_child(Treenode("JavaScripts"))
    FE.add_child(Treenode("HTML"))
    FE.add_child(Treenode("CSS"))
    FE.add_child(Treenode("JQuery"))
    root.add_child(FE)
    FW = Treenode("FrameWork")
    FW.add_child(Treenode("Django"))
    FW.add_child(Treenode("Flask"))
    FW.add_child(Treenode(".Net"))
    root.add_child(FW)

    return root

data = helper_method()
data.print_tree_bylevels(5)
