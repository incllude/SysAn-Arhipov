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


def pprint_metadata(tree):

    for node, info in tree.items():
        print(f"Вершина: {node}; Родитель: {info['parent']}; Дети: {info['children']}; Сиблинги: {list(filter(lambda x: tree[x]['parent'] == info['parent'] and x != node, tree))}")


def main(json_string):

    tree = json.loads(json_string)
    metadata = convert_json(tree)
    pprint_metadata(metadata)


# with open("tree.json", "r") as file:
#     tree = json.load(file)

# metadata = convert_json(tree)
# pprint_metadata(metadata)
