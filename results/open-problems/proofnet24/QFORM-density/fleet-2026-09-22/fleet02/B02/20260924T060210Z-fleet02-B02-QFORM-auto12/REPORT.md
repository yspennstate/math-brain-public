SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-24T06:02:10Z.

# fleet02/B02 auto12 — rank-two one-bank receiver and fully entangled 2x2 Fourier-L1 compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING ESSENTIAL-DENSITY THEOREM + NEW FOURIER-L1 THEOREM + EXACT-TARGET D'/D5 OBSTRUCTION; FULL QFORM OPEN; FULL CONTINUITY OPEN; TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution context: **VERIFIED_BRAIN** in the programme-local sense: authenticated repository retrieval and actual receiver-memory use occurred; `full_brain_connected=false`.

The full target remains the unrestricted owner statement: every independent original-coordinate real input has a one-dimensional probability density at most one; `A` is arbitrary real symmetric with at least three eigenvalues of modulus at least one; no moments, support, log-concavity, iid, diagonal-basis independence, post-rotation independence, or deletion of nonzero coefficient tails is allowed. Continuity remains separate from essential boundedness.

## 1. Fresh state and source-pinned inputs actually used

Fresh `math-research-brain/main` was resolved at startup and the owner revision remained `2026-09-22.15`. The required control files, correction inbox, assignment, and `MEMORY_PROTOCOL.md` were read. The preceding B02 receiver-memory snapshot was read from the immutable prior run and used: its first unpaid edge was the fixed-scale diagonal/carrier-aligned-hub endpoint, with the instruction not to recycle the exhausted strategy of forcing another transverse `E3` block.

The required Claude-source package was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. In particular this run retains the exact scopes of

- D': third exterior-volume decoupling with its row-volume marginal gate and the later reviewed sharp-Hausdorff--Young refinement;
- D5: fifth exterior-volume Fourier payment with no marginal gate;
- the correction that neither theorem forces a uniformly good physical minor, and the original QFORM conjecture is still open.

The reviewed B02 constants available on a literal physical cross block are

`E3(B)>0 => ||p_Q||_infinity <= C3 E3(B)^(-1/6)`, `C3=10.345083232147514...`,

and independently

`E5(B)>0 => ||p_Q||_infinity <= (5e/sqrt(2)) E5(B)^(-1/10)`.

Both are genuine integrated-Fourier receivers on their stated scopes.

The completed rank-two affine half-Riesz theorem used below is

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For a two-dimensional product input the affine term lies automatically in the quadratic range, so its sharper completed form is

`sup_s E |Y^T S Y + beta^T Y-s|^(-1/2) <=16 sqrt(30)|det S|^(-1/4)`.

The newest completed designated partner is `fleet03/B02` r47, read at

`yspennstate/math-open-problems@859066cc3edee1bbeafe367e3bf2d630a4c425d9`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260924T045848Z-fleet03-B02-qform-r47/REPORT.md`.

Its live full physical cut `N=A[L,R]` has

`x1*x2 > kappa :=247/576`                                                (1.1)

on the robust rank-two survivor. Its strengthened global spectral-window compiler pays the diffuse branch, while the remaining off-diagonal hub branch has a physical coordinate `i` with

`g_i >1/(228 sqrt(2))`,                                                  (1.2)

unless a physical `E3` exit or at-most-four near-coloop alternative fires. The exact still-unpaid list also contains the fixed overlap-one `V1` packet and a physical diagonal `>1/228`.

## 2. New broad theorem — a robust rank-two crossing pays essential density when one bank is untwisted

### Theorem `QFORM-RANK2-ONEBANK-LINEAR-DENSITY-v1`

Let `U=(U_i)_(i in I)` and `V=(V_j)_(j in J)` be disjoint original-coordinate product banks, and let `W` denote every remaining original coordinate. Assume that after conditioning `W=w`,

`Q_w = F_w(U) + 2 U^T M V + ell_w^T V + d_w`,                         (2.1)

where `F_w` is completely arbitrary, `M` is a fixed physical cross block, and the quadratic block on the `V` bank is exactly zero. Let `s1>=s2>0` be the two largest singular values of `M`. Then the full unconditional law has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 2 sqrt(pi) (s1 s2)^(-1/2).`                 (2.2)

