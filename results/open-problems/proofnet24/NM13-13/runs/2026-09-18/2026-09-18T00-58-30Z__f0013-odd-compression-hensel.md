Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `N_exact_irred` stayed `6 -> 6`. Section-B methods actually tried: #5, #15, #29.**

# NM13-13 — F0013 odd-order compression/Hensel irreducibility route

Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-13`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `F0013` / `operations/claims/F0013.md`  
Canonical dedup key: `vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)`  
Source status after this run: **OPEN**  
Local status after this run: **PARTIAL**

## 1. Runtime, continuity, ownership, and controls

The requested `GPT-6 / maximum` setting is not a binding runtime setting in the exposed task-control surface. The model exposed to this invocation is **GPT-5.6 Sol** and authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. The available task-control schema exposes title/prompt, schedule or relative start, timing mode, and enabled state; it exposes no model-family or reasoning-effort selector. Making `GPT-6 / maximum` binding would require an authorized product/scheduler/API surface that actually exposes those fields. I did not create, edit, disable, or duplicate any schedule.

Repository policy records a historical `You cannot modify this task` result for P26 in one authorization context and a later successful P26 update from another authorized context. Therefore a future denial is an authorization/context boundary, not permission to bypass controls. The valid workaround is the owning account/workspace or another authorized product/admin surface.

This run continues the already-admitted **F0013** source. It does not reopen intake, create a new claim, or alter shard identity. The create-only claim `operations/claims/F0013.md` remains exclusively owned by NM13-13; the canonical key has SHA-256 residue `12 mod 13`. No release, handoff, retirement, posted closure, competing owner, or completed source audit was recovered.

Before new mathematics I reread or targeted-search-recovered the current controlling and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/F0013.md`;
- the F-series intake/canonicalization material and historical attempt `F0013-A001`;
- all prior NM13-13 reports, newest first, especially `proofnet24/NM13-13/runs/2026-09-18/2026-09-18T00-04-24Z__f0013-even-krylov-eisenstein.md`;
- the newest neighboring NM13-12 report, `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T00-52-07Z__p0483-span-regeneration-transfer.md`;
- the newest visible report of designated eventual second-audit partner NM13-01, `proofnet24/NM13-01/runs/2026-09-18/2026-09-18T00-01-39Z__p0292-stuck-recovery-1.md`;
- current repository searches for F0013 ownership, aliases, assignments, handoffs, attempts, posted status, and source corrections.

The historical attempt `F0013-A001` remains controlling continuity for the ERH/Chebotarev bottleneck: it already observed that full modular factorisation statistics across enough primes are much harder than determinant/cokernel information. I do not refile that observation as new work.

### Method-history correction

The preceding report nominated `#5/#15/#30` for this run. After recovering the complete method history, `#30` was found to have already been genuinely used in the order-five run. The owner rule asks for methods not previously tried on this problem, so I did **not** reuse #30. The actual new triple is therefore **#5, #15, #29**. Earlier F0013 triples were `#2/#14/#16`, `#18/#25/#30`, `#3/#20/#21`, and `#4/#11/#24`.

## 2. Exact source and bounded literature check — 2026-09-18 UTC

The exact source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / Probability Surveys 18 (2021), Section 11, Conjecture 11.1:

> for an `n x n` matrix with iid Rademacher entries, the characteristic polynomial is irreducible over `Q` with probability `1-o(1)`.

Fresh bounded searches on 2026-09-18 used combinations of:

- `Van Vu Conjecture 11.1 irreducibility Rademacher characteristic polynomial 2026`;
- `Rademacher random matrix characteristic polynomial irreducible unconditional 2025 2026`;
- `random sign matrix characteristic polynomial Hensel irreducible`;
- `Rademacher characteristic polynomial mod 2 irreducible factor degree n-1 Hensel root`;
- `integer eigenvalue random Bernoulli matrix characteristic polynomial irreducible`;
- `u^T adj random matrix characteristic polynomial F2 compression`.

The directly relevant current literature recovered remains:

1. **Sean Eberhard, *The Characteristic Polynomial of a Random Matrix*, Combinatorica 42 (2022), 491–527, arXiv:2008.01223.** For iid `+-1` entries, high-probability irreducibility is proved **conditionally on ERH**.
2. **Asaf Ferber, Vishesh Jain, Ashwin Sah, Mehtaab Sawhney, *Random symmetric matrices: rank distribution and irreducibility of the characteristic polynomial*, arXiv:2106.04049.** This is the symmetric ensemble and is also conditional on ERH.
3. **Lior Bary-Soroker, Daniele Garzoni, Sasha Sodin, *Irreducibility of the characteristic polynomials of random tridiagonal matrices*, J. Number Theory 280 (2026), 973–998, arXiv:2502.17218.** This is a different tridiagonal ensemble and is conditional on suitable Riemann hypotheses.
4. **Theresa C. Anderson, Evan M. O'Dorney, *Galois groups of random integer matrices*, published online 12 August 2026, DOI 10.1017/S0305004126102126.** This treats fixed matrix dimension with entry-height box `T -> infinity`, not the fixed-entry Rademacher `n -> infinity` source regime.

