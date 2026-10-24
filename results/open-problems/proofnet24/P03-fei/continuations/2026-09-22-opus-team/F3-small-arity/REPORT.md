# F3: the smallest fan-in that defeats the read-once potential, and read-once formulas over small gates

22-23 September 2026. Full FEI is OPEN / NOT PROVED.

Status.

CERTIFIED (exact rational arithmetic with rigorous logarithm enclosures; standalone checkers `code/witness_g7.py`, `code/witness_g7_h24.py`, `code/exact_gate.py`):
- A composition-prime monotone gate G7 on seven inputs violates the gate inequality of the read-once potential Gamma_RO (`inputs/cert_vi_h96k40.npz`). At p = (1/2, 1/2, 7/24, 1/2, 1/2, 2/7, 5/17), D = -6.7843957708e-3 and c = 0.0403647.
- That is about ten times the two-input AND margin of the same potential (4.055e-3, numerical).
- G7 also violates the inequality for the certified arity-2 potential h24k40 + 0.01 p(1-p), with D = -5.1036e-3. So the read-once induction behind H <= 6.4573 I cannot pass fan-in seven.

CERTIFIED (outward-rounded interval arithmetic, `code/xor_cert.py`, with negative controls):
- The XOR gate inequality Gamma(p) + Gamma(q) >= Gamma(p + q - 2pq) holds for both stored potentials.
- With the arity-2 certificate of 21 September, every read-once formula over gates of fan-in at most two (AND, OR, XOR, NOT) satisfies H <= 6.4573 I.

PROVED:
- The selector-expansion identity for D and W at any gate.
- A closed form of the MUX remainder.
- The list of the five composition-prime 3-input NPN classes.

NUMERICAL:
- No gate of fan-in at most six was found above the AND value; the searches have a positive control, and the coverage is detailed in section 4.
- Every prime 3-input class asks at most c = 1.04e-3 < 0.01.
- For each prime class some input's selector remainder is nonnegative on grids reaching 2^-24 of every face.
- On this evidence read-once formulas over gates of fan-in at most three satisfy H <= 6.4573 I.

Not achieved:
- An interval certificate for any prime 3-input gate. The remainders are near-tight at corners of the cube.
- A search of non-monotone gates of fan-in 5 and 6.

Notation follows `continuations/2026-09-22-gate-reformulation/REPORT.md`. A gate G has k inputs, and p_i = Pr[input i true]. Further:
- V_i = 4 p_i (1-p_i);
- D_G(p) = sum_i It_i (Gamma(p_i) + h(V_i))/V_i - Htilde_G(p) - Gamma(p_out);
- W_G(p) = sum_i It_i/4 - p_out(1-p_out);
- c_G = -D_G/W_G.

A negative D for a potential shows the potential is not admissible for that gate. It is not a lower bound on C_FEI.

## 1. The AND value of the stored potential

The figure 4.3974e-3 quoted for the AND belongs to a four-times-finer candidate `cert_vi_h96k40_f4` that was not saved. For `cert_vi_h96k40.npz` the multi-start margin search (`code/and_cmax.py`; node x dense, Hod ladder x dense, node x node and 6M random pairs) gives

    c_AND,max(h96k40) = 4.05500e-3   at p = 1/16, q = 0.666583        (NUMERICAL, logs/and_cmax_h96k40.out)

This is consistent with 4.054639e-3 at (2^-4, 2/3) in the gate-reformulation report. The local refinement stage of that script runs into underflow at p = 1e-300, and its output there is discarded. This value is the threshold below. The witness exceeds it tenfold, so its last digits are immaterial.

## 2. The seven-input witness (CERTIFIED)

G7 is the monotone gate on inputs 0..6 with minimal true sets

    {1,3}, {0,4}, {2,3,4}, {0,1,5}, {1,4,6}, {2,4,6}, {1,5,6}

It has 72 true points of 128. It is the restriction of Numaro's g with core coordinates 0..6 free, x7 = 0 and x8 = 1, auxiliaries 14, 15, 16 true and the other auxiliaries false. The checker confirms this against `inputs/numaro18_pm1_table.npy`. G7 is composition-prime: for every block A with 2 <= |A| <= 6 the cofactors over x_A take at least three distinct functions (`code/inspect_g7.py`; criterion of fleet account01/B16, Lemma 2.1).

Exact evaluation (`code/exact_gate.py`): biased Walsh weights are exact rationals, w_T = R_T^2 prod_{i in T} p_i(1-p_i), where R_T comes from the matrix [[1-p, p], [1, -1]], and Parseval is checked exactly. Logarithms use ln r = e ln 2 + 2 atanh((m-1)/(m+1)), with directed rounding to 2^-400 and an explicit tail bound. Gamma is taken exactly as stored: s times the piecewise-linear interpolant of the stored doubles in x = log2(1/s), with x enclosed rigorously.

