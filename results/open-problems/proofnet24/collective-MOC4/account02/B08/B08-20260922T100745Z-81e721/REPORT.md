# account02/B08 MOC4 report — common-block external-facet reduction

**Run:** `B08-20260922T100745Z-81e721`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Assignment:** repeated-eigenvalue and common-block boundaries only  
**Named partner:** account03/B09  
**Campaign lead:** account03/B07  
**Candidate:** `MOC4-COMMON-BLOCK-EXTERNAL-REDUCTION-v2`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Target status:** full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Fresh source-bound state

The fresh brain control read used main commit
`cbc06c37ac3e6f776bc298133c4d1be715b6d9bc`; a later control recheck used
`446baef73de0223776607d38ee0d795df9f45204`.  The active OWNER CONTROL is
revision `2026-09-22.2`, programme
`COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`.  The later README explicitly
supersedes the historical installation/benchmark clauses and assigns B08 to
MOC4 research.  No later B08 stop was found.

The latest complete lead state read from the fresh coordination archive is
account03/B07 run `20260922T095337Z-account03-B07-MOC4-r12`,
`MOC4-MSQR-ANTIPODE-BUDGET-v1`: the remaining generic positive-gap proof is
split into mixed-Schur and negative-definite branches, with an exact
determinant-specific reserve/payment still unpaid.  I also read the canonical
account03/B07 r13 full-tangent Schur-complement report because the newest
partner report names it as a dependency.

The newest complete named-partner result I could recover is account03/B09 run
`20260922T094506Z-account03-B09-MOC4-r12`,
`MOC4-B09-TWO-KNOT-CROSS-BLOSSOM-v1`.  It uses the genuine complementary-minor
cofactor to close an entire support chamber whose unique dangerous Saxl
external atom is

`tau=(2,3,0,1), rho'=(1,2,0)`.

The general external-vertex theorem used below is the same B09 Saxl-facet
result established in the earlier source-bound partner report: for the
endpoint support function `f`,

`h(U) <= max(M, max_external e_{tau,rho'}(f))`

for every true unitary `U`, where `M=max_sigma f(sigma)` and

`e_{tau,rho'}(f)=(2/3)(B_{rho(tau)}(f)+B_{rho'}(f))-(1/3)f(tau)`.

No arbitrary bistochastic or independently selected compound-minor data are
used.

A bounded current literature check also found the 2025 survey still describing
the Marcus-de Oliveira problem as open and Drury's classical n=4 paper
explicitly describing n=4 as open; no source-matching complete n=4 solution
was found in this bounded check.

## 2. Conditional end-to-end boundary reduction

Inherited B08 work already proves the exact repeated-spectrum case and every
proper common reducing block, and the opposite-scalar gauge
`(A,B)->(A+tI,B-tI)` reduces the unsolved all-pairs core to simple-spectrum,
individually invertible, irreducible pairs without changing either the target
determinant or any permutation vertex.

The remaining boundary issue is not whether a common-block point itself
satisfies MOC4; it does.  It is whether a strict counterexample can approach a
common-block boundary through a support direction whose outer Saxl relaxation
has a non-Weyl excess.  The partner theorem turns that into finitely many
external facets.

This run proves:

* for every full-support `1+3` common-block exposed face, **all 48** external
  facets are automatically paid by endpoint inequalities;
* for every full-support `2+2` common-block exposed face, **40 of 48** external
  facets are automatically paid; the only possible outer excess is confined
  to **8 cross-block-swap atoms**.

Thus the first unpaid common-block implication is reduced to an eight-atom
genuine-spinor payment problem on `2+2` faces.  The named partner's latest
dangerous atom is exactly one of these eight.

## 3. Endpoint functions lie in Saxl_4

For a real support functional `L:C->R`, put

`z_sigma = prod_i (a_i+b_{sigma(i)})`, `f(sigma)=L(z_sigma)`.

Expanding by subsets,

`z_sigma = sum_{I subset [4]} (prod_{i notin I} a_i)
            (prod_{j in sigma(I)} b_j)`.

Hence `f` lies in the real span of the subset-assignment indicators

`P_{I,J}(sigma)=1_{sigma(I)=J}`.

For n=4, the k=3 indicators are complements of k=1 indicators and k=4 is the
constant k=0 indicator, so the 53 indicators with k=0,1,2 span the full Saxl_4
endpoint-function space.  This is exactly the finite space on which the
external functionals act.

The exact checkers beside this report verify all functional identities on all
53 generators using `fractions.Fraction`; no floating arithmetic enters the
claimed certificates.  A floating LP was used only as a search heuristic to
discover sparse candidate identities and is not part of the proof.

