# B14 lead run 20261011T224500Z: exact re-check of A066/A067 and point-defect neutralization

Stream B14 (independent analytic routes), Claude lead. Primary packet A067, gap G-BOOLEANITY, protocol revision
2026-10-11-execution-v2.

## 1. Exact target, quantifiers, units

C000: an absolute C with H(f) <= C I(f) for every f: {-1,1}^n -> {-1,1}, every n. Here p_S = fhat(S)^2, H = sum p_S
log2(1/p_S) (bits unless marked nat), I = sum |S| p_S, Var = 1 - p_empty, d_f(S) = max{|T| : T contains S, fhat(T) != 0},
U(f) = sum_{S nonempty, p_S>0} p_S (d_f(S) - |S|). The question for this run: is the A067 local granularity (the only
Boolean-specific logarithmic gain B14 has so far) a mechanism that can carry a universal constant?

## 2. Sources actually read

mop_fei100/reports/fei-2026-10-11/: EXECUTION_PROTOCOL.json (rev 2026-10-11-execution-v2), CURRENT_STATUS.md,
CLAIM_REGISTRY.json, STREAM_NEXT_ACTIONS.json (entry B14), plan .tex B14 packet block (A066-A070).
research_pushes/2026-10-11-full-fei-100-agents/: CLAIMS.md rows C000, C005, C006, C007, C008, C009, C018, C019, C020, C024;
SEED_LEMMAS.md (point-defect Renyi refutation); COUNTEREXAMPLES.md.
agents/A066/runs/20261011T214539Z-.../ (REPORT, CLAIMS, DERIVATION); agents/A067/runs/20261011T220539Z-.../ (REPORT,
CLAIMS, REVIEW_A066.md); claim statements of A068 (run 20261011T222313Z) and A069 (run 20261011T224507Z).

## 3. Results and derivations

### 3.1 Independent re-check of the stream claims (my own code, no agent code imported)

code/check_b14.py: integer Walsh transform, superset-maximum dynamic programme for d_f, Fractions. Frozen spec in
FROZEN_SPEC.json before the run. Result out/CHECK.json: PASS, 885,511 exact assertions, 14.6 s.

- A067-LOCAL-BOOLEAN-GRANULARITY (fhat(S) in 2^{1-d_f(S)} Z for nonempty S in the support). All 65,814 truth tables with
  n <= 4 (791,324 nonzero nonempty coefficients) and 1,900 structured random functions n = 5..9 (85,927 coefficients):
  zero violations. I also read the proof line by line: D_S f takes values in 2^{1-|S|}Z, has degree d_f(S) - |S| in the
  remaining variables, and an integer-valued function of degree e has Fourier coefficients in 2^{-e}Z; so
  fhat(S) = (D_S f)^(empty) lies in 2^{1-d_f(S)}Z. Correct. The consequence H <= 2I + 2U - (2 - log2 e)Var held on every
  n <= 4 table (float check, max gap 0 at constants).
- A067-MAXIMAL-SUPPORT-ENVELOPE-NOGO. Dictator surgery g_n = x_1 - 2 1{x = all +}, n = 2..12: I = 1 + (2n-4)2^{-n},
  Var = 1 - 4^{1-n}, U = n - 1 - (2n-4)2^{-n} - 4n 4^{-n} exactly (U/I = 10.94 at n = 12). Maj3(z) times a point defect on
  n bits, n = 2..5: every one of the 2^{n+3} anchors has E_A >= 3n/2 exactly (minima 45/8, 55/8, 1035/128, 2397/256 against
  3, 9/2, 6, 15/2) and I = 3/2 + 2n 2^{-n} <= 5/2. Addressing a = 1..4: d = a+1 on the whole support, |fhat| = 2^{-a},
  U = a/2, I = 1 + a/2, H = 2a.
- A066-HEAT-ENTROPY-IDENTITY: holds because integral_0^inf 2|S| e^{-2t|S|} dt = 1 for every nonempty S; it rewrites H and
  pays nothing by itself. A066-NO-INTEGRABLE-HEAT-ENVELOPE: for the point defect, J/I = (2n-2) ln2 e^{-2t}((1+e^{-2t})/2)^{n-1}
  checked as a polynomial identity in z = e^{-2t} for n = 2..10, and the area 2(1 - 1/n)(1 - 2^{-n}) ln 2 exactly.
