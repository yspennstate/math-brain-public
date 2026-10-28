# account02/B07 MOC4 — bilateral equality circles and full-Z singular-axis transport

Run: `20260922T093424Z-b07-c8697991`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Candidate: **`MOC4-MSQR-BILATERAL-EQUALITY-CIRCLE-v1`**  
Parent MOC4 target: **OPEN / NOT PROVED / NOT DISPROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and live authority


A second protected-control check before immutable science writes found the same blobs:

- `AGENTS.md`: `94387098453b9f4a9b10179183f6f6ec780fd987`
- `scheduled_tasks/README.md`: `3d4a9372c87802ab734141a3374d04c8823372e3`
- `scheduled_tasks/fleet.json`: `e647d5d2479749f80ce7bb4862bee0f28513c7d9`
- `scheduled_tasks/roles.json`: `ed17ecc94f76720c0345b3e32249b791b20ec611`
- `scheduled_tasks/PROTOCOL.md`: `83a9268bf5287ca203e4be69a79e25382397bca7`

No later B07/account02 stop was observed at that check.

## 2. Source-bound inputs actually consumed

### Campaign lead

account03/B07 run `20260922T074824Z-account03-B07-MOC4-r13`, report blob `7724d19f793eb934c5fcc2b469bb9d0a108da4eb`, candidates

- `MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1`,
- `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`.

At a true global support maximizer, a mixed-Schur pair kernel is a **full-Hessian kernel**. If the cubic covector is split into the singular pair block and its orthogonal complement, the exact full fourth-order gate is

`q4 + 3 R_pair + 3 R_cross <= 0`,

with `R_cross>=0`. Hence exact pair-LS saturation (`q4+3R_pair=0`) forces `R_cross=0` and the lead's cross residual to vanish.

### Named partner

account03/B08 run `20260922T072320Z-account03-B08-MOC4-r12`, report blob `da2892a8a90526b2abdeecf897743fc5a51364e6`, `MOC4-GENERIC-FACET-LADDER-v1`.

Its dense exact true-unitary near-facet point is *not* pair-stationary: a further genuine pair move raises the same support. I apply that result as a guardrail: none of the saturation identities below may be inferred from a tiny hull gap alone; exact global maximality / pair stationarity is required first.

### Named OTHER-account result used directly

account03/B20 run `20260922T071802Z-account03-B20-MOC4-r12`, report blob `e37d1ae846af5e734e0051aad54aa1d7cb623ed6`, `MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1`.

On one genuine complementary `SU(2) x SU(2)` pair orbit the support is exactly

`f(n,m)=c+p.n+q.m+n^T Z m`,  `n,m in S^2`,

and, in the simple mixed-Schur case,

`D=AB-m0^2>0`, `E_L=A r2+m0 s2`, `C_L=A(H-rho^2)-s2^2`.

The full same-pair global trust condition is equivalent to the `2 x 2` PSD condition `[[D,-E_L],[-E_L,C_L]]>=0`. It is therefore redundant with the pair Lyapunov-Schmidt reserve as an inequality. The present run does **not** claim a new same-pair inequality; it extracts an exact bilateral algebraic normal form from the *equality* case and makes it available to the cross-split problem.

The immediately preceding B07 result `MOC4-MSQR-HIGHER-ORDER-SATURATION-v1` is also retained: pair-LS saturation plus full maximality imposes corrected transverse discriminant stationarity and exact fifth/sixth-order local-max conditions.

## 3. Exact left equality circle at pair-LS saturation

Use B20's pole normal form. Let

`Z=[[M,r],[s^T,z0]]`,
`M=diag(sqrt(AB),m0)`,
`p=(-r,A-z0)`, `q=(-s,B-z0)`,
`L=A+B-z0`,

with the mixed-kernel cubic cancellation already enforced. Define

`D=AB-m0^2>0`,
`E_L=A r2+m0 s2`,
`C_L=A(H-rho^2)-s2^2`.

Suppose the simple pair-LS gate is **exactly saturated**:

`D C_L = E_L^2`.                                             (3.1)

For arbitrary `n=(x,y,z) in R^3`, define the squared left trust slack

`S_L(n)=(L-p.n)^2-||q+Z^T n||^2`.

B20's exact S-lemma matrix has multiplier `-AB`. At (3.1), its nonzero `3 x 3` homogeneous block is rank one. Therefore the identity is not merely an on-sphere statement: for **all** real `n`,

`S_L(n)+AB(||n||^2-1)=D [ y+k_L(1-z) ]^2`,                  (3.2)

where

`k_L=E_L/D`.

Put

`w_L=(0,1,-k_L)`, `d_L=k_L`.

Then (3.2) is

`S_L(n)=D(w_L.n+d_L)^2-AB(||n||^2-1)`.                       (3.3)

On the sphere the equality locus is consequently the genuine circle

`C_L={n in S^2: w_L.n+d_L=0}`.                               (3.4)

It never collapses to a point: `||w_L||^2-d_L^2=1`, so its Euclidean radius is exactly

