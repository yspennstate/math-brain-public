# account03/B19 — Hölder Schur splice and closure of the `s2(A-diag A)<=3/20` branch

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`.
Run: `20260922T160316Z-account03-B19-QFORM-r14`.
Assignment: Universal proof assembly.
Status: `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_BRANCH_PROVED / FULL_CONJECTURE_OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Target, corrections, and source dependencies

The target is the full unrestricted statement: for every dimension, every independent real coordinates with densities bounded by one, and every real symmetric matrix A with at least three eigenvalues of modulus at least one, prove a universal finite essential-density bound for Q=X^T A X, or give a target-valid counterexample. Continuity is a separate desired conclusion and is not proved in the new branch below.

No uniform pointwise quadratic-phase decay, post-rotation independence, conditional density cap after aggregate rotation, fiber-supremum closure, fixed local-minor extraction, compact support, moments, or log-concavity is used.

This run uses two existing compatible inputs at their stated scopes.

1. `QFORM-FINITE-UNION-CORE-v1`, designated partner account04/B19, canonical source `yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`. It transfers interval-concentration inequalities proved on bounded finite-union product indicators of measure one to all admissible independent cap-one densities with no constant loss.
2. The characteristic-envelope part of `QFORM-RIDGE-DENSITY-v1`, canonical source `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`. Its source report supplies a complete analytic proof, while independent review of that extension is still pending. For an original-coordinate cross block C, gamma>0, q in [1,2], K=C C^T(gamma^2 I+C C^T)^(-1), theta=tr K, D=det(I+C C^T/gamma^2), and max diag K<=q/2, it gives before any time-integrability assumption

`|phi(t)| <= D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q))`,

where `L_q=pi e sqrt(2/q)`.

The preceding B19 run `0e6d1715955458010d43193cab3dafc293c0e28c` proved the physical-pivot quarter kernel and exact Schur reduction. I reproduce the needed interface so the new argument is checkable.

## 2. Hölder version of the Schur critical-value splice

Let the two original pivot coordinates have principal block

`B=[[a,c],[c,-b]]`,  a,b>=m>0,  Delta=ab+c^2.

Condition on all other original coordinates Z and complete the square only in these two physical coordinates. With the exact Schur complement

`S=C0-K^T B^(-1)K`,  `kappa(Z)=Z^T S Z`,

the previous binary estimate gives a conditional density kernel

`h_z(t) <= K0 |t-kappa(z)|^(-1/4)`,

with

`K0=2 Delta^(-1/4)m^(-1/4) <= 2 m^(-3/4)`.

### Lemma 2.1 — Hölder splice

If for some alpha>1/4 and L<infinity,

`P(|kappa-t|<=r) <= L r^alpha` for every t and 0<r<=1,

then Q has an essentially bounded density and

`||p_Q||_infinity <= K0 [1 + L/(4 alpha-1)]`.                 (2.1)

Proof. Put D_t=|t-kappa|. Layer cake gives

`E D_t^(-1/4)= integral_0^infinity P(D_t<u^(-4)) du`
`<=1 + L integral_1^infinity u^(-4 alpha)du`
`=1+L/(4alpha-1)`.

Average the conditional quarter-kernel. No rotated conditional law appears. QED.

This strictly lowers the outside obligation from square-root concentration to any Hölder exponent greater than 1/4.

## 3. A two-physical-coordinate `3/8` small-ball lemma

### Lemma 3.1 — mixed-coordinate quadratic sublevel estimate

Let X,Y be independent real variables with densities bounded by one. For

`q(x,y)=a x^2+2cxy+b y^2+u x+v y+w`,  c!=0,

for every t and r>0,

`P(|q(X,Y)-t|<=r) <= 2 (2r/|c|)^(3/8)`.                       (3.1)

Proof. Let E be the sublevel event and, for fixed x, E_x its y-section. Define g(y)=P_X((X,y) in E). Since the law of Y is a probability measure nu,

`P(E)^2 <= integral g(y)^2 dnu(y)`
`=E_{X1,X2} nu(E_X1 intersect E_X2)`.

If x1!=x2 and y belongs to both sections, subtracting the two quadratic inequalities yields

`|(x1-x2)[a(x1+x2)+2cy+u]|<=2r`.

Hence the intersection lies in a y-interval of length at most

`epsilon/|X1-X2|`,  `epsilon=2r/|c|`.

