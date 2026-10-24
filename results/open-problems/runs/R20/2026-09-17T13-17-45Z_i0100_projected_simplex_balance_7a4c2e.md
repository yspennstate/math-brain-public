Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed runtime still provides no authenticated applied-model receipt or reasoning-effort telemetry, so I do not claim GPT-6 / maximum. **NO MOVEMENT in the fixed metric: `1201 -> 1201`; exact covered set remains `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201}`; post-movement unchanged count `0 -> 1`; status PARTIAL / SOURCE OPEN. Section-B moves used: second-pass #2 ATTACK THE NEGATION FIRST, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS.**

# R20 / I0100 — projected-simplex radial depth and exact transverse balancing

Repository / branch: `yspennstate/math-open-problems` / `master`.
Canonical claim: `operations/claims/I0100.md`.
Outside source: Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26; stable compilation arXiv:2603.29571.
Target:
\[
T_p:=\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2},\qquad p\equiv1\pmod4.
\]
Tracked quantity: largest admissible prime with a matching exact primal/dual certificate for this source-normalized quantity, retaining the complete exact-certified set.

## 1. Continuity, source gate, ownership, and audit state

I continued from

`runs/R20/2026-09-17T12-06-06Z_i0100_p1201_jacobi_arcsine_c9e41a.md`

at commit `5f5844e3963156420d550e8973f0f39626110c51`. I reread the campaign index/ranking, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the canonical I0100 claim, the newest own report, and current neighboring Paley reports/claims. The connector is bounded on the full ~780-row intake corpus, so ownership was rechecked by exact I0100 claim plus targeted repository search rather than pretending a truncated rendering was a byte-for-byte reread of every unrelated intake row.

The live Randomstrasse/Jig source was rechecked on 2026-09-17. Conjecture 26 is still presented as OPEN and still asks for the asymptotic above. P04/I0101 remains the separate two-localization Conjecture 27; the former R12 degree-four-SoS assignment is not imported here; C28/I0103 remains the separate Paley ETF/RIP Conjecture 29.

The frozen exact frontier remains
\[
\boxed{p_{\max}=1201},
\]
with exact-certified set
\[
\boxed{\{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201\}}.
\]
The existing p=1201 checker/output remains the finite evidence; I did not spend this run manufacturing another finite certificate.

Audit update: P26 has now independently reconstructed the p=241 finite Fourier primal/dual theorem and records

`P26-AUDIT-R20-I0100-P241-FOURIER-DUAL-ENDTOEND-22 = PASS_FULL_FINITE_PROOF / CLAIM_SCOPED / SOURCE_PARTIAL_OPEN / PRIOR_ART_UNVERIFIED`,

with reconciliation

`P26-RECONCILE-R20-I0100-P241-2OF2-22 = PASS`.

Together with the earlier distinct R19 audit, p=241 is now another 2/2 outside-audited **finite** theorem. This does not audit any asymptotic claim below.

---

## 2. Idea before code

The previous run showed that the raw one-sided Chebyshev certificate has a genuine Jacobi/arcsine endpoint `sqrt(2)` and that any correction reaching constant `1` must be dense. The next question is therefore not “how do I sharpen the same scalar Jacobi bound?” but:

> what geometric object is the Chebyshev optimizer, and which part of that geometry is invisible to the one-point Jacobi phase?

The answer is unexpectedly clean: the problem is the radial depth, opposite one distinguished vertex, of a **projected regular simplex**. The raw Jacobi values are only the longitudinal coordinates of the other projected vertices. All room for improving `sqrt(2)` to `1` lies in their transverse geometry.

No new finite code was needed for the structural claims below; they are proved on the page.

---

## 3. #27 SWAP THE QUANTIFIERS — exact projected-simplex radial-depth formulation

I first state the general finite-cyclic lemma because it applies to both complementary Fourier halves.

