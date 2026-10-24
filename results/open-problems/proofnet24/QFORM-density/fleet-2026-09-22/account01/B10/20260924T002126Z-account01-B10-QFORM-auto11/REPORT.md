SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-24T00:21:26Z.
attacking: QFORM-SHARED-HUB-ONE-PLUS-TWO-BANK-GLUING-v1 via exact triangular source-bank conditioning and null-hub Gram identities.

# account01/B10 — exact triangular-bank gluing for a null hub, sparse-leakage closure, and the residual triple-volume identity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case  
Status: `NEW_ANALYTIC_BRANCH / NEW_EXACT_STRUCTURAL_IDENTITY / PARTNER_RESULT_APPLIED / PROJECTED-CROSSING-BARRIER-QUANTIFIED / GENERIC_RANK3_OPEN / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and first unpaid implication

Fresh control from `yspennstate/math-research-brain` remained OWNER CONTROL revision `2026-09-22.15`, QFORM-only. The current correction inbox was consumed. Nothing below uses independence after spectral rotation, a law-uniform pointwise quadratic-phase estimate, the false arbitrary-joint coarea estimate, a conditional-density-cap-for-independence substitution, a moment/support/log-concavity hypothesis, or deletion of a small coefficient times an unbounded random variable.

The immediate B10 input is

`yspennstate/math-open-problems@61c5b1fb0c5b97f06722ad26b5185ecb2a6e2ef2`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260923T225225Z-account01-B10-QFORM/REPORT.md`.

It proved the two-bank receiver: if one scalar variable is genuinely source-independent of an arbitrary two-dimensional random vector having a bounded joint density, then the hyperbolic-plus-square form has a continuous bounded density. The unresolved generic near-coloop issue was that the longitudinal leakage and the transverse pair may use the same original coordinates.

This run pays a nontrivial part of that same-source obstruction exactly: same-source longitudinal leakage is harmless whenever, after conditioning an exceptional ORIGINAL-coordinate bank, it is an exact linear combination of the two transverse aggregate coordinates on the surviving bank. No independence is asserted within that surviving two-dimensional projection.

The designated partner actually used is account02/B10:

`yspennstate/math-open-problems@ca0549ef8c582478415aba1a953bdc6115fe84c6`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T214702Z-account02-B10-QFORM-auto11/REPORT.md`.

Its exact target-valid near-coloop family and its arbitrary-fragmentation hub discussion are applied quantitatively in Section 6.

A standard external input used exactly as in the predecessor is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016): every `k`-dimensional orthogonal projection of a product density with one-dimensional caps one has density cap at most `2^(k/2)`. Only `k=2`, hence cap `2`, is used.

## 2. Affine completion of the two-bank receiver

The predecessor stated the receiver without arbitrary affine terms. The following extension is immediate but important under conditioning.

### Lemma 2.1 — `QFORM-TWO-BANK-AFFINE-HYPERBOLIC-SQUARE-v1`

Let `H` be independent of `(Y,Z)`, with

`||p_H||_infinity <= K_H`,
`||p_(Y,Z)||_infinity <= K_2`.

Let `s,d` be nonzero and let `a,b,l,m,r` be arbitrary real numbers. Then

`Q=2sHY+aY^2+2bYZ+dZ^2+lY+mZ+r`

has a continuous density and

`||p_Q||_infinity <= 6 (K_H K_2)^(2/3) (s^2|d|)^(-1/3)`.              (2.1)

The same bound holds if an affine term in `H` is also present.

### Proof

For the displayed form, replace

`Z -> Z+(b/d)Y+m/(2d)`.

This is a determinant-one affine shear of the pair, so its joint density cap remains `K_2`, and it remains independent of `H`. The quadratic becomes

`2sHY+kappa Y^2+ell Y+dZ_1^2+constant`.

The proof of the predecessor receiver depends on the `Y`-part only as a translation of the target value inside the argument of `p_H`; the two competing estimates

`A_y(q)<=K_H m(y)`

and

`A_y(q)<=4 K_2 sqrt(K_H |s|/|d|) sqrt(|y|)`

are unchanged. Splitting at `|y|=R` and optimizing therefore reproduces (2.1). If a term `gamma H` is present, first translate `Y` by `gamma/(2s)`; this leaves the pair cap unchanged and moves only pair-affine terms. The predecessor's near-zero/far-tail approximation also remains unchanged, so continuity survives. QED.

## 3. Exact null-hub normal form

Let

`A=U M U^T`, `U^T U=I_3`,

with symmetric invertible `M` whose three eigenvalues have modulus at least one. Suppose one ORIGINAL physical row is

`u_0=sqrt(h) r`, `h>0`, `||r||=1`,

and is null-Rayleigh:

`r^T M r=0`.                                                         (3.1)

Put

`s=||Mr||`, `v=Mr/s`,

and complete `(r,v)` to an orthonormal spectral basis `(r,v,q)`. Then

`M=[[0,s,0],[s,b,c],[0,c,d]]`,                                       (3.2)

with `s!=0`, `d!=0`, and

`D:=|det M|=s^2|d| >=1`.                                              (3.3)

Write every leaf row as

`u_i=t_i r+y_i v+z_i q`.                                              (3.4)

Parseval gives, over all leaves,

`sum t_i^2=1-h`,
`sum y_i^2=sum z_i^2=1`,
`sum t_i y_i=sum t_i z_i=sum y_i z_i=0`.                              (3.5)

The exact quadratic form is

`Q=2s( sqrt(h)X_0+T )Y+bY^2+2cYZ+dZ^2`,                              (3.6)

where

`T=sum t_i X_i`, `Y=sum y_iX_i`, `Z=sum z_iX_i`.

## 4. Main theorem: exact triangular same-source leakage can be conditioned away

### Theorem 4.1 — `QFORM-NULL-HUB-TRIANGULAR-BANK-RECEIVER-v1`

Partition the leaf ORIGINAL coordinates into disjoint sets `L union R`. Suppose

1. the transverse Gram on `R`,

   `G_R=[[||y_R||^2,<y_R,z_R>],[<y_R,z_R>,||z_R||^2]]`,               (4.1)

   is positive definite;

2. on the same unconditioned source bank `R`, the longitudinal coefficients are exactly triangular over the transverse coefficients:

   `t_R=alpha y_R+beta z_R`                                           (4.2)

   for some real `alpha,beta`.

Then `Q` has a continuous density and

`boxed: ||p_Q||_infinity
 <= 6*2^(2/3) h^(-1/3) D^(-1/3) (det G_R)^(-1/3).`                    (4.3)

This theorem allows arbitrary dependence between the two transverse projected coordinates and arbitrary cap-one laws, supports and fragmentation on every original coordinate.

### Proof

Condition on the ORIGINAL variables `(X_i)_{i in L}`. Their aggregates `T_L,Y_L,Z_L` are now fixed. Put

`Ybar=Y_L+Y_R`, `Zbar=Z_L+Z_R`,
`gamma_L=T_L-alpha Y_L-beta Z_L`.

By (4.2), exactly

`T_L+T_R=alpha Ybar+beta Zbar+gamma_L`.                               (4.4)

Substitute (4.4) into (3.6):

`Q=2s sqrt(h)X_0 Ybar
 +(b+2s alpha)Ybar^2
 +2(c+s beta)Ybar Zbar
 +d Zbar^2
 +2s gamma_L Ybar`.                                                    (4.5)

Thus the same-source leakage has become only transverse quadratic/affine curvature. No probabilistic independence was manufactured.

After conditioning `L`, the hub variable `sqrt(h)X_0` is genuinely independent of the entire vector `(Ybar,Zbar)`, because the latter uses only the disjoint ORIGINAL-coordinate bank `R` plus deterministic translations. Its density cap is

`K_H<=h^(-1/2)`.                                                       (4.6)

Normalize the `R`-pair. The coefficient matrix `P_R=[y_R,z_R]` has Gram `G_R`. Hence

`V=G_R^(-1/2) P_R^T X_R`

is an orthogonal two-dimensional projection of the product law on `R`. The sharp product-marginal theorem gives `||p_V||_infinity<=2`; undoing the linear map yields

`||p_(Ybar,Zbar)||_infinity
 =||p_(Y_R,Z_R)||_infinity
 <=2/(sqrt(det G_R))`.                                                 (4.7)

Apply Lemma 2.1 to (4.5), use (3.3), and obtain the conditional bound (4.3), independent of the conditioned values. Averaging the conditional laws gives the same essential bound unconditionally.

For continuity, choose the continuous conditional density furnished by Lemma 2.1. The proof there gives a jointly measurable integral formula in the conditioning parameters and target value. For every fixed conditioning value it is continuous in the target and is uniformly bounded by the right side of (4.3). Dominated convergence over the probability law of `X_L` therefore shows that their mixture is continuous. QED.

### Interpretation

The key point is that (4.2) is **not** an independence condition. The leakage `T_R` may use exactly the same original variables as both transverse projections. It is harmless because it is algebraically measurable through those two aggregate coordinates and therefore changes only the coefficients of the already-present two-dimensional quadratic polynomial.

This is a strict enlargement of the predecessor's source-disjoint two-bank branch.

## 5. Exact residual identity: the unpaid quantity is hub-free triple volume

For any `R` with `G_R>0`, define the least-square nontriangular residual

`delta_R^2 := dist(t_R,span{y_R,z_R})^2`.                              (5.1)

Let `H_R` be the `3x3` Gram matrix of the three coefficient columns `(t_R,y_R,z_R)`. Schur's determinant formula gives

`det H_R=(det G_R) delta_R^2`.                                        (5.2)

But the rows of the corresponding `|R| x3` coefficient matrix are precisely the spectral coordinates of the physical rows `u_i`. Cauchy--Binet therefore gives

`det H_R
 =sum_{i<j<k; i,j,k in R} det(u_i,u_j,u_k)^2`.                    (5.3)

Combining,

`boxed:
 delta_R^2 det G_R
 =sum_{i<j<k in R} det(u_i,u_j,u_k)^2.`                               (5.4)

Consequences:

- The exact triangular criterion (4.2) is equivalent to **all hub-free three-row minors inside `R` vanishing**.
- Over the entire leaf set, (3.5) gives `G=I_2` and `t perpendicular span{y,z}`, so

  `sum_{i<j<k leaves} det(u_i,u_j,u_k)^2=1-h`.                         (5.5)

Thus the near-coloop obstruction is exactly a small but nonzero hub-free triple-volume. Smallness alone cannot be treated as a small random perturbation under arbitrary unbounded source laws.

Equivalently, Theorem 4.1 pays every configuration admitting a deletion/conditioning set `L` that hits all nonzero hub-free three-minors while retaining a quantitatively nondegenerate transverse Gram on the surviving original-coordinate bank.

## 6. Quantitative corollary: sparse or low-transverse-energy leakage is uniformly paid

A useful concrete branch follows without solving any combinatorial selection problem.

Assume `t_i=0` outside a set `L`, and let

`E_L=sum_{i in L} p_i p_i^T`, `p_i=(y_i,z_i)`.                         (6.1)

Then on `R=L^c`, `t_R=0`, so Theorem 4.1 applies with `alpha=beta=0`. Since the full transverse Gram is `I_2`,

`G_R=I_2-E_L`.                                                        (6.2)

If `||E_L||_op<=eta<1`, then

`det G_R >=(1-eta)^2`,                                                 (6.3)

and therefore

`boxed: ||p_Q||_infinity
 <=6*2^(2/3) h^(-1/3)D^(-1/3)(1-eta)^(-2/3),`                         (6.4)

with a continuous density.

In particular, in the previously isolated diffuse collar where every leaf transverse leverage satisfies

`tau_i=||p_i||^2<1/4`,                                                 (6.5)

if the longitudinal leakage is supported on at most three leaves, then

`||E_L||_op<=tr E_L<3/4`,

so `det G_R>1/16` and

`boxed: ||p_Q||_infinity <24 h^(-1/3)D^(-1/3).`                       (6.6)

In the current ultra-coloop numerical chamber from the predecessor, `h>4095/4096` and `D>=1`, so this is

`boxed: ||p_Q||_infinity <24(4096/4095)^(1/3)<24.002.`                (6.7)

This is a new paid portion of the same-source leakage state: the leakage-support originals may themselves have arbitrary transverse components and arbitrary cap-one laws.

## 7. Designated account02/B10 result applied to actual inequalities

The completed partner report at commit

`ca0549ef8c582478415aba1a953bdc6115fe84c6`

constructs, for `0<=rho<1/64` and `c_0=1-rho`, the exact target-valid Parseval frame

`u_0=sqrt(c_0)e_1`,
`u_1=sqrt(rho)e_1`,
`u_2,...,u_65=e_2/8`,
`u_66,...,u_129=e_3/8`,                                                (7.1)

with spectral matrix

`M=[[0,1,0],[1,0,0],[0,0,1]]`,                                       (7.2)

so the nonzero spectrum is exactly `{-1,1,1}` and `D=1`.

Take `L={1}` and let `R` be all transverse leaves. Then `t_R=0` and `G_R=I_2`. Theorem 4.1 therefore applies to **arbitrary cap-one laws on every original coordinate** and gives the actual partner-family inequality

`boxed: ||p_(Q_rho)||_infinity
 <=6*2^(2/3)c_0^(-1/3)
 <6*2^(2/3)(64/63)^(1/3)
 <9.575,`                                                            (7.3)

with a continuous density. This recovers the predecessor's best two-bank payment through the new conditioning theorem rather than by first aggregating the pure longitudinal variable with the hub.

There is also a genuinely contaminated variant. Orthogonally rotate the two physical rows `u_1=sqrt(rho)e_1` and `u_2=e_2/8` through any angle `theta`, leaving every other row unchanged:

`u_1'=cos(theta)sqrt(rho)e_1+sin(theta)e_2/8`,
`u_2'=-sin(theta)sqrt(rho)e_1+cos(theta)e_2/8`.                         (7.4)

