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

def get_siblings(graph, node):
    return [k for k, v in graph.items() if v["parent"] == graph[node]["parent"] and k != node]

def count_parents(node, graph):
    count = 0
    while graph[node]["parent"]:
        count += 1
        node = graph[node]["parent"]
    return count

def count_indirect_children(graph, children):
    count = 0
    for child in children:
        count += 1
        count += count_indirect_children(graph, graph[child]["children"])
    return count

def calculate_relations(graph):
    relations = [[0] * len(graph) for _ in range(5)]
    
    for node, data in graph.items():
        idx = int(node) - 1
        relations[0][idx] = 1 if data["parent"] else 0
        relations[1][idx] = len(data["children"])
        relations[2][idx] = count_parents(node, graph) - 1 if data["parent"] else 0
        relations[3][idx] = sum(count_indirect_children(graph, graph[x]["children"]) for x in data["children"])
        relations[4][idx] = len(get_siblings(graph, node))
        
    for row in relations:
        print(row)

def main(json_str):
    calculate_relations(json_to_tree(json_str))


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
}'''

main(test_string)
