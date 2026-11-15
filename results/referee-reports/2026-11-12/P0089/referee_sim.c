/* Independent vertex-weight Fenwick sampler, updated after EVERY endpoint.
 * cc -O2 -o referee_sim referee_sim.c -lm
 * ./referee_sim sqrt|log|osc|two|uniform n m seed > output.json
 * One worker, <100 MB at n=1e6,m=3, hard wall limit 240 seconds.
 */
#include <assert.h>
#include <math.h>
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

static uint64_t rng_state;
static uint64_t next64(void) {
    uint64_t z = (rng_state += UINT64_C(0x9e3779b97f4a7c15));
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    return z ^ (z >> 31);
}
static double uniform(void) { return (next64() >> 11) * 0x1.0p-53; }
static int kind;
static double f(int k) {
    if (kind == 0) return sqrt(k + 1.0);
    if (kind == 1) return log(k + 2.0);
    if (kind == 2) return sqrt(k + 1.0) + (k % 2 ? -0.4 : 0.4);
    if (kind == 3) return k == 0 ? 1 : 2;
    return 1;
}
static void add(double *tree, int n, int v, double delta) {
    for (int i = v + 1; i <= n; i += i & -i) tree[i] += delta;
}
static int choose(double *tree, int n, int top, double x) {
    int pos = 0;
    for (int bit = top; bit; bit >>= 1) {
        int nxt = pos + bit;
        if (nxt <= n && tree[nxt] <= x) { x -= tree[nxt]; pos = nxt; }
    }
    return pos;
}
static int distinct(const int *vs, int count) {
    for (int i = 0; i < count; ++i) for (int j = 0; j < i; ++j)
        if (vs[i] == vs[j]) return 0;
    return 1;
}
/* An induced ball of radius one with indegree zero is a simple star iff
 * its m parents are distinct and there are no edges between these parents.
 */
static int star0(int v, int m, const int *out) {
    int parents[3];
    for (int a = 0; a < m; ++a) parents[a] = out[v*m+a];
    if (!distinct(parents, m)) return 0;
    for (int a = 0; a < m; ++a) if (parents[a] > 0)
        for (int s = 0; s < m; ++s) for (int b = 0; b < m; ++b)
            if (out[parents[a]*m+s] == parents[b]) return 0;
    return 1;
}

