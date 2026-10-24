SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-24T06:44:52Z.
attacking: the singular/definite physical-pair survivor by routing rank-one hub pairs into an aggregate mixed frame before any pair determinant is inverted.

# account02/B09 r19 — singular hub-pair routing: diffuse frame, double retention, and the weak-coupling obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid obstructions  
Run: `20260924T064452Z-account02-B09-QFORM-r19`  
Status: **NEW SUPPORTING COROLLARY + REQUIRED SOURCE APPLICATIONS + PRECISE REMAINING OBSTRUCTION / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**

All random variables below are literal original source coordinates. Inputs are arbitrary independent real variables with probability densities bounded by one. No moment, support, connectedness, log-concavity, iid, Gaussian, diagonal-basis, or post-rotation-independence assumption is used. Deterministic orthogonal changes of basis appear only when computing matrix spectra; they are never used to claim independence of transformed random variables.

## 1. First unpaid implication

The latest completed designated partner account03/B09 r45 gives a polynomialized aggregate receiver for invertible indefinite physical pairs, but also proves that the owner spectral hypothesis does not force such a pair resource: a target-valid rank-two-cross packet can have every relevant physical `2 x 2` pair singular. The next B09 debt is therefore not another reciprocal-minor estimate.

This run narrows it to

`QFORM-SINGULARDEFINITE-GENERAL-CURVATURE-COMPILER-v1`:

> In the chamber where the aggregate indefinite-pair resource is small or zero, compile the coefficient mass before pair selection into one of: (i) a source-coordinate mixed frame, allowing retained hub densities; (ii) a grouped crossing/volume receiver; or (iii) a genuinely bounded physical core. The compiler must retain arbitrary same-bank quadratic curvature exactly. It may not treat small matrix norm as a small random perturbation.

Two singular rank-one hub-pair endpoints are paid below. A third calculation shows exactly why retained-hub smoothing alone cannot be uniform through the weak-coupling limit exposed by the partner no-go family.

## 2. Source inputs used

### 2.1 Required pinned mixed-hub theorem

Use the proved Theorem H at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For a literal split `H union I union J`, if

`A_II = D + sum_{k=1}^r lambda_k v_k v_k^T`

with `D` diagonal, and the mixed rows

`rho_i=((v_k)_i ; A_{ih}, h in H)`

have positive Gram `G=sum rho_i rho_i^T` and normalized leverage at most `1/2`, then

`|phi_Q(t)| <= (2|t|)^(-|H|) prod_k(4 pi |t lambda_k|)^(-1/2) (4 pi)^(r+|H|) det(G)^(-1/2)`.

The physical hub core and all outside blocks are arbitrary. There is no Weyl-differencing square of the probability.

### 2.2 Previous B09 retained-hub extension

The immediately preceding account02/B09 result proved that selected hub densities may be left inside the same Brascamp--Lieb integral. If

`Gbar = sum_i rho_i rho_i^T + sum_{a in S} e_a e_a^T`,
`c_i=rho_i^T Gbar^(-1)rho_i <= 1/2`,
`b_a=e_a^T Gbar^(-1)e_a`,
`Bsum=sum b_a`,
`alpha=|H|+r/2-Bsum>1`,

then

`|phi_Q(t)| <= K |t|^(-alpha)`

with

`K=(prod_a b_a^(-b_a/2)) 2^(-|H|+Bsum) (4 pi)^alpha
   (prod_k |lambda_k|)^(-1/2) det(Gbar)^(-1/2)`,

and

`||p_Q||_infinity <= alpha/[pi(alpha-1)] K^(1/alpha)`.

The proof keeps original-coordinate product provenance and gives a continuous density.

### 2.3 Latest designated partner

Account03/B09 r45, commit `73d75d3dfda80b1025e756b7c68fab50b2a8cc20`, proves for a literal three-coordinate packet `P` with rank-two cross block `C` the exact identity

`det(P^2+CC^T)=(det P)^2+sum_k ||g_k||^2+Delta^2||Pn||^2`,

and an aggregate indefinite-pair density receiver

`||p_Q||_infinity <= 17.275934 R_pair^(-1/8)`

when

`R_pair=sum_{k in E} kappa_k^2[(det P)^2+||g_k||^2]>0`.

Its deterministic checker passed all recorded assertions. It also gives a target-valid family with `R_pair=0`, so a universal forcing theorem for this pair currency is false.

## 3. New specialization — `QFORM-TWOHUB-DOUBLE-RETENTION-v1`

Consider the two-hub/one-square case `|H|=2`, `r=1`. Suppose the literal mixed Gram is normalized to

`G=sum_i rho_i rho_i^T=I_3`,

where coordinates in the mixed frame are ordered `(v,U,V)`. Retain both physical hub densities, `S={U,V}`. Then

`Gbar=diag(1,2,2)`,
`det Gbar=4`,
`b_U=b_V=1/2`,
`Bsum=1`,
`alpha=2+1/2-1=3/2`.

