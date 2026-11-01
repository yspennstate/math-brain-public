SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-24T09:12:45Z.
attacking: a sharp square-plus-one-crossing rearrangement theorem: one physical quadratic coordinate regularizes a rank-one product crossing with explicit Lp constants and logarithmic critical scaling.

# fleet01/B04 r33 — one square + one product crossing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: revision `2026-09-22.15`  
Status: **NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity in the theorem below: **continuous C_0 density is proved**.

## 1. Scope and source boundary

The unrestricted conjecture remains open. This run uses only original-coordinate conditioning and rearrangement/Young inequalities. It does **not** use law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, a bare bounded projection density as a replacement for curvature, or small-coefficient perturbation.

The live correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` is respected: a square plus one heavy off-diagonal coefficient does not absorb arbitrary quadratic curvature on that same second coordinate. The theorem below therefore requires that the second physical coordinate have exactly zero self-quadratic coefficient and zero mutual edge to the square coordinate. Curvature on every other coordinate is arbitrary.

A source-valid one-dimensional product projection cap `sqrt(2)` is recorded at
`yspennstate/math-open-problems@85c3d540cf82ea6a6aca0f22f31811516a8b81aa`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260923T013147Z-bf13c29b/REPORT.md`,
via Livshyts--Paouris--Pivovarov / Rogozin--Ball. The main theorem is stated with an abstract cap `M`, so this external input is needed only for the row-norm corollary.

