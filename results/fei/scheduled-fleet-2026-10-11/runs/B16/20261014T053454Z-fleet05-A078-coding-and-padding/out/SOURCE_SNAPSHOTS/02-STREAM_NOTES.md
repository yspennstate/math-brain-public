# B16 stream notes (Claude lead) - v2, 2026-10-11 23:25Z

Full FEI OPEN. Bits. Lead run: claude/B16/runs/20261011T225600Z-claude-B16-retained-kl-sandwich (CLAIMS.json holds the proofs; REPORT.md could not be saved there).

## Established
- B16-RETAINED-KL-SANDWICH@1 (PROVED, author; review A092): for every f and EVERY stopping tree,
  Q_T + E H(leaf) <= H(f) <= Q_T + E H(leaf) + (3/ln2) M_T, M_T <= I(f) - E I(leaf),
  Q_v = sum_T m_T log2(q_T/m_T) = M_v[log2(1/M_v) - D_2(nu||q)]. Node: Q_v <= B_v <= Q_v + M_v/ln2, JS_v <= 2M_v/ln2.
  So ISOSPECTRAL (8.1) holds for one complete tree iff for all trees iff FEI (shift 3/ln2). Tree selection is irrelevant for Q.
  Checked on all 65,536 functions of 4 variables, every node: violations 0.0.
- B16-MAJORITY-LAMBDA-DIVERGENCE@1 (EVIDENCE): complete trees of Maj_n, Lambda_T/I >= 0.39, 0.65, 0.98, 1.36, 1.77, 2.20, 2.65, 3.12 at n = 5..513 (doubling), about (1/2)log2 n - 1.4; skipping exact isospectral splits (s=0, share of I ~ 1.25/sqrt n) leaves 2.95 at n=513; H/I <= 2.83. Thresholds are monotone so no tensor factor. LOG_ALLOCATION route (8) is not self-contained: it needs outside leaf certificates (OWZ symmetric FEI).
- A076 tribes spectrum and I formula: re-derived (product formula) and brute-force checked exactly for 6 (w,t). Whole-block K>=4 is dominated by spectator-tensored high-ratio functions (known C lower bound about 6.5).
- A077 point-defect ledger: R/I=(n-1)/2, Q<=2I, Q/I -> 1 confirmed to n=12 (A078 also accepted it).
- A078: parity coding is peeled at zero entropy cost; minimal code cost M(f) tensorizes; H <= C M(f) is FEI-strength.

## Next target per agent
- A076: f = Maj(x_1..x_{n-1}, Tribes_{w,t}(y)). Exact Lambda_T and true B_v over y-first, x-first, interleaved orders, all influence included, leaves certified only by the symmetric-function theorem. Does Lambda + certificates stay O(I)?
- A077: drop Q/I tests (vacuous unless H/I diverges). Prove the majority divergence: explicit local-limit constants for the good-node mass sum_{d<=n/2,|s|<=sqrt(n-d)} w_v j_v >= c I and kappa_min >= c' there (first unproved line of B16-MAJORITY-LAMBDA@1).
- A078: find a per-node charge L_v with Q_v <= L_v that uses more than (epsilon, kappa_min) (e.g. j_v times a log of a child Renyi-2 or level-weight ratio) and test L_T/I on Maj_n with the A076 threshold code. Per-node statement Q_v <= C Inf_v at a selected coordinate is the only non-vacuous use of Q: hunt a family where it fails at every coordinate.
- A079 (G-PHASE-COND): address selector f(x,y)=sum_u 1{x=u} g_u(y), distinct bent g_u: exact H(S_Y|S_X), I_Y, marginal phase energy; name the conditional bound that fails; tensor guard.
- A080: FEI_DISPROOF_STANDARD.md (actual Boolean f_m, proved H/I -> infinity; tensoring and spectator rules; activation equivalence; the sandwich: no gap between Q and H can give a disproof). Then review B16-RETAINED-KL-SANDWICH@1 line by line.

## Do not repeat
- Q/I on any family with bounded H/I; blind M log(1/M) charges (refuted); point-defect H/I (-> 4); fixed-Renyi (O-RENYI); B05 local no-go.
- Whole-block constant lower bounds without the spectator comparison.
- Floating-point ratios called certificates.
