/* fei_coin.c - anneal over Boolean functions on m + k inputs that are affine in k coins:
       g(x, y) = a(x) + sum_j b_j(x) Y_j,   x in {0,1}^m,  Y_j = +-1 fair coins,
   where every x carries one label:  0: g = +1,  1: g = -1,  2+2j: g = Y_j,  3+2j: g = -Y_j.
   The spectrum of g is the union of the spectra of a and of the b_j, so one evaluation costs (k+1) 2^m.
   The 18-input record (matchings of K_{3,3} plus nine coin-switched minterms) is the case m = 9, k = 9.

   Score at uniform inputs:  G = entropy of the normalised non-constant weights, J = I / Var, p' = Pr[g = -1],
       value = (G + W(p')) / J,    slack = G - c J + W(p'),   c = W(1/2) of the table.
   A balanced g has value > c  iff  H/(I-1) > c  iff  slack > 0.

   usage: fei_coin m k seconds seed outfile wfile init [iters] [T0] [T1] [obj] [jmin] [qbal] [pedge]
     qbal  chance that a move changing the mean is paired with one that restores it (default 0.9)
     pedge chance of an edge move: both ends of a cube edge take one coin label (default 0.1)
     init hex:FILE[:LINE]   library line "m hex" (bit x of the integer is 1 when g(x) = -1)
           lab:FILE[:LINE]   line "m k labels", labels = one character per x, chr(48 + label)
     obj   0: anneal on value   1 (default): anneal on slack - max(0, jmin - J)
     output lines:  run seed value slack | G J mean | coins used | labels
*/
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAXK 38

static int m, k, N;
static unsigned char *lab, *runbest, *gbest, *init0;
static int *A;
static double *lg;
static unsigned char *pc;
static double E[MAXK + 1], IS[MAXK + 1], WT[MAXK + 1], sE[MAXK + 1], sIS[MAXK + 1], sWT[MAXK + 1];
static int touched[MAXK + 1], tlist[MAXK + 1], nt;
static double *WX, *WY;
static int WM;
static double C0;
static unsigned long long rs;
static int objmode = 1;
static double jmin = 1.2;

static unsigned long long rnd64(void) {
    rs ^= rs >> 12; rs ^= rs << 25; rs ^= rs >> 27;
    return rs * 2685821657736338717ULL;
}
static double rnd(void) { return (double)(rnd64() >> 11) / 9007199254740992.0; }

static double Wof(double p) {
    double t = log2(p / (1.0 - p));
    if (t <= WX[0]) return WY[0];
    if (t >= WX[WM - 1]) return WY[WM - 1];
    int lo = 0, hi = WM - 1;
    while (hi - lo > 1) { int mid = (lo + hi) / 2; if (WX[mid] <= t) lo = mid; else hi = mid; }
    double f = (t - WX[lo]) / (WX[hi] - WX[lo]);
    return WY[lo] + f * (WY[hi] - WY[lo]);
}

static void upd(int r, int x, int d) {
    int *a = A + (size_t)r * N;
    for (int S = 0; S < N; S++) a[S] += __builtin_parity((unsigned)(S & x)) ? -d : d;
}

static void sums(int r) {
    int *a = A + (size_t)r * N;
    double e = 0, is = 0, wt = 0, inv = 1.0 / ((double)N * (double)N);
    for (int S = (r == 0); S < N; S++) {
        int v = a[S];
        if (!v) continue;
        if (v < 0) v = -v;
        double w = (double)v * (double)v * inv;
        e += w * 2.0 * (m - lg[v]);
        is += w * pc[S];
        wt += w;
    }
    E[r] = e; IS[r] = is; WT[r] = wt;
}

static void touch(int r) { if (!touched[r]) { touched[r] = 1; tlist[nt++] = r; } }

