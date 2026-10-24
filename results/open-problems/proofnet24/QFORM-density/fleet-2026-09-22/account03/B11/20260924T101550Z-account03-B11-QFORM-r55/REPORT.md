SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T10:15:50Z.
attacking: the general physical indefinite-pair L^3 endpoint, then spend a third original-coordinate square before taking L^infinity.

# account03/B11 r55 — every physical indefinite binary form has a uniform L^3 density

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: indefinite signatures / quantitative inequalities and rigorous computations  
Status: `NEW SUPPORTING THEOREM + NEW AMBIENT INDEFINITE BRANCH + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

Fresh owner control at publication remains revision `2026-09-22.15`: QFORM is the sole research target, no account or slot is paused, and the unrestricted theorem and full-target continuity remain open. The live corrections against law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, independence after rotation, conditional-density caps, and worst-fiber supremum arguments are retained. No Gaussian, moment, log-concavity, compact-support, connected-support, or diagonal-basis hypothesis is used below.

The first essential implication attacked here is the one named independently by account01/B05 and the designated account04/B11 worker:

`QFORM-INDEFINITE-PAIR-L3-v1`.

It is proved below for every physical indefinite pair, with an explicit constant 22.

## 1. Main theorem

### Theorem 1 — `QFORM-INDEFINITE-PAIR-L3-v1`

Let `X,Y` be independent real random variables with probability densities satisfying

`0<=f_X<=m_X`, `0<=f_Y<=m_Y`.

Let

`q(X,Y)=aX^2+2tXY+bY^2+alpha X+beta Y+gamma`,

and assume

`B=[[a,t],[t,b]]`

is invertible indefinite. Put

`D=|det B|=t^2-ab>0`.

Then `q(X,Y)` has a density in `L^3(R)` and

`boxed: ||p_q||_3 <=22 D^(-1/3) (m_X m_Y)^(2/3).`             (1.1)

For the target cap-one inputs this is simply

`boxed: ||p_q||_3 <=22 |det B|^(-1/3).`                         (1.2)

The logarithmic point singularity of an opposite-sign rank-two saddle is therefore uniformly compatible with a finite `L^3` norm for every physical orientation, including both nonzero diagonal coefficients.

### 1.1 Affine reduction and normalization

Because `B` is invertible, completing the square by the constant translation

`(x,y) -> (x,y)+(1/2)B^{-1}(alpha,beta)^T`

removes all affine terms up to an additive constant. The two translations are coordinatewise constants, so independence and density caps are unchanged.

First take `m_X=m_Y=1`. Scaling `B` by `D^(-1/2)` reduces to

`t^2-ab=1`.                                                     (1.3)

If the normalized quadratic has density `p`, restoring the coefficient scale `sqrt(D)` multiplies its `L^3` norm by `D^(-1/3)`. Thus it remains to prove a universal constant in the normalization (1.3).

General density caps follow by the source-coordinate dilations `U=m_X X`, `V=m_Y Y`; their densities are cap one and the transformed determinant is `D/(m_X^2m_Y^2)`, giving (1.1).

## 2. Off-diagonal-dominated chamber

Assume

`|ab| <= t^2/4`.                                                  (2.1)

From (1.3): if `ab>=0`, then `ab<=1/3`; if `ab<0`, then `|ab|<=1/5`. Hence

`|t| >= 2/sqrt(5)`.                                               (2.2)

Split the literal source plane into

`R1={|by|<=|tx|/2}`, `R2=R1^c`.                                  (2.3)

For fixed `x`, on `R1`

`|partial_y q|=2|tx+by| >= |tx|`,                                (2.4)

and `y -> q(x,y)` is monotone on the interval `R1(x)`. Let `k_x` be the pushforward of `f_Y(y)1_R1(x)`. The one-dimensional change of variables gives

`||k_x||_3^3
 = int_R1(x) f_Y(y)^3 / |partial_y q|^2 dy
 <= |tx|^(-2) int f_Y^3
 <= |tx|^(-2).`                                                   (2.5)

Minkowski therefore yields

`||p_1||_3
 <= |t|^(-2/3) int f_X(x)|x|^(-2/3) dx`.                       (2.6)

Among all probability densities bounded by one, the last integral is maximized by filling the unit interval centered at zero. Thus

`int f_X(x)|x|^(-2/3)dx
 <= int_(-1/2)^(1/2)|x|^(-2/3)dx
 =6*2^(-1/3).`                                                    (2.7)

On `R2`,

`|x| < 2|b||y|/|t|`,

hence by (2.1)

`|ax| < 2|ab||y|/|t| <= |ty|/2`.                                 (2.8)

Therefore

`|partial_x q|=2|ax+ty| >= |ty|`,                                (2.9)

with constant sign on `R2(y)`, and the symmetric calculation gives the same estimate for `p_2`. Consequently

`||p_q||_3
 <=12*2^(-1/3)|t|^(-2/3)
 <=12*(5/8)^(1/3)
 =10.259855680060182... .`                                        (2.10)

This chamber already beats the final constant 22 by more than a factor two.

## 3. Diagonal-dominated chamber

Now assume

`|ab| > t^2/4`.                                                   (3.1)

Again using (1.3), either `ab>1/3` or `ab<-1/5`, so

`max(|a|,|b|)>1/sqrt(5)`.                                         (3.2)

Swap the two physical source coordinates if necessary and assume

`|b|>1/sqrt(5)`.                                                   (3.3)

For fixed `x`, the discriminant in `y` of

`b y^2+2txy+a x^2-z=0`

is exactly

`4[(t^2-ab)x^2+bz]=4(x^2+bz)`.                                   (3.4)

At a regular root,

`|tx+by|=sqrt(x^2+bz)`.                                           (3.5)

There are at most two roots and `f_Y<=1`, so the conditional output density is bounded by `(x^2+bz)^(-1/2)` on the positive-discriminant region. Therefore

`p_q(z) <= F(bz)`,                                                (3.6)

where

`F(u)=int f_X(x)|x^2+u|^(-1/2) dx`.                              (3.7)

Let `h` be the density of `X^2`. Then

`h(y)=[f_X(sqrt(y))+f_X(-sqrt(y))]/(2sqrt(y))`, `y>0`,             (3.8)

so

`0<=h(y)<=y^(-1/2)`, `int h=1`,                                  (3.9)

and, with `s=-u`,

`F(u)=int_0^infinity h(y)|s-y|^(-1/2)dy=:I_(1/2)h(s)`.             (3.10)

### 3.1 A self-contained fractional/maximal bound

Let `Mh(s)` be the centered Hardy-Littlewood maximal function. For `R>0`, put

`H_s(r)=int_{|s-y|<=r}h(y)dy <=2r Mh(s)`.                         (3.11)

Stieltjes integration gives

`int_{|s-y|<=R}|s-y|^(-1/2)h(y)dy
 <=4 R^(1/2) Mh(s)`.                                              (3.12)

The complementary integral is at most `R^(-1/2)` because `h` has mass one. Optimizing at `R=1/(4Mh(s))` yields the pointwise Hedberg inequality

`I_(1/2)h(s) <=4 sqrt(Mh(s)).`                                    (3.13)

For completeness, the one-dimensional centered maximal operator has weak `(1,1)` constant 3 by the interval Vitali lemma. Apply that weak estimate to `h 1_{h>lambda/2}`; since the remaining part has maximal function at most `lambda/2`,

`|{Mh>lambda}| <= (6/lambda) int_{h>lambda/2}h`.                  (3.14)

Layer cake at `p=3/2` gives

`int (Mh)^(3/2)
 <=9*2^(3/2) int h^(3/2)
 <26 int h^(3/2).`                                                (3.15)

Finally, by (3.9),

`int h^(3/2)
 <=int h(y)y^(-1/4)dy
 =E|X|^(-1/2)
 <=int_(-1/2)^(1/2)|x|^(-1/2)dx
 =2sqrt(2).`                                                       (3.16)

Combining (3.13)-(3.16),

`||F||_3^3 <=64*26*2sqrt(2)`.                                     (3.17)

Since `p_q(z)<=F(bz)`, (3.3) gives

`||p_q||_3
 <=|b|^(-1/3)||F||_3
 <(64*26*2sqrt(2))^(1/3) 5^(1/6)
 =21.91430856947024... <22.`                                      (3.18)

Equations (2.10) and (3.18) prove Theorem 1.

## 4. The mandatory opposite-sign rank-two control

Take independent `X,Y ~ Uniform[-1/2,1/2]` and

`R=2XY`.

Then for `0<|r|<1/2`,

`p_R(r)=log(1/(2|r|))`,                                           (4.1)

so the density is genuinely unbounded at zero. But

`||p_R||_3^3
 =int_(-1/2)^(1/2) log^3(1/(2|r|))dr
 =int_0^1 (-log u)^3du
 =6`.                                                              (4.2)

Thus `||p_R||_3=6^(1/3)`: the logarithmic rank-two obstruction is exactly the kind of singularity that survives in `L^3`. Theorem 1 shows this is not an accident of the canonical hyperbola; `L^3` is uniformly controlled for every physical indefinite orientation.

## 5. Third source-disjoint square: full-line bounded density

The completed account01/B05 theorem `QFORM-SHIFTED-SQUARE-L32-v1`, source

`yspennstate/math-open-problems@4fea394eafc8bce4f335cce2a6150ed50f95ed1a`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260924T100503Z-account01-B05-QFORM-auto11/REPORT.md`

