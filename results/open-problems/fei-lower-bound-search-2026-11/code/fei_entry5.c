/* fei_entry5.c - every Boolean function on 5 uniform inputs as an entry gate against a Bellman table.
 *
 * For f : {0,1}^5 -> {+1,-1} (table bit x set <=> f(x) = -1) with mean mu and variance v = 1 - mu^2:
 *   G = entropy (bits) of the non-empty Fourier weights divided by v,  J = total influence / v,  p' = (1 - mu)/2,
 *   slack = G - c J + W(p'),  c = W(1/2).   slack > 0 would be a new lower bound.
 * Tables with bit 0 clear only (f and -f have the same G, J and the table is symmetric in p').
 * usage: fei_entry5 WFILE chunk nchunks outfile     (chunk in 0..nchunks-1 splits the 2^31 tables by their top bits)
 * output: best slack for every output bias, then the 40 best tables: slack G J p' hex
 */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define TOP 40
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
    if (argc < 5) { fprintf(stderr, "usage: fei_entry5 WFILE chunk nchunks outfile\n"); return 2; }
    FILE *fw = fopen(argv[1], "r");
    if (!fw) { perror("wfile"); return 2; }
    char line[256];
    while (fgets(line, sizeof line, fw)) {
        if (line[0] == '#') continue;
        if (sscanf(line, "%lf %lf", &Wt[Wn], &Ww[Wn]) == 2) Wn++;
    }
    fclose(fw);
    long chunk = atol(argv[2]), nch = atol(argv[3]);
    double c = w_at(0.5);
    double wlw[33];                       /* -w log2 w for w = k^2/1024, k = |coefficient| */
    for (int k = 0; k <= 32; k++) { double w = k * k / 1024.0; wlw[k] = k ? -w * log2(w) : 0.0; }
    double Wp[33];                        /* W at p' = ones/32 */
    for (int k = 1; k < 32; k++) Wp[k] = w_at(k / 32.0);
    int pc[32];
    for (int s = 0; s < 32; s++) pc[s] = __builtin_popcount(s);
    double best_by[33]; uint32_t arg_by[33];
    for (int k = 0; k <= 32; k++) { best_by[k] = -1e9; arg_by[k] = 0; }
    double ts[TOP], tg[TOP], tj[TOP]; uint32_t tt[TOP]; int tk[TOP]; int nt = 0;
    uint64_t total = 1ull << 31, lo = total / nch * chunk, hi = (chunk == nch - 1) ? total : total / nch * (chunk + 1);
    for (uint64_t u = lo; u < hi; u++) {
        uint32_t tab = (uint32_t)(u << 1);        /* bit 0 clear */
        int a[32];
        for (int x = 0; x < 32; x++) a[x] = ((tab >> x) & 1) ? -1 : 1;
        for (int h = 1; h < 32; h <<= 1)
            for (int i = 0; i < 32; i += 2 * h)
                for (int j = i; j < i + h; j++) { int p = a[j], q = a[j + h]; a[j] = p + q; a[j + h] = p - q; }
        int m0 = a[0];
        if (m0 == 32 || m0 == -32) continue;
        double mu = m0 / 32.0, v = 1 - mu * mu, e = 0, inf = 0;
        for (int s = 1; s < 32; s++) { int k = a[s] < 0 ? -a[s] : a[s]; e += wlw[k]; inf += pc[s] * (double)(k * k); }
        double J = inf / 1024.0 / v;
        if (J <= 1 + 1e-9) continue;
        double G = e / v + log2(v);
        int ones = (32 - m0) / 2;
        double sl = G - c * J + Wp[ones];
        if (sl > best_by[ones]) { best_by[ones] = sl; arg_by[ones] = tab; }
        if (nt < TOP || sl > ts[nt - 1]) {
            int i = nt < TOP ? nt++ : TOP - 1;
            while (i > 0 && ts[i - 1] < sl) { ts[i] = ts[i - 1]; tg[i] = tg[i - 1]; tj[i] = tj[i - 1]; tt[i] = tt[i - 1]; tk[i] = tk[i - 1]; i--; }
            ts[i] = sl; tg[i] = G; tj[i] = J; tt[i] = tab; tk[i] = ones;
        }
    }
    FILE *fo = fopen(argv[4], "w");
    if (!fo) { perror("out"); return 2; }
    fprintf(fo, "# entry5 wfile=%s points=%d c=%.12f chunk=%ld of %ld\n", argv[1], Wn, c, chunk, nch);
    for (int k = 1; k < 32; k++)
        if (best_by[k] > -1e8) fprintf(fo, "bias %2d/32 W %.6f best slack %+.9f  %08x\n", k, Wp[k], best_by[k], arg_by[k]);
    for (int i = 0; i < nt; i++) fprintf(fo, "top %+.9f G %.9f J %.9f p %2d/32 %08x\n", ts[i], tg[i], tj[i], tk[i], tt[i]);
    fclose(fo);
    return 0;
}
