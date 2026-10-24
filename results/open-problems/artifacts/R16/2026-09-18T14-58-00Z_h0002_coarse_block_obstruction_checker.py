from collections import defaultdict

# Exact finite obstruction to the inference:
# "if conceptual macroblocks can be linked by one sprinkling edge per chain link,
# then all weight in those macroblocks becomes connected."
# The macroblocks below are unions of disconnected first-round components.

weights = {0: 1, 1: 1, 2: 1, 3: 1}
B1 = {0, 1}
B2 = {2, 3}
blocks = [B1, B2]

# There is a sprinkling edge between the two conceptual blocks.
sprinkle_edges = {(0, 2)}

adj = defaultdict(set)
for u, v in sprinkle_edges:
    adj[u].add(v)
    adj[v].add(u)

assert any(
    (u in B1 and v in B2) or (u in B2 and v in B1)
    for u, v in sprinkle_edges
)

seen = set()
components = []
for v in weights:
    if v in seen:
        continue
    stack = [v]
    seen.add(v)
    comp = set()
    while stack:
        x = stack.pop()
        comp.add(x)
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    components.append(comp)

component_weights = [sum(weights[v] for v in comp) for comp in components]
total_weight = sum(weights.values())
largest_connected_weight = max(component_weights)

print("CONCEPTUAL_BLOCKS", blocks)
print("SPRINKLE_EDGES", sprinkle_edges)
print("CHAIN_LINK_EXISTS", True)
print("CONNECTED_COMPONENTS", sorted([sorted(c) for c in components]))
print("COMPONENT_WEIGHTS", sorted(component_weights, reverse=True))
print("TOTAL_BLOCK_WEIGHT", total_weight)
print("LARGEST_CONNECTED_WEIGHT", largest_connected_weight)

assert largest_connected_weight < total_weight
print(
    "INVALID_INFERENCE_CERTIFIED",
    "one inter-block link does not connect all weight in disconnected macroblocks",
)
print("ALL_EXACT_CHECKS_PASS")
