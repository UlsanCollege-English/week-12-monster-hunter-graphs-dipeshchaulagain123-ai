"""Week 12: Monster Hunter Graphs.

Complete each function using Python 3.11+.

Rules:
- Standard library only.
- Use type hints.
- Keep public function docstrings.
- Run tests with: pytest -q
"""

"""Week 12: Monster Hunter Graphs."""

import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Build an undirected adjacency list from route pairs."""
    graph = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        if b not in graph[a]:
            graph[a].append(b)
        if a not in graph[b]:
            graph[b].append(a)
    return graph


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """Build an undirected weighted graph from route triples."""
    graph = {}
    for a, b, score in edges:
        if score <= 0:
            raise ValueError(f"Danger score must be positive, got {score}")
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        # Keep the lowest score if the route appears more than once
        if b not in graph[a] or score < graph[a][b]:
            graph[a][b] = score
            graph[b][a] = score
    return graph


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """Return the number of locations and undirected routes."""
    locations = len(graph)
    # Each edge is stored twice (both directions), so divide total by 2
    routes = sum(len(neighbors) for neighbors in graph.values()) // 2
    return {"locations": locations, "routes": routes}


def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """Return the location with the most neighbors."""
    if not graph:
        return None
    # Sort alphabetically first so ties go to the alphabetically first name
    return max(sorted(graph), key=lambda loc: len(graph[loc]))


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent."""
    heap = []
    for priority, location in reports:
        heapq.heappush(heap, (priority, location))
    result = []
    while heap:
        _, location = heapq.heappop(heap)
        result.append(location)
    return result