# B08 lead run 20261011T225000Z: TC restriction ledger, posterior-credit cap, edge-ratio form

Full FEI is OPEN. This run proves two exact statements (one is an equivalent reformulation of FEI, not progress on it), refutes a local price for the product-reference transfer on AND_n, and re-checks the A036 and A037 inputs exactly.

## 1. Exact target, quantifiers, hypotheses and units

Every n >= 1 and every f: {0,1}^n -> {-1,1} under the uniform measure. P(S) = fhat(S)^2. Logs are base 2 unless ln is written; 0 log 0 = 0. Inf_i = P(i in S), I = sum_i Inf_i, H = H(P), S_i = 1[i in S], S_-i = S \ {i}.

- M(f) = sum_i h2(Inf_i) (marginal sum). TC(f) = D(P || prod_i Ber(Inf_i)) = M - H (exact: the log of a product law is affine in the indicators).
- Campaign B(f) = sum_i B_i, B_i = H(S_i | S_-i) (C018). Note M is not B.
- Restriction g_s = f|_{x_i=s}, ghat_s(T) = fhat(T) + (-1)^s fhat(T u {i}). JS_i = JS(P_{g_0}, P_{g_1}). Gamma_i = sum_{j != i} JS(Ber(Inf_j(g_0)), Ber(Inf_j(g_1))). Posterior credit at the node: I_i = I_P(S_i ; S_-i).

Targets. (T1) exact one-step TC ledger and its tree sum. (T2) a cap on posterior credit collected along any adaptive restriction tree, with the debt written explicitly. (T3) an exact one-sided form of B and its FEI equivalence. (T4) test of the local prices Gamma_i <= c Inf_i and Gamma_i <= c (Inf_i + JS_i). (T5) independent re-check of the A036 and A037 v1 claims.

## 2. Sources actually read, revisions and theorem locators

- ~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json, schema fei-execution-protocol/2, revision 2026-10-11-execution-v2 (required files, report, progress and claim fields; unreviewed-claim cap 2 per stream).
- Campaign registries read earlier in this session: PACKET_STATUS.json (B08 packets A036-A040, reviewers A088, A094), STREAM_NEXT_ACTIONS (B08 action), CLAIMS.md (C005, C006, C018, C019, C023, C024), obstructions O-B05, O-RAW-CONV, O-RENYI, O-FINITE-BOOL, SEED_LEMMAS, plan line 1319.
- agents/A036/runs/20261011T214139Z-account05-A036-reference-law-divergence: REPORT.md, CLAIMS.json (A036-POINT-DEFECT-TENSOR-NORMALIZED-PAYMENT-RECOVERY v1, sha ca9f2080...), code/check.py, out/verification.json.
- agents/A037/runs/20261011T220010Z-account05-A037-conditional-credit-ledger: REPORT.md, CLAIMS.json (A037-CONDITIONAL-CREDIT-CONSERVATION v1 sha d23c07e7..., A037-PHYSICAL-SPECTRAL-COMMON-LIFT v1 sha aa45c0da...), code/ledger_check.py.
- agents/A038/runs/20261011T221733Z-account05-A038-occupancy-term-audit: REPORT.md sections 1-2, CLAIMS.json (A038-OCCUPANCY-CROSSLAW-AUDIT).
- agents/A039/runs/20261011T223903Z-account05-A039-projection-under-restrictions: REPORT.md (claims file not yet present at 23:13Z).
- agents/A040/runs/20261011T225840Z-account05-A040-credit-insufficiency-tests: empty at 23:09Z.

## 3. Complete derivation

### 3.1 One-step ledger (T1)

(a) Mixture. (P_{g_0}(T) + P_{g_1}(T))/2 = fhat(T)^2 + fhat(T u i)^2 = P(S_-i = T). Hence H(S_-i) = avg_s H(P_{g_s}) + JS_i, and Inf_j(f) = avg_s Inf_j(g_s) for j != i.

(b) C005. H(f) = H(S_-i) + H(S_i | S_-i) = B_i + JS_i + avg_s H(g_s).

(c) Marginal sum. M(f) = h2(Inf_i) + sum_{j != i} h2(avg_s Inf_j(g_s)) = h2(Inf_i) + avg_s M(g_s) + Gamma_i, by the mixture identity for each Bernoulli marginal.

(d) TC = M - H and h2(Inf_i) - B_i = H(S_i) - H(S_i | S_-i) = I(S_i ; S_-i). Subtract (b) from (c):

    TC(f) = I(S_i;S_-i) - JS_i + Gamma_i + avg_s TC(g_s).                    (L1)

(e) Tree sum. Take any adaptive restriction tree: internal node h at depth t has weight p_h = 2^-t and restricts coordinate i_h of its node function g_h; leaves l have weights p_l. Iterating (L1):

    sum_h p_h I_h + sum_h p_h Gamma_h + sum_l p_l TC(g_l) = TC(f) + sum_h p_h JS_h.   (L2)

