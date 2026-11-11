/* Regenerate graph number `rep` of a sim_mn run (same generator, same order) and check the longest
 * minimum-weight path by a second method: hop-limited Bellman-Ford from the root of that path.
 * usage: check_rep n rep seed
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

static uint64_t st[4];
static inline uint64_t rotl(uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t splitmix(uint64_t *x) {
    uint64_t z = (*x += 0x9e3779b97f4a7c15ULL);
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
    z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
    return z ^ (z >> 31);
}
static inline uint64_t next(void) {
    uint64_t r = rotl(st[1] * 5, 7) * 9, t = st[1] << 17;
    st[2] ^= st[0]; st[3] ^= st[1]; st[1] ^= st[2]; st[0] ^= st[3];
    st[2] ^= t; st[3] = rotl(st[3], 45);
    return r;
}
static inline double exp1(void) {
    double u = (double)(next() >> 11) * (1.0 / 9007199254740992.0);
    return -log(1.0 - u);
}

int main(int argc, char **argv) {
    int n = atoi(argv[1]), rep = atoi(argv[2]);
    uint64_t seed = strtoull(argv[3], NULL, 10);
    for (int i = 0; i < 4; i++) st[i] = splitmix(&seed);
    double *w = malloc((size_t)n * n * sizeof *w);
    double *dist = malloc((size_t)n * sizeof *dist);
    int *hop = malloc((size_t)n * sizeof *hop), *pred = malloc((size_t)n * sizeof *pred);
    char *done = malloc((size_t)n);
    for (int g = 0; g <= rep; g++)
        for (int i = 0; i < n; i++) {
            w[(size_t)i * n + i] = INFINITY;
            for (int j = i + 1; j < n; j++) {
                double x = exp1();
                w[(size_t)i * n + j] = x; w[(size_t)j * n + i] = x;
            }
        }
    /* weight statistics */
    double mn = INFINITY, sum = 0; long cnt = 0, small = 0;
    for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) {
        double x = w[(size_t)i * n + j];
        if (x < mn) mn = x;
        sum += x; cnt++;
        if (x < 0.01) small++;
    }
    printf("edges %ld mean weight %.5f min %.3e  below 0.01: %ld (expected %.1f)\n", cnt, sum / cnt, mn, small,
           cnt * (1 - exp(-0.01)));
    int M = 0, br = -1, bu = -1;
    for (int r = 0; r < n; r++) {
        const double *wr = w + (size_t)r * n;
        for (int v = 0; v < n; v++) { dist[v] = wr[v]; hop[v] = 1; done[v] = 0; }
        done[r] = 1;
        for (int it = 1; it < n; it++) {
            int u = -1; double best = INFINITY;
            for (int v = 0; v < n; v++) if (!done[v] && dist[v] < best) { best = dist[v]; u = v; }
            done[u] = 1;
            if (hop[u] > M) { M = hop[u]; br = r; bu = u; }
            const double *wu = w + (size_t)u * n;
            for (int v = 0; v < n; v++) {
                double nd = best + wu[v];
                if (!done[v] && nd < dist[v]) { dist[v] = nd; hop[v] = hop[u] + 1; }
            }
        }
    }
    printf("Dijkstra: M = %d, attained from %d to %d\n", M, br, bu);
    /* Bellman-Ford with at most h edges from br; cur[v] = least weight of a walk br -> v with <= h edges */
    double *cur = malloc((size_t)n * sizeof *cur), *nxt = malloc((size_t)n * sizeof *nxt);
    for (int v = 0; v < n; v++) { cur[v] = (v == br) ? 0.0 : INFINITY; pred[v] = -1; }
    double prev_target = INFINITY;
    int first_h = -1, last_change = 0;
    for (int h = 1; h < n; h++) {
        memcpy(nxt, cur, (size_t)n * sizeof *cur);
        for (int u = 0; u < n; u++) {
            if (cur[u] == INFINITY) continue;
            const double *wu = w + (size_t)u * n;
            for (int v = 0; v < n; v++) {
                double nd = cur[u] + wu[v];
                if (nd < nxt[v]) { nxt[v] = nd; pred[v] = u; }
            }
        }
        double *t = cur; cur = nxt; nxt = t;
        if (cur[bu] < prev_target) {
            if (h >= M - 3) printf("  at most %d edges: least weight to target %.12f\n", h, cur[bu]);
            prev_target = cur[bu]; last_change = h;
            if (first_h < 0) first_h = h;
        }
    }
    printf("Bellman-Ford: the least weight to the target last improves when %d edges are allowed; final %.12f\n",
           last_change, cur[bu]);
    /* the path and its edge weights */
    int path[1024], len = 0;
    for (int v = bu; v != -1 && len < 1000; v = (v == br) ? -1 : pred[v]) path[len++] = v;
    printf("path edges %d:", len - 1);
    double tot = 0;
    for (int i = len - 1; i > 0; i--) {
        double x = w[(size_t)path[i] * n + path[i - 1]];
        tot += x;
        printf(" %.4f", x);
    }
    printf("\n total %.12f  (typical distance log n / n = %.5f)\n", tot, log((double)n) / n);
    printf("path vertices:");
    for (int i = len - 1; i >= 0; i--) printf(" %d", path[i]);
    printf("\n");
    return 0;
}