Assume only the **augmented** source-row gate

`rho_i^T diag(1,1/2,1/2) rho_i <= 1/2`                     (3.1)

for every literal leaf row. This is strictly weaker in the hub directions than pinned Theorem H's gate: a pure physical hub-partner row of original leverage one is permitted.

Then the full ambient form, with arbitrary hub core and arbitrary allowed outside blocks/affine terms, has a continuous density and

`boxed: ||p_Q||_infinity <= 6 |lambda|^(-1/3)`,             (3.2)

`boxed: P{Q in L} <= 6 |lambda|^(-1/3) |L|`.               (3.3)

### Proof and constant

In the retained-hub formula,

`prod_a b_a^(-b_a/2)=2^(1/2)`,
`2^(-|H|+Bsum)=2^(-1)`,
`(4 pi)^alpha=(4 pi)^(3/2)`,
`det(Gbar)^(-1/2)=1/2`.

Therefore

`K=2 sqrt(2) pi^(3/2) |lambda|^(-1/2)`

and

`|phi_Q(t)| <= K |t|^(-3/2)`.

Since

`integral_R min(1,K|t|^(-3/2)) dt = 6 K^(2/3)`,

Fourier inversion gives

`||p_Q||_infinity <= (3/pi)K^(2/3)=6 |lambda|^(-1/3)`.

No square-root decoupling or reciprocal physical minor occurs.

## 4. Actual target-valid maximally localized singular-hub family

Let `m>=2`, let `q in R^m` be a flat unit vector, and use literal independent coordinates `U,V,Y0,Y1,Y_T`. Define

`Q_loc = 2(U+V)^2 + 2 U Y0 + 2 V Y1 + <q,Y_T>^2`.          (4.1)

The physical hub core is

`B=2[[1,1],[1,1]]`,                                                    (4.2)

which is rank-one positive semidefinite: `det B=0`.

For deterministic spectral bookkeeping only, put

`u_+=(U+V)/sqrt(2)`, `u_-=(U-V)/sqrt(2)`,
`y_+=(Y0+Y1)/sqrt(2)`, `y_-=(Y0-Y1)/sqrt(2)`.

The active coefficient matrix is orthogonally equivalent to

`[[4,1],[1,0]] direct_sum [[0,1],[1,0]] direct_sum [1]`,     (4.3)

so

`spec_nonzero(A)={2+sqrt(5), 2-sqrt(5), 1, -1, 1}`.         (4.4)

Thus the owner's three-large-eigenvalue hypothesis holds.

Use `H={U,V}`, `I={Y0,Y1} union T`, `r=1`, `lambda=1`. The mixed rows are

`rho_0=(0,1,0)`,
`rho_1=(0,0,1)`,
`rho_i=(q_i,0,0)` for `i in T`.                              (4.5)

Hence `G=I_3`. Both private-partner rows have original leverage exactly one, so pinned Theorem H fails maximally. Conditioning away `U` leaves the `V-Y1` row at leverage one, and conditioning away `V` leaves the `U-Y0` row at leverage one; the obvious one-hub Theorem-H routes therefore also fail.

After retaining both hub densities, (3.1) gives leverage exactly `1/2` for `Y0,Y1` and `q_i^2=1/m<=1/2` on `T`. The new specialization applies:

`boxed: ||p_Qloc||_infinity <= 6`,                              (4.6)
`boxed: P{Q_loc in L} <= 6 |L|`.                                (4.7)

The density is continuous. This pays a maximally localized two-coloop endpoint while the dense same-side block `q q^T` remains in the physical source coordinates.

## 5. Required direct application of pinned Theorem H: diffuse singular hub pair

The same singular physical hub core can instead have diffuse partner rows. Let `m=2^k>=8`, choose flat orthonormal Walsh vectors `c,d,q in R^m`, and set

`Q_diff = 2(U+V)^2
       + 2 U <c,Y>
       + 2 V <d,Y>
       + <q,Y>^2`.                                             (5.1)

Again the hub core is the singular rank-one matrix (4.2), and the same-side leaf block `q q^T` is dense in the literal coordinates. In the deterministic coefficient basis obtained by rotating the two hub directions together with `c,d`, the active spectrum is again

`{2+sqrt(5), 2-sqrt(5), 1, -1, 1}`,                           (5.2)

so this is target-valid.

For pinned Theorem H, `H={U,V}`, `r=1`, and

`rho_i=(q_i,c_i,d_i)`.

Orthogonality gives `G=I_3`, while flatness gives every physical leverage

`q_i^2+c_i^2+d_i^2=3/m<=3/8<1/2`.                             (5.3)

Therefore the **completed pinned result** gives

`|phi_Qdiff(t)| <= 8 pi^(5/2) |t|^(-5/2)`.                    (5.4)

Exact integration of this envelope yields

`boxed: ||p_Qdiff||_infinity <= (5/3) 2^(6/5)
       = 3.828994516656783...`,                                (5.5)

