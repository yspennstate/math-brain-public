# MOC4 account02/B09 r15 — Cartan/standard-channel transport defect

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Target:** complex-normal `4 x 4` Marcus–de Oliveira  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh state actually used

The newest complete campaign-lead report present during this run is **account03/B07**, run `20260922T043708Z-account03-B07-MOC4-r11`, `MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`. It proves exact transposition-subgroup roofs/cubature and leaves the positive residual `MOC4-SUBGROUP-RESIDUAL-STATIONARITY-v1`: exclude a positive-gap genuine global maximizer after imposing the endpoint subgroup roofs, bidirectional pair roofs, same-unitary compatibility, stationarity and Cartan/Hessian constraints.

The named OTHER-account result applied directly is **account04/B09**, run `20260922T041453Z-b09-moc4-r34`, report blob `faaf77b4fcebb8fed6a6c9763251acc1042105ac`, `MOC4-STANDARD-CHANNEL-CEILING-v1`. With endpoint supports `H_sigma`, Klein-fiber means `B_rho`,

\[
M=\max H_\sigma,\qquad m=\frac1{24}\sum H_\sigma,\qquad d=M-m,
\]
\[
Q=\max B_\rho,\qquad \Delta=M-Q,\qquad
\kappa_\sigma=H_\sigma-B_{\rho_\sigma},\qquad K=\max\kappa_\sigma,
\]
it proves for the actual unistochastic `P=(|u_ij|^2)` that every Birkhoff decomposition `P=sum lambda_sigma P_sigma` satisfies

\[
k(U)=\sum_\sigma\lambda_\sigma\kappa_\sigma,
\tag{1}
\]
so a support violation `h(U)=M+gamma` obeys `k>=gamma+Delta` and `gamma<=K-Delta`.

I also use the exact Cartan one-entry polarization from this worker's r13 and the pair-Hessian identity/positivity used by account01/B07: at a global maximizer, for each entry `(i,j)` there is a genuine CS path to the `3+1` common-block endpoint with

\[
h(t)=h(c)-\Gamma_{ij}(t-c)^2,\qquad c=|u_{ij}|,
\tag{2}
\]
while the negative pair Hessian is positive semidefinite and has trace `8T`, where

\[
T=3(d+\gamma)-k.
\tag{3}
\]
No arbitrary bistochastic middle compound is substituted for the true unitary.

## 2. New transport-defect theorem

Assume first that the standard endpoint maximum `K` is attained at a unique permutation `sigma_*`. Define Hamming distance

\[
d_H(\sigma,\sigma_*)=|\{i:\sigma(i)\ne\sigma_*(i)\}|
\]
and the exact standard transport slope

\[
\boxed{
c_*:=\min_{\sigma\ne\sigma_*}
\frac{K-\kappa_\sigma}{d_H(\sigma,\sigma_*)}>0.
}
\tag{4}
\]

### Theorem A — `MOC4-STANDARD-HAMMING-DEFECT-v1`

For every true unitary,

\[
\boxed{
K-k(U)\ge c_*\sum_{i=0}^3\bigl(1-P_{i,\sigma_*(i)}\bigr).
}
\tag{5}
\]

**Proof.** Use any Birkhoff decomposition in (1). Then

\[
K-k=\sum_\sigma\lambda_\sigma(K-\kappa_\sigma)
\ge c_*\sum_\sigma\lambda_\sigma d_H(\sigma,\sigma_*).
\]
The expected Hamming distance is exactly

\[
\sum_i\Pr\{\sigma(i)\ne\sigma_*(i)\}
=\sum_i(1-P_{i,\sigma_*(i)}),
\]
which proves (5). The right side is decomposition-independent. `QED`

Thus the standard-channel reserve is not only bounded by its largest endpoint: it must pay quantitatively for moving the **same** first-compound matrix `P` away from the unique maximizing permutation.

## 3. Common-block roofs turn Hessian trace into an entrywise collar

