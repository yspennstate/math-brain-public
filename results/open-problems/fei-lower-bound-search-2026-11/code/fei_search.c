/* fei_search.c - simulated annealing over Boolean functions on n <= 14 variables (monotone or general).
   Successor of mono_search.c: no entropy table (logs are taken directly, so n up to 14 fits in a few MB) and one
   more objective, the tower score of a balanced function.
   A function is a set U of {0,1}^n (x in U <=> f(x) = -1).  mu(T) = fhat(T)^2, eta(x) = x log2(1/x).
     H = sum_T eta(mu(T)),  I = sum_T |T| mu(T),  Inf_i = sum_{T not containing i} mu(T+i),
     E_i = H - sum_{T not containing i} eta(mu(T) + mu(T+i)).
   Objectives:
     0  minE    = min_i E_i/Inf_i
     1  ruleMax = E_i/Inf_i at the coordinate of largest influence (smallest ratio among ties)
     2  Q0      = sum_i E_i / I
     3  HI      = H / I
     4  balHI1  = H/(I-1) on balanced functions with I > 1 (limit of H/I along the self-composition tower)
   Monotone mode (gen = 0): moves add a maximal point of the complement, remove a minimal point of U, or (rarely)
   add an up-closure / remove a down-closure.  For objective 4 the walk may leave the balanced functions; it pays
   pen * |mean| * 2^n / 2 per step of imbalance and only balanced tables are reported.
   General mode (gen = 1): single-point flips; for objective 4, swaps of a point of U with a point outside U from a
   balanced start, so every table visited is balanced.
   usage: fei_search n obj seconds seed outfile [iters_per_run] [T0] [T1] [gen] [pen]
   One line per run: run seed obj value | minE ruleMax Q0 HI H I mean | hex table (high index first). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define NOBJ 5
static int n, N, gen, obj;
static double NN, LNN, pen;
static unsigned char *U, *save;
static int *F;
static long long *sq;
typedef struct { double v[NOBJ], H, I, mean; int bal; } st;

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs >> 12; rs ^= rs << 25; rs ^= rs >> 27; return rs * 2685821657736338717ULL; }
static inline double runif(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }
static inline double eta(long long m) { return m ? (double)m * (LNN - log2((double)m)) / NN : 0.0; }

static int evaluate(st *s) {
    for (int x = 0; x < N; x++) F[x] = 1 - 2 * U[x];
    for (int len = 1; len < N; len <<= 1)
        for (int i = 0; i < N; i += 2 * len)
            for (int j = i; j < i + len; j++) { int u = F[j], v = F[j + len]; F[j] = u + v; F[j + len] = u - v; }
    double H = 0; long long Inum = 0;
    for (int T = 0; T < N; T++) { sq[T] = (long long)F[T] * F[T]; H += eta(sq[T]); Inum += (long long)__builtin_popcount(T) * sq[T]; }
    if (Inum == 0) return 0;
    double I = Inum / NN;
    s->H = H; s->I = I; s->mean = F[0] / (double)N; s->bal = F[0] == 0;
    s->v[3] = H / I;
    if (obj == 3) { s->v[0] = s->v[1] = s->v[2] = s->v[4] = 0; return 1; }
    if (obj == 4) {
        s->v[0] = s->v[1] = s->v[2] = 0;
        if (I <= 1.0 + 1e-9) { s->v[4] = -1e6; return 1; }
        s->v[4] = H / (I - 1.0) - pen * fabs((double)F[0]) / 2.0;
        return 1;
    }
    double minE = 1e300, rmax = 1e300, sumE = 0; long long infmax = -1;
    for (int i = 0; i < n; i++) {
        int bit = 1 << i; long long infn = 0; double S = 0;
        for (int T = 0; T < N; T++) { if (T & bit) continue; infn += sq[T | bit]; S += eta(sq[T] + sq[T | bit]); }
        if (infn == 0) continue;
        double E = H - S, re = E / (infn / NN);
        sumE += E;
        if (re < minE) minE = re;
        if (infn > infmax) { infmax = infn; rmax = re; } else if (infn == infmax && re < rmax) rmax = re;
    }
    s->v[0] = minE; s->v[1] = rmax; s->v[2] = sumE / I; s->v[4] = 0;
    return 1;
}

static void random_start(void) {
    if (gen && obj == 4) {
        for (int x = 0; x < N; x++) U[x] = x & 1;
        for (int x = N - 1; x > 0; x--) { int y = (int)(rnd() % (uint64_t)(x + 1)); unsigned char t = U[x]; U[x] = U[y]; U[y] = t; }
        return;
    }
    if (gen) { double p = 0.05 + 0.9 * runif(); for (int x = 0; x < N; x++) U[x] = runif() < p; return; }
    memset(U, 0, N);
    int m = 1 + (int)(rnd() % (2 * n));
    for (int k = 0; k < m; k++) {
        int x = 0; double p = 0.2 + 0.6 * runif();
        for (int i = 0; i < n; i++) if (runif() < p) x |= 1 << i;
        if (x == 0) x = 1 << (rnd() % n);
        for (int y = 0; y < N; y++) if ((y & x) == x) U[y] = 1;
    }
}

/* returns a flipped point, -1 if `save` holds the old table (closure move or swap), -2 if nothing legal was found */
static int move(void) {
    if (gen && obj == 4) {
        memcpy(save, U, N);
        int x, y;
        do { x = (int)(rnd() % N); } while (!U[x]);
        do { y = (int)(rnd() % N); } while (U[y]);
        U[x] = 0; U[y] = 1;
        return -1;
    }
    if (gen) { int x = (int)(rnd() % N); U[x] ^= 1; return x; }
    if (runif() < 0.03) {
        memcpy(save, U, N);
        int x = (int)(rnd() % N);
        if (!U[x]) { for (int y = 0; y < N; y++) if ((y & x) == x) U[y] = 1; }
        else { for (int y = 0; y < N; y++) if ((y & x) == y) U[y] = 0; }
        return -1;
    }
    for (int tries = 0; tries < 8192; tries++) {
        int x = (int)(rnd() % N), ok = 1;
        if (U[x]) { for (int i = 0; i < n && ok; i++) if ((x >> i & 1) && U[x ^ (1 << i)]) ok = 0; }
        else { for (int i = 0; i < n && ok; i++) if (!(x >> i & 1) && !U[x | (1 << i)]) ok = 0; }
        if (ok) { U[x] ^= 1; return x; }
    }
    return -2;
}