No rank assumption is made beyond `s2>0`; all additional singular directions only help the norm estimate below. Arbitrary same-bank curvature on `U`, arbitrary outside curvature, and every outside coupling are retained through conditioning.

### Proof

Condition on `(W,U)`. Put

`c=M^T U+ell_w/2`.                                                       (2.3)

The remaining random part is the linear form `2 c^T V`. The sharp scalar product-projection bound gives a density cap at most

`sqrt(2)/(2||c||)=1/(sqrt(2)||c||)`.                                    (2.4)

Let `u1,u2` and `v1,v2` be the first two left/right singular vectors of `M`. Project `c` onto `span(v1,v2)`. If

`Y=(u1^T U,u2^T U)`,                                                    (2.5)

then this projection is an affine translate of

`(s1 Y1,s2 Y2)`.                                                        (2.6)

The two-dimensional product-projection theorem bounds the joint density of `Y` by `2`. Therefore the vector in (2.6), including its affine translation, has a probability density bounded by

`K=2/(s1 s2)`.                                                          (2.7)

Because `||c||` dominates the Euclidean norm of its two-dimensional projection, the two-dimensional bathtub inequality gives

`E[||c||^(-1)]
 <= K int_(|z|<=R) |z|^(-1) dz
 =2 sqrt(pi K)
 =2 sqrt(2pi/(s1 s2)),`                                                 (2.8)

where `pi R^2=1/K`. Averaging (2.4) gives exactly (2.2). QED.

### r47 payment

On the partner's robust full cut (1.1), `s1 s2=sqrt(x1 x2)>sqrt(kappa)`. Hence if either side of that literal full partition is an untwisted bank as in (2.1), then

`boxed: ||p_Q||_infinity < 2 sqrt(pi) kappa^(-1/4)
                         =4.380627393.`                               (2.9)

This is a genuine payment of a nontrivial r47 survivor subbranch. It is an essential-density theorem; no continuity claim is made from (2.2) alone.

## 3. New Fourier theorem — arbitrary fully entangled physical 2x2 crossing

The preceding B02 run paid two isolated hyperbolic pairs. The next theorem removes the isolated-pair/diagonal-crossing requirement.

### Theorem `QFORM-FULL2X2-ONESIDED-TWIST-L1-v1`

Let `U1,U2,V1,V2` be four literal independent original coordinates with densities at most one. Let `W` contain every other original coordinate. Suppose that after conditioning `W=w`,

`Q_w = F_w(U1,U2) + 2 U^T C V + ell_w^T V + d_w`,                    (3.1)

where `C` is any invertible real `2x2` physical cross block and `F_w` is arbitrary. The `V`-bank quadratic block is exactly zero; no condition is imposed on the `U`-bank quadratic block. Then

`boxed: integral_R |phi_Q(t)| dt
        <=16 pi sqrt(60) |det C|^(-1/2),`                             (3.2)

so `Q` has a continuous `C0` density. Independently, the sharper direct height estimate is

`boxed: ||p_Q||_infinity <=2 |det C|^(-1/2).`                        (3.3)

Thus a fully entangled physical `2x2` crossing is just as good for the direct height estimate as two isolated matching edges; the Fourier constant is larger because it is routed through the rank-two half-Riesz theorem rather than pairwise factorization.

### 3.1 Fourier-L1 proof

Write

`L=C^T U+ell_w/2`,                                                     (3.4)

and let `psi_1,psi_2` be the characteristic functions of `V1,V2`. Then

`phi_w(t)=E_U exp(it(F_w(U)+d_w)) psi_1(2tL1) psi_2(2tL2)`.            (3.5)

Take absolute values only after preserving the original product variables. Tonelli and Cauchy--Schwarz in `t` give

