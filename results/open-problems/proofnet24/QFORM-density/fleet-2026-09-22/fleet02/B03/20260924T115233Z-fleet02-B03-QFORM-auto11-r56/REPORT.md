SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-24T11:52:33Z.
attacking: the one-square/two-hyperbolic-slope collar — upgrade the newest partner's negative-half slice resource to an L1 Fourier estimate inside the same packet, so linear small-ball scaling no longer needs a source-disjoint positive-half packet.

# fleet02/B03 r56 — square plus two hyperbolic slopes gives direct L1 Fourier closure

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING DENSITY/TIME THEOREM; REQUIRED PINNED THEOREM H APPLIED; NEWEST PARTNER r53 APPLIED; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN; WITHOUT_VERIFIED_BRAIN**.

## 1. First unpaid implication

The previous r55 obstruction showed that a universal negative-half whole-copy budget `A_-` cannot by itself force bounded one-copy density after a two-coordinate product bank has been compressed to an arbitrary dependent density cap. The newest compatible fleet03/B03 r53 improves the analytic side: a same-bank square plus **one** independent hyperbolic scalar has a pivot-stable negative-half time estimate, but still no one-copy height theorem without a complementary resource.

This run identifies the minimal same-packet repair for that route. If the same square-bearing bank carries **two** hyperbolic coordinates coupled to an independent two-dimensional bank through an invertible `2x2` matrix, the r53 slice fourth-moment estimate and two-dimensional bilinear Plancherel combine directly to an `L1_t` characteristic-function estimate. No external source-disjoint positive-half packet is needed.

The remaining full-target implication is structural: in a rough survivor of the existing volume/grouped/pivot exits, expose product-preservingly either

1. a square-plus-two-hyperbolic-slope packet with determinant currency `J=|a||det B|^2` bounded below and a controlled genuine joint density cap inherited from original product coordinates, or
2. an already-paid projected-volume/Fresnel/grouped-hub/finite-carrier receiver.

The bare three-large-eigenvalue hypothesis does not itself supply this five-direction packet, so this is a supporting branch, not a full proof.

## 2. Main theorem

### `QFORM-SQUARE-DOUBLE-HYPERBOLIC-L1-v1`

Let `(S,R)` with `R in R^2` have an arbitrary joint probability density `g` satisfying

`||g||_infinity <= M`.

Let `V in R^2` be independent of `(S,R)` with an arbitrary joint probability density `h` satisfying

`||h||_infinity <= N`.

Let `a!=0`, let `B` be an invertible real `2x2` matrix, and let `G:R^2->R`, `H:R^2->R`, `K:R^2->R` be arbitrary measurable real functions for which

`Q = a(S+G(R))^2 + 2 R^T B V + H(R)+K(V)`                         (2.1)

is well-defined. Put

`J := |a| |det B|^2`.                                               (2.2)

Then `phi_Q in L1(R)` and `Q` has a continuous `C_0` density satisfying

`||p_Q||_infinity <= (15/4) 3^(1/5) (MN)^(2/5) J^(-1/5).`          (2.3)

Equivalently, every interval `I` satisfies

`P(Q in I) <= (15/4) 3^(1/5) (MN)^(2/5) J^(-1/5) |I|.`            (2.4)

The same packet obeys the dependence-safe whole-copy weighted-time estimate

`A_-(Q):=int_R |t|^(-1/2)|phi_Q(t)|^2 dt`
` <= 5*2^(-1/5)*3^(3/10)*sqrt(pi) (MN)^(1/5) J^(-1/10),`          (2.5)

and hence, for an independent copy `Q'` of the **entire scalar output**,

`E|Q-Q'|^(-1/2)`
` <= (5/2) 6^(3/10) (MN)^(1/5) J^(-1/10).`                       (2.6)

No marginal density cap for either component of `R` is assumed. No independence between `S` and `R` is assumed. No moment, support, log-concavity, or smoothness hypothesis is used. The arbitrary phases `H(R)` and `K(V)` are retained exactly.

## 3. Slice fourth moment: the r53 resource is dimension-free in the environment

The shear `(s,r)->(s+G(r),r)` has Jacobian one, so it preserves the joint density cap `M`. Hence take `G=0`.

For almost every `r in R^2`, define

`m(r)=int_R g(s,r) ds`,
`A_r(t)=int_R g(s,r) exp(i a t s^2) ds`,
`F(t)=int_(R^2) |A_r(t)|^2 dr`.                                  (3.1)

The proof of fleet03/B03 r53 Section 2 depends on `r` only as a parameter. Its one-dimensional square pushforward and centered-interval bathtub bound therefore give verbatim

`||A_r||_4^2 <= C0 M m(r) |a|^(-1/2),`
`C0=(3/2)sqrt(6 pi).`                                             (3.2)

Minkowski and `int m(r)dr=1` yield

`||F||_2 <= C0 M |a|^(-1/2).`                                    (3.3)

