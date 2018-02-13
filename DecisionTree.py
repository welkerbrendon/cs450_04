class DecisionTree(object):
    left = None
    right = None
    middle = None
    data = None
    def __init__(self):
        self.left = DecisionTree()
        self.right = DecisionTree()
        self.middle = DecisionTree()
        return self