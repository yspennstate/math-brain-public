/* Exhaustive census of the up-ratio functional B on Boolean functions of 5 variables.
   f: {0,1}^5 -> {+1,-1}, truth table tt (bit x set <=> f(x) = -1). Only tt with bit 0 clear (f(0)=+1); f and -f agree.
   c[S] = sum_x f(x) (-1)^{S.x}  (integer, |c| <= 32),  mu(S) = c^2/1024,  up(S) = sum_{U >= S} mu(U).
   H = sum mu log2(1/mu),  B = sum mu log2(up/mu),  I = sum |S| mu,  Var = 1 - mu(0).
   usage: census5 lo hi out_prefix      (range of tt >> 1, i.e. 31-bit index)
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

static double L[1025];
static int pc[32];

typedef struct { double v; uint32_t tt; double H, B, I, var; } best_t;
static void upd(best_t *b, double v, uint32_t tt, double H, double B, double I, double var) {
    if (v > b->v) { b->v = v; b->tt = tt; b->H = H; b->B = B; b->I = I; b->var = var; }
}

int main(int argc, char **argv) {
    if (argc < 4) return 2;
    uint64_t lo = strtoull(argv[1], 0, 10), hi = strtoull(argv[2], 0, 10);
    for (int k = 1; k <= 1024; k++) L[k] = log2((double)k);
    for (int s = 0; s < 32; s++) pc[s] = __builtin_popcount(s);
    /* max B and max H for each (|c0|/2, Iint): Iint = sum |S| c^2 in [0, 5120] */
    static float maxB[17][5121], maxH[17][5121];
    static uint32_t argB[17][5121];
    for (int a = 0; a < 17; a++) for (int i = 0; i <= 5120; i++) { maxB[a][i] = -1; maxH[a][i] = -1; }
    best_t bBI = {-1}, bHI = {-1}, bBbal = {-1}, bHbal = {-1}, bT1 = {-1}, bBIv = {-1}, bHIv = {-1};
    uint64_t cnt = 0;
    double worst_t1 = -1e9;
    for (uint64_t idx = lo; idx < hi; idx++) {
        uint32_t tt = (uint32_t)(idx << 1);
        int c[32];
        for (int x = 0; x < 32; x++) c[x] = 1 - 2 * (int)((tt >> x) & 1);
        for (int h = 1; h < 32; h <<= 1)
            for (int x = 0; x < 32; x++) if (!(x & h)) { int u = c[x], v = c[x | h]; c[x] = u + v; c[x | h] = u - v; }
        int m[32], up[32], Iint = 0;
        for (int s = 0; s < 32; s++) { m[s] = c[s] * c[s]; up[s] = m[s]; Iint += pc[s] * m[s]; }
        if (Iint == 0) continue;
        for (int h = 1; h < 32; h <<= 1)
            for (int x = 0; x < 32; x++) if (!(x & h)) up[x] += up[x | h];
        double Hs = 0, Bs = 0;
        for (int s = 0; s < 32; s++) if (m[s]) { Hs += m[s] * (10.0 - L[m[s]]); Bs += m[s] * (L[up[s]] - L[m[s]]); }
        double H = Hs / 1024.0, B = Bs / 1024.0, I = Iint / 1024.0, var = 1.0 - m[0] / 1024.0;
        cnt++;
        int a = abs(c[0]) / 2;
        if (B > maxB[a][Iint]) { maxB[a][Iint] = (float)B; argB[a][Iint] = tt; }
        if (H > maxH[a][Iint]) maxH[a][Iint] = (float)H;
        upd(&bBI, B / I, tt, H, B, I, var);
        upd(&bHI, H / I, tt, H, B, I, var);
        upd(&bBIv, B / (2 * I - var), tt, H, B, I, var);
        upd(&bHIv, H / (2 * I - var), tt, H, B, I, var);
        double t1 = H - (2 * B + 2 * I - 2 * var);
        if (t1 > worst_t1) worst_t1 = t1;
        upd(&bT1, H / (2 * B + 2 * I - 2 * var), tt, H, B, I, var);
        if (c[0] == 0 && Iint > 1024) {
            upd(&bBbal, B / (I - 1), tt, H, B, I, var);
            upd(&bHbal, H / (I - 1), tt, H, B, I, var);
        }
    }
    char fn[512];
    snprintf(fn, sizeof fn, "%s.summary.txt", argv[3]);
    FILE *o = fopen(fn, "w");
    fprintf(o, "range %llu %llu count %llu worst_H_minus_bound %.3e\n", (unsigned long long)lo, (unsigned long long)hi, (unsigned long long)cnt, worst_t1);
#define P(name, b) fprintf(o, "%s %.10f tt %08x H %.8f B %.8f I %.8f var %.8f\n", name, (b).v, (b).tt, (b).H, (b).B, (b).I, (b).var)
    P("max_B_over_I", bBI); P("max_H_over_I", bHI); P("max_B_over_2I_minus_var", bBIv); P("max_H_over_2I_minus_var", bHIv);
    P("max_H_over_thm1_bound", bT1); P("balanced_max_B_over_I_minus_1", bBbal); P("balanced_max_H_over_I_minus_1", bHbal);
    fclose(o);
    snprintf(fn, sizeof fn, "%s.frontier.csv", argv[3]);
    o = fopen(fn, "w");
    fprintf(o, "abs_c0,Iint,maxB,maxH,argB\n");
    for (int a = 0; a < 17; a++) for (int i = 0; i <= 5120; i++) if (maxB[a][i] >= 0)
        fprintf(o, "%d,%d,%.7f,%.7f,%08x\n", 2 * a, i, maxB[a][i], maxH[a][i], argB[a][i]);
    fclose(o);
    return 0;
}