Let `G=Z_n`. Let `Z` be a nonempty symmetric set of nonzero frequencies and put
\[
E_Z=\{r\in\mathbb R^G:\widehat r(0)=0,\ \operatorname{supp}\widehat r\subseteq Z\}.
\]
Let `P_Z` be the orthogonal projection onto `E_Z`, let `d=|Z|`, and set
\[
q=\frac dn=P_Z(x,x).
\]
Define the one-sided Chebyshev constant
\[
a_Z=\min_{\substack{r\in E_Z\\r(0)=1}}\left(-\min_{x\in G}r(x)\right).
\tag{3.1}
\]
Since every `r in E_Z` has mean zero, the minimum is attained away from zero.

Define projected-simplex vertices
\[
u_x=q^{-1/2}P_Ze_x\in E_Z.
\tag{3.2}
\]
Then
\[
\|u_x\|=1,\qquad \sum_xu_x=0,\qquad
\sum_xu_xu_x^\top=\frac nd I_{E_Z}.
\tag{3.3}
\]
Thus these are the vertices of the regular coordinate simplex after orthogonal projection to `E_Z`, rescaled to unit norm.

### Theorem R20-HULL1 — Chebyshev constant = opposite-vertex radial depth

For every such `Z`,
\[
\boxed{
a_Z=\max\{a\ge0:-a u_0\in\operatorname{conv}\{u_x:x\ne0\}\}.
}
\tag{3.4}
\]
Equivalently, `a_Z` is the radial function of the convex hull of all projected simplex vertices except `u_0`, evaluated in direction `-u_0`.

#### Proof

Put
\[
c_x=\langle u_0,u_x\rangle,
\qquad
z_x=u_x-c_xu_0\in u_0^\perp
\quad(x\ne0).
\tag{3.5}
\]
For `r in E_Z` with `r(0)=1`, put `v=sqrt(q) r` (identifying a function in `E_Z` with its Euclidean coordinate vector). Since
\[
r(x)=\langle v,u_x\rangle,
\qquad
\langle v,u_0\rangle=1,
\]
we may write uniquely
\[
v=u_0+h,\qquad h\perp u_0,
\]
and hence
\[
r(x)=c_x+\langle h,z_x\rangle.
\tag{3.6}
\]
Therefore
\[
a_Z=\min_{h\perp u_0}\max_{x\ne0}
\bigl(-c_x-\langle h,z_x\rangle\bigr).
\tag{3.7}
\]
The finite-dimensional LP dual is
\[
\boxed{
a_Z=\max_{\substack{y_x\ge0,\ \sum_{x\ne0}y_x=1\\
\sum_{x\ne0}y_xz_x=0}}
\left(-\sum_{x\ne0}y_xc_x\right).
}
\tag{3.8}
\]
For every feasible `y`,
\[
\sum_{x\ne0}y_xu_x
=\left(\sum y_xc_x\right)u_0
=-a u_0.
\]
Conversely every convex representation of `-a u_0` has zero transverse part and gives such a `y`. This is exactly (3.4). QED.

This is the promised quantifier swap. Instead of finding one trigonometric function whose lower bound holds **for every coordinate**, a lower bound on `a_Z` asks for the existence of **one convex combination** of projected vertices landing far enough along `-u_0`.

The category is classical. Baryshnikov--Vitale (1994) prove that a randomly rotated/projected regular simplex is affine-equivalent to a Gaussian sample, and Donoho--Tanner study neighborliness/phase transitions of randomly projected simplices. The Paley object is a deterministic harmonic projection at the critical half-dimensional aspect ratio. I found no bounded-source reference applying this opposite-vertex radial statistic to Randomstrasse Conjecture 26; that is negative search evidence only, not a novelty certificate.

---

## 4. #15 BREAK THE SYMMETRY — exact longitudinal/transverse decomposition

The projected-simplex frame gives much more structure than the scalar Jacobi row.

