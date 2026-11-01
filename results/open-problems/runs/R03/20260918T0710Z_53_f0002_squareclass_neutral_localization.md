Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated GPT-6 selector, reasoning-effort selector, guaranteed-duration field, or applied-run attestation, so I do not claim otherwise. F0002 NO MOVEMENT: `gamma_sym = POSITIVE_UNMEASURED -> POSITIVE_UNMEASURED`; inherited stagnation count remains `UNKNOWN`; methods #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS, #26 HUNT THE SPORADIC CASE.**

# R03 HARD OUTSIDE — F0002: determinant square classes, an exponential pointwise obstruction, and a larger affine-support sieve

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source, current literature, and ownership

I continued the canonical R03 assignment **F0002**, not the stale native-title F0001 target. `operations/claims/F0002.md` assigns F0002 exclusively to R03 and preserves the mandatory third-stuck handoffs of F0001 and F0097. Reopening the nonsymmetric sharp-prefactor problem would violate the owner continuity rule.

Before new mathematics I reread/recovered the required campaign state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the canonical F0002 claim and F-intake history, including `F0002-A001`;
- newest own report `runs/R03/20260918T0630Z_52_f0002_affine_remainder.md`;
- the neighboring current random-matrix report `research7_2026-09-17/R7-07/runs/2026-09-18/2026-09-18T050955Z__report.md` on F0003.

The exact outside source remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797, Section 3, Conjecture 3.3. For a symmetric sign matrix `A_n` with iid uniform Rademacher entries on and above the diagonal,

`q_n^sym := P(det A_n = 0)`,

and the source target is

`q_n^sym = (1/2 + o(1))^n = 2^{-n+o(n)}.`

Fresh primary-source checks on 2026-09-18 again recovered no base-`1/2` theorem. Campos--Jenssen--Michelen--Sahasrabudhe, arXiv:2105.11384 / JAMS 38 (2025), prove `q_n^sym <= exp(-c n)` for an unspecified absolute `c>0`. Yi Han, arXiv:2506.01155 / JLMS 113 (2026), proves `exp(-c'kn)` large-deviation control for corank `k <= c sqrt(n)`, not the sharp singularity base. A bounded current search also recovered no later source-matching theorem. This is negative search evidence, not a novelty certificate.

The frozen metric remains

`gamma_sym = sup { gamma in [0,1] : q_n^sym <= 2^{-(gamma-o(1))n} }`.

The checked literature certifies positivity but does not expose a numerical constant in the theorem statement, so the honest value remains `POSITIVE_UNMEASURED`; target `gamma_sym=1`.

Run 52 reduced the source-rate conjecture to the typical-core transversality statistic

`T(D) = #{0 != z in {0,1}^d : z^T D^{-1}z in {0,1}, 1^T D^{-1}z != 1}`

for invertible symmetric `0/1` cores `D` (and `T(D)=0` on singular cores):

`q_n^sym = 2^{-n+o(n)}  <=>  E T(D_d) = 2^{o(d)}.`

Equivalently, with `E_m^aff` the no-zero-row affine-corank-one event from run 52 and `r_m=P(E_m^aff)`, the target is `r_m <= 2^{-m+o(m)}`.

## 2. Idea before code

The first question this run was whether `T(D)` hides an arithmetic invariant stronger than a generic inverse-quadratic Littlewood--Offord estimate. It does: every counted `z` creates a singular one-vertex child whose **complement is invertible**, and the parent and complementary-child determinants lie in the same rational square class.

The second question was whether this invariant could support a pointwise bound on `T(D)`. It cannot. There is a concrete `3 x 3` unimodular block whose direct sums have exponentially many counted Boolean vectors. This is a genuine obstruction, not a renamed coupling failure.

The third question was what survives after accepting that only a typical-core bound can work. The affine filter from run 52 excludes support one and two entirely, and a cube-hyperplane count plus Erdős--Littlewood--Offord pushes the already-negligible support range from `O(sqrt m)` to almost `(1/2)sqrt(m log_2 m)`.

Only after these three facts were obtained did I write one exact checker.

## 3. Method #12 — conserved determinant square class

Let `D` be an invertible symmetric `d x d` `0/1` matrix and let `0 != z in {0,1}^d` be counted by `T(D)`. Put

`q = z^T D^{-1}z in {0,1}`,

`ell = 1^T D^{-1}z != 1`,

and form the singular child

`C = [[D,z],[z^T,q]]`.

Since `D` is invertible, `C` has corank exactly one and a spanning null vector is