This row rotation preserves `U^T U=I_3` and therefore preserves the exact nonzero spectrum `{-1,1,1}`. For nontrivial `theta`, both rotated ORIGINAL rows simultaneously carry longitudinal and transverse coefficients, so the simple three-independent-bank factorization is gone.

Condition those two mixed originals: `L={1',2'}`. The remaining bank has `t_R=0` and

`G_R=diag(63/64,1)`, `det G_R=63/64`.                                 (7.5)

Theorem 4.1 yields, uniformly in `theta` and in all cap-one source laws,

`boxed: ||p_Q||_infinity
 <6*2^(2/3)(64/63)^(2/3)
 <9.625,`                                                            (7.6)

again with a continuous density. This is a strict same-source-contamination extension of the partner construction, not merely a reproof of its pure-longitudinal factorization.

## 8. Exact factorization of the one-hub projected-crossing certificate

The fresh grouped projected-crossing theorem from the interactive source is powerful when its volume certificate is nondegenerate, but it explicitly warned that `Q_epsilon` loses the small leakage scale. In the null-hub coordinates above, that loss can be identified exactly.

Split leaves into `I union J`. The hub-to-`J` cross row is

`w_J=sqrt(h)s y_J`,                                                    (8.1)

so

`S^2:=||w_J||^2=h s^2||y_J||^2`.                                     (8.2)