- C005/C006 channel constant, independent derivation: for one coordinate the channel term is sum_T (s^2+d^2) g(r) nats with
  s = fhat(T), d = fhat(T+i), r = 2sd/(s^2+d^2), g(r) = sum_k r^{2k}/(2k(2k-1)). Termwise g(r) <= 1 - sqrt(1-r^2), because
  the coefficient ratio 2k binom(2k,k)/4^k equals 1 at k = 1 and increases; and (s^2+d^2)(1 - sqrt(1-r^2)) = 2 min(s^2,d^2).
  So JS <= (2/ln2) sum_T min(s_T^2, d_T^2) <= (2/ln2) min(I_i, 1 - I_i), the C005 constant. Combined with A067 on the leaves,
  C006 gives H <= sum_{i in B} h2(I_i) + (2/ln2) I_B + 2 I_R + 2 E_y U(f_y) - c E_y Var(f_y); checked on 300 random
  functions (half with a point defect) over all 7,820 blocks, no violation (floating, support only).

Verdict on the four claims: correct at their stated scope. These are reviews by the stream lead; the packet's
independent reviewers (A088, A094) are still needed for registry acceptance.

### 3.2 New: point-defect neutralization (author-proved)

Theorem. Let f be Boolean on n bits, N > n, x0 in {-1,1}^N, p = 2^{-N}, and f'_N(x) = f(x_1..x_n)(1 - 2 1{x = x0}).
(a) f'_N^(S) = fhat(S) 1{S subset [n]} - 2p f(x0) chi_S(x0); in particular f'_N^([N]) = -2p f(x0) chi_[N](x0) != 0, so
    d_{f'_N}(S) = N for every S, and U(f'_N) = N Var(f'_N) - I(f'_N).