### 3.2 Posterior credit cannot be reused (T2)

Gamma_h >= 0 and TC >= 0. C005 gives JS_h <= (2/ln 2) min(Inf_{i_h}(g_h), 1 - Inf_{i_h}(g_h)). Influence is conserved by (a): sum_h p_h Inf_{i_h}(g_h) + sum_l p_l I(g_l) = I(f). Therefore

    sum_h p_h I_h <= TC(f) + (2/ln 2)(I(f) - E I(g_l)) <= TC(f) + (2/ln 2) I(f).      (NR)

Explicit debt. B_h = h2(Inf_h) - I_h, so the erasure the tree pays is sum_h p_h B_h = D_tree - sum_h p_h I_h, with debt D_tree = sum_h p_h h2(Inf_{i_h}(g_h)) and credit capped by (NR). Credit spent at node h leaves the children's TC budget, in expectation by exactly I_h + Gamma_h - JS_h; nothing is counted twice.

What (L2) does not do. It is an exact rearrangement of C005 and the Bernoulli mixture identity, equivalent to the stopping-tree identity H(f) = sum_h p_h (B_h + JS_h) + E H(g_l). It proves nothing about FEI. First unsupported line on this route: "there is a tree with D_tree - sum_h p_h I_h + E H(g_l) <= C I(f)".

### 3.3 Edge-ratio form (T3)

Define M_edge(f) = sum_S P(S) sum_{i in S} log2(1 + P(S \ i)/P(S)), omitting P(S) = 0.

For fixed i and T not containing i, put p = P(T u i), q = P(T). Then (p+q) h2(p/(p+q)) = p log2((p+q)/p) + q log2((p+q)/q). Summing over T and i, B = M_edge + R with R = sum_i sum_T q log2(1 + p/q), and 0 <= R <= log2(e) sum_i sum_T p = log2(e) I. So

    M_edge(f) <= B(f) <= M_edge(f) + log2(e) I(f).

If FEI holds with C, then M_edge <= B <= H <= C I (H - B is the dual total correlation, nonnegative). If M_edge(g) <= K I(g) for every Boolean g, then B(g) <= (K + log2 e) I(g) for every g, and C018 gives FEI with C <= K + log2 e + 2/ln 2. So FEI holds iff there is an absolute K with M_edge <= K I on all Boolean functions. This is a reformulation; its use is that the mismatch logarithm named in G-R-MISMATCH has an exact one-sided form whose remainder R is at most log2(e) I.

### 3.4 No local price for Gamma (T4)

AND_n is the point defect f = 1 - 2*1_{x = x*}: P(empty) = (1-d)^2, P(S) = d^2 for S nonempty, d = 2^(1-n), Inf_j = d. Restricting any coordinate leaves one constant child and one copy of AND_{n-1}, whose influences are 2d. So Gamma_i = (n-1) phi(d) with phi(d) = h2(d) - h2(2d)/2 = d + psi(d)/ln 2, psi(d) = (1/2)(1-2d) ln(1-2d) - (1-d) ln(1-d). psi(0) = 0 and psi'(d) = ln((1-d)/(1-2d)) >= 0, so phi(d) >= d and Gamma_i >= (n-1) Inf_i. With JS_i <= (2/ln 2) Inf_i, Gamma_i/(Inf_i + JS_i) >= (n-1)/(1 + 2/ln 2), unbounded, at every coordinate. Neither Gamma_i <= c Inf_i nor Gamma_i <= c (Inf_i + JS_i) holds, even at the best coordinate. AND_n itself satisfies FEI (H/I -> 4), so Gamma must stay in the ledger as a transfer, not be priced locally. A039 proved the same refutation independently.

### 3.5 Reviews of stream inputs (T5)

- A036 v1. The collision profile re-derived: the autocorrelation of b = sign(fhat) sqrt(Q) at shift U, |U| = k, is (d(1-d))^(k/2) R_U with R_U = 2^k - 4(1-d)^(m-k) (only the shifts that exchange empty with nonempty flip sign). Hence v_U = 4^k (d(1-d))^k [1 - 2^(2-k)(1-d)^(m-k)]^2, matching A036. Exact for m = 2..7 by Fractions; Z(3) = 319/256. K, M, T and I are additive over disjoint tensors (v and Z multiply, so L/Z adds), so per-factor validity of A036's three linear inequalities gives the tensor statements; per factor they hold for m = 2..40 at 80 digits with margins at least 7.47 I and 3.00 I (evidence; the all-m analytic part was not re-proved here). Defect: A036's "B" is sum_i h2(d_i) = M, not C018's B; it must be renamed before anyone invokes C018 with it. The class already has H <= 4I directly, so this is calibration. Verdict: accept at scope after the rename.
- A037 v1, both claims. The lift identity reduces to C005 telescoping: Y_h is independent of S_0 given (path, S_h \ i_h), so I(S_0 ; L) = sum_h p_h I(T_h ; Y_h) = sum_h p_h JS_h and H(S_0 | L) = sum_h p_h B_h + E H(g_l). Exact check on all 256 three-bit functions and all 12 depth-2 coordinate trees: 0 failures, every branch fair. Verdict: accept as bookkeeping; it pays nothing new.
- A038 v1. K_full = v K_occ + Delta is a Pythagorean split with affine log-ratio, correct in form. Cross-check from Part C: T/(4I) - (m - 7) >= 2.55 for m = 8..40, tending to 4, consistent with A038's T/(4I) > m - 7. Not independently re-proved.
- A039. Its compensated TC identity is (L1); the exact census below agrees.

