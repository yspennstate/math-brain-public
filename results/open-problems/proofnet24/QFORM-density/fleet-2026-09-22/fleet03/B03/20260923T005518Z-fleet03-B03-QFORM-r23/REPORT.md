SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T00:55:18Z.
attacking: decoupled time integral — keep the exact hub ambiguity function and use a rank-one physical screen bank to convert the dependent independent-copy integral into an integrable |t|^{-5/4} one-copy bound.

# QFORM-HUB-RANKONE-SCREEN-AMBIGUITY-v1

## Status

**SUPPORTING THEOREM PROVED / FULL QFORM OPEN.** This note proves a new original-coordinate hub/screen theorem with an explicit continuous-density and linear-small-ball bound. It starts from the exact independent-copy ambiguity identity and never treats a coordinate sum and difference as independent. It also applies the valid collision lemma from the designated partner fleet04/B03 to an explicit new inequality. It does not prove the unrestricted three-large-eigenvalue conjecture.

## 1. Setup

Let the original independent cap-one coordinates be split as

`{h} disjoint_union I disjoint_union J_V disjoint_union J_L disjoint_union K`.

Condition on `X_K`; this only changes affine and constant terms in the active variables. Write `w=(A_{hj})_{j!=h}` for the physical hub row, `a=A_hh`, and

`M_V=A[I,J_V]`, `M_L=A[I,J_L]`.

Assume the **rank-one screen condition**

`M_L = u v^T`,

with `u in R^I`, `v in R^{J_L}`, and assume the two deterministic pairs `(w_I,u)` and `(v,w_{J_L})` are linearly independent. Define

`G_I = Gram(w_I,u)`,

`Delta_J = det Gram(v,w_{J_L}) > 0`,

and let the row leverage of coordinate `i in I` in the two-column matrix `[w_I,u]` be

`ell_i = (w_i,u_i) G_I^{-1} (w_i,u_i)^T`.

Assume `max_{i in I} ell_i <= 1/2`.

There is **no restriction** on `M_V=A[I,J_V]`, on any same-bank quadratic block, on `A_hh=a`, on blocks involving conditioned coordinates, on affine terms, or on the signs of the spectrum.

The factorization `M_L=u v^T` is not normalized. The final certificate is invariant under `u -> c u`, `v -> v/c`.

## 2. Theorem

Under the hypotheses above, put

`Xi := det(G_I)^2 * ||v||_2^2 * Delta_J`.

Then the characteristic function of the full conditioned quadratic polynomial satisfies, for every nonzero `t`,

`|phi_Q(t)|^2 <= 2^(11/4) pi^(5/2) Xi^(-1/4) |t|^(-5/2)`,          (2.1)

that is,

`|phi_Q(t)|^2 <= 2^(11/4) pi^(5/2)
                  det(G_I)^(-1/2) ||v||^(-1/2) Delta_J^(-1/4)
                  |t|^(-5/2)`.

Fourier inversion gives a continuous density vanishing at infinity and

`boxed( ||p_Q||_infinity <= 5 * 2^(11/10) * Xi^(-1/10) )`.          (2.2)

Numerically the universal prefactor is

`5*2^(11/10)=10.717734625362931...`.

Consequently, for every interval `B`,

`P(Q in B) <= 10.718 Xi^(-1/10) |B|`.                               (2.3)

This is a genuine linear small-ball estimate in the stated physical-screen branch.

## 3. Exact independent-copy identity and preservation of sum/difference dependence

Use the proved hub ambiguity identity from

`yspennstate/math-open-problems@f68817886312b904e2cf86ccbfb14f4f130229f3:proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/hub_decoupling/REPORT.md`, Proposition 4.1.

Duplicate the hub and the `J_0:=J_V union J_L` block and keep `I` shared. For the hub copies write

`X_h = mu + sigma/2`, `X_h' = mu - sigma/2`.

For each original coordinate pair in `J_0`, write the difference `W=X-X'`. The coordinates of `W` are independent, each with density

`g_j=f_j * tilde(f_j) <= 1` and total mass one.

Define

`F_sigma(mu)=f_h(mu+sigma/2)f_h(mu-sigma/2)`,

and its Fourier transform in `mu`, `Fhat_sigma(s)`. Then the exact source identity implies

`|phi_Q(t)|^2
 <= int_R d sigma E_W [
      |Psi_I(2t( sigma w_I + M_V W_V + M_L W_L ))|
      |Fhat_sigma(2t( <w_{J_V},W_V> + <w_{J_L},W_L> + a sigma ))|
    ]`.                                                            (3.1)

Crucially,

`int_R |Fhat_sigma(s)|^2 ds <= 2 pi g_h(sigma)`,                    (3.2)

where `g_h(sigma)<=1` and `int g_h=1`.

Equation (3.1) is an independent-copy identity in the **original coordinates**. No statement that `X_j-X_j'` is independent of `X_j+X_j'` is made or used. The dependence is exactly what the ambiguity function `Fhat_sigma` retains.

