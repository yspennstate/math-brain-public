/* fei_bias.c - simulated annealing over Boolean functions F on k <= 14 inputs under a product measure with
   Pr[y_j = 1] = p = a/2^b, for lower bounds on the FEI constant through composition towers.

   F is a set U of {0,1}^k (y in U <=> F(y) = -1).  With phi_j = (y_j - p)/sqrt(p(1-p)) and Ft(T) = E_p[F phi_T]:
     mean = Ft(0),  var = 1 - mean^2,  w(T) = Ft(T)^2,
     G = sum_{T != 0} (w(T)/var) log2(var/w(T))      entropy of the normalised non-constant spectrum
     J = sum_T |T| w(T) / var                        total influence over variance
   Composition law (inputs replaced by independent copies of a Boolean psi of mean 1 - 2p under uniform bits):
     G(F o psi) = G_p(F) + J_p(F) G(psi),   J(F o psi) = J_p(F) J(psi),
   and for a Boolean g on uniform bits H(g)/I(g) = [G(g) + log2(1/var) + (mean^2/var) log2(1/mean^2)] / J(g).
   If Pr_p[F = -1] = p exactly (a fixed point), the tower psi, F o psi, F o F o psi, ... has H/I -> [G_p(F)/(J_p(F)-1)
   + G(psi)] / J(psi).  At p = 1/2, psi = one bit, this is the balanced score H/(I-1).

   Objective: S = (G + al*J + be) / (ga*J - de), defaults al = be = 0, ga = de = 1 (the fixed-point score).
   The walk pays pen * 2^k * |Pr_p[U] - c/2^d| and only tables that hit the target mass exactly (integer
   arithmetic) are reported.
   Monotone mode (gen = 0): add a maximal point of the complement, remove a minimal point of U, or (rarely) add an
   up-closure / remove a down-closure.  General mode (gen = 1): single-point flips.
   usage: fei_bias k a b c d seconds seed outfile [iters] [T0] [T1] [gen] [pen] [al] [be] [ga] [de] [wfile] [preal] [seedfile]
   Bellman mode (wfile and preal given): S = (G_p(F) + W(p')) / J_p(F), W read from wfile (lines "log-odds W" on a
   uniform grid, as tower_vi.py --dump writes), p' = Pr_p[U]; monotone tables only, every run reported.
   Seeded (seedfile given, first data line "n0 hex"): every run starts from that function of the low n0 inputs,
   the other k - n0 inputs free; k <= 18.
   One line per run: run seed S | G J mean | hex table (high index first). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>

static int k, N, gen;
static double p, sd, pen, al, be, ga, de;
static unsigned char *U, *save;
static double *A;
static long long *wx, target, total;
static int wmode, WM;
static unsigned char *seedtab; static int seedn;
static double *Wt, Wlo, Wstep;
typedef struct { double val, S, G, J, mean; int exact; } st;

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs >> 12; rs ^= rs << 25; rs ^= rs >> 27; return rs * 2685821657736338717ULL; }
static inline double runif(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

static int evaluate(st *s) {
    long long mass = 0;
    for (int x = 0; x < N; x++) { A[x] = 1 - 2 * U[x]; if (U[x]) mass += wx[x]; }
    if (mass == 0 || mass == total) return 0;
    if (wmode && (!U[N - 1] || U[0]) && !gen) return 0;
    for (int len = 1; len < N; len <<= 1)
        for (int i = 0; i < N; i += 2 * len)
            for (int j = i; j < i + len; j++) { double lo = A[j], hi = A[j + len]; A[j] = (1 - p) * lo + p * hi; A[j + len] = sd * (hi - lo); }
    double mean = A[0], var = 1 - mean * mean, G = 0, J = 0;
    for (int T = 1; T < N; T++) {
        double w = A[T] * A[T] / var;
        if (w > 1e-300) G -= w * log2(w);
        J += __builtin_popcount(T) * w;
    }
    s->G = G; s->J = J; s->mean = mean; s->exact = mass == target;
    if (wmode) {   /* Bellman step: (G + W(p')) / J with W read from a table in log-odds of p' = Pr_p[U] */
        double q = (1 - mean) / 2, t = log2(q / (1 - q)), u = (t - Wlo) / Wstep;
        if (u < 0) u = 0; if (u > WM - 1) u = WM - 1;
        int i = (int)u; if (i > WM - 2) i = WM - 2;
        double w = Wt[i] + (u - i) * (Wt[i + 1] - Wt[i]);
        s->exact = 1;
        s->S = s->val = J > 1 + 1e-9 ? (G + w) / J : -1e6;
        return 1;
    }
    double den = ga * J - de;
    s->S = den > 1e-9 ? (G + al * J + be) / den : -1e6;
    long long diff = mass > target ? mass - target : target - mass;
    s->val = s->S - pen * N * ((double)diff / (double)total);
    return 1;
}