`v = (-D^{-1}z, 1)`.

Let

`E = J_{d+1} - C`.

Run 52's affine-corank criterion says `E` is invertible precisely because `1^T v = 1-ell !=0`.

### C320 — exact square-class identity

For every such pair `(D,z)`,

`det(D) det(E) = (-1)^d [ det(D) (1-ell) ]^2`.                    (C320)

In particular the absolute determinants of `D` and `E` have the same squarefree part.

#### Proof

Because `C` has corank one and its lower-right principal cofactor is `det(D)`,

`adj(C) = det(D) v v^T`.

The rank-one determinant formula remains valid at a singular matrix in adjugate form:

`det(-C + 11^T) = det(-C) + 1^T adj(-C) 1`.

Here `det(-C)=0` and, since `C` has size `d+1`,

`adj(-C)=(-1)^d adj(C)`.

Therefore

`det(E) = (-1)^d det(D) (1^T v)^2`
`       = (-1)^d det(D) (1-ell)^2`.

Multiplying by `det(D)` gives C320. Since both determinants are integers, `det(D)(1-ell)` is in fact an integer; equivalently, if `a=det D` and `u=adj(D)z`, then the square is `(a-1^T u)^2`. QED.

There is a Smith-normal-form interpretation. If `w` is a primitive integer generator of `ker C`, then `adj(C)=Delta w w^T` for an integer `Delta !=0`, hence

`det(D)=Delta w_{d+1}^2`,

`det(E)=(-1)^d Delta (sum_i w_i)^2`.

Thus the same determinantal divisor `Delta` controls the parent minor and the complementary rank-one perturbation. This is the conserved arithmetic object. I make no novelty claim for adjugate/Smith facts themselves.

A possible future route is to bound high richness by the distribution of these square classes or of the corresponding torsion invariant. However the next section shows why square class alone is insufficient.

## 4. Method #20 — why pointwise / square-class algorithms fail

Define the neutral sector

`N(D) = { z in {0,1}^d : z^T D^{-1}z = 0 and 1^T D^{-1}z = 0 }`,

`M(D)=|N(D)|`.

Every nonzero neutral vector is counted by `T(D)`. Moreover direct sums preserve neutral choices: if `z_i in N(D_i)`, then

`(z_1,z_2) in N(D_1 direct_sum D_2)`

because both the quadratic value and the affine linear value add across blocks. Hence

`M(D_1 direct_sum D_2) >= M(D_1) M(D_2)`.

Now take the explicit unimodular block

`D0 = [[1,1,1],
       [1,1,0],
       [1,0,1]].`

It has

`det(D0)=-1`,

`D0^{-1}=[[-1,1,1],[1,0,-1],[1,-1,0]]`.

Its neutral sector contains exactly

`000, 001, 010`.

Therefore for

`D_k = D0 direct_sum ... direct_sum D0`  (`k` copies, dimension `d=3k`),

choosing independently one of those three neutral vectors in every block gives `3^k` neutral vectors. All but the zero vector are counted by `T(D_k)`, so

`T(D_k) >= 3^k - 1`

`       = 2^{(log_2 3 / 3)d} - 1`.                                (C321)

Also `det(D_k)=(-1)^k`, so these exponentially rich cores live in squarefree determinant class one.

This is the precise failure mode of a pointwise strategy. The source-rate criterion `E T(D_d)=2^{o(d)}` can only be true because exponentially rich deterministic cores are themselves sufficiently rare. No deterministic estimate `T(D)<=2^{o(d)}` is possible, and a sieve using only the squarefree part of `det(D)` cannot prove the target because the richest explicit family already has trivial square class.

This substantially strengthens run 50's finite observation that pointwise rigidity fails: here the failure is an explicit exponential family in arbitrarily large dimension.

## 5. Method #26 — the sporadic small-support regime and a larger rigorous localization

Let `C_m` be a uniform symmetric `0/1` matrix and let `E_m^aff` be the run-52 event:

- `corank(C_m)=1`;
- its kernel is spanned by `v` with `1^T v !=0`;
- `C_m` has no zero row.

Write `s(v)=|supp(v)|`.

### First sporadic fact: support one and two are impossible

Support one forces a zero column and, by symmetry, a zero row, contradicting `E_m^aff`.

Suppose support is exactly `{i,j}` and `v_i=a`, `v_j=b`, with `a,b !=0` and `a+b !=0`. For every `k` outside the support,

`C_{ki} a + C_{kj} b = 0`.