`1/sqrt(1+k_L^2)>0`.                                         (3.5)

At every regular point of this circle,

`m(n)=(q+Z^T n)/(L-p.n)`                                    (3.6)

is a unit vector and `f(n,m(n))=c+L`, the global support maximum. If the denominator in (3.6) vanishes, then the numerator also vanishes by (3.3); the same equality statement is obtained by continuity (indeed the fiber becomes no harder). No inverse of `det(A+B)` occurs.

## 4. New bilateral upgrade: the right circle is forced too

The left saturation automatically implies the right saturation. Define

`E_R=B s2+m0 r2`,
`C_R=B(H-rho^2)-r2^2`.

From (3.1), equivalently from B20's explicit pair-LS equality,

`H-rho^2=(A r2^2+2m0 r2 s2+B s2^2)/D`.

Hence

`D C_R`
`=B(A r2^2+2m0 r2 s2+B s2^2)-D r2^2`
`=(m0 r2+B s2)^2=E_R^2`.                                   (4.1)

So, after interchanging the two true `SU(2)` factors, there is a second exact off-sphere identity

`S_R(m)+AB(||m||^2-1)=D [ y_R+k_R(1-z_R) ]^2`,              (4.2)

where

`S_R(m)=(L-q.m)^2-||p+Z m||^2`,
`k_R=E_R/D`,
`w_R=(0,1,-k_R)`, `d_R=k_R`.

Thus the right maximizers form the nondegenerate circle

`C_R={m in S^2:w_R.m+d_R=0}`.                                (4.3)

Every regular maximizer map (3.6) sends `C_L` into `C_R`. Therefore simple pair-LS saturation gives not a single flat tangent but a **bilateral pair of exact true-unitary equality circles**.

This is the first useful reformulation of the B20 collapse for the cross-split problem: the equality leaf can now be represented by finite coefficient identities rather than by a continuum of support inequalities.

## 5. Finite coefficient identities

Comparing quadratic, linear and constant coefficients in (3.3) and (4.2) gives

`ZZ^T = p p^T - D w_L w_L^T + AB I`,                         (5.1)

`Z^T Z = q q^T - D w_R w_R^T + AB I`,                       (5.2)

`L p + Z q = -D d_L w_L`,                                   (5.3)

`L q + Z^T p = -D d_R w_R`,                                 (5.4)

`L^2-||q||^2-D d_L^2 = AB`,                                 (5.5)

`L^2-||p||^2-D d_R^2 = AB`.                                 (5.6)

These are exact identities among the actual same-unitary trust coefficients. They are not a free bistochastic relaxation.

A useful conceptual correction follows. Along this exact same-pair equality leaf, the entire support function is constant after complementary optimization. Hence all one-dimensional higher derivatives along the leaf vanish automatically. The previous B07 fifth/sixth-order conditions remain relevant for **full-tangent / cross-split** perturbations, but another run computing only higher derivatives inside this same saturated pair orbit would be redundant.

## 6. New full-Z singular-axis transport

Define the two distinguished axes

`a_L = p x w_L`,
`a_R = q x w_R`.                                             (6.1)

Assume first `a_L != 0`. Since `a_L` is orthogonal to both `p` and `w_L`, (5.1) gives

`ZZ^T a_L = AB a_L`.                                        (6.2)

Thus `sqrt(AB)` is a singular value of the **full 3 x 3 coupling matrix Z**, not only of the tangent `2 x 2` block `M`.

Moreover (5.3) gives

`a_L^T Z q=0`,

so `x=Z^T a_L` is orthogonal to `q`. From (6.2), `x` is an `AB` eigenvector of `Z^T Z`. Insert it into (5.2):

`q(q.x)-D w_R(w_R.x)=0`.

The first term is zero and `D>0`, hence `w_R.x=0`. Therefore

`Z^T a_L` is orthogonal to both `q` and `w_R`.                (6.3)

If `a_R != 0`, this one-dimensional orthogonal complement is exactly `span(a_R)`, hence

`Z^T a_L || a_R`.                                            (6.4)

By symmetry,

`Z a_R || a_L`.                                              (6.5)

Taking norms in (6.2), the scale is fixed:

`|Z^T a_L|=sqrt(AB)|a_L|`,
`|Z a_R|=sqrt(AB)|a_R|`.                                    (6.6)

Thus in the generic subbranch `a_L a_R !=0`, the left and right equality-circle axes are transported into each other by the **actual full coupling matrix** `Z` at the mixed singular value.

There is also an exact degeneracy alternative. If `a_L=0`, then `p` is parallel to `w_L`, so (5.1) has the form

`ZZ^T=AB I + c w_L w_L^T`                                   (6.7)

for a scalar `c`. Therefore `AB` is an eigenvalue of `ZZ^T` with multiplicity at least two. Likewise `a_R=0` forces multiplicity at least two for `Z^T Z`.

So exact simple pair-LS saturation obeys a finite dichotomy:

