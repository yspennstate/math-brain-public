SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T22:31:35Z.
attacking: partner account03/B06 r45's all-diagonals-small off-diagonal anchored-curvature survivor; aggregate its aligned rank-one K currency through a source-preserving diagonal-twist half-Riesz receiver before any individual-minor inversion.

# account02/B06 — aligned anchored-K diagonal-twist receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `b06-20260923T223135Z-0620e71a33be`  
Role: Curved fiber integration  
Status: **NEW SUPPORTING THEOREM + PARTNER r45 BRANCH ADVANCED + TARGET-LEVEL COMPILER COUNTEREXAMPLE + PINNED RESULTS APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. Nothing below assumes moments, compact support, log-concavity, iid laws, independence after spectral rotation, or a diagonal spectral-coordinate product law. Every conditioning/grouping step is performed on literal original independent coordinate banks. Continuity is not claimed by the new theorem.

The first unpaid implication on entry was the exact/near alignment collar left after the preceding B06 wedge compiler:

`QFORM-R45-ALIGNED-HOLLOW-K-DIAGONAL-TWIST-v1`.

Partner account03/B06 r45 already pays a fixed diagonal anchored curvature `(K_H)_{kk}` through its physical-triple determinant theorem. The preceding account02/B06 run pays off-diagonal **misalignment** by an aggregate wedge/E2 receiver. What remained was the genuinely aligned case, where all off-diagonal wedges vanish and the first physical Schur remainder becomes `diagonal + rank one` in exactly the same original-product innovation direction. The point of this run is that the diagonal twist can be retained at full strength without reintroducing a curved-fiber supremum.

## 1. Sources actually used


The newest completed designated partner at invocation was account03/B06 r45, source-pinned as

`yspennstate/math-open-problems@b5d4a62bb80a7ad84db292cb8d886282a95e851b`.

It proves, for every literal environment coordinate `k`,

`|(K_H)_{kk}|>=eta  =>  ||p_Q||_infinity <=102 eta^(-1/3)`,      (1.1)

where

`K_H=det(H) C-E^T adj(H)E`                                      (1.2)

is the complete bank of physical `3 x 3` minors anchored at the two hubs.

The immediately preceding account02/B06 report established, after one physical completion, the exact identity

`K_H=a(delta R-gamma gamma^T)`,                                  (1.3)

with notation recalled in Section 3, and proved an aggregate wedge compiler paying every sufficiently non-aligned off-diagonal K packet.

The owner-required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.

Two completed pieces are applied below at equation level:

1. `FOURIER_ROUTE_REPORT.md`, Theorem F at rank one: for a literal product bank, a diffuse unit vector `u` with `max u_i^2<=1/2`, arbitrary physical diagonal quadratic twists and arbitrary linear terms,

`|phi(t)| <= min(1, 2 sqrt(pi) |lambda t|^(-1/2))`.              (1.4)

2. `FOURIER_ROUTE_REPORT.md`, Lemma 4.2 (physical square peel): for a literal scalar pivot `a!=0`,

`D(Q)<=|a|^(-1/2) H_(1/2)(Schur_a Q)`.                           (1.5)

The pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A is applied in Section 6 to a genuine three-large-eigenvalue family that defeats the tempting stronger K-currency structural claim.

The translated quadratic kernel and its averaging lemma used in Section 2 are the completed programme lemmas in `interactive/20260922T161801Z-rank-two-fusion/REPORT.md`: for

`Psi(x)=1+log(1/|x|)` on `0<|x|<=1`, `Psi(x)=|x|^(-1/4)` on `|x|>=1`,

one has

`sup_(f<=1, int f=1) int f(y)|x-y^2|^(-1/2)dy <=8 Psi(x)`,       (1.6)

and if `P(|W|<rho)<=L sqrt(rho)` for every rho, then

`E Psi(W)<=4 sqrt(L)`.                                           (1.7)

## 2. New pinned-Fourier consequence: rank-one curvature survives arbitrary diagonal twists

### Lemma 2.1 — `QFORM-RANK1-DIAGONAL-TWIST-SMALLBALL-v1`

Let `Z=(Z_i)` have independent density caps one. Let `u` be a unit vector with