Let `P_J` denote orthogonal projection in the `J` coordinate space onto `y_J^perp`. The projected light crossing appearing in the grouped theorem is

`C=A_{I,J}P_J
 =[y_I,z_I] [[s,c],[0,d]] [P_J t_J,P_J z_J]^T`.                    (8.3)

Therefore, by Cauchy--Binet for this rank-at-most-two factorization,

`Z_2(C)
 =(sd)^2 det G_I * det Gram(P_J t_J,P_J z_J)`.                        (8.4)

Multiplying by (8.2) and using `D=s^2|d|` gives the exact identity

`boxed:
 S^2 Z_2(C)
 = hD^2 ||y_J||^2 det G_I
   det Gram(P_J t_J,P_J z_J).`                                       (8.5)

Since `||y_J||^2<=1`, `G_I<=I_2`, and

`det Gram(P_J t_J,P_J z_J)
 <=||t_J||^2||z_J||^2
 <=1-h`,                                                             (8.6)

we obtain for **every** such partition

`boxed: S^2 Z_2(C) <= hD^2(1-h).`                                    (8.7)

Thus a one-hub `k=1, ell=2` projected-crossing proof necessarily loses the near-coloop scale on this exact normal form. In the already isolated ultra-collar `D^2(1-h)<2^(-12)`, every such certificate is `<2^(-12)`. This is a barrier for that proof architecture, not for QFORM itself.

