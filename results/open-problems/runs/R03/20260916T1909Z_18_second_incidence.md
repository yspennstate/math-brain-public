Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed scheduler still has no model or reasoning selector or authenticated runtime telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: `r(10)` improves from `275.9996818469674...` to `275.9747699588589...`, and `r(11)` from `525.1358249571144...` to `525.1348531358815...`. Section-B methods actually used: #15 BREAK THE SYMMETRY, #25 COUNT THE SAME THING TWICE, #30 ONE PRIME / ONE SCALE / ONE DIRECTION.**

Problem: **iid Rademacher square-matrix singularity — Komlos (1967) lineage; Jain--Sah--Sawhney (2021), Conjecture 1.1 specialized to uniform Rademacher; Sahasrabudhe (2025), Eq. (4.1). Overall source status: OPEN / R03 status: PARTIAL.**

# R03 run 18 — second projective incidence and a collision-conditioned modular sieve

Run ID: `20260916T1909Z_18_second_incidence`  
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Continuity, source, exact target, and fixed metric

Before new mathematics I reread/recovered the campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, and `operations/NEW_METHODS_2026-09-16.md`; the newest own report `runs/R03/20260916T1834Z_17_projective_incidence.md`; the repository F0001 lineage by search; the newest available R02 directory; and the newest available R04 report `runs/R04/20260916T181213Z_i0027_diameter_profile.md`. Large intake JSONL responses remain connector-truncated, so I do not claim a semantic row-by-row reread of every approximately 780 intake row.

Current source chain checked again on 2026-09-16:

1. Janos Komlos, *On the determinant of (0-1) matrices* (1967), the historical lineage.
2. Vishesh Jain, Ashwin Sah and Mehtaab Sawhney, *Singularity of discrete random matrices*, arXiv:2010.06554 / GAFA 31 (2021), Conjecture 1.1. In the uniform Rademacher specialization, the zero-row mechanism vanishes and the two signed pair mechanisms give the exact leading count `2 n(n-1) 2^{-n}` before overlap correction. Their sharp full theorem covers finite-support laws not uniform on their support, including biased Bernoulli; in the uniform-support case containing iid Rademacher the full theorem remains exponential-scale, while the compressible contribution is treated sharply.
3. Julian Sahasrabudhe, *Probabilistic combinatorics at exponentially small scales*, arXiv:2512.15077v1 (17 Dec 2025), Eq. (4.1): `P(det B_n=0)=(1+o(1))2 n^2 2^{-n}`. The surrounding text states that the exact iid sign asymptotic remains a central open problem; the symmetric Bernoulli ensemble is then treated separately.
4. Konstantin Tikhomirov, *Singularity of random Bernoulli matrices*: `P(det B_n=0)=(1/2+o(1))^n`, the exponential rate only.
5. Kenneth Maples, *Singularity of Random Matrices over Finite Fields*, arXiv:1012.2372. This is relevant to the modular route below, but its finite-field universality error is only `O(exp(-c alpha n))`.

A fresh bounded 2026 search again found no independently verified source-matching exact resolution. Exact dated queries and prior-art notes are archived in `artifacts/R03/20260916T1909Z_18_status_search.md`. A negative bounded search is not a novelty proof.

Let `T_n` be the exact union of all signed equal/opposite row-pair and column-pair events. Retained C225 proves the matching lower asymptotic with overlap correction. The fixed owner metric is

\[
\boxed{r(n):=2^n\Pr(\det B_n=0,\ T_n^c).}
\tag{M}
\]

Sharp closure is equivalent to

\[
\boxed{r(n)=o(n^2).}
\]

Retained C240/C246 normalize an iid sign matrix to a uniform binary matrix `A` of order

\[
m=n-1,
\]

and identify `T_n^c` exactly with

\[
\mathcal G_m:=\{A\in\{0,1\}^{m\times m}:\text{ all rows and columns are nonzero and pairwise distinct}\}.
\]

Retain without re-deriving C225--C252 and killed routes X27--X29. In particular, for a prime `p`, run17 defines

