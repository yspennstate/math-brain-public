Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `N_exact = 95 -> 96`; Section-B routes actually used in this invocation were #18 SAY IT IN ANOTHER LANGUAGE, #19 MAKE IT AN ALGORITHM, #20 FIND WHY THE ALGORITHM FAILS, followed by #2 ATTACK THE NEGATION FIRST, #25 COUNT THE SAME THING TWICE, and #7 TAKE THE LIMIT. All are explicitly RECYCLED because all 30 numbered methods had already genuinely been used on P0282.**

# NM13-07 — P0282: shadow-density ULC through defect 32, a seven-eighths long-LIS window, and exact row 96

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-07` / `proofnet24/NM13-07/`  
Category: `CLOSABLE OUTSIDE`  
Canonical source / claim: `P0282` / `operations/claims/P0282.md`  
Canonical dedup key: `chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis`  
Canonical SHA-256: `08312c764bd0e9331fed25b1f255810f3c3b9e0f81134520fa26aca4c9c471a4`  
Exclusive shard: `int(SHA256(key),16) mod 13 = 6`  
Run date: 2026-09-19 UTC  
Source status after this run: **OPEN**  
Worker status after this run: **PARTIAL**

## 1. Runtime truth and model-control limitation

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, an hour-long execution, or a support escalation.

The scheduling/task-control surface exposed here still has title/prompt, schedule or relative-start fields, timing mode, enabled state, and ordinary update/list controls. It still exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Therefore `GPT-6 / maximum` remains prompt text only in this interface. Making it binding would require an owner-authorized product/workspace/API/admin scheduler that actually persists model and effort routing fields and returns authenticated applied-runtime telemetry.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary, not a reason to bypass controls. Current root continuity also records that P26 was later successfully updated from an authorized context. The compliant workaround is therefore the task-owning/authorized workspace or an approved platform/admin/API/support repair path for the same task; never duplicate a protected task or bypass permissions. This invocation changed no schedule, permission, or ownership control.

## 2. Authoritative continuity, ownership, and required reads

The exact source remains Chen's fixed-size LIS conjecture. For uniform `sigma in S_n`, let

`ell_{n,k} = #{sigma : LIS(sigma)=k}`.

The source asks whether

`ell_{n,k}^2 >= ell_{n,k-1} ell_{n,k+1}`

for every positive integer `n` and every `1<k<n`. Poissonized Plancherel log-concavity, involution versions, Hilbert-series reformulations, and stronger Kronecker or ULC statements are related but are not substitutions for this exact source.

