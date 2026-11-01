SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-24T04:07:07Z.
attacking: the exact-null near-coloop same-bank puncture after partner r48; spend an actual original-coordinate transverse Pluecker atom before any dependence-blind L^p split, and isolate the genuinely diffuse transverse remainder.

# fleet02/B11 r12 — null-hub Pluecker atom and sign-specific three-leaf closure

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING THEOREM / TARGET-VALID SAME-BANK SUBCLASS CLOSED / FULL QFORM OPEN**.

The unrestricted owner target remains OPEN / NOT PROVED / NOT DISPROVED. The results below concern the exact-rank-three null-pivot near-coloop chamber isolated by the designated partner. Arbitrary additional nonseparable spectrum remains a separate bridge. No moments, support bounds, log-concavity, identical laws, post-rotation independence, conditional-density-as-independence, or two-sheet X-ray transfer is used. Continuity is kept separate: the new estimates are essential-density estimates unless explicitly stated otherwise.

## 1. Inputs actually consumed

The latest completed compatible designated-partner result read in full is fleet03/B11 r48:

- canonical mathematics `yspennstate/math-open-problems@1981b7ded0883caf72e23b833f34274a6763a43c`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260924T023910Z-fleet03-B11-QFORM-r48/REPORT.md`.

Its correction `QFORM-SAMEBANK-L3-L32-DEPENDENCE-BARRIER-v1` constructs, for arbitrarily small puncture `eta`, a nonlinear same-bank residual law for which both the hyperbolic `L^3` resource and the square `L^(3/2)` resource are finite while their dependent sum retains the rank-two logarithmic blow-up. It is not a QFORM counterexample because the residual triple is not an orthogonal linear projection of independent originals. Therefore a valid proof must spend original-product projection provenance before replacing the residual law by marginal or joint density caps.

The required pinned source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was also consumed. In particular its completed ruled-level-set Theorem C gives the universal one-sheet estimate `pi sqrt(2)/s` for exact rank-three signatures `(2,1)` and `(1,2)` whose nonzero eigenvalue magnitudes are at least `s`. I apply that theorem below to an explicit same-bank target family and do not extend it to the opposite two-sheet side.

I also use the completed fleet02/B16 null-scalar/dependent-pair receiver (`QFORM-NULL-SCALAR-DEPENDENT-PAIR-v1`, canonical source `yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`) and first record the affine extension needed after conditioning physical coordinates.

## 2. Affine null-scalar/dependent-pair receiver

### Theorem 2.1 — `QFORM-NULL-SCALAR-DEPENDENT-PAIR-AFFINE-v1`

Let `X` be independent of a pair `(C,D)`. Assume

`||f_X||_infinity <= F`, `||g_(C,D)||_infinity <= M`.

Let `beta,gamma !=0`; let `alpha,delta,l_X,l_C,l_D,k_0` be arbitrary reals, and put

`Q = 2 beta X C + alpha C^2 + 2 delta C D + gamma D^2
     + l_X X + l_C C + l_D D + k_0`.

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 3 (2MF)^(2/3) |beta^2 gamma|^(-1/3).`                 (2.1)

If

`B=[[0,beta,0],[beta,alpha,delta],[0,delta,gamma]]`,

then `det B=-beta^2 gamma`, hence equivalently

`boxed: ||p_Q||_infinity <=3(2MF)^(2/3)|det B|^(-1/3).`    (2.2)

#### Proof

Condition on `(C,D)=(c,d)`. The affine slope in `X` is

`L(c)=2 beta c+l_X`.

Outside the null set `L(c)=0`, the conditional density kernel at output level `s` is

`K_s(c,d)=|L(c)|^(-1)
 f_X((s-R(c,d))/L(c))`,                                    (2.3)

where `R(c,d)` is quadratic in `d` with leading coefficient `gamma`.

Fix `u>0`. If `K_s(c,d)>u`, then necessarily

`|L(c)|<F/u`.                                               (2.4)

For such a `c`, set `m=u|L(c)|` and `E_m={x:f_X(x)>m}`. Probability normalization gives

`|E_m|<=1/m`.                                               (2.5)

As a function of `d`, `(s-R(c,d))/L(c)` is a quadratic with leading coefficient `-gamma/L(c)`. For any quadratic `A(d-d_0)^2+v` and any measurable set `E` of length `L_E`, the two inverse branches give

`|{d:A(d-d_0)^2+v in E}| <=2 sqrt(L_E/|A|)`.                (2.6)

Using (2.5), the allowed `d`-length is therefore at most

`2 / (sqrt(|gamma|) sqrt(u))`.                              (2.7)

The `c`-set in (2.4) has length `F/(|beta|u)`. Consequently

`|{(c,d):K_s(c,d)>u}|
 <= [2F/(|beta|sqrt(|gamma|))] u^(-3/2).`                   (2.8)