Put
\[
A=\frac nd.
\]
From (3.3), after removing the distinguished vertex, one obtains the exact identities
\[
\boxed{\sum_{x\ne0}c_x=-1,}
\tag{4.1}
\]
\[
\boxed{\sum_{x\ne0}c_x^2=A-1,}
\tag{4.2}
\]
\[
\boxed{\sum_{x\ne0}z_x=0,\qquad
\sum_{x\ne0}c_xz_x=0,}
\tag{4.3}
\]
\[
\boxed{\sum_{x\ne0}z_xz_x^\top=A I_{u_0^\perp}.}
\tag{4.4}
\]

The previous run's raw Chebyshev vector is exactly the longitudinal coordinate row `c`: indeed
\[
\frac1qP_Ze_0(x)=c_x.
\tag{4.5}
\]
For the Paley `N` half, `q=1/2`, so this is precisely `2P_N delta_0`, whose scaled coordinates have the Jacobi/arcsine law from `R20-ARC1`.

The decisive point is that the transverse vectors are not arbitrary noise: they are centered, exactly tight, and exactly uncorrelated with the longitudinal coordinate. That gives a canonical way to repair any proposed scalar weight profile.

### Theorem R20-BAL1 — exact transverse-balancing projection

For a real coefficient vector `f=(f_x)_{x ne 0}`, put
\[
R_f=\sum_{x\ne0}f_xz_x
\]
and define
\[
\boxed{
(\mathcal B_Z f)_x
=f_x-\frac1A\langle R_f,z_x\rangle.
}
\tag{4.6}
\]
Then
\[
\boxed{\sum (\mathcal B_Zf)_xz_x=0,}
\tag{4.7}
\]
while both total mass and longitudinal moment are preserved:
\[
\boxed{
\sum (\mathcal B_Zf)_x=\sum f_x,
\qquad
\sum c_x(\mathcal B_Zf)_x=\sum c_xf_x.
}
\tag{4.8}
\]
Moreover `B_Z` is the orthogonal projection in coefficient space onto
\[
K_Z:=\{y:\sum_{x\ne0}y_xz_x=0\}.
\tag{4.9}
\]
Consequently, if
\[
\mathcal B_Zf\ge0,\qquad \sum f_x>0,
\]
then
\[
y=\frac{\mathcal B_Zf}{\sum f_x}
\]
is feasible in (3.8) and gives the rigorous lower bound
\[
\boxed{
a_Z\ge-rac{\sum c_xf_x}{\sum f_x}.}
\tag{4.10}
\]

#### Proof

Equation (4.7) follows from (4.4):
\[
\sum_x(\mathcal B_Zf)_xz_x
=R_f-\frac1A\left(\sum_xz_xz_x^\top\right)R_f=0.
\]
The two identities in (4.8) follow from (4.3). If `Zmat` is the matrix with columns `z_x`, then
\[
\mathcal B_Z=I-A^{-1}Zmat^\top Zmat,
\]
and `Zmat Zmat^T=A I`; hence `B_Z` is symmetric and idempotent, with range `ker Zmat=K_Z`. QED.

There is also an explicit cyclic formula. Extend `f` to `G` by `f(0)=0`, put
\[
C_f=\sum_{x\ne0}f_xc_x,
\]
and recall `q=d/n=1/A`. Then for `x ne 0`,
\[
\boxed{
(\mathcal B_Zf)_x
=f_x-(P_Zf)(x)+q C_f c_x.
}
\tag{4.11}
\]
Thus the whole missing step has become a positivity problem for one explicit nonlinear projection. This is substantially more concrete than “find a dense correction.”

### Why the obvious affine repair still cannot work

Because `1` and `c` both lie in `K_Z`, every affine profile `f_x=alpha+beta c_x` is already fixed by `B_Z`; transverse balancing gives it no new freedom.