This is the key inherited partner resource. It keeps arbitrary dependence inside `(S,R)` and does not ask for a marginal cap on `R`.

## 4. Two-dimensional bilinear Plancherel

Put

`q_t(r)=A_r(t)e^{itH(r)}` and `w_t(v)=h(v)e^{itK(v)}`.

Then

`phi_Q(t)=int_(R^2) int_(R^2) q_t(r)w_t(v)e^{i2t r^T Bv} dr dv.`  (4.1)

Because `h<=N` and `int h=1`,

`||w_t||_2^2=int h(v)^2dv <= N.`                                 (4.2)

Cauchy-Schwarz in `v`, the change `xi=2tBv`, and two-dimensional Plancherel give, for `t!=0`,

`|phi_Q(t)|^2`
` <= N int |q_t^(hat)(2tBv)|^2 dv`
` =  N (2pi)^2/[|det(2tB)|] int |q_t(r)|^2dr`
` =  pi^2 N |det B|^(-1)|t|^(-2) F(t).`                          (4.3)

The same-bank phase `H` and independent-bank phase `K` disappear only through unit modulus; they are not deleted as small perturbations.

## 5. Direct `L1_t` optimization

For `T>0`, use `|phi_Q|<=1` on `|t|<=T`. On the complement, (4.3) gives

`|phi_Q(t)| <= pi N^(1/2)|det B|^(-1/2)|t|^(-1)F(t)^(1/2).`      (5.1)

Hölder with exponents `4/3` and `4`, together with (3.3), yields

`int_(|t|>T)|t|^(-1)F(t)^(1/2)dt`
` <= [int_(|t|>T)|t|^(-4/3)dt]^(3/4) [int F(t)^2dt]^(1/4)`
` <= 6^(3/4) T^(-1/4) C0^(1/2) M^(1/2)|a|^(-1/4).`              (5.2)

Therefore

`int_R |phi_Q(t)|dt <= 2T + D T^(-1/4),`                         (5.3)

where

`D=pi*6^(3/4)*C0^(1/2)(MN)^(1/2)|a|^(-1/4)|det B|^(-1/2).`      (5.4)

The minimum occurs at `T^(5/4)=D/8`, and then the right side is `10(D/8)^(4/5)`. Fourier inversion gives

`||p_Q||_infinity <= (5/pi)(D/8)^(4/5)`
` = (15/4)3^(1/5)(MN)^(2/5)|a|^(-1/5)|det B|^(-2/5),`           (5.5)

which is (2.3). Since `phi_Q in L1`, the density is continuous and vanishes at infinity.

The exponent has the exact five-dimensional determinant homogeneity: the core coefficient matrix in `(S,R_1,R_2,V_1,V_2)` has determinant magnitude `J=|a||det B|^2`, and (5.5) is `J^(-1/5)`.

## 6. Direct assigned negative-half time estimate

From (4.3),

`A_-(Q)`
` <= 4sqrt(T) + pi^2 N|det B|^(-1) int_(|t|>T)|t|^(-5/2)F(t)dt.` (6.1)

Cauchy-Schwarz and (3.3) give

`int_(|t|>T)|t|^(-5/2)F(t)dt`
` <= [int_(|t|>T)|t|^(-5)dt]^(1/2)||F||_2`
` <= (1/sqrt(2)) T^(-2) C0 M|a|^(-1/2).`                        (6.2)

Thus `A_-(Q)<=4sqrt(T)+E T^(-2)` with

`E=(pi^2/sqrt(2))C0 MN |a|^(-1/2)|det B|^(-1).`                (6.3)

At the optimum `T^(5/2)=E`, the value is `5E^(1/5)`, which simplifies to (2.5). Using only the whole-output identity

`|phi_Q(t)|^2=E exp(it(Q-Q'))`                                  (6.4)

and the positive regularized Riesz identity

`int_R |t|^(-1/2)e^{itx}dt=sqrt(2pi)|x|^(-1/2)`                 (6.5)

gives (2.6). No coordinatewise sum/difference pair is separated or asserted independent.

## 7. Strict original-product target application

Take five genuine independent cap-one original coordinates `X_1,...,X_5` and set

`Q_5 = X_1^2 + 4X_2X_4 + 4X_3X_5.`                             (7.1)

Use `S=X_1`, `R=(X_2,X_3)`, `V=(X_4,X_5)`, `a=1`, `B=2I_2`. Then `M=N=1`, `det B=4`, and `J=16`. The coefficient matrix has spectrum

`{1,2,-2,2,-2}`.                                                 (7.2)

Hence this is strictly inside the owner target, with all five nonzero eigenvalues already of modulus at least one. The new theorem gives

`||p_(Q_5)||_infinity`
` <= (15/4)3^(1/5)16^(-1/5)`
` = 2.683067027072354... ,`                                     (7.3)

so

`P(Q_5 in I) <= 2.683067027072354... |I|.`                       (7.4)

The direct assigned time estimate is

`int |t|^(-1/2)|phi_(Q_5)(t)|^2dt <= 8.129490346791867... ,`    (7.5)

