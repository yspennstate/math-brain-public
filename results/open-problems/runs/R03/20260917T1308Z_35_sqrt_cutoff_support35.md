Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the accessible runtime exposes no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: `r(10)=222.6104736743168493957921796888577...` remains exact and `r(11)<=523.5160924680886551737549902615365... -> 523.4894710902614257202829985613411...`; unchanged count `0 -> 0`. Methods used: #3 PROVE SOMETHING STRONGER; #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE; #26 HUNT THE SPORADIC CASE.**

# R03 run35 — square-root coefficient-complexity cutoff and a new support-(3,5) exact-corank family

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source OPEN.** This run proves a stronger asymptotic structural reduction and gives one replay-certified finite improvement. It does not prove the sharp singularity asymptotic.

All thirty Section-B moves had already appeared somewhere in the R03 history by run34, so a literally unused method number no longer exists. I therefore reused three methods in genuinely new incarnations, none from the immediately preceding run34 triple `#4,#21,#27`. This preserves rather than resets the method history.

## 1. Continuity, exact outside source and frozen metric

Before new mathematics I recovered/read the required campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the F0001 intake record, the newest own report `runs/R03/20260917T1205Z_34_coeff_complexity_overlap2.md`, newest discoverable R02 report `runs/R02/20260917T1204Z_4e8c1a73.md`, and newest discoverable R04 report `runs/R04/20260917T0112Z_i0027_stuck_thinking_01.md`.

The assigned outside target is still intake `F0001`, Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / Probability Surveys 18 (2021), Conjecture 2.2. The intake statement is

\[
 p_n=(2+o(1))n^2 2^{-n}
\]

for an iid uniform Rademacher `n x n` matrix. This is exactly equivalent at the claimed precision to

\[
\boxed{\Pr(\det B_n=0)=(1+o(1))n(n-1)2^{1-n}.}
\tag{1.1}
\]

Indeed `n(n-1)2^{1-n}=(2+o(1))n^2 2^{-n}`. I retain (1.1) only after that source match.

Let `T_n` be the exact union of equal/opposite signed row-pair and column-pair events. Retained C225 pays their intersections. The fixed R03 remainder remains

\[
\boxed{r(n):=2^n\Pr(\det B_n=0,T_n^c),}
\tag{1.2}
\]

and source closure remains equivalent to

\[
\boxed{r(n)=o(n^2).}
\tag{1.3}
\]

Current primary literature was checked again on 2026-09-17. Jain--Sah--Sawhney, arXiv:2010.06554 / GAFA 2021, prove the sharp elementary-mechanism asymptotic for finite-support laws that are **not uniform on their support**; their uniform-support result gives exponential-scale full singularity precision and sharp compressible-sector control, not the missing Rademacher polynomial prefactor. Song--Wang, arXiv:2607.00495 (2026), determine growing-corank Bernoulli probabilities, and Hunter--Kwan--Sauermann--Sawhney, arXiv:2510.12933, prove `P(corank>=k)<=exp(-cnk)` for iid Rademacher matrices. Neither determines the sharp corank-one prefactor. A bounded fresh search found no later primary-source proof of (1.1). Details and search scope are archived in `artifacts/R03/20260917T1308Z_35_source_status.md`.

Pre-run frozen envelope:

\[
r(10)=222.6104736743168493957921796888577\ldots
\]

exactly, and

\[
\boxed{r(11)\le523.5160924680886551737549902615365\ldots.}
\tag{1.4}
\]

## 2. Method #3 — prove something stronger: push C290 to a fixed fraction of `sqrt(d)`

Run31/C285 reduced the dense corank-one problem, after paying the structured sector and higher corank, to the excess number of cube points in a random affine cube section. Put `d=n-1`. For an invertible sign matrix

\[
R\in\{\pm1\}^{d\times d}
\]

write

\[
w_R=R^{-1}{\bf1},\qquad
C(w)=\{x\in\{\pm1\}^d:\langle x,w\rangle=1\},
\qquad M(w)=|C(w)|,
\]

and

\[
\kappa(w)=\#\{|w_i|:w_i\ne0\}.
\]