`max_i u_i^2<=1/2`,                                               (2.1)

and let `lambda!=0`. For arbitrary real diagonal coefficients `d_i`, arbitrary affine vector `b`, and arbitrary constant `c`, put

`T=sum_i d_i Z_i^2 + lambda (u dot Z)^2 + b dot Z+c`.             (2.2)

Then, uniformly in the centre `s` and `rho>0`,

`boxed:
 P(|T-s|<rho) <= min(1,12 sqrt(rho/|lambda|)).`                  (2.3)

#### Proof

Apply the pinned Theorem F, rank `r=1`, **with all diagonal and affine terms retained as twists**. It gives exactly

`|phi_T(t)|<=min(1,2sqrt(pi)|lambda t|^(-1/2)).`                 (2.4)

For any `v>0`,

`1_(|x|<rho)<=exp(v) exp(-v x^2/rho^2)`.                         (2.5)

Gaussian Fourier inversion therefore yields

`P(|T-s|<rho)
 <= exp(v) rho/(2sqrt(pi v))
    int_R exp(-rho^2 t^2/(4v)) |phi_T(t)|dt`.                    (2.6)

Use the second factor of (2.4) everywhere. Since

`int_R exp(-A t^2)|t|^(-1/2)dt=A^(-1/4) Gamma(1/4)`,             (2.7)

setting `v=1/4` gives

`P(|T-s|<rho)
 <=2 exp(1/4) Gamma(1/4) sqrt(rho/|lambda|)
 <12 sqrt(rho/|lambda|).`                                       (2.8)

For the last safe numerical inequality one may use the elementary bound `Gamma(1/4)<=4+e^(-1)` and `e^(1/4)<1.285`. Probability normalization supplies the minimum with one. QED.

This is the first crucial point: an arbitrarily large, arbitrarily signed original-coordinate diagonal quadratic twist does not damage the rank-one `sqrt(rho)` credit. It is kept inside the product Fourier factors, rather than frozen and maximized over.

## 3. A two-direction half-Riesz theorem with an arbitrary diagonal product twist

Let `Y` be another cap-one variable independent of the product bank `Z`, and let `u` satisfy (2.1). Consider

`T
 = beta Y^2+2 gamma_0 Y(u dot Z)+eta (u dot Z)^2
   +sum_i d_i Z_i^2 + ell Y+b dot Z+c`,                           (3.1)

and put

`Lambda=[[beta,gamma_0],[gamma_0,eta]]`,
`D_Lambda=|det Lambda|>0`.                                       (3.2)

### Theorem 3.1 — `QFORM-HEAVY-LIGHT-DIAGONAL-TWIST-HALFRIESZ-v1`

For every choice of the diagonal twist and affine terms,

`boxed:
 H_(1/2)(T):=sup_s E|T-s|^(-1/2)
 <=64 sqrt(3) D_Lambda^(-1/4).`                                  (3.3)

The constant `64sqrt(3)=110.8512516844...` is deliberately source-safe; no optimization is intended.

#### Proof when `beta!=0`

Complete the literal original coordinate `Y`:

`T=beta(Y+gamma_0(u dot Z)/beta+ell/(2beta))^2+R_0(Z)`,           (3.4)

where

`R_0
 =(det Lambda/beta)(u dot Z)^2
  +sum_i d_i Z_i^2
  +[b-(ell gamma_0/beta)u] dot Z
  +c-ell^2/(4beta).`                                             (3.5)

For fixed `Z`, translation preserves the cap of `Y`, so the kernel (1.6) gives

`E_Y |T-s|^(-1/2)
 <=8 |beta|^(-1/2) Psi(W)`,                                     (3.6)

where

`W=(s-R_0)/beta`.                                                (3.7)

The rank-one coefficient of `W`, in the normalized original-product direction `u`, has magnitude

`lambda_0=D_Lambda/beta^2`.                                      (3.8)

All remaining quadratic terms of `W` are diagonal. Lemma 2.1 therefore gives

`P(|W|<rho)<=12 lambda_0^(-1/2) sqrt(rho)`.                      (3.9)

Apply (1.7):