The contrast with Theorem 4.1 is precise: when the residual in (5.4) vanishes after conditioning a transverse-cheap exceptional bank, the leakage is absorbed algebraically and no factor `(1-h)^(-1/6)` is paid at all. The genuinely remaining state is where the hub-free triple volume is nonzero on every transverse-rich surviving bank.

## 9. Remaining implication

The unrestricted exact-rank-three theorem is **not** proved. The new result covers the exact null-Rayleigh hub branch whenever there is a quantitatively transverse-rich surviving bank on which the longitudinal coefficient vector is exactly in the transverse coefficient span. In particular it uniformly closes diffuse null-hub leakage supported on at most three original coordinates and a broader low-transverse-energy exceptional-set class.

What remains in this mechanism is

`QFORM-NULL-HUB-NONTRIANGULAR-PRODUCT-TRACE-v1`:

> In the null-hub near-coloop state, control the case where every surviving bank with order-one transverse Gram has a genuinely nonzero residual `delta_R`, equivalently nonzero hub-free triple volume (5.4), without paying a negative power of the total `1-h` scale and without replacing the product-origin law by arbitrary conditional density caps.

For the full rank-three assignment there is also the punctured near-null issue `r^TMr !=0` with very small physical pivot. The existing orientation-free half-Riesz scalar-Schur theorem pays every fixed nonzero pivot but deteriorates as that pivot tends to zero; the present theorem is an endpoint/null-hub result and does not silently fill that punctured gap.

Therefore:

- `QFORM-NULL-HUB-TRIANGULAR-BANK-RECEIVER-v1`: **PROVED SUPPORTING THEOREM**.
- sparse-leakage diffuse null-hub branch (<=3 leakage-source leaves): **PROVED**, continuous density `<24.002` in the current ultra-collar.
- partner pure-longitudinal family: **PROVED** here with continuous density `<9.575`.
- row-mixed contaminated partner family: **PROVED** here with continuous density `<9.625`.
- generic nontriangular null-hub state: **OPEN**.
- punctured near-null rank-three state: **OPEN**.
- arbitrary exact rank three: **OPEN**.
- full owner QFORM target: **OPEN / NOT PROVED / NOT DISPROVED**.

No numerical histogram or extremality claim is used. The algebraic identities are exact, and all probabilistic independence used above is between disjoint ORIGINAL-coordinate banks only.