static void random_start(void) {
    if (seedtab) { int m = (1 << seedn) - 1; for (int x = 0; x < N; x++) U[x] = seedtab[x & m]; return; }
    if (gen) { double q = 0.05 + 0.9 * runif(); for (int x = 0; x < N; x++) U[x] = runif() < q; return; }
    memset(U, 0, N);
    int m = 1 + (int)(rnd() % (2 * k));
    for (int t = 0; t < m; t++) {
        int x = 0; double q = 0.2 + 0.6 * runif();
        for (int i = 0; i < k; i++) if (runif() < q) x |= 1 << i;
        if (x == 0) x = 1 << (rnd() % k);
        for (int y = 0; y < N; y++) if ((y & x) == x) U[y] = 1;
    }
}

/* returns a flipped point, -1 if `save` holds the old table, -2 if nothing legal was found */
static int move(void) {
    if (gen) { int x = (int)(rnd() % N); U[x] ^= 1; return x; }
    if (runif() < 0.03) {
        memcpy(save, U, N);
        int x = (int)(rnd() % N);
        if (!U[x]) { for (int y = 0; y < N; y++) if ((y & x) == x) U[y] = 1; }
        else { for (int y = 0; y < N; y++) if ((y & x) == y) U[y] = 0; }
        return -1;
    }
    /* walk from a random point to the boundary: down inside U to a minimal point, up outside U to a maximal one */
    int x = (int)(rnd() % N), cand[20], c;
    if (U[x]) {
        for (;;) {
            c = 0; for (int i = 0; i < k; i++) if ((x >> i & 1) && U[x ^ (1 << i)]) cand[c++] = i;
            if (!c) break;
            x ^= 1 << cand[rnd() % c];
        }
    } else {
        for (;;) {
            c = 0; for (int i = 0; i < k; i++) if (!(x >> i & 1) && !U[x | (1 << i)]) cand[c++] = i;
            if (!c) break;
            x |= 1 << cand[rnd() % c];
        }
    }
    U[x] ^= 1; return x;
}