`E Psi(W)<=4 sqrt(12) lambda_0^(-1/4)`.                          (3.10)

Combining (3.6), (3.8), and (3.10), the apparently dangerous `beta` cancels exactly:

`H_(1/2)(T)
 <=32 sqrt(12)|beta|^(-1/2)lambda_0^(-1/4)
 =64 sqrt(3) D_Lambda^(-1/4).`                                  (3.11)

No diagonal twist coefficient occurs in the final bound.

#### Proof when `beta=0`

Then `D_Lambda=gamma_0^2`. Conditional on `Z`, (3.1) is affine in the literal original variable `Y`, with slope `2gamma_0(u dot Z)+ell`. The cap-one negative-half-moment bathtub estimate gives

`E_Y |T-s|^(-1/2)
 <=2sqrt(2)|2gamma_0(u dot Z)+ell|^(-1/2).`                      (3.12)

The scalar original-product projection `u dot Z` has density at most `sqrt(2)`. Rescaling the same bathtub estimate and averaging (3.12) gives in fact

`H_(1/2)(T)<=2^(11/4)|gamma_0|^(-1/2)
 <8D_Lambda^(-1/4)`,                                             (3.13)

which is stronger than (3.3). QED.

This theorem is exactly the weighted replacement needed by the aligned collar: the heavy physical variable is integrated first, but the resulting singular kernel is averaged against the complete product-derived rank-one law while every same-bank diagonal curvature remains in the small-ball estimate.

## 4. Main anchored-K theorem: exact off-diagonal alignment is paid uniformly through the null determinant limit

Return to the literal two-hub/environment block

`A=[[H,E],[E^T,C]]`,
`H=[[a,b],[b,d]]`,
`E=[alpha^T;beta^T]`,                                            (4.1)

with `a!=0`. Put

`delta=d-b^2/a=det(H)/a`,
`Gamma=a beta-b alpha`,
`gamma=Gamma/a`,
`R=C-alpha alpha^T/a`.                                           (4.2)

After completing only the original coordinate corresponding to `a`, the untouched quadratic matrix on `(Y,Z)` is

`S_1=[[delta,gamma^T],[gamma,R]]`,                               (4.3)

and the exact identity from the preceding B06 run is

`K_H=a(delta R-gamma gamma^T)`.                                  (4.4)

Assume `delta!=0`, `Gamma!=0`, and the off-diagonal K packet is **exactly aligned** with the innovation:

`K_H=D_K+tau Gamma Gamma^T`,                                     (4.5)

for some diagonal matrix `D_K` and scalar `tau!=0`. Let

`G=||Gamma||_2^2`, `u=Gamma/sqrt(G)`,                            (4.6)

and assume the diffuse innovation condition

`max_i Gamma_i^2<=G/2`.                                         (4.7)

Solving (4.4) for `R` gives the exact, source-preserving decomposition

`R
 =D_K/(a delta)
  +(1+a tau) Gamma Gamma^T/(a^2 delta).`                         (4.8)

Thus (4.3) is an arbitrary diagonal twist on the original `Z_i`, plus a two-direction form on the literal variable `Y` and the single product projection `u dot Z`. Its `2 x 2` middle matrix is

`Lambda_*
 =[[delta, sqrt(G)/a],
   [sqrt(G)/a,(1+a tau)G/(a^2 delta)]].`                         (4.9)

The key determinant identity is

`boxed: det Lambda_* = tau G/a.`                                (4.10)

The small physical determinant `delta` cancels completely.

### Theorem 4.1 — `QFORM-ALIGNED-K-DIAGONAL-TWIST-RECEIVER-v1`

Under (4.1)--(4.7), with **all ambient outside couplings and affine terms arbitrary**, the full quadratic form satisfies

`boxed:
 ||p_Q||_infinity
 <=64 sqrt(3) (|a tau| G)^(-1/4).`                               (4.11)

In particular, the bound is uniform as the indefinite hub determinant tends to zero. It retains every diagonal entry of `D_K` at its exact (possibly divergent Schur-scaled) strength.

#### Proof

The pinned physical square peel (1.5) gives

`D(Q)<=|a|^(-1/2) H_(1/2)(S_1)`.                                (4.12)

