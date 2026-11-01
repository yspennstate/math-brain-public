from collections import defaultdict


def states(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def ordinary_edges(n):
    for p, q in states(n):
        for r in range(q + 1, n):
            yield (p, q), (q, r)  # R
        for s in range(p):
            yield (p, q), (s, p)  # L


def direction(prev, curr):
    a, b = prev
    c, d = curr
    if c == b and d > b:
        return "R"
    if d == a and c < a:
        return "L"
    raise ValueError((prev, curr))


def allowed_next(prev, curr, nxt):
    pd = direction(prev, curr)
    nd = direction(curr, nxt)
    if pd == nd:
        return True
    a, b = prev
    p, q = curr
    if pd == "R" and nd == "L":
        # (a,b)->(b,q)->(s,b): after removing descent/backtrack,
        # a genuine switch is the strict envelope expansion s<a.
        s, _ = nxt
        return s < a
    # (a,b)->(s,a)->(a,t): strict envelope expansion requires t>b.
    _, t = nxt
    return t > b


def find_cycle(n):
    nodes = list(ordinary_edges(n))
    graph = defaultdict(list)
    by_prev = defaultdict(list)
    for u, v in nodes:
        by_prev[u].append(v)
    for prev, curr in nodes:
        for nxt in by_prev[curr]:
            if allowed_next(prev, curr, nxt):
                graph[(prev, curr)].append((curr, nxt))

    color, stack, where = {}, [], {}

    def dfs(u):
        color[u] = 1
        where[u] = len(stack)
        stack.append(u)
        for v in graph[u]:
            if color.get(v, 0) == 0:
                ans = dfs(v)
                if ans:
                    return ans
            elif color[v] == 1:
                return stack[where[v]:] + [v]
        stack.pop()
        where.pop(u, None)
        color[u] = 2
        return None

    for u in nodes:
        if color.get(u, 0) == 0:
            ans = dfs(u)
            if ans:
                return ans
    return None


for n in range(3, 7):
    cycle = find_cycle(n)
    print(f"n={n} cycle={cycle is not None}")
    if cycle:
        for edge_state in cycle:
            print(edge_state)
        break