Because the Y density is at most one,

`nu(E_X1 intersect E_X2)<=min(1,epsilon/|D|)`, D=X1-X2.

The density of D is `f_X * tilde(f_X)` and has L-infinity norm at most one. For epsilon<=1/2, layer cake gives

`E min(1,epsilon/|D|)`
`= integral_0^1 P(|D|<epsilon/s) ds`
`<= integral_0^1 min(1,2epsilon/s) ds`
`=2epsilon[1+log(1/(2epsilon))]`
`<=4 epsilon^(3/4)`.

For the last inequality, with z=2epsilon in (0,1], the maximum of `z^(1/4)(1+log(1/z))` is `4e^(-3/4)<2^(5/4)`. Taking square roots proves (3.1). If epsilon>=1/2, the right side of (3.1) exceeds one, so the claim is trivial. QED.

The key point is that arbitrary self-quadratics and arbitrary affine terms are allowed. Thus after conditioning every other original coordinate, any one physical cross coefficient gives a `3/8` small-ball exponent, which is already above the quarter-kernel threshold.

## 4. Ridge envelopes also yield Hölder concentration below the density threshold

Suppose a real random variable Y has characteristic envelope

`|phi_Y(t)| <= min(1,(t0/|t|)^beta)`.

For any `0<alpha<=beta` with `alpha<1`, Gaussian smoothing gives

`P(|Y-y|<=r) <= C_alpha (t0 r)^alpha` when t0 r<=1,              (4.1)

and the trivial probability bound handles t0 r>=1, where

`C_alpha=e^(1/2) sqrt(2/pi) [1+I_alpha]`,
`I_alpha=2^(-(alpha+1)/2) Gamma((1-alpha)/2)`.

Indeed `1_{|x|<=r}<=e^(1/2)e^(-x^2/(2r^2))`; Fourier inversion of the Gaussian and the envelope, with u=r|t|, give

`P<=e^(1/2)sqrt(2/pi)[ integral_0^(t0r) e^(-u^2/2)du +(t0r)^alpha integral_(t0r)^infinity e^(-u^2/2)u^(-alpha)du]`,

which is at most (4.1) when t0r<=1. For alpha=2/5,

`C_(2/5)=3.7379978492...`.

Consequently the ridge characteristic argument is useful to the quarter splice already when beta>=2/5; it need not reach the beta>1 threshold needed for a bounded density of Y itself.

## 5. Every Schur cross bank of fixed first singular value is now paid

Assume the pivot pair above has m>0 and the exact Schur complement S has a disjoint original-coordinate cut I,J with

`s1(C)>=sigma>0`,  C=S[I,J].

I claim this alone implies a universal essential-density bound for Q, with a constant depending only on m and sigma.

### Case A: `s2(C)>=sigma/8`

Take q=2 and gamma=s2(C)/2. The two leading ridge eigenvalues are at least 4/5. Hence theta>=8/5, beta=theta/(2q)>=2/5, and `max diag K<=1=q/2` automatically. The ridge source gives

`t0<=L_2/(2gamma)=pi e/s2(C)<=8 pi e/sigma`.

Use Section 4 with alpha=2/5 and then Lemma 2.1.

### Case B: `s2(C)<sigma/8`

Write the top singular pair as s1 u v^T. Take q=1 and gamma=s1/2. The leading ridge weight is 4/5 and the tail ridge operator norm is <1/16.

If `max_i u_i^2<=35/64`, then

`K_ii <= (4/5)(35/64)+1/16=1/2=q/2`,

while theta>=4/5 and beta>=2/5. Thus

`t0<=pi e sqrt(2)/s1<=pi e sqrt(2)/sigma`,

and the same Hölder splice closes. If u is not diffuse but the right singular vector v is, apply the same argument to C^T.

It remains that both u and v are localized. Choose i,j with `u_i^2>35/64` and `v_j^2>35/64`. If E=C-s1uv^T, then `||E||=s2(C)<sigma/8`, so

`|C_ij| >= s1|u_i v_j|-s2(C)`
`> (35/64)sigma-(1/8)sigma = 27sigma/64`.                       (5.1)

Condition all Schur variables except the physical coordinates i,j. Lemma 3.1 gives exponent alpha=3/8 for kappa, and Lemma 2.1 closes Q.