Use both `g<=M` and `int g=1`, then layer cake:

`p_Q(s)
 <= int_0^infinity min(1,A u^(-3/2)) du
 = 3 A^(2/3),`

where

`A=2MF/(|beta|sqrt(|gamma|))`.                              (2.9)

This is exactly (2.1). No independence inside `(C,D)` is used. The affine terms merely translate the short `c` interval and the quadratic vertex. QED.

This is the precise local smoothing mechanism needed below: a null scalar/hyperbolic pair contributes the borderline reciprocal slope, while the genuinely nonzero third curvature `gamma` converts its superlevel set into weak `L^(3/2)` size. At `gamma=0` the determinant vanishes and the rank-two logarithmic endpoint is no longer removed.

## 3. Sign-specific Schur geometry at a null physical pivot

Let an invertible physical `3x3` block have a null first pivot. Rotate only the last two coordinates by an orthogonal determinant-one map so that the first coordinate couples only to the second. Its matrix becomes

`B=[[0,beta,0],
    [beta,alpha,delta],
    [0,delta,gamma]],       beta gamma !=0.`                (3.1)

The leading hyperbolic block

`H_2=[[0,beta],[beta,alpha]]`

has one positive and one negative eigenvalue. Moreover

`H_2^(-1)=[[-alpha/beta^2,1/beta],[1/beta,0]]`,

so the Schur complement in the third coordinate is exactly

`gamma - [0,delta]H_2^(-1)[0,delta]^T = gamma`.             (3.2)

Therefore

- `gamma>0` gives signature `(2,1)`;
- `gamma<0` gives signature `(1,2)`;
- `det B=-beta^2 gamma`.

The cross coefficient `delta` can shear the two sheets but cannot change the sign or magnitude of the determinant currency seen by Theorem 2.1. This is the sign-specific form of the third-direction mechanism: after the hyperbolic rank-two saddle, the remaining Schur curvature is exactly `gamma`.

## 4. Null-hub Pluecker atom theorem

### Theorem 4.1 — `QFORM-NULL-HUB-PLUCKER-ATOM-v1`

Let

`A=R M R^T`, `R^T R=I_3`,                                  (4.1)

have exact rank three, and assume the three eigenvalues of `M` have magnitudes at least `s>0`. Let original coordinate `0` satisfy

`A_00=0`, `q=||r_0||^2>0`,                                  (4.2)

where `r_i` is row `i` of `R`.

Rotate only the three-dimensional spectral bookkeeping so

`r_0=sqrt(q)e_1`.

For `i!=0`, decompose

`r_i=a_i e_1+b_i`, `b_i in e_1^perp ~= R^2`.                (4.3)

Parseval gives

`sum_{i!=0} b_i b_i^T=I_2`.                                 (4.4)

Define the transverse Pluecker weights

`omega_ij=det(b_i,b_j)^2`,
`omega_*=max_{i<j} omega_ij`.                               (4.5)

Then

`sum_{i<j} omega_ij=1`,                                     (4.6)

and for arbitrary independent original coordinates with one-dimensional density caps at most one,

`boxed:
 ||p_(X^T A X)||_(infinity,ess)
 <=3*2^(2/3) (|det M| q omega_*)^(-1/3)
 <=3*2^(2/3) (q omega_*)^(-1/3)/s.`                        (4.7)

#### Proof

Equation (4.6) is the two-dimensional Cauchy-Binet identity applied to (4.4). Choose a pair `(i,j)` attaining `omega_*`. Because the first row is `sqrt(q)e_1`,

`det(R_{0ij})^2=q omega_*`.                                 (4.8)

For the physical principal block `B=A[{0,i,j}]`, exact rank three gives

`det B = det(R_{0ij} M R_{0ij}^T)
       = det M * det(R_{0ij})^2`,

hence

`|det B|=|det M| q omega_*`.                                (4.9)

Condition on every original coordinate except `X_0,X_i,X_j`. The remaining quadratic block is exactly `B`; everything outside it becomes only affine/constant terms. The scalar `X_0` stays genuinely independent of the physical pair `(X_i,X_j)`.

Because `B_00=A_00=0`, rotate only the pair `(X_i,X_j)` so the coupling vector from `X_0` is aligned with the first pair coordinate. This does **not** assert independence after rotation. The rotated pair has joint density

`g(c,d)=f_i((O^T(c,d))_1) f_j((O^T(c,d))_2) <=1`

because `|det O|=1`; and the whole pair remains independent of `X_0`. Theorem 2.1 with `F=M=1` gives, uniformly in every conditioned outside value,

`||p_(Q | outside)||_infinity
 <=3*2^(2/3)|det B|^(-1/3)`.                               (4.10)

Average the conditional densities and substitute (4.9). QED.

### Corollary 4.2 — finite residual support