I reread or exact-target-recovered the current controlling and continuity material required by policy before making the theorem claims in this report:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/P0282.md`;
- predecessor report `proofnet24/NM13-07/runs/2026-09-19/2026-09-19T08-45-00Z__p0282-six-sevenths-row95.md` at commit `5ac98929d0dc323d449f54bd87fb49d9e69d7279`;
- newest visible neighboring NM13-06 and NM13-08 reports;
- exact P0282 / canonical-key / `P0282-A` / ownership / audit searches;
- the Git delta from the predecessor report commit to the frozen pre-write head.

The canonical claim still assigns P0282 exclusively to NM13-07 with the same source, canonical key, SHA-256 and shard. I recovered no owner-authorized release, competing alias owner, source retirement, POSTED settlement, campaign closure, or P0282 audit PASS. The newest NM13-06 report explicitly treats NM13-07/P0282 as an active neighbor at `N_exact=95`; the newest NM13-08 report remains `ADMISSION_PENDING` on its own screening work and contains no P0282 secondary-audit PASS. The exact `P0282-AUDIT` search still recovers no P26 or NM13-08 PASS. Required audits therefore remain **P26 NOT PASSED / NM13-08 NOT PASSED**.

The append-only intake JSONL corpora are too large for an honest claim that every unchanged byte was freshly rendered model-visible this hour. I instead relied on the already completed canonical intake reconciliation, reread the exact canonical claim, searched the exact canonical identity / attempt / audit keys, and compared the predecessor to the current Git head. Missing display was not treated as permission to reopen ownership or invent history.

The exact comparison from predecessor commit `5ac98929d0dc323d449f54bd87fb49d9e69d7279` to frozen pre-write `master` `da4d7ce2d8b2644e6e35eb5e3465ca8008dfeea0` is `ahead`, 167 commits, 0 behind. It contains no mutation of `operations/claims/P0282.md`, controlling policy files, root `QUEUE.md` / `POSTED.md` / `RESULTS.md`, campaign `INDEX.md` / `RANKING.md`, or P0282 ownership/audit state. It does contain a set of unreported own-namespace P0282 artifacts created after the predecessor report; I recover and consolidate those below rather than discarding them or pretending the run restarted at 08:45.

## 3. Frozen metric and retained theorem state on entry

Frozen metric, unchanged definition:

`N_exact` = largest integer `N` for which NM13-07 has archived exact-arithmetic certificates verifying every Chen inequality for every `1<=n<=N`.

Entry value: **95**.  
Exit value: **96**.

Retained theorem state on entry:

- complete all-`n` Chen fixed-defect frontier: `j=n-k <= 66`;
- complete all-`n` binomial-normalized ULC frontier: `j<=26`;
- growing-defect theorem: for the genuinely new `j>=67` sector, Chen holds whenever `j+1 <= n^(6/7)/8`;
- source itself remains OPEN.

No theorem frontier is silently substituted for the frozen metric.

## 4. First route: normalized Viennot-shadow density

### 4.1 Change of language

Write

`F_j(n) = ell_{n,n-j}`.

Rhoades's Viennot-shadow standard-monomial model identifies `F_j(n)` with the number of rank-`j` shadow sets, a downward-closed family inside the size-`j` nonattacking rook placements of `[n] x [n]`. The ambient number of size-`j` rook placements is

`R_j(n) = j! * binom(n,j)^2 = (n)_j^2 / j!`.

Define the normalized shadow density

`rho_j(n) = F_j(n)/R_j(n)`.

A direct cancellation gives the exact source ratio factorization

`F_j(n)^2/(F_{j-1}(n)F_{j+1}(n))`

`= ((j+1)/j) * ((n-j+1)/(n-j))^2 * rho_j(n)^2/(rho_{j-1}(n)rho_{j+1}(n))`.

Thus log-concavity of the density sequence `rho_j(n)` is strictly stronger than Chen at interior cells.

In the stable long-first-row regime `n>=2j`, `rho_j(n)` is exactly the predecessor's Plancherel correction `A_j(n)` from

`F_j(n) = (n)_j^2/j! * A_j(n)`.

### 4.2 Extension-probability algorithm and exact obstruction

For a valid rank-`r` shadow set `S`, let `e(S)` be the number of one-rook extensions that are still shadow sets. Double-counting rank-`r` to rank-`r+1` incidence edges gives

`rho_{r+1}(n)/rho_r(n) = E_{S uniform in Delta_r}[ e(S)/(n-r)^2 ]`.

This turns density log-concavity into monotonicity of an **average normalized valid-extension fraction**.

Method #20 deliberately tested the stronger pointwise statement along every valid inclusion `S subset T`:

`e(T)/(n-|T|)^2 <= e(S)/(n-|S|)^2`.

The exact shadow enumerator finds no failure for `n=2,3,4`, then finds the first failure at `n=5`, parent rank 1:

`S={(3,4)}` has `e(S)=7`, so `q(S)=7/16`, while

`T={(2,5),(3,4)}` has `e(T)=4`, so `q(T)=4/9`.

Since `4/9 > 7/16` (`64>63`), the pointwise monotonicity route is false. This does **not** refute Chen or the averaged density inequality; it identifies exactly why the obvious local extension algorithm is too strong. The archived falsifier independently checks the shadow counts `n=5: [1,16,61,41,1]` and ends `ALL_EXACT_CHECKS_PASS`.

### 4.3 Exact all-n shadow-density theorem for defects 27 through 32

The failed pointwise route led to a weaker but complete finite-defect theorem.

**Claim `NM13-07-P0282-SHADOW-DENSITY-32-01`.** For every `j` with `27<=j<=32` and every source-valid `n>=j+2`,

`rho_j(n)^2 > rho_{j-1}(n) rho_{j+1}(n)`.

**Proof.** Split at `n=2j+2`, which is the point at which the stable dimension formula simultaneously applies to defects `j-1,j,j+1`.

For `n>=2j+2`, define the integer polynomial margin

`D_j(n) = F_j(n)^2 R_{j-1}(n)R_{j+1}(n) - F_{j-1}(n)F_{j+1}(n)R_j(n)^2`.

Each `F_q(n)` has degree at most `2q` in the stable range and each `R_q(n)` has degree `2q`, so `deg D_j <= 8j`. The exact checker evaluates `D_j(n0+m)` at `n0=2j+2` for enough consecutive integer `m` to recover its complete Newton / forward-difference expansion

`D_j(n0+m) = sum_r Delta^r D_j(n0) * binom(m,r)`.

For every `j=27,...,32`, every nonzero recovered Newton coefficient is **strictly positive**; the final two degree slots are exactly zero. The archived exact counts are:

- `j=27`: 215 positive coefficients, 2 trailing zero coefficients;
- `j=28`: 223 positive, 2 zero;
- `j=29`: 231 positive, 2 zero;
- `j=30`: 239 positive, 2 zero;
- `j=31`: 247 positive, 2 zero;
- `j=32`: 255 positive, 2 zero.

Because `binom(m,r)>=0` for every integer `m>=0`, this proves `D_j(n)>0` for all integer `n>=2j+2`.

For the finite boundary `j+2 <= n <= 2j+1`, an independent exact Gessel Bessel/Toeplitz computation reconstructs the relevant `F_q(n)` by 16-prime CRT and checks all 177 boundary cells. Every normalized density margin is strictly positive; the smallest boundary ratio occurs at `(j,n,k)=(32,65,33)` and is approximately

`1.00767397093317145 > 1`.

Combining the stable Newton certificate with the exact boundary certificate proves the claim. QED.

### 4.4 Consequence: the all-n ULC frontier advances 26 -> 32

The earlier ULC condition at defect `j`, with `m=n-j=k>=2`, is

`F_j(n)^2/(F_{j-1}(n)F_{j+1}(n)) > ((j+1)m)/(j(m-1))`.

Shadow-density log-concavity gives the stronger lower bound

`((j+1)/j) * ((m+1)/m)^2`.

Their ratio is

`((m+1)^2(m-1))/m^3 = 1 + (m^2-m-1)/m^3 > 1`

for every `m>=2`. Therefore the new all-n density theorem for `j=27,...,32` implies the binomial-normalized ULC inequality on those defects. Chaining with the retained `j<=26` theorem moves the complete all-n **ULC frontier from 26 to 32**.

This is theorem movement, not frozen-metric movement and not closure of the all-`n` source conjecture.

## 5. Second route: falsify the sixth-order curvature before proving another window

The predecessor's `n^(6/7)` theorem came from the analytic expansion

`G_j(t)=log A_j(t)=sum_{m>=1} D_m(j)t^m`, `t=1/n`,

with `A_j` the Plancherel expectation of the hook correction. Before attempting another exponent lift, I wrote the new route down and explicitly tried to refute the natural hypothesis that the sixth coefficient has favorable Chen discrete curvature.

For a partition `mu` of `j`, let

`C(mu)=S_1(mu)=sum_{cells}(c-r)`,

`S_q(mu)=sum_{cells}(c-r)^q`.

Let `B_m(mu)` be the coefficient of `t^m` in `log R_mu(t)`, so `F_mu(t)=2 sum_m B_m(mu)t^m` and `G_j(t)=log E exp(F_mu(t))` under Plancherel(`j`). The one-cell formula is

`B_m(mu) = -sum_cells ((j+x)^m-(j+x-1)^m)/m`, `x=c-r`.

At order six this expands exactly to

`B_6 = j[-j^5+(5/2)j^4-(10/3)j^3+(5/2)j^2-j+1/6]`

` + (-5j^4+10j^3-10j^2+5j-1) C`

` + (-10j^3+15j^2-10j+5/2) S_2`

` + (-10j^2+10j-10/3) S_3`

` + (5/2-5j) S_4 - S_5`.

The exact self-check verifies this identity partition-by-partition through `j=12`.

## 6. Two new Plancherel moment identities by regular-representation counting

Let `X_i=sum_{a<i}(a i)` be the Jucys-Murphy elements. On an irreducible indexed by `mu`, the symmetric power sum `sum_i X_i^q` acts with eigenvalue `S_q(mu)`. Under Plancherel measure, expectation is normalized regular-representation trace, equivalently the identity coefficient of the corresponding central group-algebra element.

### 6.1 The squared second-content moment

Let `J=binom(j,2)` and `P_2=sum_i X_i^2`. Directly expanding the two-star-transposition words gives

`P_2 = J e + K_3`,

where `K_3` is the sum of all 3-cycles, each with coefficient one. Therefore the identity coefficient of `P_2^2` is

`J^2 + # {3-cycles} = J^2 + 2 binom(j,3)`.