Among the four binary pairs `(C_{ki},C_{kj})`, `(1,0)` would force `a=0`, `(0,1)` would force `b=0`, and `(1,1)` would force `a+b=0`. Therefore every outside pair is `(0,0)`.

For the internal `2 x 2` block, if `C_{ij}=0`, the two kernel equations force `C_{ii}=C_{jj}=0`, giving zero rows. If `C_{ij}=1`, the first kernel equation forces `C_{ii}=1` and `b=-a`, again contradicting `a+b!=0`. Hence

`E_m^aff => s(v)>=3`.                                              (C322.1)

Support three is genuinely possible (the exact checker sees it), so this is the true first sporadic scale rather than an artefact of the proof.

### C322 — cube-hyperplane sieve through almost `sqrt(m log m)` support

For `s>=3`, define

`p_s = 2^{-s} binom(s, floor(s/2)).`

Let

`r_{m,s}=P(E_m^aff and s(v)=s)`.

Then

`r_{m,s} <= binom(m,s) * s * 2^{s(s-1)} * p_s^{m-s}`.              (C322.2)

Consequently, for every fixed `epsilon in (0,1/2)` and

`L_m = floor((1/2-epsilon) sqrt(m log_2 m))`,

`P(E_m^aff and s(v)<=L_m)`

`<= 2^{-(log_2(8/3)-o(1))m}`

`= o(2^{-m}).`                                                     (C322.3)

Thus any source-scale affine remainder must be carried by kernel support larger than almost `(1/2)sqrt(m log_2 m)`. This is a strict extension of the earlier generic `O(sqrt m)` support sieve because it uses the affine-filtered problem produced in run 52.

#### Proof of C322.2

Fix a support `S` of size `s` and write the nonzero coordinates of the kernel vector as `a=(a_1,...,a_s)`, all `a_i !=0`. Every row indexed by `k notin S` must satisfy

`X_k . a = 0`,

where `X_k=(C_{ki})_{i in S}` is a uniform vector in `{0,1}^s`. The vectors `X_k`, `k notin S`, are independent because they use distinct symmetric cross-cut entries.

Let

`Z(a)={x in {0,1}^s : x.a=0}`.

The Erdős--Littlewood--Offord bound, after writing `2x_i-1` as Rademacher signs, gives

`|Z(a)| / 2^s <= p_s`

because every coefficient `a_i` is nonzero.

It remains to union over the possible cube sections `Z(a)` without unioning over uncountably many real coefficient vectors. Put `K=span_R Z(a)`. Since `K subset a^perp`, `dim K<=s-1`, and

`Z(a)=K intersect {0,1}^s`:

one inclusion is the definition of `K`, while any cube point in `K` lies in `a^perp` and hence lies in `Z(a)`. Therefore every possible zero set is determined by a subspace spanned by at most `s-1` cube vectors. The number of such spanning lists is at most

`sum_{r=0}^{s-1} (2^s)^r <= s 2^{s(s-1)}`.

For each zero set, all `m-s` independent cross rows must land in it, at probability at most `p_s^{m-s}`. Finally union over the `binom(m,s)` supports. This proves C322.2. Notice that we deliberately ignore all constraints inside `S` and outside `S`, so the result is a genuine upper bound.

#### Proof of C322.3

For every `s>=3`, `p_s<=3/8`. Fix

`eta = epsilon(1-epsilon)>0`.

For

`3<=s<=m^{1/2-eta}`,

the combinatorial prefactor in C322.2 has binary logarithm

`O(s log m + s^2)=o(m)`,

uniformly. Hence this entire range contributes at most

`2^{-(log_2(8/3)-o(1))m}`.

For

`m^{1/2-eta}<s<=L_m`,

use the elementary central-binomial estimate `p_s<=s^{-1/2}`. The binary logarithm of the right side of C322.2 is at most

`s log_2(em/s) + s^2 + O(log s) - ((m-s)/2) log_2 s`.

Since `s<=c sqrt(m log_2 m)` with `c=1/2-epsilon`, the positive quadratic term is at most

`c^2 m log_2 m = (1/4-epsilon+epsilon^2)m log_2 m`,

while `s>m^{1/2-eta}` makes the negative term at most

`-(1/4-eta/2-o(1))m log_2 m`.

Their leading difference is

`[-epsilon+epsilon^2+eta/2]m log_2 m`

`= -(epsilon(1-epsilon)/2)m log_2 m`,

so this second range is `2^{-Omega_epsilon(m log m)}`. Summing over at most `L_m` values of `s` does not alter either estimate. QED.