## 4. Executed validation

Command: `cd runs/20261011T225000Z-claude-B08-tc-restriction-ledger && python -X utf8 code/b08_checks.py out` (15.2 s, peak working set 230 MB, no GPU). code/b08_checks.py sha256 9dd4a65dff96701ff8d6f3660c3a3fa9582d8f5426fc968d458d410665fc9b3d; out/checks.json sha256 81e7a99b3804301349d1cf46bb66e413a564a01c973deb4f7b6361080927adda.

- Part A, all 65,536 Boolean functions on 4 bits, every coordinate: (L1) failures 0, C005 failures 0. Each logarithm is an integer vector over log2 p, p prime <= 61 (all masses are k/64); logs of distinct primes are linearly independent over Q, so vector equality is equality of reals. Gamma >= 0; Gamma_i <= sum_{j != i} |Inf_j(g_0) - Inf_j(g_1)| with equality cases (float, 30-ulp margin).
- Part B, exhaustive n = 4 (maxima at 20 digits from the exact vectors at the float argmax; float bound with margin over all f): max H/I = 3.4024755512 (point defect, I = 1/2); max B/I = 2.7041532056; max M_edge/I = 1.5913770175; max TC/I = 1.0281953111; max M/I = 4.3485155456; max over f of min_i B_i/Inf_i = 2.6724889840 (AND_3). M_edge <= B: 0 violations; B <= M_edge + I log2 e: 0 violations; max (B - M_edge)/I = 1.1128 < log2 e.
- Part C: A036 profile exact for m = 2..7; Z(3) = 319/256; inequalities for m = 2..40 (evidence); 2*1087^6 < 3*1024^6 true.
- Part D: A037 lift, 3,072 cases, 0 identity failures, 0 unfair branches.
- Part E: AND_n, n = 3..40: Gamma_1/((n-1) Inf_1) in [1, 1.246] and tending to 1; Gamma_1/(Inf_1 + JS_1) = 13.0 at n = 40; (L1) residual 0 at 50 digits.
- The first run had a scaling bug in one diagnostic (64 B compared with an unscaled I log2 e, 64,832 false violations). Fixed and re-run; the first stdout is kept as out/run_stdout_first_run_scaling_bug.txt.

Floating values are evidence. The identities are exact on the census; (T2)-(T4) rest on the proofs in section 3.

## 5. Proof dependencies and changed downstream conclusions

- (L1), (L2): Walsh orthogonality, the entropy chain rule, H(mixture) = average H + JS. (NR): C005's JS bound. (T3): C018 for the reverse direction and B <= H.
- Downstream: every posterior-credit route (C023, C024, G-J-COST, G-R-MISMATCH) has total credit capped by TC(f) + (2/ln 2) I(f) and must carry Gamma_h explicitly. Pricing Gamma by the removed influence or by JS is refuted on AND_n. A036's B must be renamed M before any C018 use.

## 6. One next mathematical action and independent reviewer

Next: on the B05 sparse bent-defect family (k = 2, 3), compute the ledger terms I_h, Gamma_h, JS_h and E TC(leaves) for the control-first and selector-first trees as exact log-vectors, and decide whether D_tree - sum_h p_h I_h + E H(g_l) = O(I) on either tree. Reviewer: A088 (primary), A094.

## 7. Persistence receipts

Written in this run directory: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, code/b08_checks.py, out/checks.json, out/run_stdout.txt, out/run_stdout_first_run_scaling_bug.txt, out/ARTIFACT_SHA256.json, .final. Stream files: ../../STREAM_NOTES.md, ../../LEARNED.md. No git, mesh, brain or checklist writes: the task forbids them; repository persistence is the coordinator's step.

## Universal bridge

Posterior credit in an entropy-erasure ledger is a mutual information measured against a fixed product reference. When the cube is split by a restriction, each child re-optimizes its own product reference, and that re-optimization, Gamma, is an exact nonnegative transfer that the removed influence cannot pay for (AND_n makes it n times larger). Any FEI route that collects credit along a tree therefore works inside a fixed budget, TC(f) + O(I) in total, and has to show that its debt, the sum of h2(Inf) over the queried coordinates, minus that credit stays O(I). The edge-ratio form states the same target in one line with no tree: the expected logarithm of P(S \ i)/P(S) over the down-edges of the spectral sample must be O(1) per unit of influence.
