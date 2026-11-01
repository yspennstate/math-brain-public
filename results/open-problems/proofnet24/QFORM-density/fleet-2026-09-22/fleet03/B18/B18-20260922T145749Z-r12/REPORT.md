# fleet03/B18 — literature transfer to banked Schur smoothing

**Run:** `B18-20260922T145749Z-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** literature-to-proof transfer  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full conjecture:** **OPEN / NOT PROVED**

This run changes mechanism from the preceding two-coordinate cross-averaging route.  It aggregates disjoint original-coordinate banks first and only then performs a Schur pivot.  The point is to avoid paying a reciprocal physical minor before the product source has been compressed.

## 1. Exact literature input

Two equivalent source-valid one-dimensional marginal inputs are available.

* Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949, Theorem 1.1: for a product density `prod_i f_i` with every `||f_i||_infinity<=1`, every one-dimensional orthogonal marginal has density at most `sqrt(2)`.
* Rudelson--Vershynin, *Small ball probabilities for linear images of high-dimensional distributions*, Theorem 1.2, records the sharp one-dimensional form explicitly: if `sum a_i^2=1`, then `sum a_i X_i` has density at most `sqrt(2)`.  Their proof combines Rogozin's convolution extremal theorem with Ball's cube-slicing theorem.  Rogozin's primary source is B. A. Rogozin, *The Estimate of the Maximum of the Convolution of Bounded Densities*, Theory Probab. Appl. 32 (1987), 48--56, DOI 10.1137/1132004; Ball's primary source is K. Ball, *Cube slicing in R^n*, Proc. Amer. Math. Soc. 97 (1986), 465--473, DOI 10.1090/S0002-9939-1986-0840631-0.

The hypotheses match the owner target exactly for the linear aggregate: independence plus one-dimensional density caps.  No moments, centering, connected support, compact support, identical laws, Gaussianity or log-concavity enter.  No rotated eigen-coordinate independence is asserted.

Thus for every unit vector `u` supported on an original-coordinate bank `I`,

`Y=<u,X_I>` satisfies `||p_Y||_infinity <= sqrt(2)`.                    (1.1)

A singleton bank has the sharper cap `1`.

## 2. Completed peer inputs read in full

### 2.1 Fresh two-bank definite compression

`fleet01/B18`, canonical report

`yspennstate/math-open-problems@af33ca7715dcdf248d4bb4732ee533a1f47b253b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260922T145319Z-qform-B18-a01-r12/REPORT.md`

proves the following scaled statement.  If independent real `U,V` have density caps `K_1,K_2`, and their quadratic matrix `S` is positive or negative definite, with arbitrary fixed linear terms, then the resulting scalar quadratic polynomial has density cap

`M <= pi K_1 K_2 / sqrt(|det S|)`.                                 (2.1)

The result is obtained in the original product provenance; it does not diagonalize `(U,V)` and then pretend the rotated variables remain independent.

### 2.2 Designated partner: dependent square smoothing

The completed `fleet04/B18` report

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`

proves `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`: if `R` has density cap `M`, and conditionally on `R=r` the variable `V_r` has density cap `1`, then, without any independence assumption,

`||p_{R+a V_R^2}||_infinity <= 2 sqrt(M/|a|)`.                     (2.2)

A scaling consequence used below is important.  If the conditional density cap is `K` instead of `1`, put `W=K V`; then `W` has conditional cap `1` and `aV^2=(a/K^2)W^2`.  Therefore

`||p_{R+a V_R^2}||_infinity <= 2 K sqrt(M/|a|)`.                   (2.3)

This is an actual use of the designated partner theorem, not a replacement by convolution independence.

## 3. New theorem: three-bank Schur smoothing with arbitrary aligned outside coupling

### Theorem `QFORM-THREE-BANK-SCHUR-SMOOTHING-v1`

Partition the original physical coordinates into four disjoint sets

`I_1, I_2, I_3, K`.

For `r=1,2,3`, let `u_r` be a unit vector supported on `I_r` and put

`Y_r=<u_r,X_{I_r}>`, `Y=(Y_1,Y_2,Y_3)^T`.