## 4. The rank-one screen estimate

Because `M_L=u v^T`, put

`Z=<v,W_L>`, `Y=<w_{J_L},W_L>`.

The random vector `(Z,Y)` is a two-dimensional projection of a product law whose coordinate densities are at most one. The Ball/Livshyts--Paouris--Pivovarov projection bound, in the normalization already used in the source report, gives its density `p(z,y)` the cap

`||p||_infinity <= 2 Delta_J^(-1/2)`.                               (4.1)

The scalar marginal `Z` satisfies

`||p_Z||_infinity <= sqrt(2) ||v||^(-1)`.                           (4.2)

Fix `sigma` and `W_V`; abbreviate all terms depending only on them by `C`. For fixed `z`, Cauchy--Schwarz in the **actual joint density** `p(z,y)` gives

`int p(z,y) |Fhat_sigma(2t(y+C))| dy
 <= p_Z(z)^(1/2)
    [ int p(z,y)|Fhat_sigma(2t(y+C))|^2 dy ]^(1/2)`.

Using (4.1), the change of variable `s=2t(y+C)`, and (3.2),

`int p(z,y)|Fhat_sigma(2t(y+C))|^2 dy
 <= [2 Delta_J^(-1/2)] [1/(2|t|)] [2 pi g_h(sigma)]
 = 2 pi |t|^(-1) Delta_J^(-1/2) g_h(sigma)`.

Together with (4.2) and `g_h<=1`,

`int p(z,y)|Fhat_sigma(2t(y+C))| dy
 <= 2^(1/4)(2pi)^(1/2)
    |t|^(-1/2)||v||^(-1/2)Delta_J^(-1/4)`.                         (4.3)

This is the new point: the hub ambiguity function is paid in `L^2`, while the physical screen contributes a genuine two-dimensional projection density. We never normalize a conditional `Y|Z` law, so the known exploding conditional-cap obstruction is avoided.

## 5. Translated two-row Brascamp--Lieb integral

After (4.3), (3.1) reduces to the integral

`int d sigma int dz E_{W_V}
 |Psi_I(2t( sigma w_I + z u + M_V W_V ))|`.

For each fixed `W_V`, the term `M_VW_V` is merely a coordinatewise translation in the arguments of the characteristic functions. Let `P=[w_I,u]`. Since every row leverage of `P` is at most `1/2`, the translated two-dimensional Brascamp--Lieb estimate from the same source report gives

`int_R2 |Psi_I(P xi + beta)| d xi <= (4pi)^2 det(G_I)^(-1/2)`       (5.1)

uniformly in every translation `beta`.

Substituting `xi=2t(sigma,z)` therefore yields

`int d sigma dz E_{W_V}
 |Psi_I(2t( sigma w_I + z u + M_V W_V ))|
 <= (2|t|)^(-2)(4pi)^2 det(G_I)^(-1/2)`.                           (5.2)

Multiplying (4.3) and (5.2) proves (2.1).

Notice that the dense cross block `M_V` was never assumed small, low rank, or perturbative; it survives as a harmless translation **only after** the two screen variables `(sigma,z)` have been retained and integrated jointly.

## 6. Inversion and constants

Let

`B = 2^(11/8) pi^(5/4)
     det(G_I)^(-1/4)||v||^(-1/4)Delta_J^(-1/8)`.

Then

`|phi_Q(t)| <= min(1,B|t|^(-5/4))`.

For `b=5/4`,

`int_R min(1,B|t|^(-b)) dt = [2b/(b-1)] B^(1/b)=10 B^(4/5)`.

Hence

`||p_Q||_infinity <= (1/(2pi))*10 B^(4/5)
 = 5*2^(11/10)
   det(G_I)^(-1/5)||v||^(-1/5)Delta_J^(-1/10)
 = 5*2^(11/10) Xi^(-1/10)`.

Because `phi_Q in L^1`, Fourier inversion gives a **continuous** density in this branch, not merely an essentially bounded representative.

The certificate is invariant under the arbitrary rank-one factorization rescaling `u->c u`, `v->v/c`: `det G_I` gains `c^2`, `||v||^2` loses `c^2`, and `Delta_J` loses `c^2`, so `Xi=(det G_I)^2||v||^2Delta_J` is unchanged.

## 7. New L2 collision estimate and designated-partner application

Equation (2.1) also yields a sharper collision certificate. With

`C2=2^(11/4)pi^(5/2)
    det(G_I)^(-1/2)||v||^(-1/2)Delta_J^(-1/4)`,

we have `|phi|^2<=min(1,C2|t|^(-5/2))`, and therefore

`int_R |phi(t)|^2 dt <= (10/3) C2^(2/5)`.

Plancherel gives

`||p_Q||_2^2
 <= (5/3) 2^(11/10) Xi^(-1/10)
 = 3.5725782084543107... Xi^(-1/10)`.                              (7.1)

