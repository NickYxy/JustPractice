__author__ = 'nickyuan'

class SimpleItemContainer(object):
    def __init__(self, id, item_container):
        self.id = id
        self.data = {}
        for item in item_container:
            self.data[item.id] = item

containerA = SimpleItemContainer(2,['a','b','c'])
print(containerA)