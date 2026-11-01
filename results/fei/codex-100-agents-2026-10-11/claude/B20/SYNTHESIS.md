# B20 synthesis: gap map for C000 after the first cycle (2026-10-11, last written 23:38Z by the shell clock)

Sources: every claude/B01..B19/STREAM_NOTES.md (all nineteen present, stamped 22:29-23:16Z), BOARD.md of 23:19Z, the B20 Codex runs A096, A097, A098, and the B20 run 20261011T225100Z-claude-B20-erasure-activation-transfer. Statuses below are as the streams report them; "author-proved" means not yet independently reviewed. Full FEI (C000) is OPEN. Nothing in this cycle proves or refutes it.

## 1. Gap map for C000

**One inequality is left.** Every stream that reduced C000 landed on the same statement, in one of its equivalent forms (constants move by at most 2/ln 2 or 3/ln 2):

- C018: K_E = sup B/I finite, B = sum_i H(S_i|S_-i); equivalently L <= K I with L the downward-log-ratio sum (B08 calls it M_edge; B13 and B16 call the per-coordinate piece lambda_i or Q_v).
- Existential erasure K_B = sup_f min_i B_i/Inf_i finite (A001, B06 R3, B15, B17).
- Block existence (B11 open line): by B06 R1, H(S_A|S_Ac) >= sum_{i in A} B_i, so a good proper block exists iff a good singleton exists. The B11 target is FEI-equivalent, not weaker.
- KL form (B13): every f has i with KL(nu_i || q_i) >= log2(1/Inf_i) - K.
- Retained-KL tree payment (B13 and B16 sandwich): on every stopping tree the summed lambda charge equals the entropy drop up to (3/ln 2) times the influence queried.

**Hardness-preserving reductions (none of these weakens C000):** small total influence for H (Shalev, literature) and now for B as well (B20 run: K_E <= K_E(low influence) + 1.7501); small maximal influence (B01 localization with A002 diffuse admission); full Fourier support (A002 point flip); activated seeds (C013; B20 run gives the exact B of an activation); recursive composition, where B/I stays B(f)/I(f) while H/I tends to H(f)/(I(f)-1) (B15), so the difficulty sits in restrictions and any proof must be hereditary; product-biased prime gates (B09 localization, equivalent to universal biased FEI+).

**Closed fragments (author-proved unless noted).** Root pairs (empty,{i}) of B are paid with 1.7501 I (B20); for balanced h the level-one log bank Lambda(h) <= (4+6/e)(I-1) nats (B12 lead); B_i <= h2(Inf_i), hence any coordinate with Inf_i >= tau has B_i <= log2(e/tau) Inf_i (B01, B05); the multiplexer selector debt is at most I_sel log2(e^3 a/I_sel) and that is sharp (B04 lead); J_i <= B_i at uniform bias (B13, Maassen-Uffink); the one-bit biased tax has the closed form tau*(p) = h2(p) - min_t F(t) (B10 lead); tau*(p) <= Delta(p)/2 is so far checked numerically only, while the endpoint coefficient 1/2 is proved (A041, A046, A047, A096; B09 lead). Classes with FEI recorded this cycle: read-k unions of gates (C003, constant 7 log k), the threshold-function theorem B19 is auditing (Theorem A, C_reg = log2(4+e) + 2 log2(e pi) ~ 8.9365; chain read with no gap so far), sunflower (A006, <= 25/2 I), PP_q projective-plane DNFs with rank and rarity paid below 93 I (A014), point-defect tensors (H <= 4I), affine support dimension <= 4 (a finite statement, B06/B17/B18 agree).

**The gap, in its sharpest current form:** for arbitrary Boolean f,

    sum over nonempty S and i not in S of phi(fhat(S)^2, fhat(S+i)^2) <= K I(f),

where phi(a,b) = (a+b) h2(b/(a+b)). The root pairs are paid; Booleanity has to enter at |S| >= 1, because every refuted helper below is a statement that holds or fails without using it at those levels.

**Refuted or retired (do not retest under unchanged quantifiers):** all-coordinate local refunds L <= Kd + A V_post + B M_inf (B05, accepted); selector-only payment B_W <= C I_W (bent splice, already at a = 1); fixed Renyi order below 1 (point defect); tax-free biased J <= M (AND at p = 1/8, q = 1/4); any O(p) one-bit tax; raw-L collision payment (Z = 319/256); blind M log(1/M) (A077); a single global order with the rank code (B19, XOR of AND_L blocks); component-entropy and max-component-ratio descent (B11); exact-arithmetic invariants without perturbation stability (B14: pad and flip one point and U grows like N Var); "restriction preserves H/I"; pointwise heat envelopes (A066); amplitude proxy A_i (fails at K = 4, n = 32).

