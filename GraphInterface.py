import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from NltkExample import NLTKSteps


def create_networkx_graph(sentenceData, labelData):
    G = nx.DiGraph()

    graphData = []

    for i in range(len(sentenceData)):
        for j in range(len(sentenceData)):
            if j == i:
                continue
            else:
                graphData.append((sentenceData[i], sentenceData[j]))

    G.add_edges_from(graphData)

    # Create a Tkinter window
    root = tk.Tk()
    root.title("NetworkX Graph")

    # Create a Matplotlib figure
    fig = plt.figure(figsize=(10, 10))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    # Draw the NetworkX graph on the Matplotlib figure
    pos = nx.circular_layout(G)

    node_labels = {
        node: node[:18] + "\n" + node[18:] if len(node) > 18 else node
        for node in G.nodes
    }
    node_sizes = [7500 for _ in G.nodes]

    nx.draw(
        G,
        pos,
        with_labels=True,
        labels=node_labels,
        node_color="#8D9EFF",
        edge_color="gray",
        font_size=8,
        node_size=node_sizes,
        arrowsize=20,
        alpha=0.7,
    )

    # u ve v başlangıç ve bitiş düğümleri,
    # x ve y iki düğümün orta noktası
    rectangles = []

    for u, v, d in G.edges(data=True):
        x = (pos[u][0] + pos[v][0]) / 2
        y = (pos[u][1] + pos[v][1]) / 2

        rect = plt.Rectangle(
            (x - 0.1, y - 0.05),
            0.2,
            0.1,
            facecolor=(250 / 255, 217 / 255, 213 / 255),
            edgecolor=(213 / 255, 155 / 255, 147 / 255),
        )
        rectangles.append(rect)

    for rect in rectangles:
        plt.gca().add_patch(rect)

    for u, v, d in G.edges(data=True):
        x = (pos[u][0] + pos[v][0]) / 2
        y = (pos[u][1] + pos[v][1]) / 2

        if (u, v) in labelData:
            label = labelData[(u, v)]
            max_chars_per_line = 10
            lines = [
                label[i : i + max_chars_per_line]
                for i in range(0, len(label), max_chars_per_line)
            ]
            labelText = "\n".join(lines)

            plt.text(
                x,
                y,
                labelText,
                ha="center",
                va="center",
                fontsize=8,
                multialignment="center",
            )
            print(label)

    text = f"Cümle benzerliği threshold değeri:"
    font = {"family": "serif", "weight": "normal", "size": 8, "color": "magenta"}

    label = plt.text(x + 0.6, y + 1.87, text, fontdict=font)
    plt.gca().add_artist(label)
    rect = plt.Rectangle(
        (x + 1.1, y + 1.85),
        0.1,
        0.05,
        facecolor=(255 / 255, 242 / 255, 204 / 255),
        edgecolor=(230 / 255, 206 / 255, 134 / 255),
    )
    plt.gca().add_patch(rect)

    canvas.draw()
    # Start the Tkinter event loop
    root.mainloop()


labelData = {}
sentenceData = ["merhaba ben ilkay", "sinemi seviyorum", "yemek pişirmeyi seviyorum"]

# Create and display the NetworkX graph in Tkinter
# create_networkx_graph(sentenceData, labelData)