No unconditional source-matching resolution and no paper stating the odd-order compression/Hensel mechanism below was recovered in this bounded search. This is **bounded negative evidence only**; it is not a proof of worldwide openness or publication novelty. The determinant lemma, Gauss's lemma, finite-field conjugacy counting, Hensel lifting, and 2-adic implicit-function ideas used below are classical/folklore ingredients. Publication novelty of their particular synthesis here is **UNVERIFIED**.

## 3. Frozen metric — no movement

The frozen metric remains exactly the admission metric:

`N_exact_irred` = largest order `n` for which NM13-13 has an exhaustive exact certification covering **all** `2^(n^2)` Rademacher matrices, with exact rational factor-degree distribution and irreducibility probability.

Before this run: **6**.  
After this run: **6**.  
Movement: **none**.

The order-six signed-permutation atlas remains the last exhaustive all-matrix census. This run proves an analytic theorem for a polynomial-density odd-order subfamily and therefore does **not** rename that subfamily probability as the metric.

This is the **second consecutive unchanged run** since the order-six metric movement:

`unchanged_runs = 2`,  
`stuck_recoveries_used = 0`.

If the next run again leaves `N_exact_irred` unchanged, that run reaches the three-unchanged threshold; the following invocation must use the owner's Section-I stuck-recovery protocol.

---

# 4. New odd-order route

Let `n>=3` be odd. For a Rademacher matrix `A`, write uniquely

`A = J - 2B`,

where `J=uu^T` is the all-ones matrix, `u=(1,...,1)^T`, and `B` is a binary `0/1` matrix. For uniform `A`, `B` is uniform over all binary matrices.

Define

`f_B(y) = det(yI+B)`,

`g_B(y) = u^T adj(yI+B) u`,

`F_B(y) = 2 f_B(y) - g_B(y)`.

The rank-one determinant identity gives

`chi_A(2y) = det(2(yI+B)-uu^T) = 2^(n-1) F_B(y)`.              (4.1)

The even-order run used the special event `g_B=1 mod 2`. Odd order has a completely different geometry because

`u^T u = n = 1  (mod 2)`.

Thus over `F_2`, if

`H := u^perp`,

then

`F_2^n = <u> direct_sum H`.                                        (4.2)

This direct sum is the symmetry-breaking input of method #15.

Define the canonical projection onto `H` along `<u>` by

`pi_H(v) := v + (u^T v)u`,                                        (4.3)

and define the compressed binary operator

`D_B := pi_H B|_H : H -> H`.                                      (4.4)

Put `d=n-1`.

# 5. Theorem F0013-ODD-COMPRESSION-HENSEL-05

### Theorem

Let `n>=3` be odd and let `A` be an `n x n` Rademacher matrix. Define `B`, `u`, `H`, `D_B` as above, and let

`h_B(y) := det(y I_H + D_B) in F_2[y]`.

Assume `h_B` is irreducible over `F_2` (necessarily of degree `d=n-1`). Then:

1. **Exact mod-2 compression identity.**

   `F_B(y) = h_B(y)  (mod 2)`.                                    (5.1)

2. **All rational reducibility collapses to one linear obstruction.**

   `chi_A` is reducible over `Q` **if and only if** `A` has an odd integer eigenvalue. Equivalently, every rational factorisation of `chi_A` on this event has degree pattern `1+(n-1)`.

3. **The compression event has exact polynomial density.** If `A` is iid Rademacher and

   `G_n := {h_B is irreducible over F_2}`,                          (5.2)

   then

   `P(G_n)
    = [I_2(d)/2^d] product_(j=1)^(d-1) (1-2^(-j)),`               (5.3)

   where

   `I_2(d) = (1/d) sum_(r|d) mu(r) 2^(d/r)`                        (5.4)

   is the number of monic irreducible degree-`d` polynomials over `F_2`. Hence

   `P(G_n) ~ C_2/(n-1)`,                                           (5.5)

   with

   `C_2 = product_(j>=1)(1-2^(-j)) > 0`.