Hence

`E[S_2^2] = J^2 + 2 binom(j,3)`

`= j(j-1)(3j^2+j-8)/12`.

### 6.2 The mixed moment E[C S_3]

The content sum `C` is the eigenvalue of the full transposition class sum `T=sum_i X_i`; `S_3` is the eigenvalue of `P_3=sum_i X_i^3`. Thus `E[C S_3]` is the identity coefficient of `T P_3`, i.e. the total coefficient mass on transpositions in `P_3`.

Fix `i` and write `m=i-1`. A length-three word in star transpositions `(a i)(b i)(c i)` is a transposition exactly when either all three indices agree (`m` words) or exactly two agree (`3m(m-1)` words). With all three distinct the product is a 4-cycle. Therefore the transposition coefficient mass contributed by `X_i^3` is

`m(3m-2)`.

Summing `m=0,...,j-1` gives

`E[C S_3] = sum_m m(3m-2)`

`= j(j-1)(2j-3)/2`.

Both identities were exact-rationally checked against direct partition enumeration through `j=12`.

## 7. Sixth coefficient of log A_j and its exact favorable curvature

Retain the predecessor identities

`E C=0`,

`E S_2=J`,

`E S_3=0`,

`E C^2=J`,

`E[C S_2]=0`,

`E S_4=j(j-1)(4j-5)/6`,

