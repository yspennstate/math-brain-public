SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T09:37:09Z.
attacking: near-collinear zero-anchor arbitrary-background receiver: isolate genuinely transverse same-bank curvature and convert it to aggregate bordered cross-volume before reciprocal payment.

# fleet01/B06 r29 — transverse background budget and bordered cross-volume receiver

## Status and scope

Status: **NEW SUPPORTING STRUCTURAL THEOREMS + TWO ACTUAL RECEIVER APPLICATIONS / FULL QFORM OPEN**. No counterexample to the owner target is claimed. The new statements concern the zero-anchor/two-hub chamber that survives the previous curved-fiber and grouped-hub exits. Essential boundedness is obtained on the explicitly certified branches below; global continuity remains open. The newest Claude volume theorem gives continuity on its certified branch.

All coordinates in the argument are ORIGINAL independent coordinates. Orthogonal changes below are used only to prove deterministic matrix identities such as singular-value or compound-volume formulas; no probabilistic independence is transferred through those rotations.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

### Source-valid inputs actually used

1. **Designated partner fleet02/B06, r30-ish latest handoff.** `QFORM-SHARED-COEFFICIENT-MAX-RECIPROCAL-v1`, canonical source `yspennstate/math-open-problems@2fdec7c0b085cb5acf5a09847b293b5bcb296b80`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260923T083202Z-7358ab1fe71c/REPORT.md`. If `X,Y` are independent cap-one scalars, independent of a background `Omega`, and `(U,V)` is a background-measurable pair with joint density cap `K`, then `2XU+2YV+R(Omega)` has continuous density at most `2 sqrt(K)`. For affine product projections `U=a.Z+u0`, `V=b.Z+v0`, the earlier weighted affine-fiber BL theorem gives `K<=e/Delta`, where
   
   `Delta=sqrt(||a||^2||b||^2-(a.b)^2)`.
   
   Hence
   
   `||p||inf <= 2 sqrt(e/Delta)`.                                      (0.1)

2. **Newest Claude volume-sampling theorem D'.** Source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, path `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. For any ORIGINAL-coordinate cross block `M=A_IJ`, let `Z_3=E_3(M)=e_3(MM^T)`, and let `alpha_i` be the row marginals of squared-minor volume sampling. If `max_i alpha_i<=h<3/4`, then, with arbitrary self blocks, outside conditioning and affine terms,
   
   `||p_Q||inf <= C_h Z_3^(-1/6)`,                                   (0.2)
   
   where
   
   `C_h=6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1)`.
   
   In particular `C_{1/2}=6 sqrt(e)`. This is an integrated Fourier/product theorem, not a pointwise scalar stationary-phase estimate.

3. The current live corrections are retained: no arbitrary-joint rank-three coarea bound, no post-rotation independence, no law-uniform pointwise quadratic-phase decay, no worst conditional-density moment/supremum, and no unrestricted spectral-fiber supremum.

## 1. Chamber and notation

After conditioning any outside ORIGINAL coordinates, consider the quadratic part

`A = [[0,0,a^T], [0,0,b^T], [a,b,C]]`,                              (1.1)

with two physical hub coordinates `X,Y` and a product bank `Z`. Affine terms created by conditioning are harmless for both input theorems above. Write the two-by-m star coefficient matrix

`B = [a^T; b^T]`.                                                     (1.2)

Let `s=s_3(A)`; in the owner target `s>=1` after the usual normalization of the selected three-large-eigenvalue scale.

The purpose of this report is to avoid paying a reciprocal of one physical coefficient or one physical minor. Two aggregate quantities are used instead:

- the full coefficient-plane area `Delta(a,b)`;
- an aggregate third volume of a bordered cross block after a physical split of the Z-bank.

## 2. First receiver: a star-area/background-curvature dichotomy

Let

`S = [[0,0,a^T], [0,0,b^T], [a,b,0]]`.                              (2.1)

The nonzero singular values of the symmetric star `S` are

`s_1(B), s_1(B), s_2(B), s_2(B)`.                                    (2.2)

Therefore

`s_3(S)=s_2(B)`.                                                      (2.3)

Since `A=S+diag(0,0,C)`, singular-value Weyl gives

`boxed: s_3(A) <= s_2(B)+||C||op.`                                   (2.4)

The coefficient-plane area satisfies

`Delta(a,b)=sqrt(det(BB^T))=s_1(B)s_2(B)>=s_2(B)^2`.                 (2.5)

Consequently, if the background curvature is small in operator norm,

`||C||op <= s/2`,                                                     (2.6)

then `s_2(B)>=s/2`, so

`Delta(a,b)>=s^2/4`.                                                  (2.7)

Now apply the **designated partner fleet02/B06 theorem at the actual density inequality** (0.1):

`boxed: ||p_Q||inf <= 4 sqrt(e)/s`                                   (2.8)

on branch (2.6). Under `s>=1`, the numerical constant is `<6.595`.

This closes the entire small-background branch without inspecting a single physical star entry. It also gives the contrapositive structural fact that every unpaid small-area branch must carry target-scale background curvature.

## 3. Stronger near-collinear budget: only genuinely transverse C counts

