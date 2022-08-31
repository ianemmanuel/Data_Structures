class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children  = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        prefix = ' ' * self.get_level() *3
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root = TreeNode('Electronics')
    laptops = TreeNode('Laptops')
    laptops.add_child(TreeNode('HP'))
    laptops.add_child(TreeNode('Dell'))
    laptops.add_child(TreeNode('Mac'))
    laptops.add_child(TreeNode('Lenovo'))

    TV = TreeNode('TV')
    TV.add_child(TreeNode('LG'))
    TV.add_child(TreeNode('Sony'))
    TV.add_child(TreeNode('SamSung'))
    
    phones = TreeNode('Phones')
    phones.add_child(TreeNode('SamSung'))
    phones.add_child(TreeNode('Tecno'))
    phones.add_child(TreeNode('Iphone'))

    root.add_child(laptops)
    root.add_child(TV)
    root.add_child(phones)

    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree()