SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T11:03:36Z.
attacking: absolute-continuity/regularity at the random-critical-value heat-mode interface; compile the completed account02/B15 one-sheet posterior estimate into a deterministic original-coordinate gradient-cone criterion and an algebraic principal-adjugate identity.

# QFORM account01/B15 — gradient-cone compiler and principal-adjugate identity

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T110336Z-account01-B15-QFORM-auto11`  
**Assignment:** absolute continuity and regularity  
**Status:** `ESSENTIAL_STEP_APPLIED / GRADIENT-CONE-COMPILER / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted QFORM conjecture remains **OPEN**. The new point here is that the random conditional critical values occurring in the completed one-sheet theorem can be eliminated *exactly* from the majority-event geometry: for every physical invertible indefinite three-block, the majority event is a fixed quadratic-cone test on the corresponding coordinates of the global gradient `grad Q=2AX`. This turns the latest account02/B15 posterior bound into a deterministic matrix-only cone-cover certificate for the fixed-unit heat height. A second exact identity sums the corresponding local quadratic forms through the principal adjugates of `A`.

## 1. Fresh sources and corrections

Fresh owner control remained QFORM-only, OWNER CONTROL revision `2026-09-22.15`, with no later B15 stop observed before publication. The live corrections used here are: no law-uniform pointwise quadratic Fourier decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea shortcut, no generic projection/X-ray replacement for the minority two-sheet trace, and no assumption of a uniformly conditioned single physical minor.

The completed assigned-partner theorem actually applied is account02/B15:

`yspennstate/math-open-problems@4a7b432e38619707420962a272805f9646ad7e59`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T090720Z-account02-B15-QFORM-auto11/REPORT.md`.

For an invertible indefinite ORIGINAL-coordinate `3x3` principal block `B=A_SS`, after conditioning on the outside coordinates `W`, it completes the square and defines the conditional critical value `c_S(W)`. If `G_S` is the majority/one-sheet event and `mu_S^+` its output submeasure, then for arbitrary rough cap-one product inputs

`mu_S^+ <= C_S dx`,                                                   (1.1)

where `C_S` is the exact ruled one-sheet constant. In particular, at every Gaussian heat mode of any width, with mode height `M` and Gibbs posterior `nu`,

`boxed( M nu(G_S) <= C_S. )`                                         (1.2)

The same partner report proves the stronger random-critical-gap inequality; (1.2) is the piece used below.

The current newest-Claude/volume source actually applied at an equation is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`.

Its exact scope is used in Section 6; it is not extrapolated to the low-tail/high-leverage complement.

## 2. Exact removal of the random critical value from the majority event

Fix an invertible physical triple `S`, write the matrix in original coordinates as

`A = [[B,E],[E^T,F]]`,                                                (2.1)

with `B=A_SS`, and write the source point as `x=(u,w)`. Then

`Q(x)=u^T B u + 2u^T E w + w^T Fw`.                                  (2.2)

Completing the square only in the three original coordinates gives

`Q(x) = z^T Bz + c_S(w)`,                                             (2.3)

where

`z=u+B^{-1}Ew`,

`c_S(w)=w^T(F-E^T B^{-1}E)w`.                                        (2.4)

On the other hand the `S`-coordinates of the *global* gradient are

`g_S := (grad Q(x))_S = 2(Bu+Ew)=2Bz`.                               (2.5)

Therefore there is the exact identity

`boxed(
 Q(x)-c_S(w) = (1/4) g_S^T B^{-1} g_S.
)`                                                                    (2.6)

No probability, smoothness, Fourier transform, or rotated coordinate is involved in (2.6).

Suppose `B` is indefinite. Let

`sigma_S = +1` if `B` has signature `(2,1)`,
`sigma_S = -1` if `B` has signature `(1,2)`.

Equivalently, in dimension three,

`sigma_S = -sign(det B)`.                                             (2.7)

The majority/ruled event of the partner theorem is exactly

`G_S={ sigma_S (Q-c_S(W)) >=0 }`.

Using (2.6),

`boxed(
 G_S = { sigma_S g_S^T B^{-1} g_S >=0 }.
)`                                                                    (2.8)

Thus the apparently random critical value `c_S(W)` disappears completely from the *event*: it is a fixed quadratic cone in the restriction of the global gradient `g=2Ax`. This is the first new structural step of this run.

## 3. Deterministic gradient-cone bank compiler

Take any finite bank `B_1,...,B_N` of invertible indefinite original-coordinate principal triples. Let `C_j` be their exact one-sheet constants and let `sigma_j=-sign(det B_j)`. Choose arbitrary weights

`w_j>=0`, `sum_j w_j=1`,                                              (3.1)

and define, for `g in range(A)`,

`Gamma_w(g)
 := sum_j w_j 1{ sigma_j g_{S_j}^T B_j^{-1}g_{S_j} >=0 }`.           (3.2)

At a fixed-unit Gaussian heat mode `y_*`, let

`M=max_y E gamma_1(Q-y)`

and let `nu` be the associated Gibbs posterior. Since `grad Q(X)=2AX` always lies in `range(A)`, (1.2) and (2.8) give

`M E_nu Gamma_w(grad Q)
 = M sum_j w_j nu(G_j)
 <= sum_j w_j C_j`.                                                   (3.3)

Define the deterministic cone-coverage number

`delta_w(A):=inf_{g in range(A)} Gamma_w(g)`.                         (3.4)

(The value at `g=0` is one under the closed-cone convention, so the infimum is harmless.) If `delta_w(A)>0`, then (3.3) yields the completely source-independent certificate

`boxed(
 M <= [sum_j w_j C_j]/delta_w(A).
)`                                                                    (3.5)

This is a **matrix-only compiler** for the full heat height: all dependence on the random conditional critical values has vanished. It preserves the original-coordinate product theorem only in the analytic premise (1.2); after that premise is paid, the remaining coverage problem is deterministic linear algebra on `range(A)`.

A useful optimized formulation is

`C_cone(A)
 := inf_w { [sum_j w_j C_j]/delta_w(A) : delta_w(A)>0 },`             (3.6)

where the infimum ranges over finite banks of invertible indefinite physical triples and probability weights. Then

`boxed( ||mu_Q*gamma_1||_infinity <= C_cone(A) )`                    (3.7)

for every cap-one product source whenever `C_cone(A)<infinity`.

Since the already completed heat-boundary reduction identifies the sharp scaled raw-density constant with the sharp fixed-unit heat-height constant, the full owner theorem would follow from the purely matrix statement

`sup_A s_3(A) C_cone(A) < infinity`,                                  (3.8)

possibly after adjoining the already-paid definite/volume/ridge exits. Equation (3.8) is a sufficient structural target, not a proved consequence of the three-large-eigenvalue hypothesis.

### Harmonic version

Let `h_j=1/C_j`, `H=sum_j h_j`, and take the harmonic weights

`w_j=h_j/H`.                                                          (3.9)

Then

`sum_j w_j C_j = N/H`,                                                (3.10)

so if

`H/N >= c s_3(A)` and `delta_w(A)>=delta`,                            (3.11)

then

`boxed( s_3(A) M <= 1/(c delta). )`                                  (3.12)

This is stronger in form than selecting one well-conditioned block: arbitrarily weak blocks may remain in the bank and are automatically downweighted by their exact ruled cost.

A posterior-only variant also follows immediately from (3.3): without any pointwise cone cover,

`E_nu Gamma_w(grad Q) <= [sum_jw_jC_j]/M`.                            (3.13)

For harmonic weights and `H/N>=c s_3(A)`, a blow-up sequence `s_3(A)M->infinity` forces

`E_nu Gamma_w(grad Q)->0`.                                            (3.14)

Thus its heat Gibbs posterior must concentrate on gradients lying in the **minority cone for almost all ruled capacity weight**. This is a sharper source-space classification than saying only that the random cone vertices shadow the output mode.

## 4. Principal-adjugate identity for the cone bank

There is an exact algebraic identity that organizes the local cone quadratic forms.

For every three-element coordinate set `S`, let `E_S` denote coordinate embedding and `A_S=A_SS`. Define

`J_3(A)=sum_{|S|=3} E_S adj(A_S) E_S^T`.                              (4.1)

Then

`boxed(
 J_3(A)=A^2-(tr A)A+e_2(A) I,
 e_2(A)=((tr A)^2-tr(A^2))/2.
)`                                                                    (4.2)

Proof: `e_3(A)` is the sum of all `3x3` principal minors. Its differential can be computed in two ways. Differentiating the principal-minor expansion gives

`D e_3(A)[H]
 = sum_{|S|=3} tr(adj(A_S) H_SS)
 = tr(J_3(A)H)`.                                                      (4.3)

Newton's identity gives

`grad e_3(A)=A^2-(tr A)A+e_2(A)I`,                                   (4.4)

and comparison of (4.3)-(4.4) proves (4.2). This is a polynomial identity, so no nonsingularity is needed.

Now suppose a particular triple is invertible. By (2.6),

`det(B_S)[Q-c_S(W)]
 = (1/4) g_S^T adj(B_S) g_S`.                                        (4.5)

On a generic matrix for which every physical `3x3` principal block is invertible, summing (4.5) over all triples yields

`boxed(
 sum_{|S|=3} -det(A_S)[Q-c_S(W_S)]
 = -(1/4) g^T [A^2-(tr A)A+e_2(A)I] g.
)`                                                                    (4.6)

For an indefinite triple, `-det(A_S)[Q-c_S]` is exactly

