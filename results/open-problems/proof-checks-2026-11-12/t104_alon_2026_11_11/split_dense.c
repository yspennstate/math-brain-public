/* Exact coefficient test for the polyhedral split (an agent, 11 Nov 2026).

   x = sum_t z_t rho_t over the extreme rays rho_t of
       R1 = {sorted decreasing, sum 0, x_1 + x_n >= 0, x_2 + x_(n-1) >= 0}   (mode A, M = x_1 x_2)
       R2 = {sorted decreasing, sum 0, x_1 + x_n >= 0, x_2 + x_(n-1) <= 0}   (mode B, M = x_n x_(n-1))
   G = (n-4)(2Q - T^2) T - 2(n-3) P^2 + (n-1)((n^2-6n+6) T^2 + 2n Q) M,  T = sum x^2, P = sum x^3, Q = sum x^4,
   a form of degree 6 in z.  The program expands G densely (128-bit integers, monomials ranked as multisets of
   ray indices), counts negative coefficients, and checks the coefficient array against the formula at random z
   modulo 2^61 - 1.  Independent of the sympy script split_cert.py except for the rays file.

   Build: cc -O2 -o split_dense split_dense.c ; run: ./split_dense A rays_R1_n14.txt
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

typedef __int128 i128;
typedef unsigned __int128 u128;
#define MAXK 120
#define MAXD 6
#define MAXN 40

static int k, n;
static long R[MAXK][MAXN];
static uint64_t binom[MAXK + MAXD + 2][MAXD + 2];
static uint8_t *tuptab[MAXD + 1];

typedef struct { int d; uint64_t len; i128 *c; double bnd; } poly;

static uint64_t count(int d) { return binom[k + d - 1][d]; }

static inline uint64_t rank_t(const uint8_t *t, int d) {
    uint64_t r = 0;
    for (int j = 0; j < d; j++) r += binom[t[j] + j][j + 1];
    return r;
}

static inline int next_t(uint8_t *t, int d) {
    int j = d - 1;
    while (j >= 0 && t[j] == k - 1) j--;
    if (j < 0) return 0;
    uint8_t v = (uint8_t)(t[j] + 1);
    for (int i = j; i < d; i++) t[i] = v;
    return 1;
}

static void gen_tuples(int d) {
    uint64_t len = count(d), seen = 0;
    uint8_t *tb = malloc(len * d);
    if (!tb) { fprintf(stderr, "out of memory tuples %d\n", d); exit(2); }
    memset(tb, 0xFF, len * d);
    uint8_t t[MAXD];
    memset(t, 0, sizeof t);
    do {
        uint64_t r = rank_t(t, d);
        if (r >= len) { fprintf(stderr, "rank out of range\n"); exit(2); }
        if (tb[r * d] != 0xFF) { fprintf(stderr, "rank collision d=%d\n", d); exit(2); }
        memcpy(tb + r * d, t, d);
        seen++;
    } while (next_t(t, d));
    if (seen != len) { fprintf(stderr, "tuple count mismatch d=%d\n", d); exit(2); }
    tuptab[d] = tb;
}

static poly pnew(int d) {
    poly p; p.d = d; p.len = count(d); p.bnd = 0;
    p.c = calloc(p.len, sizeof(i128));
    if (!p.c) { fprintf(stderr, "out of memory deg %d\n", d); exit(2); }
    return p;
}

static double linf(const poly *A) {
    i128 m = 0;
    for (uint64_t i = 0; i < A->len; i++) { i128 v = A->c[i] < 0 ? -A->c[i] : A->c[i]; if (v > m) m = v; }
    return (double)m;
}

static void chk(const poly *p, const char *what) {
    if (!(p->bnd < 1e37)) { fprintf(stderr, "overflow bound reached in %s: %g\n", what, p->bnd); exit(3); }
}

static void addscaled(poly *out, const poly *A, long s) {
    out->bnd += (double)(s < 0 ? -s : s) * linf(A);
    chk(out, "addscaled");
    for (uint64_t i = 0; i < A->len; i++) out->c[i] += (i128)s * A->c[i];
}

static void mulacc(poly *out, const poly *A, const poly *B, long s) {
    int da = A->d, db = B->d, d = da + db;
    out->bnd += (double)binom[d][da] * (double)(s < 0 ? -s : s) * linf(A) * linf(B);
    chk(out, "mulacc");
    const uint8_t *TA = tuptab[da], *TB = tuptab[db];
    uint64_t nb = 0, *ib = malloc((B->len ? B->len : 1) * sizeof(uint64_t));
    for (uint64_t j = 0; j < B->len; j++) if (B->c[j]) ib[nb++] = j;
    for (uint64_t i = 0; i < A->len; i++) {
        i128 a = A->c[i];
        if (!a) continue;
        a *= s;
        const uint8_t *ta = TA + i * da;
        for (uint64_t jj = 0; jj < nb; jj++) {
            uint64_t j = ib[jj];
            const uint8_t *tb = TB + j * db;
            uint8_t m[MAXD];
            int x = 0, y = 0, z = 0;
            while (x < da && y < db) m[z++] = ta[x] <= tb[y] ? ta[x++] : tb[y++];
            while (x < da) m[z++] = ta[x++];
            while (y < db) m[z++] = tb[y++];
            out->c[rank_t(m, d)] += a * B->c[j];
        }
    }
    free(ib);
}

static void p128(i128 v) {
    char buf[64]; int i = 63; buf[i] = 0;
    int neg = v < 0; u128 u = neg ? (u128)(-v) : (u128)v;
    if (!u) buf[--i] = '0';
    while (u) { buf[--i] = (char)('0' + (int)(u % 10)); u /= 10; }
    if (neg) buf[--i] = '-';
    fputs(buf + i, stdout);
}

static const uint64_t MP = ((uint64_t)1 << 61) - 1;
static inline uint64_t mred(u128 x) {
    uint64_t r = (uint64_t)(x & MP) + (uint64_t)(x >> 61);
    r = (r & MP) + (r >> 61);
    return r >= MP ? r - MP : r;
}
static inline uint64_t mmul(uint64_t a, uint64_t b) { return mred((u128)a * b); }
static inline uint64_t madd(uint64_t a, uint64_t b) { uint64_t r = a + b; return r >= MP ? r - MP : r; }
static inline uint64_t msub(uint64_t a, uint64_t b) { return a >= b ? a - b : a + MP - b; }
static inline uint64_t mfrom(i128 v) { i128 r = v % (i128)MP; if (r < 0) r += MP; return (uint64_t)r; }

static uint64_t rs = 0x9E3779B97F4A7C15ULL;
static uint64_t rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }

int main(int argc, char **argv) {
    if (argc < 3 || (argv[1][0] != 'A' && argv[1][0] != 'B')) { fprintf(stderr, "usage: split_dense A|B raysfile\n"); return 1; }
    int modeB = argv[1][0] == 'B';
    FILE *f = fopen(argv[2], "r");
    if (!f || fscanf(f, "%d %d", &n, &k) != 2 || n > MAXN || n < 5 || k > MAXK || k < 1) { fprintf(stderr, "bad rays file\n"); return 1; }
    for (int t = 0; t < k; t++) {
        long s = 0;
        for (int c = 0; c < n; c++) { if (fscanf(f, "%ld", &R[t][c]) != 1) { fprintf(stderr, "short file\n"); return 1; } s += R[t][c]; }
        int ok = s == 0 && R[t][0] + R[t][n - 1] >= 0;
        for (int c = 0; c + 1 < n; c++) if (R[t][c] < R[t][c + 1]) ok = 0;
        long e = R[t][1] + R[t][n - 2];
        if (modeB ? e > 0 : e < 0) ok = 0;
        if (!ok) { fprintf(stderr, "ray %d not in the cone\n", t); return 1; }
    }
    fclose(f);
    for (int a = 0; a < MAXK + MAXD + 2; a++) {
        binom[a][0] = 1;
        for (int b = 1; b < MAXD + 2; b++) binom[a][b] = a == 0 ? 0 : binom[a - 1][b - 1] + binom[a - 1][b];
    }
    double need = (double)count(6) * 22.0 + (double)count(4) * 16.0 * 5;
    printf("n=%d mode %c rays=%d monomials(deg 6)=%llu  memory about %.0f MB\n", n, modeB ? 'B' : 'A', k,
           (unsigned long long)count(6), need / 1048576.0);
    fflush(stdout);
    if (need > 6.0e9 && argc < 4) { fprintf(stderr, "would need more than 6 GB; pass a third argument to allow\n"); return 4; }
    clock_t t0 = clock();
    for (int d = 1; d <= 6; d++) gen_tuples(d);

    poly T = pnew(2), P = pnew(3), Q = pnew(4), M = pnew(2);
    poly *x = malloc(n * sizeof(poly));
    for (int i = 0; i < n; i++) {
        x[i] = pnew(1);
        long mx = 0;
        for (int t = 0; t < k; t++) { x[i].c[t] = R[t][i]; long v = R[t][i] < 0 ? -R[t][i] : R[t][i]; if (v > mx) mx = v; }
        x[i].bnd = (double)mx;
    }
    for (int i = 0; i < n; i++) {
        poly sq = pnew(2);
        mulacc(&sq, &x[i], &x[i], 1);
        addscaled(&T, &sq, 1);
        mulacc(&P, &sq, &x[i], 1);
        mulacc(&Q, &sq, &sq, 1);
        free(sq.c);
    }
    if (modeB) mulacc(&M, &x[n - 1], &x[n - 2], 1); else mulacc(&M, &x[0], &x[1], 1);
    poly T2 = pnew(4), U = pnew(4), K = pnew(4), G = pnew(6);
    mulacc(&T2, &T, &T, 1);
    addscaled(&U, &Q, 2);
    addscaled(&U, &T2, -1);
    addscaled(&K, &T2, (long)n * n - 6L * n + 6);
    addscaled(&K, &Q, 2L * n);
    mulacc(&G, &U, &T, n - 4);
    mulacc(&G, &P, &P, -2L * (n - 3));
    mulacc(&G, &K, &M, n - 1);
    printf("expanded in %.1f s, overflow bound %.3g\n", (double)(clock() - t0) / CLOCKS_PER_SEC, G.bnd);
    fflush(stdout);

    /* identity check at random z modulo 2^61 - 1 */
    int idok = 0;
    for (int rep = 0; rep < 3; rep++) {
        uint64_t z[MAXK], xv[MAXN];
        for (int t = 0; t < k; t++) z[t] = rnd() % MP;
        uint64_t Tm = 0, Pm = 0, Qm = 0;
        for (int i = 0; i < n; i++) {
            uint64_t v = 0;
            for (int t = 0; t < k; t++) v = madd(v, mmul(mfrom(R[t][i]), z[t]));
            xv[i] = v;
            uint64_t v2 = mmul(v, v);
            Tm = madd(Tm, v2); Pm = madd(Pm, mmul(v2, v)); Qm = madd(Qm, mmul(v2, v2));
        }
        uint64_t Mm = modeB ? mmul(xv[n - 1], xv[n - 2]) : mmul(xv[0], xv[1]);
        uint64_t T2m = mmul(Tm, Tm);
        uint64_t Um = msub(madd(Qm, Qm), T2m);
        uint64_t Km = madd(mmul(mfrom((i128)n * n - 6 * n + 6), T2m), mmul(mfrom(2 * n), Qm));
        uint64_t want = mmul(mfrom(n - 4), mmul(Um, Tm));
        want = msub(want, mmul(mfrom(2 * (n - 3)), mmul(Pm, Pm)));
        want = madd(want, mmul(mfrom(n - 1), mmul(Km, Mm)));
        uint64_t got = 0;
        const uint8_t *T6 = tuptab[6];
        for (uint64_t r = 0; r < G.len; r++) {
            if (!G.c[r]) continue;
            uint64_t v = mfrom(G.c[r]);
            const uint8_t *tp = T6 + r * 6;
            for (int j = 0; j < 6; j++) v = mmul(v, z[tp[j]]);
            got = madd(got, v);
        }
        if (got == want) idok++;
    }
    printf("identity check: %d of 3\n", idok);

    uint64_t nz = 0, neg = 0, shown = 0;
    i128 mn = 0, mxv = 0;
    const uint8_t *T6 = tuptab[6];
    uint64_t negray[MAXK]; memset(negray, 0, sizeof negray);
    for (uint64_t r = 0; r < G.len; r++) {
        i128 v = G.c[r];
        if (!v) continue;
        nz++;
        if (v > mxv) mxv = v;
        if (v < 0) {
            neg++;
            if (v < mn) mn = v;
            const uint8_t *tp = T6 + r * 6;
            for (int j = 0; j < 6; j++) if (j == 0 || tp[j] != tp[j - 1]) negray[tp[j]]++;
            if (shown < 12) {
                shown++;
                printf("  NEGATIVE "); p128(v); printf(" at rays");
                for (int j = 0; j < 6; j++) printf(" %d", tp[j]);
                printf("\n");
            }
        }
    }
    printf("nonzero %llu of %llu, negative %llu, min ", (unsigned long long)nz, (unsigned long long)G.len, (unsigned long long)neg);
    p128(mn); printf(", max "); p128(mxv); printf("\n");
    if (neg) {
        printf("negative monomials per ray:");
        for (int t = 0; t < k; t++) if (negray[t]) printf(" %d:%llu", t, (unsigned long long)negray[t]);
        printf("\n");
    }
    printf("RESULT n=%d mode %c rays %d negative %llu identity %d/3 time %.1f s\n", n, modeB ? 'B' : 'A', k,
           (unsigned long long)neg, idok, (double)(clock() - t0) / CLOCKS_PER_SEC);
    return neg ? 10 : (idok == 3 ? 0 : 5);
}