Run34/C290 proved superexponential negligibility for dense normals with `kappa(w)<=d^(1/2-epsilon)`. The gap was the near-square-root window. The new observation is that the section-pattern count can be sharpened enough to combine with the classical Sárközy--Szemerédi distinct-coefficient bound.

### 2.1 Refined pattern count

Fix `k>=1`. Label every coordinate by `0` or by a signed magnitude class `+j/-j`, `j in [k]`. There are at most

\[
(2k+1)^d
\tag{2.1}
\]

such coordinate assignments.

For a fixed assignment, after flipping cube coordinates to absorb coefficient signs, let the positive magnitudes be `a_1,...,a_k` and their multiplicities be `m_1,...,m_k`. A cube point enters the section equation only through the block-sum vector

\[
z=(z_1,\ldots,z_k),\qquad
z_j\in\{-m_j,-m_j+2,\ldots,m_j\}.
\]

Thus

\[
Z=\prod_{j=1}^k Z_j,
\qquad |Z|=\prod_{j=1}^k(m_j+1)
\le\left(1+\frac dk\right)^k
\tag{2.2}
\]

by AM--GM.

For `z in Z`, the condition `a dot z=1` is an affine hyperplane in `a`-space. For a fixed `a`, its equality pattern is determined by the affine flat obtained by intersecting all those hyperplanes that contain `a`. A flat in `R^k` is defined by at most `k` of the hyperplanes. Therefore the number of section patterns for this coordinate assignment is at most

\[
\sum_{j=0}^k\binom{|Z|}{j}
\le(|Z|+1)^k
\le2^k\left(1+\frac dk\right)^{k^2}.
\tag{2.3}
\]

Consequently the number of possible cube-section patterns with exactly `k` nonzero magnitude classes is bounded by

\[
\boxed{
N_{d,k}
\le(2k+1)^d 2^k\left(1+\frac dk\right)^{k^2}.
}
\tag{2.4}
\]

This replaces the coarser `(d+2)^{k^2}` term in C290 by the multiplicity-sensitive factor `(1+d/k)^{k^2}`.

### 2.2 Two anticoncentration regimes

Fix the retained density constant `delta>0` and suppose `|supp w|>=delta d`.

First, weighted Sperner gives

\[
M(w)\le C_\delta\frac{2^d}{\sqrt d}.
\tag{2.5}
\]

Second, if `k=kappa(w)`, choose one coordinate from each distinct nonzero absolute-magnitude class and condition on all remaining signs. Since `w_R` is rational, multiplying by a common denominator makes these `k` selected absolute coefficients distinct integers. The Sárközy--Szemerédi theorem therefore gives the conditional atom bound

\[
\sup_t\Pr\left(\sum_{j=1}^k\varepsilon_j a_j=t\right)
\le Ck^{-3/2}.
\]

Averaging over the conditioned signs gives

\[
\boxed{M(w)\le C2^d k^{-3/2}.}
\tag{2.6}
\]

### 2.3 Basis-weighted counting

Let `I_d` be the number of invertible `d x d` sign matrices. Tikhomirov's theorem gives `I_d=(1-o(1))2^{d^2}`, so for large `d`, `I_d>=2^{d^2-1}`.

For a fixed cube section `C` of size `M`, there are at most `M^d` ordered sign-row tuples in `C`, hence at most `M^d` invertible bases. The weight `(M-d)_+` is at most `M`. An invertible basis `R` determines `w_R=R^{-1}1` uniquely, so summing by **section patterns**, rather than by numerical coefficient vectors, introduces no missing multiplicity. Thus a family of at most `N` section patterns, each of size at most `M`, contributes at most

\[
2N M^{d+1}2^{-d^2}
\tag{2.7}
\]

to the expectation over uniform invertible `R`.

### R03-C292 — square-root coefficient-complexity cutoff

**STATUS: PROVED.** Fix `delta>0` and any constant

\[
0<c<\frac1{\sqrt2}.
\]

Then

\[
\boxed{
\mathbb E\Big[(M(w_R)-d)_+
\mathbf1_{\{|\operatorname{supp}w_R|\ge\delta d\}}
\mathbf1_{\{\kappa(w_R)\le c\sqrt d\}}\Big]
\le \exp(-(1-o(1))d\log\log d).
}
\tag{C292}
\]