If exactly `m` residual original coordinates carry the active frame, then (4.6) gives

`omega_* >= 1/binom(m,2)`,

so

`boxed:
 ||p||_infinity
 <=3*2^(2/3) [binom(m,2)/q]^(1/3)/s.`                     (4.11)

At the live near-coloop threshold `q>=63/64`, the `m=3` constant is

`3*2^(2/3)*(3*64/63)^(1/3)
 =6.904434991977456...`.                                    (4.12)

Thus every exact r45 null-pivot same-bank model whose residual orthogonal triple is supported on three original coordinates is paid on the **entire line**, uniformly through puncture size zero. The argument never replaces the rotated residual triple by independent coordinates.

### Corollary 4.3 — obstruction to a source-valid counterexample sequence

Let `D=||p||_infinity` and assume `|det M|>=s^3`. From (4.7), any sequence in this null-pivot chamber with `sD>=L` must satisfy

`omega_* <=108/(q L^3)`.                                    (4.13)

If the residual support size is `m`, then necessarily

`binom(m,2) >= q L^3/108`.                                  (4.14)

Hence any source-valid sequence trying to imitate the r48 logarithmic cancellation while making the normalized density height diverge must have

- residual support size tending to infinity, and
- every individual transverse original-coordinate Pluecker atom tending to zero.

The partner r48 nonlinear cancellation therefore cannot be realized by a true product model while a fixed physical transverse area survives.

## 5. Concrete genuine same-bank target family

Let `H,X_1,X_2,X_3` be mutually independent, each with density cap at most one. Define the orthonormal residual linear forms

`T=(X_1+X_2+X_3)/sqrt(3)`,
`W=(X_1-X_2)/sqrt(2)`,
`V=(X_1+X_2-2X_3)/sqrt(6)`.                                 (5.1)

No independence among `(T,W,V)` is asserted; for arbitrary non-Gaussian product inputs they are generally dependent and they use the same original source bank.

For `0<q<=1`, `kappa>0`, `c!=0`, put

`Q=2 kappa (sqrt(q) H+sqrt(1-q) T) W + c V^2`.              (5.2)

In the orthonormal bookkeeping coordinates `(H,T,W,V)`, the quadratic matrix is

`[[0,0,kappa sqrt(q),0],
  [0,0,kappa sqrt(1-q),0],
  [kappa sqrt(q),kappa sqrt(1-q),0,0],
  [0,0,0,c]]`.                                               (5.3)

The combination

`L=sqrt(q)H+sqrt(1-q)T`

is unit and orthogonal to `W,V`, while the orthogonal combination in `span(H,T)` is the kernel. Hence

`spec(Q)={+kappa,-kappa,c,0}`.                              (5.4)

So if `kappa>=s` and `|c|>=s`, (5.2) is an exact owner-target family. It has signature `(2,1)` when `c>0` and `(1,2)` when `c<0`.

For the residual frame (5.1), every transverse two-row Pluecker atom is exactly

`omega_12=omega_13=omega_23=1/3`.                           (5.5)

Therefore Theorem 4.1 gives

`boxed:
 ||p_Q||_infinity
 <=3*2^(2/3) [3/(q kappa^2 |c|)]^(1/3).`                  (5.6)

In particular, for `q>=63/64` and `kappa,|c|>=1`,

`boxed: ||p_Q||_infinity <=6.904434991977456... .}`          (5.7)

This is a genuine same-bank third-square closure: `T,W,V` share the same three independent originals, yet the full two-sheet side is paid because a physical null triple retains determinant currency.

## 6. Rank-two logarithm and exactly how the third direction removes it

Set `q=1` and first delete the third direction by taking `c=0`. Choose `H,X_1,X_2` to be centered unit uniforms. Then `W=(X_1-X_2)/sqrt(2)` has density

`p_W(w)=sqrt(2)(1-sqrt(2)|w|), |w|<=1/sqrt(2)`,             (6.1)

so `p_W(w)>=1/sqrt(2)` on `|w|<=1/(2sqrt(2))`. For

`R=2 kappa H W`,                                             (6.2)

the product formula gives, whenever `0<|t|<|kappa|/(2sqrt(2))`,

`p_R(t)
 >= [1/(sqrt(2)|kappa|)]
    log(|kappa|/(2sqrt(2)|t|))
 -> infinity` as `t->0`.                                    (6.3)

Thus the opposite-sign rank-two singularity remains genuinely logarithmic inside the same construction.

Restore `cV^2`. The square is **not** source-disjoint from `W`; ordinary convolution is unavailable. The third direction removes the logarithm as follows. A physical pair with transverse area `omega_*>0` and the original null hub gives an invertible physical triple. After the allowed two-dimensional pair rotation, its sign-specific Schur form is (3.1): the first two variables are a hyperbolic pair and the third Schur curvature is exactly `gamma`, with