## 2. What each stream closed this cycle

- B01: good-coordinate equivalence and tensor/selector/point-flip admissions (A001, A002) re-derived; erasure-fraction bridge and low-influence localization (lead, in write-up).
- B02: sunflower posterior and dictionary codes (A006-A008, three unreviewed, over the cap of two); single-gate tables cost log m per used gate on tribes (lead).
- B03: the 7 log k of Theorem 5.1 split into label, subset and rank terms; PP_q unbounded-read family (lead); A014 interference repair for PP_q.
- B04: A016/A017 addressing ledgers re-derived; sharp selector debt I_sel log2(e^3 a/I_sel) with tensor bent splices attaining it (lead).
- B05: no-go accepted at local scope; odd-2-face credit Q(f), tree-independent, with B_i <= (1/2)I(g h) + log2(e) d (lead).
- B06: block-to-singleton reduction R1; leaf-partition invariance R2 (only leaves matter); good coordinates on restriction-closed classes are FEI theorems.
- B07: signed entropy anchor (A031) holds but its calibration needs no Booleanity; support <= 4 law census (A032).
- B08: exact TC restriction ledger with a nonnegative Gamma term (lead); notation clash fixed (A036 "B" is the marginal sum M).
- B09: biased block identity; uniform one-bit tax with coefficient 1/2 (lead); localization to prime gates.
- B10: the same one-bit bound in closed form through optimal qubit uncertainty (lead); multi-bit case would follow from additivity of the optimal Shannon uncertainty bound under tensor products (not yet used).
- B11: critical witnesses are tensor-indecomposable (A051); log-Sobolev constant re-derived (A052).
- B12: coherent erasure split and monotone bound L_j(x) <= B_j(g); level-one log bank for balanced h (lead); A057 root ledger is depth-lossy.
- B13: retained-KL sandwich, J_i <= B_i, KL form of FEI, exhaustive n <= 4 constants (C_4 = 3.4025 at AND_4; K* for D = 4.8677 at the 3-bit point function); Q* per rule as the right falsifier.
- B14: A067 granularity proof holds; point-defect neutralization no-go; hybrid code lemma (lead).
- B15: A071 grid retired; composition calibration (B/I invariant under recursion while H/I grows toward H(f)/(I(f)-1)).
- B16: retained-KL tree payment equals the entropy drop tree by tree (lead), so Q/I tests on bounded-ratio families prove nothing.
- B17: K_B two-sided equivalence; zero-erasure transport (H/I never decreases under a B_i = 0 restriction); A082 finite constant 2.6725 at the 3-bit point function.
- B18: A031, A061, A067 and the affine-4 bridge hold; the bridge is exactly the n <= 4 statement.
- B19: Theorem A (LTFs) proof chain read with no gap so far; rank-code no-go for any single global order.
- B20: K_E is low-influence complete (B20 run); A096 claims hold with one sign typo in its report text; A097 reference telescope read; A098 reconstructed the A097 KL subclaim.

## 3. Contradictions and duplications between streams