and the same coefficient times interval length. The density is continuous. The physical singular hub determinant never appears; the two hub directions and the dense leaf square are spent jointly before any physical-pair inversion.

This is the requested mixed-hub smoothing on an actual source-coordinate star with dense same-side coupling and no square-root decoupling loss.

## 6. Latest partner r45 applied with a dense same-side residual

Take the partner regression packet

`P=[[0,1,1],[1,0,1],[1,1,0]]`,
`C=(1/2)[[1,0],[0,1],[0,0]]`,                                  (6.1)

and add a disjoint literal bank `W` carrying an arbitrary dense rank-one same-side term `<q,W>^2`. Thus

`Q = Y^T P Y + 2 Y^T C Z + <q,W>^2`,                            (6.2)

with all variables independent and cap one. The partner theorem permits the entire residual in the disjoint variables, so its pair currencies are unchanged:

`det P=2`, `D_1=D_2=D_3=4.5`, `R_pair=13.5`.                    (6.3)

The five-coordinate principal packet in `(Y,Z)` has spectrum

`{-1.20710678,-1.08113883,0,0.20710678,2.08113883}`,            (6.4)

hence is already target-valid; adding the disjoint dense square cannot invalidate the three-large-eigenvalue condition. Account03/B09 r45 therefore gives the actual full-law inequality

`boxed: ||p_Q||_infinity <= 12.478138789189643`,                 (6.5)
`boxed: P{Q in L} <= 12.478138789189643 |L|`.                    (6.6)

This is an essential-density/linear-small-ball conclusion; r45 does not separately assert continuity.

## 7. Weak-coupling obstruction: retained hubs cannot by themselves close the partner no-go family

The partner's source-valid no-go family is

`P=2[[1,1,1],[1,1,-1],[1,-1,1]]`,
`C_eps=eps [[1,0],[0,1],[0,0]]`,
`A_eps=[[P,C_eps],[C_eps^T,0]]`,                                 (7.1)

with `0<eps<=1/2`. Its three large eigenvalues remain uniformly large, but every `2 x 2` principal pair inside `P` is singular and `R_pair=0`.

Condition on the third core coordinate and look only at the first two coordinates as physical hubs. With no transverse Fresnel square (`r=0`), the two partner rows have mixed Gram

`G=eps^2 I_2`                                                        (7.2)

and each has leverage one. Retaining both hub densities gives

`Gbar=(1+eps^2)I_2`,
`b_1=b_2=1/(1+eps^2)`,
`alpha=2-2/(1+eps^2)=2 eps^2/(1+eps^2)`.                        (7.3)

For every `eps<=1/2`, `alpha<=2/5<1`. Thus the retained-hub Fourier envelope is **not integrable**. This is an exact obstruction to closing the partner's weak-coupling survivor merely by retaining the two hub densities.

The obstruction is to this proof mechanism, not to QFORM. The same family has a literal three-coordinate core `P` with eigenvalues `{-2,4,4}`. The completed physical three-coordinate theorem recorded in the pinned counterexample-search source gives, after conditioning on the two cross-bank coordinates,

`boxed: ||p_Q||_infinity <= 6 sqrt(pi)/2 = 3 sqrt(pi)
       = 5.317361552716548...`,                                  (7.4)

uniformly in `eps`. Hence the partner no-go family itself routes to a finite-core receiver; what remains is the genuinely nonlocalized singular/definite chamber where neither that core nor a uniformly nondegenerate augmented frame is available.

The order-of-operations lesson is precise: when cross scale tends to zero, hub-density retention spends almost all available Fourier power (`Bsum -> 2`) before an integrable exponent is reached. A full structural compiler must instead spend strong core curvature, grouped crossing volume, or another independent source-coordinate smoothing resource before taking any reciprocal weak coupling.

## 8. Resulting proof frontier

The singular physical-pair chamber now has three explicit paid exits:

1. **diffuse mixed partners + dense leaf square:** pinned Theorem H, (5.5), continuous;
2. **two maximally localized private partners + dense leaf square:** double hub retention, (4.6), continuous;
3. **weak cross but a uniformly nonsingular literal three-coordinate core:** physical finite-core theorem, (7.4).

The latest partner's positive aggregate pair currency remains a fourth exit, (6.5), for the invertible-indefinite chamber.

The first unpaid implication is therefore exactly `QFORM-SINGULARDEFINITE-GENERAL-CURVATURE-COMPILER-v1`: prove that failure of these exits forces an already-paid grouped crossing/volume configuration, or construct a valid full-target counterexample. The difficult missing point is arbitrary dense same-bank curvature entangled with a weak singular/definite pair when no bounded physical core is available. Small coefficient/Frobenius error cannot be discarded probabilistically under arbitrary unbounded cap-one input laws.

No valid counterexample to the full QFORM target is produced here. The required pinned counterexample source also reports none. Full unrestricted essential boundedness and full-target continuity remain OPEN.