Apply Theorem 3.1 to (4.8)--(4.9), including all induced affine terms. Using (4.10),

`H_(1/2)(S_1)
 <=64sqrt(3)|tau G/a|^(-1/4).`                                  (4.13)

Substitution into (4.12) gives exactly (4.11). Conditioning first on every ambient coordinate outside the displayed physical block changes only affine terms, already allowed in Theorem 3.1; averaging therefore gives the full-ambient statement. QED.

The theorem is determinant-stable for the intended reason: the same near-null scaling that makes the diagonal Schur twist huge also makes the moving rank-one centre huge, and the product-weighted small-ball calculation keeps both instead of taking a fiber supremum.

### Off-diagonal Frobenius formulation

Define the aggregate off-diagonal anchored curvature

`F_off^2=sum_(j!=k)(K_H)_(jk)^2`.                                (4.14)

Under exact alignment (4.5),

`F_off
 =|tau| sqrt(G^2-sum_j Gamma_j^4).`                              (4.15)

The diffuse condition (4.7) implies

`G/sqrt(2)<=sqrt(G^2-sum Gamma_j^4)<=G`.                         (4.16)

Hence `|tau|G>=F_off`, and (4.11) gives the useful partner-facing form

`boxed:
 ||p_Q||_infinity
 <=64sqrt(3)(|a|F_off)^(-1/4).`                                  (4.17)

No individual off-diagonal K entry is extracted or inverted.

At the exact rank-one hub endpoint one has `K_H=-(1/a)Gamma Gamma^T`, so `tau=-1/a`; (4.11) tends to the finite estimate

`||p_Q||_infinity<=64sqrt(3)||Gamma||^(-1/2)`.                   (4.18)

The already-completed r43 exact-rank-one theorem has a much better numerical constant, but (4.18) confirms that the present mechanism is algebraically continuous at the endpoint.

## 5. Apply the newest designated partner r45 to a real inequality

Partner r45's live survivor is exactly the branch where every diagonal anchored curvature is below its triple-determinant extraction scale and substantial K currency may remain off diagonal. The preceding B06 wedge compiler pays the quantitatively **misaligned** portion of that packet. Theorem 4.1 now pays its exact aligned diffuse portion.

Concretely, on any r45 state for which

`(K_H)_(jk)=tau Gamma_j Gamma_k` for every `j!=k`,                 (5.1)

with `Gamma` diffuse and `tau!=0`, the full ambient target form obeys the actual aggregate inequality

`boxed:
 ||p_Q||_infinity
 <=64sqrt(3)(|a|F_off)^(-1/4).`                                  (5.2)

This consumes the whole off-diagonal Frobenius packet before any local minor is selected. The diagonal K entries remain arbitrary and are retained as the physical diagonal twist in (4.8).

On the inherited r43--r45 innovation branch `||Gamma||>=2^(-12)`, a more explicit parameterized consequence is

`|a tau|>=theta>0
 =>
 ||p_Q||_infinity
 <=4096sqrt(3) theta^(-1/4)
 =7094.480108... theta^(-1/4).`                                  (5.3)

No claim is made that r45 supplies a universal lower bound on `theta`; (5.2), rather than an invented numeric floor, is the source-valid advance.

Together with r45's diagonal theorem (1.1) and the preceding wedge-misalignment compiler, the only genuinely aligned collar not paid by the present mechanism is where the aligned coefficient itself collapses (`tau` tends to zero) or where exact alignment is replaced by a defect too small to spend directly but too large to discard.

## 6. A target-level compiler counterexample: neither aligned tau nor anchored K entries need stay large

A stronger structural hope would be that the three-large-eigenvalue condition forces, in the diffuse exact-alignment collar, either `|a tau|G` or one physical anchored curvature `|(K_H)_{kk}|` to stay uniformly positive. That is false.

For `N>=2` let `X,Y,Z,U_1,...,U_N` be independent cap-one variables, set

`gamma=(sqrt(2/N),...,sqrt(2/N))`, `||gamma||=sqrt(2)`,
`L=gamma dot U`,                                                  (6.1)

and for `0<epsilon<=1` define