In particular this sector is `o(1)`, far below the `o(d^2)` source target.

**Proof.** Split at

\[
K_0=\frac{\sqrt d}{\log d}.
\]

For `k<=K_0`, use (2.4), (2.5), and (2.7). Uniformly in this range,

\[
d\log(2k+1)
\le\frac12d\log d-d\log\log d+O(d),
\]

while

\[
k^2\log(1+d/k)
\le O(d/\log d).
\]

The factor `M^{d+1}2^{-d^2}` from (2.5) contributes

\[
-\frac12d\log d+O(d).
\]

Therefore the total logarithm is at most

\[
-d\log\log d+O(d).
\tag{2.8}
\]

For `K_0<=k<=c sqrt(d)`, use (2.4), (2.6), and (2.7). We have

\[
d\log(2k+1)\le\frac12d\log d+O(d),
\]

and

\[
k^2\log(1+d/k)
\le\left(\frac{c^2}{2}+o(1)\right)d\log d.
\]

Since `k>=sqrt(d)/log d`, (2.6) contributes

\[
-\frac32d\log k
\le-\frac34d\log d+O(d\log\log d).
\]

Thus this range has logarithm at most

\[
\left(-\frac14+\frac{c^2}{2}+o(1)\right)d\log d.
\tag{2.9}
\]

The coefficient is strictly negative because `c<1/sqrt(2)`. Summing over at most `d` values of `k` does not affect either estimate. Combining (2.8) and (2.9) proves C292. QED.

### Consequence

C290 said a polynomial-scale obstruction must satisfy `kappa(w_R)>=d^(1/2-o(1))`. C292 improves this to the fixed leading square-root constant:

\[
\boxed{
\text{any source-relevant surviving dense normal must have }
\kappa(w_R)\ge\left(\frac1{\sqrt2}-o(1)\right)\sqrt d.
}
\tag{2.10}
\]

This still does not prove the source conjecture. It localizes the remaining dense corank-one mass to normals with at least about `0.707 sqrt(d)` distinct coefficient magnitudes.

The literature ingredients in C292 are classical; the particular basis-weighted combination with C285/C290 was not located in the bounded search, but **no novelty claim is made** without a dedicated prior-art audit.

## 3. Method #17 — look for the numbers elsewhere: the 2026 Sidon-subset route does not beat C292

I checked a genuinely new 2026 additive-combinatorics input: Bailleul--Riblet, *On the largest Sidon subset in a finite subset of R^N*, arXiv:2605.03181, which proves that every `k`-point subset of `R^N` contains a Sidon subset of size

\[
\left(\frac1{3\sqrt3}+o(1)\right)\sqrt k.
\]

The hope was that many distinct magnitudes might automatically contain a large additive-dissociated subfamily and hence yield stronger Halász/Gunby anticoncentration.

At the source scale this route loses. Even granting a `Theta(sqrt(k))` subfamily with the ideal distinct-coefficient Sárközy--Szemerédi atom size, conditioning only on that subfamily yields at best a power around `k^{-3/4}`, much weaker than applying Sárközy--Szemerédi directly to **all `k` distinct magnitudes**, which gives `k^{-3/2}`. Stronger distance-code/Halász estimates require additional exclusion of short additive relations and are not automatic from the Sidon-subset theorem in the needed form. So this route produced no stronger source bound and is recorded as a failed attack, not repackaged as a lemma.

The useful lesson is that the post-C292 obstruction is not simply “many distinct coefficients.” The next invariant has to measure the **short additive-relation energy among those magnitudes**. The promising dichotomy is: low short-relation energy should improve anticoncentration beyond `k^{-3/2}`; high short-relation energy should reduce the effective parameter entropy of section patterns via Freiman-type structure. That is a genuinely different next route from further sparse-plane enumeration.

## 4. Method #26 — hunt the finite sporadic family: support-(3,5), overlap-two planes

The asymptotic theorem above consumed the research effort; the finite work below is a bounded-dimension cleanup used only because it actually moves the frozen metric.