and, by conjugation, all odd pure-content expectations needed here vanish, including `E S_5=0` and `E C^3=0`.

Substitution into `B_6` gives

`E B_6 = -j(2j-1)(3j^4+9j^3-13j^2-4j+6)/6`.

For the cumulant correction, the retained formulas

`B_2 = const - C`,

`B_3 = const + (1-2j)C - S_2`,

`B_4 = const + (-3j^2+3j-1)C + (-3j+3/2)S_2 - S_3`

give, using the two new moments,

`Cov(B_2,B_4) = j(j-1)^2(3j+2)/2`,

`Var(B_3) = j(j-1)(12j^2-10j-1)/6`,

and `kappa_3(B_2)=0` because centered `B_2=-C` and the Plancherel content distribution is conjugation-symmetric.

At total order six, the logarithm-of-expectation cumulant formula has no other random contributions because `B_1` is deterministic. Therefore

`D_6(j) = 2 E B_6 + 4 Cov(B_2,B_4) + 2 Var(B_3) + (4/3) kappa_3(B_2)`

`= -j(6j^5+15j^4-65j^3+51j^2+13j-19)/3`.

Now compute its Chen second difference:

`2D_6(j)-D_6(j-1)-D_6(j+1)`

`= (4/3)(45j^4+75j^3-150j^2+114j-23)`.

This is strictly positive for every `j>=1`: at `j=1` the parenthesis is `61`; for `j>=2`, `45j^4-150j^2=15j^2(3j^2-10)>0`, while `75j^3+114j-23>0`.

Thus the falsification-first test did **not** find a sign obstruction at sixth order; the exact curvature remains favorable.

## 8. The seven-eighths growing-defect theorem

The predecessor established an analytic disk that does not depend on truncating after order five: for

`r=1/(6j)`

and `|t|<=r`, one has `|F_mu(t)|<=1/2`, hence `|A_j(t)-1|<2/3`, so `G_j(t)=log A_j(t)` is analytic there and `|G_j(t)|<2`.

Cauchy's estimate therefore gives `|D_m(j)|<=2r^{-m}`. If `n>=12j`, then `t/r<=1/2` and the tail after the sixth coefficient obeys

`|epsilon_j(n)| <= 2 sum_{m>=7}(t/r)^m`

`<= 4(6j/n)^7`

`< 2^21 j^7/n^7`.

Consequently its discrete Chen second difference is bounded by

`|2epsilon_j-epsilon_{j-1}-epsilon_{j+1}|`

