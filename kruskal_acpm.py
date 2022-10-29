#create a tree class which associate a parent to a node
class TreeNode:
    def __init__(self, node: int, parent = None):
        self.node = node
        self.parent = parent

#in a tree of node, return the parent at the root or if the node doesn't have parent return itself
def find(node: TreeNode):
    if node.parent == None:
        return node
    else: return find(node.parent)

#merge trees of node_u and node_v from an edge
def union(tree_node_u: TreeNode, tree_node_v: TreeNode):
    node_u_root = find(tree_node_u)
    node_v_root = find(tree_node_v)
    if node_u_root != node_v_root:
        node_u_root.parent = node_v_root

#use a dico to proceed kruskal algorithm that returns the ACPM of a graph
def kruskal(dico):
    #create the ACPM, his weight and the individual trees of all nodes in the graph
    ACPM: list[tuple] = []
    ACPM_total_weight: int = 0
    tree_nodes: list = []

    #initialize all the trees for all nodes in the graph
    for key in dico:
        tree_nodes.append(TreeNode(key))
    
    #create temp trees to complete the initialization for special case in the graph
    temp_tree_key: TreeNode | None = None
    temp_tree_inner_key: TreeNode | None = None

    #merge tree node of the same station name
    for key, value in dico.items():
        for inner_key, inner_value in value.items():
            #in the data structure, case where there is a transition inside the same station
            if inner_value == 180 or inner_value == 240 or inner_value == 300:
                #take the tree of key and inner_key from the tree_node list
                for tree_node in tree_nodes:
                    if key == tree_node.node:
                        temp_tree_key = tree_node
                    elif inner_key == tree_node.node:
                        temp_tree_inner_key = tree_node
                union(temp_tree_key, temp_tree_inner_key)

    #create list to sort edges by weight
    already_processed: list[tuple] = []
    weighted_edges: list[tuple] = []

    #create edges (u, v, w) of the graph with the dico data structure
    for key, value in dico.items():
        for inner_key, inner_value in value.items():
            edge_A_to_B = (key, inner_key)
            edge_B_to_A = (inner_key, key)

            if edge_A_to_B not in already_processed and edge_B_to_A not in already_processed:
                #add in list to not create a same edge twice
                already_processed.append(edge_A_to_B)
                already_processed.append(edge_B_to_A)

                #trivial case doesn't take transitions inside a same station (no use of that)
                if inner_value != 180 and inner_value != 240 and inner_value != 300: #in the data structure, case where there is a transition inside the same station
                    weighted_edges.append((edge_A_to_B[0], edge_A_to_B[1], inner_value))

    #sort edges by weight
    weighted_edges.sort(key = lambda y: y[2])

    #complete the ACPM
    for edge in weighted_edges:
        #extract node_u and node_v form the edge in weighted edges
        node_u: int = edge[0]
        node_v: int = edge[1]
        tree_node_u: TreeNode | None = None
        tree_node_v: TreeNode | None = None

        #take the tree of node_u and node_v from the tree_node list
        for tree_node in tree_nodes:
            if node_u == tree_node.node:
                tree_node_u = tree_node
            elif node_v == tree_node.node:
                tree_node_v = tree_node
        
        #control if trees exist
        assert(isinstance(tree_node_u, TreeNode))
        assert(isinstance(tree_node_v, TreeNode))

        #add edge to ACPM list if both trees don't have same parent at their root
        if find(tree_node_u) != find(tree_node_v):
            ACPM.append(edge)
            ACPM_total_weight = ACPM_total_weight + edge[2]
            union(tree_node_u, tree_node_v)

    print('Weight of the ACPM :', ACPM_total_weight)
    return ACPM