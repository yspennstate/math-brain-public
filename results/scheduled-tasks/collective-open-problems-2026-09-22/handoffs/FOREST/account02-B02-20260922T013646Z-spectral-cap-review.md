# FOREST handoff — account02/B02 — `FOREST-SPECTRAL-CAP-REVIEW-v1`

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent target remains **OPEN** under the collective review gate. Context: **WITHOUT_VERIFIED_BRAIN**.

## Fresh lead consumed and independently reviewed

Consumed latest lead `account01/B01` `FOREST-KN-HERMITE-REDUCTION-v1`, handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`, scientific report commit `77e2822624d2ea3881807aa7bfa56174563728c6` / blob `e11be369a70e59449ea744da6f1e32040889c216`.

B02 independently checked the five requested points and records **`PASS_SOURCE_BOUND_REVIEW_1`**:

1. Semple--Welsh's published definition of independence correlation quantifies over all positive real edge weights.
2. Their final note explicitly records Cocks's fixed-graph theorem: unit Conjecture 1.1 for a graph `G` implies `M(G)` is independence correlated.
3. Proposition 3.5 gives minor closure, so unit pNC on every `K_n` reduces all simple graphs to complete graphs by deletion.
4. The disjoint marked-pair EGF `F A^4(1+4/(1-R))`, the Lagrange/Cauchy Hermite identities, and the one-variable gap reduction were independently rederived.
5. The Hermite root bound and shifted positive polynomial were independently checked. A separate exact checker brute-enumerates `K_2`--`K_6` and regresses the rational Hermite identities through `n=500`; all checks passed.

No scope failure or counterexample was found. A second independent existing-worker end-to-end review is still required before any solved-problem promotion.

## New source-valid comparison

For the all-unrooted-forest generating polynomial
`P_G(z)=sum_{F acyclic} z^F`, complete log-concavity of the homogenized matroid independent-set polynomial applies exactly: graphic-matroid independent sets are all forests, and restricting the homogenizing coordinate to `1` gives `P_G`; evaluating `z=1` is the unit uniform law.

Let `C=(rho_ij)` be the Pearson correlation matrix and `p_i=P(i in F)`. Log-concavity and multiaffinity give

`D-C >= 0`,  where `D=diag(1/(1-p_i))`.

Down-closure gives the injection `F containing i -> F\{i}` and hence `p_i<=1/2`. Therefore

`0 <= C <= 2I`.

Combining `2I-C>=0` with the lead's minimal-counterexample matching geometry improves the standardized violation cap. If `c=rho_ef>0` is a violating pair and `S` is an external pairwise-nonpositive set of size `s>=ceil((m-2)/2)`, then

`c^2+2 s c-1 <=0`, hence

`rho_ef <= sqrt(s^2+1)-s`.

With inherited `m>=15`, `s>=7`, this is `rho_ef<=sqrt(50)-7=0.071067811865...`, improving the previous `1/13` cap. In count form, a hypothetical minimal violation satisfies

`0 < ZZ_ef-Z_eZ_f <= (sqrt(s^2+1)-s)*sqrt(Z_e(Z-Z_e) Z_f(Z-Z_f))`.

An exact rational control at `s=7,c=9/121` passes the old PSD/`1/13` test but violates the new `2I-C` cap, so the new input is genuinely stronger.

## Named partner consumed

Consumed assigned OTHER-account partner `account03/B03`, run `20260922T005605Z-b03-forest-r11b`, handoff blob `e340981b9ba04a77a0b2e51e458542980b272ff3`. Its exact activity ratio on disjoint pairs of `K_n` has `1-R_n=n^-2+O(n^-3)`, forbidding any graph-independent fixed multiplicative margin. The lead Hermite proof and the new spectral cap are compatible: both are sign-exact/asymptotically shrinking rather than fixed-epsilon arguments.

## Scientific authority

Authoritative report: `yspennstate/math-open-problems` commit `7e55e6e2259bde9d70acd38c8f08d51510d7130b`, path under `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B02/B02-20260922T013646Z-forest-r12/report.md`.

Independent audit source SHA-256: `4e320a504c35fa6fe09fabbdbb2376cdd597c91ab6aceaf1431b5be099eb9fc7`; output SHA-256: `3cce554d398260658bd7aeb8fe6a2a64b4d13f2341490e592806f96b51620a58`.

Spectral-control source SHA-256: `c3922dd899c2d89a1b74568d94256880d6c861adb7127ae8038a7b9226a6a5e4`; output SHA-256: `35a36d9a21e0a65dd9543c67f33349c0608db7017306eda9454c300f44c5ffb3`.

## B20 inventory note

Only account02's managed inventory was inspected: current managed B01--B20 are 20/20 enabled, unique/hourly-valid, role-aligned under the current owner reallocation, with quiet delivery preserved. No deficit was observed and B02 made zero scheduler mutations.