\[
d_p(A)=m-\operatorname{rank}_{\mathbb F_p}A,
\]

\[
Z_{1,p}(A)={d_p(A)\brack1}_p=\frac{p^{d_p(A)}-1}{p-1},
\]

and

\[
M_{1,p,m}:=\sum_{A\in\mathcal G_m}Z_{1,p}(A).
\]

Every real-singular integer matrix is singular modulo every prime, so run17 proved

\[
r(n)\le R_p(n):=2^{m+1-m^2}M_{1,p,m}.
\tag{1.1}
\]

The preceding best strict certificates were

\[
R_7(10)
=\frac{1272823873864066932975}{4611686018427387904}
=275.9996818469674\ldots,
\]

and

\[
R_{11}(11)
=\frac{1269700515190567964091374325}{2417851639229258349412352}
=525.1358249571144\ldots.
\]

The first-incidence bound deliberately counts every projective modular null direction. This run asks whether that overcount can itself be rigorously paid.

## 2. #15 BREAK THE SYMMETRY — modular corank one versus modular corank at least two

For `d>=0`, write

\[
Z_1(d)={d\brack1}_p,
\qquad
Z_2(d)={d\brack2}_p.
\]

The first incidence is exact on modular nullity `d=1`, but overcounts when `d>=2`. Rather than treat all modular-singular matrices symmetrically, split off the second Grassmann incidence.

### R03-C253 — universal second-incidence correction

**STATUS: PROVED.**

For `A in G_m`, its row span over `F_p` contains its `m` distinct nonzero binary rows and the zero vector. If the row rank is `rho`, choose `rho` pivot coordinates. Projection to those coordinates is injective on the row span; therefore

\[
|\operatorname{rowspan}(A)\cap\{0,1\}^m|\le2^\rho.
\]

Since the left side is at least `m+1`,

\[
\rho\ge\lceil\log_2(m+1)\rceil.
\]

Thus

\[
\boxed{
d_p(A)\le d_{\max}(m):=m-\lceil\log_2(m+1)\rceil.
}
\tag{C253.1}
\]

For `d>=2`, the Gaussian-binomial identities give

\[
\frac{Z_1(d)-1}{Z_2(d)}
=
\frac{p(p^2-1)}{p^d-1}.
\tag{C253.2}
\]

The right side decreases in `d`. Put

\[
\boxed{
c_{p,m}:=\frac{p(p^2-1)}{p^{d_{\max}(m)}-1}.}
\tag{C253.3}
\]

Then for every permitted `0<=d<=d_max(m)`,

\[
\boxed{
\mathbf 1_{\{d\ge1\}}
\le Z_1(d)-c_{p,m}Z_2(d).
}
\tag{C253.4}
\]

Indeed it is equality at `d=0,1`; for `d>=2`, C253.4 is exactly C253.2 plus monotonicity.

Define

\[
M_{2,p,m}:=\sum_{A\in\mathcal G_m}{d_p(A)\brack2}_p.
\]

A real-singular `A` is modular-singular, so summing C253.4 yields

\[
\boxed{
\#\{A\in\mathcal G_m:\det A=0\}
\le M_{1,p,m}-c_{p,m}M_{2,p,m}.
}
\tag{C253.5}
\]

This is the desired asymmetry: the earlier first-incidence certificate is strictly improvable as soon as one has any positive lower bound on the number of null 2-plane incidences.

## 3. #25 COUNT THE SAME THING TWICE — explicit null 2-planes

`M_2` can be read two ways:

1. matrix-first: each matrix of modular nullity `d` contributes the number `{d choose 2}_p` of null 2-planes;
2. plane-first: for every 2-plane `V <= F_p^m`, count collision-free binary matrices whose every column lies in `V^perp`.

The second view gives a concrete lower bound using sparse null relations.

Let `L_m` be the following projective null lines over an odd prime:

- all support-three lines of type `(+,+,-)`, three projective sign patterns per 3-set;
- all support-four balanced lines of type `(+,+,-,-)`, three projective sign patterns per 4-set.

