# MOC4 account01/B09 — dense true-unitary no-go for a minimal anchored coefficient lift

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T035002Z-b09-moc4-r11`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Assignment:** construct genuine unitary/spectrum adversaries to proposed coefficient representations; a representation failure is not a target counterexample  
**Outcome:** `CANDIDATE_REFUTED` for `MOC4-DENSE-ANCHOR-MARGINAL-LIFT-v1`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Current proof state and conditional end-to-end chain

The source-exact target is

\[
\det(A+B)\in\operatorname{conv}\left\{
 \prod_{r=0}^3(a_r+b_{\sigma(r)}):\sigma\in S_4
\right\}
\tag{MOC4}
\]

for every pair of complex normal `4 x 4` matrices, including repeated spectra and singular sums.

The newest complete campaign-lead state consumed is account03/B07
`MOC4-V4-PAIR-GAP-CEILING-v1`, report blob
`28cbce0f0a6213c0760e0777a5baa5b0de12b31a`. It proves a genuine
`V_4` fiber roof and, together with pair-specific roofs, confines every
support violation of gap `gamma` to

\[
0<\gamma\le \frac{\mathcal R}{4},\qquad
\mathcal R=3d-\Delta-\frac G2,
\]

on endpoint configurations where the reserve is positive. The lead's
first unpaid implication is `MOC4-RESIDUAL-PR-RESERVE-v1`: use
same-unitary compatibility plus maximizer stationarity/Cartan constraints
to eliminate that residual branch.

The assigned partner account02/B07's current complete result
`MOC4-ONE-CYCLE-NORMAL-CONE-v1`, report blob
`0c82b0d30738d20a146e52abb4b7ba8e410f128c`, gives a finite exact
copositivity criterion for every support direction on a genuine closing
`SU(2)` orbit. I also use its earlier source-exact
`MOC4-BIRAYLEIGH-ORBIT-v1`: at a global support maximizer every genuine
row/column pair orbit has zero first derivative and satisfies the
corresponding top-Rayleigh condition.

Thus a compact surviving route is:

1. separate a hypothetical MOC4 failure by a real support direction and
   choose a genuine global unitary maximizer;
2. use the lead's `V_4`/pair roofs to close all nonpositive-reserve
   endpoint configurations and localize the rest;
3. use the exact pair-Rayleigh, Cartan and same-unitary compatibility
   equations in the positive-reserve branch;
4. prove the residual support bound; then continuity returns repeated and
   singular cases.

The present run attacks a tempting shortcut inside step 3: perhaps the
actual first exterior-power marginals and only nine anchored second
exterior-power marginals already come from one probability law on
`S_4`. That statement is much weaker than a full compound-minor common
lift. It is nevertheless false on a dense genuine unitary.

## 2. A universal 24-state inequality for the proposed projected lift

For a permutation `sigma in S_4`, define

\[
\ell(\sigma)=
1_{\sigma(1)=3}+1_{\sigma(2)=1}+1_{\sigma(3)=2}
-1_{\sigma(1)=2}-1_{\sigma(2)=3}-1_{\sigma(3)=1}.
\tag{1}
\]

For `i,j in {1,2,3}` put

\[
(c_{ij})=
\begin{pmatrix}
0&2&1\\
1&0&2\\
2&1&0
\end{pmatrix}.
\tag{2}
\]

Then every one of the 24 permutations satisfies the pointwise inequality

\[
\boxed{
\ell(\sigma)+
\sum_{i,j=1}^3c_{ij}
 1_{\{\sigma(0),\sigma(i)\}=\{0,j\}}
\ge0.}
\tag{3}
\]

This directly extends account04/B09
`MOC4-ZERO-ANCHOR-MARGINAL-LIFT-v1`. If `sigma(0)!=0`, there is exactly
one anchored event in (3), and the peer's 18-state inequality applies.
If `sigma(0)=0`, the three anchored events reduce to
`j=sigma(i)`; checking the six permutations of `{1,2,3}` gives values

\[
0,3,3,3,6,3,
\]

so (3) also holds on the six states excluded by the zero-entry argument.
The exact verifier independently enumerates all 24 states and obtains
the multiset

\[
0^{\times13},\quad3^{\times10},\quad6^{\times1}.
\tag{4}
\]

Consequently, if a probability law `lambda` on `S_4` reproduces

\[
P_{rc}=\Pr_\lambda[\sigma(r)=c]
\tag{5}
\]

and only the nine anchored two-set marginals

\[
Q_{ij}=\Pr_\lambda[\sigma(\{0,i\})=\{0,j\}],
\qquad i,j\in\{1,2,3\},
\tag{6}
\]

then expectation in (3) forces

\[
\boxed{
P_{13}+P_{21}+P_{32}-P_{12}-P_{23}-P_{31}
+2Q_{12}+Q_{13}+Q_{21}+2Q_{23}+2Q_{31}+Q_{32}\ge0.}
\tag{7}
\]

This is a necessary inequality for the projected positive coefficient
representation. It is not an MOC4 inequality.

## 3. Dense genuine orthogonal violation

Take the exact rational orthogonal matrix

\[
U=\begin{pmatrix}
-656/21025&2433/3625&2688/4205&-1356/3625\\
-5856/47125&-192/325&35733/47125&16/65\\
35733/47125&16/65&5856/47125&192/325\\
2688/4205&-1356/3625&656/21025&-2433/3625
\end{pmatrix}.
\tag{8}
\]

Exact arithmetic gives

\[
UU^T=I,\qquad\det U=-1.
\tag{9}
\]

Every one of its 16 entries and every one of its 36 two-by-two minors is
nonzero, so the obstruction is not a zero-entry or vanishing-minor face.

Set the actual unitary marginals

\[
P_{rc}=|u_{rc}|^2,\qquad
Q_{ij}=\left|\det U[\{0,i\},\{0,j\}]\right|^2.
\tag{10}
\]

For this true unitary, the first line of (7) is

\[
-\frac{1758848358993}{1867663890625},
\]

while the anchored two-set cost is

\[
\frac{1088931150054849}{1167289931640625}.
\]

Their sum is

\[
\boxed{
-\frac{10349074315776}{1167289931640625}<0.}
\tag{11}
\]

Hence no probability law on the 24 permutations can reproduce even the
singleton marginals and these nine anchored two-set marginals of this
dense true unitary.

This refutes `MOC4-DENSE-ANCHOR-MARGINAL-LIFT-v1`. In particular it
rules out any stronger universal common-permutation coefficient
representation that would imply (5)-(6).

## 4. Genuine simple complex spectra and exact target-hull certificate

To make the adversary source-valid at the matrix/spectrum level, take

\[
a=(-4+4i,-i,-3+2i,-4-4i),
\]

\[
b=(-4-4i,2-i,2-4i,4-i).
\tag{12}
\]

Both spectra are simple and every spectral value is nonreal. With

\[
A=D_a,\qquad B=UD_bU^T,
\]

both matrices are complex normal and exact arithmetic gives

\[
D:=\det(A+B)=
-\frac{339555707994799046}{2244788330078125}
+
\frac{1180709302197143977}{29182248291015625}i.
\tag{13}
\]

All 24 target permutation products are distinct. Three of them are

\[
z_{0123}=80-240i,\qquad
z_{0132}=64+256i,\qquad
z_{0213}=-280+120i.
\tag{14}
\]

Define

\[
w_1=\frac{54558530528515739941}{210112187695312500000},
\]

\[
w_2=\frac{478548274942418793}{4669159726562500000},
\]

\[
w_3=\frac{67009492397193957187}{105056093847656250000}.
\tag{15}
\]

Then `w_1,w_2,w_3>0`, `w_1+w_2+w_3=1`, and

\[
\boxed{D=w_1z_{0123}+w_2z_{0132}+w_3z_{0213}.}
\tag{16}
\]

The doubled area of the triangle in (14) is exactly `172800`, so it is
nondegenerate. Therefore (13) lies strictly inside that target triangle
and hence inside the full MOC4 hull.

Thus (11) is emphatically **not** a Marcus-de Oliveira counterexample:
the projected coefficient representation fails while the actual target
containment has an exact strict certificate on the same simple-complex
datum.

## 5. Direct application of the account02/B07 pair-Rayleigh theorem

Take support direction `eta=1`, i.e. real part, and rotate columns `0,3`
through the genuine orthogonal one-parameter subgroup with infinitesimal
generator `K_03=1`, `K_30=-1`. Differentiating the exact determinant
without an inverse gives

\[
\left.\frac{d}{dt}\right|_{t=0}
\Re\det(D_a+Ue^{tK}D_be^{-tK}U^T)
=
\frac{3697747106152704}{6939892578125}\ne0.
\tag{17}
\]

By account02/B07 `MOC4-BIRAYLEIGH-ORBIT-v1`, a global support maximizer
must be stationary on every such pair orbit. Therefore this dense
coefficient-lift adversary is **not** a support maximizer in the
`eta=1` direction.

That is exactly the distinction needed for the current proof
architecture: universal positive coefficient lifting is too strong,
but maximizer-local geometry is not refuted. The latest account02/B07
normal-cone theorem and the lead's positive-reserve reduction are
therefore compatible with this no-go.

## 6. Consequence and first remaining implication

The new result closes another possible coefficient shortcut:

> Even away from zero-entry and vanishing-minor faces, one cannot
> represent simultaneously the true `k=1` unistochastic marginals and
> only nine anchored `k=2` squared-minor marginals by one positive law on
> `S_4`.

Therefore the positive-reserve branch in
`MOC4-RESIDUAL-PR-RESERVE-v1` cannot be discharged merely by upgrading
the lead's same-unitary compatibility to this projected classical
matching law. Any successful proof has to use support-specific
structure at a maximizing unitary: pair-Rayleigh stationarity, Cartan
curvature, the `V_4`/pair roofs, the exact `P-R-D` compatibility and
odd-Weyl constraints, or an equivalent mechanism.

The first essential unpaid implication remains the lead's
`MOC4-RESIDUAL-PR-RESERVE-v1`: when the endpoint reserve is positive,
exclude a genuine common-unitary support maximizer with positive gap,
or produce an actual true-unitary/spectrum target counterexample.
Equation (17) shows the present dense no-go witness is a negative
control, not such a counterexample.

## 7. Exact verification and provenance

`verify_dense_anchor_lift.py` uses only exact
`fractions.Fraction` arithmetic and finite permutation enumeration. It
checks (9), density of all entries/minors, the 24-state inequality, the
exact negative gap (11), simple nonreal spectra, the determinant (13),
all 24 distinct target vertices, the positive barycentric certificate
(16), and the nonzero pair derivative (17).

No arbitrary bistochastic surrogate is promoted to a true-unitary
claim. No benchmark material, held-out answer, credential, scheduler
identifier, machine-local data, unrelated private data, email/Drive
data, public posting, paid model/API/Codex call, remote workflow or
permission change was used.

**Status:** `MOC4-DENSE-ANCHOR-MARGINAL-LIFT-v1 = REFUTED`; full MOC4
remains **OPEN**.
