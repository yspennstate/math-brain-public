SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T22:26:14Z.
attacking: target-level regularity through an explicit Schur-remainder small-ball estimate for an indefinite physical pair, then same-constant C0 closure.

# fleet03/B15 — physical-entry Schur small-ball and quantitative indefinite-pair regularity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T222614Z-fleet03-B15-qform-auto27`  
Status: `SCHUR_SMALLBALL_LEMMA_PROVED / INDEFINITE_PAIR_BRANCH_EXTENDED / PARTNER_APPLIED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and first unpaid implication

The unrestricted owner theorem remains OPEN. This run proves a new quantitative branch for arbitrary dimension and arbitrary rough cap-one marginals. It keeps the original coordinates throughout.

Let two ORIGINAL coordinates be denoted by `U=(U1,U2)` and all remaining original coordinates by `Z`. Write the physical block decomposition

`A = [[D,B],[B^T,C]]`,

where `D` is the selected `2x2` principal block. If `D` is invertible indefinite, define the physical Schur remainder

`S = C-B^T D^(-1) B`.

If `rank(A)>=3`, then `S!=0` because `rank(A)=2+rank(S)`. The new point is that **every nonzero physical Schur remainder, of arbitrary rank and sign, has an elementary dimension-free square-root small-ball estimate depending on one actual physical coefficient**. Combining that estimate with the completed logarithmic two-coordinate envelope yields an explicit density bound. The constant may deteriorate when all relevant physical entries become tiny, so this is not yet the universal spectral theorem.

The hard remaining structural implication is therefore sharper: either produce a quantitatively paid nonsingular physical pair and Schur entry, or route the singular/ill-conditioned physical-pair geometry into the already-paid grouped-bank/diffuse/ridge branches. No such universal extraction is claimed here.

## 2. Elementary physical-entry half-small-ball lemma

### Lemma 2.1 — `QFORM-PHYSICAL-ENTRY-HALF-SMALLBALL-v1`

Let `Z=(Z1,...,Zm)` have independent real coordinates with probability densities bounded by one. Let `S` be a nonzero real symmetric `m x m` matrix, and let

`R(Z)=Z^T S Z + ell^T Z + c`.

Define a positive physical coefficient `eta(S)` as follows:

- if some diagonal entry of `S` is nonzero, set

  `eta(S)=max_i |S_ii|`;

- if every diagonal entry vanishes, set

  `eta(S)=max_{i<j}|S_ij|`.

Then for every `rho>0` and every `t in R`,

`boxed( P(|R-t|<rho) <= 2 sqrt(2) sqrt(rho/eta(S)). )`            (2.1)

The right side is allowed to exceed one. No moment, support, connectedness, smoothness or identical-law assumption is used.

### Proof: nonzero diagonal case

Choose `i` with `|S_ii|=eta`. Condition on every coordinate except `Zi`. Independence preserves the cap-one density of `Zi`. On a conditional fiber,

`R = a Zi^2 + b Zi + d`,

where `a=S_ii` and `b,d` may depend arbitrarily on the conditioned coordinates. Completing the square reduces the event to

`|x^2-v|<delta`,

with `delta=rho/|a|`. Its Lebesgue measure is at most `2 sqrt(2 delta)`:

- if `v<=-delta`, the set is empty;
- if `-delta<v<delta`, it lies in `|x|<sqrt(v+delta)` and has length at most `2sqrt(2delta)`;
- if `v>=delta`, its length is

  `2[sqrt(v+delta)-sqrt(v-delta)]`,

  which decreases with `v` and equals `2sqrt(2delta)` at `v=delta`.

The cap-one density of `Zi` therefore gives (2.1) conditionally, hence unconditionally.

### Proof: all diagonals zero

Now all `S_ii=0`. Choose `i<j` with `|S_ij|=eta`. Condition on every coordinate except `Zi,Zj`. The remaining polynomial is

`R = 2s Zi Zj + b Zi + d Zj + e`,

with `|s|=eta`. Separate translations of `Zi,Zj` turn this into

`2s X Y + e'`,

while preserving independence and both density caps. Put

`delta=rho/(2|s|)`.

For arbitrary `v`, split the event `|XY-v|<delta` according to `|X|<=sqrt(delta)` and its complement. The first part has probability at most `2sqrt(delta)`. On the complement, conditional on `X=x`, the admissible `Y` interval has length `2delta/|x|<=2sqrt(delta)`, hence conditional probability at most that amount. Therefore

`P(|XY-v|<delta) <=4sqrt(delta)
 =2sqrt(2) sqrt(rho/|s|)`.

This is (2.1). QED.

### Remarks

1. The lemma is genuinely product-preserving: conditioning is only on other ORIGINAL coordinates.
2. It is not a spectral lower bound. `eta(S)` may tend to zero with dimension even when `S` carries a fixed nonzero spectral direction.
3. It works for arbitrary rank and sign of `S`, unlike the earlier rank-one affine small-ball input.