For the Paley `N` half, `A=2`, so `sum c_x^2=1`. Write `M=n-1` and let
\[
c_+=\max_{x\ne0}c_x.
\]
Among nonnegative probability weights of the form
\[
y_x=\alpha-\beta c_x,\qquad \beta\ge0,
\]
the best possible choice is obtained when the largest-`c` weight is zero, giving
\[
\boxed{
a_{\rm affine}
=\frac{1+c_+}{1+M c_+}.}
\tag{4.12}
\]
The previous Jacobi/arcsine endpoint implies
\[
\sqrt n\,c_+\to\sqrt2,
\]
so
\[
\boxed{\sqrt n\,a_{\rm affine}\to\frac1{\sqrt2}.}
\tag{4.13}
\]
Hence the factor-`sqrt(2)` obstruction survives **even after exact transverse balancing** if one stays in the affine span of the raw Jacobi coordinate. A successful proof must use a genuinely nonlinear profile and must exploit joint longitudinal/transverse structure, not only the one-point Jacobi phase.

This is the main “break symmetry” conclusion of the run.

---

## 5. The two complementary projected simplexes

Return to the Paley localization. Put
\[
n=(p-1)/2,\qquad |N|=n/2,\qquad |S|=n/2-1.
\]
Let `a_N` and `a_S` be the Chebyshev/radial constants (3.1) for the two frequency sets.

The two exact moment programs from earlier R20 work give
\[
\max_{\mu:\widehat\mu|_N=0}\mu_0=\frac{T_p}{n},
\qquad
\max_{\nu:\widehat\nu|_S=0}\nu_0=\frac1{T_p}.
\]
The abstract moment/Chebyshev duality therefore gives the exact identities
\[
\boxed{
a_N=\frac{T_p}{n-T_p},
\qquad
a_S=\frac1{T_p-1}.}
\tag{5.1}
\]
Equivalently,
\[
\boxed{
T_p=\frac{n a_N}{1+a_N}=1+\frac1{a_S}.}
\tag{5.2}
\]

### Theorem R20-TWORAD1 — the source conjecture from two existence lower bounds

It is sufficient to prove only
\[
\boxed{
\liminf_{p\to\infty}\sqrt n\,a_N\ge1,
\qquad
\liminf_{p\to\infty}\sqrt n\,a_S\ge1.}
\tag{5.3}
\]
Indeed, the first inequality and (5.2) give
\[
\liminf\frac{T_p}{\sqrt n}\ge1,
\]
while the second gives
\[
\limsup\frac{T_p}{\sqrt n}\le1.
\]
Conversely, `T_p/sqrt(n) -> 1` forces both scaled radial depths to tend to one.

This is a useful strengthening of the public self-dual/product reduction in shape, not a claim of new logical content over Lovasz vertex-transitive duality. The gain is constructive: **both sides are now lower-bound / convex-combination existence problems.** We no longer need to prove a universal Chebyshev upper inequality directly.

There is also an exact relation between the two raw longitudinal rows. Let `c^N,c^S` denote (4.5) for the two projections. Since
\[
P_N+P_S+P_{\{0\}}=I,
\]
for every `x ne 0`,
\[
\boxed{
c^S_x=-\frac{n c^N_x+2}{n-2}.}
\tag{5.4}
\]
Thus the previous Jacobi/arcsine law is inherited by **both** complementary projected-simplex problems, with reflection and an `O(1/n)` shift. The one-point distribution cannot distinguish which side is the hard side.

---

## 6. A second exact obstruction: a shared balancing profile is necessarily affine

For `B=G\setminus\{0\}`, extend a coefficient vector `y in R^B` by `y(0)=0`. From (3.8),
\[
y\in K_Z
\]
if and only if the Fourier transform of this extension is **constant on `Z`**. Therefore
\[
K_N\cap K_S
\]
consists exactly of vectors whose Fourier transform is constant on `N` and separately constant on `S`.

