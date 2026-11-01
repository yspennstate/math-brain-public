# Reviewer C: report on RANKING.md (probability campaign, September 2026)

Written 2026-09-14. I read RANKING.md and INDEX.md in full, then the memos behind every Tier 1 row
(F0090, F0064, F0064b, I0086 and the classical companion, thirteen_settled §§2, 11, 12 with the Codex
packets P0340/P0341, H0019, F0063, F0055, F0056, F0057, F0058, F0059, F0060, F0061/F0062) and seven
Tier 2 rows (P0243, P0242, H0020, H0010, H0013/H0014, thirteen_settled §4 Agresti–Veraar and §10
Lyons–Peres, the Leskelä pair P0289/P0291). Where a memo's claim rests on a displayed identity or
inequality I re-derived it by hand rather than trusting the memo's "author checked". I list the
Lean files' theorem statements as they stand in `prob1000_lean_20260908/` (P0340, P0208, F0055
are what they say: arithmetic cores, no probability). I did not read the Rozikov, Khoshnevisan,
frog-model, Konstantopoulos, MMPP or Randomstrasse memos beyond their index lines, and I say so
where it affects a score.

Scores are 1–5 as in the draft: importance = would the community care that this particular
question is settled; strength = is the argument complete on the page and would a referee accept it.

## 1. The most important finding: one Tier 1 row is wrong as stated

**Janson Problem 18.40 (memo F0060) — the theorem is false as stated and the proof has a gap.**

The memo claims: for every weight sequence with w_0 > 0 and ρ = 0 and m/n → λ, there are infinitely
many n with P(Y_(1) = m) → 1 (the whole mass in one box). Counterexample: w_k = k! on the full
support {0,1,2,...} (Φ has radius 0, so ρ = 0, ν = 0, λ > ν). At any m, compare the single box
(n·m!) with "one box of size m−1 plus one singleton" (n(n−1)·(m−1)!·1!): the ratio is (n−1)/m → 1/λ,
and "box of m−k plus k singletons" contributes ≈ λ^{−k}/k!. So P(Y_(1) = m) → e^{−1/λ} < 1 along
every subsequence, not 1. (The memo's own numerics use Janson's sparse support {0,1}∪{i!}, where the
singleton competitors are not available — that is why its table shows 120.00 and 720.00.)

Exact check (`scratchpad/f0060_check.py`, rational partition functions, w_k = k! on the full support):

| m | n | λ | P(Y_(1) = m) exact | e^{−1/λ} |
|---|---|---|---|---|
| 20 | 20 | 1 | 0.3384 | 0.3679 |
| 40 | 40 | 1 | 0.3567 | 0.3679 |
| 20 | 40 | 1/2 | 0.0948 | 0.1353 |
| 40 | 20 | 2 | 0.6075 | 0.6065 |

The probability converges to e^{−1/λ}, nowhere near 1.

The gap is inequality (3): "a mixed configuration cannot beat the best pure one, up to o(m)". Mixing
box sizes gains entropy of order m: with f ≡ 0, λ = 1, m = 400, the class "100 boxes of size 2, 200
of size 1" has log-weight log[400!/(100!200!100!)] ≈ 407 > 400 = m·max F. In general the extra term
is m·Σ_j θ_j log(1/θ_j)/s_j, which is Θ(m), not O(√m); the chaining over multiplicative blocks in
the proof of the Theorem then does not close (the per-block error is O(1) per ball, not C/√m, and
F can grow more slowly than log log s while ρ = 0 still holds).

What survives: the weaker conclusion Y_(1)/n ↛ 0 is true in the k! example (Y_(1) = m − Poisson(1/λ))
and is plausible in general, but it is not proved by this memo. The reduction memo F0059 (Problem
18.39) inherits the same rate comparison and its "Proposition" is only as good as (3). Both rows
should go back to `unverified`; INDEX.md's "Janson Problem 18.40 | NO" should read "open; flawed
argument on file".