Thus the previous `QFORM-SCHUR-CROSS-LOWRIDGE-STABILITY-v1` obstruction is completely removed: low ridge-effective dimension is not an unpaid branch. It either has a diffuse side and supplies enough ridge-Hölder mass, or it localizes into a genuine physical mixed coefficient.

## 6. Push the off-diagonal second-singular threshold from `1/8` to `3/20`

Let

`H=A-diag(A)`

and suppose

`s2(H)<=tau:=3/20`.                                                     (6.1)

Choose a top eigenpair and write

`H=lambda vv^T+R`,  `||R||op<=tau`.

Because H has zero diagonal,

`|lambda| v_i^2=|R_ii|<=tau`,                                         (6.2)

and for i!=j,

`|H_ij|<=|lambda v_i v_j|+|R_ij|<=2tau=3/10`.                         (6.3)

Put D=diag(A) and A0=D+lambda vv^T=A-R. Since the target hypothesis is `s3(A)>=1`, Weyl gives

`s3(A0)>=1-tau=17/20=:h`.                                             (6.4)

A rank-one perturbation raises singular-value counting by at most one, so

`s2(D)>=17/20`.                                                        (6.5)

Thus two physical diagonal entries have magnitude at least h.

If they have the same sign, their physical 2x2 block is definite and, by (6.3),

`|det B| >= h^2-(3/10)^2 = 253/400`.                                  (6.6)

This branch has a uniform density bound by the exact definite-section argument.

Suppose the two heavy diagonals have opposite signs. Set

`d:=53/500`.

If some third diagonal has magnitude at least d, pair it with the heavy diagonal of the same sign. The resulting definite physical block satisfies the deliberately small but positive exact margin

`|det B| >= (17/20)(53/500)-(3/10)^2 = 1/10000`.                      (6.7)

For bounded finite-union product indicators, conditioning all other coordinates makes the inverse image of an interval under this definite two-variable quadratic a translated elliptic shell of area at most `pi |I|/sqrt(det B)`. Therefore

`P(Q in I)<=100 pi |I|`.

Now apply the designated partner account04/B19 theorem `QFORM-FINITE-UNION-CORE-v1`: the identical `100pi` interval bound transfers to every arbitrary independent cap-one input law. This is the partner theorem applied to an actual inequality in this run.

Hence a remaining candidate under (6.1) must have opposite heavy diagonals p,q and

`|D_kk|<53/500` for every k outside {p,q}.                              (6.8)

Since `s3(D)<d`, (6.4) implies

`|lambda|>h-d=93/125=:L`.                                              (6.9)

From (6.2),

`v_i^2< tau/L =25/124=:u`.                                             (6.10)

Let T be the outside coordinates, `r^2=||v_T||^2`, and `w=v_T/r`. Then

`r^2>1-2u=37/62=:R2`,                                                   (6.11)
`max_k w_k^2 < u/R2 =25/74<1/2`.                                      (6.12)

## 7. Exact mixed three-plane still has a positive gap

In the orthonormal basis `(e_p,e_q,w)`, after a global sign and relabeling if needed, define the core

`M0=diag(a,-b,0)+lambda (x,y,r)^T(x,y,r)`,

where a,b>=h, x^2,y^2<=u, r^2>=R2 and |lambda|>=L.

Its inverse is exactly

`[[1/a,0,-x/(ar)],`
` [0,-1/b,y/(br)],`
` [-x/(ar),y/(br),1/(lambda r^2)+x^2/(a r^2)-y^2/(b r^2)]]`.

Therefore

`||M0^(-1)||F^2`
`<=2/h^2 + 4u/(h^2 R2) + [(1/L+2u/h)/R2]^2`
`=49579300/3560769`
`< (1000/267)^2`.                                                       (7.1)

Hence

`s_min(M0)>267/1000`.                                                   (7.2)

The actual A-compression to this three-plane differs from M0 by the R-compression plus the outside diagonal compression. Its operator norm is less than

`tau+d = 32/125 =256/1000`.

Weyl now gives the exact strict gap

`boxed: s_min(A|span(e_p,e_q,w)) > 11/1000 =:delta.`                   (7.3)

This is the same product-preserving mixed-coordinate/aggregate geometry as the preceding B19 normal form, but at the larger off-diagonal threshold 3/20.

## 8. Convert the `11/1000` gap to an original-coordinate Schur bank and close it

