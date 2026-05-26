[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/80z-ZS6n)
# Week 12: Monster Hunter Graphs

## Student

Name: Dipesh Chaulagain

Student ID: 2312123

## Summary

This assignment represents monster sighting locations across a city as an undirected graph. Locations like Old Theater, Train Station, and Library Basement are nodes, and the routes between them are edges. I built both a basic adjacency list and a weighted version that stores danger scores. I also wrote functions to summarize the graph, find the most connected location, and sort sighting reports by urgency using a heap. The hardest function was `most_connected_location` because of the tie-breaking rule requiring alphabetical order.

## Approach

- `build_hunter_map`: Used a dictionary to store each location as a key with a list of neighbors. For each edge, added both directions and checked for duplicates before appending.
- `build_weighted_hunter_map`: Same structure but stored danger scores in a nested dictionary. Raised `ValueError` for non-positive scores, and kept the lowest score when the same route appeared more than once.
- `map_summary`: Counted dictionary keys for locations. Summed all neighbor list lengths and divided by 2 to avoid double-counting undirected edges.
- `most_connected_location`: Sorted keys alphabetically first, then used `max` with neighbor count as the key — this ensures alphabetical order wins on ties.
- `priority_hunt_order`: Pushed all `(priority, location)` tuples into a `heapq` min-heap. Since tuples compare element by element, ties on priority automatically sort alphabetically by location name.

## Complexity

### `build_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why: We loop over each edge once. The graph stores every vertex and every edge in both directions.

### `build_weighted_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why: Same as above — one pass over edges, storing each connection twice.

### `map_summary`

- Time: O(V + E)
- Space: O(1)
- Why: We visit every key and every neighbor list once to sum lengths. No extra data structures needed.

### `most_connected_location`

- Time: O(V log V)
- Space: O(1)
- Why: Sorting the keys takes O(V log V), then `max` does a single O(V) pass over them.

### `priority_hunt_order`

- Time: O(N log N)
- Space: O(N)
- Why: Each `heappush` and `heappop` is O(log N), done N times. The heap holds all N reports.

## Edge-Case Checklist

- [x] Empty graph
- [x] One route
- [x] Duplicate routes
- [x] Disconnected locations
- [x] Tie for most connected location
- [x] Positive weighted routes
- [x] Invalid zero or negative danger score
- [x] Empty priority report list

## Tests

```bash
python -m pytest -q
```

Result:

```text
16 passed in 0.02s
```

## Assistance & Sources

AI used? Yes

If yes, what did it help with?

- Explaining what adjacency lists and graphs are
- Guidance on how heapq works for priority ordering
- Setting up the project and running pytest

Other sources used:

- Python docs: https://docs.python.org/3/library/heapq.html