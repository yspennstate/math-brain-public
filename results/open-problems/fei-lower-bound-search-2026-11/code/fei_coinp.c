/* fei_coinp.c - fei_coin at a biased input measure.

   All m + k inputs are independent with Pr[input bit = 1] = p (bit 1 is the value -1).  The gate is affine in the
   k coin inputs: every x in {0,1}^m carries one label
       0: g = +1,  1: g = -1,  2+2j: g = Y_j,  3+2j: g = -Y_j        (Y_j = 1 - 2 * coin bit j).
   In the p-biased orthonormal basis g = a(x) + sum_j b_j(x) phi(y_j) with a = +-1 or +-(1-2p) and
   b_j = -+2 sqrt(p(1-p)), so the p-biased spectrum is the union of the spectra of a and of the b_j.

   Score, with W the value table and all inputs taken as towers of bias p:
       G = entropy of the normalised non-constant weights, J = total influence / Var, p' = Pr[g = -1],
       value = (G + W(p')) / J,     slack = G - W(p) J + W(p').
   slack > 0 means the gate beats the table at bias p (Bellman excess times J).  At p = 1/2 this is fei_coin.

   usage: fei_coinp p m k seconds seed outfile wfile init [iters] [T0] [T1] [jmin] [qbal] [pedge]
     init hex:FILE[:LINE]   library line "m hex" (bit x of the integer is 1 when g(x) = -1)
          lab:FILE[:LINE]   line "m k labels", one character per x, chr(48 + label)
     output lines:  run seed value slack | G J mean | coins used | labels          (run -1 is the start state)
*/
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAXK 38

static int m, k, N;
static unsigned char *lab, *runbest, *gbest, *init0;
static double *A, *tmpv;
static unsigned char *pc;
static double E[MAXK + 1], IS[MAXK + 1], WT[MAXK + 1], sE[MAXK + 1], sIS[MAXK + 1], sWT[MAXK + 1];
static int touched[MAXK + 1], tlist[MAXK + 1], nt;
static double *WX, *WY;
static int WM;
static double P, SQ, MUC, SIG2, WP;
static double powS[20], powP[20], powQ[20], powMS[20];
static unsigned long long rs;
static double jmin = 1.05;

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

/* add d * (column x of the biased transform) to array r */
static void upd(int r, int x, double d) {
    double *a = A + (size_t)r * N;
    int nx = pc[x];
    double F1[20], F0[20];
    for (int c = 0; c <= nx; c++) F1[c] = powS[c] * powP[nx - c];             /* S_i = 1 or 0 where x_i = 1 */
    for (int c = 0; c <= m - nx; c++) F0[c] = powMS[c] * powQ[m - nx - c];    /* S_i = 1 or 0 where x_i = 0 */
    int nxm = (N - 1) & ~x;
    for (int S = 0; S < N; S++) a[S] += d * F1[pc[S & x]] * F0[pc[S & nxm]];
}

static void sums(int r) {
    double *a = A + (size_t)r * N;
    double e = 0, is = 0, wt = 0, sc = r ? SIG2 : 1.0;
    for (int S = (r == 0); S < N; S++) {
        double w = a[S] * a[S] * sc;
        if (w < 1e-300) continue;
        e -= w * log2(w);
        is += w * pc[S];
        wt += w;
    }
    E[r] = e; IS[r] = is; WT[r] = wt;
}

static void touch(int r) { if (!touched[r]) { touched[r] = 1; tlist[nt++] = r; } }

/* value of the constant part and of the coin part for a label */
static double aval(int l) { return l == 0 ? 1.0 : l == 1 ? -1.0 : (l & 1) ? -MUC : MUC; }
static double bval(int l) { return (l & 1) ? 1.0 : -1.0; }

