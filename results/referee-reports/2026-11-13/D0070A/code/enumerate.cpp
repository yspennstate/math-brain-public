// Exact depth-first enumeration on a finite graph or a complete rooted ball.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
#include <sys/resource.h>
struct Graph {
    std::vector<std::vector<int>> a;
    std::vector<int> h;
    std::vector<unsigned char> seen;
    std::vector<uint64_t> counts, bridges;
    int depth;
    void dfs(int v, int n, bool positive, int maximum) {
        ++counts[n];
        if (n == 0 || (positive && h[v] == maximum)) ++bridges[n];
        if (n == depth) return;
        for (int w : a[v]) if (!seen[w]) {
            seen[w] = 1;
            dfs(w, n+1, positive && h[w] > 0, std::max(maximum, h[w]));
            seen[w] = 0;
        }
    }
};
int main() {
    int size, root;
    Graph g;
    if (!(std::cin >> size >> root >> g.depth)) return 1;
    if (size < 1 || g.depth < 0 || g.depth > 35) return 2;
    g.a.resize(size); g.h.resize(size); g.seen.resize(size);
    g.counts.resize(g.depth+1); g.bridges.resize(g.depth+1);
    for (int v=0; v<size; ++v) {
        int degree; std::cin >> g.h[v] >> degree;
        for (int j=0,w; j<degree; ++j) {
            std::cin >> w;
            if (w<0 || w>=size || w==v) return 3;
            g.a[v].push_back(w);
        }
    }
    if (g.h[root] != 0) return 4;
    g.seen[root]=1; g.dfs(root,0,true,0);
    for (int n=0; n<=g.depth; ++n)
        std::cout << n << ' ' << g.counts[n] << ' ' << g.bridges[n] << '\n';
    std::cerr << "nice=" << getpriority(PRIO_PROCESS,0) << "\n";
}