`< 2^23 (j+1)^7/n^7`.

All retained deterministic curvatures at orders two through five are nonnegative, and the new sixth-order curvature is strictly positive. Returning to the exact Chen ratio

`Q_j(n)=F_j(n)^2/(F_{j-1}(n)F_{j+1}(n))`,

we may discard those favorable deterministic terms and keep only the factorial-ratio contribution and the analytic tail:

`log Q_j(n) >= log((j+1)/j) - 2^23 (j+1)^7/n^7`.

Since `log((j+1)/j)>=1/(j+1)`, the condition

`n^7 >= 2^24 (j+1)^8`

implies

`log Q_j(n) >= 1/(2(j+1)) > 0`.

For the genuinely new sector `j>=67`, this same condition is more than strong enough to imply the analytic prerequisite `n>=12(j+1)`. The retained complete fixed-defect theorem handles `j<=66` for every source-valid `n`.

Therefore:

**Claim `NM13-07-P0282-SEVEN-EIGHTHS-WINDOW-06`.** In the genuinely new `j>=67` range,

`n^7 >= 2^24 (j+1)^8`

implies

`F_j(n)^2 > F_{j-1}(n)F_{j+1}(n)`.

Equivalently, combining with the retained `j<=66` theorem, Chen is proved throughout the long-LIS boundary window

`j+1 <= n^(7/8)/8`.

This improves the rigorous growing-defect exponent from **6/7 to 7/8**. It remains a PARTIAL result because it does not reach the central `j=Theta(n)` regime.

## 9. Exact self-check for the sixth-order theorem

The idea was archived before the production checker at

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_seven_eighths_window_idea.md`

(commit `9d60e76191436a4ffe6d12f515666692a4fda570`).

The exact-rational checker is

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_seven_eighths_selfcheck.py`

(commit `3bd25454e5accece572098c8e0f486c2224d8269`), with archived output

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_seven_eighths_selfcheck.out`

(commit `27b6a90cc63f6750dd65a7d125edb87ceac8a57a`).

The exact computation verifies for every partition of every `j=1,...,12`:

- Plancherel mass `sum (f^mu)^2=j!`;
- `E[S_2^2]=j(j-1)(3j^2+j-8)/12`;
- `E[C S_3]=j(j-1)(2j-3)/2`;
- the complete partitionwise `B_6` formula;
- every coefficient of `log A_j` through `n^-6`;
- the exact `D_6` discrete-curvature identity;
- positive source Chen margins at the theorem thresholds.

The seven-eighths threshold sequence for `j=1,...,12` is

`24,38,53,68,84,100,116,133,150,167,185,202`,

versus the predecessor's six-sevenths thresholds

`26,41,58,74,92,110,128,147,167,186,206,226`.

The archived output ends `ALL_EXACT_CHECKS_PASS`. I also freshly re-executed the exact-rational identities and threshold-margin calculation locally during this invocation and obtained the same values. This is a **self-check**, not either required outside audit.

## 10. Frozen metric movement: exact row 96

The retained all-`n` fixed-defect theorem `j<=66` covers row 96 for

`k>=96-66=30`.

Thus the only newly uncertified source cells are `k=2,...,29`, 28 inequalities. The archived Gessel Bessel/Toeplitz row-96 checker is

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_row96_gessel_low.cpp`

with output

`proofnet24/NM13-07/artifacts/2026-09-19/p0282_row96_gessel_low.out`.

It uses 17 independently checked prime moduli. The CRT modulus has 509 bits, while `96!` has 499 bits, so the reconstructed counting integers are unique in the required range. The exact `u_2(96)=Catalan_96` identity passes. All **28/28** new low-seam inequalities are strictly positive.

The weakest newly computed low-seam ratio occurs at `k=29`:

`ell_{96,29}^2/(ell_{96,28} ell_{96,30})`

`~= 1.10738107403817665 > 1`.

The archived checker records the exact numerator, denominator, positive margin, and `ell_{96,30}`, and terminates `ALL_EXACT_CHECKS_PASS`.

Chaining `k=2,...,29` to the retained all-`n` theorem for `k>=30` verifies every interior Chen inequality in row 96. Therefore the frozen metric moves honestly:

`N_exact: 95 -> 96`.

No zero baseline was invented and no theorem frontier was substituted for this metric.