static void setlab(int x, int nl) {
    int ol = lab[x];
    if (ol == nl) return;
    double da = aval(nl) - aval(ol);
    if (da != 0.0) { upd(0, x, da); touch(0); }
    if (ol >= 2) { int j = (ol - 2) / 2; upd(1 + j, x, -bval(ol)); touch(1 + j); }
    if (nl >= 2) { int j = (nl - 2) / 2; upd(1 + j, x, bval(nl)); touch(1 + j); }
    lab[x] = (unsigned char)nl;
}

static void transform(double *v) {
    for (int i = 0; i < m; i++) {
        int h = 1 << i;
        for (int base = 0; base < N; base += 2 * h)
            for (int t = base; t < base + h; t++) {
                double u0 = v[t], u1 = v[t + h];
                v[t] = (1.0 - P) * u0 + P * u1;
                v[t + h] = SQ * (u1 - u0);
            }
    }
}

static void rebuild(void) {
    for (int r = 0; r <= k; r++) {
        double *a = A + (size_t)r * N;
        for (int x = 0; x < N; x++) {
            int l = lab[x];
            if (r == 0) a[x] = aval(l);
            else a[x] = (l >= 2 && (l - 2) / 2 == r - 1) ? bval(l) : 0.0;
        }
        transform(a);
        sums(r);
    }
}

static double evalst(double *val, double *slack, double *G, double *J, double *mean) {
    double H = 0, I = 0;
    for (int r = 0; r <= k; r++) { H += E[r]; I += IS[r]; if (r) I += WT[r]; }
    double mu = A[0], var = 1.0 - mu * mu;
    *mean = mu;
    if (var < 1e-9) { *val = *slack = -1e9; *G = *J = 0; return -1e9; }
    *G = H / var + log2(var);
    *J = I / var;
    double W = Wof((1.0 - mu) / 2.0);
    *slack = *G - WP * *J + W;
    *val = (*G + W) / *J;
    return *slack - (*J < jmin ? 20.0 * (jmin - *J) : 0.0);
}

static int sgn(int l) { return l == 0 ? 1 : l == 1 ? -1 : 0; }

