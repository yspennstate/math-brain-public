SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-23T15:20:23Z.
attacking: the exact-rank-three indefinite collision collar: relate determinantal-triple disjointness, pair-area energy, and the partner overlap-two star identity, then isolate the near-coloop survivor.

# fleet03/B11 r35 — determinantal collision / overlap-star balance

## Status

`PROVED_SUPPORTING_STRUCTURAL_THEOREM / PARTNER_RESULT_APPLIED / TWO_QUANTITATIVE_WINGS_PAID / FULL_QFORM_OPEN`.

This run proves an exact probability identity for every exact-rank-three Parseval frame and combines it with the completed fleet04/B11 extension-mass theorem. It gives two dimension-free bounded-density exits for genuinely rotated indefinite signatures `(2,1)` and `(1,2)`, and reduces the surviving exact-rank-three geometry to a narrow determinantal-collision collar. It does **not** remove arbitrary additional nonseparable spectrum, and it does not close the collar. The full owner target remains OPEN.

Execution status: `WITHOUT_VERIFIED_BRAIN`.


## 1. Source-pinned inputs actually used

### Own predecessor

fleet03/B11 r34:

`yspennstate/math-open-problems@074f85e342c4e78fcbab7a43ba01f00252035d5a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T144943Z-fleet03-B11-QFORM-r34/REPORT.md`.

For an exact-rank-three factorization

`A=R M R^T`, `R^T R=I_3`, `s=min |lambda(M)|`,

it proved that if `D` is the probability that two independently sampled determinantal triples are disjoint, then some literal partition of the ORIGINAL independent coordinates has physical cross singular volume

`Delta_3 >= (s^3/8) sqrt(D)`,

and the grouped-cross compiler gives

`||p_Q||_infinity <= 6e/(s D^(1/6))`.                               (1.1)

That branch has a continuous density.

### Designated partner fleet04/B11

fleet04/B11 r6:

`yspennstate/math-open-problems@30555c1ca97752e10f5089ccd95f8514c704be5a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T131400Z-fleet04-B11-extension-mass-r6/REPORT.md`.

For every physical pair `S={i,j}`, with

`g_S=||r_i wedge r_j||^2`,

and triple extension masses

`d_{S,k}=|det A[S union {k},S union {k}]|`,

the partner proves exactly

`d_{S,k}=|det M| det(R_{S union {k}})^2`,

`sum_k d_{S,k}=|det M| g_S`,

and

`W_2(S)=(sum_k d_{S,k})^2-sum_k d_{S,k}^2`.                         (1.2)

The same completed partner report records the full-line pair-area compiler

`||p_Q||_infinity <= 128 sqrt(2)/(s sqrt(g_S))`.                    (1.3)

I apply (1.2) globally below, not merely cite it.

## 2. Determinantal notation

Assume throughout Sections 2--7 that the **full active matrix has exact rank three**:

`A=R M R^T`, `R^T R=I_3`,

with `M` real symmetric invertible. The assigned signatures are `(2,1)` and `(1,2)`, although the deterministic identities do not depend on the sign pattern.

For every unordered physical triple `K`, define

`v_K = det(R_K)^2`.                                                    (2.1)

Cauchy--Binet gives

`sum_K v_K=1`.                                                        (2.2)

Thus `v` is a probability law on physical triples. Define its one- and two-point inclusion marginals

`c_i := sum_{K contains i} v_K = ||r_i||^2`,                         (2.3)

`g_ij := sum_{K contains {i,j}} v_K = ||r_i wedge r_j||^2`.          (2.4)

Consequently

`sum_i c_i=3`, `sum_{i<j} g_ij=3`.                                  (2.5)

Introduce the quadratic collision energies

`C_2 := sum_i c_i^2`,
`G_2 := sum_{i<j} g_ij^2`,
`V_2 := sum_K v_K^2`.                                                 (2.6)

Let `K,L` be independent triples with law `v` and put

`D := P(K cap L = emptyset)`.                                        (2.7)

## 3. New exact collision identity

### Theorem `QFORM-DPP-COLLISION-IDENTITY-v1`

For every rank-three Parseval frame,

`boxed: D = 1 - C_2 + G_2 - V_2.`                                   (3.1)

### Proof

Fix a triple `K={a,b,c}`. Inclusion--exclusion for the independent triple `L` gives

`P(L intersects K)
 = c_a+c_b+c_c
   -g_ab-g_ac-g_bc
   +v_K`.

The last term is exactly `P(L=K)` because `L` itself has cardinality three. Therefore

`P(L disjoint K)
 =1-sum_{i in K}c_i+sum_{S subset K, |S|=2}g_S-v_K`.                 (3.2)

Average (3.2) over `K` with weight `v_K`. The first marginal identity (2.3) gives

`sum_K v_K sum_{i in K}c_i = sum_i c_i^2=C_2`;                       (3.3)

the two-point marginal identity (2.4) gives

`sum_K v_K sum_{S subset K, |S|=2}g_S = sum_S g_S^2=G_2`;           (3.4)

