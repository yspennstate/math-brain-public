/* fei_gate5.c - every Boolean function on 5 inputs as a tower gate at every input bias, against a Bellman table.
 *
 * Inputs are independent copies of a state of bias p (Pr[input = -1] = p; table bit x set <=> F(x) = -1, bit i of x
 * set <=> input i is -1).  In the p-biased basis F has coefficients a_S; V = sum_{S != 0} a_S^2,
 *   G_p = entropy (bits) of a_S^2 / V over S != 0,   J_p = sum |S| a_S^2 / V,   p' = (1 - a_0) / 2,
 *   slack = G_p + W(p') - J_p W(p).
 * slack > 0 at some p means the table is not yet the value of the gate set; at p = 1/2 it is the entry test of
 * fei_entry5.c (same numbers, a built-in check).
 * Reductions: bit 0 clear (F and -F: same G, J, p' -> 1 - p', table symmetric); one table per orbit of input
 * permutations is enough, so only tables whose five half-cube counts are non-decreasing are evaluated; biases
 * p <= 1/2 are enough because the bias 1 - p is the table read backwards.
 * usage: fei_gate5 WFILE chunk nchunks outfile [nbias=48]     biases p = j / (2 nbias), j = 2..nbias
 * output: per bias the 6 best tables: p slack G J p' hex
 */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define TOP 6
#define MAXB 200
static double Wt[20000], Ww[20000];
static int Wn;

static double w_at(double p) {
    double x = log2(p / (1 - p));
    if (x <= Wt[0]) return Ww[0];
    if (x >= Wt[Wn - 1]) return Ww[Wn - 1];
    int lo = 0, hi = Wn - 1;
    while (hi - lo > 1) { int mid = (lo + hi) / 2; if (Wt[mid] <= x) lo = mid; else hi = mid; }
    double f = (x - Wt[lo]) / (Wt[hi] - Wt[lo]);
    return Ww[lo] + f * (Ww[hi] - Ww[lo]);
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: fei_gate5 WFILE chunk nchunks outfile [nbias]\n"); return 2; }
    FILE *fw = fopen(argv[1], "r");
    if (!fw) { perror("wfile"); return 2; }
    char line[256];
    while (fgets(line, sizeof line, fw)) {
        if (line[0] == '#') continue;
        if (sscanf(line, "%lf %lf", &Wt[Wn], &Ww[Wn]) == 2) Wn++;
    }
    fclose(fw);
    long chunk = atol(argv[2]), nch = atol(argv[3]);
    int nb = argc > 5 ? atoi(argv[5]) : 48;
    int NB = 0;
    double P[MAXB], Q[MAXB], R[MAXB], WP[MAXB];
    for (int j = 2; j <= nb && NB < MAXB; j++) {
        P[NB] = j / (2.0 * nb); Q[NB] = 1 - P[NB]; R[NB] = sqrt(P[NB] * Q[NB]); WP[NB] = w_at(P[NB]); NB++;
    }
    int pc[32];
    for (int s = 0; s < 32; s++) pc[s] = __builtin_popcount(s);
    static double ts[MAXB][TOP], tg[MAXB][TOP], tj[MAXB][TOP], tp[MAXB][TOP];
    static uint32_t tt[MAXB][TOP];
    static int nt[MAXB];
    uint64_t total = 1ull << 31, lo = total / nch * chunk, hi = (chunk == nch - 1) ? total : total / nch * (chunk + 1);
    uint64_t kept = 0;
    for (uint64_t u = lo; u < hi; u++) {
        uint32_t tab = (uint32_t)(u << 1);        /* bit 0 clear */
        if (!tab) continue;
        int s0 = __builtin_popcount(tab & 0xAAAAAAAAu), s1 = __builtin_popcount(tab & 0xCCCCCCCCu);
        if (s0 > s1) continue;
        int s2 = __builtin_popcount(tab & 0xF0F0F0F0u);
        if (s1 > s2) continue;
        int s3 = __builtin_popcount(tab & 0xFF00FF00u);
        if (s2 > s3) continue;
        int s4 = __builtin_popcount(tab & 0xFFFF0000u);
        if (s3 > s4) continue;
        kept++;
        double f0[32];
        for (int x = 0; x < 32; x++) f0[x] = ((tab >> x) & 1) ? -1.0 : 1.0;
        for (int b = 0; b < NB; b++) {
            double a[32], p = P[b], q = Q[b], r = R[b];
            for (int x = 0; x < 32; x++) a[x] = f0[x];
            for (int h = 1; h < 32; h <<= 1)
                for (int i = 0; i < 32; i += 2 * h)
                    for (int j = i; j < i + h; j++) { double u0 = a[j], u1 = a[j + h]; a[j] = q * u0 + p * u1; a[j + h] = r * (u0 - u1); }
            double V = 0, inf = 0, e = 0;
            for (int s = 1; s < 32; s++) { double w = a[s] * a[s]; V += w; inf += pc[s] * w; if (w > 1e-300) e -= w * log2(w); }
            if (V < 1e-12) continue;
            double J = inf / V, G = e / V + log2(V), pp = 0.5 * (1 - a[0]);
            if (pp < 1e-12 || pp > 1 - 1e-12) continue;
            double sl = G + w_at(pp) - J * WP[b];
            int n = nt[b];
            if (n < TOP || sl > ts[b][n - 1]) {
                int i = n < TOP ? nt[b]++ : TOP - 1;
                while (i > 0 && ts[b][i - 1] < sl) { ts[b][i] = ts[b][i - 1]; tg[b][i] = tg[b][i - 1]; tj[b][i] = tj[b][i - 1]; tp[b][i] = tp[b][i - 1]; tt[b][i] = tt[b][i - 1]; i--; }
                ts[b][i] = sl; tg[b][i] = G; tj[b][i] = J; tp[b][i] = pp; tt[b][i] = tab;
            }
        }
    }
    FILE *fo = fopen(argv[4], "w");
    if (!fo) { perror("out"); return 2; }
    fprintf(fo, "# gate5 wfile=%s points=%d c=%.12f chunk=%ld of %ld nbias=%d evaluated=%llu\n", argv[1], Wn, w_at(0.5), chunk, nch, NB, (unsigned long long)kept);
    for (int b = 0; b < NB; b++)
        for (int i = 0; i < nt[b]; i++)
            fprintf(fo, "%.6f %+.9f %.9f %.9f %.9f %08x\n", P[b], ts[b][i], tg[b][i], tj[b][i], tp[b][i], tt[b][i]);
    fclose(fo);
    return 0;
}