static void setlab(int x, int nl) {
    int ol = lab[x];
    if (ol == nl) return;
    if (ol < 2) { upd(0, x, ol == 0 ? -1 : 1); touch(0); }
    else { int j = (ol - 2) / 2; upd(1 + j, x, (ol & 1) ? 1 : -1); touch(1 + j); }
    if (nl < 2) { upd(0, x, nl == 0 ? 1 : -1); touch(0); }
    else { int j = (nl - 2) / 2; upd(1 + j, x, (nl & 1) ? -1 : 1); touch(1 + j); }
    lab[x] = (unsigned char)nl;
}

static void rebuild(void) {
    memset(A, 0, sizeof(int) * (size_t)(k + 1) * N);
    for (int x = 0; x < N; x++) {
        int l = lab[x];
        if (l < 2) upd(0, x, l == 0 ? 1 : -1);
        else upd(1 + (l - 2) / 2, x, (l & 1) ? -1 : 1);
    }
    for (int r = 0; r <= k; r++) sums(r);
}

static double evalst(double *val, double *slack, double *G, double *J, double *mean) {
    double H = 0, I = 0;
    for (int r = 0; r <= k; r++) { H += E[r]; I += IS[r]; if (r) I += WT[r]; }
    double mu = (double)A[0] / N, var = 1.0 - mu * mu;
    *mean = mu;
    if (var < 1e-12) { *val = *slack = -1e9; *G = *J = 0; return -1e9; }
    *G = H / var + log2(var);
    *J = I / var;
    double W = (A[0] == 0) ? C0 : Wof((1.0 - mu) / 2.0);
    *slack = *G - C0 * *J + W;
    *val = (*G + W) / *J;
    if (objmode == 0) return *val;
    return *slack - (*J < jmin ? (jmin - *J) : 0.0);
}

static int aval(int l) { return l == 0 ? 1 : l == 1 ? -1 : 0; }

static int propose(int *px, int *pnl) {
    int x = (int)(rnd64() % (unsigned long long)N), nl;
    if (rnd() < 0.85) {
        int x2 = x ^ (1 << (int)(rnd64() % (unsigned long long)m));
        if (lab[x2] == lab[x]) return 0;
        nl = lab[x2];
    } else {
        double r = rnd();
        if (k == 0 || r < 0.5) nl = r < 0.25 ? 0 : 1;
        else nl = 2 + (int)(rnd64() % (unsigned long long)(2 * k));
        if (k == 0) nl = rnd() < 0.5 ? 0 : 1;
        if (nl == lab[x]) return 0;
    }
    *px = x; *pnl = nl;
    return 1;
}

static int coins_used(const unsigned char *l) {
    int used[MAXK], c = 0;
    memset(used, 0, sizeof(used));
    for (int x = 0; x < N; x++) if (l[x] >= 2) used[(l[x] - 2) / 2] = 1;
    for (int j = 0; j < k; j++) c += used[j];
    return c;
}

static void writeline(FILE *o, long run, long seed, const unsigned char *l, double val, double slack, double G,
                      double J, double mean) {
    fprintf(o, "%ld %ld %.12f %+.12f | %.12f %.12f %.12f | %d | ", run, seed, val, slack, G, J, mean, coins_used(l));
    for (int x = 0; x < N; x++) fputc(48 + l[x], o);
    fputc('\n', o);
    fflush(o);
}

static char *getline_k(const char *spec, size_t cap) {
    char path[1024];
    int want = 0;
    strncpy(path, spec, sizeof(path) - 1); path[sizeof(path) - 1] = 0;
    char *c = strrchr(path, ':');
    if (c && c > path + 1) { want = atoi(c + 1); *c = 0; }
    FILE *f = fopen(path, "r");
    if (!f) { fprintf(stderr, "cannot open %s\n", path); exit(2); }
    char *buf = malloc(cap);
    int idx = 0;
    int fresh = 1;
    while (fgets(buf, (int)cap, f)) {
        size_t got = strlen(buf);
        int start = fresh;
        fresh = got > 0 && buf[got - 1] == '\n';
        if (!start) continue;                    /* the rest of a line longer than cap: not a new line */
        if (buf[0] == '#' || buf[0] == '\n') continue;
        if (idx++ == want) { fclose(f); return buf; }
    }
    fprintf(stderr, "line %d not found in %s\n", want, path);
    exit(2);
}