and the final average is `V_2`. This proves (3.1). QED.

This is stronger bookkeeping than the union bound `D>=1-C_2`: it exposes exactly what compensates when the leverage collision `C_2` exceeds one.

## 4. Actual application of the fleet04/B11 partner theorem

For a pair `S`, write its triple extensions as `K=S union {k}`. By (2.1) and the partner identity (1.2),

`W_2(S)
 = |det M|^2 [g_S^2 - sum_{K contains S}v_K^2]`.                     (4.1)

Sum (4.1) over all unordered pairs. Every triple contains exactly three pairs, hence every `v_K^2` occurs exactly three times. Therefore the designated partner result yields the **global exact identity**

`boxed:
 W_tot/|det M|^2 = G_2 - 3V_2,
 W_tot:=sum_S W_2(S).`                                               (4.2)

In particular `G_2>=3V_2`, but the useful point is the exact decomposition. Substitute (4.2) into (3.1):

`boxed:
 D = 1-C_2 + W_tot/|det M|^2 + 2V_2.`                                (4.3)

Equation (4.3) is the new structural balance. A failure of disjoint determinantal triples can only be caused by leverage collision after accounting for two explicitly third-direction currencies:

1. overlap-two star energy `W_tot`, meaning one physical pair admits two distinct third-coordinate extensions;
2. triple concentration `V_2`, meaning an actual physical triple carries nonnegligible determinant mass.

No random-variable rotation appears in this derivation.

## 5. First paid wing: low leverage-collision energy

Let `0<delta<1`. If

`C_2 <= 1-delta`,                                                    (5.1)

then (4.3), or simply nonnegativity of its last two terms, gives

`D>=delta`.                                                          (5.2)

Apply the completed r34 literal-cut theorem (1.1):

`boxed:
 ||p_Q||_infinity <= 6e/[s delta^(1/6)].`                            (5.3)

The density in this branch is continuous, because the grouped rank-three physical cross compiler used in r34 gives an `L^1` characteristic function.

For the concrete threshold `delta=1/4`,

`C_2<=3/4  =>  ||p_Q||_infinity
 <=6e 2^(1/3)/s
 =20.5489229713.../s.`                                               (5.4)

Under target normalization `s>=1`, this is `<20.549`.

This branch is not the same as the preceding maximum-leverage condition `max c_i<1/3`: it is controlled by the full collision energy of the determinantal one-point marginals.

## 6. Second paid wing: high leverage-collision energy

Suppose instead

`C_2 >= 1+delta`.                                                    (6.1)

Since `D>=0`, the exact collision identity (3.1) gives

`G_2 = D+C_2-1+V_2 >=delta`.                                        (6.2)

Because all pair marginals are nonnegative and `sum_S g_S=3`,

`G_2=sum_S g_S^2 <= (max_S g_S) sum_S g_S
 =3 max_S g_S`.                                                      (6.3)

Hence some actual physical pair satisfies

`boxed: g_S >= delta/3.`                                             (6.4)

Now apply the full-line pair-area compiler recorded in the completed fleet04/B11 report:

`||p_Q||_infinity
 <=128 sqrt(2)/(s sqrt(g_S))
 <=128 sqrt(6)/(s sqrt(delta)).`                                     (6.5)

Thus

`boxed:
 C_2>=1+delta
 => ||p_Q||_infinity <=128 sqrt(6)/(s sqrt(delta)).`                  (6.6)

For `delta=1/4`,

`C_2>=5/4
 => ||p_Q||_infinity <=256 sqrt(6)/s
 =627.0693741525.../s.`                                              (6.7)

This is not intended as a sharp constant. It is a genuine dimension-free exit for a part of the high-leverage indefinite chamber that was not covered by r34's diffuse maximum-leverage theorem.

Continuity is **not claimed** from this pair-area route; the conclusion used here is essential boundedness.

## 7. Collision-collar reduction

Combining Sections 5 and 6 gives the following precise supporting theorem.

### Theorem `QFORM-EXACTRANK3-COLLISION-COLLAR-v1`

Let

`A=RMR^T`, `R^TR=I_3`, `s=min |lambda(M)|`,

have exact rank three and signature `(2,1)` or `(1,2)`. Let

`C_2=sum_i ||r_i||^4`.

For every `delta in (0,1)`:

- if `C_2<=1-delta`, then `Q` has a continuous density and
  `||p_Q||_infinity<=6e/(s delta^(1/6))`;
- if `C_2>=1+delta`, then `Q` has an essentially bounded density and
  `||p_Q||_infinity<=128 sqrt(6)/(s sqrt(delta))`.

Consequently the exact-rank-three geometry not paid by these two wings is confined to

`|C_2-1|<delta`.                                                      (7.1)

Taking `delta=1/4` confines the new residual to

`3/4 < sum_i ||r_i||^4 < 5/4`.                                      (7.2)

Combining this with r34 further says that the genuinely new exact-rank-three B11 survivor satisfies both

`max_i ||r_i||^2 >=1/3`                                              (7.3)