proves, for a cap-one scalar `W`,

`||p_{lambda(W-s)^2}||_(3/2)<=2|lambda|^(-1/3)`.                  (5.1)

Hence if three literal original coordinates `(H,L,W)` have principal block

`B3=[[a,t,0],[t,b,0],[0,0,lambda]]`,                              (5.2)

with `t^2-ab>0` and `lambda!=0`, then conditioning on all other original coordinates leaves `H,L,W` mutually independent and converts every outside coupling only into affine terms. Theorem 1, (5.1), and Young's conjugate-exponent inequality give uniformly in the conditioning variables

`boxed:
 ||p_(X^T A X)||_infinity
 <=44 [(t^2-ab)|lambda|]^(-1/3)
 =44 |det B3|^(-1/3).`                                            (5.3)

The convolution is in `C_0(R)` because it is an `L^3 * L^(3/2)` convolution. Uniform domination in the outside variables then gives a continuous `C_0` density after averaging the conditioning. If `sigma=s_3(B3)>0`,

`boxed: ||p_(X^T A X)||_infinity <=44/sigma.`                     (5.4)

Changing the sign of `lambda` realizes both signatures `(2,1)` and `(1,2)`. This is a genuine ambient theorem: all outside coefficients, outside couplings, and additional spectrum are arbitrary.