For every distinct pair of lines `ell_1,ell_2 in L_m`, let

\[
V=\operatorname{span}(\ell_1,\ell_2).
\]

Deduplicate identical `V`.

For such a plane put

\[
S_V=(V^\perp\cap\{0,1\}^m)\setminus\{0\}.
\]

Ordered choices of `m` distinct columns from `S_V` automatically have nonzero pairwise-distinct columns, and there are

\[
(|S_V|)_m
\]

of them. The remaining bad row events are:

- one row is identically zero;
- two rows are identical.

For each such row-bad linear condition `H`, the number of ordered column choices satisfying it is exactly

\[
(|S_V\cap H|)_m,
\]

where the notation here already excludes the zero cube vector. Hence union bound gives the rigorous lower count

\[
\boxed{
g(V):=
\max\left\{0,
(|S_V|)_m-
\sum_{H\in\mathcal B_m}(|S_V\cap H|)_m
\right\}.}
\tag{3.1}
\]

Every resulting matrix lies in `G_m` and has `V` in its modular left nullspace. Different planes are **supposed** to be counted separately: `M_2` itself is an incidence count `(A,V)`. Therefore

\[
\boxed{
M_{2,p,m}\ge\sum_{V\in\mathcal V_m}g(V),
}
\tag{3.2}
\]

where `V_m` is the deduplicated sparse-plane family.

### R03-C254 — exact finite second-incidence improvements at n=10 and n=11

**STATUS: PROVED WITH EXECUTED EXACT CHECKER.**

For `m=9,p=7` the checker finds

\[
|L_9|=630,
\qquad
|\mathcal V_9|=166635,
\]

with cube-intersection distribution

\[
\begin{array}{c|ccccc}
|V^\perp\cap\{0,1\}^9|&64&72&80&96&128\\ \hline
\#V&52920&89775&15750&7560&630.
\end{array}
\]

The exact union-bound lower incidence count is

\[
M_{2,7,9}\ge
2942127020232812160000.
\tag{C254.1}
\]

Here `d_max=5`, so

\[
c_{7,9}=\frac{56}{2801}.
\]

Substituting C254.1 into C253.5 gives

\[
\boxed{
r(10)\le
\frac{3564857875550413515432975}
{12917332537615113519104}
=275.9747699588589\ldots.}
\tag{C254.2}
\]

The strict improvement over run17 is

\[
\boxed{
\frac{20112196427372739375}
{807333283600944594944}
=0.024911888108547206\ldots.}
\tag{C254.3}
\]

For `m=10,p=11`, the exact checker finds

\[
|L_{10}|=990,
\qquad
|\mathcal V_{10}|=420255,
\]

and

\[
M_{2,11,10}\ge
807305539038902680414176000.
\tag{C254.4}
\]

Here `d_max=6` and

\[
c_{11,10}=\frac{11}{14763}.
\]

Therefore

\[
\boxed{
r(11)\le
\frac{446298905163058911334081193175}
{849874851189084309818441728}
=525.1348531358815\ldots.}
\tag{C254.5}
\]

The improvement is

\[
0.000971821232940905\ldots .
\]

These are small numerical moves, but they are strict moves in the owner's fixed collision-subtracted metric, and they come from a reusable second-incidence mechanism rather than another support cutoff.

## 4. #30 ONE PRIME / ONE SCALE / ONE DIRECTION — an analytic second-incidence family

The exact sparse-plane enumeration above is finite. There is also a closed family valid for all dimensions.

Choose two disjoint 3-sets and on each choose one support-three projective relation `x_k=x_i+x_j`. The corresponding two null lines have disjoint support. Any linear combination using both basis lines has support six, so the only support-three lines in their span are the original two. Hence different unordered pairs of such lines generate different 2-planes.

The number of planes is therefore exactly

\[
\boxed{
N_m=\frac92{m\choose3}{m-3\choose3}.}
\tag{C255.1}
\]

Put