Suppose `a!=0` and decompose

`b=lambda a+epsilon`, `epsilon perp a`.                              (3.1)

Put `u=a/||a||` and `P=I-uu^T`. Define

`C_0=C-PCP`.                                                         (3.2)

Construct `H` from `A` by replacing `b` by `lambda a` and `C` by `C_0`. In the orthogonal decomposition of the Z-space as `span{u} direct_sum u^perp`, put the single `u` coordinate last. Every entry of `H` among the remaining leaves (`X,Y,u^perp`) is zero: the collinear star and `C_0` only connect those leaves to the central coordinate `u`, with a possible diagonal entry at `u`. Thus

`H = [[0,v],[v^T,c]]`                                                (3.3)

for a suitable vector `v`, and in particular

`rank(H)<=2`.                                                        (3.4)

The difference is

`A-H = epsilon-star + diag(0,0,PCP)`,                                (3.5)

where the symmetric star joining the physical hub `Y` to `epsilon in u^perp` has operator norm exactly `||epsilon||`. Hence

`||A-H||op <= ||epsilon||+||PCP||op`.                                (3.6)

Eckart--Young (`s_3(A)=inf_{rank R<=2}||A-R||op`) gives the sharper budget

`boxed: s_3(A) <= ||epsilon|| + ||P_{a^perp} C P_{a^perp}||op.`       (3.7)

This strictly refines the partner r30 inequality `s_3(A)<=||epsilon||+||C||op`: curvature confined to the central `a` row/column belongs to a rank-two arrowhead and cannot pay the third singular direction.

In particular, if `s>=1` and `||epsilon||<s/4`, then

`||P C P||op > 3s/4`.                                                (3.8)

### Quantitative trichotomy with the partner receiver

Choose the larger of the two physical star rows as the base row `a`. Then

`||a|| >= s_1(B)/sqrt(2)`.                                          (3.9)

If `s_1(B)>s/2` and

`Delta(a,b) >= delta s^2`,                                          (3.10)

the partner theorem yields

`||p_Q||inf <= 2 sqrt(e)/(sqrt(delta) s)`.                           (3.11)

If instead `Delta<delta s^2`, then from `Delta=||a||||epsilon||` and (3.9),

`||epsilon|| < 2 sqrt(2) delta s`,                                  (3.12)

so (3.7) gives

`||PCP||op > (1-2 sqrt(2) delta)s`.                                 (3.13)

For example, with `delta=1/(8 sqrt(2))`, either

`||p_Q||inf <= 2 sqrt(e) sqrt(8 sqrt(2))/s < 11.10/s`,               (3.14)

or

`||PCP||op > 3s/4`.                                                  (3.15)

If instead `s_1(B)<=s/2`, Weyl applied in the other direction to the block-diagonal background gives

`s_3(C) >= s_3(A)-||S||op >= s/2`.                                  (3.16)

Thus after the partner receiver, the unpaid geometry has been reduced to a background carrying genuine spectral curvature: either `C` itself has three target-scale singular directions, or the near-collinear chamber has a target-scale compression on `a^perp`.

## 4. Exact same-hub third-compound identity

The transverse compression in (3.7) has an exact aggregate physical-minor representation. Consider the one-hub matrix

`K=[[0,g^T],[g,C]]`.                                                  (4.1)

Let index `0` denote the hub. Then

`boxed:
 sum_{j<k} sum_{l<m}
 det K[{0,j,k},{0,l,m}]^2
 = ||g||^4 ||P_{g^perp} C P_{g^perp}||_F^2.`                         (4.2)

**Proof.** The left side is the squared Frobenius norm of the block of the third compound `wedge^3 K` acting on the invariant coordinate subspace `e_0 wedge wedge^2(R^m)`. It is unchanged by an orthogonal change inside the Z-space. Rotate `g` to `G e_1`, `G=||g||`. A minor in (4.2) vanishes unless its row pair and column pair both contain coordinate `1`. For residual indices `r,s>=2`,

`det K[{0,1,r},{0,1,s}] = -G^2 C'_{rs}`,                             (4.3)

where `(C'_{rs})_{r,s>=2}` is exactly the rotated compression `P_{g^perp}CP_{g^perp}`. Summing squares proves (4.2). QED.

This identity explains why single-minor selection is the wrong scale in the diffuse endpoint: a target-scale transverse curvature can be spread over arbitrarily many mixed physical triples while its **total third-compound mass** remains fixed.

## 5. Physical split: bordered cross third-volume theorem

Now physically split the product bank as `Z=(Z_S,Z_T)`, with `S cap T=emptyset`. Put

`I={X} union S`, `J={Y} union T`.                                    (5.1)

The ORIGINAL-coordinate cross block is

`M=A_IJ=[[0,a_T^T],[b_S,C_ST]]`.                                    (5.2)

Assume `a_T` and `b_S` are nonzero and set

`q=a_T/||a_T||`, `p=b_S/||b_S||`,                                   (5.3)

`C_perp=P_{p^perp} C_ST P_{q^perp}`.                                (5.4)

### Theorem 5.1 — `QFORM-BORDERED-CROSS-THIRD-VOLUME-v1`

