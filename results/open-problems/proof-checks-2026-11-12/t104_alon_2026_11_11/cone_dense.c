/* Dense exact coefficient certificate for H >= 0 on the cone C (an agent, 11 Nov 2026).

   Third implementation, sharing no code with cone_recheck.py / cone_recheck2.py or the sympy scripts:
   C, 128-bit integers, polynomials stored densely by the rank of the monomial (a multiset of ray indices),
   rays read from a file written by rays_enum.py (vertex enumeration, not the closed formula).

   H = K*Nh + 2(n-3) W*Dh with, for x = sum_t z_t rho_t,
     T = sum x^2, P = sum x^3, Q = sum x^4, a = x_1,
     K = (n^2-6n+6) T^2 + 2n Q,  Nh = n(n-1)(T^2 - Q + 2aP - 2a^2 T) + T^2,
     Dh = n Q T - T^3 - n P^2,   W = n(n-1) a^2 - T.

   Overflow: every product A*B accumulated into a coefficient has at most binom(d, da) contributions, each of size
   at most max|A| max|B| |s|; the program keeps this bound for every polynomial and stops if it reaches 1e37
   (2^126 is 8.5e37). Identity check: H(z) from the coefficient array against the formula evaluated at
   x = sum z_t rho_t, modulo 2^61 - 1, at random z.

   Build: cc -O2 -o cone_dense cone_dense.c ; run: ./cone_dense rays_n10.txt
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

typedef __int128 i128;
typedef unsigned __int128 u128;
#define MAXK 64
#define MAXD 8
#define MAXN 32

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

/* next nondecreasing tuple with entries in 0..k-1; returns 0 after the last */
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
    uint8_t t[MAXD];
    memset(t, 0, sizeof t);
    do {
        uint64_t r = rank_t(t, d);
        if (r >= len) { fprintf(stderr, "rank out of range\n"); exit(2); }
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
    uint64_t nb = 0, *ib = malloc(B->len * sizeof(uint64_t));
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

static void pfree(poly *p) { free(p->c); p->c = NULL; }

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
    if (argc < 2) { fprintf(stderr, "usage: cone_dense raysfile\n"); return 1; }
    FILE *f = fopen(argv[1], "r");
    if (!f || fscanf(f, "%d %d", &n, &k) != 2 || n > MAXN || k > MAXK - 8) { fprintf(stderr, "bad rays file\n"); return 1; }
    for (int t = 0; t < k; t++) {
        long s = 0;
        for (int c = 0; c < n; c++) { if (fscanf(f, "%ld", &R[t][c]) != 1) { fprintf(stderr, "short file\n"); return 1; } s += R[t][c]; }
        if (s != 0 || R[t][0] + R[t][n - 1] < 0) { fprintf(stderr, "ray %d not in the cone\n", t); return 1; }
        for (int c = 0; c + 1 < n; c++) if (R[t][c] < R[t][c + 1]) { fprintf(stderr, "ray %d not ordered\n", t); return 1; }
    }
    fclose(f);
    clock_t t0 = clock();
    for (int i = 0; i < MAXK + MAXD + 2; i++)
        for (int j = 0; j < MAXD + 2; j++)
            binom[i][j] = j == 0 ? 1 : (i == 0 ? 0 : binom[i - 1][j - 1] + binom[i - 1][j]);
    for (int d = 1; d <= 6; d++) gen_tuples(d);

    poly T = pnew(2), P = pnew(3), Q = pnew(4), a = pnew(1);
    for (int c = 0; c < n; c++) {
        poly x = pnew(1), x2 = pnew(2), x3 = pnew(3), x4 = pnew(4);
        for (int t = 0; t < k; t++) x.c[t] = R[t][c];
        mulacc(&x2, &x, &x, 1); mulacc(&x3, &x2, &x, 1); mulacc(&x4, &x2, &x2, 1);
        addscaled(&T, &x2, 1); addscaled(&P, &x3, 1); addscaled(&Q, &x4, 1);
        if (c == 0) for (int t = 0; t < k; t++) a.c[t] = x.c[t];
        pfree(&x); pfree(&x2); pfree(&x3); pfree(&x4);
    }
    long nn1 = (long)n * (n - 1);
    poly a2 = pnew(2), T2 = pnew(4);
    mulacc(&a2, &a, &a, 1);
    mulacc(&T2, &T, &T, 1);
    poly K = pnew(4), Nh = pnew(4), Dh = pnew(6), W = pnew(2);
    addscaled(&K, &T2, (long)n * n - 6 * n + 6); addscaled(&K, &Q, 2L * n);
    addscaled(&Nh, &T2, nn1 + 1); addscaled(&Nh, &Q, -nn1);
    mulacc(&Nh, &a, &P, 2 * nn1); mulacc(&Nh, &a2, &T, -2 * nn1);
    mulacc(&Dh, &Q, &T, n); mulacc(&Dh, &T2, &T, -1); mulacc(&Dh, &P, &P, -n);
    addscaled(&W, &a2, nn1); addscaled(&W, &T, -1);
    poly H = pnew(8);
    mulacc(&H, &K, &Nh, 1);
    mulacc(&H, &W, &Dh, 2L * (n - 3));
    double tb = (double)(clock() - t0) / CLOCKS_PER_SEC;

    /* statistics and the modular identity check in one pass over all degree-8 monomials */
    enum { NPT = 3 };
    uint64_t z[NPT][MAXK], hv[NPT] = {0, 0, 0};
    for (int q = 0; q < NPT; q++) for (int t = 0; t < k; t++) z[q][t] = rnd() % MP;
    uint64_t nz = 0, neg = 0, zero = 0, seen = 0;
    i128 mn = 0, mx = 0; int have = 0;
    uint8_t t[MAXD], tmin[MAXD];
    memset(t, 0, sizeof t); memset(tmin, 0, sizeof tmin);
    printf("n=%d rays=%d monomials=%llu\n", n, k, (unsigned long long)H.len);
    do {
        i128 v = H.c[rank_t(t, 8)];
        seen++;
        if (v == 0) {
            zero++;
            if (zero <= 60) { printf("  zero coefficient at rays"); for (int j = 0; j < 8; j++) printf(" %d", t[j]); printf("\n"); }
        } else {
            nz++;
            if (v < 0) { neg++; if (neg <= 12) { printf("  NEGATIVE "); p128(v); printf(" at rays"); for (int j = 0; j < 8; j++) printf(" %d", t[j]); printf("\n"); } }
            if (!have || v < mn) { mn = v; memcpy(tmin, t, 8); }
            if (!have || v > mx) mx = v;
            have = 1;
            uint64_t cm = mfrom(v);
            for (int q = 0; q < NPT; q++) {
                uint64_t pr = cm;
                for (int j = 0; j < 8; j++) pr = mmul(pr, z[q][t[j]]);
                hv[q] = madd(hv[q], pr);
            }
        }
    } while (next_t(t, 8));
    int bad = 0;
    for (int q = 0; q < NPT; q++) {
        uint64_t Tm = 0, Pm = 0, Qm = 0, am = 0;
        for (int c = 0; c < n; c++) {
            uint64_t x = 0;
            for (int tt = 0; tt < k; tt++) x = madd(x, mmul(mfrom((i128)R[tt][c]), z[q][tt]));
            uint64_t x2 = mmul(x, x);
            Tm = madd(Tm, x2); Pm = madd(Pm, mmul(x2, x)); Qm = madd(Qm, mmul(x2, x2));
            if (c == 0) am = x;
        }
        uint64_t T2m = mmul(Tm, Tm), a2m = mmul(am, am);
        uint64_t Km = madd(mmul(mfrom((i128)n * n - 6 * n + 6), T2m), mmul(mfrom(2 * n), Qm));
        uint64_t in = msub(madd(msub(T2m, Qm), mmul(2, mmul(am, Pm))), mmul(2, mmul(a2m, Tm)));
        uint64_t Nm = madd(mmul(mfrom(nn1), in), T2m);
        uint64_t Dm = msub(msub(mmul(mfrom(n), mmul(Qm, Tm)), mmul(T2m, Tm)), mmul(mfrom(n), mmul(Pm, Pm)));
        uint64_t Wm = msub(mmul(mfrom(nn1), a2m), Tm);
        uint64_t Hm = madd(mmul(Km, Nm), mmul(mfrom(2 * (n - 3)), mmul(Wm, Dm)));
        if (Hm != hv[q]) bad++;
    }
    printf("seen=%llu nonzero=%llu negative=%llu zero=%llu identity_mismatch=%d of %d\n",
           (unsigned long long)seen, (unsigned long long)nz, (unsigned long long)neg, (unsigned long long)zero, bad, NPT);
    printf("min_coeff="); p128(mn); printf(" at rays"); for (int j = 0; j < 8; j++) printf(" %d", tmin[j]);
    printf("\nmax_coeff="); p128(mx);
    printf("\noverflow_bound=%g (limit 1e37) build_seconds=%.1f total_seconds=%.1f\n", H.bnd, tb,
           (double)(clock() - t0) / CLOCKS_PER_SEC);
    for (int tt = 0; tt < k; tt++) {
        uint8_t pt[MAXD]; memset(pt, tt, 8);
        if (H.c[rank_t(pt, 8)] == 0) { printf("pure power zero on ray %d:", tt); for (int c = 0; c < n; c++) printf(" %ld", R[tt][c]); printf("\n"); }
    }
    return neg ? 4 : 0;
}
