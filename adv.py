from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world hh
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# total_rooms = 500

# for room backtracking
reverse = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

def traverse(room, visited=None):
    """
    recursive depth-first traversal function
    """
    path = []
    room = player.current_room

    # create the set to store visited nodes/rooms
    if visited is None:
        visited = set()

    # check possible exit directions from current room
    for direction in room.get_exits():
        player.travel(direction)
        room = player.current_room

        # if room has already been visited, backtrack
        if room in visited:
            player.travel(reverse[direction])

        # if room hasn't been visted before,
        else:
            # add room to visited dict
            visited.add(room)
            # append direction to path dicts
            path.append(direction)

            # recursively call fxn again on this room and append to path
            path = path + traverse(room, visited)
            player.travel(reverse[direction])
            path.append(reverse[direction])

    return path


traversal_path = traverse(player.current_room)
### TESTS PASSED: 1000 moves, 500 rooms visited

# print(f"Starting room:{world.starting_room}")

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