| bias p | p_out | W | D | c |
|---|---|---|---|---|
| (1/2, 1/2, 7/24, 1/2, 1/2, 2/7, 5/17) | 11483/22848 | 87741665/522031104 | -6.784395770752406699e-3 (width 1.5e-87) | 0.0403646957711 |
| (1/2, 1/2, 9/32, 1/2, 1/2, 9/32, 5/16) | 2061/4096 | 2821417/16777216 | -6.324690636864725019e-3 | 0.0376090102767 |

At the first point the influences are It = (0.3163, 0.4108, 0.0668, 0.3178, 0.4127, 0.0660, 0.0819), so every input matters and the configuration is not a limit of a smaller gate.

For the certified potential h24k40 + 0.01 p(1-p), at the first point, D = -5.103621113310e-3 < 0 (`logs/witness_g7_h24.out`).

Numerically the maximum is c = 0.0406436 at p = (1/2, 1/2, 0.29045, 1/2, 1/2, 0.28793, 0.29187), p_out = 0.502441. The value is the same under h24k40, whose nodes on [1/32, 1/2] coincide with those of h96k40.

## 3. Mechanism: the dips of the read-once potential

Gamma_RO equals the AND-chain slack at dyadic measures and rises steeply around them:

    near 1/2:  one-sided slopes -30.48 / +30.48; Gamma(1/2) = 6.4548, Gamma(1/2 +- 0.0026) = 6.5014 (a local maximum),
               Gamma(1/2 +- 0.01) = 6.4897
    near 1/4:  slopes -12.79 / +38.57;   near 1/8:  slopes -2.09 / +35.0

A gate whose output measure sits on a shoulder of the dip at 1/2 pays about 0.047 more in Gamma(p_out) than a balanced gate at uniform bias. G7 sits on the shoulder (p_out = 0.50244).