`Q_(N,epsilon)
 =X^2-epsilon Y^2+2YL-epsilon^(-1)L^2+Z^2`.                      (6.2)

The `(Y,U)` block is exactly

`-epsilon^(-1)(epsilon e_Y-gamma)(epsilon e_Y-gamma)^T`,         (6.3)

so the complete original matrix has precisely three nonzero eigenvalues

`boxed: {1,1,-(epsilon+2/epsilon)}.`                             (6.4)

Thus (6.2) is a genuine owner-target family for every `N>=2` and `0<epsilon<=1`, while every individual `Y-U_j` edge tends to zero as `N` grows.

Take the physical hubs `(X,Y)`. Then `a=1`, `Gamma=gamma`, the innovation is diffuse, and a direct calculation from (1.2) gives

`boxed: K_H=-epsilon e_Z e_Z^T.`                                (6.5)

Therefore

`tau=0`, `F_off=0`, and `max_k |(K_H)_(kk)|=epsilon ->0`.         (6.6)

So target spectrum alone does **not** force either the new aligned off-diagonal currency or r45's one-coordinate diagonal currency to remain quantitatively visible.

This is not a QFORM counterexample. Put

`W=epsilon Y-L`.                                                 (6.7)

The original-product one-dimensional projection bound gives `||p_L||_infinity<=1`. Since `epsilon Y` is independent of `L`, convolution gives

`||p_W||_infinity<=1`.                                           (6.8)

Moreover `W` is independent of the disjoint original variables `X,Z`, and

`Q_(N,epsilon)=X^2-epsilon^(-1)W^2+Z^2`.                         (6.9)

Now apply the owner-required pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A to the **actual three independent cap-one variables** `(X,W,Z)`. The matrix is `diag(1,-epsilon^(-1),1)`, whose least eigenvalue magnitude is one, hence

`boxed:
 ||p_(Q_(N,epsilon))||_infinity
 <=6sqrt(pi)
 =10.6347231054... .`                                            (6.10)

This grouping is source-valid: `W` is formed from a coordinate bank disjoint from `X,Z`; no post-rotation independence is asserted.

The example exposes the next real mechanism. When `tau=0`, the aligned two-direction determinant (4.10) collapses, but the target's third direction may survive as a physical diagonal twist whose **Schur-scaled coefficient is order one even though the anchored K entry is only order epsilon**. An argument based solely on the size of K_H therefore loses the null-limit scale.

## 7. First unpaid implication after this run

The new first debt is

`QFORM-R45-ALIGNED-TAUZERO-DIAGONAL-RESCUE-v1`.

In the r45 diffuse alignment collar, retain the full cross tail and arbitrary same-bank curvature and handle the regime in which

* the wedge/misalignment defect is below the determinant-favorable receiver's useful scale;
* the aligned coefficient `|a tau|G` is too small for Theorem 4.1;
* every individual `(K_H)_(kk)` is below r45's physical-triple extraction scale.

The family (6.2) shows why the missing quantity cannot be `||K_H||` alone: a genuine target may have `K_H ->0` while a source-preserving diagonal third square remains order one after division by the near-null determinant. The next receiver should therefore aggregate the **pre-Schur diagonal twist scale** `D_K/(a delta)` jointly with the rank-one moving square, using original-coordinate grouping/two-square peeling before any individual reciprocal K entry is paid. A small nonzero alignment defect cannot simply be discarded as a perturbation; it must continue to be spent by the preceding wedge receiver.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains OPEN.

## 8. Checks

The identities are algebraic. In particular, substitution of (4.8) into (4.4) gives (4.5) exactly, and direct determinant expansion of (4.9) gives `det Lambda_*=tau G/a`.

For the target family (6.2), numerical checks at `N=10` give the nonzero spectra

* `epsilon=1`: `{-3,1,1}`;
* `epsilon=0.3`: `{-6.9666666667,1,1}`;
* `epsilon=0.05`: `{-40.05,1,1}`,

matching (6.4). The source-safe theorem constant is

`64sqrt(3)=110.8512516844...`,

and the pinned target-family bound is

`6sqrt(pi)=10.6347231054...`.

Finite computation is only a sanity check; Sections 2--7 are the mathematical argument.