The sharp scalar-square Lp rearrangement lemma used below was already proved in this slot at
`yspennstate/math-open-problems@08728154a68cb8f41ae42d97e1365e90a8b8db82`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260924T084623Z-fleet01-B04-QFORM-auto11-r32/REPORT.md`.
For completeness its one-line bathtub proof is repeated.

## 2. Main theorem

### Theorem — `QFORM-ZERODIAG-ONECROSS-SQUARE-REARRANGEMENT-v1`

Let the independent cap-one original coordinates be partitioned as

`{i,j} union K union O`.

Allow an arbitrary deterministic affine term as well as the quadratic form. Assume only

`b=A_ii !=0`,
`A_ij=0`,
`A_jj=0`.

Write

`v=A[j,K]`.

Assume the scalar original-product linear form

`S=v dot X_K`

has a density of essential supremum at most `M<infinity`. No assumption is made on `A[i,K]`, `A[i,O]`, `A[j,O]`, `A[K,K]`, `A[K,O]`, or `A[O,O]`.

Then, for every `1<p<2`, the full quadratic-plus-affine law has a density in `C_0(R)` and

`boxed:
 ||p_Q||_infinity
 <= [2^(p-1)/(2-p)]^(1/p) * p/(p-1)
    * |b|^(-(p-1)/p) * M^(1/p).`                                  (2.1)

At `p=3/2`,

`boxed:
 ||p_Q||_infinity <= 6 |b|^(-1/3) M^(2/3).`                       (2.2)

If `K={k}` is a single physical coordinate and `c=A_jk !=0`, then `M<=1/|c|`, hence

`boxed:
 ||p_Q||_infinity <= 6 |A_ii|^(-1/3)|A_jk|^(-2/3),
 p_Q in C_0(R).`                                                   (2.3)

If instead one uses the whole row bank, the one-dimensional product-projection theorem gives

`M<=sqrt(2)/||v||_2`,

and therefore

`boxed:
 ||p_Q||_infinity
 <=6*2^(1/3)|b|^(-1/3)||v||_2^(-2/3).`                            (2.4)

The important structural point is that the square coordinate `i` may couple arbitrarily to the crossing bank `K`; only the edge `ij` must vanish. Thus this is not the source-separated square theorem from r32.

## 3. Proof

Condition first on the original coordinates `X_O=o`. Their only effect on the two active coordinates is to create deterministic affine shifts. For fixed `o`, write the remaining form as

`Q = b X_i^2
   +2 X_i (r dot X_K + alpha_o)
   +2 X_j (v dot X_K + beta_o)
   +H_o(X_K),`                                                     (3.1)

where `H_o` is completely arbitrary. The identities `A_ij=A_jj=0` are exactly what make (3.1) contain no `X_i X_j` and no `X_j^2` term.

Now condition also on `X_K=y`. Put

`a_y=(r dot y+alpha_o)/b`,
`s_y=v dot y+beta_o`.

Up to an additive constant,

`Q | (X_K=y,X_O=o)
 = U_y + V_y`,

`U_y=b (X_i+a_y)^2`,
`V_y=2 s_y X_j`.                                                   (3.2)

The variables `U_y,V_y` are independent because they depend on two distinct original independent coordinates.

### 3.1 Sharp square Lp rearrangement

For a cap-one scalar density `f`, the density `h_a` of `(X-a)^2` satisfies

`h_a(u)=[f(a+sqrt(u))+f(a-sqrt(u))]/(2sqrt(u)) <=u^(-1/2)`, `u>0`,

and has mass one. Among all nonnegative mass-one functions under the cap `u^(-1/2)`, the decreasing-rearrangement/bathtub maximizer of the Lp norm is

`u^(-1/2) 1_[0,1/4](u)`.

Therefore, for `1<p<2`,

`int h_a(u)^p du <= int_0^(1/4) u^(-p/2)du
 =2^(p-1)/(2-p)`.                                                 (3.3)

Scaling by `b` gives

`||p_Uy||_p
 <= [2^(p-1)/(2-p)]^(1/p)|b|^(-(p-1)/p).`                        (3.4)

The bound is uniform in the moving shift `a_y`.

### 3.2 Linear factor and Young

Let `q=p/(p-1)`. Since every input density is at most one and has mass one,

`||f_j||_q<=1`.

Hence, when `s_y !=0`,

`||p_Vy||_q <=(2|s_y|)^(-1/p).`                                   (3.5)

Young/Hölder convolution gives

`||p_(Q|y,o)||_infinity
 <= C_p |b|^(-(p-1)/p)(2|s_y|)^(-1/p)`,                           (3.6)

where

`C_p=[2^(p-1)/(2-p)]^(1/p)`.

### 3.3 Translation-uniform fractional moment

If a scalar random variable `Z` has density cap `M`, then for every `0<alpha<1` and every shift `t`, decreasing rearrangement gives the sharp bound

`E|Z-t|^(-alpha)
 <= M * 2 int_0^(1/(2M)) r^(-alpha)dr
 = (2M)^alpha/(1-alpha).`                                         (3.7)

Apply this with `Z=v dot X_K`, `alpha=1/p`, and shift `-beta_o`. Thus, uniformly in `o`,

`E_K |s_y|^(-1/p)
 <=(2M)^(1/p) * p/(p-1).`                                        (3.8)

Averaging (3.6) and using (3.8), the factors `2^(-1/p)` and `2^(1/p)` cancel exactly, yielding (2.1).

### 3.4 Continuity

For almost every `y`, `s_y !=0` because `v dot X_K` has a density. For such `y`, `p_Uy in L^p` and `p_Vy in L^q` with `1<p,q<infinity`, hence

`p_Uy * p_Vy in C_0(R)`.

The right side of (3.6) is integrable over `(y,o)` by (3.8), uniformly in `o`. Dominated convergence therefore survives both averaging steps and proves that the unconditional representative belongs to `C_0(R)`.

This completes the theorem.

## 4. Critical logarithmic regime

The theorem also quantifies the exact critical transition to a bare rank-one crossing. Let the cap in (2.1) be `M` and set

`R=1/(|b|M)`.

If `R>e`, put `ell=log R>1` and choose

`p=1+1/ell`.

Then (2.1) becomes

`boxed:
 ||p_Q||_infinity
 <= M (ell+1) e^(ell/(ell+1))
    [2^(1/ell) ell/(ell-1)]^(ell/(ell+1)).`                        (4.1)

Hence, as `|b|M ->0`,

`||p_Q||_infinity <= (e+o(1)) M log(1/(|b|M)).`                   (4.2)

So one physical square regularizes the logarithmic singularity of a one-dimensional product crossing with only a logarithmic loss as the square coefficient tends to zero. No pointwise Fourier decay is used.

## 5. Exact three-coordinate target-valid rotated carrier

Take

`T = [[3/2, 0,   1/10],
      [0,   0,   2   ],
      [1/10,2,   0   ]].`                                         (5.1)

This is genuinely non-diagonal and indefinite. Write

`T0=[3/2] direct_sum [[0,2],[2,0]].`

The perturbation `T-T0` has operator norm exactly `1/10`, while

`spec(T0)={-2,3/2,2}`.

Weyl therefore places the eigenvalues of `T` inside

`[-2.1,-1.9]`, `[1.4,1.6]`, `[1.9,2.1]`                         (5.2)

in sorted order. Thus **all three eigenvalues have absolute value >1**, proving the exact owner spectral hypothesis without relying on floating-point diagonalization.

For `i=1,j=2,k=3`,

`b=3/2`, `A_12=A_22=0`, `c=A_23=2`.

Equation (2.3) gives the explicit law-uniform estimate

`boxed:
 ||p_(X^T T X)||_infinity
 <=6 (3/2)^(-1/3) 2^(-2/3)
 =6^(2/3)
 =3.301927248894626... ,
 p_(X^T T X) in C_0(R).`                                          (5.3)

Note that `A_13=1/10` is nonzero: the square coordinate itself couples to the crossing source coordinate, so this example is outside the source-separated square pattern of r32.

## 6. Completed designated partner applied on the same enlarged matrix

The completed designated partner result is fleet02/B04 r21:

`yspennstate/math-open-problems@bb6e1a7e2e46a3434649dfd1b6a4afe94d25e7fa`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/9a73ca69-5439-45c6-9b34-581521e6e6a2/REPORT.md`.