Two kinds of search cannot see this. The balanced uniform slice, searched exhaustively by the fleet (account01/B17: no balanced restriction of Numaro's g below essential arity ten beats the cap), puts p_out exactly at the bottom of the dip. Random bias vectors almost never land on the shoulder: under a logit-normal bias distribution G7 exceeds the AND value on 1e-5 of the draws.

## 4. Evidence that seven is the smallest fan-in (NUMERICAL)

The dip-targeted screen (`code/cusp_screen.py` for monotone gates, `code/cusp_general.py` for any gate): for each input subset S, the common bias of the inputs in S is solved so that p_out lands on a shoulder of the dip at 1/4, 1/2 or 3/4, with targets the dip centre +- 0.0012, 0.0026, 0.004 and 0.007; the remaining inputs are held at 1/2 (and also at 1/4 and 3/4 in the general version); the best points are then bias-optimized by pattern search.

Positive control: on the 54 arity-7 restriction classes of Numaro's g, the screen flags G7 with screened c = 0.0405, optimized to 0.04062.

The table's values are all below the AND value 4.055e-3. "Degenerate" means the maximum is reached with some input's influence below 1e-9, i.e. a smaller gate in disguise.

| family | arity | method | largest c found |
|---|---|---|---|
| restrictions of Numaro's g, 374 spectral classes | 2..6 | pattern search, 5 starts per class | 1.05e-3 |
| same | 7 / 8 / 9 / 10 | same | 0.0402 (G7) / 0.0335 / 0.170 / 0.200 |
| all NPN classes depending on every input | 3 (10 classes) | dip screen + optimization | screened -3.6e-3; optimized 7.7e-4, degenerate |
| same | 4 (208 classes) | same | screened -5.2e-6; optimized 1.17e-3, degenerate; best genuine point 7.9e-6 at p_out = 0.50244 |
| all 7,581 monotone functions | 5 | 417 bias multisets + optimization | 1.17e-3, degenerate |
| the 6,894 monotone functions depending on every input | 5 | dip screen, rest of inputs at 1/4, 1/2, 3/4 | screened -3.5e-3; best genuine optimized 6.8e-5 |
| monotone, 15,951 invariant classes of the 16,351 permutation classes | 6 | dip screen + optimization of 150 | screened <= 0; optimized 1.05e-3, degenerate |

Controls that bound what a null means: a plain hill climb over all 7-input truth tables with the bias optimized jointly did not rediscover any gate above the AND value in 20 restarts, so no weight is placed on hill-climb nulls; random-bias screens find G7 in 3 of 20 trials, so a random-bias n = 6 run was stopped and replaced by the dip screen.

Scope: fan-in 3 and 4 are covered class by class; fan-in 5 is covered for all monotone gates; fan-in 6 for 97.5 per cent of the monotone permutation classes (the spectral invariant merges about 400 of them). Non-monotone gates of fan-in 5 or 6 are not excluded.

## 5. Gates of fan-in at most three

### 5.1 Prime classes (PROVED, by exhaustive cofactor count)

A 3-input gate is F(g(x_A), x_B) iff some pair block has at most two distinct cofactors. Exactly five of the 14 NPN classes are composition-prime (`code/prime3.py`); true points are written x0 x1 x2:

    one-hot  {100, 010, 001}         MAJ3  (as {000, 100, 010, 001})      EQ3  {110, 001} ~ {000, 111}
    MUX      {000, 100, 110, 001} = x0 ? not x2 : not x1                 Q3   {000, 110, 001}

The other nine classes are constant or degenerate; read-once over AND/OR (NOR3, and not x2 and not(x0 and x1)); or read-once with XOR (not x2 and (x0 xor x1), x2 xor (x0 or x1), XOR3).

By the composition identity, a read-once formula over gates of fan-in at most three is a read-once formula over AND, OR, XOR, NOT and these five. FEI for that class with a constant C therefore follows from D >= 0 for XOR and the five prime classes with the same potential, given the AND/OR certificate.

### 5.2 XOR (PROVED reduction, CERTIFIED inequality)

The biased spectrum of XOR is the product of the input spectra: It_i = V_i and Htilde = h(V_p) + h(V_q). Hence exactly

    D_XOR(p, q) = Gamma(p) + Gamma(q) - Gamma(p + q - 2pq).

Reductions: negating an input maps p to 1-p and p_out to 1-p_out, and Gamma is symmetric, so we may take p, q <= 1/2; D is symmetric, so we may take p <= q; the margin term c z(1-z) contributes c V_p V_q/4 >= 0, because z(1-z) = (1-m^2)/4 with m = 1 - 2z, and m multiplies under XOR.

`code/xor_cert.py` covers 0 < p <= q <= 1/2 in three pieces:
- (T) q <= 2^-41. There Gamma(u) = sigma u log2(1/u) + b* u with sigma = (G_J - b*)/K > 0. Since u log(1/u) is concave, vanishes at 0 and increases on (0, 1/e), D >= 2 b* p q >= 0.
- (L) For each of 1,280 q-cells of width 1/32 in log2(1/q): Gamma is absolutely continuous with Gamma' <= Lc on [q_lo, 2 q_hi], where Lc is the maximum over the pieces met of G - s_j/ln 2. Then D >= p [G(log2 1/p) - (1-2q) Lc] >= 0 for p <= p*, with p* taken from a suffix minimum of G.
- (C) Direct enclosures on 3,467 cells for p* <= p <= q.

Arithmetic is float64 with nextafter rounding and 8-ulp padding of log2, the same assumptions as the 09-21 certificate.

Results: both `cert_vi_h24k40` and `cert_vi_h96k40` give VERIFIED (`logs/xor_cert_h24.out`, `logs/xor_cert_h96.out`). Negative controls, two copies of h24k40 with a planted violation (a steep 60 per cent step; a smooth Gaussian bump; grid minima of D -3.31 and -2.89), both give NOT VERIFIED (`logs/xor_control.out`). Sampled self-check: the numerical Gamma' never exceeds Lc (worst gap -3.8e-6); the (L) bound never exceeds the true D; the bound stays >= 0.0179 p (`logs/xor_cert_selfcheck.out`).

A simpler proof is not available. The monotonicity of G in x would give the lemma in one line, but the stored G is not monotone (smallest node increment -0.0546, at the dip at 1/4; `logs/xor_lemma_check.out`).

Theorem (computer-assisted). Combined with the AND/OR certificate of 21 September (h24k40, c = 0.01), every read-once formula f over AND, OR, XOR and NOT satisfies

    H(f) <= 6.4573 I(f) - Gamma_hat(Pr f).

That is, the constant 6.4573 holds for read-once formulas over every gate of fan-in at most two.

### 5.3 The selector expansion (PROVED)

For a gate G, an input i of bias r, and cofactors G_0 (x_i false) and G_1 (x_i true):

    D_G = (1-r) D_{G_0} + r D_{G_1} + R_i,
    R_i = d (Gamma(r) + h(V_r)) + (1-r) Gamma(p_0) + r Gamma(p_1) - Gamma(p_out) - JS_r(mu_0, mu_1) - H(S_i | S_{-i}),
    W_G = (1-r) W_{G_0} + r W_{G_1} + r(1-r) [d - (p_1 - p_0)^2],   the last term >= 0 since |p_1 - p_0| <= d <= 1.

Here d = Pr[G_0 != G_1]; p_0, p_1 are the output measures of G_0, G_1, and mu_0, mu_1 their biased spectral laws; m = (1-r) mu_0 + r mu_1; and H(S_i | S_{-i}) = sum_T m(T) h(r(1-r)(G0hat(T) - G1hat(T))^2 / m(T)).

Proof. In the biased basis, G = (1-r) G_0 + r G_1 + (sigma_r/2) phi_r (G_0 - G_1). Hence Ghat(T)^2 + Ghat(T+i)^2 = m(T) for i not in T. So It_j(G) = (1-r) It_j(G_0) + r It_j(G_1) for j != i, It_i = V_r d, and the entropy splits as stated. The margin term c p(1-p) adds c times the W-remainder.

For MUX(s, a, b) = s ? a : b expanded on a (biases t, p, q for s, a, b): G_0 = AND(not s, b), G_1 = OR(s, b), d = t; p_0 = (1-t) q, p_1 = t + (1-t) q; the cofactor spectra agree on {b} and {s, b} and differ on the empty set and on {s}. This gives

    R_a = t (Gamma(p) + h(V_p)) + (1-p) Gamma((1-t)q) + p Gamma(t + (1-t)q) - Gamma(tp + (1-t)q)
          - [phi(m_0) - (1-p) phi(alpha_0) - p phi(alpha_1)] - m_0 h(4 p(1-p) t^2 / m_0)
          - V_t [phi(ybar) - (1-p) phi(q^2) - p phi((1-q)^2) + ybar h(p(1-p)/ybar)],

where alpha_j = (1 - 2p_j)^2, m_0 = (1-p) alpha_0 + p alpha_1, ybar = (1-p) q^2 + p (1-q)^2 and phi(w) = w log2(1/w).

Checks: the closed form agrees with D_MUX - (1-p) D_AND - p D_OR to 1.8e-14 on 20,000 random points (`logs/mux_closed_form.out`). For fixed interior (t, q), the p log(1/p) parts of the JS and conditional terms total ||G_0 - G_1||^2 p log2(1/p) = 4 t p log2(1/p); therefore R_a = 2(C0-4) t p log2(1/p) + O(tp) as p -> 0. Numerically R_a/(t p log2 1/p) = 4.00, 4.68, 4.39 at p = 2^-40 for three (t, q), against 2(C0-4) = 4.91 (`logs/mux_asymptotic.out`). So the a-faces of MUX carry no tightness in R_a; their tightness sits in the AND/OR terms, which the arity-2 certificate controls.

### 5.4 Numerics for the five prime classes (NUMERICAL)

With h24k40 + 0.01 p(1-p), on a 65^3 logit grid from 2^-24 to 1 - 2^-24 (`logs/mux_explore_h24_c001.out`): every selector remainder R_i is nonnegative for one-hot, MAJ3, EQ3 and MUX, for every input. For Q3 the remainder is nonnegative for inputs 0 and 1; input 2 gives R_2 down to -0.196, so Q3 must be expanded on input 0 or 1. The normalized minima min R_i/(d r(1-r)) lie between 5.8e-6 and 3.6e-5, at corners of the cube.

Without the margin, the largest c each class asks is (`logs/prime3_h24_c0.out`): EQ3 1.04e-3; one-hot 8.8e-4; MUX 8.8e-4; MAJ3 7.7e-4; Q3 7.7e-4. Each is attained at a dead-input face; interior grid maxima are between -0.2 and -2.2. On this evidence the fan-in-three constant equals the read-once one.

What a certificate still needs: R_i >= 0 for one input per prime class (MUX on a or b, Q3 on input 0). These inequalities are non-tight at the faces of the expansion input but near-tight at corners, where the asymptotics above must be carried to second order before interval subdivision can close.

## Files

`code/`: `fgate.py` (D, W and c for any gate at any bias, batched); `test_basic.py` (reproduces the AND certificate formula, the fleet's G10 value 0.018289126551415 and both published Numaro witnesses, D = -0.01761141995580 and -0.03802373437); `and_cmax.py`, `numaro.py`, `restr_enum.py`, `restr_opt.py`, `inspect_g7.py`; `exact_gate.py`, `witness_g7.py`, `witness_g7_h24.py` (the exact checkers); `mono_screen.py`, `mono_classes.py`, `mono_full.py`, `hill.py`, `cusp_screen.py`, `cusp_general.py` (the searches); `prime3.py`, `mux_explore.py`, `mux_closed_form.py` (fan-in three); `xor_lemma_check.py`, `xor_cert.py`, `xor_control.py` (XOR).

`logs/`: one output per script, plus the control potentials `control_steep.npz` and `control_smooth.npz`.