C322 is PARTIAL by the owner's rule: it eliminates a growing support range, not the full affine remainder.

## 6. Exact self-check written only after the ideas

Artifacts:

- `artifacts/R03/20260918T0710Z_53_f0002_squareclass_neutral_exact.py` — creation commit `46b337fe5f916808c61f2a953b5db4b6b8ed703a`;
- `artifacts/R03/20260918T0710Z_53_f0002_squareclass_neutral_exact.out` — creation commit `95da65f642c406039ff146d77acc398b5911a6c0`.

The checker uses exact `Fraction` linear algebra and integer Bareiss determinants. It exhausts every symmetric `0/1` core through `d=5`, verifies C320 for every one of the 100,836 counted transversality solutions encountered across `d<=5`, and records the finite richness distributions. It also checks the `D0` neutral sector exactly and the certified direct-sum lower bounds through four blocks. The archived output ends `EXACT_CHECK_PASS`.

The finite diagnostic is informative but not promoted to asymptotic evidence: through `d=5`, the maximum observed `T(D)` is `0,0,2,5,13`; at `d=5` the maximum by squarefree determinant class is `{1:13, 2:6, 3:4, 5:0}`. Thus the richest small cores already sit in square class one, consistent with the explicit direct-sum obstruction.

## 7. What moved and what did not

The frozen metric did **not** move:

`gamma_sym : POSITIVE_UNMEASURED -> POSITIVE_UNMEASURED`.

No numerical exponent is manufactured from the new structural results. Status remains **OPEN / PARTIAL**.

Substantive mathematical movement is instead:

1. C320: every transversality solution preserves an exact determinant square class across the singular child/complement operation;
2. C321: there is an explicit arbitrarily large unimodular family with `T(D)>=2^{0.5283... d}-1`, proving that all pointwise-richness strategies and square-class-only sieves are impossible;
3. C322: the affine remainder contributed by kernel support up to `(1/2-epsilon)sqrt(m log_2 m)` is `o(2^{-m})`, so the source-scale obstruction is forced into larger support.

The central remaining obligation is still the genuinely typical statement

`E T(D_d)=2^{o(d)}`,

or equivalently `r_m<=2^{-m+o(m)}`, now with the additional knowledge that rare block-rich cores can be exponentially bad and that all small/mesoscopic affine supports through the C322 range are negligible.

Because run 52 inherited stagnation count `UNKNOWN`, this run preserves `UNKNOWN`; it does not silently reset or increment an unknowable historical streak.

## 8. Next route

Do not repeat this run's triple. The next planned methods are **#6 DEFORM TO A POINT YOU CAN SOLVE, #14 FIND THE GROUP ACTING, #27 SWAP THE QUANTIFIERS**.

Concrete target: start from the explicit neutral-rich block family `D0^{direct_sum k}` and add random cross-block symmetric bits. Determine how quickly the neutral sector collapses. In parallel, swap quantifiers from “a random `D` has many `z`” to moments counting tuples `(D,z_1,...,z_r)` and quotient tuples by the span/group action of their Boolean solution patterns. A sufficiently strong high-moment bound for `T(D)` would directly attack the typical-core criterion while respecting C321's pointwise obstruction.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R03
  target: F0002
  source: "Vu arXiv:2005.02797, Section 3, Conjecture 3.3"
  metric: gamma_sym
  before: POSITIVE_UNMEASURED
  after: POSITIVE_UNMEASURED
  movement: NO_MOVEMENT
  inherited_stagnation_count: UNKNOWN
  status: PARTIAL
  new_claims:
    - C320 determinant-square-class identity
    - C321 explicit exponential pointwise transversality-richness family
    - C322 affine support localization through almost 0.5*sqrt(m log_2 m)
  remaining_obligation: "prove E T(D_d)=2^{o(d)} (equiv. r_m <= 2^{-m+o(m)}) for a uniform symmetric 0/1 core"
  next_methods: [6,14,27]
  closure: false
```

## 10. Model/scheduler control status

Still unchanged. The exposed scheduled-task schema provides prompt/title, schedule/timing, enablement and relative-start controls, but **no binding model-family selector and no reasoning-effort selector**. GPT-6/maximum is therefore only requested in prompt text from this surface; no authenticated completed-run telemetry verifies it. The historical P26 `You cannot modify this task` result was authorization-context dependent: another authorized context later succeeded on P26 while other contexts rejected R-series edits. The legitimate remedy is the owning/authorized task-management context or platform support, not task duplication or permission bypass. No scheduler or permission state was changed in this run.
