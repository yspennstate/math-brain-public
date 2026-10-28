SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-24T09:49:57Z.
attacking: the r47 two-mode complementary-cancellation survivor: convert its two complementary crossing singular values into two additional genuine eigenvalues, route that branch through the hereditary five-large-eigenvalue dimension drop, and sharpen the remaining aligned rank-two carrier to a many-bank physical footprint.

# account01/B08 r48 — double-cancellation spectral escape and ten-bank carrier footprint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING INDUCTIVE EXIT + SHARPER PRODUCT-SAFE CARRIER FOOTPRINT / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN**. The full-target continuity conclusion remains **OPEN**. This report does not rotate the random coordinates, does not use moments, support regularity, Gaussianity, log-concavity, arbitrary-joint coarea, fiber-supremum, law-uniform pointwise quadratic-phase decay, or deletion of a nonzero coefficient tail.

## 1. Fresh sources and exact inherited state


The immediate own source is r47:

`yspennstate/math-open-problems@25986ed3ac4468867fad7663cae00b3843592497`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260924T090807Z-account01-B08-qform-r47/REPORT.md`.

In its edge-capped diffuse survivor one has a selected genuine three-eigenvector component

`A_3=U Lambda U^T`, `U^T U=I_3`, `min_j |lambda_j|>=L`,          (1.1)

and the complementary spectral matrix

`E=A-A_3`.                                                        (1.2)

The selected frame has physical leverage at most `1/48`. A literal original-coordinate cut is chosen with a distinguished physical row `k`; after deleting that row from the crossing, write

`D=A[S\{k},T]`, `C^-=E[S\{k},T]`.                               (1.3)

The completed designated-partner result actually consumed is account02/B08 r35,

`yspennstate/math-open-problems@087cf5aa5cfcee4eb6ae243facb9e0fcf2391e29`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/account02-B08-20260924T083643Z-r35/REPORT.md`.

At the exact scale

`c_0=sqrt(67/800)`,
`sigma=c_0/2=(1/2)sqrt(67/800)=0.14469796128487783...`,           (1.4)

its two-mode cancellation branch gives the actual inequality

`boxed: s_2(C^-)>sigma L`.                                       (1.5)

The other branch is the rank-two alignment branch developed further by r47: with `z=A[k,T]` and `V=V_2(D)` the top-two right singular plane,

`dist(z,V)<||z||/2`,                                             (1.6)

and there are sixteen pairwise-disjoint ORIGINAL-coordinate banks `J_1,...,J_16 subset T` such that

`||z_{J_r}|| > (sqrt(31)/24)||z||` for every r.                  (1.7)

The hereditary dimension-drop theorem used below is account01/B12 r18, read at the immutable containing commit