static void hexout(FILE *o, const unsigned char *t) {
    for (int i = N / 4 - 1; i >= 0; i--) fprintf(o, "%x", t[4 * i] | t[4 * i + 1] << 1 | t[4 * i + 2] << 2 | t[4 * i + 3] << 3);
}

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage: fei_bias k a b c d seconds seed outfile [iters] [T0] [T1] [gen] [pen] [al] [be] [ga] [de]\n"); return 2; }
    k = atoi(argv[1]); int a = atoi(argv[2]), b = atoi(argv[3]), c = atoi(argv[4]), d = atoi(argv[5]);
    double seconds = atof(argv[6]); uint64_t seed = strtoull(argv[7], 0, 10);
    long iters = argc > 9 ? atol(argv[9]) : 200000; double T0 = argc > 10 ? atof(argv[10]) : 0.05, T1 = argc > 11 ? atof(argv[11]) : 0.0005;
    gen = argc > 12 ? atoi(argv[12]) : 0; pen = argc > 13 ? atof(argv[13]) : 2.0;
    al = argc > 14 ? atof(argv[14]) : 0; be = argc > 15 ? atof(argv[15]) : 0; ga = argc > 16 ? atof(argv[16]) : 1; de = argc > 17 ? atof(argv[17]) : 1;
    if (k < 2 || k > 18 || b < 1 || b * k > 60 || a < 1 || a >= (1 << b) || d > b * k || c < 1 || c >= (1 << d)) return 2;
    N = 1 << k; p = a / (double)(1 << b);
    if (argc > 19) {   /* Bellman mode: argv[18] = W table (lines "log-odds W", uniform grid), argv[19] = real bias p */
        FILE *wf = fopen(argv[18], "r"); if (!wf) return 3;
        Wt = malloc(100000 * sizeof(double)); char line[256]; double t0w = 0, t1w = 0;
        while (fgets(line, sizeof line, wf)) {
            double tt, ww; if (line[0] == '#' || sscanf(line, "%lf %lf", &tt, &ww) != 2) continue;
            if (WM == 0) t0w = tt; if (WM == 1) t1w = tt;
            if (WM < 100000) Wt[WM++] = ww;
        }
        fclose(wf); if (WM < 2) return 3;
        Wlo = t0w; Wstep = t1w - t0w; wmode = 1; p = atof(argv[19]);
        if (!(p > 0 && p < 1)) return 3;
    }
    if (argc > 20) {   /* seeded: argv[20] = file whose first data line is "n0 hex"; every run starts from that
                          function of the low n0 inputs, the other k - n0 inputs being free ("coins") */
        FILE *sf = fopen(argv[20], "r"); if (!sf) return 4;
        char *buf = malloc(70000); int ok = 0;
        while (fgets(buf, 70000, sf)) {
            if (buf[0] == '#') continue;
            char *sp = strchr(buf, ' '); if (!sp) continue;
            seedn = atoi(buf); char *hx = sp + 1; int len = 0;
            while ((hx[len] >= '0' && hx[len] <= '9') || ((hx[len] | 32) >= 'a' && (hx[len] | 32) <= 'f')) len++;
            int N0 = 1 << seedn; if (seedn < 1 || seedn > k) return 4;
            seedtab = calloc(N0, 1);
            for (int i = 0; i < len; i++) {   /* hex digit i from the end holds points 4i..4i+3 */
                char ch = hx[len - 1 - i]; int v = ch <= '9' ? ch - '0' : (ch | 32) - 'a' + 10;
                for (int j = 0; j < 4; j++) if (4 * i + j < N0) seedtab[4 * i + j] = v >> j & 1;
            }
            ok = 1; break;
        }
        fclose(sf); free(buf); if (!ok) return 4;
    }
    sd = sqrt(p * (1 - p));
    total = 1LL << (b * k); target = (long long)c << (b * k - d);
    U = malloc(N); save = malloc(N); A = malloc(N * sizeof(double)); wx = malloc(N * sizeof(long long));
    for (int x = 0; x < N; x++) { long long w = 1; for (int i = 0; i < k; i++) w *= (x >> i & 1) ? a : (1 << b) - a; wx[x] = w; }
    unsigned char *best = malloc(N);
    rs = seed * 0x9E3779B97F4A7C15ULL + 0x1234567ULL; for (int t = 0; t < 20; t++) rnd();
    time_t t0 = time(0); double gbest = -1e300; long run = 0, hits = 0; unsigned long long evals = 0;
    FILE *o = fopen(argv[8], "a");
    fprintf(o, "# fei_bias k=%d a=%d b=%d c=%d d=%d seconds=%g seed=%llu iters=%ld T0=%g T1=%g gen=%d pen=%g al=%g be=%g ga=%g de=%g\n",
            k, a, b, c, d, seconds, (unsigned long long)seed, iters, T0, T1, gen, pen, al, be, ga, de);
    if (wmode) fprintf(o, "# bellman p=%.15f wfile=%s points=%d\n", p, argv[18], WM);
    if (seedtab) fprintf(o, "# seeded from %s (n0=%d)\n", argv[20], seedn);
    fflush(o);
    while (difftime(time(0), t0) < seconds) {
        st cur, nw, bst; int have = 0;
        do { random_start(); } while (!evaluate(&cur));
        if (cur.exact) { bst = cur; memcpy(best, U, N); have = 1; }
        double ratio = pow(T1 / T0, 1.0 / iters), T = T0;
        for (long it = 0; it < iters; it++, T *= ratio) {
            int x = move();
            if (x == -2) break;
            int ok = evaluate(&nw); evals++;
            if (ok && (nw.val >= cur.val || runif() < exp((nw.val - cur.val) / T))) {
                cur = nw;
                if (cur.exact && (!have || cur.S > bst.S)) { bst = cur; memcpy(best, U, N); have = 1; }
            } else {
                if (x >= 0) U[x] ^= 1; else memcpy(U, save, N);
            }
            if ((it & 1023) == 0 && difftime(time(0), t0) >= seconds) break;
        }
        if (have) {
            fprintf(o, "%ld %llu %.12f | %.12f %.12f %.12f | ", run, (unsigned long long)seed, bst.S, bst.G, bst.J, bst.mean);
            hexout(o, best); fprintf(o, "\n"); fflush(o);
            if (bst.S > gbest) gbest = bst.S;
            hits++;
        }
        run++;
    }
    fprintf(o, "# done runs=%ld hits=%ld evals=%llu best=%.12f\n", run, hits, evals, gbest); fclose(o);
    return 0;
}