static void hexout(FILE *o, const unsigned char *t) {
    for (int i = N / 4 - 1; i >= 0; i--) fprintf(o, "%x", t[4 * i] | t[4 * i + 1] << 1 | t[4 * i + 2] << 2 | t[4 * i + 3] << 3);
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: fei_search n obj seconds seed outfile [iters] [T0] [T1] [gen] [pen]\n"); return 2; }
    n = atoi(argv[1]); obj = atoi(argv[2]); double seconds = atof(argv[3]); uint64_t seed = strtoull(argv[4], 0, 10);
    long iters = argc > 6 ? atol(argv[6]) : 200000; double T0 = argc > 7 ? atof(argv[7]) : 0.03, T1 = argc > 8 ? atof(argv[8]) : 0.0005;
    gen = argc > 9 ? atoi(argv[9]) : 0; pen = argc > 10 ? atof(argv[10]) : 0.1;
    if (n < 2 || n > 14 || obj < 0 || obj >= NOBJ) return 2;
    N = 1 << n; NN = (double)N * N; LNN = 2.0 * n;
    U = malloc(N); save = malloc(N); F = malloc(N * sizeof(int)); sq = malloc(N * sizeof(long long));
    unsigned char *best = malloc(N);
    rs = seed * 0x9E3779B97F4A7C15ULL + 0x1234567ULL; for (int k = 0; k < 20; k++) rnd();
    time_t t0 = time(0); double gbest = -1e300; long run = 0; unsigned long long evals = 0;
    FILE *o = fopen(argv[5], "a");
    fprintf(o, "# fei_search n=%d obj=%d seconds=%g seed=%llu iters=%ld T0=%g T1=%g gen=%d pen=%g\n", n, obj, seconds, (unsigned long long)seed, iters, T0, T1, gen, pen); fflush(o);
    while (difftime(time(0), t0) < seconds) {
        st cur, nw, bst; int have = 0;
        do { random_start(); } while (!evaluate(&cur));
        if (obj != 4 || cur.bal) { bst = cur; memcpy(best, U, N); have = 1; }
        double ratio = pow(T1 / T0, 1.0 / iters), T = T0;
        for (long it = 0; it < iters; it++, T *= ratio) {
            int x = move();
            if (x == -2) break;
            int ok = evaluate(&nw); evals++;
            if (ok && (nw.v[obj] >= cur.v[obj] || runif() < exp((nw.v[obj] - cur.v[obj]) / T))) {
                cur = nw;
                if ((obj != 4 || cur.bal) && (!have || cur.v[obj] > bst.v[obj])) { bst = cur; memcpy(best, U, N); have = 1; }
            } else {
                if (x >= 0) U[x] ^= 1; else memcpy(U, save, N);
            }
            if ((it & 1023) == 0 && difftime(time(0), t0) >= seconds) break;
        }
        if (have) {
            fprintf(o, "%ld %llu %d %.12f | %.12f %.12f %.12f %.12f %.9f %.9f %.6f | ", run, (unsigned long long)seed, obj, bst.v[obj],
                    bst.v[0], bst.v[1], bst.v[2], bst.v[3], bst.H, bst.I, bst.mean);
            hexout(o, best); fprintf(o, "\n"); fflush(o);
            if (bst.v[obj] > gbest) gbest = bst.v[obj];
        }
        run++;
    }
    fprintf(o, "# done runs=%ld evals=%llu best=%.12f\n", run, evals, gbest); fclose(o);
    return 0;
}