`||phi_w||_1
 <= pi E_U |L1 L2|^(-1/2)`,                                         (3.6)

because Plancherel and `f_{V_j}<=1` imply

`int |psi_j(2tLj)|^2 dt <= pi/|Lj|`.                                 (3.7)

The quadratic part of the scalar polynomial `L1L2` in the two physical variables `U` is

`S=C J C^T`, `J=[[0,1/2],[1/2,0]]`,                                  (3.8)

hence

`|det S|=|det C|^2/4`.                                                (3.9)

Apply the completed in-range rank-two affine half-Riesz theorem at this actual polynomial. Since the ambient input here is exactly two-dimensional, every affine term lies in the quadratic range:

`E_U |L1L2|^(-1/2)
 <=16 sqrt(30)|det S|^(-1/4)
 =16 sqrt(60)|det C|^(-1/2).`                                        (3.10)

Substitution into (3.6) is (3.2), uniformly in `w` and `F_w`. Since `phi_Q=E_W phi_w`, Tonelli transfers the same `L1` bound to the unconditional characteristic function. Fourier inversion gives a continuous density vanishing at infinity.

### 3.2 Direct height proof

Condition on `(W,U)`. The remaining random variable is

`2L1 V1+2L2 V2`                                                        (3.11)

plus a deterministic shift. Convolution cannot increase a density supremum, so its conditional density height is at most

`1/[2 max(|L1|,|L2|)]`.                                               (3.12)

The transformed vector `L=C^T U+ell_w/2` has a probability density bounded by

`K=|det C|^(-1)`.                                                      (3.13)

For the decreasing `l_infinity`-radial kernel `1/(2||x||_infinity)`, bathtub places the cap-`K` density on the centered square of radius `r=1/(2sqrt(K))`. Therefore

`E [1/(2||L||_infinity)]
 <= K int_(||x||_infinity<=r) [2||x||_infinity]^(-1) dx
 =4Kr
 =2 sqrt(K)
 =2|det C|^(-1/2),`                                                   (3.14)

which proves (3.3).

The theorem uses neither post-rotation independence nor law-uniform pointwise quadratic decay.

## 4. Exact-target stress family: r47's strong carrier-aligned hub is real even when all D'/D5 currency vanishes

Take five literal original coordinates ordered

`(h,u1,u2,v1,v2)`.                                                     (4.1)

Let

`C=(1/sqrt(2)) [[1,1],[1,-1]]`,                                      (4.2)

and define the symmetric coefficient matrix by

`A_(h,u1)=A_(u1,h)=1`,

`A_[{u1,u2},{v1,v2}]=C`,                                             (4.3)

with all other entries zero. Equivalently,

`Q=2 h u1 + 2 U^T C V`.                                               (4.4)

### 4.1 Exact owner-target spectrum

Reorder the coefficient coordinates as `{h,v1,v2} | {u1,u2}`. The matrix is bipartite with rectangular block `B` satisfying

`B^T B = diag(2,1)`.                                                   (4.5)

Hence

`spec(A)={-sqrt(2),-1,0,1,sqrt(2)}`.                                 (4.6)

The family therefore satisfies the owner target with four eigenvalues of modulus at least one.

### 4.2 Equation-level application of fleet03/B02 r47

Use the literal full cut

`L={h,u1,u2}`, `R={v1,v2}`.                                          (4.7)

Its crossing is

`N=[[0,0],[C row 1],[C row 2]]`,                                    (4.8)

so its two nonzero singular values are both one and

`x1*x2=1>247/576`.                                                    (4.9)

For the physical hub `h`, the partner's four alignment quantities are exactly

`ell_h=0`, `q_h=0`, `d_h=0`, `g_h=1`.                               (4.10)

Thus neither r47 physical-`E3` escape fires, the hub is not a near-coloop, and the family lands exactly in the partner's unpaid carrier-aligned strong-hub branch

`g_h>1/(228 sqrt(2))`.                                                (4.11)

This is not a loose-constant artefact: the residual transverse quantities vanish identically while the aligned hub stays order one.

