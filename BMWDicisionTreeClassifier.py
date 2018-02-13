import math

from DecisionTree import DecisionTree


class BMWDecisionTreeClassifier:
    root = DecisionTree()
    data = []
    targets = []
    def __init__(self):
        return self

    def fit(self, data, targets):
        self.data = data
        self.targets = targets
        for data_list, target in zip(data, targets):
            data_list.append(target)
        self.create_tree(self.calculate_next_node(list(range(1,len(self.data)))), self.root, None)

    def create_tree(self, index_list, node, yes_no_unknown):
        if not index_list:
            return
        node.data = self.calculate_next_node(index_list, -1, yes_no_unknown)
        if 'r' not in node.data and 'd' not in node.data and 'u' not in node.data:
            index_list.remove(node.data)
            self.create_tree(index_list, node.left, 'y')
        if 'r' not in node.data and 'd' not in node.data and 'u' not in node.data:
            index_list.remove(node.data)
            self.create_tree(index_list, node.left, '?')
        if 'r' not in node.data and 'd' not in node.data and 'u' not in node.data:
            index_list.remove(node.data)
            self.create_tree(index_list, node.left, 'n')
        return

    def calculate_next_node(self, index_list, last_index, yes_no_unknown):
        lowest_entropy = None
        index_to_return = -1
        for index in index_list:
            if last_index == -1:
                temp_entropy = self.calculate_entropy(self.data[:,index] == 'y',
                                                      self.data[:,index] == 'n',
                                                      self.data[:,index] == '?')
            else:
                temp_entropy, republican, democrat = self.calculate_entropy((self.data[:,index] == 'y')[:,last_index == yes_no_unknown],
                                                      (self.data[:,index] == 'n')[:,last_index == yes_no_unknown],
                                                      (self.data[:,index] == '?')[:,last_index == yes_no_unknown])
            if temp_entropy is 0:
                if republican:
                    return "republican"
                elif democrat:
                    return "democrat"
                else:
                    return "unknown"
            if lowest_entropy == None:
                lowest_entropy = temp_entropy
                index_to_return = index
            elif lowest_entropy > temp_entropy:
                lowest_entropy = temp_entropy
                index_to_return = index
        return index_to_return

    def calculate_entropy(self, yes_data_rows, no_data_rows, unknown_data_rows):
        yes_republican_count, yes_democrat_count = self.republican_democrat_counter(yes_data_rows)
        no_republican_count, no_democrat_count = self.republican_democrat_counter(no_data_rows)
        unknown_republican_count, unknown_democrat_count = self.republican_democrat_counter(unknown_data_rows)

        yes_total_count = yes_democrat_count + yes_republican_count
        no_total_count = no_democrat_count + no_republican_count
        unknown_total_count = unknown_democrat_count + unknown_republican_count
        total_count = yes_total_count + no_total_count + unknown_total_count

        yes_entropy = self.smaller_entropy_calculator(yes_republican_count/(yes_republican_count + yes_democrat_count)) + \
                      self.smaller_entropy_calculator(yes_democrat_count/(yes_republican_count + yes_democrat_count))
        no_entropy = self.smaller_entropy_calculator(no_republican_count/(no_republican_count + no_democrat_count)) + \
                     self.smaller_entropy_calculator(no_democrat_count/(no_republican_count + no_republican_count))
        unknown_entropy = self.smaller_entropy_calculator(unknown_republican_count/(unknown_republican_count + unknown_democrat_count)) + \
                          self.smaller_entropy_calculator(unknown_democrat_count/(unknown_republican_count + unknown_democrat_count))

        total_entropy = (yes_entropy * (yes_total_count/total_count)) + \
               (no_entropy * (no_total_count/total_count)) + \
               (unknown_entropy * (unknown_total_count/total_count))
        if total_entropy is not 0:
            return total_entropy, False, False
        else:
            return 0, (yes_republican_count + no_republican_count + unknown_republican_count) is not 0,
            (yes_democrat_count + no_democrat_count + unknown_republican_count) is not 0






    def smaller_entropy_calculator(self, probability):
        return -(probability * math.log2(probability))

    def republican_democrat_counter(self, data_array):
        republican = 0
        democrat = 0
        for row in data_array:
            if "rep" in row[0]:
                republican += 1
            elif "dem" in row[0]:
                democrat += 1
        return republican, democrat