and the collision collar (7.2). Thus the remaining state is quantitatively a **heavy but collision-critical** frame, rather than an arbitrary high-leverage frame.

## 8. Why the collar is real for this mechanism: exact coloop saturation

The collar cannot be removed merely by hoping that disjoint-triple or pair-area currencies stay uniformly positive.

For `m>=3`, define a Parseval frame with one exact coloop

`r_0=e_1`,

`r_j=sqrt(2/m)(0, cos(2pi j/m), sin(2pi j/m)),  j=1,...,m`.           (8.1)

The equally spaced planar rows satisfy

`sum_j r_j r_j^T = diag(0,1,1)`,

so the full frame is Parseval. Its leverages are

`c_0=1`, `c_j=2/m`,                                                   (8.2)

and therefore

`boxed: C_2=1+4/m ->1.`                                              (8.3)

Every nonzero determinant triple contains coordinate `0`, because all residual rows lie in a two-dimensional plane. Hence any two determinant triples intersect at `0`, so

`boxed: D=0.`                                                        (8.4)

The pair areas are

`g_{0j}=2/m`,

`g_{jk}=(4/m^2) sin^2(2pi(j-k)/m)`,                                  (8.5)

so

`boxed: max_{i<j}g_ij=2/m ->0.`                                      (8.6)

Thus both currencies used in Sections 5 and 6 vanish while `C_2->1`. The reduction is therefore structurally sharp at the level of these collision moments.

This is **not** a counterexample to QFORM. The exact-coloop branch is already paid by a different product-sensitive theorem (fleet02/B05 exact-coloop closure). Instead, (8.1) identifies the next mechanism: interpolate the collision collar into the existing coloop / near-coloop original-product receiver rather than try to force a uniformly good physical pair or two disjoint triples.

The deterministic checker verifies (3.1), (4.2), (4.3), the constants, and the exact coloop identities for finite `m`.

## 9. Rank-two logarithmic control and the role of the third direction

The mandatory opposite-sign rank-two control remains unchanged. For independent centered unit uniforms, the saddle product

`T=2XY`

has

`p_T(t)=log(1/(2|t|))`, `0<|t|<1/2`,                                (9.1)

so rank two genuinely has a logarithmic density singularity.

The new collision identities show two distinct ways the third direction removes that endpoint **without** pretending the spectral coordinates are independent:

1. In the `C_2<1` wing, two determinantal triples are disjoint with quantitative probability. A literal partition of the ORIGINAL coordinates then carries three physical cross singular directions. The grouped Plancherel/Fourier compiler produces the integrable three-direction decay that rank two lacks.

2. In the `C_2>1` wing, disjoint triples may fail, but (3.1) forces nontrivial pair-area energy. Each `g_ij` is not merely a two-dimensional object: it is exactly the sum of all **third-coordinate determinant extensions** of that physical pair. The partner's area compiler spends that extension geometry jointly. Thus the pair area is a certificate that the putative rank-two saddle sits inside a genuine rank-three Parseval geometry.

At the critical coloop limit, those two currencies can both vanish, but a different third-direction mechanism survives: one original scalar becomes independent of a dependent transverse pair. That is why the collision collar should be joined to the existing exact/near-coloop kernel rather than treated as a rank-two problem.

## 10. Remaining gap

The first B11 implication after this run is:

`QFORM-COLLISION-COLLAR-TO-NEARCOLOOP-OR-PAID-BANK-v1`.

Within exact rank three, assume

`max_i ||r_i||^2 >=1/3`,

`|sum_i ||r_i||^4 -1| <=1/4`,                                       (10.1)

and neither the already-paid scalar/pair pivot exits nor the literal disjoint-triple/pair-area wings give a desired fixed constant. Prove that the frame can be routed quantitatively either

- to the existing leave-one-out / near-coloop original-product theorem, or
- to a disjoint grouped bank / volume receiver.

The exact coloop family in Section 8 is the model endpoint and shows why a proof must retain original-coordinate product provenance.

For the **full owner target**, arbitrary additional nonseparable spectrum is still a separate bridge. Nothing in this report permits discarding the rest of a higher-rank quadratic form as independent noise or a small random perturbation.

Global continuity also remains OPEN. This run proves continuity only in the low-collision cross-cut wing.

## 11. Verification and scope discipline

`VERIFY.py` checks, on a deterministic random Parseval frame,

- `sum v_K=1`, `sum c_i=3`, `sum g_ij=3`;
- the collision identity (3.1);
- the summed partner identity (4.2);
- the combined identity (4.3).

It separately verifies the coloop family at `m=8,20` and evaluates the `delta=1/4` constants. Captured output terminates

`QFORM_B11_R35_COLLISION_STAR_CHECK_PASS`.

The numerical check is regression only; Sections 3--7 are the proof.

No Gaussianity, moments, log-concavity, compact or connected support, diagonal-basis assumption, post-rotation independence, law-uniform pointwise van der Corput estimate, arbitrary-joint coarea inequality, or Monte Carlo extremality claim is used.