1. **A falsifier that adds nothing.** B08 (A040), B17 (A082), B18 (A089) and B01 (A001) are all assigned to compute min_i B_i/Inf_i on the B05 sparse bent defect family, and two of the notes say growth there would refute FEI. It cannot grow unless H/I grows first: min_i B_i/Inf_i <= B/I (mediant) <= H/I (B <= H by the chain rule, since conditioning on all other coordinates only lowers each term). So the test of record is H/I on that family, which is cheaper. B13's min_i D_i/d_i = 3.38 and 3.87 (k = 4 and 6, at data coordinates) are upper bounds for min_i B_i/Inf_i provided D_i = B_i + J_i (see the end of this section). The min_i computation calibrates a coordinate rule; it is not an FEI test. One agent (A082, symbolic in k) is enough.
2. **The one-bit half tax was derived three times** (B09 lead, B10 lead, A096) and four reviews are scheduled (A045, A046, A073, A090). The B10 closed form tau*(p) = h2(p) - min_t F(t) is the sharp quantity; the A096 bound h2(r) - h2(delta) is a cruder bound on the same tax (0.1275 bits at r = 1/2, where it is not sharp). Whether the two are ordered pointwise was not checked here. One review (A090) suffices.
3. **The retained-KL sandwich was proved twice** (B13 lead, B16 lead) and is the per-coordinate form of the C018 L-bound (also A061, B08 M_edge). Consolidate under one claim id before A099 assembles.
4. **The existential erasure equivalence was re-derived four times** (A001, B06 R3, B15, B17). It is the C018 induction.
5. **B11 open line versus B06 R1.** B11 lists proper-block descent as its open target; with R1 it is FEI-equivalent. Not a contradiction of results, but the B11 target is mislabeled as a weaker statement.
6. **Notation.** "B" is C018 erasure everywhere except A036 (marginal sum, fixed by B08); B04 and B12 use B_W for the block version H(S_W|S_Wc). Keep the subscript.
No numerical contradiction found. The n <= 4 constants of B13 (4.8677 = 12 - (9/2) log2 3, for D_i/d_i) and A082 (2.6725, for B_i/Inf_i) both sit at the 3-bit point function. Re-derived here: fhat(empty)^2 = 9/16, the other seven squared coefficients are 1/16, Inf_i = 1/4 and B_i = (5/8) h2(1/10) + 3/8 = 1 + (5/8) log2 5 - (9/8) log2 3 = 0.6681, so 4 B_i = 2.6725 matches A082 exactly. The gap 4.8677 - 2.6725 = 8 - (5/2) log2 5 = 2.1952 equals 4 J_i with J_i = 2 - (5/8) log2 5 = 0.5488, which is what D_i = B_i + J_i predicts; J_i <= B_i (B13) and J_i/Inf_i < 2/ln 2 both hold. That reading of B13's D is inferred from the numbers, not from B13's definition.

## 4. Five routes to full FEI, ranked, with the next step for each

1. **Booleanity above the root of B.** Everything else reduces to the displayed gap, and the root level is paid. Next step: bound the level-one-to-two pairs sum_{|S|=1} sum_{i not in S} phi(fhat(S)^2, fhat(S+i)^2) by C I(f), replacing |fhat(i)| <= Inf_i by the level-two Booleanity relations sum_S fhat(S) fhat(S xor U) = 0, or find a family where that ratio diverges. Owners: A096 with B07 (A031 has the F^4 = 1 form of one coordinate) and B12 (the level-one bank). Test every candidate against the non-Boolean control n^(-1/2) sum x_i (B07, B14).
2. **Odd-face credit charged at bad nodes (B05).** The credit is tree-independent and cannot be double spent; the open line is localization. Next step: freeze a spec and compute E sum over bad nodes of (1/2) I(g_v h_v) against I(f) for the control-first and greedy rules on the B05 family k = 2..8 and on AND-of-bent splices (A025), then prove the bound for one rule on a class not already known FEI.
3. **Biased prime gates with the sharp tax (B09/B10).** The channel part is paid by tau*(p) <= Delta(p)/2. Next step: E_{>=2} <= K Delta for two-weight thresholds uniformly in arity and bias (A041), and the multi-bit tax through tensor additivity of the optimal uncertainty bound (A048/A049).
4. **Whole-set codes and congestion (B02/B03).** Next step: the PI-J posterior residual on Majority_n exactly, aiming at O(sqrt n) = O(I) (A006), and the A014 interference lemma stated for an arbitrary union (not only PP_q).
5. **Rule-based heredity (B13/B06/B17).** Since min_i is automatic on bounded-ratio families, the content is a rule computable without knowing H that stays good along its own tree. Next step: Q*_root/I for structural rules (control-first, max-influence, data-first) on B05 k = 6 and AND-of-bent splices (A065), and a proof for one rule on a class closed under restriction, tensor and activation.

## 5. Distinct next actions issued by B20 (one per agent)
- A096: correct the sign in the report sentence; then route 1, level one to two.
- A097: insert the B05 activated bent-defect leaf laws into the telescope and report sum pi (B_h - kappa_h)/I_removed exactly for k = 2, 4, 6, 8 (with the B20 activation formula as the leaf input).
- A098: allocation: retire three of the four min_i computations on the B05 family (keep A082), retire three of the four half-tax reviews (keep A090), move the freed packets to routes 1 and 2.
- A099: assemble the reduction chain C005, C006, C018, C019/C024, the B06 R1 and R2 identities, the B20 low-influence completeness and the A097 telescope into one source, open leaves as explicit conjectures, one claim id per duplicated theorem.
- A100: propagate: A096 sign typo; B11 open line relabeled FEI-equivalent; min_i on bounded-ratio families relabeled calibration.