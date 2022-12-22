"""
Created By Jivansh Sharma 
December 2022
@parzuko
"""

from models import MetroGraph

# Global Graph Object
kamui_graph = MetroGraph()
kamui_graph.populate_graph()

def style_shortest_path(shortest_path):
    styled_shortest_path = []
    for station in shortest_path:
        pretty_station = f"{station.capitalize()} {kamui_graph.get_station_line(station)}"
        styled_shortest_path.append(pretty_station)
    
    return styled_shortest_path

def main():
    source = "Jahangirpuri"
    destination = "Noida City Centre"

    while True:
        source = input("Enter the source station: ").lower()
        destination = input("Enter the destination station: ").lower()
        shortest_path, duration = kamui_graph.get_shortest_path(source, destination)

        if shortest_path == [] and duration == 0:
            print("There was a disconnect between the source and destination stations. Please try again.")
            continue

        styled_shortest_path = style_shortest_path(shortest_path)

        print(f"The shortest path from {source.capitalize()} to {destination.capitalize()} is:\n")
        print(" → ".join(styled_shortest_path))
        print(f"\nThis route will take {int(duration)} minutes!")
        break

if __name__ == "__main__":
    main()