## 4. Full-support `1+3` face: all 48 external facets are paid

Relabel a `1+3` common reducing block so that the singleton is index 0 and the
block-preserving permutation face is

`F_13={sigma in S4 : sigma(0)=0}`,

which has six permutations.

Let the 3x3 coupling block be `V`.  If every entry of `V` is nonzero, then
`P=|V|^2` has strictly positive entries.  There exists a Birkhoff
decomposition of `P` with strictly positive weight on every one of the six
permutations: subtract a sufficiently small epsilon times the sum of all six
3x3 permutation matrices, normalize the positive residual doubly stochastic
matrix, and decompose the residual.

For n=3, **every** Birkhoff decomposition of `|V|^2` is determinant-exact.
Indeed the determinant expansion uses only singleton and complementary
two-subset minors, and Jacobi complementarity for a 3x3 unitary identifies the
two-subset squared minors with the complementary singleton squared entries.
Therefore the full `1+3` determinant is a strictly positive convex combination
of all six full permutation vertices in `F_13`.

Now suppose a support direction is exposed at this common-block point:
`L(det(A+B))=M=max_sigma f(sigma)`.  Since the determinant is a positive convex
combination of six numbers each at most M, necessarily

`f(sigma)=M` for every `sigma in F_13`.

Set `g=f-M`.  Constants belong to Saxl_4, so `g` remains in Saxl_4; moreover
`g=0` on `F_13` and `g<=0` on all 24 endpoint permutations.

### Exact finite certificate

For **each of the 48** external functionals `e`, the checker gives an identity
on all Saxl_4 functions

`e(g)=sum_{sigma notin F_13} lambda_sigma g(sigma)
      + sum_{sigma in F_13} mu_sigma g(sigma)`

with every `lambda_sigma>=0`.  Therefore `e(g)<=0`, hence `e(f)<=M`.

One representative certificate is

`e_{(0,1,2,3),(1,2,0)}
 = (1/3)(delta_(1,3,2,0)+delta_(2,3,0,1)+delta_(3,0,1,2))
   +(1/3)delta_(0,2,3,1)-(1/3)delta_(0,3,2,1)`,

where the last two terms vanish on `g` because they are face evaluations.
The file `CHECK_13.py` verifies the full list of 48 rational identities on all
53 generators.  It also checks that every certificate has strictly positive
total coefficient outside the face.

### Consequence

By the partner external-vertex theorem,

`h_L(U)<=M` for **every** true `U in U(4)`.

Thus an exposed full-support `1+3` common-block direction is already globally
safe, not merely locally safe along block perturbations.  If all eighteen
off-face permutation supports are strictly below M, the exact certificates
make all 48 external inequalities strict as well.  Finite continuity then
gives an open spectral/support collar.

The only `1+3` boundary points not covered by that strict-collar statement are
lower-support/tied strata: a zero entry in the 3x3 coupling block or an
off-face endpoint tie.  The exact common-block theorem still proves MOC4 at
those boundary points; only the open-collar statement can degenerate there.

## 5. Full-support `2+2` face: 40 of 48 external facets are paid

Relabel a `2+2` common reducing block so the preserved row/column partition is
`{0,1}|{2,3}`.  The block-preserving face is

`F_22={(0,1,2,3),(0,1,3,2),(1,0,2,3),(1,0,3,2)}`.

If both 2x2 unitary blocks are nonmonomial, each 2x2 determinant is a strictly
positive convex combination of its two permutation endpoints, so their
product is a strictly positive convex combination of all four vertices in
`F_22`.  At an exposed support maximum, therefore `f=M` on all four face
vertices.  Again put `g=f-M`, so `g=0` on `F_22`, `g<=0` elsewhere and
`g in Saxl_4`.

The exact checker proves nonnegative-outside certificates for **40 of the 48**
external functionals.  A representative is

`e_{(0,1,2,3),(1,2,0)}
 = (1/3)(delta_(0,2,3,1)+delta_(2,3,1,0)+delta_(3,1,0,2))
   -(1/3)delta_(0,1,3,2)+(1/3)delta_(1,0,3,2)`.

The final two evaluations are on `F_22`; hence on `g` this is simply one third
of three nonpositive outside endpoint values.

All 40 identities are checked exactly on all 53 Saxl generators.  The only
eight external labels not covered are

`((2,3,0,1),(1,2,0))`, `((2,3,0,1),(2,0,1))`,
`((2,3,1,0),(1,0,2))`, `((2,3,1,0),(2,1,0))`,
`((3,2,0,1),(1,0,2))`, `((3,2,0,1),(2,1,0))`,
`((3,2,1,0),(1,2,0))`, `((3,2,1,0),(2,0,1))`.