`yspennstate/math-open-problems@25986ed3ac4468867fad7663cae00b3843592497`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B12/20260922T211917Z-account01-B12-QFORM-r18/REPORT.md`.

It proves: at threshold `ell>0`, if the full QFORM estimate with constant `C` is available in every smaller dimension and

`(p_ell(A)-1)_+ +(q_ell(A)-1)_+ >=3`,                            (1.8)

then conditioning on one ORIGINAL coordinate and using interlacing plus affine closure gives

`||p_(X^T A X)||_infinity <= C/ell`.                             (1.9)

In particular, five eigenvalues of modulus at least `ell` satisfy (1.8), for every sign pattern.

## 2. New theorem: two-mode complementary cancellation forces five large eigenvalues

### Theorem 2.1 — `QFORM-DOUBLECANCEL-FIVE-LARGE-SPECTRAL-ESCAPE-v1`

Let `A=A_3+E` be as in (1.1)-(1.2), where `A_3` is the spectral sum of three actual eigenpairs of `A` with modulus at least `L`, and `E` is the exact orthogonal spectral complement. Let `I,J` be arbitrary original-coordinate sets. If

`boxed: s_2(E[I,J])>sigma L`,                                    (2.1)

then `A` has at least five eigenvalues of modulus greater than or equal to `sigma L`; more precisely, besides the selected three, the complement `E` has at least two eigenvalues of modulus `>sigma L`.

#### Proof

Let `P_I,P_J` denote the coordinate orthogonal projections. The rectangular block is

`E[I,J]=P_I E P_J`                                                (2.2)

after the usual identification with its nonzero coordinate rows/columns. Singular values are an operator ideal: for contractions `P,Q`,

`s_j(P E Q)<=s_j(E)` for every j.                                (2.3)

Thus (2.1) implies

`s_2(E)>=s_2(E[I,J])>sigma L`.                                   (2.4)

Because `A_3` is formed from actual orthonormal eigenvectors of the symmetric matrix `A`, its range is reducing for `A`, and

`E=A-A_3`                                                        (2.5)

has exactly the remaining eigenvalues of `A` together with zeros on the selected three-dimensional eigenspace. Since `E` is symmetric, its singular values are the absolute values of its eigenvalues. Equation (2.4) therefore supplies two eigenvalues of `A`, outside the selected triple, with modulus `>sigma L`. The selected three already have modulus at least `L>=sigma L`. Hence the total count at threshold `sigma L` is at least five. QED.

This implication is completely sign-free and dimension-free. It uses no probabilistic input at all.

## 3. Actual application of the designated partner inequality

Apply Theorem 2.1 to the literal complementary block in the designated-partner branch (1.5), taking

`I=S\{k}`, `J=T`.                                                 (3.1)

The partner inequality gives exactly

`s_2(E[I,J])=s_2(C^-)>sigma L`.                                  (3.2)

Therefore

`boxed: p_(sigma L)(A)+q_(sigma L)(A)>=5`.                       (3.3)

This is the promised equation-level application of account02/B08 r35. The apparently local two-mode cancellation cannot remain a purely crossing-level pathology: it necessarily exposes two additional genuine spectral directions in the exact complementary spectrum.

## 4. Hereditary dimension drop: the entire double-cancellation branch is inductively free

Combine (3.3) with account01/B12's hereditary theorem at threshold

`ell=sigma L`.                                                    (4.1)

Five `ell`-large eigenvalues imply

`(p_ell(A)-1)_+ +(q_ell(A)-1)_+>=3`,                             (4.2)

regardless of signs. Consequently:

### Corollary 4.1 — `QFORM-DOUBLECANCEL-INDUCTIVE-EXIT-v1`

Assume the universal QFORM density estimate with constant `C` has already been proved in every dimension `<n` (equivalently after scaling, at every positive threshold). Then every `n`-dimensional state in the r47/account02-B08-r35 two-mode complementary-cancellation branch obeys

`boxed:
 ||p_Q||_infinity <= C/(sigma L)
 =sqrt(3200/67) C/L
 <6.911 C/L.
}`                                                               (4.3)

No new analytic receiver is needed on this branch in a dimension induction.

Equivalently, the deterministic content is that **every** original-coordinate principal compression obtained by deleting one physical coordinate retains at least three eigenvalues of modulus at least `sigma L` in the sense needed by the B12 interlacing argument, and conditioning on that deleted original coordinate produces only an affine tilt of the lower-dimensional QFORM problem.

#### Scope / regularity

This is an inductive reduction, not an unconditional stand-alone density theorem because the lower-dimensional full target remains globally unproved. It establishes essential boundedness on this branch once the lower-dimensional theorem is available. The B12 weak-limit affine closure does not automatically preserve continuity, so no new `C_0` conclusion is claimed here.

The practical consequence for B08 is sharp: in a recursive proof assembly, the r47 unpaid dichotomy collapses to the **relative rank-two alignment branch only**. The two-mode complementary cancellation branch is no longer a primitive obstruction.

## 5. New deterministic strengthening: ten-bank footprint in the aligned branch

The remaining branch satisfies (1.6)-(1.7). Let `P` be the orthogonal projection onto the two-dimensional carrier plane `V=V_2(D)`, and write

`v=Pz`, `e=(I-P)z`.                                               (5.1)

Then

`||e||<||z||/2`.                                                  (5.2)

Set

`a=sqrt(31)/24`.                                                  (5.3)

Every one of the sixteen disjoint banks from r47 obeys

`||z_{J_r}||>a||z||`.                                            (5.4)

### Theorem 5.1 — `QFORM-R2-CARRIER-TENBANK-FOOTPRINT-v1`

Under (5.2)-(5.4), at least ten of the sixteen banks satisfy

`boxed: ||v_{J_r}||>||z||/24`.                                  (5.5)

Consequently, for the normalized vector

`u=v/||v|| in V`, `||u||=1`,                                    (5.6)

at least ten pairwise-disjoint ORIGINAL-coordinate banks satisfy

`boxed: ||u_{J_r}||>1/24`.                                      (5.7)

In particular the rank-two physical carrier projection has bank leverage

`boxed: tr(P 1_{J_r} P)=tr(1_{J_r}P)>1/576`                     (5.8)

on each of those ten banks.

#### Proof

Call a bank bad if

`||v_{J_r}||<=||z||/24`.                                        (5.9)

On a bad bank, triangle inequality and (5.4) give

`||e_{J_r}||
 >=||z_{J_r}||-||v_{J_r}||
 >(sqrt(31)-1)||z||/24`.                                        (5.10)

If seven banks were bad, their disjoint supports would give

`||e||^2
 > 7 (sqrt(31)-1)^2 ||z||^2/576`.                               (5.11)

But the exact inequality

`7(sqrt(31)-1)^2/576 >1/4`                                      (5.12)

holds: it is equivalent to `40>7sqrt(31)`, whose square is `1600>1519`. This contradicts (5.2). Hence at most six banks are bad, so at least ten satisfy (5.5).

Since `||v||<=||z||`, division by `||v||` yields (5.7). Finally, on the two-dimensional range of `P`, the positive operator `P 1_{J_r} P` has trace `tr(1_{J_r}P)`, and its Rayleigh quotient at the unit vector `u` equals `||u_{J_r}||^2`; therefore the trace is at least that Rayleigh quotient, proving (5.8). QED.

This strengthens r47's three-bank `1/8` footprint in a complementary direction: the per-bank mass is smaller, but the same actual rank-two physical carrier must now visit **ten disjoint original-coordinate banks** at a fixed quantitative scale. No independence is assigned to the singular-vector coordinate itself; the point is that the coefficient carrier has a genuinely distributed physical realization available for a subsequent grouped-coordinate receiver.

## 6. Updated B08 frontier

Within the edge-capped diffuse chamber reached by r43/r47, the current router is now:

1. **third-compound payment:** already gives a continuous universal density bound on the non-aligned crossing branch;
2. **two-mode complementary cancellation:** by Sections 2--4, this is a five-large-eigenvalue state at the reduced scale `sigma L` and is therefore an **inductive dimension-drop exit** with cost factor `sqrt(3200/67)<6.911` relative to the lower-dimensional constant;
3. **only primitive survivor:** the rank-two aligned child crossing, in which the physical star is within relative distance `1/2` of `V_2(D)`, the star itself is spread over sixteen disjoint physical banks, and the carrier plane contains a unit vector with the new ten-bank footprint (5.7)-(5.8).

Thus the first unpaid implication for this slot is now

`QFORM-TENBANK-R2-ALIGNED-CARRIER-COMPILER-v1`:

> consume the relative rank-two carrier whose physical plane has ten disjoint bank leverage packets, while retaining arbitrary same-bank child curvature, arbitrary complementary spectrum and all induced affine terms. The receiver must use the banks in original independent coordinates; it may not condition on or declare independence of the spectral/singular coordinate `u^T X`.

A natural next split is whether the second orthogonal vector in the carrier plane is itself localized on a small number of physical banks or diffuse across the ten-bank support. The former should feed an original-coordinate localized pivot/pair receiver; the latter should feed a genuinely two-dimensional grouped-bank/Fresnel receiver. That split has not yet been proved to close the branch.

## 7. Integrity and status

- Full universal bounded density: **OPEN**.
- Full-target continuous density: **OPEN**.
- New Theorem 2.1 is deterministic and unconditional.
- Corollary 4.1 is a rigorous **inductive reduction**, conditional only on the already-standard lower-dimensional induction hypothesis, and does not claim a stand-alone solution.
- Theorem 5.1 is deterministic coefficient geometry.
- No Monte Carlo or histogram is used as proof; all numerical decimals evaluate exact radicals/rationals.
- No task identity, cadence, enabled/paused state, email/push setting, permission, repository visibility, cross-account authentication, paid API/model setting, or installation setting was changed.
- This run remains `WITHOUT_VERIFIED_BRAIN`.
