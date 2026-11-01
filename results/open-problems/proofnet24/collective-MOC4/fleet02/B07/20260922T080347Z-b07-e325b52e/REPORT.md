# MOC4 fleet02/B07 — exact mixed-Schur saturation manifold and double-saturation zero-face reduction

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T080347Z-b07-e325b52e`  
**Worker:** fleet02/B07  
**Assignment:** support-functional and second-variation estimates for the complex-normal `4 x 4` Marcus–de Oliveira target  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `MOC4-MSQR-LS-SATURATION-MANIFOLD-v1`  
**Parent target:** **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no benchmark material used.

## 1. Fresh authority and source-bound state

At invocation start I resolved `math-research-brain/main` to
`a983b52bc071cc0ec59ca37f06f7b681a66970be` and read all five required
live control entry files plus the collective ORDER/TARGETS/ASSIGNMENTS.
fleet02/B07 stop or pause was present.

Before the main scientific write I resolved fresh main again at
`9b0bf9927bf52384d2ce93a11fd1c68a379fab11`.  An exact commit comparison
from the start control commit to that head shows only concurrent research,
run, login, lease and handoff files changed; none of AGENTS.md,
scheduled_tasks/README.md, fleet.json, roles.json, PROTOCOL.md, ORDER.md,
TARGETS.md or ASSIGNMENTS.json changed.  Therefore the live authority used
below is still the same owner revision rather than cached permission.

Newest complete campaign-lead snapshot actually consumed:

- fleet03/B07 run `20260922T074824Z-fleet03-B07-MOC4-r13`,
  report blob `7724d19f793eb934c5fcc2b469bb9d0a108da4eb`,
  `MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1` and
  `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`.

Newest complete named-partner snapshot actually consumed:

- fleet03/B08 run `20260922T072320Z-fleet03-B08-MOC4-r12`,
  report blob `da2892a8a90526b2abdeecf897743fc5a51364e6`,
  `MOC4-GENERIC-FACET-LADDER-v1`.

Essential OTHER-account input used directly:

- fleet03/B20 run `20260922T064515Z-fleet03-B20-MOC4-r12`,
  report blob `69574583d7e7ade0aa97b0a03f79a9a7b2d216b9`,
  `MOC4-SPIN4-BIAFFINE-ORBIT-v1` and
  `MOC4-SPIN4-GLOBAL-TRUST-REGION-GATE-v1`;
- fleet03/B20 run `20260922T071802Z-fleet03-B20-MOC4-r12`,
  report blob `e37d1ae846af5e734e0051aad54aa1d7cb623ed6`,
  `MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1`.

The immediately preceding fleet02/B07 result is
`MOC4-MIXED-SCHUR-FULL-LS-CROSS-RESERVE-v1`: at pair Lyapunov–Schmidt
saturation, the remaining transverse cubic residual must vanish.  The lead
r13 independently sharpened that same local statement.  This run therefore
does **not** repeat another Schur-complement reserve calculation.  It asks
what exact genuine-unitary geometry pair-reserve saturation forces.

## 2. Conditional end-to-end position

Fix a real-linear support functional
\[
h(U)=\operatorname{Re}\left(\eta\det(D_a+UD_bU^*)\right)
\]
and suppose, for contradiction, that a true unitary global maximizer has
\[
h(U)=M+\gamma,\qquad \gamma>0,
\]
where \(M\) is the maximum of the same functional over the 24 permutation
vertices.

The current proof tree is:

1. Repeated-spectrum and singular determinant values do not require an
   inverse in the support/Cauchy–Binet formulation; the known genericization
   and pair-symmetrized boundary reductions remain available.
2. Elementary pair saturation is excluded at a positive-gap maximizer, so
   each scalar pair curvature is strict.
3. For each complementary Spin(4) block, either its mixed Hessian is
   negative definite or it reaches the mixed-Schur boundary.
4. On an MSQR boundary, fleet03/B20 identifies the exact pair
   Lyapunov–Schmidt reserve with the complete global trust-region condition
   on that **same genuine** `SU(2) x SU(2)` orbit.
5. The lead r13 shows that equality in the pair reserve forces annihilation
   of cross-Hessian couplings and, at full reserve saturation, zero
   transverse cubic residual.

The first branch that was still geometrically opaque was therefore **exact
pair-reserve equality**.  The theorem below integrates that local kernel
exactly.

## 3. Genuine Spin(4) normal form

On a complementary row-pair product orbit, fleet03/B20 proves that the
support is exactly
\[
f(n,m)=c+p\cdot n+q\cdot m+n^T Zm,\qquad n,m\in S^2,
\tag{1}
\]
with the north pole \(e=(0,0,1)\) representing the present unitary.  At a
positive-gap global maximizer,
\[
p+Ze=Ae,\qquad q+Z^Te=Be,\qquad A,B>0.
\tag{2}
\]
Write
\[
Z=\begin{pmatrix}M&r\\s^T&z_0\end{pmatrix}.
\tag{3}
\]

At the mixed-Schur boundary choose tangent singular bases so that
\[
M=\operatorname{diag}(\sqrt{AB},m),\qquad |m|\le\sqrt{AB}.
\tag{4}
\]
Write \(r=(r_1,r_2)\), \(s=(s_1,s_2)\) and
\(H=A+B-2z_0\).  Local maximality forces the kernel-cubic cancellation
\[
A r_1+\sqrt{AB}\,s_1=0,
\tag{5}
\]
so set
\[
r_1=\sqrt B\,\rho,\qquad s_1=-\sqrt A\,\rho.
\tag{6}
\]

Fleet03/B20's exact trust certificate then reduces to
\[
\begin{pmatrix}D&-E\\-E&C\end{pmatrix}\succeq0,
\tag{7}
\]
where
\[
D=AB-m^2,\qquad
E=A r_2+m s_2,\qquad
C=A(H-\rho^2)-s_2^2.
\tag{8}
\]

The key point for this run is to retain the *unsimplified quadratic on the
sphere*.  In Bloch coordinates \(n=(x,y,z)\), its squared trust gap is
\[
\Phi(n)
 =D y^2+2E\,y(1-z)+C(1-z)^2.
\tag{9}
\]
On \(S^2\), the inherited sign condition makes
\(\Phi(n)=0\) equivalent to equality in the actual, unsquared support
inequality after maximizing over the complementary factor \(m\).

No determinant inverse appears in (1)-(9).

## 4. New theorem: simple mixed-Schur saturation is an exact circle of global maxima

Assume first
\[
D>0
\]
(the second tangent singular value is strictly below the top one).  Pair
Lyapunov–Schmidt saturation is exactly
\[
DC=E^2.
\tag{10}
\]
Substituting (10) into (9) gives the exact factorization
\[
\boxed{
\Phi(n)
 =D\left(y+\frac{E}{D}(1-z)\right)^2.
}
\tag{11}
\]

Therefore the projected equality set is not merely a formal Hessian kernel:
it is the complete circle
\[
\boxed{
\mathcal C_k=
\{(x,y,z)\in S^2:\ y=-k(1-z)\},\qquad
k=\frac ED.
}
\tag{12}
\]

The plane in (12) has distance
\[
\frac{|k|}{\sqrt{1+k^2}}<1
\]
from the origin, so it always cuts \(S^2\) in a genuine circle.  Its center
and squared radius are
\[
c_k=
\left(0,-\frac{k}{1+k^2},\frac{k^2}{1+k^2}\right),
\qquad
R_k^2=\frac{1}{1+k^2}.
\tag{13}
\]
The north pole belongs to the circle.

For every \(n\in\mathcal C_k\), the exact product-orbit maximum over the
second sphere equals \(f(e,e)\).  Wherever the denominator is nonzero the
corresponding maximizing second factor is explicitly
\[
\boxed{
m(n)=\frac{q+Z^Tn}{L-p\cdot n},
\qquad
L=p_3+B,
}
\tag{14}
\]
because equality gives
\(\|q+Z^Tn\|=L-p\cdot n\).  At an exceptional point where numerator and
denominator both vanish, take the continuous limiting maximizing factor (or
any maximizing sphere point).

Hence every point
\[
(n,m(n)),\qquad n\in\mathcal C_k,
\tag{15}
\]
is a **genuine-unitary global support maximizer** with the same positive gap
\(\gamma\).  This is an exact one-dimensional family inside the real
unitary orbit, not a bistochastic or independently assigned compound-minor
family.

Near the north pole, the sphere and (12) give
\[
y=-\frac{k}{2}x^2+O(x^4).
\tag{16}
\]
Thus the Lyapunov–Schmidt quadratic correction is literally the curvature
of the exact equality circle; the local kernel direction has been
integrated to a global same-orbit maximizer family.

### Consequence for cross-split stationarity

Because each point in (15) is a global maximizer of the **full** support
functional on \(U(4)\), every transverse root and Cartan first derivative
vanishes at every point of this circle.  The lead's local
cross-block-annihilation and cross-residual-zero conditions are therefore
the first Taylor coefficients of an exact one-parameter family of full
stationarity identities.

This is strictly stronger information than the pair-only LS scalar
inequality.  In particular, on an arc where (14) is regular, the remaining
source-structured stationarity equations may be pulled back to one real
circle parameter; after clearing the explicit positive denominator they
become finite algebraic identities in the same spectral/minor data.  That
is the concrete next target, rather than another same-pair trust
optimization.

## 5. New theorem: double mixed saturation reaches the zero-entry boundary exactly

Now suppose the second mixed singular value also saturates:
\[
m=\varepsilon\sqrt{AB},\qquad \varepsilon\in\{+1,-1\}.
\tag{17}
\]
Then \(D=0\).  Positivity of (7) forces
\[
E=0,
\tag{18}
\]
and fleet03/B20's double-kernel cubic relation lets us write
\[
r_2=\sqrt B\,\rho_2,\qquad
s_2=-\varepsilon\sqrt A\,\rho_2.
\tag{19}
\]
Exact pair-LS saturation is
\[
H=\rho^2+\rho_2^2.
\tag{20}
\]
Consequently
\[
C=A(H-\rho^2)-s_2^2
 =A\rho_2^2-A\rho_2^2=0.
\tag{21}
\]
Thus
\[
\boxed{\Phi(n)\equiv0\quad\text{on all of }S^2.}
\tag{22}
\]

So for **every** first-pair Bloch direction \(n\), there is a complementary
second-pair factor giving exactly the same global support value.

This has a source-valid boundary consequence.  Let the first embedded
`SU(2)` act on rows \(i,j\), and choose a column \(c\) for which
\[
w=(U_{ic},U_{jc})^T\ne0.
\]
Such a column exists because the two rows have total squared norm two.  Put
\(w=(\alpha,\beta)^T\), \(r=(|\alpha|^2+|\beta|^2)^{1/2}\), and define
\[
G=\frac1r
\begin{pmatrix}
\overline\alpha&\overline\beta\\
-\beta&\alpha
\end{pmatrix}.
\tag{23}
\]
Then \(G\in SU(2)\) and
\[
Gw=(r,0)^T.
\tag{24}
\]
Equation (22) allows the Bloch class of this exact \(G\).  Choose the
corresponding maximizing element in the complementary disjoint
`SU(2)` factor.  That second factor acts only on the other row pair and
therefore does not disturb the zero created in (24).

We have proved:

> **Double-saturation zero-face reduction.**  
> If a positive-gap genuine global MOC4 support maximizer reaches a
> complementary mixed-Schur block with both tangent singular values
> saturated **and** its pair Lyapunov–Schmidt reserve is saturated, then
> the same genuine unitary product orbit contains an equal-support global
> maximizer with a zero matrix entry.

This does **not** claim the zero-entry support branch is solved.  The
campaign has explicitly recorded `MOC4-ZERO-FACE-SUPPORT-v1` as a separate
unpaid source-structured inequality after the older common-permutation-lift
shortcut was refuted.  What is new is that the double mixed-Schur
pair-saturation branch is no longer an independent interior branch: it
lands exactly on that existing zero-face obligation.

The identical argument applies to a complementary right product orbit,
with columns and rows interchanged.

## 6. Singular determinant and repeated-spectrum safety

The derivation uses only:

- the Cauchy–Binet/squared-minor support expression,
- true embedded `SU(2)` row or column actions,
- finite-dimensional quadratic identities, and
- the global support maximum.

It never divides by \(\det(D_a+UD_bU^*)\), an eigenvalue gap, or a matrix
inverse.  Therefore determinant-zero points are included without a limiting
argument.

No spectral simplicity is used in the saturation-manifold theorem itself.
When a repeated spectrum supplies additional invariance, the theorem
continues to hold; the campaign's separate repeated-spectrum reductions may
be applied before or after it.  This report does not re-claim those peer
theorems.

## 7. Application of the named partner result

The named partner fleet03/B08
`MOC4-GENERIC-FACET-LADDER-v1` constructed an exact true-unitary,
complex-spectrum near-facet stress datum with a very small positive support
distance to one target face, then found a sixth genuine pair move that
strictly improves support.  I use that result here as a hard guardrail:

- tiny target-face distance does **not** approximate the branch treated by
  this theorem;
- the equality-circle conclusion requires an actual global maximizer,
  exact pair stationarity, the mixed-Schur boundary, and exact pair-LS
  saturation;
- B08's stress datum fails before those hypotheses and is therefore not a
  candidate saturation witness.

Any computational attack on the new residual must impose exact pair
stationarity/saturation first rather than search merely for near-hull
points.

## 8. First essential remaining implication

The pair-saturated MSQR branch now splits cleanly.

1. **Double mixed singular value:** reduced by Section 5 to the existing
   zero-entry support branch.
2. **Simple mixed singular value:** carries the exact maximizer circle
   \(\mathcal C_k\) and the explicit complementary maximizer map (14).
3. **Positive pair-LS slack:** remains the lead's cross-split reserve
   payment problem rather than a saturation problem.
4. **All pair blocks negative definite:** remains the separate NDI branch.

The first new implication for this worker is therefore:

> **`MOC4-MSQR-EQUALITY-CIRCLE-RIGIDITY-v1` (OPEN).**  
> For arbitrary complex spectra and a real support direction, let a
> genuine positive-gap global maximizer have a *simple* mixed-Schur pair
> block with exact pair-LS saturation.  Along its exact circle
> \(\mathcal C_k\), impose the same-unitary determinant structure and all
> full left/right transverse stationarity equations.  Prove that these
> identities force a zero-entry/common-block boundary or target support
> safety.  Alternatively construct actual complex spectra and a true
> unitary for which the whole equality circle consists of positive-gap
> global maximizers and all transverse conditions hold.

This is narrower than the previous local
`MOC4-CROSS-SPLIT-CUBIC-PAYMENT-v1`: the saturation subbranch has been
converted from one kernel vector with a pseudoinverse reserve into an exact
one-dimensional manifold of true global maxima.

A practical next calculation is to substitute the rational map (14) into
one transverse root derivative, clear its denominator, and use vanishing
on all of \(\mathcal C_k\) to force its coefficient identities.  The
zero-face identity should be tested as the first possible factor.

## 9. Exact self-check

The companion standard-library exact checker verifies the factorization
geometry, a nontrivial rational point on the simple equality circle, the
double-saturation identically-zero trust gap, and the Gaussian-integer
numerator in the explicit `SU(2)` zeroing map.

Exact executed output:

```text
PASS MOC4-MSQR-LS-SATURATION-MANIFOLD-v1
simple_sample_n = (8/9,-4/9,1/9)
simple_Q = 0
simple_k = 1/2
simple_radius_squared = 4/5
double_saturation_Q_identically_zero = True
SU2_zeroing_second_coordinate_numerator = 0
```

The code is `verify_msqr_saturation_manifold.py`.  The separate output-file
commit was attempted but the connector safety layer declined that write;
the exact successful execution output is preserved above instead.  This
checker validates only the stated algebraic identities, not the remaining
MOC4 rigidity implication.

## 10. Honest status

- `MOC4-MSQR-LS-SATURATION-MANIFOLD-v1`: **PROVED** from the exact genuine
  Spin(4) trust normal form.
- Double mixed + pair-LS saturation -> equal-support zero-entry global
  maximizer: **PROVED**.
- `MOC4-MSQR-EQUALITY-CIRCLE-RIGIDITY-v1`: **OPEN**.
- Zero-entry support branch: **OPEN** in the campaign state used here.
- NDI branch: **OPEN**.
- Full MOC4: **OPEN / NOT PROVED / NOT DISPROVED**.
- No arbitrary bistochastic surrogate, independent compound-minor
  assignment, benchmark gold, paid model/API/Codex, email, Drive, public
  posting, credentials, scheduler identifiers, machine paths, or unrelated
  private transcript was used.
