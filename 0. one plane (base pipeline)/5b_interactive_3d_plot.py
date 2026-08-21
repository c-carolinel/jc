import json
import numpy as np
import pandas as pd
from pathlib import Path
import plotly.express as px

# File path
OUT_3D = Path('figures/interactive_3d/')
OUT_3D.mkdir(exist_ok=True)

# Load partition files
partition_names = ['louvain', 'greedy', 'greedy_bestn', 'hybrid_optimized', 'qpu_optimized']
method_labels   = ['Louvain', 'Greedy', 'Greedy (best_n)', 'Hybrid', 'QPU']

partitions = {}
for name, label in zip(partition_names, method_labels):
    path = Path(f'partitions/partition_{name}.json')
    with open(path) as f:
        partitions[label] = np.array(json.load(f))
    print(f'Loaded {label}: {len(np.unique(partitions[label]))} communities')

# List of non-pruned neurons
neurons = ["3","5","6","7","10","12","13","14","15","17","19",
           "21","26","27",
           "30","32","33","34","35","36","37",
           "41","42","43","45","47","48",
           "50","51","52","57","58",
           "61","66",
           "70","72","76",
           "84","85","87","88",
           "90","93","94","95","97","99",
           "102","104","106",
           "111","113","114","115","118",
           "120","126","128",
           "133","139",
           "140","142","144","148","149",
           "150","153","154","156","158",
           "163","164","165","166","167","168","169"]

# Load location data
locations = pd.read_csv('neuron_locations.csv', header=None, names=['x', 'y', 'z'])

partition_temp = {}
for name, label in zip(partition_names, method_labels):    
    # Read the file content as a string
    partition_json = Path(f'partitions/partition_{name}.json')
    jsonStr = partition_json.read_text()
    partition_temp = np.array(json.loads(jsonStr))

    # Adding pruned neurons to partition
    communities = np.zeros(172)

    for p in range(len(partition_temp)):
        idx = int(neurons[p])
        communities[idx] = partition_temp[p] + 1

    locations_communities = locations.copy()
    locations_communities['communities'] = communities
    locations_communities['communities'] = locations_communities['communities'].astype(str)

    fig = px.scatter_3d(locations_communities, x='x', y='y', z='z', color='communities')
    fig.show()
    fig.write_html(OUT_3D / f'interactive_3d_{name}.html')