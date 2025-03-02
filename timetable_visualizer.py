import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors

def visualize_timetable(professors, offices, hours, schedule):
    data = []
    for office in range(offices):
        for hour in range(hours):
            assigned_profs = [prof for prof in range(professors) if schedule[office, prof, hour] == 1]
            for professor in assigned_profs:
                data.append([professor + 1, hour + 1, office + 1])
    
    df = pd.DataFrame(data, columns=["Professor", "Hour", "Office"])
    pivot_df = df.pivot(index="Professor", columns="Hour", values="Office").fillna(0)
    
    cmap = mcolors.ListedColormap(['gray', 'red', 'blue', 'green', 'purple', 'orange'])
    bounds = list(range(offices + 2))
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    
    fig, ax = plt.subplots(figsize=(15, professors * 0.6))
    im = ax.imshow(pivot_df, cmap=cmap, norm=norm, aspect='auto', extent=[0.5, hours + 0.5, 0.5, professors + 0.5])
    
    for i in range(professors):
        for j in range(hours):
            ax.add_patch(plt.Rectangle((j + 0.5, i + 0.5), 1, 1, fill=False, edgecolor='black', linewidth=1))
    
    cbar = plt.colorbar(im, label='Office')
    cbar.set_ticks(range(offices + 1))
    cbar.set_ticklabels(["No Office"] + [f"Office {i + 1}" for i in range(offices)])
    
    ax.set_xticks(np.arange(1, hours + 1))
    ax.set_xticklabels([str(i) for i in range(1, hours + 1)], ha='center')
    ax.set_yticks(np.arange(1, professors + 1))
    ax.set_yticklabels([f'Professor {i}' for i in range(1, professors + 1)], va='center')
    
    ax.set_xlabel("Hour")
    ax.set_ylabel("Professor")
    ax.set_title("Professors Timetable")
    
    plt.show()

professors = 5
offices = 2
hours = 8
schedule = np.zeros((offices, professors, hours), dtype=int)

data_entries = [
    (1, 1, 1, 0), (1, 1, 2, 0), (1, 1, 3, 0), (1, 1, 4, 1), (1, 1, 5, 1), (1, 1, 6, 1), (1, 1, 7, 1), (1, 1, 8, 1),
    (1, 2, 1, 0), (1, 2, 2, 0), (1, 2, 3, 0), (1, 2, 4, 0), (1, 2, 5, 0), (1, 2, 6, 0), (1, 2, 7, 0), (1, 2, 8, 0),
    (1, 3, 1, 0), (1, 3, 2, 0), (1, 3, 3, 0), (1, 3, 4, 0), (1, 3, 5, 0), (1, 3, 6, 0), (1, 3, 7, 0), (1, 3, 8, 0),
    (1, 4, 1, 1), (1, 4, 2, 1), (1, 4, 3, 1), (1, 4, 4, 0), (1, 4, 5, 0), (1, 4, 6, 0), (1, 4, 7, 0), (1, 4, 8, 0),
    (1, 5, 1, 0), (1, 5, 2, 0), (1, 5, 3, 0), (1, 5, 4, 1), (1, 5, 5, 1), (1, 5, 6, 1), (1, 5, 7, 1), (1, 5, 8, 1),
    (2, 1, 1, 0), (2, 1, 2, 0), (2, 1, 3, 0), (2, 1, 4, 0), (2, 1, 5, 0), (2, 1, 6, 0), (2, 1, 7, 0), (2, 1, 8, 0),
    (2, 2, 1, 0), (2, 2, 2, 0), (2, 2, 3, 1), (2, 2, 4, 1), (2, 2, 5, 1), (2, 2, 6, 1), (2, 2, 7, 1), (2, 2, 8, 1),
    (2, 3, 1, 1), (2, 3, 2, 1), (2, 3, 3, 1), (2, 3, 4, 1), (2, 3, 5, 1), (2, 3, 6, 1), (2, 3, 7, 0), (2, 3, 8, 0),
    (2, 4, 1, 0), (2, 4, 2, 0), (2, 4, 3, 0), (2, 4, 4, 0), (2, 4, 5, 0), (2, 4, 6, 0), (2, 4, 7, 1), (2, 4, 8, 1),
    (2, 5, 1, 0), (2, 5, 2, 0), (2, 5, 3, 0), (2, 5, 4, 0), (2, 5, 5, 0), (2, 5, 6, 0), (2, 5, 7, 0), (2, 5, 8, 0)
]

for office, professor, hour, value in data_entries:
    schedule[office-1, professor-1, hour-1] = value

visualize_timetable(professors, offices, hours, schedule)