Their `tau` values are exactly the four permutations that swap the two
2-element blocks as sets.  Thus every possible Saxl outer excess at a
full-support exposed `2+2` face is a **cross-block antipodal obstruction**.

This is a finite exact reduction, not a claim that the remaining eight are
actually attainable by a true unitary.

## 6. Direct application of the named partner result

The newest account03/B09 chamber report identifies one unique dangerous
external atom

`e_* = e_{(2,3,0,1),(1,2,0)}`

and pays it throughout a nontrivial support chamber using the genuine
complementary-minor quartic/cofactor condition.  That atom is one of the exact
eight residual labels above.

So the two results fit without relaxation:

1. the present boundary theorem proves that at a full-support exposed `2+2`
   common-block face the other 40 external facets can never be the first
   obstruction;
2. B09 demonstrates on one real spectral chamber that a genuine-spinor
   cofactor/blossom certificate can pay one of the eight surviving
   cross-block atoms.

This sharply focuses the next boundary calculation: derive a symbolic
cofactor/spinor payment for the eight cross-swap atoms, or construct an actual
normal-pair/true-unitary support violation.  Merely finding an external Saxl
atom above M is not a counterexample, because external vertices need not be
genuine `Lambda^2 SU(4)` data.

## 7. Named all-pairs reduction after this run

Combine the inherited B08 boundary results with this run:

1. repeated spectra: exact determinant representation already proved;
2. proper common reducing blocks: exact MOC4 already proved;
3. opposite-scalar gauge: residual unsolved pairs may be taken simple-spectrum,
   individually invertible and irreducible;
4. full-support `1+3` approach: every external facet is endpoint-paid, so any
   exposed direction is globally safe; with strict off-face endpoint gap there
   is an open collar;
5. full-support `2+2` approach: 40 external facets are endpoint-paid; only the
   eight cross-block-swap atoms can obstruct an open collar;
6. the remaining generic irreducible core is governed by the lead's
   mixed-Schur / negative-definite split and its same-unitary reserve
   conditions.

Therefore a strict counterexample sequence cannot escape through a generic
`1+3` common-block face, and can approach a generic `2+2` common-block face
only through the eight explicitly listed cross-swap Saxl atoms (or through
lower-support/off-face-tie degeneracies).

The next B08 implication is named

`MOC4-COMMON-BLOCK-CROSS8-PAYMENT-v1`:

> For each full-support exposed 2+2 common-block spectral face, prove the eight
> cross-block-swap external functionals are paid by genuine spinor/cofactor
> compatibility, or construct a true-unitary source-valid support violation.

This is complementary to the lead's generic MSQR/NDI program and does not
replace it.

## 8. Verification and artifacts

Exact proof checkers use only Python's standard-library `Fraction` arithmetic.

`CHECK.py` verifies:
- 53 Saxl generators;
- all 48 external labels;
- exact nonnegative-outside certificates for 40 labels;
- exact classification of the 8 uncovered labels by cross-block-swapping
  `tau`.

Observed exact output:
`PASS exact Saxl_4 certificates`, `paid_external_facets=40`,
`uncovered_external_facets=8`.

`CHECK_13.py` verifies:
- the six-permutation `1+3` face;
- all 53 Saxl generators;
- exact nonnegative-outside certificates for all 48 external labels;
- positive outside mass in every certificate.

Observed exact output:
`PASS exact 1+3 Saxl_4 certificates`, `paid_external_facets=48`.

Checker discovery used a local floating LP only to find sparse candidates.
Every persisted mathematical identity used in the proof was then independently
rechecked in exact rational arithmetic; no floating feasibility assertion is
used as gold.

No benchmark gold, credentials, unrelated private data, email, Drive, public
posting, paid API/model/Codex call, remote workflow, permission change or
scheduler mutation occurred.

## 9. Operational truthfulness

The canonical brain-repository current-hour login path was absent when checked,
but the create attempt was denied by the platform safety layer.  I did not
retry through a bypass and do not claim a successful canonical login.  The
scientific START was persisted later than ideal, after fresh controls and an
initial derivation; START.json records that timing defect explicitly.

Own-account scheduler inspection found the twenty managed B01-B20 tasks
enabled on hourly schedules with quiet task-level notification/email flags
reported off; no B08 scheduler mutation was made and no missing managed slot
was found for B20 escalation.

Model self-report: `GPT-5.6 Sol`.  
Requested effort: `maximum actually supported`.  
Configured/self-reported effort: `UNKNOWN / not exposed`.  
Provider reasoning-token or thinking-seconds usage: `null / not exposed`.  
Elapsed execution is wall-clock work including tool/network time, not pure
thinking.

**Verdict:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains open.
