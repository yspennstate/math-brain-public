# MOC4 account01/B08 — exact complex-Hadamard common lift and an interior P/R gluing criterion

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T044241Z-b08-moc4-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact team state consumed

The target is, for every complex normal `4 x 4` pair,

\[
\det(A+B)\in\operatorname{conv}\{v_\pi:\pi\in S_4\},\qquad
v_\pi=\prod_{j=0}^3(a_{\pi(j)}+b_j),
\]

with singular and repeated-spectrum cases included.

The latest complete campaign-lead theorem consumed is account03/B07
`MOC4-V4-PAIR-GAP-CEILING-v1`, report blob
`28cbce0f0a6213c0760e0777a5baa5b0de12b31a`.  It confines any genuine
support violation `h(U)=M+gamma` to an explicit positive V4/pair reserve
and shows that a purely low-frequency endpoint relaxation is insufficient.

The assigned OTHER-account partner result consumed and applied is
account02/B09 run `20260922T034112Z-account02-B09-MOC4-r14`, theorem
`MOC4-ZERO-FIBER-HAAR-LIFT-v1`, report blob
`20a1ea240bb65b81b880cad265e4db5f225d2a8a`.  It gives one positive
24-permutation law reproducing *all* compound-minor marginals after Haar
averaging the residual U(2) fiber of a genuine zero-entry face.  Thus
positive common lifting is source-valid on that averaged boundary object,
although it is false for an arbitrary fixed unitary.

I also use the exact determinant-relevant P/R decomposition from
account01/B07 `MOC4-BIORIENTATION-PAIR-GATE-v1`: with `P=|U|^2`, the
middle exterior-power channel can be written in complementary-pair block
coordinates as

\[
D=\frac14E^TPE,\qquad R_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2,
\]

where `R` is doubly stochastic, and every real support functional has
nonconstant part `s=<D,K>+(1/2)<R,X>`.  This is a same-unitary identity,
not an independent-bistochastic replacement.

## 2. New theorem: a full all-compound lift on the order-four complex-Hadamard locus

For `|z|=1`, put

\[
U(z)=\frac12\begin{pmatrix}
1&1&1&1\\
1&z&-1&-z\\
1&-1&1&-1\\
1&-z&-1&z
\end{pmatrix},\qquad r=\Re z.
\tag{1}
\]

Permutations below are written in zero-based image notation
`pi(0)pi(1)pi(2)pi(3)`.  Define

\[
S_+=\{0231,0312,1203,1320,2013,2130,3021,3102\},
\tag{2}
\]

\[
S_-=\{0132,0213,1023,1302,2031,2310,3120,3201\}.
\tag{3}
\]

Define a probability law on `S_4` by

\[
\nu_z(\pi)=
\begin{cases}
(1+r)/16,&\pi\in S_+,\\
(1-r)/16,&\pi\in S_-,\\
0,&\text{otherwise}.
\end{cases}
\tag{4}
\]

### Theorem — `MOC4-COMPLEX-HADAMARD-COMMON-LIFT-v1`

For every `|z|=1`, every pair of subsets `I,J subset {0,1,2,3}` with
`|I|=|J|`, one has simultaneously

\[
\boxed{
|\det U(z)[I,J]|^2
=
\Pr_{\pi\sim\nu_z}\{\pi(J)=I\}.}
\tag{5}
\]

Consequently, for **every** complex spectra `a,b`, without simplicity or
nonsingularity assumptions,

\[
\boxed{
\det(D_a+U(z)D_bU(z)^*)
=\sum_{\pi\in S_4}\nu_z(\pi)
\prod_{j=0}^3(a_{\pi(j)}+b_j).}
\tag{6}
\]

Thus the Marcus-de Oliveira inclusion holds on this entire one-parameter
relative-eigenbasis family by an honest positive law using the **same
24 permutation states for every exterior degree**.

### Proof

Both `S_+` and `S_-` have eight elements, are disjoint, and each of their
uniform laws has every one-point marginal equal to `1/4`.  Hence (5) is
immediate for exterior degree `k=1`, and (4) is a probability law because
`|r|<=1`.

For `k=2`, every unnormalized `2 x 2` minor of the matrix `2U(z)` is,
up to a unimodular factor and sign, one of

\[
0,\quad 2,\quad 1+z,\quad 1-z.
\]

Therefore every squared normalized two-minor is one of

\[
0,\quad \frac14,\quad \frac{1+r}{8},\quad \frac{1-r}{8},
\tag{7}
\]

and in particular is affine in `r`.  At `r=+1`, direct inspection of the
36 pair events shows that the uniform law on `S_+` reproduces all of the
`2 x 2` squared minors of `U(1)`.  At `r=-1`, the uniform law on `S_-`
reproduces all of the `2 x 2` squared minors of `U(-1)`.  Since both the
minor side of (7) and the event probability under (4) are affine in `r`,
the equality holds for every `r in [-1,1]`, hence for every phase `z`.
The adjacent exact verifier performs the complete finite endpoint check.