Work at the retained binary reduction `m=10`, prime `p=11`. A projective sign-relation line of support `3` has

\[
\binom{10}{3}2^{2}=480
\]

possibilities; support `5` has

\[
\binom{10}{5}2^{4}=4032.
\]

Form a two-plane from one support-3 line and one support-5 line whose supports overlap in exactly two coordinates. Canonical projective RREF deduplication gives exactly

\[
\boxed{806400}
\]

candidate planes.

To keep the new exact-nullspace family matrix-disjoint from every previously credited exact-corank-two family, the checker conservatively removes a plane if:

1. it contains any projective vector of support at most two;
2. it contains any pair of projective sign-relation lines whose supports overlap in `0` or `1` coordinate (the old disjoint/overlap-one families); or
3. it contains an overlap-two sign-line pair both of whose supports are at most four (the entire run34 support-3/4 overlap-two candidate class, even the portion that failed its own basis certificate).

This leaves exactly

\[
\boxed{403200}
\]

new planes. Every generating support union has size six. Compressing by the local rowspace gives exactly

\[
\boxed{1920}
\]

local rowspace types.

For each local type the checker enumerates the Boolean orthogonal slice and every projective linear functional over `F_11`. Exactly

\[
226800
\]

planes fail because their Boolean local slice does not span the four-dimensional local factor of `V^perp`. The remaining

\[
\boxed{176400}
\]

planes all lie in the single positive class

\[
(h_{loc},q,h,Q)=(7,6,112,96).
\tag{4.1}
\]

Here `h=112` is the full Boolean slice size and `Q=96` is the exact largest proper-hyperplane occupancy bound after adjoining the four free Boolean coordinates.

### R03-C293 — new exact-modular-corank-two family

**STATUS: PROVED WITH EXECUTED EXACT CHECKER.** For every positive plane `V`, a greedy ordered Boolean basis count gives at least

\[
B_V=
\prod_{j=0}^{7}
\left(112-\min\{2^j,96\}\right)
\tag{4.2}
\]

ordered bases of `V^perp`. After choosing those eight basis columns, the last two distinct nonzero columns have

\[
(112-9)(112-10)
\tag{4.3}
\]

choices. The columns therefore span `V^perp`, so the left modular nullspace is **exactly** `V`. The support-`<=2` exclusion rules out zero/repeated rows; the column construction itself uses distinct nonzero Boolean columns. Exact nullspace uniqueness makes the matrix families for distinct planes disjoint.

Summing over the `176400` positive planes gives at least

\[
\boxed{
E_{10}^{(3,5),ov2}
=1499101974069006827520000
}
\tag{4.4}
\]

collision-free binary `10 x 10` matrices with exact modular nullity two.

At `m=10,p=11`, the retained C253 branch has modular-nullity ceiling `D=5`, so

\[
c_{11,5}=\frac{132}{16105}.
\]

Regardless of whether one of these planes had already received one retained second-incidence credit, exact nullity two leaves at least the conservative reclaimable slack

\[
11-c_{11,5}
=\frac{177023}{16105}.
\]

Thus the additional normalized correction is

\[
\boxed{
\Delta_{11}
=
\frac{197720176544500735125}
{7427120332677308219392}
=0.02662137782722945347199170019\ldots .
}
\tag{4.5}
\]

Subtracting from the run34 envelope yields

\[
\boxed{
r(11)\le
\frac{32615069759481592686393385491735}
{62303201039659529147657486336}
=523.4894710902614257202829985613411\ldots .
}
\tag{C293}
\]

The exact C++ checker was executed locally before archival. It verifies all `806400` candidate planes, every prior-family exclusion, all `1920` local rowspaces, all projective hyperplane fibers, the exact-corank basis count, the big-integer matrix total, the rational C253 correction, and the final envelope. Its output ends `SELF-CHECK PASS`.

Checker: `artifacts/R03/20260917T1308Z_35_support35_exact.cpp`  
Archived output: `artifacts/R03/20260917T1308Z_35_support35_exact.out`  
Local source SHA-256 before upload: `3d4a08d53f10946a9d57014eb39f4388c750bbf8002f0ee0312a3be40a643459`.

## 5. Full-domain envelope and honest status

