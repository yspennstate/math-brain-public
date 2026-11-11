/* Longest minimum-weight path in the complete graph K_n with independent Exp(1) edge weights.
 *
 * For each sampled graph the program runs Dijkstra's algorithm from every vertex and records
 *   M = max over pairs of the number of edges of the minimum-weight path,
 *   R = max over j of the number of edges of the minimum-weight path from vertex 0 to j.
 * It also accumulates, over all graphs, the number of unordered pairs at each hopcount.
 *
 * usage: sim_mn n reps seed out_prefix
 * The program stops before the next graph if a file named STOP exists in the working directory.
 * output: out_prefix.graphs.csv  (rep,M,R)   and   out_prefix.hist.csv  (hopcount,pairs summed over graphs)
 *
 * cc -O3 -o sim_mn sim_mn.c -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>
#include <unistd.h>

static uint64_t st[4];
static inline uint64_t rotl(uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t splitmix(uint64_t *x) {
    uint64_t z = (*x += 0x9e3779b97f4a7c15ULL);
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
    z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
    return z ^ (z >> 31);
}
static inline uint64_t next(void) { /* xoshiro256** */
    uint64_t r = rotl(st[1] * 5, 7) * 9, t = st[1] << 17;
    st[2] ^= st[0]; st[3] ^= st[1]; st[1] ^= st[2]; st[0] ^= st[3];
    st[2] ^= t; st[3] = rotl(st[3], 45);
    return r;
}
static inline double exp1(void) {
    double u = (double)(next() >> 11) * (1.0 / 9007199254740992.0); /* [0,1) */
    return -log(1.0 - u);
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: sim_mn n reps seed out_prefix\n"); return 2; }
    int n = atoi(argv[1]), reps = atoi(argv[2]);
    uint64_t seed = strtoull(argv[3], NULL, 10);
    for (int i = 0; i < 4; i++) st[i] = splitmix(&seed);
    char name[1024];
    snprintf(name, sizeof name, "%s.graphs.csv", argv[4]);
    FILE *fg = fopen(name, "w");
    if (!fg) { perror(name); return 1; }
    fprintf(fg, "rep,M,R\n");
    double *w = malloc((size_t)n * n * sizeof *w);
    double *dist = malloc((size_t)n * sizeof *dist);
    int *hop = malloc((size_t)n * sizeof *hop);
    char *done = malloc((size_t)n);
    long long *hist = calloc((size_t)n, sizeof *hist);
    if (!w || !dist || !hop || !done || !hist) { fprintf(stderr, "out of memory\n"); return 1; }
    for (int rep = 0; rep < reps; rep++) {
        if (access("STOP", F_OK) == 0) break;
        for (int i = 0; i < n; i++) {
            w[(size_t)i * n + i] = INFINITY;
            for (int j = i + 1; j < n; j++) {
                double x = exp1();
                w[(size_t)i * n + j] = x; w[(size_t)j * n + i] = x;
            }
        }
        int M = 0, R = 0;
        for (int r = 0; r < n; r++) {
            const double *wr = w + (size_t)r * n;
            for (int v = 0; v < n; v++) { dist[v] = wr[v]; hop[v] = 1; done[v] = 0; }
            done[r] = 1;
            for (int it = 1; it < n; it++) {
                int u = -1; double best = INFINITY;
                for (int v = 0; v < n; v++) if (!done[v] && dist[v] < best) { best = dist[v]; u = v; }
                done[u] = 1;
                int h = hop[u];
                if (u > r) hist[h]++;
                if (h > M) M = h;
                if (r == 0 && h > R) R = h;
                const double *wu = w + (size_t)u * n;
                for (int v = 0; v < n; v++) {
                    double nd = best + wu[v];
                    if (!done[v] && nd < dist[v]) { dist[v] = nd; hop[v] = h + 1; }
                }
            }
        }
        fprintf(fg, "%d,%d,%d\n", rep, M, R);
        fflush(fg);
    }
    fclose(fg);
    snprintf(name, sizeof name, "%s.hist.csv", argv[4]);
    FILE *fh = fopen(name, "w");
    if (!fh) { perror(name); return 1; }
    fprintf(fh, "hopcount,pairs\n");
    for (int h = 1; h < n; h++) if (hist[h]) fprintf(fh, "%d,%lld\n", h, hist[h]);
    fclose(fh);
    return 0;
}
