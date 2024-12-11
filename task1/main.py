import json


def make_node(parent, children):
    return {"parent": parent, "children": children}

def build_tree(parent, data, graph):
    children = list(data.keys())
    for key, value in data.items():
        graph[key] = make_node(parent, build_tree(key, value, graph) if value else [])
    return children

def json_to_tree(json_string):
    graph = {}
    build_tree(None, json.loads(json_string), graph)
    return graph

def print_tree(graph):
    for node, data in graph.items():
        siblings = [k for k, v in graph.items() if v["parent"] == data["parent"] and k != node]
        print(f"Вершина: {node}")
        print(f"    Сиблинги: {siblings}")
        print(f"    Дети:     {data['children']}")

def main(json_str):
    print_tree(json_to_tree(json_str))


test_string = '''{
    "1": {
        "2": {
            "3": {
                "5": {},
                "6": {}
            },
            "4": {
                "7": {},
                "8": {}
            }
        }
    }
}
'''
main(test_string)