For `k=3`, complementary-minor duality for a unitary gives

\[
|\det U[I,J]|^2=|\det U[I^c,J^c]|^2,
\]

while for every permutation the event `pi(J)=I` is equivalent to
`pi(J^c)=I^c`; therefore `k=3` follows from `k=1`.  Degrees `k=0,4` are
trivial.  This proves (5).

Finally Cauchy-Binet gives

\[
\det(D_a+UD_bU^*)=
\sum_{k=0}^4\sum_{|I|=|J|=k}
a_{I^c}b_J |\det U[I,J]|^2.
\]

Insert (5), interchange the finite sums, and expand by subsets for each
fixed permutation.  The inner sum is exactly
`prod_j(a_{pi(j)}+b_j)`, yielding (6).  No division by a spectral
quantity occurs, so singular and repeated spectra are included. `QED`

### Order-four complex-Hadamard corollary

The standard order-four classification says every `4 x 4` complex
Hadamard matrix is equivalent, under diagonal unitary row/column factors
and row/column permutations, to the one-parameter family (1).  One
reference is W. Tadej and K. Zyczkowski, *A concise guide to complex
Hadamard matrices*, Open Systems & Information Dynamics 13 (2006),
133--177, DOI `10.1007/s11080-006-8220-2`, summarizing the order-four
classification.  Diagonal phase factors do not change squared compound
minors, while row/column permutations only relabel the permutation law.
Hence (5)--(6) transport to **every 4 x 4 complex Hadamard relative
unitary**.

This closes a genuine positive-dimensional source-valid MOC4 class by the
strong common-minor mechanism requested in this assignment.

## 3. Second new result: canonical V4 gluing for the determinant-relevant P/R channels

The full all-minor lift above is special; dense true unitaries are already
known to violate even weaker anchored common-minor representations.  A
weaker representation is nevertheless enough for the determinant because
its structured middle-degree coefficient sees only the exact `(D,R)`
channels, with `D` fixed by the same `P`.

Let `rho:S_4 -> S_3` be the quotient action on the three complementary-pair
partitions; its kernel is the Klein four group `V_4`.  Choose any Birkhoff
decompositions

\[
P=\sum_{\pi\in S_4}\lambda_\pi P_\pi,
\qquad
R=\sum_{\rho\in S_3}\mu_\rho R_\rho,
\tag{8}
\]

and set the `P`-decomposition fiber totals

\[
\theta_\rho=\sum_{\pi:\rho(\pi)=\rho}\lambda_\pi.
\tag{9}
\]

Define

\[
\boxed{
\nu_\pi=\lambda_\pi+
\frac{\mu_{\rho(\pi)}-\theta_{\rho(\pi)}}4.}
\tag{10}
\]

### Theorem — `MOC4-V4-BIRKHOFF-GLUE-v1`

If all 24 numbers in (10) are nonnegative, then they are a probability law
and give an exact MOC4 determinant representation

\[
\det(D_a+UD_bU^*)=\sum_\pi\nu_\pi v_\pi
\tag{11}
\]

for all complex spectra `a,b`.

### Proof

Each quotient fiber is a coset of `V_4`, and `V_4` acts regularly on four
points.  Hence the uniform average of the four point-permutation matrices
in **every** quotient fiber is `J_4/4`.  The corrections in (10) have total
sum zero across the six fibers, so their contribution to the one-point
matrix is

\[
\sum_\rho (\mu_\rho-\theta_\rho)J_4/4=0.
\]

Therefore the law (10) still has one-point channel exactly `P`.  On the
other hand its total mass in quotient fiber `rho` is exactly `mu_rho`, so
its complementary-pair quotient channel is exactly `R`.  Consequently its
endpoint average has the same `D=(1/4)E^TPE` and the same `R` as the true
unitary.  The exact support decomposition `<D,K>+(1/2)<R,X>` therefore
agrees for every real-linear support functional and every spectra pair;
this is equivalent to the complex identity (11). `QED`

**Important scope distinction.**  The gluing theorem in this section is a
*determinant-relevant projected lift*.  For a general unitary it does not
claim that (10) reproduces every individual `2 x 2` squared minor.  The
all-compound statement (5) is stronger and was proved above only on the
complex-Hadamard locus (plus other separately established team classes).
This distinction is necessary because the team has exact dense
counterexamples to universal fixed-unitary common-minor lifting.

## 4. A spectra-independent interior certificate

Put

\[
p=\min_{i,j}P_{ij},\qquad q=\min_{\alpha,\beta}R_{\alpha\beta}.
\tag{12}
\]

Because `P` is `4 x 4` doubly stochastic,

\[
P=4p\,(J_4/4)+(1-4p)P'
\]

with `P'` doubly stochastic (with the endpoint case interpreted directly).
Choose a Birkhoff decomposition of `P'` and spread the uniform part over all
24 permutations.  This produces a decomposition in (8) with

\[
\lambda_\pi\ge p/6\quad\text{for all }\pi.
\tag{13}
\]