## 11. Section-B methods actually used and outcomes

Because all 30 numbered methods had already genuinely been used on P0282, every method here is marked RECYCLED. The run nevertheless changed routes and did not repeat the predecessor's `#5/#21/#4` triple.

1. **#18 SAY IT IN ANOTHER LANGUAGE — RECYCLED.** Recast the Plancherel correction as density of Viennot shadow sets inside the matching complex. Outcome: exact ratio factorization and a stronger shadow-density target.

2. **#19 MAKE IT AN ALGORITHM — RECYCLED.** Express `rho_{r+1}/rho_r` as an average normalized one-rook extension probability. Outcome: a concrete local mechanism to interrogate instead of another coefficient lemma.

3. **#20 FIND WHY THE ALGORITHM FAILS — RECYCLED.** Exact enumeration falsified pointwise extension-probability monotonicity first at `n=5`, rank 1, with `7/16 < 4/9`. Outcome: killed an overstrong local route, then redirected to an averaged exact density theorem, which succeeded through defects 27-32 and moved the ULC frontier `26->32`.

4. **#2 ATTACK THE NEGATION FIRST — RECYCLED.** Before claiming another asymptotic exponent, explicitly looked for a sign failure in the sixth Taylor coefficient's Chen curvature. Outcome: no failure; the exact curvature polynomial is strictly positive.

5. **#25 COUNT THE SAME THING TWICE — RECYCLED.** Computed the two new Plancherel moments both as content expectations and as identity/class coefficients in the regular representation using Jucys-Murphy elements. Outcome: exact formulas for `E[S_2^2]` and `E[C S_3]`.

6. **#7 TAKE THE LIMIT — RECYCLED.** Used the favorable sixth coefficient plus the retained analytic disk to convert one more controlled Taylor order into a larger growing-defect regime. Outcome: rigorous exponent improvement `6/7 -> 7/8`.

The research effort was idea-first; production checking followed only after the routes produced precise claims worth checking.

## 12. Literature and prior-art refresh — dated 2026-09-19

Fresh bounded searches used combinations of the exact Chen fixed-size statement, longest-increasing-subsequence log-concavity, Rhoades/Viennot shadows, Kauers-Wang long-LIS recurrences, Baslingker-Krishnapur-Madiman Plancherel log-concavity, and Jucys-Murphy/content-moment terminology.

Recovered primary/currently relevant items:

- William Y. C. Chen, 2008, *Log-concavity and q-Log-convexity Conjectures on the Longest Increasing Subsequences of Permutations*: original fixed-size conjecture.
- Bóna-Lackner-Sagan, *Longest increasing subsequences and log concavity*: explicitly restates Chen's fixed-size conjecture and proves related restricted statements.
- Gao-Xie-Yang, *Schur positivity and log-concavity related to longest increasing subsequences*: restricted Schur-positive progress, not the full fixed-size conjecture.
- Novak-Rhoades, *Increasing Subsequences and Kronecker Coefficients*: proposes a stronger Kronecker-coefficient conjecture implying Chen.
- Brendon Rhoades, *Increasing subsequences, matrix loci and Viennot shadows*, Forum of Mathematics, Sigma 12 (2024), e97: gives the quotient/Hilbert-series and Viennot-shadow standard-monomial model used in the density translation here.
- Baslingker-Krishnapur-Madiman, arXiv:2412.15116 / later 2026 version: proves the **Poissonized** Plancherel top-row result and describes it as the first known positive result toward Chen, not a fixed-size resolution.
- Manuel Kauers and Chen Wang, arXiv:2609.02220, submitted **2026-09-02**, *Recurrences for permutations with long increasing subsequences*: proves bivariate recurrences and D-finiteness consequences in a long-LIS range, not fixed-size log-concavity.

A fresh MathDB page also still labels Chen's conjecture open. No source-matching fixed-size resolution, no published all-`n` shadow-density theorem through defect 32, and no published `n^(7/8)` defect-window theorem surfaced in this bounded search. That is **negative evidence only**, not proof of worldwide openness or novelty. The Jucys-Murphy / regular-trace mechanism and content-moment technology are classical; I do not claim novelty for those ingredients. Novelty/priority of the exact combinations and resulting restricted theorems remains **UNVERIFIED**.