\[
u=m-6.
\]

For one such 2-plane, each constrained triple admits exactly three Boolean patterns, so

\[
|V^\perp\cap\{0,1\}^m|=9\,2^u.
\]

The row-bad union bound can be counted exactly by row type. With `(x)_m` the falling factorial, define

\[
\begin{aligned}
G_m={}&(9\,2^u-1)_m
-8(6\,2^u-1)_m
-4(3\,2^u-1)_m\\
&-5(5\,2^u-1)_m
-4(4\,2^u-1)_m\\
&-\left(7u+{u\choose2}\right)(9\,2^{u-1}-1)_m.
\end{aligned}
\tag{C255.2}
\]

The coefficients have direct meanings:

- `4` addend-zero events plus `4` within-triple addend/target equality events give the coefficient `8` at `6*2^u`;
- `2` target-zero events plus `2` within-triple addend/addend equality events give the coefficient `4` at `3*2^u`;
- the nine cross-triple row pairs split as five events with `5*2^u` patterns and four with `4*2^u` patterns;
- the `u` free-row zero events, the `6u` relation/free equalities, and the `C(u,2)` free/free equalities all leave `9*2^{u-1}` patterns.

Thus for every odd prime and every `m>=7`,

\[
\boxed{
M_{2,p,m}\ge N_m\,[G_m]_+.
}
\tag{C255.3}
\]

This is **R03-C255 — PROVED.** The exact checker independently verifies the `m=9` closed form

\[
G_9=22039379834572800,
\qquad N_9=7560.
\]

Combining C253 and C255 yields the explicit complete-domain corrected modular bound

\[
\boxed{
R_p^{(2)}(n)
=
R_p(n)-
2^{m+1-m^2}c_{p,m}N_m[G_m]_+,
\qquad m=n-1,
}
\tag{C255.4}
\]

for odd primes and `m>=7`.

### R03-C256 — updated retained complete-domain envelope

**STATUS: PROVED PARTIAL BOUND.**

Retain the exact published/certified values through `n=9`. At `n=10` use C254.2; at `n=11` use C254.5. For `n>=12`, take the minimum of the retained C249 certificate, the run17 first-incidence certificates, and C255.4 for the tested odd primes `3,5,7,11,13`.

This is pointwise no worse than run17's complete-domain envelope. It is **not** `o(n^2)` and therefore does not close the source conjecture.

## 5. What the three new-method routes actually taught us

### #15 BREAK THE SYMMETRY — SUCCESS at finite scale

The first modular incidence treats nullity one and high modular nullity identically. C253 breaks that symmetry and gives a strict correction whenever any null 2-plane incidence is certified. This moved the frozen metric at `n=10,11`.

### #25 COUNT THE SAME THING TWICE — SUCCESS as a reusable incidence compiler

Counting modular nullity matrix-first gives Gaussian binomials; counting plane-first turns the correction into Boolean cube intersections with explicit row-collision exclusions. Sparse two-relation planes give both the exact finite C254 computation and the analytic C255 family.

### #30 ONE PRIME / ONE SCALE / ONE DIRECTION — ASYMPTOTIC OBSTRUCTION IS NOW SHARPER

Run17 already killed the idea that one fixed small prime is uniformly optimal: `p=7` is best among the tested primes at `n=10`, while `p=11` beats it at `n=11`. A growing prime is the natural next scale.

Maples' finite-field theorem is uniform enough to say that an alpha-dense iid matrix over `F_q` has the uniform finite-field singularity law up to `O(exp(-c alpha n))` with absolute constants. But after multiplying by `2^n`, an unspecified exponential error is not a collision-subtracted `o(n^2)` estimate. Worse, the row/column collision mechanisms themselves live at the exact `n^2 2^{-n}` scale inside that error. Maples' determinant-residue work explicitly notes that substantially sharper residue control would require sub-exponential estimates beyond the method there.

So the current modular route has an exact, source-relevant missing statement:

\[
\boxed{
\text{prove collision-conditioned finite-field / determinant-residue error}
=o(n^2 2^{-n})
\text{ for a useful growing modulus.}
}
\tag{OPEN-18}
\]

This is not a renamed coupling lemma: it is the point where a prime-by-prime modular certificate would have to be sharp enough to distinguish the real singular matrices from modular false positives at the exact source scale.

Two additional exploratory routes failed to displace C254:

- an exact `F_2` event count after collision exclusion is substantially worse than the `p=7` first/second incidence at `n=10`;
- simultaneous small-prime projective witnesses overcount higher nullity even more aggressively, and the tested prime pairs did not beat the best single-prime certificate.

No theorem claim is attached to those exploratory numbers.

## 6. Independent R04 audit status

The newest available R04 report at this run start is

`runs/R04/20260916T181213Z_i0027_diameter_profile.md`.

It is the same C2 package already independently audited by R03 in the preceding cycle as

`R03-AUDIT-R04-I0027-C2-05 = PASS`

at claim scope. No newer R04 package was present, so I did **not** manufacture a duplicate audit. R04 remains PARTIAL on Aldous--Fill 6.13.

## 7. Failed routes / prior-art corrections retained

Retain the following as killed or limited, without resetting their history:

- exponential-rate singularity bounds are not the sharp prefactor problem;
- X27: blindly sending the fixed JSS epsilon to zero at polynomial scale is not justified by the published constants;
- X28: conditional row/column independence is false already in a small exact case;
- X29: one fixed `best prime` is false even between `n=10` and `n=11`;
- naive multiplication of left- and right-normal probabilities is invalid;
- the fixed-support circuit classifications through seven are useful finite certificates, but the underlying `novel partition` classifications overlap prior Arratia--DeSalvo literature and are not claimed novel;
- the private entropy-defect programme remains, at most, an intermediate route and never substitutes for this outside source target.

## 8. Reproducibility

Executed exact checker:

`artifacts/R03/20260916T1909Z_18_second_incidence_exact.py`

Creation commit:

`e002b1bba61df2d0208ee0e284c6680277aba683`

Blob SHA:

`ec2161a42022091790c35ea702f20a929d33a6bf`

Local SHA-256:

`277d7c4ec5291bb090e67cf58853d1897543b6bcb834626320271e1a5ad107a6`

Archived output:

`artifacts/R03/20260916T1909Z_18_second_incidence_exact.out`

Creation commit:

`c26963157bfba2f9172f020e9e21f4a9ed5f7537`

Blob SHA:

`d6b5f9f2657417f08b40f9c76a39383909d9dcc2`

Local output SHA-256:

`8a3a60f768055d35c718996d181c856446ad295c6510a3b4275e133ec882bd53`

The output terminates `SELF-CHECK PASS`.

Dated source/prior-art record:

`artifacts/R03/20260916T1909Z_18_status_search.md`

commit `96ec32bbfc43ce63e3878162ad6dcffce67da3a6`.

## 9. Cumulative current ledger

| Item | Status |
|---|---|
| Source target `P(det B_n=0)=(1+o(1))2n(n-1)2^{-n}` | **OPEN** |
| C225 matching lower bound including overlaps | **PROVED** |
| Exact collision subtraction C246/C247 | **PROVED** |
| Fixed/growing support payments through retained C237 | **PARTIAL / paid scopes** |
| JSS structured/compressible reduction C238/C239 | **PROVED REDUCTION using published theorem** |
| C250/C251 first modular projective incidence | **PROVED** |
| C252 prior complete-domain modular envelope | **PROVED PARTIAL** |
| **C253 universal second-incidence correction** | **PROVED NEW** |
| **C254 exact n=10/n=11 second-incidence improvements** | **PROVED NEW** |
| **C255 analytic disjoint-triple 2-plane family** | **PROVED NEW** |
| **C256 updated complete-domain envelope** | **PROVED NEW / PARTIAL toward source** |
| `r(10)` strict bound | **`<=275.9747699588589...` NEW** |
| `r(11)` strict bound | **`<=525.1348531358815...` NEW** |
| Full `r(n)=o(n^2)` | **OPEN** |
| R02 audit `R02-AUDIT-R03-C227-01` | **PASS, old claim-scoped** |
| P26 full R03 audit | **NONE YET** |
| second full-package R03 audit | **NONE YET** |
| R04 C2 audit | **`R03-AUDIT-R04-I0027-C2-05=PASS`, no newer package this run** |