The full `n`-range is retained rather than replacing the source metric by a bounded case:

- all exact values through `n=10` remain unchanged;
- C293 replaces the `n=11` upper bound by `523.48947109026142572028...`;
- every previously certified full-domain branch remains available for `n>=12`.

So the frozen metric genuinely moves and the unchanged count remains zero.

This is still **PARTIAL**. C293 is bounded-dimensional and cannot prove the source asymptotic. C292 is the important asymptotic development, but it only eliminates coefficient complexity below `(1/sqrt(2)-o(1))*sqrt(d)`.

A concise remaining obligation is now

\[
\boxed{
\mathbb E\Big[(M(w_R)-d)_+
\mathbf1_{\rm nontrivial}
\mathbf1_{\rm JSS\text{-}unstructured}
\mathbf1_{\{\kappa(w_R)\ge(1/\sqrt2-o(1))\sqrt d\}}
\Big]
=o(d^2).
}
\tag{5.1}
\]

The highest-value next route is a **short-additive-relation dichotomy on the distinct coefficient magnitudes**. Low relation energy should feed a higher-order Halász/Gunby atom bound; high relation energy should force Freiman-type structure, lowering the dimension/entropy of the section-pattern arrangement. Either half would attack exactly the sector that C292 leaves and is more promising than another hour of bounded-support modular cleanup.

## 6. Runtime/model-control status

The accessible scheduled-task control schema still exposes prompt/title, schedule/timing, enabled state and notification controls, but **no model-family field and no reasoning-effort field**. There is also no authenticated applied-runtime telemetry in this worker surface. The requested `GPT-6 / maximum` therefore remains prompt text only from this worker's point of view.

The historical P26 `You cannot modify this task` result remains consistent with an authorization/workspace boundary; repository history records later success from a different authorized context. The legitimate remedy is an owning/admin-authorized product context that both owns the task and exposes model/reasoning controls, or a platform-side change/support intervention. There is no repository workaround and this run made no scheduler or permission change.

## 7. Structured ledger delta

```yaml
ledger_delta:
  task: R03
  source: "F0001 / Vu Conjecture 2.2; JSS arXiv:2010.06554 uniform-Rademacher specialization"
  metric: "full-domain envelope for r(n)=2^n P(det B_n=0, T_n^c)"
  before:
    r10: "exact 222.6104736743168493957921796888577..."
    r11_upper: "523.5160924680886551737549902615365..."
  after:
    r10: "exact 222.6104736743168493957921796888577..."
    r11_upper: "523.4894710902614257202829985613411..."
  status_before: PARTIAL
  status_after: PARTIAL
  source_status: OPEN
  unchanged_count_before: 0
  unchanged_count_after: 0
  tried_moves: [3, 17, 26]
  method_history_note: "all 30 method numbers were already exhausted before run35; reused three non-consecutive methods in new routes"
  new_claims:
    - "R03-C292 square-root coefficient-complexity cutoff: arbitrary dense kappa<=c sqrt(d), every fixed c<1/sqrt(2), is superexponentially negligible in basis-weighted excess"
    - "R03-C293 support-(3,5), overlap-two exact-modular-corank correction at m=10,p=11"
  failed_route:
    - "2026 Bailleul-Riblet universal Sidon-subset theorem does not by itself improve the direct Sárközy-Szemerédi atom bound at the R03 basis-weighted scale"
  remaining_obligation: "pay the dense JSS-unstructured corank-one sector with kappa(w_R)>=(1/sqrt(2)-o(1)) sqrt(d) at o(d^2) basis-weighted excess, preferably via short-additive-relation energy versus Freiman-entropy dichotomy"
  evidence:
    - "artifacts/R03/20260917T1308Z_35_support35_exact.cpp"
    - "artifacts/R03/20260917T1308Z_35_support35_exact.out"
    - "artifacts/R03/20260917T1308Z_35_source_status.md"
  audits:
    retained: ["R02-AUDIT-R03-C253-04=PASS"]
    current_full_package_P26: NONE
    second_current_full_package: NONE
```

No shared root ledger, peer-track file, email, Drive file, public post, purchase, permission, workflow, or scheduler state was changed.