The opposite-sign physical pivot pair B is invertible and has diagonal magnitudes at least m=h=17/20. Let S be its exact Schur complement. The scalar Schur complement of the 3x3 compression along w is `w^T S w`; by the block inverse identity and (7.3),

`|w^T S w|>delta=11/1000`.                                             (8.1)

If some physical Schur diagonal obeys

`|S_ii|>=delta/4=11/4000`,                                             (8.2)

conditioning all other original coordinates gives the standard one-coordinate square-root small-ball bound, and the preceding quarter-kernel splice closes Q. Numerically this branch is <34.

Otherwise put O=S-diag(S). Then

`|w^T O w|>3delta/4`.

A random bipartition of the outside physical coordinates has expected signed cross contribution equal to one quarter of `w^T O w`; hence some disjoint I,J satisfy

`|w_I^T S[I,J] w_J|>3delta/16`.

Since `||w_I|| ||w_J||<=1/2`,

`s1(S[I,J]) > 3delta/8 = 33/8000 =:sigma`.                             (8.3)

Section 5 pays every such cross bank. Using alpha=2/5 in the two ridge cases and alpha=3/8 in the localized case gives, with m=17/20 and sigma=33/8000, the safe numerical bounds

- two-singular-value ridge branch: `<688`;
- one-diffuse-side ridge branch: `<346`;
- both-localized physical mixed-entry branch: `<130`.

Together with (6.6)-(6.7) and (8.2), this proves the following target-level branch theorem.

### Theorem 8.1 — `QFORM-OFFDIAG-S2-3OVER20-CLOSURE-v1`

Under the exact owner target hypotheses, if

`s2(A-diag(A))<=3/20`,

then `Q=X^TAX` has an essentially bounded density satisfying the universal branch bound

`||p_Q||_infinity <700`.

The bound is intentionally not optimized. The proof is valid for arbitrary signs, repeated eigenvalues, arbitrary extra spectrum, arbitrary dimension, and arbitrary independent cap-one coordinate densities. It never rotates the input product law. A continuous representative is not proved in the quarter-splice/localized branches.

The ridge-dependent subbranches use the complete source proof of `QFORM-RIDGE-DENSITY-v1`; that extension is still awaiting its requested independent review, so this dependency status must remain visible until that review lands.

## 9. Residual and next implication

Combining this run with the previous B19 near-diagonal/stable-rank reductions, any remaining counterexample must in particular satisfy

`||A-diag A||op>7/16`,
`sr(A-diag A)<32`,
`and s2(A-diag A)>3/20`.

The first unpaid structural implication is now

`QFORM-TWO-OFFDIAGONAL-RESOURCE-EXTRACTION-3OVER20-v1`:

from `s2(H)>3/20` under the three-large-eigenvalue hypothesis, force an original-coordinate product-preserving resource paid by the existing analytic mechanisms (a definite physical pair, a ridge-Hölder cross bank, a localized mixed coefficient, or an aggregate rank-two bank), without using the refuted fixed-minor/local-Schur dichotomies.

A concrete next handle is random sign-cut averaging. For a diagonal sign matrix D_eps and

`M_eps=(H-D_eps H D_eps)/2`,

M_eps is exactly the cross part of H across the induced original-coordinate cut and `E M_eps=H/2`. Convexity of Ky Fan norms therefore guarantees a cut with

`||M_eps||_(4)>=||H||_(4)/2`.

Since the nonzero singular values of M_eps are the singular values of its cross block, each repeated twice, this yields

`s1(C)+s2(C) >= [s1(H)+s2(H)+s3(H)+s4(H)]/4`.

This does not by itself force s2(C), but it is an exact product-coordinate starting point for the next mechanism and avoids a single-minor reciprocal loss.

## 10. Status

Newly proved here: the Hölder quarter-splice, the physical mixed-coordinate `3/8` small-ball lemma, the below-density-threshold ridge-to-Hölder conversion, complete closure of the prior fixed-s1 Schur cross-bank residual, and the target-level closure of the entire `s2(A-diag A)<=3/20` branch.

Applied designated partner mathematics: account04/B19 finite-union-core theorem, used explicitly in the `100pi` definite physical-section inequality.

Not proved: the complementary `s2(A-diag A)>3/20` extraction, the full conjecture, or global continuity. No claim of a full solution is made.
