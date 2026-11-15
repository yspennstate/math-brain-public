/* The loop-erased ant process of Kious, Mailler and Schapira on the graph G_l.
   Vertices N, u, v, F; edges Nu, Nv, uv; a path of l edges from u to F and a path of l edges from v to F.
   Each ant walks from N until it first hits F, moving along an edge with probability proportional to its weight
   (weights are frozen during the walk). The walk is then reversed, its loops are erased in chronological order,
   and every edge of the resulting simple path gains weight 1. All weights start at 1.

   run:    ./sim_ants run l ants seed
           prints, at n = 10^3, 10^4, ..., the fractions a = W_Nu/(n+2), c = W_ux/(n+2), h = W_uv/(n+2) and
           (1-1/l) a (1-a); it also checks that the edges of each tail carry one common weight and that
           W_Nu + W_Nv = n + 2.
   freeze: ./sim_ants freeze l A B C D R ants seed
           keeps the weights fixed (A on Nu, B on Nv, C on the u-tail, D on the v-tail, R on uv) and prints the
           empirical frequencies of the four simple paths next to the formula of Lemma 2.                          */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

static uint64_t s[4];
static uint64_t rotl(uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t next(void) {
    uint64_t r = rotl(s[1] * 5, 7) * 9, t = s[1] << 17;
    s[2] ^= s[0]; s[3] ^= s[1]; s[1] ^= s[2]; s[0] ^= s[3]; s[2] ^= t; s[3] = rotl(s[3], 45);
    return r;
}
static void seed(uint64_t x) {
    for (int i = 0; i < 4; i++) { x += 0x9E3779B97F4A7C15ULL; uint64_t z = x;
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL; s[i] = z ^ (z >> 31); }
}
static double unif(void) { return (next() >> 11) * (1.0 / 9007199254740992.0); }

#define MAXV 64
#define MAXE 64
static int nv, ne, deg[MAXV], nbr[MAXV][3], eid[MAXV][3];
static double w[MAXE];
static int eNu, eNv, eUV, eC[32], eD[32];

static int add_edge(int x, int y) {
    nbr[x][deg[x]] = y; eid[x][deg[x]++] = ne; nbr[y][deg[y]] = x; eid[y][deg[y]++] = ne; return ne++;
}
static void build(int l) {          /* N = 0, u = 1, v = 2, F = 3 */
    nv = 4; ne = 0; memset(deg, 0, sizeof deg);
    eNu = add_edge(0, 1); eNv = add_edge(0, 2); eUV = add_edge(1, 2);
    int prev = 1; for (int i = 0; i < l; i++) { int nx = (i == l - 1) ? 3 : nv++; eC[i] = add_edge(prev, nx); prev = nx; }
    prev = 2;     for (int i = 0; i < l; i++) { int nx = (i == l - 1) ? 3 : nv++; eD[i] = add_edge(prev, nx); prev = nx; }
}

static int *traj; static long cap = 0;
static int path[MAXV], onpath[MAXV];

/* one ant; returns the number of vertices of the reinforced path, stored in path[] from F to N */
static int ant(void) {
    long T = 0; int x = 0;
    for (;;) {
        if (T >= cap) { cap = cap ? 2 * cap : 1024; traj = realloc(traj, cap * sizeof(int)); }
        traj[T++] = x;
        if (x == 3) break;
        double tot = 0; for (int k = 0; k < deg[x]; k++) tot += w[eid[x][k]];
        double r = unif() * tot; int k = 0;
        while (k < deg[x] - 1 && r >= w[eid[x][k]]) { r -= w[eid[x][k]]; k++; }
        x = nbr[x][k];
    }
    /* chronological loop erasure of the reversed walk traj[T-1], ..., traj[0] */
    int len = 0; memset(onpath, 0, sizeof onpath);
    for (long t = T - 1; t >= 0; t--) {
        int y = traj[t];
        if (onpath[y]) { while (path[len - 1] != y) onpath[path[--len]] = 0; }
        else { path[len++] = y; onpath[y] = 1; }
    }
    return len;
}
static int edge_between(int x, int y) { for (int k = 0; k < deg[x]; k++) if (nbr[x][k] == y) return eid[x][k]; return -1; }

int main(int argc, char **argv) {
    if (argc >= 5 && !strcmp(argv[1], "run")) {
        int l = atoi(argv[2]); long ants = atol(argv[3]); seed(strtoull(argv[4], 0, 10)); build(l);
        for (int e = 0; e < ne; e++) w[e] = 1;
        long nextp = 1000; int ok = 1;
        printf("l %d seed %s\n        n        a        c        h  (1-1/l)a(1-a)  invariants\n", l, argv[4]);
        for (long n = 1; n <= ants; n++) {
            int len = ant();
            for (int i = 0; i + 1 < len; i++) w[edge_between(path[i], path[i + 1])] += 1;
            if (n == nextp || n == ants) {
                double S = n + 2.0;
                for (int i = 1; i < l; i++) if (w[eC[i]] != w[eC[0]] || w[eD[i]] != w[eD[0]]) ok = 0;
                if (w[eNu] + w[eNv] != S || w[eC[0]] + w[eD[0]] != S) ok = 0;
                double a = w[eNu] / S;
                printf("%9ld %8.5f %8.5f %8.5f %14.5f  %s\n", n, a, w[eC[0]] / S, w[eUV] / S, (1.0 - 1.0 / l) * a * (1 - a), ok ? "ok" : "BROKEN");
                fflush(stdout); if (n == nextp) nextp *= 10;
            }
        }
        return 0;
    }
    if (argc >= 10 && !strcmp(argv[1], "freeze")) {
        int l = atoi(argv[2]); double A = atof(argv[3]), B = atof(argv[4]), C = atof(argv[5]), D = atof(argv[6]), R = atof(argv[7]);
        long ants = atol(argv[8]); seed(strtoull(argv[9], 0, 10)); build(l);
        w[eNu] = A; w[eNv] = B; w[eUV] = R; for (int i = 0; i < l; i++) { w[eC[i]] = C; w[eD[i]] = D; }
        long cnt[4] = {0, 0, 0, 0};
        for (long n = 0; n < ants; n++) {
            int len = ant();                      /* path[] runs from F back to N; path[len-2] is u or v */
            int first_u = (path[len - 2] == 1), rung = (len == l + 3);
            cnt[(first_u ? 0 : 1) + (rung ? 2 : 0)]++;
        }
        /* un-normalised form of Lemma 2: weights of the spanning trees containing each path, divided by C^(l-1) D^(l-1) */
        double SA = A + B, SC = C + D, Z = C * D * SA + l * A * B * SC + l * R * SA * SC;
        double q[4] = { A * C * (D + l * B + l * R) / Z, B * D * (C + l * A + l * R) / Z, l * A * R * D / Z, l * B * R * C / Z };
        const char *nm[4] = {"N u ... F", "N v ... F", "N u v ... F", "N v u ... F"};
        printf("l %d weights A %g B %g C %g D %g R %g, %ld ants\n", l, A, B, C, D, R, ants);
        for (int i = 0; i < 4; i++) printf("%-12s empirical %.5f  formula %.5f\n", nm[i], cnt[i] / (double)ants, q[i]);
        return 0;
    }
    fprintf(stderr, "usage: sim_ants run l ants seed | sim_ants freeze l A B C D R ants seed\n"); return 1;
}