Assume the full quadratic form has the exact original-coordinate factorization

`Q = Y^T B Y + 2 Y^T L X_K + X_K^T D X_K`,                       (3.1)

where `B` is real symmetric `3 x 3`, `L` and the symmetric `D` are arbitrary.  Thus all coupling from each bank to the other banks and to `K` occurs through its displayed one-dimensional aggregate; the outside block itself is unrestricted.

After permuting the three banks, write

`B = [[C,b],[b^T,a]]`,                                             (3.2)

where `a!=0`, `C` is symmetric `2 x 2`, and set

`S=C-bb^T/a`.                                                       (3.3)

If `S` is positive definite or negative definite, then `Q` has an essentially bounded density and

`boxed( ||p_Q||_infinity <= 4 sqrt(pi) / (|a det B|)^(1/4) ).`     (3.4)

More precisely, if `K_r=||p_{Y_r}||_infinity`, then

`boxed( ||p_Q||_infinity <=
  2 sqrt(pi) K_3 sqrt(K_1 K_2) / (|a det B|)^(1/4) ).`             (3.5)

Here each `K_r<=sqrt(2)` by (1.1), giving (3.4).  Singleton banks may replace their corresponding `sqrt(2)` by `1` in (3.5).

### Proof

Condition on `X_K=w`.  The outside block is then a scalar constant and the bank coupling is a fixed linear term.  Write that linear term as `2d_w^T Y`.  Completing the square only in the third aggregate gives

`Q_w = a( Y_3 + a^{-1}(b^T Y_{12}+d_{w,3}) )^2
      + Y_{12}^T S Y_{12} + 2 e_w^T Y_{12} + c_w`,                 (3.6)

where `Y_{12}=(Y_1,Y_2)` and `e_w,c_w` are fixed after conditioning.

Because the physical banks are disjoint, `Y_1,Y_2,Y_3` are independent before the displayed conditioning and remain independent of `X_K`.  By the completed two-bank definite theorem (2.1), the base variable

`R_w=Y_{12}^T S Y_{12}+2e_w^T Y_{12}+c_w`

has a density satisfying uniformly in `w`

`||p_{R_w}||_infinity <= M := pi K_1K_2/sqrt(|det S|)`.             (3.7)

Now condition further on `R_w=r`.  The translation

`m(Y_{12},w)=a^{-1}(b^T Y_{12}+d_{w,3})`

depends on the variables used to make `R_w`, so the final square is not independent of `R_w`.  However `Y_3` is independent of `(Y_{12},X_K)`.  Consequently the conditional density of

`V=Y_3+m(Y_{12},w)` given `(R_w=r,X_K=w)`

is a mixture of translations of `p_{Y_3}` and is therefore bounded by `K_3` for almost every `(r,w)`.  This is precisely the dependence allowed by fleet04/B18's theorem.

Apply the scaled partner inequality (2.3):

`||p_{Q|X_K=w}||_infinity
 <= 2 K_3 sqrt( pi K_1K_2 / ( |a| sqrt(|det S|) ) ).`              (3.8)

Since `det B = a det S`, (3.8) is exactly (3.5).  Using `K_r<=sqrt(2)` yields (3.4).  Averaging the conditional densities over `X_K` preserves the same essential-supremum bound.  This proves the theorem.

No independence after a rotation or after the square completion was used.  The only conditional statement is the mixture-of-translations cap, which is valid because the third bank is physically disjoint from the variables defining the base residual.

### Continuity status

The theorem proves absolute continuity and an `L^infinity` bound.  I do **not** claim a continuous representative from this argument: the fleet04 dependent-smoothing lemma supplies an essentially bounded density, and the random translation can depend measurably on the base residual.  Continuity remains a separate question for this wrapper.

## 4. Exact fully coupled target family with vanishing physical minors

The theorem is not merely a restatement of a fixed physical `3 x 3` result.  For every `m>=1`, split `3m` physical coordinates into three size-`m` banks and let `c_r` be the normalized all-ones vector on bank `r`.  Let `C_m` be the `3m x 3` matrix with disjoint-support columns `c_1,c_2,c_3`, so `C_m^T C_m=I_3`.  Define