static int propose(int *px, int *pnl) {
    int x = (int)(rnd64() % (unsigned long long)N), nl;
    if (rnd() < 0.85) {
        int x2 = x ^ (1 << (int)(rnd64() % (unsigned long long)m));
        if (lab[x2] == lab[x]) return 0;
        nl = lab[x2];
    } else {
        double r = rnd();
        if (k == 0 || r < 0.5) nl = rnd() < 0.5 ? 0 : 1;
        else nl = 2 + (int)(rnd64() % (unsigned long long)(2 * k));
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
    if (argc < 9) { fprintf(stderr, "usage: fei_coinp p m k seconds seed outfile wfile init [iters] [T0] [T1] [jmin] [qbal] [pedge]\n"); return 2; }
    P = atof(argv[1]);
    m = atoi(argv[2]); k = atoi(argv[3]);
    double seconds = atof(argv[4]);
    long seed = atol(argv[5]);
    long iters = argc > 9 ? atol(argv[9]) : 1000000;
    double T0 = argc > 10 ? atof(argv[10]) : 1e-2, T1 = argc > 11 ? atof(argv[11]) : 2e-5;
    if (argc > 12) jmin = atof(argv[12]);
    double qbal = argc > 13 ? atof(argv[13]) : 0.5;
    double pedge = argc > 14 ? atof(argv[14]) : 0.1;
    if (m < 2 || m > 16 || k < 0 || k > MAXK || P <= 0 || P >= 1) { fprintf(stderr, "need 2 <= m <= 16, 0 <= k <= %d, 0 < p < 1\n", MAXK); return 2; }
    N = 1 << m;
    SQ = sqrt(P * (1.0 - P)); MUC = 1.0 - 2.0 * P; SIG2 = 4.0 * P * (1.0 - P);
    for (int c = 0; c < 20; c++) {
        powS[c] = pow(SQ, c); powMS[c] = (c & 1) ? -powS[c] : powS[c];
        powP[c] = pow(P, c); powQ[c] = pow(1.0 - P, c);
    }
    rs = 0x9E3779B97F4A7C15ULL ^ ((unsigned long long)seed * 0xD1B54A32D192ED03ULL);
    for (int i = 0; i < 20; i++) rnd64();

    FILE *wf = fopen(argv[7], "r");
    if (!wf) { fprintf(stderr, "cannot open %s\n", argv[7]); return 2; }
    int cap = 200000; WX = malloc(sizeof(double) * cap); WY = malloc(sizeof(double) * cap); WM = 0;
    char line[512];
    while (fgets(line, sizeof(line), wf)) {
        if (line[0] == '#') continue;
        double a, b;
        if (sscanf(line, "%lf %lf", &a, &b) == 2 && WM < cap) { WX[WM] = a; WY[WM] = b; WM++; }
    }
    fclose(wf);
    WP = Wof(P);

    lab = malloc(N); runbest = malloc(N); gbest = malloc(N); init0 = malloc(N);
    A = malloc(sizeof(double) * (size_t)(k + 1) * N);
    pc = malloc(N);
    for (int S = 0; S < N; S++) pc[S] = (unsigned char)__builtin_popcount((unsigned)S);

    size_t capl = (size_t)N + (size_t)N / 4 + 4096;
    if (!strncmp(argv[8], "hex:", 4)) {
        char *b = getline_k(argv[8] + 4, capl);
        int n0; char *hx = malloc(capl);
        if (sscanf(b, "%d %s", &n0, hx) != 2 || n0 != m) { fprintf(stderr, "hex line has n = %d, want %d\n", n0, m); return 2; }
        size_t L = strlen(hx);
        for (int x = 0; x < N; x++) {
            size_t pos = (size_t)x / 4;
            int v = 0;
            if (pos < L) { char ch = hx[L - 1 - pos]; v = ch <= '9' ? ch - '0' : (ch | 32) - 'a' + 10; }
            init0[x] = (unsigned char)((v >> (x % 4)) & 1);
        }
    } else if (!strncmp(argv[8], "lab:", 4)) {
        char *b = getline_k(argv[8] + 4, capl);
        int m0, k0; char *ls = malloc(capl);
        if (sscanf(b, "%d %d %s", &m0, &k0, ls) != 3 || m0 != m || (int)strlen(ls) != N) { fprintf(stderr, "bad lab line\n"); return 2; }
        for (int x = 0; x < N; x++) {
            int l = ls[x] - 48;
            if (l < 0 || l >= 2 + 2 * k) { fprintf(stderr, "label %d out of range at x = %d\n", l, x); return 2; }
            init0[x] = (unsigned char)l;
        }
    } else { fprintf(stderr, "init must be hex:FILE or lab:FILE\n"); return 2; }

    FILE *o = fopen(argv[6], "a");
    if (!o) { fprintf(stderr, "cannot open %s\n", argv[6]); return 2; }
    fprintf(o, "# coinp p=%.12f m=%d k=%d wfile=%s points=%d Wp=%.12f init=%s iters=%ld T0=%g T1=%g jmin=%g qbal=%g pedge=%g\n",
            P, m, k, argv[7], WM, WP, argv[8], iters, T0, T1, jmin, qbal, pedge);
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
            if ((it & 1023) == 0 && time(NULL) >= tend) break;
            double T = T0 * pow(T1 / T0, (double)it / (double)iters);
            int xs[4], ols[4], nch = 0, x, nl;
            nt = 0;
            if (k > 0 && rnd() < pedge) {
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
                int d = sgn(nl) - sgn(lab[x]);
                memcpy(sE, E, sizeof(E)); memcpy(sIS, IS, sizeof(IS)); memcpy(sWT, WT, sizeof(WT));
                xs[0] = x; ols[0] = lab[x]; setlab(x, nl);
                nch = 1;
                if (d != 0 && rnd() < qbal) {
                    for (int t = 0; t < 40; t++) {
                        int xx, ll;
                        if (!propose(&xx, &ll) || xx == x) continue;
                        if (sgn(ll) - sgn(lab[xx]) != -d) continue;
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