Access/scope limit: this was a bounded web/arXiv/publisher search, not exhaustive citation-graph access to every paywalled or unpublished manuscript.

## 13. Status, audits, and closure discipline

Source verdict: **OPEN**.  
Worker verdict: **PARTIAL**.

New theorem-sized partial claims this run:

- `NM13-07-P0282-SHADOW-DENSITY-32-01`: strict normalized shadow-density log-concavity for every source-valid `n` at defects `27<=j<=32`; consequence: all-`n` ULC frontier `26->32`.
- `NM13-07-P0282-SEVEN-EIGHTHS-WINDOW-06`: strict Chen inequality in the genuinely new long-LIS sector whenever `n^7 >= 2^24(j+1)^8`, equivalently `j+1 <= n^(7/8)/8`, combined with retained `j<=66` coverage.

Finite movement:

- `N_exact: 95 -> 96`.

Neither theorem closes Chen's all-`n`, all-`k` statement. No paper folder is created because closure requirements are not met. P26 and NM13-08 are not presumed to pass and no audit request is counted as progress.

## 14. Stuck / rotation counters

Frozen metric moved this run, so:

- `unchanged_runs: 0 -> 0`;
- `stuck_recoveries: 0 -> 0`.

The six-unchanged-run closable rotation rule is not triggered.

## 15. Next step

The next primary route should **not** be another routine row census and should not merely repeat seventh-order asymptotics mechanically.

First choice: exploit the shadow-density formulation at the averaged level. The pointwise extension monotonicity is false by only `1/144` in the first counterexample, while averaged density log-concavity is now proved through defect 32. Seek a covariance / negative-regression / injection statement for the distribution of `e(S)` that is strong enough to imply monotonicity of the rank-average without requiring pointwise monotonicity.

Second choice: if that route stalls, compute the seventh logarithmic coefficient only far enough to identify the first genuinely new mixed Plancherel moment and test its **curvature sign before any theorem claim**. If the coefficient remains favorable and the analytic tail can be controlled without explosive constants, test an `n^(8/9)` window; if an adverse term appears, record it as the obstruction instead of forcing another exponent lift.

Routine finite rows remain secondary because the current exact seam machinery already makes them inexpensive and they are no longer the research bottleneck.

## 16. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-07
  source_id: aim_kpz_followup_2025
  claim_id: P0282
  canonical_dedup_key: chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis
  source_status: OPEN
  worker_status: PARTIAL
  metric:
    name: N_exact
    before: 95
    after: 96
    movement: true
  theorem_frontiers:
    chen_fixed_defect_all_n:
      before: 66
      after: 66
    ulc_fixed_defect_all_n:
      before: 26
      after: 32
    growing_defect_exponent:
      before: 6/7
      after: 7/8
      condition: n^7 >= 2^24*(j+1)^8
  claims_this_run:
    - NM13-07-P0282-SHADOW-DENSITY-32-01
    - NM13-07-P0282-SEVEN-EIGHTHS-WINDOW-06
  methods_actual:
    - 18
    - 19
    - 20
    - 2
    - 25
    - 7
  methods_note: all RECYCLED because all 30 were already used; predecessor triple was 5/21/4
  unchanged_runs:
    before: 0
    after: 0
  stuck_recoveries:
    before: 0
    after: 0
  audits:
    P26: NOT_PASSED
    NM13-08: NOT_PASSED
  closure: false
  next_step: averaged shadow-extension covariance route; fallback seventh-order sign test
```

## 17. Safeguards / writes

Own-namespace substantive artifacts used or created in the unreconciled delta and this invocation:

- `p0282_shadow_density_extension_idea.md`;
- `p0282_shadow_extension_falsifier.py/.out`;
- `p0282_shadow_density_newton_j27_32.py/.out`;
- `p0282_shadow_density_boundary_j32.cpp/.out`;
- `p0282_seven_eighths_window_idea.md`;
- `p0282_seven_eighths_selfcheck.py/.out`;
- `p0282_row96_gessel_low.cpp/.out`.

No shared root, canonical claim, peer namespace, workflow, permission, public surface, email/Gmail, Drive, paid compute, or schedule was modified by this report operation. This file is the single immutable `runs/` report for the invocation. It must be read back at its returned creation commit; no receipt-only follow-up commit is authorized.