`A_m=C_m B_0 C_m^T`,                                               (4.1)

with

`B_0 = [[31/16, -1/16, 1/4],
        [-1/16, 31/16, 1/4],
        [1/4,    1/4,  -1 ]].`                                    (4.2)

All three bank couplings are nonzero.  The characteristic polynomial factors exactly as

`det(lambda I-B_0)=(lambda-2)(8lambda^2-7lambda-16)/8`,             (4.3)

so the three nonzero eigenvalues are

`2, (7+sqrt(561))/16, (7-sqrt(561))/16`.                           (4.4)

Because `sqrt(561)>23`, their absolute values are all strictly greater than or equal to one.  Thus every `A_m` is a genuine member of the owner's target, in arbitrarily large dimension.  The nonzero spectrum of `A_m` is exactly the spectrum of `B_0` because `C_m` is an isometry on the compressed three-dimensional bank space.

Use the third bank as pivot.  Here

`a=-1`, `b=(1/4,1/4)^T`,
`C=[[31/16,-1/16],[-1/16,31/16]]`,

and the Schur complement is exactly

`S=C-bb^T/a=2 I_2`.                                                 (4.5)

Also `det B_0=-4`.  Therefore (3.4) gives the dimension-free bound

`boxed( ||p_{X^T A_m X}||_infinity
       <= 4sqrt(pi)/4^(1/4)
       = 2sqrt(2pi)
       = 5.013256549262... ).`                                     (4.6)

This holds for **every** choice of independent cap-one physical input densities and every `m`.

At the physical-coordinate level all entries inside and between these diffuse banks are `O(1/m)`.  In particular a principal triple choosing one coordinate from each bank is exactly `B_0/m`, so its least singular value is `O(1/m)`.  The uniform estimate is recovered only after aggregating each physical bank before the Schur payment.  This is the same structural lesson forced by the live `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` correction, now for a genuinely coupled indefinite bank matrix rather than the diagonal `{1,1,-1}` bank example.

`CHECK.py` in this run folder verifies the exact determinant, Schur complement and characteristic-polynomial identities using rational arithmetic, and prints the numerical bound in (4.6).

## 5. What this changes and what remains unpaid

This theorem closes the following source-valid branch:

> three disjoint original-coordinate one-dimensional banks, arbitrary aligned coupling to an arbitrary outside quadratic block, and a compressed scalar pivot whose two-bank Schur complement is definite.

It strictly preserves the original product provenance.  It also shows that diffuse physical minors need not be paid individually: a bank can first be converted to one independent scalar with sharp density cap `sqrt(2)`, after which the fleet04 dependent-square theorem survives the random shift generated by the other banks.

It does **not** establish that the bare hypothesis of three eigenvalues with `|lambda|>=1` forces such a three-bank factorization or a definite compressed Schur pivot.  The live corrections already refute extraction of one uniformly useful physical pivot/minor or one rank-three cross cut.  The full conjecture therefore remains open.

The next target-level structural obligation for this route is an **aggregate-before-pivot dichotomy**: from an arbitrary three-large-eigenvalue matrix, either enter the existing diffuse regularized-determinant branch, or produce a bounded number of disjoint physical aggregates for which the bank coupling is sufficiently exact to invoke (3.4), while controlling the non-bank remainder without destroying the conditional density caps.  Approximate bank factorization cannot simply be treated as an independent additive error; that perturbative step is presently unpaid.

## 6. Status ledger

- `QFORM-THREE-BANK-SCHUR-SMOOTHING-v1`: **PROVED in the stated exact-factorization scope**.
- Fully coupled family (4.1)--(4.2): **PROVED target-valid density bound `2sqrt(2pi)` for all `m` and all cap-one product inputs**.
- Designated partner `fleet04/B18` `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`: **substantively applied** in (3.8), with the conditional cap scaled exactly.
- Fresh `fleet01/B18` two-bank definite theorem: **substantively applied** in (3.7).
- Continuity for the new dependent-smoothing wrapper: **NOT PROVED**.
- Full arbitrary-dimensional three-large-eigenvalue conjecture: **OPEN / NOT PROVED**.