and

`E|Q_5-Q_5'|^(-1/2) <= 3.243197417450581... .`                  (7.6)

The density is continuous `C_0` for this family.

## 8. Newest partner fleet03/B03 r53 applied at an equation

The latest compatible partner report is fleet03/B03 r53, `QFORM-SQUARE-HYPERBOLIC-WEIGHTED-COLLISION-v1`, with its spectral wording correction in `SUPPLEMENT.md`; all theorem constants are unchanged.

Apply r53 to the strict target-valid three-variable subpacket

`Q_3 = X_1^2 + 4X_2X_4.`                                       (8.1)

Here `(S,R)=(X_1,X_2)` has joint cap `M=1`, `V=X_4` has cap `N=1`, `a=1`, `b=2`, and the coefficient spectrum is `{1,2,-2}`. Partner r53 gives the actual weighted collision inequality

`int |t|^(-1/2)|phi_(Q_3)(t)|^2dt`
` <= 3sqrt(6pi)2^(-1/3)`
` = 10.337808534221727... ,`                                   (8.2)

and

`E|Q_3-Q_3'|^(-1/2) <= 3sqrt(3)2^(-1/3)`
` = 4.124188910995808... .`                                    (8.3)

The present theorem explains exactly what the second independent hyperbolic slope buys: the two-dimensional bilinear Jacobian changes the squared-Fourier tail from `|t|^-1 F(t)` to `|t|^-2 F(t)`, and the inherited `F in L2` resource then makes `phi in L1`.

## 9. Required pinned `e5f71d79...` Theorem H applied on a diffuse version

To apply a completed result from the required pinned package at an actual inequality, take eight independent cap-one original coordinates and define

`S=(X_1+X_2)/sqrt(2)`,
`R_1=(X_3+X_4)/sqrt(2)`,
`R_2=(X_5+X_6)/sqrt(2)`,
`V_1=X_7`, `V_2=X_8`,

`Q_diff=S^2+4R_1V_1+4R_2V_2.`                                  (9.1)

This again has nonzero spectrum `{1,2,-2,2,-2}`. For pinned Theorem H choose hub set `H={7,8}` and light set `I={1,...,6}`. The light quadratic block is exactly the rank-one square `S^2`. The augmented frame rows are

`(1/sqrt(2),0,0)` twice,
`(0,sqrt(2),0)` twice,
`(0,0,sqrt(2))` twice.                                          (9.2)

Thus

`G_tilde=diag(1,4,4)`, `det G_tilde=16`,                        (9.3)

and every normalized leverage is exactly `1/2`, so the pinned theorem's gate is met. Theorem H therefore yields the explicit envelope

`|phi_(Q_diff)(t)| <= min{1, 2 pi^(5/2)|t|^(-5/2)}.`            (9.4)

Integrating it gives the genuine target inequality

`||p_(Q_diff)||_infinity <= (5/3)2^(2/5)`
` = 2.199179851288157... .`                                    (9.5)

The same envelope gives

`int |t|^(-1/2)|phi_(Q_diff)(t)|^2dt`
` <= (40/9)2^(1/5)sqrt(pi)`
` = 9.04895476819256... ,`                                     (9.6)

hence

`E|Q_diff-Q_diff'|^(-1/2) <= (40/9)2^(-3/10)`
` = 3.610010650472158... .`                                    (9.7)

This is an equation-level use of the required pinned completed result. It also shows the relationship between the two receivers: pinned Theorem H is stronger when a diffuse augmented-frame leverage gate is available, while the new theorem needs no leverage control at all and tolerates arbitrary phases `H(R),K(V)` once the genuine group density caps `M,N` are available.

For comparison, each normalized sum in (9.1) has density cap at most `sqrt(2)`, and the three sums use disjoint original coordinate pairs, so the new theorem itself gives `M<=2sqrt(2)`, `N<=1` and

`||p_(Q_diff)||_infinity <= (15/4)(3/2)^(1/5)=4.066769141991371...` (9.8)

without using the leverage geometry.

## 10. Why this does not close the full theorem

The analytic threshold is sharp for this particular slice mechanism. With only one hyperbolic scalar, r53 gives a negative-half collision estimate but no `L1_t` bound, and r55 exhibited an explicit dependent-cap compression where a uniform `A_-` coexists with arbitrarily large one-copy density. The second slope changes the Fourier Jacobian enough to cross the `L1` threshold.

The owner hypothesis supplies only three large eigenvalues, not automatically one square plus two quantitatively nondegenerate independent hyperbolic slopes. A full proof must still show that every remaining rough matrix either supplies such a packet with `J` bounded below (while preserving original-product provenance) or enters another already-paid aggregate branch. No spectral rotation is used probabilistically here, and no small operator remainder is discarded on unbounded inputs.

The unrestricted conjecture remains **OPEN**. Unrestricted continuity remains **OPEN**; continuity is proved on the branch of this theorem because `phi_Q in L1`.