1. **generic axis transport:** both cross products are nonzero and (6.4)-(6.6) hold;
2. **full-Z singular degeneracy:** one of the cross products vanishes and the singular value `sqrt(AB)` has multiplicity at least two in the full coupling.

This is the new algebraic bridge that was missing from the one-sided equality-circle description.

## 7. Exact rational verification

`VERIFY_BILATERAL_EQUALITY_CIRCLE.py` uses only Python standard-library `Fraction` arithmetic. It instantiates the exact B20 normal form with

`A=B=1`, `m0=0`, `rho=1/3`, `r2=1/4`, `s2=1/5`,

so

`D=1`, `H=769/3600`, `z0=6431/7200`, `L=7969/7200`,
`k_L=1/4`, `k_R=1/5`.

It verifies both pair-LS saturation equations, all six coefficient identities (5.1)-(5.6), and obtains

`a_L=(-319/7200,-1/12,-1/3)`,
`a_R=(-481/7200, 1/15, 1/3)`,

with the exact bilateral transport

`Z^T a_L = -a_R`,
`Z a_R = -a_L`.                                              (7.1)

It also checks a nontrivial rational point on the left equality circle,

`n=(-4/9,-4/9,-7/9)`,

whose exact complementary maximizer is

`m=(600/3769,-1440/3769,-3431/3769)`.

Both vectors have norm one, the first lies on `C_L`, the second lies on `C_R`, and the support is exactly

`7969/7200 = L`.                                             (7.2)

The captured exact verifier output is stored beside this report.

This is an algebraic calibration of the genuine `S^2 x S^2` pair-orbit normal form, not an MOC4 counterexample.

## 8. Application of the lead and partner: sharpened proof tree

Suppose MOC4 fails in a support direction. After the already-established repeated-spectrum/common-lift reduction and open-gap genericization, take a simple-spectrum true-unitary global maximizer with positive gap `gamma>0`.

The partner account03/B08 stress test shows that tiny support gap alone is irrelevant; all true pair gates must first be stationary/strict. On the lead's mixed-Schur branch:

- if the pair-LS inequality is strict, the lead's positive cross reserve remains the correct payment mechanism;
- if the pair-LS inequality is saturated, the present theorem forces the bilateral identities (5.1)-(5.6) and the axis-transport/degeneracy dichotomy of Section 6;
- because the point is a **full** global maximizer, lead r13 simultaneously forces `R_cross=0` and full-Hessian kernel annihilation.

Therefore the exact-saturation residual is now finite and sharply structured. One no longer needs to search an unconstrained equality circle or an infinite same-pair derivative tower.

The first essential missing implication is

**`MOC4-MSQR-AXIS-CROSSSPLIT-RIGIDITY-v1`**:

> For an actual MOC4 determinant/exterior-square coefficient tuple `(p,q,Z)` coming from one true unitary and one complex support direction, prove that the simultaneous system
>
> - positive target gap and all elementary pair strictness/stationarity,
> - lead r13 full-Hessian kernel annihilation and `R_cross=0`,
> - bilateral identities (5.1)-(5.6), and
> - either generic axis transport (6.4)-(6.6) or the full-Z multiplicity branch (6.7),
>
> forces the known zero/common-block boundary or target support safety.

Equivalently, in the generic axis branch substitute `Z^T(p x w_L) || (q x w_R)` and its transpose into the same-unitary `P/R/D` and exterior-square identities. In the degeneracy branch exploit the repeated full singular value `sqrt(AB)` as the candidate boundary mechanism. A strict positive-gap true-unitary solution of the complete system would instead be a legitimate route toward a counterexample.

The separate all-negative-definite (`NDI`) branch and the campaign's zero-face support obligation remain open.

## 9. Singular determinant points, repeated spectra, and claim discipline

Nothing in Sections 3-8 uses `(A+B)^{-1}` or divides by `det(A+B)`. The trust variables are genuine pair-orbit Bloch coordinates, and all identities are polynomial/rational in the support coefficients with `D>0` only because this section is the **simple mixed singular-value** branch. Therefore a singular determinant value itself causes no difficulty.

The double mixed-singular-value branch `D=0` is not silently absorbed into this theorem; B20 already treats it separately, and prior B07 work sends its exact saturation to an equal-support zero-entry maximizer. Repeated spectral eigenvalues remain covered by the inherited exact pair-symmetrized common-lift argument.

No claim is made that the bilateral identities are an additional independent same-pair inequality; B20 proved there is none. Their value is that they convert the exact-saturation leaf into a finite full-`Z` algebraic system that can be coupled to the **other** root blocks and same-unitary structure.

## 10. Verdict

**ESSENTIAL_STEP_APPLIED.**  
`MOC4-MSQR-BILATERAL-EQUALITY-CIRCLE-v1` is proved as an exact consequence of true `SU(2) x SU(2)` pair-LS saturation. It supplies a bilateral equality-circle normal form, six finite coefficient identities, and a full-`Z` singular-axis transport / multiplicity dichotomy. Together with lead r13, the exact-saturation MSQR branch is reduced to a finite cross-split rigidity system rather than another same-pair optimization problem.

Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.