## 10. Next attack

The second-incidence correction proves that modular corank overcount can be paid, but with a worst-nullity coefficient `c_{p,m}` that becomes tiny for fixed `p`. The next new-method run should not merely add third-incidence bookkeeping. The useful alternatives are:

1. **Growing-prime collision-conditioned universality:** make the Maples finite-field error explicit after excluding the exact fat row/column collision hyperplanes, at a modulus `p=p(n)` chosen so modular false positives are rare enough on the `2^{-n}` scale.
2. **Low-rank cube geometry:** classify the genuinely collision-free small-rank row/column spans that force the worst `d_max`; if the worst modular nullity cannot coexist with the sparse high-incidence planes, the coefficient in C253 can increase by orders of magnitude.
3. **Determinant residue sieve:** use several primes at the event level rather than multiplying projective null directions, while explicitly controlling correlations; the obstruction is precisely the lack of a sharp collision-conditioned residue theorem.

The source problem remains OPEN. This run moved the frozen metric and therefore is not a stuck episode.

## 11. Model/runtime interface

The interface limitation is still the same. The exposed native automation mutation schema offers prompt/title/schedule/enabled/timing controls but **no model-family selector, no reasoning-effort selector, and no authenticated runtime telemetry**. `GPT-6 / maximum` can only be placed in prompt text from this interface, which does not verify runtime selection.

Repository policy records that P26/P01/P03 modification probes returned `You cannot modify this task` in one context, while `RESULTS.md` records that P26 later updated successfully in a different authorized context. This is consistent with an ownership/workspace authorization boundary. The legitimate remedy is to use the owning/admin-authorized native-task context or platform support. I did not create a duplicate, bypass the permission boundary, or change any schedule in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  source:
    - "Komlos 1967, On the determinant of (0-1) matrices"
    - "Jain-Sah-Sawhney 2021, arXiv:2010.06554, Conjecture 1.1 specialized to uniform Rademacher"
    - "Sahasrabudhe 2025, arXiv:2512.15077, Eq. (4.1)"
  target: "P(det B_n=0)=(1+o(1))*2*n*(n-1)*2^(-n)"
  metric: "r(n)=2^n P(det B_n=0, T_n^c); success r(n)=o(n^2)"
  before:
    n10: "<=1272823873864066932975/4611686018427387904 = 275.9996818469674..."
    n11: "<=1269700515190567964091374325/2417851639229258349412352 = 525.1358249571144..."
  after:
    n10: "<=3564857875550413515432975/12917332537615113519104 = 275.9747699588589..."
    n11: "<=446298905163058911334081193175/849874851189084309818441728 = 525.1348531358815..."
  status: PARTIAL
  unchanged_count: 0
  exact_evidence:
    - "artifacts/R03/20260916T1909Z_18_second_incidence_exact.py @ e002b1bba61df2d0208ee0e284c6680277aba683"
    - "artifacts/R03/20260916T1909Z_18_second_incidence_exact.out @ c26963157bfba2f9172f020e9e21f4a9ed5f7537"
    - "artifacts/R03/20260916T1909Z_18_status_search.md @ 96ec32bbfc43ce63e3878162ad6dcffce67da3a6"
  audits:
    R02_AUDIT_R03_C227_01: PASS_CLAIM_SCOPED
    P26_full_R03: NONE_YET
    second_full_R03: NONE_YET
    R03_AUDIT_R04_I0027_C2_05: PASS_CLAIM_SCOPED_RETAINED
```

No shared ledger, peer file, email, Drive, public publication, purchase, permission, workflow or scheduler state was changed.
