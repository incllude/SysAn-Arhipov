from pprint import pprint
import json


def tree_descendent(tree, output, parent):

    for node, childs in tree.items():
        node = int(node)
        output[node] = {"parent": parent, "children": tree_descendent(childs, output, node)}

    return list(map(int, tree.keys()))


def convert_json(tree):

    output = {}
    tree_descendent(tree, output, None)
    return output


def get_siblings(tree, node):
    return list(filter(lambda x: tree[x]['parent'] == tree[node]['parent'] and x != node, tree))


def calc_upper(tree, key):
    if tree[key]['parent'] is None:
        return 0
    return calc_upper(tree, tree[key]['parent']) + 1

        
def calc_under(tree, node):
    if len(tree[node]["children"]) == 0:
        return 1
    return 1 + sum(calc_under(tree, child) for child in tree[node]["children"])


def calc_matrix(tree):

    matrix = {node: [0 for _ in range(5)] for node in sorted(tree.keys())}

    for node, info in tree.items():
        siblings = get_siblings(tree, node)

        matrix[node][0] = 1 if info["parent"] is not None else 0
        matrix[node][1] = len(info["children"])
        matrix[node][2] = calc_upper(tree, node) + len(get_siblings(tree, info["parent"])) - 1 if info["parent"] is not None else 0
        matrix[node][3] = sum(calc_under(tree, child) for child in info["children"]) - len(info["children"])
        matrix[node][3] += sum(calc_under(tree, sibling) for sibling in siblings) - len(siblings)
        matrix[node][4] = len(siblings)
    
    return matrix


def main(json_string):

    tree = json.loads(json_string)
    metadata = convert_json(tree)
    matrix = calc_matrix(metadata)
    
    for node in matrix:
        print(matrix[node])


# with open("tree.json", "r") as file:
#     tree = json.load(file)

# metadata = convert_json(tree)
# matrix = calc_matrix(metadata)

# for node in matrix:
#     print(matrix[node])