## 3. Indefinite physical-pair Schur theorem

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-SCHUR-ENTRY-v1`

Let `X=(U,Z)` have independent real coordinates with density caps one. Suppose the physical `2x2` principal block `D` on the ORIGINAL coordinates `U=(U1,U2)` is invertible and indefinite. Set

`Delta=|det D|`,
`kappa=sigma_min(D)`,
`S=C-B^T D^(-1) B`.

Assume `S!=0` and let `eta=eta(S)` from Lemma 2.1. Then the full quadratic form

`Q=X^T A X`

has an essentially bounded density satisfying

`boxed( ||p_Q||_infinity
 <= 2^(13/4) (Delta*kappa*eta)^(-1/4). )`                       (3.1)

Numerically `2^(13/4)=9.513656920021768...`.

Every outside coefficient and every pair-to-outside coupling is arbitrary. There is no rank restriction on `S` and no support/moment regularity on the marginals.

### Proof

Include arbitrary affine terms because outside conditioning may create them. Write

`Q(U,Z)=U^T D U +2 U^T B Z + alpha^T U
        +Z^T C Z + beta^T Z +c`.

For fixed `Z`, complete the square in the physical pair:

`Q=(U+m(Z))^T D (U+m(Z)) + R(Z)`,                                (3.2)

where

`m(Z)=D^(-1)(BZ+alpha/2)`

and

`R(Z)=Z^T S Z + tilde_beta^T Z + tilde_c`.                       (3.3)

For each fixed `Z=z`, the two translated pair coordinates remain independent and retain density caps one.

The completed physical-pair logarithmic envelope (rederived in the source-pinned pair-log theorem and used here in its exact scope) says that for every gradient cutoff `r>0`, the conditional pair output has a density satisfying

`p_(Q|Z=z)(t)
 <= 2sqrt(2)/r
 + Delta^(-1/2) log_+( 2r^2/[kappa |t-R(z)|] ).`                 (3.4)

For completeness, (3.4) is obtained by splitting the translated pair into `|D u|>r` and `|D u|<=r`. On the first region original-coordinate one-variable inversion gives `2sqrt(2)/r`. On the second, only the joint density cap `<=1` is used: diagonalize `D` as a change of Lebesgue variables, then use hyperbolic coordinates `x+y,x-y`; the bounded gradient region lies in a square of side scale `r/sqrt(kappa)`, and the `uv` pushforward contributes the logarithm. No independence is asserted after diagonalization.

Average (3.4) in `Z`. Lemma 2.1 gives, with

`H=2sqrt(2)/sqrt(eta)`,                                           (3.5)

`P(|R-t|<rho)<=H sqrt(rho)` for every `rho,t`. Hence layer cake gives, for every `a>0`,

`E log_+(a/|t-R|)
 =int_0^infinity P(|t-R|<a e^(-v)) dv
 <=H sqrt(a) int_0^infinity e^(-v/2) dv
 =2H sqrt(a).`                                                     (3.6)

Use `a=2r^2/kappa` in (3.4):

`p_Q(t)
 <=2sqrt(2)/r
   +2sqrt(2) H r/sqrt(Delta*kappa).`                              (3.7)

Optimizing over `r` gives

`r^2=sqrt(Delta*kappa)/H`

and therefore

`||p_Q||_infinity
 <=4 sqrt(2H) (Delta*kappa)^(-1/4).`                              (3.8)

Substituting (3.5),

`4 sqrt( 4sqrt(2) eta^(-1/2) )
 =2^(13/4) eta^(-1/4)`,

which proves (3.1). QED.

## 4. Immediate target corollary: every paid indefinite physical pair

If `A` is in the owner's target, then `rank(A)>=3`. If it has an invertible indefinite physical `2x2` principal block `D`, the Schur rank identity

`rank(A)=rank(D)+rank(S)=2+rank(S)`                                (4.1)

forces `S!=0`. Thus Theorem 3.1 applies automatically and gives

`boxed( ||p_Q||_infinity
 <=2^(13/4)( |det D| sigma_min(D) eta(S) )^(-1/4). )`             (4.2)

This is an explicit fixed-matrix target bound for arbitrary dimension and arbitrary rank/sign of the Schur remainder. It is not universal because the bare three-large-eigenvalue condition does not force the physical certificate in (4.2) to stay away from zero.

The theorem strictly broadens the earlier exact-rank-three use of the pair-log envelope: the old residual was forced to be rank one and paid by a spectral coefficient; here the residual may have arbitrary rank and sign, and only one actual nonzero physical Schur coefficient is needed.

## 5. Definite physical pair companion

If the selected invertible `2x2` physical pair `D` is positive or negative definite, then for every conditional outside configuration completing the square translates the pair but preserves its coordinate density caps. The pushforward of Lebesgue measure under the definite quadratic form has constant radial density `pi/sqrt(|det D|)`. Therefore

`boxed( P(Q in I) <= [pi/sqrt(|det D|)] |I|,
        ||p_Q||_infinity <=pi/sqrt(|det D|). )`                   (5.1)

Thus, whenever a target matrix has ANY nonsingular physical `2x2` principal block, there is an explicit finite height certificate: (5.1) in the definite case and (4.2) in the indefinite case.

This does not contradict the known hard sign/Hadamard configurations: a symmetric matrix of rank at least three can have every physical `2x2` principal determinant equal to zero, so nonsingular-pair extraction is not automatic.

## 6. Designated partner applied to an actual inequality: same-constant C0 closure

The latest completed designated partner result is fleet04/B15,

`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260923T221909Z-fleet04-B15-ruled-trace-c0-r8/REPORT.md`.

Its Theorem 6.1 states: for every fixed target/product instance with `rank(A)>=3`, any separately proved interval domination

`P(Q in I)<=M|I|`

upgrades to a canonical representative `p_Q in C_0(R)` with the **same** pointwise height `||p_Q||_infinity<=M`.

Apply that theorem to the actual interval inequality furnished by (3.1). Because `D` is invertible and `S!=0`, (4.1) gives `rank(A)>=3`. Hence

`boxed( p_Q in C_0(R),
        ||p_Q||_infinity
        <=2^(13/4)(Delta*kappa*eta)^(-1/4). )`                    (6.1)

Likewise, for a definite physical pair inside any target instance,

`boxed( p_Q in C_0(R),
        ||p_Q||_infinity<=pi/sqrt(|det D|). )`                    (6.2)

This is a genuine use of the partner result at an actual inequality. Continuity is not used to obtain either height bound; it is added afterwards with zero constant loss.

## 7. Concrete full-target cross-coupled family

Let

`D=[[0,2],[2,0]]`, `S=[2]`, `B=(u,v)^T`,

and choose the third diagonal entry so that the Schur remainder stays exactly `2`. Since

`B^T D^(-1) B = u v`,

consider

`A_(u,v)=
 [[0,2,u],
  [2,0,v],
  [u,v,2+uv]].`                                                   (7.1)

For `|u|,|v|<=1/4`, compare with

`A_0=[[0,2,0],[2,0,0],[0,0,2]]`,

whose eigenvalues are `-2,2,2`. The perturbation has Frobenius norm

`sqrt(2u^2+2v^2+u^2v^2)
 <=sqrt(65/256)=0.5038911092686593...`.

Weyl therefore gives three eigenvalues of `A_(u,v)` with absolute value at least

`2-0.5038911092686593...=1.4961088907313407...>1`.

So every matrix in this two-parameter family is literally in the owner target. Here

`Delta=4`, `kappa=2`, `eta(S)=2`,

and (6.1) gives, for every three independent cap-one input laws,

`boxed( p_Q in C_0(R),
        ||p_Q||_infinity <=2^(9/4)
        =4.756828460010884... . )`                                (7.2)

The bound is uniform in the displayed cross couplings `u,v` throughout this target chamber because the Schur remainder is held fixed.

## 8. Absolute continuity versus boundedness versus continuity

This run keeps the three statements separate.

1. **Absolute continuity.** For any nonconstant quadratic polynomial under an absolutely continuous joint input law, qualitative absolute continuity follows by coarea away from the proper affine critical set. This alone gives no useful height.
2. **Essential boundedness.** Equations (3.1), (4.2), and (5.1) are obtained before any continuity input, at the interval/density-height level.
3. **Continuous representative.** Equation (6.1) uses the completed fixed-matrix rank-at-least-three partner theorem only after the interval constant has been paid. No law-uniform modulus of continuity is asserted.
4. **Full universal target.** Still OPEN. The physical certificate `|det D| sigma_min(D) eta(S)` may collapse, and target matrices may have no nonsingular physical pair at all.

## 9. Exact next step

The productive next structural question is not another regularity argument. It is whether the three-large-eigenvalue condition admits a product-preserving decomposition in which either

- a nonsingular physical pair has `|det D| sigma_min(D) eta(S)` bounded below after aggregation, or
- the matrix is forced into an already-paid grouped-bank, projected-crossing, ridge-window, or diffuse exit.

The known no-single-minor and sign/Hadamard counterexamples rule out claiming such a lower bound for one raw pair. Aggregation must precede reciprocal payment in the remaining chamber.

## 10. Source and integrity ledger

Fresh owner controls were read from `yspennstate/math-research-brain` main; owner-control revision remains `2026-09-22.15` and the full conjecture remains OPEN. Relevant live corrections retained include: no post-rotation independence, no generic arbitrary-joint coarea height theorem, no naive fiber-sup dimension-free argument, no universal fixed fragment count, and no single physical-minor extraction theorem.

Analytic source used for the conditional indefinite-pair envelope:
`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Designated partner actually applied:
`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260923T221909Z-fleet04-B15-ruled-trace-c0-r8/REPORT.md`.

No Gaussian, log-concavity, moment, compact-support, connected-support, post-rotation-independence or pointwise oscillatory-decay assumption is used. No Monte Carlo claim is used. The numerical constants in Section 7 are finite algebra/Weyl checks only.