For every edge `(i,j)`, put

\[
M_{ij}:=\max_{\sigma:\sigma(i)=j}H_\sigma,
\qquad \beta_{ij}:=M-M_{ij}\ge0.
\tag{6}
\]

The `t=1` endpoint of the exact Cartan path (2) is a `3+1` common block pairing `a_i` with `b_j`. The known `n=3` theorem therefore gives the **sharper** endpoint roof `h(1)<=M_ij`, not merely `h(1)<=M`. Hence at a positive-gap global maximizer,

\[
\Gamma_{ij}(1-c)^2=h(c)-h(1)\ge\gamma+\beta_{ij}.
\tag{7}
\]

The radial pair-Hessian curvature in the corresponding unit tangent direction is

\[
A_{ij}=2\Gamma_{ij}(1-c^2).
\tag{8}
\]
Because the full negative pair Hessian `A` is positive semidefinite and has trace `8T`, every unit-direction curvature obeys `A_ij<=8T`. Combining (7)-(8),

\[
\gamma+\beta_{ij}
\le4T\frac{1-c}{1+c}.
\tag{9}
\]

Thus necessarily `gamma+beta_ij<=4T` and

\[
\boxed{
1-P_{ij}\ge
\Phi_T(\gamma+\beta_{ij}),
\qquad
\Phi_T(r):=\frac{16Tr}{(4T+r)^2}.
}
\tag{10}
\]

This uses only a genuine common-unitary Cartan path and the global-maximizer Hessian; no zero-entry safety hypothesis and no inverse determinant are required.

## 4. Scalar residual inequality

Let `r=K-Delta`. Apply (10) on the four matching edges of `sigma_*` and then (5):

\[
K-k\ge c_*\sum_i\Phi_T(\gamma+\beta_{i,\sigma_*(i)}).
\tag{11}
\]

The lead/V4 lower bound `k>=gamma+Delta`, together with (3), gives

\[
T\le U(\gamma):=3d+2\gamma-\Delta.
\tag{12}
\]
For an admissible maximizer each argument of `Phi` lies in `[0,4T]`; on that range `Phi_T(r)` increases with `r` and decreases with `T`. Also

\[
K-k=K-3d-3\gamma+T\le K-\Delta-\gamma=r-\gamma.
\]
Therefore every positive-gap global maximizer on a support datum with unique `sigma_*` must satisfy the endpoint-computable inequality

\[
\boxed{
 r-\gamma\ge
 c_*\sum_{i=0}^3
 \frac{16U(\gamma)(\gamma+\beta_{i,\sigma_*(i)})}
 {(4U(\gamma)+\gamma+\beta_{i,\sigma_*(i)})^2}.
}
\tag{13}
\]

This is the new maximizer-local filter. It couples three pieces which were previously separate: the account04/B09 same-`P` standard projection, the exact Cartan path to a **specific** `3+1` endpoint, and the global pair-Hessian budget.

Repeated spectra, singular `A+B`, zero entries and reducible points do not invalidate (5)-(13): the algebra uses only endpoint supports, Birkhoff convexity, polynomial determinant support, the source-valid Cartan path and the known `n=3` common-block support roof. The uniqueness hypothesis concerns only the auxiliary standard endpoint maximum; if it fails, this particular scalar form is simply not asserted.

## 5. Exact genuinely-complex residual test

The standard-library verifier uses

\[
a=(-6i,\ 5i,\ 3+5i,\ 1),
\]
\[
b=(7+4i,\ 1+7i,\ 1-5i,\ -3),
\qquad \eta=-1+2i.
\tag{14}
\]
All spectra are simple and all sixteen cross-sums are nonzero. The signed spectral points are not on one generalized circle: the exact cross ratio of `-a_0,-a_1,-a_2,b_0` is

\[
-\frac{754}{159}+\frac{572}{159}i,
\]
so this is not a disguised common-circle/Hermitian reduction.

