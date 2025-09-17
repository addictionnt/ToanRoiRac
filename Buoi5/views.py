from flask import Blueprint, render_template, request, current_app, redirect, url_for
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64

views = Blueprint('views', __name__)

node = ["a", "b", "c", "d", "e", "f", "g", "h"]

edge = [("a", "b"), ("a", "c"), ("a", "e"), ("b", "d"), ("b", "f"), ("c", "d"), ("c", "f"), ("c", "g"), ("d", "e"), ("d", "h"), ("e", "f"), ("e", "g"), ("f", "h"), ("g", "h")]

Ga = nx.Graph()
Gb = nx.DiGraph()
Ga.add_nodes_from(node)
Gb.add_nodes_from(node)
Ga.add_edges_from(edge)
Gb.add_edges_from(edge)

pos = {
    "a": (0, 4),
    "b": (4, 4),
    "c": (1, 3),
    "d": (3, 3),
    "e": (1, 1),
    "f": (3, 1),
    "g": (0, 0),
    "h": (4, 0)
}
nx.draw(Ga, pos , with_labels=True)
bufa = io.BytesIO()
plt.savefig(bufa, format='png')
bufa.seek(0)
nx.draw(Gb, pos , with_labels=True)
bufb = io.BytesIO()
plt.savefig(bufb, format='png')
bufb.seek(0)
plt.close()

#hàm bậc và đỉnh kề
def get_node_details(graph, start_node):
    if start_node not in graph.nodes:
        return {}

    levels = {node: -1 for node in graph.nodes}
    levels[start_node] = 0
    queue = [(start_node, 0)]
    
    head = 0
    while head < len(queue):
        current_node, level = queue[head]
        head += 1
        for neighbor in graph.neighbors(current_node):
            if levels[neighbor] == -1:
                levels[neighbor] = level + 1
                queue.append((neighbor, level + 1))
    
    node_details = {}
    for n in graph.nodes:
        node_details[n] = {
            'level': levels[n],
            'degree': graph.degree(n),  
            'neighbors': list(graph.neighbors(n))
        }
    
    return node_details

def check_connetted(graph):
    if nx.is_connected(graph):
        tb = "Liên thông"
    else:
        tb = "Không liên thông"
    return tb

def check_connettedb(graph):
    if nx.is_strongly_connected:
        tb = "Liên thông mạnh"
    else:
        tb = "Liên thông yếu"
    return tb

# Mã hóa hình ảnh thành chuỗi Base64
image_a = base64.b64encode(bufa.getvalue()).decode('utf-8')
image_b = base64.b64encode(bufb.getvalue()).decode('utf-8')



@views.route("/")
def index():
    return render_template("trangchu.html", image_a = image_a, image_b = image_b)
    
@views.route("/a")
def dothiGa():
    start_node = "a"
    connected_status = check_connetted(Ga)
    all_node_details = get_node_details(Ga, start_node)
    return render_template("dothiGa.html",
                           image_a = image_a,
                           all_node_details=all_node_details, 
                           start_node=start_node,
                           connected_status=connected_status)
    
@views.route("/b")
def dothiGb():
    start_node = "a"
    connected_statusb = check_connettedb(Gb)
    all_node_detailsb = get_node_details(Gb, start_node)
    return render_template("dothiGb.html",
                           image_b = image_b,
                           all_node_detailsb=all_node_detailsb, 
                           start_node=start_node,
                           connected_statusb=connected_statusb)