`|det(A_S)| sigma_S [Q-c_S]`,                                        (4.7)

so it is positive precisely on the partner's majority side. For a definite `3x3` block, `adj(A_S)` is positive definite (both positive- and negative-definite odd-dimensional blocks have positive-definite adjugate), hence its contribution to the right side of (4.6) is nonpositive.

Consequently, on the all-principal-minors-nonsingular core,

`boxed(
 g^T [A^2-(tr A)A+e_2(A)I] g <0
 => at least one indefinite physical triple is on its majority side.
)`                                                                    (4.8)

This does **not** yet give the universal weighted coverage `delta_w(A)>0`; a single majority block may carry vanishing bank weight. Its value is that the random-critical-value geometry now has a global polynomial diagnostic. The remaining quantitative problem is to upgrade existence/aggregate signed mass in (4.6) into a capacity-weighted cone coverage, or route the failure to a paid low-tail/ridge/grouped-coordinate branch.

## 5. Why this respects the live corrections

The cone identity (2.8) is derived by completing the square in ORIGINAL coordinates and differentiating the original polynomial. No spectral rotation is used to claim independence.

No pointwise Fourier decay is used. No arbitrary projected joint density is inserted into a coarea theorem. No X-ray/line-integral estimate is used for the two-sheet contribution. The only probabilistic input in the compiler is the completed rough-product one-sheet submeasure theorem (1.1), whose product provenance is retained exactly at its valid scope.

The adjugate identity is purely algebraic and makes no probabilistic regularity claim by itself.

## 6. Actual application of the newest volume/tail result

The current volume-tail extension supplies an already-paid exit. In its exact hypotheses, for an ORIGINAL-coordinate cross block `M` with top-two projection leverage and collective-tail gate as stated in that source, putting

`T2=sum_{j>=3} s_j(M)^2`,

it proves

`||p_Q||_infinity
 <= (9 sqrt(3)e/2) [s_1(M)^2 s_2(M)^2 T2]^(-1/6).`                  (6.1)

The fixed-unit Gaussian heat convolution is an `L^infinity` contraction, so at the exact B15 heat functional

`boxed(
 s_3(A) M
 <= (9 sqrt(3)e/2) s_3(A)
    [s_1(M)^2 s_2(M)^2 T2]^(-1/6).
)`                                                                    (6.2)

Thus every instance satisfying that volume/tail certificate is already paid at the same heat functional used in Sections 2-4. The new cone compiler is needed only in the surviving low-total-tail/high-leverage or other non-volume branches. Continuity supplied by the volume theorem is stronger but is not needed for the inequality (6.2).

## 7. Regularity ledger

1. **Absolute continuity.** For any nonzero symmetric `A` and any absolutely continuous joint input law, `X^TAX` is absolutely continuous: coarea away from the critical subspace `ker A` proves that the inverse image of every null output set is null. Product structure and the cap are unnecessary for this qualitative fact.
2. **Fixed-instance boundedness/continuity.** The completed account02/B15 fixed-matrix theorem, independently reviewed in account03/B15, proves at its stated scope that every fixed rank-`>=3` target has an individually bounded density with a `C_0(R)` representative. Its constant may deteriorate with the physical geometry of `A`; it is not the universal theorem.
3. **Universal `L^infinity` height.** This is the central unresolved quantitative target. It is exactly enough to bound the fixed-unit Gaussian heat height after spectral scaling. The cone compiler (3.5) is a new sufficient matrix criterion for that height.
4. **Continuity remains logically separate.** Neither (1.2), (2.8), (3.5), nor the adjugate identity uses raw-output continuity. The fixed-unit heat profile is automatically smooth for every probability law, even before raw absolute continuity is known.

## 8. First unpaid implication after this run

A concrete structural target is now:

- outside the already-paid volume/tail/ridge/definite branches, construct a finite bank of invertible indefinite ORIGINAL-coordinate triples and weights `w` for which

`sum_j w_j C_j <= C0/s_3(A)`                                         (8.1)

and

`inf_{g in range(A)} sum_j w_j
  1{ -sign(det B_j) g_{S_j}^T B_j^{-1}g_{S_j} >=0 } >= delta0`       (8.2)

with universal `C0,delta0>0`;

- or prove that failure of (8.2), i.e. existence of a common gradient direction lying in the minority cones of almost all cost-efficient blocks, forces one of the paid low-tail/ridge/grouped-coordinate exits.

The principal-adjugate formula (4.6) is an exact algebraic starting point for (8.2). It shows that the collection of local majority cones is not unrelated: their determinant-weighted signed gaps sum to one global quadratic form in the gradient. What is still missing is a dimension-free conversion from that signed identity to the cost-weighted coverage required by (8.2).

**Full QFORM status: OPEN / NOT PROVED / NOT DISPROVED.**