Now apply the valid collision lemma in the designated partner fleet04/B03 report

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`,

namely

`P(|Y-Y'|<=epsilon) <= 2 epsilon ||p_Y||_2^2`.

The partner report's separate weighted-L2 compiler is known to have a homogeneity/time-weight error and is **not** used. Applying the valid lemma to (7.1) gives the actual new inequality

`boxed(
 P(|Q-Q'|<=epsilon)
 <= (10/3) 2^(11/10) Xi^(-1/10) epsilon
 )`                                                                    (7.2)

with prefactor

`(10/3)2^(11/10)=7.1451564169086215...`.

Thus the same dependence-safe construction supplies both a one-copy continuous-density bound and linear independent-copy collision scaling.

## 8. Application to the strict-N3 mixed-hub witness

The fresh fleet02/B19 report gives the exact target-class family

`A_m = [[0,g^T],[g,u u^T]]`,

where on `m` leaves

`g=m^(-1/2)(1,...,1)`,

`u=m^(-1/2)(1,...,1,-1,...,-1)`,

with equal numbers of signs. The nonzero spectrum is exactly `{1,-1,1}`; every physical cross block has rank at most two, so all `e_3` and `e_5` cross-volume exits vanish. It is therefore a useful strict-N3/hub control, not a counterexample.

Take `m` divisible by four, `m>=8`, and split the leaves into two banks `I,J_L`, each containing equal numbers of the plus and minus signs. Set `J_V=empty`. Then

`A[I,J_L]=u_I u_{J_L}^T`,

so in the theorem choose the rank-one factors `u_screen=u_I`, `v=u_{J_L}`. The hub row is `w=g`. Exact orthogonality gives

`G_I = (1/2) I_2`,       `det G_I=1/4`,

`||v||^2=1/2`,

`Gram(v,w_{J_L})=(1/2)I_2`,       `Delta_J=1/4`.

Every row leverage on `I` is `4/m<=1/2`. Therefore

`Xi=(1/4)^2*(1/2)*(1/4)=1/128`,

and the new theorem yields the uniform continuous-density bound

`boxed( ||p_{X^T A_m X}||_infinity
        <= 5*2^(9/5)
        = 17.411011265922482... )`.                                (8.1)

The designated-partner collision lemma plus (7.1) gives simultaneously

`P(|Q-Q'|<=epsilon)
 <= (10/3)2^(9/5) epsilon
 = 11.607340843948322... epsilon`.                                  (8.2)

This is weaker numerically than the newest mixed-hub theorem already known for this family, but it is a genuinely different **decoupled-time / ambiguity-function** payment and demonstrates that the B03 mechanism survives the exact strict-N3 witness where all rank-three/five cross-volume certificates vanish.

## 9. Scope and first unpaid implication

This theorem does **not** prove that every N3 survivor admits such a rank-one screen partition. The fresh singleton-heavy-hub/two-bank report identifies an aggregate bordered packet

`sum_{j in B2,k in B3}|det A[{h,j,k}]| >= 2^(-27)`

in the remaining exact-rank-three hub state, but that packet does not force one uniformly good local triple and does not force `A[B2,B3]` to have rank one. The live corrections forbid those shortcuts.

The new result pays the following previously uncovered chamber:

- one genuine original-coordinate hub;
- an arbitrary dense twist through a bank `J_V`;
- a second screen bank `J_L` whose cross matrix into the shared bank has rank one;
- two transverse physical projection pairs with quantitative Gram determinants.

The first B03 implication still unpaid is to replace the exact rank-one screen `A[I,J_L]=uv^T` by an **aggregate low-cross-rank screen** (or a sum of a rank-one screen and a residual controlled before reciprocal localization), while retaining the ambiguity function rather than conditioning on a sum/difference coordinate. This is directly aligned with the current low-cross-rank dense-twist/hub remainder.

Full QFORM status: **OPEN**. No counterexample is produced. Continuity is **PROVED only in the theorem's stated branch**, and remains OPEN for the unrestricted target.

## 10. Source/correction discipline

Used mathematical sources:

1. `yspennstate/math-open-problems@f68817886312b904e2cf86ccbfb14f4f130229f3`, `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/hub_decoupling/REPORT.md`: exact hub ambiguity identity, ambiguity L2 estimate, translated projection/BL tools.
2. `yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`, fleet04/B03 collision report: only `P(|Y-Y'|<=epsilon)<=2epsilon||p_Y||_2^2` is used.
3. `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, fleet02/B19 r22: strict-N3 mixed-hub witness and current low-cross-rank hub context.

Respected corrections include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`, `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`, `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`, and `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`.

No pointwise law-uniform van der Corput estimate, post-rotation independence, conditional sum/difference cap, moment assumption, support assumption, Gaussian assumption, or perturbative deletion of a small quadratic twist is used.

Execution status: `WITHOUT_VERIFIED_BRAIN`.
