"""Build cone_chunk.c from cone_dense.c: same polynomials K, Nh, W, Dh; the degree-8 product is formed one chunk at a
time (all monomials whose smallest ray index is s), so the peak memory is binom(k+6,7) coefficients, not binom(k+7,8)."""
import io
src = io.open("cone_dense.c", encoding="utf-8", newline="").read().replace("\r\n", "\n")
head, rest = src.split("    poly H = pnew(8);\n", 1)
helpers = r'''
typedef struct { uint64_t *idx; uint64_t start[MAXK + 1]; } grp;

/* nonzero terms of A grouped by the smallest ray index of the monomial */
static grp mkgrp(const poly *A) {
    grp g; int d = A->d; const uint8_t *TA = tuptab[d];
    uint64_t cnt[MAXK + 1]; memset(cnt, 0, sizeof cnt);
    for (uint64_t i = 0; i < A->len; i++) if (A->c[i]) cnt[TA[i * d]]++;
    g.start[0] = 0;
    for (int f = 0; f < k; f++) g.start[f + 1] = g.start[f] + cnt[f];
    g.idx = malloc((g.start[k] ? g.start[k] : 1) * sizeof(uint64_t));
    uint64_t pos[MAXK + 1]; memcpy(pos, g.start, sizeof pos);
    for (uint64_t i = 0; i < A->len; i++) if (A->c[i]) g.idx[pos[TA[i * d]]++] = i;
    return g;
}

static inline uint64_t rank7s(const uint8_t *u, int s) {
    uint64_t r = 0;
    for (int j = 0; j < 7; j++) r += binom[u[j] - s + j][j + 1];
    return r;
}

static void pairs(i128 *out, const poly *A, const grp *GA, uint64_t a0, uint64_t a1,
                  const poly *B, const grp *GB, uint64_t b0, uint64_t b1, long sc, int s) {
    int da = A->d, db = B->d;
    const uint8_t *TA = tuptab[da], *TB = tuptab[db];
    for (uint64_t ii = a0; ii < a1; ii++) {
        uint64_t i = GA->idx[ii];
        i128 a = A->c[i] * sc;
        const uint8_t *ta = TA + i * da;
        for (uint64_t jj = b0; jj < b1; jj++) {
            uint64_t j = GB->idx[jj];
            const uint8_t *tb = TB + j * db;
            uint8_t m[MAXD];
            int x = 0, y = 0, z = 0;
            while (x < da && y < db) m[z++] = ta[x] <= tb[y] ? ta[x++] : tb[y++];
            while (x < da) m[z++] = ta[x++];
            while (y < db) m[z++] = tb[y++];
            out[rank7s(m + 1, s)] += a * B->c[j];
        }
    }
}

/* all products whose smallest ray index is exactly s */
static void mulacc_chunk(i128 *out, const poly *A, const grp *GA, const poly *B, const grp *GB, long sc, int s) {
    pairs(out, A, GA, GA->start[s], GA->start[s + 1], B, GB, GB->start[s], GB->start[k], sc, s);
    pairs(out, A, GA, GA->start[s + 1], GA->start[k], B, GB, GB->start[s], GB->start[s + 1], sc, s);
}

int main('''
head = head.replace("\nint main(", helpers, 1)
tail = r'''    double bound = (double)binom[8][4] * linf(&K) * linf(&Nh)
                 + (double)binom[8][2] * 2.0 * (n - 3) * linf(&W) * linf(&Dh);
    if (!(bound < 1e37)) { fprintf(stderr, "overflow bound reached: %g\n", bound); return 3; }
    grp GK = mkgrp(&K), GN = mkgrp(&Nh), GW = mkgrp(&W), GD = mkgrp(&Dh);
    enum { NPT = 3 };
    uint64_t z[NPT][MAXK], hv[NPT] = {0, 0, 0};
    for (int q = 0; q < NPT; q++) for (int t = 0; t < k; t++) z[q][t] = rnd() % MP;
    uint64_t nz = 0, neg = 0, zero = 0, seen = 0;
    i128 mn = 0, mx = 0; int have = 0;
    uint8_t tmin[MAXD]; memset(tmin, 0, sizeof tmin);
    printf("n=%d rays=%d monomials=%llu (in %d chunks)\n", n, k, (unsigned long long)binom[k + 7][8], k);
    for (int s = 0; s < k; s++) {
        uint64_t len = binom[k - s + 6][7];
        i128 *out = calloc(len, sizeof(i128));
        if (!out) { fprintf(stderr, "out of memory chunk %d\n", s); return 2; }
        mulacc_chunk(out, &K, &GK, &Nh, &GN, 1, s);
        mulacc_chunk(out, &W, &GW, &Dh, &GD, 2L * (n - 3), s);
        uint8_t u[MAXD]; memset(u, s, sizeof u);
        do {
            i128 v = out[rank7s(u, s)];
            seen++;
            if (v == 0) {
                zero++;
                if (zero <= 80) { printf("  zero coefficient at rays %d", s); for (int j = 0; j < 7; j++) printf(" %d", u[j]); printf("\n"); }
                int pure = 1; for (int j = 0; j < 7; j++) if (u[j] != s) pure = 0;
                if (pure) { printf("pure power zero on ray %d:", s); for (int c = 0; c < n; c++) printf(" %ld", R[s][c]); printf("\n"); }
            } else {
                nz++;
                if (v < 0) { neg++; if (neg <= 12) { printf("  NEGATIVE "); p128(v); printf(" at rays %d", s); for (int j = 0; j < 7; j++) printf(" %d", u[j]); printf("\n"); } }
                if (!have || v < mn) { mn = v; tmin[0] = (uint8_t)s; memcpy(tmin + 1, u, 7); }
                if (!have || v > mx) mx = v;
                have = 1;
                uint64_t cm = mfrom(v);
                for (int q = 0; q < NPT; q++) {
                    uint64_t pr = mmul(cm, z[q][s]);
                    for (int j = 0; j < 7; j++) pr = mmul(pr, z[q][u[j]]);
                    hv[q] = madd(hv[q], pr);
                }
            }
        } while (next_t(u, 7));
        free(out);
        fprintf(stderr, "chunk %d of %d done, %llu coefficients, negative so far %llu, %.0f s\n", s, k,
                (unsigned long long)len, (unsigned long long)neg, (double)(clock() - t0) / CLOCKS_PER_SEC);
        fflush(stdout);
    }
    int bad = 0;
'''
i = rest.index("    for (int q = 0; q < NPT; q++) {\n        uint64_t Tm = 0")
j = rest.index('    printf("seen=%llu')
k2 = rest.index('    for (int tt = 0; tt < k; tt++) {\n        uint8_t pt[MAXD]')
body = tail + rest[i:j] + rest[j:k2].replace("H.bnd", "bound").replace("tb,", "0.0,") + "    return neg ? 4 : 0;\n}\n"
out = head + body
out = out.replace("Dense exact coefficient certificate", "Chunked exact coefficient certificate", 1)
io.open("cone_chunk.c", "w", encoding="utf-8", newline="\n").write(out)
print(len(out))