int main(int argc, char **argv) {
    if (argc < 8) { fprintf(stderr, "usage: fei_coin m k seconds seed outfile wfile init [iters] [T0] [T1] [obj] [jmin] [qbal]\n"); return 2; }
    m = atoi(argv[1]); k = atoi(argv[2]);
    double seconds = atof(argv[3]);
    long seed = atol(argv[4]);
    long iters = argc > 8 ? atol(argv[8]) : 2000000;
    double T0 = argc > 9 ? atof(argv[9]) : 2e-3, T1 = argc > 10 ? atof(argv[10]) : 2e-5;
    if (argc > 11) objmode = atoi(argv[11]);
    if (argc > 12) jmin = atof(argv[12]);
    double qbal = argc > 13 ? atof(argv[13]) : 0.9;
    double pedge = argc > 14 ? atof(argv[14]) : 0.1;
    if (m < 2 || m > 16 || k < 0 || k > MAXK) { fprintf(stderr, "need 2 <= m <= 16, 0 <= k <= %d\n", MAXK); return 2; }
    N = 1 << m;
    rs = 0x9E3779B97F4A7C15ULL ^ ((unsigned long long)seed * 0xD1B54A32D192ED03ULL);
    for (int i = 0; i < 20; i++) rnd64();

    /* value table */
    FILE *wf = fopen(argv[6], "r");
    if (!wf) { fprintf(stderr, "cannot open %s\n", argv[6]); return 2; }
    int cap = 200000; WX = malloc(sizeof(double) * cap); WY = malloc(sizeof(double) * cap); WM = 0;
    char line[512];
    while (fgets(line, sizeof(line), wf)) {
        if (line[0] == '#') continue;
        double a, b;
        if (sscanf(line, "%lf %lf", &a, &b) == 2 && WM < cap) { WX[WM] = a; WY[WM] = b; WM++; }
    }
    fclose(wf);
    C0 = Wof(0.5);

    lab = malloc(N); runbest = malloc(N); gbest = malloc(N); init0 = malloc(N);
    A = malloc(sizeof(int) * (size_t)(k + 1) * N);
    lg = malloc(sizeof(double) * (N + 1));
    pc = malloc(N);
    for (int v = 1; v <= N; v++) lg[v] = log2((double)v);
    for (int S = 0; S < N; S++) pc[S] = (unsigned char)__builtin_popcount((unsigned)S);

    /* initial state */
    size_t capl = (size_t)N + (size_t)N / 4 + 4096;
    if (!strncmp(argv[7], "hex:", 4)) {
        char *b = getline_k(argv[7] + 4, capl);
        int n0; char *hx = malloc(capl);
        if (sscanf(b, "%d %s", &n0, hx) != 2 || n0 != m) { fprintf(stderr, "hex line has n = %d, want %d\n", n0, m); return 2; }
        size_t L = strlen(hx);
        for (int x = 0; x < N; x++) {
            size_t pos = (size_t)x / 4;
            int v = 0;
            if (pos < L) { char ch = hx[L - 1 - pos]; v = ch <= '9' ? ch - '0' : (ch | 32) - 'a' + 10; }
            init0[x] = (unsigned char)((v >> (x % 4)) & 1);
        }
    } else if (!strncmp(argv[7], "lab:", 4)) {
        char *b = getline_k(argv[7] + 4, capl);
        int m0, k0; char *ls = malloc(capl);
        if (sscanf(b, "%d %d %s", &m0, &k0, ls) != 3 || m0 != m || (int)strlen(ls) != N) { fprintf(stderr, "bad lab line\n"); return 2; }
        for (int x = 0; x < N; x++) {
            int l = ls[x] - 48;
            if (l < 0 || l >= 2 + 2 * k) { fprintf(stderr, "label %d out of range at x = %d\n", l, x); return 2; }
            init0[x] = (unsigned char)l;
        }
    } else { fprintf(stderr, "init must be hex:FILE or lab:FILE\n"); return 2; }

    FILE *o = fopen(argv[5], "a");
    if (!o) { fprintf(stderr, "cannot open %s\n", argv[5]); return 2; }
    fprintf(o, "# coin m=%d k=%d wfile=%s points=%d c=%.12f init=%s iters=%ld T0=%g T1=%g obj=%d jmin=%g qbal=%g\n",
            m, k, argv[6], WM, C0, argv[7], iters, T0, T1, objmode, jmin, qbal);
    double val, slack, G, J, mean, gb = -1e18;
    memcpy(lab, init0, N); rebuild();
    evalst(&val, &slack, &G, &J, &mean);
    writeline(o, -1, seed, lab, val, slack, G, J, mean);

    time_t tend = time(NULL) + (time_t)seconds;
    int have = 0;
    for (long run = 0; time(NULL) < tend; run++) {
        memcpy(lab, (run % 2 == 1 && have) ? gbest : init0, N);
        rebuild();
        double cur = evalst(&val, &slack, &G, &J, &mean), rb = cur;
        memcpy(runbest, lab, N);
        for (long it = 0; it < iters; it++) {
            if ((it & 4095) == 0 && time(NULL) >= tend) break;
            double T = T0 * pow(T1 / T0, (double)it / (double)iters);
            int xs[4], ols[4], nch = 0, x, nl;
            nt = 0;
            if (k > 0 && rnd() < pedge) {
                /* edge move: both ends of a random edge of the cube take one coin label */
                x = (int)(rnd64() % (unsigned long long)N);
                int xb = x ^ (1 << (int)(rnd64() % (unsigned long long)m));
                nl = 2 + (int)(rnd64() % (unsigned long long)(2 * k));
                if (lab[x] == nl && lab[xb] == nl) continue;
                memcpy(sE, E, sizeof(E)); memcpy(sIS, IS, sizeof(IS)); memcpy(sWT, WT, sizeof(WT));
                xs[0] = x; ols[0] = lab[x]; setlab(x, nl);
                xs[1] = xb; ols[1] = lab[xb]; setlab(xb, nl);
                nch = 2;
            } else {
                if (!propose(&x, &nl)) continue;
                int d = aval(nl) - aval(lab[x]);
                memcpy(sE, E, sizeof(E)); memcpy(sIS, IS, sizeof(IS)); memcpy(sWT, WT, sizeof(WT));
                xs[0] = x; ols[0] = lab[x]; setlab(x, nl);
                nch = 1;
                if (d != 0 && rnd() < qbal) {
                    for (int t = 0; t < 40; t++) {
                        int xx, ll;
                        if (!propose(&xx, &ll) || xx == x) continue;
                        if (aval(ll) - aval(lab[xx]) != -d) continue;
                        xs[1] = xx; ols[1] = lab[xx]; setlab(xx, ll);
                        nch = 2;
                        break;
                    }
                }
            }
            for (int t = 0; t < nt; t++) sums(tlist[t]);
            double nw = evalst(&val, &slack, &G, &J, &mean);
            if (nw >= cur || rnd() < exp((nw - cur) / T)) {
                cur = nw;
                if (cur > rb) { rb = cur; memcpy(runbest, lab, N); }
            } else {
                for (int t = nch - 1; t >= 0; t--) setlab(xs[t], ols[t]);
                memcpy(E, sE, sizeof(E)); memcpy(IS, sIS, sizeof(IS)); memcpy(WT, sWT, sizeof(WT));
            }
            for (int t = 0; t < nt; t++) touched[tlist[t]] = 0;
            nt = 0;
        }
        memcpy(lab, runbest, N); rebuild();
        evalst(&val, &slack, &G, &J, &mean);
        writeline(o, run, seed, lab, val, slack, G, J, mean);
        if (rb > gb) { gb = rb; memcpy(gbest, runbest, N); have = 1; }
    }
    fclose(o);
    return 0;
}
