# MOC4 account01/B09 — simple-complex spectrum adversary to the universal even-channel lift

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T024937Z-account01-B09-MOC4-r12`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Assignment:** construct genuine unitary/spectrum adversaries to proposed coefficient representations; representation failure alone is not a target counterexample  
**Outcome:** `CANDIDATE_REFUTED` for `MOC4-SIMPLE-COMPLEX-EVEN-LIFT-v1`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and current conditional chain

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for every complex normal `4 x 4` pair, including singular and repeated-spectrum cases.

The latest complete lead snapshot consumed is account03/B07 `MOC4-ZERO-ENTRY-COMMON-LIFT-v1` (report blob `47f09f9f722aa8501330ca532a2ca261474c681c`): a common permutation lift is false even on a genuine zero-entry unitary face, so the zero-face branch must be handled at the structured support level. The named OTHER-account result applied directly is account02/B07 `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1` / `MOC4-PAIR-HESSIAN-TRACE-v1` (report blob `6aaccfff6d9b75e67e706c211eadbfe1fee7a78a`): equality in any odd-Weyl overlap constraint forces the complete exterior-square channel array into the convex hull of the 24 even endpoint arrays; a positive support violator therefore has all odd-overlap inequalities quantitatively strict and, at a local support maximum, satisfies the pair-Hessian condition. I also use account01/B08's immediately preceding exact facet refutation `MOC4-BOGOLIUBOV-EVEN-LIFT-v1`, whose true-unitary witness and facet are reproduced independently below.

Thus a compact surviving end-to-end route is: assume MOC4 fails; separate by a real support direction and choose a global true-unitary maximizer; reduce pair-flat points to the zero-entry branch, while a pair-strict maximizer satisfies the exact row/column Rayleigh and Spin(6) stationarity equations; account02/B07 removes every odd-overlap equality face; then one must prove the structured support bound in the remaining strict interior (or close the zero-entry branch directly). The first essential unpaid inference remains maximizer-local, currently expressible as `MOC4-STRICT-ORIENTATION-BIRAYLEIGH-v1` / `MOC4-STATIONARY-FACET-PAYMENT-v1`, not as an unconditional positive coefficient lift.

## 2. Stronger coefficient representation tested

For an actual unitary `U`, let `O=Lambda^2 U in SO(6)` in the complementary-pair basis `(12,34 | 13,-24 | 14,23)`. In each `2 x 2` block write the real map as `z -> m z+n zbar` and put

\[
q^+_{\alpha\beta}=|m_{\alpha\beta}|^2,\qquad q^-_{\alpha\beta}=|n_{\alpha\beta}|^2.
\]

The 24 permutation endpoints give the 24 even coloured matching arrays. A universal positive even-channel lift would assert that every actual `q=(q^+,q^-)` lies in their convex hull. Account01/B08 refuted this by an exact facet. The present run strengthens the refutation to an explicit **simple genuinely complex spectral pair** and, crucially, simultaneously gives an exact certificate that the true determinant is strictly inside the desired MOC4 hull.

## 3. Exact genuine unitary and simple complex spectra

Take the rational orthogonal matrix

```text
U =
[  636/1105,  -423/1105,   -12/65,   -772/1105 ]
[ 3576/5525,    332/5525, -144/325,  3411/5525 ]
[   164/425,     348/425,      9/25,    -96/425 ]
[      27/85,       -36/85,       4/5,       24/85 ] .
```

Exact arithmetic verifies `U^T U=I`, `det U=1`, every entry is nonzero, and all 36 two-by-two minors are nonzero. Choose

\[
a=(-4+4i,-i,-3+2i,-4-4i),
\]
\[
b=(-4-4i,2-i,2-4i,4-i).
\]

Both spectra are simple and every spectral value is nonreal. With
`A=diag(a)` and `B=U diag(b)U^T`, both matrices are complex normal and

\[
\det(A+B)=\frac{-82603754544-3513801072 i}{763140625}.
\tag{1}
\]

All 24 target permutation products are distinct for these spectra.

## 4. Exact target-hull certificate

For the three permutations

\[
\sigma_1=(0,1,2,3),\quad
\sigma_2=(0,1,3,2),\quad
\sigma_3=(0,3,1,2),
\]

using zero-based tuple notation for the images, the target vertices are

\[
z_1=80-240i,\qquad z_2=64+256i,\qquad z_3=-416-32i.
\]

Set

\[
w_1=\frac{1442439283}{4637546875},\qquad
w_2=\frac{57833177464}{180864328125},\qquad
w_3=\frac{66776018624}{180864328125}.
\]

Exact arithmetic gives `w_j>0`, `w_1+w_2+w_3=1`, and

\[
\det(A+B)=w_1z_1+w_2z_2+w_3z_3.\tag{2}
\]

The doubled signed area of this triangle is `242688 != 0`. Since all three barycentric weights are strictly positive, (1) lies in the two-dimensional interior of this triangle, hence in the interior of the full MOC4 target hull. This datum is therefore emphatically **not** a counterexample to MOC4.

## 5. Yet no positive even-channel coefficient lift exists

For `R=q^++q^-` and `D=q^+-q^-`, reproduce the account01/B08 facet

\[
\Phi=R_{11}-R_{12}+3D_{13}+3D_{21}+R_{22}-R_{23}-R_{31}-3D_{32}+R_{33}.
\]

Every one of the 24 even endpoint arrays obeys `Phi<=3`; exact enumeration gives only `3,-3,-9`. For the actual exterior-square channel array of the displayed `U`,

\[
\Phi(q(U))=\frac{2403485709}{763140625}
=3+\frac{114063834}{763140625}>3.\tag{3}
\]

Hence **no probability law on the 24 permutation endpoints can reproduce the true channel array**. Moreover, the three permutation vertices used in the exact determinant certificate (2) all lie on the tight channel facet `Phi=3`. Consequently their same convex weights give channel-facet value exactly `3`, while the true channel array remains outside by the positive rational gap in (3). Thus the successful target-hull certificate is not secretly a coefficient/channel lift.

This directly answers the B09 assignment at the source-valid level: failure of the proposed coefficient representation persists for a dense true unitary and simple complex spectra even when the actual determinant is rigorously, strictly inside the desired convex hull.

## 6. Direct application of the named OTHER-account result

Account02/B07 `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1` proves that equality in **any** odd-Weyl overlap inequality forces the complete `q` array into the convex hull of the 24 even endpoint arrays. Equation (3) proves the present `q(U)` is outside that convex hull. Therefore, by contraposition, **all odd-overlap inequalities are strict for this exact unitary**.

So this adversary is not an artifact of an odd-orientation boundary face. It lives in the strict-orientation interior singled out by the partner result. The obstruction is genuinely the lack of a universal positive endpoint representation, while the target determinant can still be safely inside its hull.

## 7. Consequence for the full proof architecture

`MOC4-SIMPLE-COMPLEX-EVEN-LIFT-v1` is refuted. This also rules out any proof whose decisive universal step is that the actual exterior-square channel masses themselves form a convex combination of the 24 target endpoint masses, even after restricting attention to simple nonreal spectra and dense unitaries.

It does **not** refute MOC4. The remaining viable chain must use the fact that a hypothetical target violation is attained at a structured support **maximizer**, not merely at an arbitrary actual unitary. In particular the next useful adversarial task is to test `MOC4-STATIONARY-FACET-PAYMENT-v1`: can an actual global/local maximizer satisfying the row/column bi-Rayleigh and Spin(6) stationarity equations point outward through a facet such as `Phi`, or do those maximizer equations force compensation in the structured spectral support? The fresh account02/B09 `MOC4-CARTAN-POLARIZATION-v1` collar further restricts a surviving violator away from zero/common-block entry faces unless a zero-entry endpoint itself violates the target.

The present result supplies a clean negative control for that maximizer-local program: any future argument that would also forbid this nonstationary/simple-complex datum is still too strong.

## 8. Exact verification and provenance

`verify_simple_complex_even_lift_nogo.py` uses only Python's standard library and exact `Fraction` arithmetic. It checks orthogonality/determinant/nonzero minors of `U`; simplicity and genuine complexity of both spectra; the exact determinant; all 24 distinct target vertices; the positive three-vertex barycentric certificate and nonzero triangle area; all 24 channel-facet endpoint values; and the exact positive facet gap (3). Captured output is in `VERIFICATION.txt`.

Inputs applied: account02/B07 `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1`; account03/B07 `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`; account01/B08 `MOC4-BOGOLIUBOV-EVEN-LIFT-v1` facet witness; and the current account02/B09 Cartan-collar handoff for the next-step architecture. No benchmark material, credentials, scheduler identifiers, machine-local data, email/Drive data, paid model/API, Codex, remote workflow or public release was used.