This is exactly the kind of error the draft's "author checked, exact toy" verification word does not
catch: the toy was run on the source's sparse example, the theorem was stated for all sequences.

## 2. Row-by-row: what I checked and how I score it

### Tier 1

| # | Row | Draft (imp/str) | Mine (imp/str) | What I checked; why I differ |
|---|---|---|---|---|
| 1 | Kalai Conj. 8 = GPS open problem 1 | 5 / 3 | 5 / 4 | I checked the Shannon step (uniquely decodable quadtree code, expected length 1 + 4ΣE|S_{2^k}| + C_0E|S_1|), the one-scale bound (this is GPS's own first-moment estimate E|S_r| ≍ (R/r)²α_4(r,R)), and the geometric sum via quasi-multiplicativity and α_4(1,r) ≥ c r^{−2+ε}. The argument is correct and short; its content is that the spectral sample has dimension < 2 so the coarse scales cost less than the finest. One independent read on file. Strength up to 4. Excluded from the paper question (posted by the author 2026-09-13). |
| 2 | Janson Problem 20.2 (b),(c) + Thévenin's closing conjecture | 4 / 3.5 | 3.5 / 3.5 | Theorem A re-derived: two rare atoms L^± ≈ (1−ν)n ± A√n with mass n^{−4}; under the conditioning exactly one is present (two exceed n−1 because q < 1/2; none forces a Hoeffding-size bulk deviation), the sign is fair by the LLT, and N_1 = B = m − L^± − M pins the count to ∓A√n up to the medium fluctuation, controlled by the Chebyshev/sup-P(B=b)/LLT ratio. Complete and elementary. Theorem B (critical, σ² = ∞), the case Thévenin actually emphasised, is a sketch resting on a lattice moderate-deviation expansion for a triangular array — that is real work, not bookkeeping. Importance down half a point: a lacunary law breaking a conjecture stated "for any μ" is what a specialist would expect after Janson's own Examples 18.36–37; the positive result under regular variation stays the substantive one. The memo's repaired question (local flatness at the condensate scale) is the paper's real contribution and should be its centre. Does the answer answer the question as posed? Yes for (b),(c) read literally; Thévenin's conjecture is quoted with "for any μ critical with infinite variance … subcritical with no exponential moment", and the construction meets both hypotheses. |
| 3 | Hasebe–Ueda Problem 3.3, C = 1 | 3.5 / 5 | 3.5 / 5 | Both proofs re-derived line by line. Choquet route: Φ and Ψ closed forms, the D,m collapse (Ψ/D = 3m² + s(6m−D²) − s², Φ/D = 3m² + m(1−D²) + s(1−2m) − s²), Lemma A (max at m = D²/4 gives (3D²−4s)(D²+4s)/16), Lemma B (concave in s, endpoints s = 0 and 3/4, convex in m with derivative (D²−1)/2 ≤ 0 at D²/4, value (1−D²)(D²+3)/16): all correct. Cauchy-profile route (§11 of thirteen_settled): the moment inequalities a ≤ D²/4 and b + 3a² ≤ D²a (from (X−X')⁴ ≤ D²(X−X')²), the identity 1/F = (b+2ay+y²)/(a+y), the Jensen step y ≤ 3a, the factorisation (y−3a)(y+a) + (4a−D²)y: all correct. The extreme-point step (≤ 2 atoms under one linear constraint) is Winkler's theorem; the criterion is the source's Lemma 3.1. The rigidity corollary follows. On the printed "2 ≤ C ≤ 4": I confirm the Bernoulli example gives C ≥ 1, not 2 (threshold t = 4 = D² with D = 2); the memo states this once, neutrally, which is right. The classical companion (D²/4 for μ ∗ N(0,t), improving 9D²) is the same argument with H(κ) = θ(a+b)(1 − t/(ab)), which I verified; its symmetric-kernel criterion ψ(a)+ψ(b) ≤ 0 is a genuine bonus (recovers the classical two-Gaussian and two-Cauchy thresholds). Agree with 3.5 / 5. |
| 4 | Aldous–Janson Ansatz 20 and Open Problem 14 | 3.5 / 4.5 | 3 / 4.5 | OP14: ℓ(T) ≤ S(T) verified (2 + |h(A)−h(B)| ≤ n(T) since a full binary tree on k leaves has height ≤ k−1), Lean-checked in P0340.lean (drawn_le_sumDepth, drawn_eq_sumHeights_add_height, standard axioms); with the authors' Theorem 3 (E depth ~ (3/π²)log²n) this gives O(n log²n), refuting n log⁴n by two logs, and the memo locates the missing 1/m in heuristic (75). The Θ(n) limit with explicit c_ℓ is a further, plausible argument. Ansatz 20: a(n,n) = 1 is a correct but cheap refutation — a test function charging the endpoint j = n along a subsequence; a referee would say the Ansatz was obviously meant for test functions that do not see the moving root, and the authors "invoke" it only for regular weights. On its own 1.5 / 5. As a pair 3 / 4.5: a short correction note the authors would welcome, not a result the community would cite. |
| 5 | arXiv:2608.04303 Conjecture 1 and layer half of Conjecture 2 | 3.5 / 4 | 3 / 4 | Theorem 1 verified: the recursion u_i = exp(−∫_0^y(1−u_{i−1})) with u_0 ≡ 0 is exactly F_i(y) = E∏F_{i−1}(y−ξ_j) for a rate-one Poisson process of children, so s_k(y) = P(M_k ≤ y) for the PWIT minimum and ℓ̄_k = E e^{−M_k}. The web search confirms Addario-Berry–Ford (AAP 2013) treat displacement v_j = sum of j Exp(1), "in particular the Poisson-weighted infinite tree", with median n/e + (3/2e)log n + O(1) and exponential tails, and derive the RRT height; Aïdékon's convergence in law closes Theorem 3. The exponential-moment step (c_1 = 2 < e) is right. Theorem 4 (max layer = ⌊diam/2⌋, two linear root subtrees) is right. So the conjecture is a theorem by dictionary: complete, but the mathematics is two citations plus one identification. Importance 3: a physics-audience arXiv preprint, the velocity-selection question is open only from where the authors stood. |
| 6 | Janson Conjecture 20.1 | 3 / 4 | 2.5 / 4.5 | Proof re-derived: Lemma 14.9 weight W_n = nℓP(S_{n−N} = n−N−ℓ)/((n−N)P(S_n = n−1)), the two LLT bounds giving W_n ≤ C'ℓ(n/(n−N))^{3/2} and W_n ≤ C'n^{3/2}ℓ^{−1/2} (from n−N ≥ ℓ), the split at N ≤ n/2, and the (r+1)-moment bound on the unconditioned generation sizes. Complete and short; the case r ∈ (0,1) with σ² = ∞ is correctly left open. Importance 2.5: Janson called this "we conjecture" and the survey's own [59] already had bounded moments under one extra moment; a nice closing lemma, not a result. |
| 7 | Janson 18.x group | 3 / 4 | 3 / 3.5 (group) | Individually: **18.4** (F0055) 3 / 4.5 — the empty-box/singleton comparison (2) re-derived; correct, elementary, removes the monotonicity obstacle Janson named; Lean core for the binomial ratio and tail sum. **18.41, 18.42** (F0061/62) 3 / 4.5 — Theorem A re-derived (spike bookkeeping, the deficit 1361/168·8^{i−2} vs m²/4 + 5m/2, the 2^{m+n}e^{−m³/128} bound); Theorem B's cliff mechanism checked against Theorem 18.33's n^{β−2} one-box advantage (the cliff supplies n^{4.33}e^4 the other way); both explicit and complete. **18.30** (F0058) 2.5 / 3.5 — Theorem 1 (part ii) complete, mechanism sound (mean of S_n outside the bulk when σ² = ∞), Theorem 2 (part iii) a sketch; the memo records its own retracted first claim, which is to its credit. **18.9** (F0056) 2.5 / 4 — Theorem 2 is a lattice (span aZ) obstruction that answers the literal question; Theorem 1 is the substantive positive result and is plausible but has no independent read. **18.10** (F0057) 2 / 3.5 — a modification of Janson's own (vi) proof; no numerics, no independent read, "pending a source correction" in the index. **18.40** (F0060) 2.5 / 1.5 — false as stated, see §1. **18.39** (F0059) 1.5 / 2 — reduction inherits the flaw. |

### Tier 2

| # | Row | Draft | Mine | Notes |
|---|---|---|---|---|
| 8 | Aldous–Fill 4.48, 4.45, 4.30, 7.27 | 3 / 4.5 | 2.5 / 4.5 | 4.48(a): τ_0 = (2+2ε)/(1+ε+ε²) re-derived from trace and principal minors; τ_1 → root of e^{−t}(1+t) = e^{−1} = 2.146; correct. 4.48(b): the eigenfunction/optional-stopping argument u_i = λ_2Σx_ju_j is correct and clean; prior-art risk moderate (Lovász–Winkler have comparable spectral bounds; the memo could not check). 4.45: exact rational witness, fine. 7.27: nine Lean theorems on the cycle blow-up. All minor questions from an unfinished 1994 book; the community treats that list as a curiosity. |
| 9 | Agresti–Veraar Problems 4, 5 (critical Allen–Cahn) | 3 / 4 | 3.5 / 4 | Itô calculus re-derived in both directions (Y = 1/U, V = e^tY, time change s = (e^{2t}−1)/2, R = V/√2 is BES(4)); the hitting estimate P(inf R ≤ x) ≍ x² gives tail index exactly one, so E sup‖u‖² = ∞ with E‖u_0‖² finite. Sharp, elegant, at the critical exponent the authors singled out. Importance up: prominent authors, a 2025 problem list, an explicit solvable obstruction. Referee risk: that the spatially constant solution is the variational solution of Theorem 6.4's framework (uniqueness) — almost certainly yes but the note must say it. Manuscript and EndpointCore.lean exist. |
| 10 | Salez Problem 2.4 | 3 / 4 | 2 / 4 | Literal form only: the degree is unbounded (~√|G| log), which is not what the workshop question means; retired in any case. |
| 11 | Lyons–Peres 17.18 | 2.5 / 4 | 2.5 / 4 | The AND/OR endogeny recursion r_{n+1} = 3/10 + (3/5)r² + (2/5)r³ re-derived (OR: 3/4 + r³), fixed point 1/2 attracting from 1/4; the stationarity argument is right. Prior-art risk: AND/OR recursive distributional equations on GW trees are a known object (Aldous–Bandyopadhyay); check before claiming. |
| 12 | Burdzy–Scheutzow 7.5 | 2.5 / 4 | 2 / 3.5 | Sound; very likely a consequence of Thorisson's shift-coupling / Last–Mörters–Thorisson; the memo says so itself. |
| 13 | Hasebe–Ueda–Wang 4.7 | 2.5 / 4.5 | 2.5 / 4.5 | Two-atom measure, exact bounds uniform in R; agree. Most likely of the free-probability items to be already noticed by the authors' group. |
| 14 | Leskelä Problems 1 and 3 | 2.5 / 4 | 3 / 4 | Raise importance: Ross's second conjecture is a named conjecture in queueing with a literature (Rolski, Chang–Chao–Pinedo, Bäuerle–Rolski); a non-reversible cyclic environment refuting the universal clause, with the light-traffic expansion re-derived by a second reader and turned into an exact second-order criterion (Var of the one-service-time average of the environment), is a real contribution. Problem 3 (three-state star, non-monotone but supermodular-ordered under speed-up) is a complete argument with a finite certificate. Prior-art comparison with Heyman and Miyoshi–Rolski is the open obligation. |
| 15 | Neri–Pinto Remark 3.7 | 2 / 4.5 | 1.5 / 5 | Arithmetic verified: w̃R = (0,16,−7,−7,−2), Q = 6 > 0. Exact; a remark in a 2026 preprint. |
| 16 | Rozikov 3, 4, 10, 11 | 2 / 4 | 1.5 / 4 | Not read closely; two Lean cores on file. Niche audience. |
| 17 | Khoshnevisan 1, 3 (d = 3, 5) | 2.5 / 3.5 | 2 / 3 | Record is a night report only; I could not audit it. |
| 18 | Kumar–Duddala 3.2; Lévy-drift 5.3(ii); frog 3.6 | 2 / 4 | 2 / 4 | Lévy drift (H0013): Theorem 2 mechanism verified — a downward jump of size m at τ gives a step function whose Rayleigh quotient is e^{−m}τ^{2δ−2}, so the confinement charges only (2δ−2)log τ per well while the Lévy measure supplies wells of depth (2δ−2+θ)log τ at rate ≥ c m^{−α}; Borel–Cantelli over independent blocks; Persson gives λ_ess = 0. Correct and sharp; on its own 2.5 / 4, and the sign dichotomy is a nice point. Kumar–Duddala: E[∂W_n] = 0 plus a.s. nonnegative limit kills uniform integrability — correct, a slip in a 2026 preprint, 1.5 / 5. Frog model: not read. |
| 19 | Pollett (ii); Bradley Q7; Konstantopoulos | 1.5 / 3.5 | 1 / 3.5 | Bradley: the constant sequence fails by the survey's own theorem; that is not what Bradley was asking (the memo says so). Pollett: probably Foley–McDonald. |

### Not candidates / partial: I agree with the draft's list. MMPP 4.1 is He 2021; Bandeira 1.2 is Hutnik 2026; Sylvester–Hadamard is 1983.

### ProofNet24 tracks: nothing closed; agree.

## 3. Literature checks run today (nothing found on any candidate)

- Hasebe–Ueda Problem 3.3 / sharp constant: only the source and its repository copies; the 2026 JTP paper on free positive multiplicative BM does not touch the additive constant. Nothing found.
- Gaussian diameter criterion (μ ∗ N(0,t) unimodal for t ≥ D²/4): searches on normal location mixtures with mixing support of length 2σ returned Behboodian/Sitek-type two-component results and nothing on the general measure. Nothing found, but this is the classical side and I would not be surprised if a 1970s statistics paper has the two-point extremal statement; flag it as the prior-art risk of the package.
- Thévenin's conjecture / outdegree counts not normal: nothing after the 2020 paper (a 2026 "tentacular" degree-distribution preprint is regular-variation work). Nothing found.
- Addario-Berry–Ford: confirmed the class and the PWIT statement. Stepanyants et al. 2608.04303 exists as described. No paper identifying the layer recursion with a BRW.
- Agresti–Veraar critical Allen–Cahn: nothing on the γ² = 2 energy bound.
- Janson 18.4 / 18.9 / 18.41: nothing since 2012 (the 2021 universal height/width paper and the Gibbs-partition phase diagram are adjacent, not on point).
- Aldous–Fill 4.48: nothing; the online book carries the problem without a note.
- Kalai / percolation entropy: 2026 FEI literature (lower bounds, new general bounds) does not state the percolation case.

## 4. Top three candidates for a stand-alone paper (Kalai excluded)

**(1) The sharp unimodality constants for free and classical Brownian motion (Hasebe–Ueda Problem 3.3, C = 1, with the classical companion D²/4 and the symmetric-kernel criterion).** Importance is moderate but honest: the problem is posed in print, the answer is sharp, the extremal measure is identified with a rigidity statement, and the same two-atom reduction settles the classical constant (improving the source's 9D² by 36) and yields a criterion that reproduces the classical two-Gaussian and two-Cauchy thresholds. Completeness: two independent proofs of the free constant, every inequality re-derived by me, numerics at four levels including an end-to-end mode count. Verifiability: the core is four real-polynomial inequalities in (D, m, s) (Lemma A, Lemma B) and the identity H(κ) = θ(a+b)(1 − t/ab) — exactly what `nlinarith`/`polyrith` can certify; the Choquet reduction and Biane's criterion stay as cited theorems. Prior-art risk: low on the free side (searched twice, nothing), moderate on the classical companion. A referee at ALEA, EJP or a free-probability venue would accept this as a short paper.

**(2) The critical Allen–Cahn energy bound fails (Agresti–Veraar Problems 4 and 5).** Importance 3.5: prominent authors, a published problem list, and the refutation is exact — at γ² = 2 the spatially constant solution is e^t/(√2 R_s) with R a BES(4), so sup‖u‖² has tail index one and infinite mean. Completeness: the Itô calculus is checked both ways; the hitting-probability step is standard. Verifiability: a partial Lean file exists but the core is stochastic calculus, not arithmetic, so a Lean verification would cover only the algebraic identities. Prior-art risk: low (2025 problem). Referee risk: the note must show that the constant-in-space process is the unique variational solution in Theorem 6.4's setting; if that is a sentence, this is publishable as is.

**(3) Outdegree counts in conditioned Galton–Watson trees need not be asymptotically normal (Janson Problem 20.2, Thévenin's conjecture), with the local-flatness question.** Highest importance of the three (Probability Surveys, a named conjecture in EJP), and Theorem A is complete and elementary. But Theorem B — the critical infinite-variance case, which is the case people care about — is a sketch whose one real input (a lattice moderate-deviation expansion uniform over a triangular array) is not on the page; and the result's flavour ("a lacunary law breaks a conjecture stated for all laws") will draw the referee comment that the conjecture needed a regularity hypothesis everyone assumed. No Lean-checkable core. Needs Theorem B written in full and the repaired conjecture stated as the paper's theorem-shaped question before it is a paper.

Near miss: the RRT layer distribution (H0019) is complete and low-risk but is two citations plus one identification, better as a short note or a letter to the authors than a paper.

**My choice: (1), the unimodality constants.** It is the only candidate that is simultaneously complete on the page, independently proved twice, checkable by a proof assistant in its load-bearing part, sharp, and low prior-art risk. (2) is close and I would write it second; (3) is the most important but is not finished.

## 5. Where I differ from the draft, in one paragraph

The draft's Tier 1 is ordered by prominence of the poser; I would order by what is actually proved. Two Tier 1 rows drop: the Janson 18.x group loses 18.40 and 18.39 outright (false theorem, flawed reduction — §1), and the Aldous–Janson pair is carried by OP14 alone, the Ansatz refutation being an endpoint technicality. One Tier 2 row rises: Agresti–Veraar is a sharper and more citable result than the draft's rank 9 suggests, and Leskelä's Ross-conjecture pair deserves 3 on importance. Janson 20.2 keeps its place at the top of the unpublished results by importance but not by readiness. The draft's strength scores are otherwise fair; the verification word "author checked, exact toy" is not a referee, and the 18.40 episode shows why: the toy was run on a sparse support and the theorem was stated for every support.

## 6. Where the "answers" answer a narrower question than the poser meant

- Bradley Q7: the constant sequence is refuted from the survey's own theorem; Bradley's question is the characterisation, untouched.
- Salez 2.4: unbounded degree; the community's conjecture almost certainly carries a degree bound.
- Aldous–Janson Ansatz 20: endpoint charging; the authors' uses are for regular weights.
- Janson 18.9 Theorem 2: a lattice obstruction (w_1 = 0); Theorem 1 is the real answer.
- Janson 20.2 and 18.30, 18.41, 18.42: lacunary constructions; they do answer the literal questions, and Janson's survey explicitly asks about general weight sequences, so these are fair — but the papers should say in the first paragraph that regular tails are untouched.
- Hasebe–Ueda 3.3 and the classical companion: answer exactly the question as posed.