int main(int argc, char **argv) {
    alarm(240);
    assert(argc == 5);
    const char *names[] = {"sqrt", "log", "osc", "two", "uniform"};
    kind = -1;
    for (int i = 0; i < 5; ++i) if (!strcmp(argv[1], names[i])) kind = i;
    assert(kind >= 0);
    int n = atoi(argv[2]), m = atoi(argv[3]);
    assert(n >= 100 && n <= 1000000 && m >= 2 && m <= 3);
    rng_state = strtoull(argv[4], NULL, 10);
    double *tree = calloc(n + 1, sizeof(double));
    int *deg = calloc(n, sizeof(int));
    int *out = malloc((size_t)n*m*sizeof(int));
    int *head = malloc((size_t)n*sizeof(int));
    int *next = malloc((size_t)n*m*sizeof(int));
    assert(tree && deg && out && head && next);
    for (int v = 0; v < n; ++v) head[v] = -1;
    for (int s = 0; s < m; ++s) out[s] = -1;
    double total = f(0), parent_ratio = 0;
    int ratios = 0, top = 1;
    while (top*2 <= n) top *= 2;
    add(tree, n, 0, total);
    double max_total_drift = 0;
    for (int v = 1; v < n; ++v) {
        for (int s = 0; s < m; ++s) {
            double x = uniform() * total;
            int w = choose(tree, n, top, x);
            assert(w >= 0 && w < v);
            // Independent direct-sum selection for the first 1000 vertices.
            if (v < 1000) {
                double sum = 0; int oracle = -1;
                for (int i = 0; i < v; ++i) { sum += f(deg[i]); if (sum > x) { oracle = i; break; } }
                assert(oracle == w);
            }
            out[v*m+s] = w;
            next[v*m+s] = head[w]; head[w] = v*m+s;
            double delta = f(deg[w] + 1) - f(deg[w]);
            ++deg[w]; add(tree, n, w, delta); total += delta;
            if (s == 0 && v + 1 >= n/2) { parent_ratio += (w+1.0)/(v+1.0); ++ratios; }
        }
        add(tree, n, v, f(0)); total += f(0);
        if ((v + 1) % 100000 == 0) {
            double check = 0;
            for (int i = 0; i <= v; ++i) check += f(deg[i]);
            double drift = fabs(check - total);
            if (drift > max_total_drift) max_total_drift = drift;
            assert(drift < 0.01);
        }
    }
    int hist[2000] = {0}, maxdeg = 0; long long sumdeg = 0;
    double S = 0;
    long long stars = 0, H0 = 0, H1 = 0, reject_collision = 0;
    for (int v = 0; v < n; ++v) {
        assert(deg[v] < 2000);
        ++hist[deg[v]]; sumdeg += deg[v]; S += f(deg[v]);
        if (deg[v] > maxdeg) maxdeg = deg[v];
        if (v == 0 || deg[v]) continue;
        stars += star0(v, m, out);
        int special = -1, valid = 1;
        for (int s = 0; s < m; ++s) {
            int p = out[v*m+s];
            if (deg[p] == 2 && special < 0) special = p;
            else if (deg[p] != 1) { valid = 0; break; }
        }
        if (!valid) continue;
        int vs[20], count = 0;
        vs[count++] = v;
        for (int s = 0; s < m; ++s) vs[count++] = out[v*m+s];
        for (int s = 0; s < m; ++s) {
            int p = out[v*m+s];
            if (p == 0) { valid = 0; break; }
            for (int t = 0; t < m; ++t) vs[count++] = out[p*m+t];
        }
        if (!valid) continue;
        if (special >= 0) {
            int extra = -1;
            for (int e = head[special]; e >= 0; e = next[e]) if (e/m != v) extra = e/m;
            if (extra < 0) continue;
            vs[count++] = extra;
        }
        if (!distinct(vs, count)) { ++reject_collision; continue; }
        int induced_edges = 0;
        for (int a = 0; a < count; ++a) if (vs[a] > 0)
            for (int s = 0; s < m; ++s)
                for (int b = 0; b < count; ++b)
                    induced_edges += out[vs[a]*m+s] == vs[b];
        if (induced_edges != count - 1) { ++reject_collision; continue; }
        if (special < 0) ++H0; else ++H1;
    }
    assert(sumdeg == (long long)m*(n-1));
    int sampled[11] = {0}, R = 100000;
    long long sampled_sum = 0;
    for (int i = 0; i < R; ++i) {
        int v = (int)(uniform()*n); sampled_sum += deg[v];
        if (deg[v] <= 10) ++sampled[deg[v]];
    }
    printf("{\"name\":\"%s\",\"n\":%d,\"m\":%d,\"seed\":%s,\"S_over_n\":%.15g,\"mean_degree\":%.15g,\"max_degree\":%d,\"max_total_drift\":%.6g,",
           names[kind],n,m,argv[4],S/n,(double)sumdeg/n,maxdeg,max_total_drift);
    printf("\"p0_to_p10\":[");
    for (int k = 0; k <= 10; ++k) printf("%s%.9g", k ? "," : "",(double)hist[k]/n);
    printf("],\"histogram\":[");
    for (int k = 0; k <= maxdeg; ++k) printf("%s%d", k ? "," : "",hist[k]);
    printf("],\"root_sample_p0_to_p10\":[");
    for (int k = 0; k <= 10; ++k) printf("%s%.9g", k ? "," : "",(double)sampled[k]/R);
    printf("],\"root_sample_mean\":%.9g,\"ball_star0\":%.9g,\"ball_H0\":%.9g,\"ball_H1\":%.9g,\"ball_collisions_rejected\":%lld,\"late_parent_age_ratio\":%.12g}\n",
           (double)sampled_sum/R,(double)stars/n,(double)H0/n,(double)H1/n,reject_collision,parent_ratio/ratios);
    free(tree); free(deg); free(out); free(head); free(next);
    return 0;
}