The mechanism is now explicit and product-valid: the two-dimensional indefinite saddle may retain its logarithmic point blow-up but has a uniform `L^3` density; an independent physical third square has exactly the conjugate `L^(3/2)` regularity; their convolution is bounded and continuous. No rotation of the source coordinates occurs.

## 6. A coupled physical 3x3 corollary with a nonzero majority-sign pivot

The same binary theorem also advances the genuinely coupled physical triple.

Write a literal physical `3x3` principal block as

`C3=[[C,r],[r^T,lambda]]`, `lambda!=0`,                            (6.1)

where `C` is `2x2`. Complete the square only in the third original coordinate. The residual physical pair matrix is the Schur complement

`S=C-r r^T/lambda`,                                               (6.2)

and

`det C3=lambda det S`.                                            (6.3)

If `S` is indefinite, Theorem 1 gives the residual pair density

`||p_R||_3 <=22 |det S|^(-1/3)`.                                  (6.4)

The completed dependent `L^3` square-smoothing lemma in account03/B06 r52 states that if a base density has `L^3` norm `M` and the conditionally translated scalar has density cap one, adding `lambda V^2` costs at most

`4 |lambda|^(-1/2) M^(3/4)`                                      (6.5)

without requiring independence after the translation. This premise is valid here: the literal third original coordinate is independent of the first two, and conditioning on any residual pair value only mixes translations of its cap-one density. Therefore

`boxed:
 ||p_(X^T A X)||_infinity
 <=4*22^(3/4)|lambda|^(-1/4)|det C3|^(-1/4).`                     (6.6)

Numerically

`4*22^(3/4)=40.63282352308103... .`                               (6.7)

For a physical triple of signature `(2,1)`, a positive pivot `lambda` leaves an indefinite Schur pair; for signature `(1,2)`, a negative pivot does the same. Thus (6.6) pays every nonzero physical pivot having the majority inertia sign. If additionally `s_3(C3)>=sigma` and `|lambda|>=c sigma`, then

`boxed: ||p_(X^T A X)||_infinity
 <=40.633 c^(-1/4) sigma^(-1).`                                   (6.8)

This branch establishes essential boundedness only; the dependent-square lemma used in (6.5) does not by itself supply a continuous representative. The unresolved difficulty is the uniform passage as every usable majority-sign physical pivot becomes small or vanishes.