Similarly

\[
R=3q\,(J_3/3)+(1-3q)R'
\]

has a Birkhoff decomposition with

\[
\mu_\rho\ge q/2\quad\text{for all }\rho.
\tag{14}
\]

Every one of the five *other* V4 fibers has mass at least
`4(p/6)=2p/3`, hence for each fiber

\[
\theta_\rho\le1-\frac{10p}{3}.
\tag{15}
\]

Substituting (13)--(15) into (10),

\[
\nu_\pi\ge
\frac p6+\frac14\left(\frac q2-1+\frac{10p}{3}\right)
=p+\frac q8-\frac14.
\tag{16}
\]

Therefore:

### Corollary — `MOC4-PR-INTERIOR-CERTIFICATE-v1`

\[
\boxed{8p+q\ge2\quad\Longrightarrow\quad
\det(D_a+UD_bU^*)\in\operatorname{conv}\{v_\pi\}
\text{ for all complex }a,b.}
\tag{17}
\]

This is an individual-true-unitary certificate, independent of the spectra
and support direction.  For a complex Hadamard unitary `p=1/4`, so (17)
is automatic even when `q=0`; Section 2 is stronger there because it gives
the full compound-minor law.

## 5. Exact verification

`verify_hadamard_common_lift.py` uses only `fractions.Fraction` and exact
Gaussian-rational arithmetic.  It verifies all `k=0,1,2,3,4` compound
marginals for both endpoint laws and for the nontrivial phase

\[
z=\frac35+\frac45 i,
\]

where the 24 weights are exactly eight copies of `1/10`, eight copies of
`1/40`, and eight zeros.  For the generic Gaussian-integer test spectra

`a=(2+i,-1+3i,4-2i,-3-i)`,
`b=(1-2i,3+i,-2+2i,5-i)`,

it also independently checks

\[
\det(D_a+U(z)D_bU(z)^*)
=\sum_\pi\nu_z(\pi)v_\pi
=-\frac{466}{5}+\frac{143}{5}i.
\]

The finite endpoint check is part of the proof of the affine-in-`r`
identity, not a numerical experiment.

## 6. Application of the named partner result and updated conditional chain

The partner theorem `MOC4-ZERO-FIBER-HAAR-LIFT-v1` and the present theorem
cover complementary positive-lift mechanisms:

1. on a genuine zero-entry face, account02/B09 constructs an exact **Haar
   averaged** law matching every compound degree;
2. on the entire order-four complex-Hadamard locus, this run constructs an
   exact **individual-unitary** law matching every compound degree;
3. more generally, any true unitary satisfying `8p+q>=2` has an exact
   positive determinant representation through the same-unitary P/R glue.

Combining with the campaign lead, a hypothetical MOC4 counterexample may
therefore be chosen as a global support maximizer lying outside all these
closed classes.  In particular on the strict interior it must satisfy

\[
\boxed{8\min_{ij}|u_{ij}|^2+
\min_{\alpha\beta}R_{\alpha\beta}<2,}
\tag{18}
\]

in addition to the lead's positive V4/pair reserve, all pair-Rayleigh and
Cartan/Hessian stationarity constraints, the exact `D=(1/4)E^TPE`
compatibility, and the odd-Weyl/biorientation gates already established by
the team.

The first essential missing implication is now the following precise
maximizer-local gluing problem:

> **`MOC4-MAXIMIZER-V4-GLUE-v1` (OPEN).**  On the remaining positive-reserve
> global-maximizer branch with (18), prove that one can choose Birkhoff
> decompositions `(lambda,mu)` of the *same unitary's* `(P,R)` for which all
> 24 canonical glued weights (10) are nonnegative; or prove the support
> bound directly from the stationarity/odd-Weyl constraints before such a
> lift exists.  A failure is relevant only if realized by an actual unitary
> that is a genuine support maximizer for actual spectra; an arbitrary pair
> of bistochastic matrices or a generic dense common-lift no-go does not
> count.

If this implication holds, (11) contradicts a positive support gap and the
lead/boundary reductions complete MOC4.  Conversely, an actual source-valid
maximizer for which every such gluing fails is the correct object for the
next counterexample search.

## 7. Status and safeguards

- `MOC4-COMPLEX-HADAMARD-COMMON-LIFT-v1`: **proved** with an explicit
  24-state law reproducing every compound degree.
- Order-four complex-Hadamard relative-unitary MOC4 class: **closed**.
- `MOC4-V4-BIRKHOFF-GLUE-v1`: **proved** as an exact determinant-relevant
  sufficient condition.
- `MOC4-PR-INTERIOR-CERTIFICATE-v1`: **proved**.
- `MOC4-MAXIMIZER-V4-GLUE-v1`: **open**.
- Full MOC4: **open**.

No benchmark material, held-out keys, credentials, scheduler identifiers,
machine paths, unrelated private data, email/Drive data, public posting,
paid model/API/Codex call, remote workflow, or permission bypass was used.