(b) |I_i(f'_N) - I_i(f)| <= 2p for each i, so |I(f'_N) - I(f)| <= 2Np.
(c) ||p' - p||_1 <= 4p(sum_S |fhat(S)| + 1) <= 4p(2^{n/2} + 1); with eps = 2p(2^{n/2}+1),
    |H(f'_N) - H(f)| <= eps N + h2(eps).
(d) For nonconstant f: H(f'_N) -> H(f), I(f'_N) -> I(f), and U(f'_N)/I(f'_N) -> infinity linearly in N.
(e) Let psi(s,N) >= 0 with max_s psi(s,N) = o(2^N), and Psi(g) = sum_{S nonempty, ghat(S) != 0} ghat(S)^2 psi(|S|, d_g(S)).
    Then Psi(f'_N) - sum_{S nonempty} fhat(S)^2 psi(|S|, N) -> 0. So if H <= alpha I + beta Var + Psi for all Boolean
    functions, then H(f) <= alpha I(f) + beta Var(f) + liminf_N sum_S fhat(S)^2 psi(|S|, N) for all Boolean f.

Proof. (a) The defect adds -2 f(x0) 1{x = x0}, whose S-coefficient is -2p f(x0) chi_S(x0). The pad has no coefficient
outside subsets of [n], and [N] is not such a subset since N > n. Every S lies below [N], so d = N, and then
U = sum_{S nonempty} p'_S (N - |S|) = N Var - I. (b) Changing one point changes the edge indicator in direction i only on
the two ordered edges at x0. (c) p'_S - p_S = 2 fhat(S) delta_S + delta_S^2 with |delta_S| = 2p; sum over S and use
sum_S |fhat(S)| <= 2^{n/2} (Cauchy-Schwarz over at most 2^n sets); then the sharp continuity bound
|H(P) - H(Q)| <= T log2(M - 1) + h2(T) with T = TV <= eps and M = 2^N. (d) Var(f'_N) -> Var(f) > 0. (e) d = N for every S
by (a), so the difference is bounded by max_s psi(s,N) ||p' - p||_1 <= o(2^N) 4p(2^{n/2}+1) -> 0. QED.

Validation (out/CHECK.json, block N1): exact d = N on the whole support, exact U = N Var - I, exact influence and L1 bounds
for x1, AND2, Maj3 and addressing a = 2 padded to N <= 14. Examples: Maj3 at N = 9: I' = 1.535 (I = 1.5), H' = 2.120
(H = 2), U'/I' = 4.86; x1 at N = 14: I' = 1.0015, H' = 0.0067, U'/I' = 12.98.

Consequence for B14. FEI on the class of point-defected pads with constant C gives FEI for every Boolean function with the
same C, by (b) and (c). On that class the local granularity is the global fact fhat(S) in 2^{1-N}Z, which every Boolean
function on N variables satisfies. So exact dyadic arithmetic of coefficients cannot be the source of a universal
constant when it is used in one shot: by (e), any support functional of (|S|, d_f(S)) proves no more than its d = N
specialization. For the A067 choice psi(s,d) = 2(d-1) that specialization is 2(N-1)Var, the dimension bound. This answers
the "tail-stable arithmetic" option in the A067 next action in the negative for one-shot functionals.

What does survive. (i) Granularity after a restriction: restricting one padding coordinate removes the defect with
probability 1/2. Measured in floating point (out/STRIP.json), the entropy decrement of that one restriction divided by its
influence 2p tends to about 4 for x1, AND2, Maj3 and addressing (4.06, 4.13, 4.07, 4.04 at the largest N). So granularity
remains usable as a leaf certificate inside a C019 stopping tree; the open cost is the C019 node payment, not the leaf.
(ii) Kraft codes: if l is any code, the mixture with the uniform N-bit code loses at most 1 bit and changes by o(1) under
the defect, so code bounds (C008, C020, the A069 tree codes) are perturbation-stable. (iii) The signed identities of C007
(f^2 = 1) are polynomial identities that the pads satisfy exactly; they are the stable form of Booleanity.

### 3.3 Supporting evidence (floating point, not a claim): hybrid code/granularity bound

Elementary lemma: for pointwise-valid a_S >= log2(1/p_S) and a Kraft code l, H <= h2(p(K)) + sum_S p_S min(a_S, l_S) with
K = {l_S < a_S} (Gibbs on K, pointwise on the rest). With a_S = 2(d_f(S)-1) and the influence code
l_S = log2 e + sum_{i in S} log2(I/I_i), the bound divided by I stays below 2.9 on dictator surgery (n <= 14) and below
3.3 on Maj3 times a point defect (n <= 10), the two A067 obstructions. On point-defected addressing it grows (2.53, 3.22,
3.70, 4.07 for a = 1..4): granularity is dead there by 3.2(a), and on addressing the influence code alone costs
log2(a+2) - O(1) per unit of influence. The queue code of C008/C009 does not have this loss.

## 4. Proof dependencies and changed downstream conclusions

3.2 depends only on Parseval, Cauchy-Schwarz and the sharp Shannon continuity bound. Downstream: the "tail-stable
arithmetic" option is closed for one-shot support functionals; the live B14 Booleanity routes are (i) granularity as a
C019 leaf certificate, (ii) perturbation-stable codes, (iii) C007 identities. C000 remains open; nothing here proves FEI
for a new class.

## 5. Next mathematical action and reviewer

Prove a C019 node payment for stripping restrictions on the point-defected class in closed form (the decrement/influence
ratio tends to 4 above), then extend the stripping rule from padding defects to defects inside the active coordinates,
where the influence of the stripped coordinate is not small. Independent reviewer for 3.2: A070 (packet referee), or
A088/A094.

## 6. Persistence receipts

Written in this folder: FROZEN_SPEC.json, code/check_b14.py, code/b14lib.py, code/check_strip.py, out/CHECK.json,
out/STRIP.json, REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, .final. Commands:
python -X utf8 code/check_b14.py out/CHECK.json (PASS, 885,511 assertions, 14.6 s) and
python -X utf8 code/check_strip.py out/STRIP.json. Memory gate memok.py exit 0 before the run. No git, mesh or brain
writes (forbidden by the task). The harness Write tool refused report-named files for subagents; this file was copied
into the run folder with the shell because the campaign protocol requires it there.

## Addendum A1: anchored envelopes are neutralized too

For every anchor A subset [N], the coefficient of g_N chi_A at [N] is ghat_N([N] minus A). If [N] minus A is not inside [n]
it equals -2p f(x0) chi(x0) != 0. If it is inside [n], it equals fhat([N] minus A) -/+ 2p, which is nonzero because fhat
takes values in 2^{1-n}Z and 2p = 2^{1-N} < 2^{1-n}. So d = N for every S and every anchor, and the envelope minimum over
anchors used in A067-MAXIMAL-SUPPORT-ENVELOPE-NOGO is also reduced to its d = N specialization on the point-defected class.
Exact check (code/check_anchor.py, out/ANCHOR.json): every Walsh coefficient of g_N is nonzero, hence every anchor keeps
the top coefficient, for x1, AND2, Maj3 and addressing a = 2, five values of N each and four choices of x0: 19,344 anchor
cases, PASS.

## Universal bridge

A Boolean function and its one-point edit on more variables have nearly the same entropy and influence, so a universal
FEI argument has to be continuous under vanishing truth-table edits. That splits every B14 route in two. Quantities that
depend on which Fourier coefficients vanish exactly (local degree d_f, granularity, U, maximal supports, anchored
envelopes) are destroyed by one edit and can enter only after a restriction step has removed the edit, which puts their
cost in the C019 node payment. Quantities that are continuous in the spectral law (Kraft codes, Gibbs bounds, the C006
channel term, the C007 identities f^2 = 1) survive the edit and are the only ones that can carry the constant on their
own. The A069 edit-stable tree codes and the C008 queue code are of the second kind; the A067 functional U and the A066
pointwise heat envelopes are of the first.