### 4.3 D', D5, and the reviewed sharp-HY receiver on the actual physical cuts

Because there are only five coordinates, disjoint physical row and column sets satisfy `|I|+|J|<=5`, hence every physical cross block has rank at most two. Therefore, exactly,

`boxed: E3(A[I,J])=0 for every disjoint I,J,`                         (4.12)

`boxed: E5(A[I,J])=0 for every disjoint I,J.`                         (4.13)

So D', its reviewed sharp-HY/marginal-free `E3` refinement, and D5 all have zero exterior currency on every literal physical cut. This is an exact-target obstruction to any attempt to close the r47 strong-hub endpoint by insisting that one of those currencies must become uniformly positive.

It is **not** a QFORM counterexample and **not** a counterexample to target-wide Fourier `L1`.

### 4.4 The new receiver pays the same family uniformly

Condition on the outside physical coordinate `h`. In (3.1), the active crossing is exactly the fully entangled Hadamard block `C`, `|det C|=1`, and

`F_h(U)=2 h u1`.                                                       (4.14)

Theorem 3 therefore gives, for every admissible rough product law,

`boxed: integral_R |phi_Q(t)|dt <=16 pi sqrt(60)
                                    =389.354752894... ,`             (4.15)

`boxed: ||p_Q||_infinity <=2.`                                       (4.16)

The density is continuous and vanishes at infinity. Thus the correct payment here comes from a source-preserving **second exterior degree** plus one-sided linearity, not from manufacturing nonexistent third/fifth physical exterior volume.

The deterministic check file in this run enumerates all `3^5=243` disjoint-cut assignments, confirms maximum physical cross-block rank two, reproduces (4.6), and verifies (4.9)-(4.10); status `PASS`.

## 5. What this changes in the B02 proof graph

This run strictly enlarges the paid analytic chamber in two directions:

1. A robust rank-two physical crossing with an exactly untwisted bank is paid at the **aggregate singular-value level**, without selecting one good physical minor: on the r47 scale the essential-density constant is below `4.381`.
2. When a literal invertible physical `2x2` crossing is exposed, all four cross edges may be present and arbitrary curvature on the opposite bank is harmless. The branch then has genuine Fourier `L1`, with direct height `2|det C|^(-1/2)`.

The exact stress family shows that the r47 carrier-aligned strong-hub endpoint can have `E3=E5=0` identically while still being uniformly Fourier-integrable. Therefore another D'/D5-forcing iteration would not attack the real remaining mechanism.

The first unpaid implication is now

`QFORM-R47-STRONGHUB-TWOSIDED-CURVATURE-OR-DIFFUSE-E2-L1-v1`:

starting from the r47 robust rank-two full cut plus the fixed `V1`/diagonal/carrier-aligned-hub/near-coloop survivor, either expose an untwisted-bank packet covered by Theorem 2, expose a physical invertible `2x2` packet covered by Theorem 3, or retain **quadratic curvature on both source banks** inside a new integrated Fourier receiver. In the diffuse rank-two case no uniformly large single `2x2` minor may exist, so the next Fourier mechanism should spend aggregate `E2`/projected density rather than reintroduce a one-good-minor premise. The two-sided curvature case is genuine: the per-variable Plancherel step in (3.7) is no longer valid after arbitrary quadratic twists on both `V` coordinates, and the phase-aligned-support correction forbids replacing it by false pointwise Fresnel decay.

No exact-target QFORM counterexample was found.

## 6. Correction boundary

No step above uses an arbitrary-joint coarea bound, conditional projection-density supremum, post-rotation independence, law-uniform pointwise quadratic-phase decay, moment/tail truncation, coefficient-smallness as a random perturbation, a one-good-minor theorem, or one-heavy-row same-square absorption. D'/D5 are used on their exact physical scopes and, in the five-coordinate stress family, their failure is an exact zero-volume obstruction rather than a numerical smallness claim.

Telemetry not exposed by the runtime remains `UNKNOWN/null`; elapsed wall time is not represented as pure thinking time.