`|beta^2 gamma|=|det M| q omega_*`.                          (6.4)

The rank-two reciprocal slope is therefore not asserted bounded. Instead, the third curvature turns each kernel superlevel into a `u^(-3/2)` set in (2.8); layer cake integrates that endpoint and produces the determinant-homogeneous `|det|^(-1/3)` bound. At `gamma=0` the determinant disappears and the logarithm (6.3) is allowed to survive. This is the exact local mechanism by which the third direction removes the rank-two log.

## 7. Required pinned ruled result applied at its exact sign scope

Apply the completed Theorem C from the required pinned `e5f71d79...` source to the concrete family (5.2). Since its nonzero eigenvalues are `{+kappa,-kappa,c}`:

- if `c>0`, signature is `(2,1)` and

  `boxed: p_Q(t)<=pi sqrt(2)/s  for t>=0;`                  (7.1)

- if `c<0`, apply Theorem C to `-Q`, giving

  `boxed: p_Q(t)<=pi sqrt(2)/s  for t<=0.`                  (7.2)

The opposite side is the two-sheet side. I do **not** transfer the ruled/X-ray estimate there; the live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` forbids that inference. The full-line bound (5.6), not the ruling, pays the two-sheet side in this same-bank family.

At `s=1`, the ruled one-sheet constant is `pi sqrt(2)=4.442882938158366...`, while the Pluecker/null-scalar full-line constant at `q>=63/64` is `6.904434991977456...`.

## 8. What partner r48 now rules out, and what this theorem adds

Partner r48 already proves that the marginal statement

`hyperbolic part in L^3` + `square part in L^(3/2)`

cannot be combined under arbitrary same-bank dependence, even if the residual joint density and coordinate marginals are capped. Its cancellation uses the nonlinear relation

`T=R-V^2/(2 eta W)`,

which hides the square inside the puncture and reduces the pulled-back original quadratic form to rank two.

Theorem 4.1 gives a complementary source-valid obstruction: in a **true** orthogonal product projection, such a cancellation cannot support unbounded density while any fixed transverse physical Pluecker atom remains. The original-coordinate determinant `|det M| q omega_ij` survives conditioning and forces the affine null-scalar receiver. Therefore a genuine counterexample sequence in the exact null-pivot chamber must be simultaneously

1. high-dimensional;
2. transverse-Pluecker diffuse (`omega_*->0`);
3. outside all already-paid large-leaf/pair-area exits; and
4. capable of using the same-bank puncture without creating a source-disjoint square or usable volume exit.

This is strictly narrower than the dependence-blind r48 interface.

## 9. First unpaid implication

`QFORM-R48-DIFFUSE-TRANSVERSE-PLUCKER-COMPILER-v1`:

In the exact-rank-three r45/r48 null-pivot normal form, after the large-leaf/pair-area exits and after Theorem 4.1 removes every fixed transverse Pluecker atom, prove a universal opposite-two-sheet essential-density bound in the regime

`max_{i<j} det(b_i,b_j)^2 ->0`,                              (9.1)

using the exact orthogonal-product factorization of the residual source before any dependence-blind `L^3 x L^(3/2)` split; or force a source-disjoint square, rank-two crossing, physical-pair, or volume exit.

The existing transverse two-frame has total Pluecker mass one by (4.6), so the unpaid issue is now an **aggregation problem**, not absence of third-direction currency. Partner r48 says the aggregation cannot be done from marginal/joint caps alone. A successful proof must spend factorization across the many small original-coordinate atoms.

Separately unpaid: the nonzero-pivot collar and arbitrary additional nonseparable spectrum needed for the unrestricted owner target; full-target continuity also remains separate.

## 10. Scope summary

Proved in this run:

- affine extension of the dependence-safe null-scalar/dependent-pair receiver, with the same determinant exponent;
- the sign-specific Schur identity showing the surviving third curvature exactly;
- `QFORM-NULL-HUB-PLUCKER-ATOM-v1`, a full-line original-coordinate estimate for every exact-rank-three null-pivot model with a transverse Pluecker atom;
- the finite-residual-support corollary and quantitative obstruction `m >= Omega((sD)^(3/2))` for a would-be blow-up sequence;
- a concrete genuine same-bank three-leaf family with exact spectrum `{+kappa,-kappa,c,0}` and uniform full-line bound `<6.905` at target scale;
- an explicit logarithm at the rank-two endpoint and an exact explanation of how the third Schur curvature removes it;
- the required pinned ruled theorem applied only on the correct one-sheet side.

Not proved:

- dimension-free aggregation in the transverse-Pluecker-diffuse same-bank regime;
- the separate nonzero-pivot collar;
- arbitrary additional nonseparable spectrum;
- the unrestricted QFORM conjecture;
- a new continuity theorem beyond scopes already supplied by cited inputs.