Since `N` and `S` partition all nonzero frequencies, the condition `y(0)=0` leaves exactly two free constants. Hence
\[
\boxed{\dim(K_N\cap K_S)=2.}
\tag{6.1}
\]
More explicitly,
\[
\boxed{K_N\cap K_S=\operatorname{span}\{\mathbf1_B,c^N_B\}.}
\tag{6.2}
\]
(The full raw vector has Fourier transform supported on `N`; removing its zero coordinate makes its transform piecewise constant on `N` and `S`.)

Combining (6.2) with (4.13): any **single coefficient profile that is automatically transverse-balanced for both complementary radial problems** lies in the affine raw-Jacobi span and is stuck at the old `1/sqrt(2)` constant. Therefore a proof of (5.3) must genuinely break the symmetry and build two different nonlinear positive profiles, one for each complementary section.

This is a precise reason the earlier “one formula should solve both halves” instinct fails.

---

## 7. #2 ATTACK THE NEGATION FIRST — what a counterexample now has to look like

Equations (5.1)--(5.3) make the negation concrete.

If along a subsequence
\[
T_p/\sqrt n\ge1+\varepsilon,
\]
then
\[
\sqrt n\,a_S\le\frac1{1+\varepsilon}+o(1),
\]
so the **S-projected simplex** has a deficient opposite-vertex radial depth.

If instead
\[
T_p/\sqrt n\le1-\varepsilon,
\]
then
\[
\sqrt n\,a_N\le1-\varepsilon+o(1),
\]
so the **N-projected simplex** is deficient.

Thus a source-level counterexample requires a macroscopic radial-depth defect in one of two complementary half-dimensional projected regular simplexes, even though both have the same asymptotic Jacobi/arcsine longitudinal marginal.

I tried three negation routes in this run:

1. **Simple complement-swapping group automorphism.** A direct multiplier/shift complement map would collapse the two radial problems, but the existing finite data do not support such a simple Cayley automorphism. This route does not explain the finite over/undershoots and was abandoned.
2. **Initial-bad-set interpolation.** Lifting exactly the coordinates below the target floor is not enough: the correction spills into previously good coordinates, i.e. the active set migrates. The exact theorem (4.6) identifies the missing object as positivity of the balanced profile, not invertibility of the first interpolation system.
3. **One shared scalar/Jacobi profile.** The intersection theorem (6.2) plus (4.13) kills this route rigorously: shared balanced profiles are affine and asymptotically stop at `1/sqrt(2)`.

So the counterexample search did not find evidence against Conjecture 26. It instead narrowed what either a proof or a counterexample must contain: genuinely nonlinear **transverse** information.

A private floating scan of random half-frequency models was used only as route discovery and is not recorded as evidence or a certificate. It did not produce a stable contrary asymptotic. No numerical output is promoted to an exact claim here.

---

## 8. Nearest literature and the new proof target

Relevant existing categories found in the dated 2026-09-17 search:

- Baryshnikov--Vitale, *Regular simplices and Gaussian samples* (Discrete Comput. Geom. 11, 1994): random projections of a regular simplex are affine-equivalent to Gaussian samples for affine-invariant statistics.
- Donoho--Tanner, *Neighborliness of randomly projected simplices in high dimensions* (PNAS, 2005) and subsequent phase-transition work: random simplex projection / nonnegative linear-program geometry.
- Su--Winterhof, *Correlation Measure of Order k and Linear Complexity Profile of Legendre-Sidelnikov Sequences* (IEICE, 2012): higher-order pseudorandomness of the relevant sequence family via character sums.
- Ping Xi's Jacobi-sum equidistribution theorem, used in the preceding run, supplies the one-point arcsine law but not the transverse positivity required here.

The public Jig already contains the Lovasz-product/self-dual reduction. I therefore do **not** claim that “use both complementary theta problems” is new. The new candidate mechanism here is the exact projected-simplex/transverse-balancing formulation (3.4), (4.6), and the two-profile obstruction (6.2). A bounded search did not locate this formulation in the Paley-localization literature; this is not a publication-priority certificate.