4. **A single 2-adic root controls the obstruction.** The polynomial `chi_A` has a unique root

   `rho_A in Z_2`, `rho_A = 1 (mod 2)`.                            (5.6)

   On `G_n`, `chi_A` is reducible over `Q` if and only if this 2-adic root is an ordinary odd integer. Any such integer lies in `[-n,n]`.

   Consequently, choose any `k` with `2^k>2n` and compute the unique lifted residue

   `r_k = rho_A (mod 2^k)`.                                        (5.7)

   There is at most one odd integer `m in [-n,n]` congruent to `r_k mod 2^k`. If there is no such `m`, `chi_A` is irreducible. If there is such an `m`, the **single exact evaluation** `chi_A(m)` decides the question: zero means reducible; nonzero means irreducible.

Thus on an explicit event of order `1/n` probability, the full rational factorisation problem collapses to one finite integer-eigenvalue check.

## 6. Proof of the theorem

### Step 1 — identify the adjugate numerator with a codimension-one compression

Work over `F_2`. Choose any basis of `H` and form a basis of `F_2^n` whose first vector is `u` and whose remaining vectors are that basis of `H`. Let `S` be the corresponding change-of-basis matrix.

Because `u^T u=1` and `u^T H=0`,

`u^T S = e_1^T`,  `S^(-1)u=e_1`.                                  (6.1)

In this basis, write

`S^(-1) B S = [[a, r^T], [c, D]]`,                                (6.2)

where `D` is the matrix of `D_B` on `H`. Therefore

`S^(-1)(yI+B)S = [[y+a, r^T], [c, yI+D]]`.                         (6.3)

Adjugation respects similarity, so

`g_B(y)
 = u^T adj(yI+B)u
 = e_1^T adj(S^(-1)(yI+B)S)e_1
 = det(yI+D)`.                                                      (6.4)

Since `F_B=2f_B-g_B`, reduction modulo `2` gives

`F_B(y) = g_B(y) = det(yI+D) = h_B(y)  (mod 2)`.                  (6.5)

This proves (5.1).

### Step 2 — an irreducible degree-`n-1` reduction forces every rational factorisation to be linear times degree `n-1`

Assume `h_B` is irreducible of degree `n-1`. The integer polynomial `F_B` has degree `n`, leading coefficient exactly `2`, and is primitive because its reduction modulo `2` is the nonzero polynomial `h_B`.

Suppose `F_B` is reducible over `Q`. By Gauss's lemma write

`F_B = P Q`                                                        (6.6)

with nonconstant primitive `P,Q in Z[y]`. Their leading coefficients multiply to `2`; after signs are absorbed, one has odd leading coefficient `1` and the other even leading coefficient `2`.

Reduce (6.6) modulo `2`. Neither factor can reduce to the zero polynomial because each is primitive. The factor with odd leading coefficient keeps its full positive degree after reduction. Since

`bar P bar Q = h_B`                                                (6.7)

and `h_B` is irreducible, the odd-leading factor must reduce to `h_B` and therefore has degree at least `n-1`. Because the other factor is nonconstant and total degree is `n`, the degrees are exactly

`n-1` and `1`.                                                      (6.8)

Moreover the linear factor is the even-leading one. Being primitive and nonzero modulo `2`, it has odd constant term, so up to sign it is

`2y-m` with `m` odd.                                                (6.9)

Hence `F_B(m/2)=0`; by (4.1),

`chi_A(m)=0`.                                                       (6.10)

Thus reducibility implies an odd integer eigenvalue.

Conversely, if `chi_A(m)=0` for odd integer `m`, then (4.1) gives `F_B(m/2)=0`. The rational root `m/2` is in lowest terms, so `2y-m` is a nontrivial factor of `F_B` over `Q`; equivalently `chi_A` is reducible. This proves assertion 2.

### Step 3 — exact probability of the compression event

The map

`B -> S^(-1) B S`                                                  (6.11)

is a linear bijection on all `n x n` matrices over `F_2`. Therefore, for uniform binary `B`, the block `D` in (6.2) is a uniform `d x d` binary matrix, independent of the other `2n-1` block coordinates.

For each monic irreducible polynomial `q` of degree `d`, every matrix with characteristic polynomial `q` is conjugate to the companion matrix of `q`; its centralizer in `GL_d(F_2)` is `F_(2^d)^*`, of size `2^d-1`. Hence the number of `D` with characteristic polynomial equal to one fixed irreducible `q` is

`|GL_d(F_2)|/(2^d-1)`.                                             (6.12)

There are `I_2(d)` monic irreducible degree-`d` polynomials. Dividing by all `2^(d^2)` binary matrices,