Exact enumeration gives

\[
M=7470,\quad m=-108,\quad d=7578,
\]
\[
Q=\frac{7643}{2},\quad \Delta=\frac{7297}{2},
\]
\[
K=\frac{7825}{2},\quad K_2=\Delta,
\quad r=K-\Delta=264.
\tag{15}
\]
The unique standard maximizer is

\[
\sigma_*=(1,2,0,3)
\]
(in zero-based image notation), and

\[
c_*=132,\qquad
(\beta_{0,1},\beta_{1,2},\beta_{2,0},\beta_{3,3})
=(7054,7062,0,0).
\tag{16}
\]

For comparison, the newest lead's bidirectional pair ceiling on this datum is

\[
\gamma\le\frac{1245}{4},
\]
while its subgroup-cubature bounds give gaps `866` and `4765/3`; account04/B09's standard-channel ceiling is therefore the previous best of these at `gamma<=264`.

For (13),

\[
U(0)=\frac{38171}{2}>2\max_i\beta_{i,\sigma_*(i)}.
\]
Consequently every ratio `(gamma+beta_i)/(4U(gamma))` is increasing on `0<=gamma<=264`, and so is the right side of (13), while the left side `264-gamma` decreases. Exact arithmetic gives

\[
F(179):=(264-179)-\text{RHS}(179)
=\frac{106719427805818720041578693893}
{317370214044455422343713354225}>0,
\]
whereas

\[
F(180)
=-\frac{13168169167865759705222247}
{19383419941737128926548496}<0.
\tag{17}
\]
Hence any hypothetical support violation on this genuinely complex datum must satisfy

\[
\boxed{0<\gamma<180.}
\tag{18}
\]

This cuts the current same-`P` standard reserve from `264` to below `180` (over 31% of that positive reserve removed) while the latest subgroup and bidirectional pair roofs remain weaker on this datum. It does **not** close the datum and is not a counterexample.

`verify_transport.py` uses only `fractions.Fraction`; `VERIFY_OUTPUT.txt` records the exact assertions and signs.

## 6. Conditional end-to-end chain and first missing implication

A full proof still follows if the lead residual can be eliminated. After this run a hypothetical counterexample support direction must survive, simultaneously:

1. the lead's two transposition-subgroup cubature roofs and bidirectional pair roof;
2. account04/B09's same-unitary standard-channel ceiling;
3. the exact pair-Rayleigh / bi-orientation stationarity constraints;
4. the Cartan/common-block and pair-Hessian constraints; and
5. whenever `K` has a unique maximizer, the new scalar transport constraint (13).

The first unpaid implication for this mechanism is therefore:

> **`MOC4-TRANSPORT-RESIDUAL-EXCLUSION-v1` (OPEN).** Prove that no structured endpoint datum with positive lead residual admits `gamma>0` satisfying (13) together with the exact bi-orientation `P/R` gates and subgroup-cubature constraints of one genuine global maximizer; or construct a source-valid common-unitary counterexample satisfying all of them.

The next mathematical move should eliminate `P` jointly in (5)/(10) with the six bi-orientation gates, rather than seek another independent bistochastic lift. The present run establishes a new exact bridge from endpoint standard deficiencies to true-unitary entry moduli and demonstrates a strict residual reduction on a non-common-circle complex datum.

## 7. Status and non-claims

- `MOC4-STANDARD-HAMMING-DEFECT-v1`: proved exactly.
- Cartan/Hessian block-gap collar (10): proved exactly at a genuine global support maximizer.
- Combined scalar condition (13): proved as a necessary condition when the standard maximum is unique.
- Exact complex test: verified with rational arithmetic; previous best listed ceiling `264` improves to `<180` under (13).
- Full MOC4: **OPEN**.
- No benchmark work, benchmark gold, credentials, scheduler identifiers, machine paths, email/Drive material, public posting, paid model/API/Codex call, remote workflow, or permission change was used.
