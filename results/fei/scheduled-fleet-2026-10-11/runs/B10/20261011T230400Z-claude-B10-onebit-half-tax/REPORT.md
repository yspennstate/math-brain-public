# B10 lead run: the one-bit tax of B09 is at most half, uniformly

## exact target, quantifiers, hypotheses and units

Frozen potential (A046 intake): B09-BIASED-BLOCK-UNCERTAINTY v1, J_A <= M_A + Delta_A with
Delta_A = sum_{i in A}[h2(p_i) + log2 max(p_i,1-p_i)]. One bit: Delta(p) = p log2((1-p)/p) for p <= 1/2.
Here M_A = H(S_A|S_{A^c}) and J_A = H(S_{A^c}) - E_Z H(child spectrum), Z the physical assignment of A, for a
function f on a finite product-biased cube in the normalized product Fourier basis. Bits throughout.

Target (A047's first unsupported line): a finite-p, dimension-free improvement of the tax.
Theorem 1 (one bit). For every p in (0,1), every finite product-biased cube, every coordinate i with bias p
and every f whose two restrictions f_0, f_1 have unit L2 norm (in particular every Boolean f):
J_i - M_i <= tau*(p) := h2(p) - min_t F(t) <= Delta(p)/2,  F(t) = h2(sin^2 t) + h2(sin^2(t-b)), sin^2 b = min(p,1-p).
Equality in the second inequality only at p = 1/2. The constant 1/2 is sharp as p -> 0 (A046, A047).
Claim 2 (CONDITIONAL, product-biased blocks of any size): J_A - M_A <= sum_{i in A} tau*(p_i) <= Delta_A/2,
conditional on additivity of the optimal Shannon uncertainty bound for local measurement pairs
(R. Schwonnek, Quantum 2, 59 (2018)), which I recall but did not re-read or re-prove in this run.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json (2026-10-11-execution-v2); CLAIMS.md C000-C035, COUNTEREXAMPLES X001-X013,
SEED_LEMMAS, obstruction registry; B09 REPORT (adb671ff) sections on the uncertainty step; B09 interval repair
(a1ff9357); A046 run 20261011T214251Z REPORT/CLAIMS; A047 run 20261011T220210Z REPORT/CLAIMS; A048 run
20261011T221822Z REPORT sections 1-4 (partial). Context papers in context/ were not used.

## complete derivation or exact first unsupported line

Reduction (exact). Children G, H (coefficients G_T, H_T, unit norm), selector law P(X=1)=p. Parent masses on
(selector label, T): a_T = ((1-p)G_T + pH_T)^2, b_T = p(1-p)(H_T-G_T)^2, q_T = a_T + b_T. Put
(sqrt(1-p)G_T, sqrt(p)H_T) = r_T(cos t_T, sin t_T), cos b = sqrt(1-p), sin b = sqrt(p). Then q_T = r_T^2,
sum q_T = 1, a_T = q_T cos^2(t_T-b), b_T = q_T sin^2(t_T-b), so M = sum q_T h2(sin^2(t_T-b)). The posterior of the
child given T is p H_T^2/q_T = sin^2 t_T, so J = I(child;T) = h2(p) - sum q_T h2(sin^2 t_T). Hence
J - M = h2(p) - sum_T q_T F(t_T) <= h2(p) - min_t F(t). (Checked numerically on 300 random Boolean pairs with biased
data bases, n<=3: max error 8.9e-16; out/checks.json.) min_t F is the optimal two-basis entropic uncertainty bound
of a qubit (real states suffice: h(u)+h(v) is concave on the filled ellipse of Bloch projections).

Inequality min_t F >= R(p) := h2(p) - Delta(p)/2 = (p/2)log2(1/p) + (1-p/2)log2(1/(1-p)), p <= 1/2. Symmetries
t -> t+pi/2 and t -> b-t give the fundamental domain t = b/2 + d, d in [0, pi/4]. R is increasing on (0,1/2]
(R' = l/2 + 1/(2(1-p)ln2), l = log2((1-p)/p)).
Lemma A (0 < p <= 0.08). a=|sin t|, c=|sin(t-b)|, a+c >= sin b = sqrt p. Case a,c <= e^{-3/2}: h2(x) >= x log2(1/x)
+ x(1-x)/ln2; k(s)=s^2 log2(1/s^2) is convex and increasing on [0,e^{-3/2}], so k(a)+k(c) >= 2k(sqrt(p)/2) =
(p/2)log2(4/p); with S=a^2+c^2 in [p/2, 2e^{-3}], S-S^2 >= p/2-p^2/4. So F >= (p/2)log2(1/p) + p + (p/2-p^2/4)/ln2,
and F - R >= 0.27865p - 0.42344p^2 > 0. Case max(a,c) > e^{-3/2}: on the domain sin^2 t <= (1+sqrt p)/2 <= 0.64143
and sin^2(t-b) <= 1/2, so F >= h2(e^{-3}) >= 0.28549 > 0.26124 >= R(0.08) >= R(p).
Lemma B (0.49 <= p <= 1/2, |t-b| <= 0.3). phi(t)=h2(sin^2 t) has phi'' = -4/ln2 + 2cos2t log2(cot^2 t) >= -4/ln2
(phi is C^1 at its cusps), so phi(b+e) >= h2(p) + 2sqrt(p(1-p)) l e - (2/ln2)e^2; and h2(sin^2 e) >= 0.97e^2
log2(1/(0.97e^2)) for |e| <= 0.3. So F - R >= (p/2)l + 2sqrt(p(1-p)) l e + A(|e|), A(d)/d^2 >= 0.52694 on [0,0.3];
for e<0 the linear loss is <= l max(0,|e|-0.245) <= 0.00318 < 0.0316 <= A(|e|) when |e| >= 0.245.
Box certificate (rest). Boxes in (b, d), b in [0.28, pi/4] (sin^2 0.28 < 0.08), d in [0, pi/4]: lower bound =
min of h2 over the enclosed range of sin^2 t (endpoint minimum by concavity) + same for sin^2(t-b) - R(p_max).
mpmath interval arithmetic, 80 bits. PASS: 4,100 boxes closed with positive bound (minimum 2.35e-4), 3 inside
lemma B, 7 splits, 3.3 s. All lemma constants are interval-checked in out/certificate.json.

Sharpness: tau*(p) = (p/2)log2(1/p) - 0.2787p + o(p) (symmetric minimiser), matching A046/A047's coefficient 1/2.
Float table (scratch explore): tau*/Delta = 0.4895 (p=1e-8), 0.394 (0.1), 0.258 (0.25), 0.044 (0.4), -> 0 at 1/2.
AND check (p=1/8, q=1/4): J-M = 0.119545 <= tau* = 0.132038 <= Delta/2 = 0.175460 (B09's certificate J-M>0.1195).

First unsupported line: Claim 2 needs the cited additivity theorem (not re-read). Two-bit float evidence:
multistart minimisation of H(w^2)+H((U1xU2 w)^2) never went below U(p1)+U(p2) (6 bias pairs, gap >= -4e-10).

## executed validation with domain, arithmetic, commands and outputs

`python -X utf8 code/certify_half_tax.py out/certificate.json` -> PASS (out/certificate_stdout.txt).
`python -X utf8 code/checks.py out/checks.json` -> identity error 8.9e-16; max (J-M)/(Delta/2) on random pairs 0.82.
`python -X utf8 code/break_check.py out/break_check.json` (independent, float, no symmetry reduction: t over the
full period, 427 values of p in (0,1) on both sides of 1/2 and at the seams 0.08, 0.0816, 0.49) -> 0 negative
margins; smallest positive margin 2.79e-7 at p = 1e-6 (= 0.279p, as the asymptotics predict); zero only at p = 1/2.
Spec frozen in FROZEN_SPEC.json before the run (one amendment logged: grid start 0.2897 -> 0.28 after a coverage gap
was found in the first PASS; the first PASS was discarded). Memory well under 300 MB; no heavy job.

## proof dependencies and changed downstream conclusions

Theorem 1 uses only the parent-mass formulas (B09/A047 ledger), Parseval, calculus and the interval certificate. It
does not use B09's unreviewed Maassen-Uffink step: for one bit it replaces it with a sharper bound. Downstream:
every one-bit use of Delta can use Delta/2 (or tau*); the A046 no-go is unchanged (a logarithmic tax is necessary);
A048's irrelevant-coordinate and unrevealed-factor obstructions apply equally to the half tax.

## one next mathematical action and independent reviewer

Prove or refute that sum over a C019 stopping tree of tau*(p_i) on essential revealed bits is <= K*I plus the C024
path-entropy slack. Reviewers: A092 (primary), A087; A046 to re-derive the reduction.

## actual persistence receipts or precise save blocker

Saved in this run directory: FROZEN_SPEC.json, code/certify_half_tax.py, code/checks.py, out/certificate.json,
out/certificate_stdout.txt, out/checks.json, REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json. No git,
brain or mesh writes (forbidden by the task).

## Universal bridge

The B09 tax entering C019 drops from Delta(p) to tau*(p) <= Delta(p)/2 per revealed bit, uniformly in dimension,
biases and children. The factor 1/2 is optimal at the rare endpoint, so the logarithmic part of the tax cannot be
removed. What remains: the multi-bit statement (one cited theorem), and paying (1/2) sum p_i log2(1/p_i) over a
stopping tree by influence, with A048's terminal-entropy obstruction still open. The tax is now sharp, so the
remaining gap sits in the stopping-tree ledger, not in the uncertainty step. Comparing the tree tax with the C024
path entropy is the shortest next step, because sum p log(1/p) over revealed rare bits is a branch-entropy term.