### Remaining obligation after this run

For each `Z in {N,S}`, find a nonlinear scalar or structured profile `f_Z` such that
\[
\boxed{\mathcal B_Z f_Z\ge0}
\tag{8.1}
\]
and
\[
\boxed{-\frac{\sum c^Z_x f_Z(x)}{\sum f_Z(x)}
\ge\frac{1-o(1)}{\sqrt n}.}
\tag{8.2}
\]
Then R20-BAL1 and R20-TWORAD1 prove the source asymptotic.

This is now a concrete joint-Jacobi / high-order-Sidelnikov problem: control the sign of the explicit balancing projection (4.11) for a nonlinear profile. The one-point arcsine theorem cannot do it; higher-order correlations are exactly the missing input.

Next second-pass Section-B moves: **#6 DEFORM TO A SOLVABLE POINT, #14 FIND THE GROUP ACTING, #25 COUNT THE SAME THING TWICE**. The intended attack is to start with a random/solvable half-subspace profile for which `B_Z f >= 0`, deform its Gram data toward the Paley harmonic frame, and try to identify an invariant or paired count that prevents positivity loss before the target constant reaches one.

---

## 9. Scheduler/model-control status

The limitation remains unchanged. The exposed task-control surface supports task text/title, schedule/timing, enabled state and timing mode, but no native model-family selector, no reasoning-effort selector, no authenticated completed-run applied-model telemetry, and no guaranteed hour-long execution control. GPT-6 / maximum therefore remains a request in prompt text only in this environment.

The historical P26 `You cannot modify this task` event was an ownership/context restriction; later repository state records that P26 was successfully updated from a different authorized context. The legitimate workaround is therefore the owning product/workspace context or platform support exposing model/reasoning controls, not a duplicate task or a permission bypass.

---

## ledger_delta

```yaml
ledger_delta:
  track: R20
  source: "Randomstrasse 2025 Conjecture 26 / I0100"
  ownership: "R20 exclusive CLOSABLE OUTSIDE; P04/I0101, former R12/I0102, C28/I0103 excluded"
  metric_name: "largest admissible prime with matching exact primal and dual source-normalized certificate"
  metric_before: 1201
  metric_after: 1201
  exact_covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201]
  status: PARTIAL
  source_status: OPEN
  unchanged_count_before: 0
  unchanged_count_after: 1
  tried_moves: [2,15,27]
  new_claims:
    - "R20-HULL1: one-sided Fourier Chebyshev constant equals opposite-vertex radial depth of a projected regular simplex"
    - "R20-BAL1: exact transverse-balancing orthogonal projection preserving mass and radial objective"
    - "R20-TWORAD1: Conjecture 26 follows from lower radial-depth constant 1 on both complementary projected simplexes"
    - "R20-INTER1: the two complementary transverse-balance spaces intersect exactly in the affine raw-Jacobi span"
    - "R20-AFFFAIL1: affine/shared raw-Jacobi profiles asymptotically stop at the old 1/sqrt(2) constructive constant"
  remaining_obligation: "for Z=N and Z=S construct nonlinear profiles f_Z with B_Z f_Z >= 0 and radial mean at least (1-o(1))/sqrt(n); equivalently prove both complementary projected-simplex radial lower bounds"
  exact_finite_evidence:
    - "p=1201 exact interval primal/dual checker remains PASS"
  outside_audits:
    - "R19 p=181 PASS_EXACT_FINITE_CASE"
    - "P26 p=181 PASS_FULL_FINITE_PROOF / 2OF2 reconciled"
    - "R19 p=241 distinct exact finite audit"
    - "P26-AUDIT-R20-I0100-P241-FOURIER-DUAL-ENDTOEND-22 PASS_FULL_FINITE_PROOF / 2OF2 reconciled"
  new_claim_audit_status: "SELF-CHECK ONLY; no OTHER-track audit yet"
  closure: false
```

**NO CLOSURE CLAIM.**