Its fully dense six-coordinate matrix `A_*` contains the physical principal triple

`2 I_3 +(199/200) 11^T`,

whose smallest eigenvalue is `2`. Using the completed physical-principal-block receiver, r21 obtains

`boxed: ||p_(X^T A_* X)||_infinity <=3 sqrt(pi).`                 (6.1)

That receiver explicitly allows arbitrary couplings from the principal triple to conditioned outside coordinates.

To apply both results to one actual matrix, set `eps=1/100` and

`Ahat = [[T, eps J_(3x6)],
        [eps J_(6x3), A_*]].`                                     (6.2)

The principal triple used by the partner is unchanged, so conditioning all six outside coordinates turns the new cross block only into affine terms. Therefore the partner result applies literally to `Ahat` and gives

`||p_(X^T Ahat X)||_infinity <=3 sqrt(pi)
 =5.317361552716548... .`                                         (6.3)

The new theorem also applies to the same `Ahat`: choose the single source coordinate `k=3`. After conditioning the six bottom coordinates, the `X_2` coefficient contains

`2 X_3 + constant`.

Translation does not change the density cap, so this scalar source has density cap at most `1/2`. Hence `M<=1/2`, and the new theorem gives

`boxed:
 ||p_(X^T Ahat X)||_infinity <=6^(2/3)
 =3.301927248894626... .`                                         (6.4)

Thus on this same coupled target matrix the new product-rearrangement estimate is sharper than the completed partner certificate by a factor

`3 sqrt(pi)/6^(2/3)=1.610381196162520...`.

The spectral target is rigorous. The top block `T` has all eigenvalue magnitudes at least `1.4` by (5.2). Partner r21 proves all six eigenvalues of `A_*` have modulus greater than `1.53`. The symmetric off-diagonal perturbation in (6.2) has operator norm

`||eps J_(3x6)||=eps sqrt(18)=3sqrt(2)/100<0.043`.

Hence every eigenvalue of `Ahat` stays at distance at least

`1.4-3sqrt(2)/100 >1.357`

from zero. In particular the owner hypothesis is satisfied very strongly.

## 7. What this pays and what remains

This theorem pays an exact boundary that was not covered by r32: a square coordinate may share arbitrary couplings with the source bank of a rank-one crossing. The only two structural zeroes are

`A_ij=0`, `A_jj=0`.

The result is dimension-free, uses only original-coordinate product structure, and provides a continuous density.

It does **not** justify treating small nonzero `A_ij` or `A_jj` as perturbations; the live corrections forbid that without additional control, and the false absorption example shows the danger. The next useful implication is therefore

`QFORM-NEAR-ZERODIAG-PAIR-TO-THREEWAY-REARRANGEMENT-v1`:
when the low-tetrad / diagonal-plus-low-rank structural funnel produces a coordinate with small rather than zero self-curvature or a small mutual edge to the square coordinate, retain that coefficient inside a genuine three-variable product rearrangement and prove a bound that limits to (2.1), instead of discarding it as a small random perturbation.

This is a supporting theorem only. The unrestricted QFORM conjecture remains **OPEN**, and full-target continuity remains **OPEN**.