`P(G_n)
 = I_2(d) |GL_d(F_2)| / [(2^d-1) 2^(d^2)]`.                       (6.13)

Using

`|GL_d(F_2)|/2^(d^2) = product_(j=1)^d (1-2^(-j))`                 (6.14)

and `2^d-1=2^d(1-2^(-d))` gives exactly (5.3). The standard Möbius formula gives (5.4), and

`I_2(d)/2^d = 1/d + O(2^(-d/2)/d)`                                (6.15)

while the finite product tends to `C_2`, proving (5.5).

### Step 4 — the unique odd 2-adic root

Since every sign is `1 mod 2`,

`A = J  (mod 2)`.                                                   (6.16)

The characteristic polynomial of `J` is

`x^(n-1)(x-n)`,                                                     (6.17)

so for odd `n`,

`chi_A(x) = x^(n-1)(x+1)  (mod 2)`.                               (6.18)

The root `x=1` is simple modulo `2`: differentiating the right side and evaluating at `1` gives `1`. Hensel's lemma therefore gives a unique

`rho_A in Z_2`, `rho_A=1 mod 2`, `chi_A(rho_A)=0`.                 (6.19)

Every odd integer root of `chi_A` is congruent to `1 mod 2`, hence by Hensel uniqueness it must equal `rho_A` in `Z_2`. Conversely, if `rho_A` is an ordinary integer then it is an odd integer eigenvalue. By Step 2, on `G_n` this is exactly the rational reducibility obstruction.

Finally every eigenvalue of `A` has absolute value at most the matrix infinity norm

`||A||_infinity = n`,                                               (6.20)

so an integer eigenvalue lies in `[-n,n]`. If `2^k>2n`, two distinct integers in that interval cannot be congruent modulo `2^k`. Therefore the lifted residue `r_k` identifies at most one possible ordinary integer root; one exact evaluation at that candidate decides whether the 2-adic root actually terminates at an integer. This proves assertion 4 and the theorem. `QED`

---

# 7. Method #15 — BREAK THE SYMMETRY ON PURPOSE

The preceding run's even-order proof exploited `u in u^perp`. This run deliberately moved to the opposite parity, where `u^T u=1` and the space splits canonically as `<u> direct_sum u^perp`.

That symmetry break is exactly what exposes the random `(n-1) x (n-1)` compression `D_B`. The adjugate numerator is not an opaque degree-`n-1` polynomial: modulo two it is literally the characteristic polynomial of a uniform smaller random matrix. This produces the exact `~C_2/(n-1)` density and the factorisation collapse theorem above.

**Outcome of #15: success.** It gives a qualitatively different odd-order route and a polynomial-density source-relevant slice.

# 8. Method #29 — ADD THE POINTS AT INFINITY

The exceptional linear factor left by the mod-2 compression argument is exactly the place where ordinary integer reasoning is too coarse. Passing from `Z` to its 2-adic completion `Z_2` closes that boundary: every odd-order sign matrix has one and only one 2-adic root above the simple mod-2 root `1`.

On `G_n`, every possible rational factorisation is encoded by the question

`is rho_A actually an ordinary integer?`                            (8.1)

Because an ordinary integer eigenvalue must lie in a finite interval, a finite Hensel lift plus at most one exact determinant evaluation decides that question.

**Outcome of #29: success.** The missing boundary point becomes a unique 2-adic branch rather than an uncontrolled factorisation tree.

# 9. Method #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

To understand whether the 2-adic root can be made probabilistic, I introduced an odd 2-adic rank-one parameter

`A_s := sJ - 2B`, `s in Z_2^*`,                                    (9.1)

and

`P_B(x,s) := det(xI-A_s)
           = det(xI+2B) - s u^T adj(xI+2B)u`.                      (9.2)

For every odd `x`, the denominator

`K_B(x):=u^T adj(xI+2B)u`                                          (9.3)

is odd, because modulo `2` we have `xI+2B=I` and `u^T u=n=1`. Thus the zero set can be written exactly as the 2-adic graph

`s = Phi_B(x)
   := det(xI+2B) / K_B(x)`.                                        (9.4)

Modulo two,

`Phi_B(x) = x^n / (n x^(n-1)) = x`,                               (9.5)

so differentiating gives

`Phi_B'(x)=1 (mod 2)`                                               (9.6)

throughout the odd branch. Hence the 2-adic root moves with unit derivative under this deformation; locally the root parameter and the rank-one parameter are invertible coordinates.

