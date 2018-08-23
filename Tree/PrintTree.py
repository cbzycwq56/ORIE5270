

class Tree(object):

    def __init__(self, root):
        self.root = root

    # get root value
    def get_value_root(self):
        if self.root is not None:
            return self.root.value
        else:
            return None

    # get the 2d list to be printed
    def store_tree_improve(self):
        array = []
        space = "|"
        if self is not None:
            # get left and right tree
            if self.root.left is not None:
                array_left = Tree(self.root.left).store_tree_improve()
            else:
                array_left = [['N']]
            if self.root.right is not None:
                array_right = Tree(self.root.right).store_tree_improve()
            else:
                array_right = [['N']]
            # make left right symmetric
            if len(array_right) < len(array_left):
                temp = [[space for j in range(len(array_left[0]))]
                        for i in range(len(array_left))]
                flat_array_right = [[] for i in range(len(array_right))]
                for i in range(len(array_right)):
                    counter = 0
                    for j in range(len(array_right[0])):
                        if array_right[i][j] != space:
                            flat_array_right[i].append(array_right[i][j])
                    for j in range(len(array_left[0])):
                        if array_left[i][j] != space:
                            temp[i][j] = flat_array_right[i][counter]
                            counter += 1
                array_right = temp

            if len(array_left) < len(array_right):
                temp = [[space for j in range(len(array_right[0]))]
                        for i in range(len(array_right))]

                flat_array_left = [[] for i in range(len(array_left))]
                for i in range(len(array_left)):
                    counter = 0
                    for j in range(len(array_left[0])):
                        if array_left[i][j] != space:
                            flat_array_left[i].append(array_left[i][j])
                    for j in range(len(array_right[0])):
                        if array_right[i][j] != space:
                            temp[i][j] = flat_array_left[i][counter]
                            counter += 1
                array_left = temp
            # merge left and right

            array = array_left
            for i in range(len(array_right)):
                for j in range(len(array_right[0])):
                    array[i].append(array_right[i][j])

            if len(array[0]) % 2 == 0:
                for i in range(len(array)):
                    array[i].insert(len(array[0]) / 2, space)
            array.insert(0, [])
            for i in range(len(array[1])):
                array[0].append(space)
            array[0][len(array[1]) / 2] = self.get_value_root()

        else:
            array = [["N"]]
        return array

    # print out the 2d list
    def get_tree(self):
        matrix = self.store_tree_improve()
        temp = [["|" for j in range(len(matrix[0])-2)] for i in range(len(matrix)-1)]
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                temp[i][j] = matrix[i][j+1]
        temp1 = [[] for i in range(len(temp))]
        for i in range(len(temp)):
            for j in range(len(temp[0]) / 2 + 1):
                if temp[i][j*2] == "N":
                    temp1[i].append("|")
                else:
                    temp1[i].append(temp[i][j * 2])
        matrix = temp1
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print '\n'.join(table)
        return matrix


# The Node Class
class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