The full squared 3-volume of this cross block obeys

`boxed: E_3(M)>=||a_T||^2 ||b_S||^2 ||C_perp||_F^2.`                 (5.5)

**Proof.** The quantity `E_3(M)=e_3(MM^T)` is the sum of squares of all `3 x 3` minors and is invariant under orthogonal row and column changes. Rotate only the deterministic S-row and T-column Euclidean spaces so that `p=e_1`, `q=e_1`. For every residual row `r>=2` and residual column `c>=2`, select rows `(X,p,r)` and columns `(Y,q,c)`. The corresponding matrix has first row `(0,||a_T||,0)` and first column below the top equal to `(||b_S||,0)^T`; direct expansion gives

`det M[(X,p,r),(Y,q,c)]
 = -||a_T|| ||b_S|| (C_perp)_{rc}`.                                 (5.6)

These minors are a subset of the nonnegative sum defining `E_3(M)`. Summing their squares gives (5.5). QED.

No probabilistic rotation is made: the rotations appear only inside the invariant deterministic evaluation of the Cauchy--Binet sum.

## 6. Newest-Claude receiver applied to the bordered volume

Define the aggregate certificate

`kappa_ST = ||a_T|| ||b_S|| ||C_perp||_F`.                           (6.1)

Then (5.5) says

`E_3(M)>=kappa_ST^2`.                                                 (6.2)

Let `alpha_i(M)` be the row marginals of squared-minor volume sampling used in the newest Claude theorem D'. If, for this physical split,

`max_{i in I} alpha_i(M) <= h < 3/4`,                                (6.3)

then apply (0.2) at the actual cross block (5.2). Since all same-side quadratic blocks and all affine terms are allowed by theorem D',

`boxed:
 ||p_Q||inf <= C_h kappa_ST^(-1/3),
 C_h=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1).`                              (6.4)

For the clean gate `h=1/2`,

`boxed: ||p_Q||inf <= 6 sqrt(e) kappa_ST^(-1/3).`                    (6.5)

This is the promised weighted curved-fiber replacement in this chamber: the whole transverse block `C_perp` enters through the aggregate Cauchy--Binet volume before the Fourier/BL payment. There is no supremum over spectral fibers and no inverse of an individual physical 3-minor.

The newer volume-stability/tail continuation can also be applied to the **same M** whenever its explicit projection certificate passes: with `T2=sum_{j>=3}s_j(M)^2`, `max diag(P)<=1/2`, and `||(I-P)M||op<=sqrt(T2)/15`, it gives the continuous-density exit

`||p_Q||inf <= (9 sqrt(3)e/2)
 [s_1(M)^2 s_2(M)^2 T2]^(-1/6)`.                                    (6.6)

Thus a diffuse collective tail of the bordered cross block can be paid even when no single third singular direction is stable.

## 7. What changed and the exact remaining implication

Before this run the partner fleet02/B06 gap was:

> near-collinear star plus arbitrary same-bank curvature C; use `||epsilon||+||C||op>=s_3(A)` without selecting a physical coefficient.

The new derivation makes that substantially sharper:

1. **Small C is completely paid** by the partner theorem, with universal `<4 sqrt(e)/s`.
2. **Near-collinear unpaid C is genuinely transverse:** central-row/column curvature is removed by the rank-two arrowhead approximation, leaving (3.7).
3. That transverse curvature has an **exact aggregate third-compound identity** (4.2).
4. Every physical bank split has a **bordered aggregate cross-volume lower bound** (5.5), and any split passing the volume-marginal gate is paid immediately by newest Claude D' via (6.4).

The first unpaid implication is therefore now the explicit structural statement

`QFORM-TRANSVERSE-CURVATURE-CUT-OR-HUB-v1`:

> Assume the partner coefficient-plane area is below the universal payment threshold and `||P_{a^perp} C P_{a^perp}||op` is target-scale. Prove that either (i) some ORIGINAL-coordinate split `S,T` has `kappa_ST` bounded below at target scale and volume marginals `<3/4`, or (ii) the failure forces a previously paid heavy physical hub / physical-pair / grouped-bank / ridge-volume exit.

A proof cannot simply select a large entry of `C`: diffuse rank-one or higher-rank curvature may have every physical entry tending to zero. Nor can it condition on a spectral complement or use a worst fiber density. The same-hub compound identity (4.2) identifies the invariant mass that the missing cut/hub lemma must redistribute without dimension loss.

## 8. Continuity and review status

- Partner branch (0.1): continuous density by the partner theorem.
- Claude D'/tail-certified bordered branch: continuous density by the integrated Fourier estimate.
- Full target: still OPEN; no global continuity claim.
- Independent review of the new identities (3.7), (4.2), (5.5) and their splice has not yet been performed.

## 9. Sanity checks

Random finite-dimensional numerical checks (not proof) were used only to catch algebraic sign/index errors: over 100 random bordered matrices the computed Cauchy--Binet `E_3(M)` exceeded the right side of (5.5), and over 100 random symmetric chambers the inequality (3.7) held. The proofs above are exact and do not rely on these checks.
