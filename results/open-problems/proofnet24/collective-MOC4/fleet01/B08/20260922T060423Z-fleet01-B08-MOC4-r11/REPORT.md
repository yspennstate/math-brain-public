# MOC4 fleet01/B08 — a 48-facet joint P/R lift obstruction and strict true-unitary no-go

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T060423Z-fleet01-B08-MOC4-r11`  
**Worker:** fleet01/B08  
**Assignment:** attempt a positive 24-permutation representation using one common unitary across compound degrees  
**Outcome:** `CANDIDATE_REFUTED` for the unconditional common-positive-lift mechanism. The parent MOC4 target remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact current team state consumed

The newest complete campaign-lead report used here is fleet03/B07 run `20260922T055130Z-fleet03-B07-MOC4-r11`, theorem `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`. For the genuine exterior-square point `O=Lambda^2 U in SO(6)`, every real `2 x 2` plane-mixing direction is a true-unitary tangent. At a support maximizer the full four-real-dimensional pair Hessian must be negative semidefinite, yielding

\[
\|M_{\alpha\gamma}\|_{\rm op}^2\le 4(T_{\alpha\gamma}^2-C_{\alpha\gamma}^2),
\]

and at pair saturation `T=|C|` the corresponding weighted traceless Gram sums vanish. Thus any surviving counterexample has much more structure than an arbitrary bistochastic or compound-minor array.

The named assigned OTHER-account result used directly is fleet02/B09 run `20260922T054507Z-fleet02-B09-MOC4-r16`, theorem `MOC4-EXTERNAL-SPINOR-SEPARATION-v1`. For each of the 48 non-Weyl normalized-Saxl outer vertices and each singleton gauge, every genuine `Lambda^2 SU(4)` point has `q`-distance strictly greater than `1/25` from that external corner. This will be applied below to the exact genuine unitary witness.

The preceding B08 run proved a positive all-compound lift on the entire order-four complex-Hadamard locus and a projected `P/R` gluing criterion. The present run changes mechanism: it asks whether such a projected common lift can hold for all true unitaries. The answer is **no**, even on a strict open set of dense real orthogonal matrices.

## 2. The necessary joint-lift polytope

Let

\[
P_{ij}=|u_{ij}|^2.
\]

Write the three complementary-pair classes as

\[
\mathcal C_0=\{01,23\},\qquad
\mathcal C_1=\{02,13\},\qquad
\mathcal C_2=\{03,12\}.
\]

Define the genuine complementary degree-two channel

\[
R_{\alpha\beta}=\frac12
\sum_{I\in\mathcal C_\alpha}
\sum_{J\in\mathcal C_\beta}
|\det U[I,J]|^2.
\tag{1}
\]

For a permutation `pi in S_4`, let `rho(pi) in S_3` be its induced action on the three complementary-pair classes. The kernel of `rho` is `V_4`. At a permutation matrix one has

\[
P=P_\pi,\qquad R=P_{\rho(\pi)}.
\]

Therefore any positive law `nu` on the 24 permutations that simultaneously reproduces even the degree-one marginals and the complementary **aggregated** degree-two marginals must satisfy

\[
(P,R)=\sum_{\pi\in S_4}\nu_\pi
(P_\pi,P_{\rho(\pi)}).
\tag{2}
\]

An all-compound common law is stronger than (2), so violating (2) is already enough to refute the universal common-minor lift mechanism.

## 3. New exact facet — `MOC4-PR-JOINT-LIFT-FACET-v1`

Use zero-based image notation and set

\[
\tau=0231.
\]

Define

\[
S(P)=P_{00}+P_{13}+P_{21}+P_{32}
=\sum_{j=0}^3P_{\tau(j),j},
\tag{3}
\]

and

\[
T(R)=(R_{00}-R_{01})+(R_{11}-R_{12})+(R_{22}-R_{20}).
\tag{4}
\]

Then every point of the joint permutation polytope (2) obeys

\[
\boxed{T(R)\le 3S(P).}
\tag{5}
\]

### Proof

It is enough to check a permutation endpoint. If `rho(pi)=id`, then `T=3`; the four elements of the `V_4` fiber are

`0123, 1032, 2301, 3210`,

and each agrees with `tau=0231` in exactly one coordinate, so `S=1` and equality holds.

If `rho(pi)=201`, then `T=-3`, hence (5) is automatic because `S>=0`. For each of the other four quotient permutations, `T=0`, so (5) is again automatic. Thus (5) holds pointwise on all 24 endpoints and therefore on their convex hull. `QED`

The exact endpoint values of `T-3S` are

\[
0\quad(13\text{ endpoints}),\qquad
-6\quad(10\text{ endpoints}),\qquad
-12\quad(1\text{ endpoint}).
\tag{6}
\]

The affine dimension of the 24-vertex joint `(P,R)` polytope is exactly `13`, while the 13 tight endpoints have affine dimension `12`. Hence (5) is genuinely facet-defining. Its complete left-right `S_4 x S_4` relabeling orbit contains exactly **48 distinct facets**, each with the same endpoint multiplicities `(13,10,1)` in (6). The adjacent exact verifier checks all these claims over `Fraction` arithmetic.

## 4. A strict rational-orthogonal true-unitary violation

Let `G_{ij}(t)` denote the rational Givens rotation with

\[
c=\frac{1-t^2}{1+t^2},\qquad s=\frac{2t}{1+t^2}
\]

in the `(i,j)` plane. Define

\[
U=G_{03}(1/2)G_{12}(1/2)G_{13}(1/4)G_{02}(4/5)G_{12}(-4/5).
\]

Exactly,

\[
U=\begin{pmatrix}
27/205&69792/142885&14168/28577&12/17\\
-32/41&8217/28577&-68292/142885&24/85\\
-24/41&-756/28577&102531/142885&-32/85\\
-36/205&-117656/142885&2976/28577&9/17
\end{pmatrix}.
\tag{7}
\]

The verifier proves exactly

\[
UU^T=I,\qquad \det U=1.
\]

Moreover every entry and every one of the 36 two-by-two minors is nonzero; in fact

\[
\min_{ij}|u_{ij}|=\frac{756}{28577},\qquad
\min_{|I|=|J|=2}|\det U[I,J]|=\frac{648}{28577}.
\tag{8}
\]

Thus this is a strict dense true-unitary datum, not a zero-entry or vanishing-minor boundary artifact.

For its genuine channels (1), direct exact calculation gives

\[
S(P)=\frac{2217495897}{20416123225},
\tag{9}
\]

\[
T(R)=\frac{212971450419}{510403080625},
\tag{10}
\]

and therefore

\[
\boxed{
T(R)-3S(P)
=\frac{46659258144}{510403080625}
\approx0.09141649005500652>0.
}
\tag{11}
\]

This violates the necessary facet (5). Consequently there is **no** probability law on the 24 permutations that simultaneously reproduces this unitary's degree-one channel `P` and complementary aggregated degree-two channel `R`. A fortiori there is no probability law reproducing every squared compound minor of this same `U`.

Because the gap in (11) is strict and (8) keeps the datum away from all entry/minor boundary strata, the failure persists on an open neighborhood of `U` in the unitary group.

## 5. Direct application of fleet02/B09 `MOC4-EXTERNAL-SPINOR-SEPARATION-v1`

The witness (7) is a genuine `SU(4)` point. Hence fleet02/B09's theorem applies to its exterior-square image: in every singleton gauge attached to every non-Weyl external Saxl vertex, its `q`-channel is strictly more than `1/25` away in `l_infinity` from that external corner.

Thus the joint-lift failure (11) cannot be dismissed as a linear-relaxation artifact caused by sitting at, or infinitesimally close to, one of the 48 phase-impossible external corners. It occurs at a genuine interior true-unitary point that already satisfies the nonlinear spinor realization constraints. The positive common-lift obstruction and the external-spinor obstruction are therefore genuinely different pieces of geometry.

## 6. What this refutes — and what it does not

The compact unconditional common-lift route would have been:

1. for each true `U`, find one probability law `nu_U` on `S_4` reproducing all squared compound-minor events;
2. substitute those probabilities into Cauchy-Binet;
3. obtain
   \[
   \det(D_a+UD_bU^*)=\sum_\pi\nu_U(\pi)
   \prod_j(a_{\pi(j)}+b_j)
   \]
   for every complex spectra pair, proving MOC4.

The exact genuine witness (7)-(11) kills Step 1, already after projecting the degree-two data to `R`. Therefore **no universal positive same-unitary common-compound representation can prove MOC4**.

This is **not** a counterexample to MOC4. The facet functional (5) is a separating functional on the joint `(P,R)` lift polytope; this run has not shown that it is realizable as a structured spectral support function

\[
\Re\!\left(\eta\prod_i(a_i+b_{\pi(i)})\right).
\]

A spectra-dependent convex law can still exist even when no spectra-independent common-minor law exists.

## 7. First essential missing implication after the no-go

The lead and partner results now identify the genuinely source-valid surviving route.

> **`MOC4-MAXIMIZER-JOINT-FACET-PAYMENT-v1` (OPEN).**  
> Fix arbitrary complex spectra and a support direction, and let `U` be a genuine global support maximizer. Assume `U` lies in the generic branch and violates one or more of the 48 joint `(P,R)` lift facets above. Using simultaneously (i) fleet03/B07's left/right mixed-conformal Hessian gates and their flat-pair Gram rigidity, (ii) fleet02/B09's gaugewise spinor separation/external-face payment constraints, and (iii) the exact same-unitary `P-R-D` identities, prove that the structured support still satisfies
> \[
> h(U)\le\max_{\pi\in S_4}\Re(\eta v_\pi),
> \]
> or construct an actual spectra/unitary/support triple with strict reverse inequality.

This is materially different from another Birkhoff/common-lift attempt. The universal lift is now rigorously excluded; what remains must exploit the **spectral structure of the support functional together with maximizer-local true-unitary geometry**.

## 8. Exact verification and non-claims

`verify_pr_joint_lift_facet.py` uses only the Python standard library and exact rational arithmetic. It verifies:

- the Givens product (7), `UU^T=I`, and `det U=1`;
- all 16 entries and all 36 two-by-two minors are nonzero;
- the exact values (9)-(11);
- all 24 endpoint facet values in (6);
- joint-polytope affine dimension `13` and tight-face affine dimension `12`;
- exactly `48` distinct left-right facet signatures.

No arbitrary bistochastic surrogate is claimed to be realizable. No benchmark material, held-out key, credential, scheduler identifier, machine path, unrelated private data, email/Drive material, paid model/API/Codex call, remote workflow, permission change, or public release was used. Full MOC4 remains open.