This does **not** yet give a source probability estimate, because the Rademacher ensemble is the single slice `s=1`; averaging over odd `s` would change the ensemble. The route therefore identifies the right 2-adic coordinate but also pinpoints why the easy deformation does not close the asymptotic conjecture.

**Outcome of #5: partial success / precise obstruction.** The odd root is nondegenerate under rank-one deformation, but a source-valid way to randomize or anti-concentrate that coordinate at fixed `s=1` is still missing.

---

## 10. Why this is source-relevant but not source closure

The prior even-order theorem certified an explicit family of density `Theta(2^(-n))`. The odd-order theorem here finds a much larger event of density

`Theta(1/n)`                                                        (10.1)

on which **all** possible rational reducibility collapses to one scalar obstruction: the unique odd 2-adic root being an ordinary bounded integer.

That is real quantitative leverage, but it is not the source statement. It does not show that `G_n` has probability tending to one (it does not), and it does not yet bound the integer-root obstruction strongly enough to turn `Theta(1/n)` into a high-probability result. The source therefore remains **OPEN** and NM13-13 remains **PARTIAL**.

No P26 or NM13-01 audit is requested or counted. No self-check is labeled an independent audit. No finite exhaustive claim was introduced in this run, so I did not manufacture a checker artifact; the new result is theorem-sized and its full argument is written above.

## 11. Next research step

The next run must not repeat any previous method number. The most promising still-untried triple is **#6 / #17 / #26**:

- **#6 deform to a point you can solve:** deform the fixed source slice inside the 2-adic root coordinate while preserving an exact source-valid involution if possible;
- **#17 look for your numbers somewhere else:** compare the `~C_2/(n-1)` compression density with finite-field cyclic-matrix / control-theory formulas and look for an existing anti-concentration theorem for the distinguished Hensel root;
- **#26 hunt the sporadic case:** classify exactly what an odd integer eigenvalue forces inside the irreducible-compression event, starting with exceptional eigenvalues `+-1` rather than treating all `|m|<=n` uniformly.

The decisive missing statement is now very concrete: obtain a source-valid upper bound on

`P(G_n and rho_A in Z)`                                             (11.1)

that is `o(P(G_n))`, or better, find a second large mod-prime slice whose union/combination drives the certified irreducibility probability upward. If that fails and the frozen metric remains unchanged for a third consecutive run, the subsequent invocation must enter the formal hard-target stuck-recovery protocol.

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-13
  category: HARD_OUTSIDE
  source_id: F0013
  claim_path: operations/claims/F0013.md
  canonical_dedup_key: vu_combinatorial_rmt_2020::conjecture_11.1_(irreducibility)
  source_status: OPEN
  track_status: PARTIAL
  metric:
    name: N_exact_irred
    before: 6
    after: 6
    movement: none
  theorem_this_run: F0013-ODD-COMPRESSION-HENSEL-05
  theorem_scope: >-
    For odd n>=3, on the exact event that the canonical (n-1)-dimensional
    F_2 compression has irreducible characteristic polynomial, rational
    reducibility of chi_A is equivalent to one odd integer eigenvalue;
    the event has exact probability [I_2(n-1)/2^(n-1)] times the finite
    GL-product and is asymptotic to C_2/(n-1). The remaining obstruction
    is the unique Hensel lift of x=1 mod 2 and can be decided after finite
    lifting by at most one exact integer evaluation.
  methods_tried:
    - 5
    - 15
    - 29
  method_outcomes:
    5: 2-adic rank-one deformation gives a unit-derivative root coordinate; fixed source slice blocks direct averaging
    15: odd parity splits <u> from u-perp and exposes a uniform (n-1)-dimensional compression
    29: Hensel completion turns the exceptional linear factor into one unique 2-adic root
  unchanged_runs: 2
  stuck_recoveries_used: 0
  audits_counted:
    p26: false
    nm13_01: false
  literature_check_date: 2026-09-18
  literature_outcome: >-
    Bounded search recovered Vu source, Eberhard conditional-ERH full-matrix
    theorem, Ferber-Jain-Sah-Sawhney conditional-ERH symmetric theorem,
    Bary-Soroker-Garzoni-Sodin conditional tridiagonal result, and
    Anderson-O'Dorney fixed-dimension growing-height result; no unconditional
    source-matching resolution or exact compression/Hensel theorem recovered.
    Worldwide openness and publication novelty remain unverified.
  next_methods:
    - 6
    - 17
    - 26
  next_step: >-
    Seek source-valid anti-concentration of the distinguished odd Hensel root
    inside the irreducible-compression event, beginning with exact structural
    consequences of eigenvalues +1 and -1.
```
