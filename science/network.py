class Node(object):
    def __init__(self, node_index, security_level, connected_list):
        self.node_index = node_index
        self.security_level = security_level if node_index != 0 else 0
        self.reached = False if node_index != 0 else True
        self.infected = False if node_index != 0 else True
        self.connected_list = connected_list

    def reaching(self):
        self.reached = True

    def attacked(self):
        if not self.infected:
            self.security_level -= 1
            if self.security_level == 0:
                self.infected = True


def iter_node(matrix):
    node_index = 0
    for row in matrix:
        security_level = row[node_index]
        connected_list = [i for i, x in enumerate(row) if i != node_index and x == 1]
        node = Node(node_index, security_level, connected_list)
        node_index += 1
        yield node


def reach(nodes):
    for node in nodes:
        if node.infected:
            for i in node.connected_list:
                nodes[i].reaching()


def attack(nodes):
    for node in nodes:
        node.attacked()


def capture(matrix):
    nodes = [x for x in iter_node(matrix)]
    time = 0
    while True:
        reach(nodes)
        attack(n for n in nodes if n.reached)
        time += 1
        if all(n.infected for n in nodes):
            return time


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