## 7. Designated account04/B11 theorem applied at an actual inequality

The newest completed designated-partner result is account04/B11

`QFORM-RULED-PHYSICAL-TRIPLE-DET6-v1`,

source

`yspennstate/math-open-problems@da4db4dae881f0b5239c93291ee3d7e76216c945`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260924T101034Z-account04-B11-ruled-triple-l3-r3/REPORT.md`.

Its literal ruled block is exactly the `b=0` boundary of (5.2):

`[[a,t,0],[t,0,0],[0,0,lambda]]`.                                 (7.1)

At this actual inequality it proves the sharper full ambient bound

`boxed:
 ||p_(X^T A X)||_infinity
 <=6 (|t|^2|lambda|)^(-1/3)
 =6 |det B3|^(-1/3),`                                             (7.2)

with a continuous `C_0` density, uniformly in the other diagonal `a` and across both signs of `lambda`. In particular, for

`B3=[[a,1,0],[1,0,0],[0,0,+/-1]]`,                                (7.3)

all arbitrary ambient extensions satisfy

`boxed: ||p_(X^T A X)||_infinity<=6.`                             (7.4)

Theorem 1 is therefore not duplicating the designated partner theorem: partner r3 sharply closes the ruled boundary, while the new binary theorem fills the previously missing case in which both physical diagonals of the indefinite pair are nonzero. The two results meet continuously in parameter space at `b=0`.

## 8. What this does and does not solve

Proved this run:

1. every physical indefinite binary quadratic, with arbitrary affine terms and arbitrary independent cap-one laws, has a density with `L^3` norm at most `22 |det B|^(-1/3)`;
2. a source-disjoint third physical square upgrades this to a continuous ambient density bounded by `44 |det B3|^(-1/3)`;
3. a general coupled physical `3x3` block is paid whenever it has a nonzero majority-sign physical pivot, with the quantitative bound (6.6);
4. the designated account04/B11 ruled theorem gives the sharper constant 6 on the exact `b=0` boundary;
5. the opposite-sign rank-two logarithm is retained and explicitly identified as an `L^3`-integrable endpoint.

Not proved:

- a uniformly good physical triple or majority-sign pivot follows from the sole global hypothesis that `A` has three eigenvalues of modulus at least one;
- (6.6) is uniform when the majority-sign pivot tends to zero;
- shared-source third curvature can always be converted into the `L^(3/2)` square resource without losing product provenance;
- arbitrary additional nonseparable spectrum is globally reduced to one of the paid local branches;
- the unrestricted conjecture or its full continuity conclusion.

The next B11 implication is therefore

`QFORM-INDEFINITE-PAIR-L3-NULLPIVOT-COMPILER-v1`:

combine the new all-orientation binary `L^3` estimate with the existing puncture/two-Jacobian and Schur-pseudodeterminant currency to remove the `|lambda|^(-1/4)` loss in (6.6) as the majority-sign physical pivot vanishes, while keeping all three original-coordinate source banks and the nonzero third shear. This is the precise remaining local indefinite interface before the broader global extraction problem.

## 9. Verification and source record

The deterministic checker in `VERIFY.py` tested 38,789 random normalized indefinite matrices. It verified the normalization, both chamber gates, the discriminant identity, the Schur determinant identity, and the numerical constants. Its output ends

`QFORM_B11_R55_INDEFINITE_PAIR_L3_CHECK_PASS`.

Recorded constants:

- off-diagonal chamber: `10.259855680060182`;
- diagonal chamber: `21.914308569470240 <22`;
- dependent-square coefficient: `40.632823523081030`;
- maximum numerical normalization error: `3.638e-12`;
- maximum discriminant identity error: `5.821e-11`;
- maximum Schur determinant identity error: `1.218e-11`.

Sources actually used at theorem scope:

- fresh owner control: `yspennstate/math-research-brain`, revision `2026-09-22.15`;
- account01/B05 mixed L3 / shifted-square theorem: `math-open-problems@4fea394eafc8bce4f335cce2a6150ed50f95ed1a`;
- designated account04/B11 ruled-triple theorem: `math-open-problems@da4db4dae881f0b5239c93291ee3d7e76216c945`;
- account03/B06 dependent L3 square smoothing: theorem recorded in its r52 report, source chain pinned there;
- all live corrections in `CORRECTION_INBOX.json` were refreshed before publication.

Full unrestricted QFORM status: `OPEN / NOT PROVED / NOT DISPROVED`.
