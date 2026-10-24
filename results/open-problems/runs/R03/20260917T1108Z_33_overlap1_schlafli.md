Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the exposed runtime provides no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime telemetry, so I do not claim otherwise. METRIC MOVED: `r(10)=222.6104736743168493957921796888577...` remains exact and `r(11)<=523.9022787113135428552389980... -> 523.8230147929823368671351006...`; unchanged count `2 -> 0`. Methods #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #19 MAKE IT AN ALGORITHM, #29 ADD THE POINTS AT INFINITY.**

# R03 run33 — unbalanced overlap-one exact corank and a quantitative Schlaefli route

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source OPEN.** This run strictly lowers the frozen full-domain finite envelope at `n=11` and resets the stagnation count. It does **not** prove the sharp asymptotic. The asymptotic part of the run identifies a quantitative threshold-arrangement statement whose required error scale is now explicit; the finite part enlarges the exact-corank-two catalog beyond all previously paid overlap-one plane families and produces a replay-certified metric improvement.

## 1. Continuity, source match, and frozen quantity

I continued from `runs/R03/20260917T1010Z_32_bias_gauge_circuits.md`; no earlier certificate, failed route, metric, or stagnation count was reset.

Before new mathematics I recovered/read `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R03 report, the newest neighboring R04 state, and the F0001 intake/history. R04's newest relevant state is its retired I0027 handoff and contains no new theorem requiring an R03 audit. The queue has no certified READY replacement that authorizes rotation, and this run moves the metric in any case.

The intake target F0001 is Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 2.2: for an iid uniform Rademacher `n x n` matrix,

\[
P(\det B_n=0)=(2+o(1))n^2 2^{-n}.
\]

The modern source Jain--Sah--Sawhney, *Singularity of discrete random matrices*, arXiv:2010.06554 / GAFA 31 (2021), Conjecture 1.1, specializes more precisely to

\[
\boxed{P(\det B_n=0)=(1+o(1))n(n-1)2^{1-n}.}
\tag{1.1}
\]

For two fixed sign rows, equality or opposition has probability `2^(1-n)`; the same holds for columns. Retained C225 pays all overlaps among these elementary mechanisms. With `T_n` their exact union, the fixed R03 quantity remains

\[
\boxed{r(n):=2^n P(\det B_n=0,T_n^c),}
\tag{1.2}
\]

and source closure is equivalent to

\[
\boxed{r(n)=o(n^2).}
\tag{1.3}
\]

Current primary literature was rechecked on 2026-09-17. Jain--Sah--Sawhney still prove the sharp full elementary-mechanism asymptotic only when the finite-support entry law is **not uniform on its support**; for uniform support they give the correct exponential scale for full singularity plus a sharp structured/compressible analysis, not the polynomial prefactor. Hunter--Kwan--Sauermann--Sawhney's 2026 large-corank theorem gives `exp(-c n k)` suppression but does not determine the sharp corank-one prefactor. A bounded fresh search found no later accepted primary-source proof of (1.1). This is dated negative-search evidence, not a worldwide novelty certificate. Details are in `artifacts/R03/20260917T1108Z_33_source_status.md`.

The pre-run finite envelope was

\[
r(10)=222.6104736743168493957921796888577\ldots
\]

exactly, and

\[
r(11)\le 523.9022787113135428552389980480274\ldots .
\tag{1.4}
\]

All exact lower-dimensional values and all retained `n>=12` branches remain available throughout this run.

## 2. Method #17 — look for the numbers elsewhere: threshold chambers and a quantitative deficit lemma

Run32 corrected the novelty ledger using Voigt--Ziegler: the conceptual equivalence between sharp Bernoulli singularity and small excess in random cube-spanned hyperplanes is old. This run asks for a **quantitative** version in the older threshold-function language.

Set

\[
d=r-1,\qquad N=2^d,
\]

and consider the `N` vectors

\[
E_d=\{(1,x):x\in\{\pm1\}^d\}\subset\mathbb R^r.
\]

Let `M_d` be their rank-`r` linear matroid. Its central hyperplane arrangement is the Boolean threshold arrangement. Write `Theta_d` for its number of chambers, i.e. the number of Boolean threshold functions in `d` variables. The Schlaefli general-position maximum for `N` central hyperplanes of rank `r` is

\[
U_d=2\sum_{j=0}^{r-1}\binom{N-1}{j}.
\tag{2.1}
\]

An iid `r x r` Rademacher matrix can be row-normalized by multiplying each row by its first coordinate. The remaining `d` coordinates are still iid uniform signs, so singularity is exactly the probability that `r` iid ordered points from `E_d` are linearly dependent.

The following elementary matroid inequality gives an explicit bridge from chamber deficit to singularity.

### R03-C287 — quantitative no-broken-circuit / Schlaefli bound

Let `P_r` denote the singularity probability of an iid `r x r` Rademacher matrix. Then

\[
\boxed{
P_r
\le
1-\frac{(N)_r}{N^r}
+\frac{(r-1)!}{N^{r-1}}\,(U_d-\Theta_d),
\qquad N=2^{r-1}.
}
\tag{2.2}
\]

#### Proof

Fix a total order on the `N` elements of `E_d`. Let `w_k(M_d)` be the unsigned Whitney coefficient of the characteristic polynomial. By the no-broken-circuit theorem, `w_k(M_d)` is the number of `k`-element NBC sets. For the uniform rank-`r` matroid `U_{r,N}`, every independent set of size below `r` is present and the rank-`r` NBC sets are precisely the `r`-sets containing the globally least element.

Every NBC set of `M_d` is also an NBC set in the uniform matroid, so

\[
w_k(M_d)\le w_k(U_{r,N})
\]

for every `k`. Let `Q` be the number of **dependent distinct** `r`-subsets of `E_d`. Average over a uniformly random ordering of the ground set. Each such dependent `r`-set contributes zero rank-`r` NBC bases to `M_d`; in the uniform matroid it is an NBC basis exactly when it contains the global minimum, which occurs with probability `r/N`. Therefore

\[
w_r(U_{r,N})-w_r(M_d)\ge \frac rN Q.
\tag{2.3}
\]

By Zaslavsky's theorem,

\[
\Theta_d=\sum_{k=0}^r w_k(M_d),
\qquad
U_d=\sum_{k=0}^r w_k(U_{r,N}),
\]

and every coefficient deficit is nonnegative, so (2.3) yields

\[
Q\le \frac Nr(U_d-\Theta_d).
\tag{2.4}
\]

The number of ordered `r`-tuples with a repeated point is `N^r-(N)_r`. Each dependent distinct `r`-set contributes `r!` ordered tuples. Dividing

\[
N^r-(N)_r+r!Q
\]

by `N^r` and applying (2.4) gives (2.2). QED.

There is no novelty claim for the ingredients: NBC theory and Zaslavsky are classical, and Irmatov's 1996 threshold-function paper already links asymptotic Schlaefli saturation to the random-sign-span problem. The useful point here is the **error scale** forced by (2.2).

Indeed,

\[
U_d=\frac{2N^{r-1}}{(r-1)!}
\left(1+O\left(\frac{r^2}{N}\right)\right)
\tag{2.5}
\]

and

\[
1-\frac{(N)_r}{N^r}
=
\frac{r(r-1)}{2N}
+O\left(\frac{r^4}{N^2}\right).
\tag{2.6}
\]

Consequently the sharp Rademacher asymptotic would follow if one could prove the quantitative threshold-chamber saturation

\[
\boxed{
\frac{U_d-\Theta_d}{U_d}
\le
(1+o(1))\frac{r(r-1)}{4N},
\qquad N=2^{r-1}.
}
\tag{2.7}
\]

The required relative deficit is therefore `Theta(r^2/2^r)`, exponentially sharper than a bare statement `Theta_d/U_d -> 1`. This explains why existing threshold-count asymptotics, and Anthony's 2026 result that average chamber facet/specification number is only `Theta(d)`, do not by themselves close the singularity problem.

This is the main conceptual output of method #17: it translates the source problem into a very explicit quantitative defect problem for a classical arrangement, with the exact scale visible.

## 3. Methods #29 and #19 — classify new overlap-one null planes and turn the classification into an exact algorithm

The finite metric movement comes from a separate route. Run27 converted previously paid **balanced** overlap-one null-plane incidences into exact-corank-two matrices. Run30 then added **unbalanced disjoint-support** planes. The missing finite family is: overlap-one planes with arbitrary projective sign-relation types, excluding exactly the balanced overlap families already paid in run18/run21.

Work in the binary reduction at

\[
m=10,\qquad p=11.
\]

A projective sign-relation line has type

\[
(s,k),\qquad 1\le k\le\lfloor s/2\rfloor,
\]

where `s` is its support size and `k` is the smaller of its numbers of `+1` and `-1` coefficients.

Take two such lines `v,w` with support sizes `s,t` and exactly one common coordinate, and let

\[
V=\operatorname{span}_{\mathbb F_{11}}\{v,w\}.
\]

### Method #29: the projective line at infinity records the plane uniquely

The projective support spectrum of `V` is rigid. In `P^1(F_11)`:

- `[1:0]` has support `s`;
- `[0:1]` has support `t`;
- exactly one mixed projective ratio cancels the shared coordinate and has support `s+t-2`;
- the remaining `p-2=9` mixed lines have support `s+t-1`.

Since `s,t>=3`, the two generators are precisely the two projective lines whose supports are below `s+t-2`. Thus the unordered generator pair, its two support/type labels, and the overlap structure are recoverable from the plane itself. In particular:

1. distinct new type-pairs cannot secretly describe the same plane;
2. these overlap-one planes cannot equal any disjoint-support plane from runs20/26/30;
3. if either generator is unbalanced, the plane cannot equal a previously paid balanced-overlap plane;
4. balanced overlap-one planes with both supports at least `5` were also absent from run18/run21;
5. every nonzero vector in `V` has support at least `3`, so a matrix with exact left nullspace `V` has no zero row and no repeated row.

This support-spectrum argument is the disjointness certificate that allows the new finite counts to be added without re-paying old `M_2` mass.

### Local affine slices

Orient the shared coefficient of each relation to `+1`. For type `(s,k)` there is one overlap class when `2k=s` and two classes when `2k<s`:

- even: multiplicity `C(s-1,k-1)`, residual signs `(k-1,k)`;
- minority overlap: multiplicity `C(s-1,k-1)`, residual signs `(k-1,s-k)`;
- majority overlap: multiplicity `C(s-1,k)`, after projective sign normalization residual signs `(s-k-1,k)`.

Fix the common Boolean bit `z in {0,1}`. If there are `a` residual `+1` coefficients, the local Boolean slice is

\[
z+\sum_+x_i-\sum_-y_j=0.
\]

Because `p=11` exceeds every support size occurring here, the modular equation agrees with the integer equation on Boolean points. By Vandermonde,

\[
A_z=\binom{s-1}{a+z}.
\tag{3.1}
\]

The checker also exhausts every projective nonconstant linear functional on this local slice and records the largest affine fiber `q_z` exactly.

For a pair of local classes, with

\[
b=m-(s+t-1)
\]

free Boolean coordinates, the common Boolean orthogonal slice has size

\[
h=(A_0B_0+A_1B_1)2^b.
\tag{3.2}
\]

Every proper hyperplane in `V^perp` meets this slice in at most

\[
Q=\max\left\{
(q^A_0B_0+q^A_1B_1)2^b,
(q^B_0A_0+q^B_1A_1)2^b,
\max(A_0B_0,A_1B_1)2^b,
\frac h2\mathbf 1_{b>0}
\right\}.
\tag{3.3}
\]

To prove (3.3), condition on every block except one on which the defining functional is genuinely nonconstant. If it is nonconstant on an `A` or `B` block, the appropriate exact `q_z` fiber bound applies. If both restrictions vanish, only the overlap bit remains; and if a free Boolean coordinate survives, at most half that free cube can be selected.

### R03-C288 — exact-corank-two completion algorithm

Since `dim V^perp=m-2`, construct an ordered Boolean basis greedily. After `j` independent columns have been chosen, their span contains at most `2^j` Boolean vectors and, as a proper subspace, lies inside a hyperplane containing at most `Q` allowed slice points. Hence there are at least

\[
h-\min(2^j,Q)
\]

choices that increase rank. Therefore each plane/class carries at least

\[
\boxed{
B_V=\prod_{j=0}^{m-3}\bigl(h-\min(2^j,Q)\bigr)
}
\tag{3.4}
\]

ordered Boolean bases of `V^perp`. After those `m-2` columns, choose two additional distinct nonzero unused slice points in

\[
(h-m+1)(h-m)
\tag{3.5}
\]

ways. The resulting `m` columns span exactly `V^perp`, so the left modular nullspace is exactly `V`, i.e. modular corank exactly two. By the support-spectrum observation there are no zero/equal rows; by construction the columns are nonzero and distinct. Thus these matrices belong to the collision-free class `G_m`.

This is the finite theorem checked by `artifacts/R03/20260917T1108Z_33_unbalanced_overlap1_exact.py`.

## 4. Exact `m=10,p=11` enumeration and metric movement

The checker first reproduces run27's old balanced overlap-one plane total exactly:

\[
1,524,600.
\]

It then enumerates every overlap-one type pair with `s+t-1<=10`, excluding precisely those for which both relations are maximally balanced and at least one support is `3` or `4` — the families already credited by run18/run21.

It finds:

\[
\boxed{33\text{ new type pairs},}
\]

\[
\boxed{4,927,890\text{ previously uncredited overlap-one planes},}
\]

of which

\[
\boxed{4,905,750}
\]

have a positive exact-corank completion certificate from (3.4)--(3.5). Summing the injective exact-nullspace families gives

\[
\boxed{
E_{10}^{\rm new,ov1}
=4,460,180,826,038,468,846,968,800
}
\tag{4.1}
\]

collision-free binary `10 x 10` matrices of exact modular corank two.

The largest contributors are not merely support-three perturbations: the `(5,2)+(5,2)` family alone certifies

\[
1,571,668,287,222,227,927,040,000
\]

matrices, and `(3,1)+(4,1)`, `(3,1)+(6,2)`, `(5,2)+(6,3)`, `(4,1)+(4,2)`, `(4,2)+(6,2)` are also large contributors. The complete 33-pair table is archived in the executed output.

### R03-C289 — replay-certified improvement of `r(11)`

These planes were completely absent from the retained second-incidence `M_2` credit. For an exact-nullity-two matrix over `F_11`, the first projective incidence pays all

\[
{2\brack1}_{11}=12
\]

null lines, while the true singular indicator is `1`. Since no `-c M_2` credit had yet been paid for these new planes, the full reclaimable slack is therefore exactly

\[
12-1=11.
\]

The binary-to-R03 normalization at `m=10` is

\[
2^{m+1-m^2}=2^{-89}.
\]

Hence the new certified subtraction is

\[
\boxed{
\Delta_{11}
=11E_{10}^{\rm new,ov1}2^{-89}
=
\frac{1533187158950723666145525}
{19342813113834066795298816}
}
\tag{4.2}
\]

\[
\Delta_{11}=0.0792639183312059881038974160716\ldots .
\]

Subtracting (4.2) from the run30/run32 baseline gives

\[
\boxed{
r(11)
\le
\frac{32635850599847726046678930103575}
{62303201039659529147657486336}
}
\tag{4.3}
\]

and therefore

\[
\boxed{
r(11)\le523.8230147929823368671351006319558\ldots .
}
\tag{4.4}
\]

The exact checker recomputes the local projective fiber maxima, verifies the Vandermonde local counts, reproduces the run27 regression total, enumerates all new plane/type classes, verifies the exact-corank lower-bound arithmetic, and checks the rational correction and final bound. Its archived output terminates `SELF-CHECK PASS`.

This is genuine movement of the **same frozen full-domain quantity**. The exact `r(10)` value and all exact values below it are unchanged; (4.4) replaces the old `n=11` entry; every prior certified branch remains available for `n>=12`. No part of the previous envelope is weakened.

## 5. What this does and does not solve

The finite construction is **PARTIAL** only. For every fixed support pattern `(s,k),(t,l)`, the Boolean slice has density strictly below one in the ambient cube, so the normalized mass of these fixed-support exact-nullity families decays exponentially with dimension. Enumerating more bounded sparse relation types can keep improving small-`n` constants but cannot prove

\[
r(n)=o(n^2).
\]

The source-level problem remains the dense/small-corank sector.

The strongest asymptotic routes now on file are complementary:

1. **C286 triangular bias:** extend the Jain--Sah--Sawhney non-uniform sharp remainder estimate uniformly to sign bias `m_n=c/n`, then transfer to the uniform law through the exact gauge-averaged likelihood lower bound.
2. **C285 / Voigt--Ziegler cube-hyperplane excess:** prove a weighted-tail / uniform-integrability bound showing that nontrivial excess cube vertices on a random invertible sign hyperplane have expectation `o(n^2)`.
3. **C287 threshold-arrangement deficit:** prove the exponentially precise chamber saturation (2.7), not merely asymptotic saturation without a rate.

Method #17 is useful because it says exactly what a threshold-function theorem would have to deliver. Current threshold-arrangement computations reach only small dimensions, Irmatov's older equivalence is qualitative at this scale, and the recent chamber-facet result controls a different statistic. Thus the next asymptotic run should not merely enumerate one more bounded sparse relation family; it should attack one of these rate statements.

## 6. Source/prior-art boundaries and runtime controls

The dated source/prior-art artifact is `artifacts/R03/20260917T1108Z_33_source_status.md`. It records the source identity, current JSS / large-corank status, Voigt--Ziegler and Irmatov threshold connections, current threshold-arrangement computation limits, and the absence of an exact binary order-10 singular count in the bounded search. No negative search is treated as a novelty certificate.

There is no source closure claim and therefore no request for end-to-end closure audits. The retained narrow `R02-AUDIT-R03-C253-04=PASS` is not a full current-package audit. The newest neighboring R04 state contains no new theorem requiring a fresh R03 audit, so none was manufactured.

The model-setting limitation is unchanged. The exposed task-control surface has prompt/title, schedule/timing and enabled-state controls, but no model-family or reasoning-effort field and no authenticated applied-runtime telemetry. The earlier `You cannot modify this task` responses are treated as authorization/workspace boundaries; a real model change requires the owning/admin-authorized product context plus an interface that actually exposes model/reasoning controls, or platform support. No scheduler, permission, email, Drive, public-posting, workflow, shared-ledger, or peer-file state was changed.

## 7. Artifacts and immutable delivery

- Exact checker: `artifacts/R03/20260917T1108Z_33_unbalanced_overlap1_exact.py`, creation commit `f7f892b20427869058f95d948705cc995fce7f7b`.
- Executed exact output: `artifacts/R03/20260917T1108Z_33_unbalanced_overlap1_exact.out`, creation commit `efb940a01b23493dc341b4fe0a14f2de05ba4a6c`, ending `SELF-CHECK PASS`.
- Dated source/prior-art record: `artifacts/R03/20260917T1108Z_33_source_status.md`, creation commit `d1993600b0688dff6478035a28723a88f23a57d9`.

## ledger_delta

```yaml
ledger_delta:
  track: R03
  lane: HARD_OUTSIDE
  target: sharp iid Rademacher matrix singularity asymptotic
  source_status: OPEN
  status_before: PARTIAL
  status_after: PARTIAL
  metric_name: "r(n)=2^n P(det B_n=0, T_n^c), full n-range retained"
  metric_before:
    r10: "exact 2053219217998690247625/9223372036854775808 = 222.6104736743168493957921796888577..."
    r11_upper: "2040049312230419145475474052475/3893950064978720571728592896 = 523.9022787113135428552389980..."
  metric_after:
    r10: "unchanged exact"
    r11_upper: "32635850599847726046678930103575/62303201039659529147657486336 = 523.8230147929823368671351006..."
  movement: MOVED
  unchanged_count_before: 2
  unchanged_count_after: 0
  methods: [17, 19, 29]
  new_claims:
    - "R03-C287 PROVED: quantitative NBC/Schlaefli chamber-deficit upper bound for Rademacher singularity"
    - "R03-C288 PROVED: arbitrary-type overlap-one exact-corank-two completion construction at m=10,p=11"
    - "R03-C289 PROVED WITH EXECUTED EXACT CHECKER: new overlap-one families lower r(11) by 0.0792639183312059881..."
  finite_certificate:
    new_planes_enumerated: 4927890
    new_planes_positive_certificate: 4905750
    exact_corank2_matrix_lower_bound: 4460180826038468846968800
    self_check: PASS
  audits_new: []
  closure: false
  next_obligation: "attack a source-scale rate: C286 triangular-bias uniformity, C285/VZ weighted hyperplane excess, or C287 threshold-chamber deficit at Theta(n^2 2^-n) relative scale"
```
