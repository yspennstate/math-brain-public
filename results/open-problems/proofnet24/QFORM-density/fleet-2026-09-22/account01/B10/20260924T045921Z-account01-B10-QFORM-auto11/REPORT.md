SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-24T04:59:21Z.
attacking: the fully diffuse near-coloop parabolic-trace survivor; derive a product-origin receiver that keeps the W^2 curvature before taking any fiber supremum, and test the first missing implication directly.

# account01/B10 — an all-finite-Lp endpoint theorem for the exact-null shared-hub survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case  
Run: `20260924T045921Z-account01-B10-QFORM-auto11`  
Status: `NEW_ANALYTIC_THEOREM / UNIFORM_NEAR_LINEAR_SMALL_BALL / PARTNER_RESULT_APPLIED / ENDPOINT_LOG_GAP_ISOLATED / FULL_EXACT_RANK3_OPEN / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and first missing implication

Fresh control was resolved from `yspennstate/math-research-brain` and refreshed before publication; OWNER CONTROL remains revision `2026-09-22.15`, QFORM is the sole research target, and the full conjecture remains OPEN. The live correction inbox was consumed. In particular, nothing below uses independence after spectral rotation, an arbitrary-joint coarea bound, a law-uniform pointwise quadratic-phase decay estimate, a conditional-density-cap-as-independence substitution, a fiber supremum, moments, compact support, connected support, log-concavity, Gaussianity, or deletion of a small coefficient times an unbounded random variable.

The immediate predecessor is

`yspennstate/math-open-problems@bc162d39d582493dbe8c1b8ef21a0fe3f7d203a0`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260924T035456Z-account01-B10-QFORM-auto11/REPORT.md`.

It proved that the raw mixed slice norm

`sup_y int sup_w rho(z,y,w) dz`

can be arbitrarily large even for fixed-dimensional diffuse orthogonal projections of cap-one product laws, and even inside an exact target-valid near-coloop family. Thus the remaining receiver must not take the `w`-supremum before spending curvature.

The newest completed designated partner input actually used is

`yspennstate/math-open-problems@2181d0927de1374b092152c7e6fb51920e5ae40d`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/account02-B10-20260924T004626Z-auto11/REPORT.md`.

Its Theorem 3.1 is the exact regression-clean endpoint receiver. I apply it quantitatively in Section 6.

A standard external input used only in the numerical corollary is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016): a one-dimensional orthogonal projection of a cap-one product density has density cap at most `sqrt(2)`.

## 2. Abstract hyperbolic Lp theorem

The first substantive missing implication was tested before any new structural selection. The endpoint singularity can be controlled much more strongly than the existing square-root small-ball interfaces suggest: the whole output has a dimension-free density in every finite `L^p`, even if the term added to the hyperbolic hub is an arbitrary measurable function of all nonhub variables.

### Theorem 2.1 — `QFORM-INDEPENDENT-HYPERBOLIC-LP-ENDPOINT-v1`

Let `H` be independent of a sigma-field `F`, with probability density `f_H` satisfying

`||f_H||_infinity <= K_H`.

Let `Y` and `S` be arbitrary real `F`-measurable random variables. Assume only that `Y` has a probability density satisfying

`||p_Y||_infinity <= K_Y`.

For `alpha != 0`, put

`Q = alpha H Y + S`.

Then `Q` is absolutely continuous. For every real `p>1`, with

`theta = 1-1/p`,

its density satisfies

`boxed: ||p_Q||_p <= p [ 2 K_H K_Y / |alpha| ]^theta.`                 (2.1)

No condition at all is imposed on the dependence between `S` and `Y`, or on the law, support, moments, or regularity of `S`.

### Proof

Since `Y` has a density, `P(Y=0)=0`. Fix a regular conditional law `mu_y` of `S` given `Y=y`. Because `H` is independent of the entire sigma-field `F`, it remains independent of `(S,Y)`. For almost every `y!=0`, the conditional law of `Q` given `Y=y` is therefore

`law(alpha y H) * mu_y`.

Let

`g_y(x) = |alpha y|^(-1) f_H(x/(alpha y))`.

Young's inequality for convolution with a probability measure gives

`||g_y * mu_y||_p <= ||g_y||_p`.

Interpolation between `L^1` and `L^infinity` gives

`||f_H||_p <= K_H^theta`,

hence

`||g_y||_p <= |alpha y|^(-theta) K_H^theta`.                          (2.2)

Disintegrating over `Y` and applying Minkowski,

`||p_Q||_p`
` <= |alpha|^(-theta) K_H^theta E |Y|^(-theta)`.                       (2.3)

It remains to use only the cap on `Y`. For every probability density bounded by `K_Y`, the decreasing rearrangement of `|y|^(-theta)` gives

`E |Y|^(-theta) <= (2 K_Y)^theta/(1-theta)`
`                    = p (2K_Y)^theta`.                               (2.4)

For completeness, (2.4) also follows directly from layer cake:

`P(|Y|^(-theta)>t) <= min(1,2K_Y t^(-1/theta))`;

integrating in `t` yields exactly `(2K_Y)^theta/(1-theta)`.

Substitution into (2.3) proves (2.1). The same disintegration explicitly constructs an `L^p` density for every `p>1`, proving absolute continuity. QED.

### Why this is useful

The theorem is product-source safe because the only independence used is the genuine ORIGINAL-coordinate independence of the hub `H` from all nonhub coordinates. The added term `S` may contain all same-bank longitudinal leakage, all transverse coupling and all parabolic curvature. In particular, the theorem does not collapse the leaf law to a joint density cap.

## 3. Exact-null rank-three corollary

Use the exact-null physical-hub normal form from the current B10 programme. Let

`A=U M U^T`, `U^T U=I_3`,

with the three nonzero eigenvalues of the symmetric invertible `M` having modulus at least one. Suppose an ORIGINAL row is

`u_0=sqrt(c) r_0`, `||r_0||=1`, `r_0^T M r_0=0`, `c>0`.

Put

`r=||M r_0||`.

Choose the deterministic spectral basis `(r_0,v,w)` with `v=M r_0/r`. Then

`M = [[0,r,0],[r,a,b],[0,b,d]]`,                                     (3.1)

and write the nonhub rows as `(t_i,y_i,w_i)`. Parseval gives

`sum_i y_i^2=1`, `sum_i w_i^2=1`, `sum_i t_i^2=1-c`,
`sum_i t_i y_i=sum_i t_i w_i=sum_i y_i w_i=0`.                       (3.2)

Set

`T=sum_i t_iX_i`, `Y=sum_i y_iX_i`, `W=sum_i w_iX_i`.

Then exactly

`Q = 2r sqrt(c) H Y
     + [2rTY+aY^2+2bYW+dW^2]`.                                       (3.3)

The bracket is an arbitrary measurable function of the nonhub ORIGINAL coordinates for purposes of Theorem 2.1. Therefore, if `K_Y=||p_Y||_infinity`,

`boxed: ||p_Q||_p <= p [ K_Y/(|r|sqrt(c)) ]^(1-1/p), p>1.`            (3.4)

Here the original hub law has `K_H<=1` and `alpha=2r sqrt(c)`, so the factor two cancels exactly.

By the one-dimensional product-marginal theorem, because `sum y_i^2=1`,

`K_Y <= sqrt(2)`.                                                      (3.5)

Also `|r|>=1`: `M r_0` has norm `|r|` and `sigma_min(M)>=1`. Hence in the live near-coloop chamber

`c>63/64`,

we obtain the completely orientation-free finite-p estimate

`boxed: ||p_Q||_p
 <= p (sqrt(128/63))^(1-1/p),  p>1.`                                  (3.6)

Numerically,

`||p_Q||_2 < 2.388`,
`||p_Q||_3 < 3.800`,
`||p_Q||_4 < 5.219`.                                                   (3.7)

These estimates are uniform in dimension, in all same-source overlap between `T,Y,W`, in the fragmentation of every input density, and in the coefficients `a,b,d`. They do not use the `W^2` curvature at all; that curvature is now isolated as the resource needed only for the `p=infinity` endpoint.

This proves absolute continuity and all finite `L^p` bounds in the exact-null near-coloop branch. It does **not** prove a continuous representative.

## 4. A uniform epsilon-log(1/epsilon) small-ball bound

The all-finite-`L^p` theorem has a useful endpoint consequence that is stronger than the previous generic square-root small-ball estimates.

Write

`A_0 = K_H K_Y/(|r|sqrt(c))`.

From (3.4), for any interval `I` of length `epsilon` and every `p>1`, Holder gives

`P(Q in I) <= p (A_0 epsilon)^(1-1/p)`.                               (4.1)

If `A_0 epsilon <= e^(-2)`, choose

`p = log(1/(A_0 epsilon)) >= 2`.

Then `(A_0 epsilon)^(-1/p)=e`, and therefore

`boxed: P(Q in I)
 <= e A_0 epsilon log(1/(A_0 epsilon)).`                              (4.2)

In the live chamber `A_0<=sqrt(128/63)<1.426`, so for every

`epsilon <= e^(-2)/sqrt(128/63) > 0.0949`,

`boxed: P(Q in I)
 < 3.875 epsilon log(1/(1.4254 epsilon)).`                            (4.3)

Thus the remaining exact-null problem is no longer a power-law anti-concentration gap. It is quantitatively a **single logarithm endpoint gap** between (4.2) and the desired `C epsilon`.

There is an equivalent high-density statement. From

`||p_Q||_p^p <= p^p A_0^(p-1)`,

for `lambda>=2eA_0`, choose `p=lambda/(eA_0)` to get

`boxed:
 Leb{x:p_Q(x)>lambda}
 <= A_0^(-1) exp[-lambda/(eA_0)].`                                    (4.4)

So any hypothetical unbounded spike in this branch must occupy exponentially small Lebesgue measure. This is still compatible with an unbounded density and therefore does not solve the endpoint.

## 5. The logarithm is sharp before the parabolic curvature is spent

The `O(p)` growth in Theorem 2.1 cannot be replaced by a uniform `p=infinity` bound under only its hypotheses. Take independent

`H,Y ~ Uniform(0,1)`,

and `S=0`, `alpha=2`. Then

`Q=2HY`

has density

`p_Q(q) = (1/2) log(2/q),  0<q<2`,                                   (5.1)

which diverges at zero. Moreover

`||p_Q||_p^p = 2^(1-p) Gamma(p+1)`,                                  (5.2)

so `||p_Q||_p` grows linearly in `p`. Thus the finite-p theorem has the correct endpoint order for the hyperbolic mechanism alone.

This matters for the QFORM proof map: one cannot get the missing uniform bound by merely optimizing the hub disintegration more carefully. The `dW^2` curvature and original product-linear provenance must remove exactly this logarithm.

## 6. Designated account02/B10 theorem applied at an actual target inequality

The current partner Theorem 3.1 states that for

`Q=2r(sqrt(c)H+T)Y+aY^2+2bYW+dW^2`,

if on an ORIGINAL leaf set `I` one has

`t_i=gamma y_i+eta w_i`

and the transverse Gram `G_I` has determinant `delta>0`, then

`||p_Q||_infinity
 <= 1/(2|r|sqrt(c))
    +16 delta^(-1/2)(|r|sqrt(c))^(-1/2)|d|^(-1/2)`.                  (6.1)

Apply this to the exact target-valid fragmented family from the preceding B10 report. There `r=d=1`, `c=1-epsilon>63/64`, and the leaves consist of three 64-coordinate blocks. On the ORIGINAL reservoir

`I = A-block union C-block`,

the longitudinal coefficient is exactly `t_i=sqrt(epsilon) w_i` on `A` and zero on `C`, so (6.1) applies with

`gamma=0`, `eta=sqrt(epsilon)`,

while

`G_I=diag(1,1/2)`, `delta=1/2`.                                      (6.2)

Therefore the partner theorem gives the actual full target-level inequality

`boxed:
 ||p_Q||_infinity
 <= 1/(2sqrt(c))+16sqrt(2)c^(-1/4)
 < 23.221.`                                                           (6.3)

This is independent of the fragmentation parameter that makes the raw mixed slice norm diverge. Hence the newest partner theorem genuinely uses product provenance that the false mixed-supremum interface destroys.

On the same family, Theorem 2.1 gives simultaneously

`||p_Q||_p <= p (sqrt(2)/sqrt(c))^(1-1/p)`                             (6.4)

for every finite `p`, again independently of fragmentation.

## 7. Application to the partner's diffuse harmonic survivor

The partner's hard exact target family uses, for odd `m>122`,

`t_j=sqrt(2rho/m) cos(2theta_j)`,
`y_j=sqrt(2/m) cos(theta_j)`,
`w_j=sqrt(2/m) sin(theta_j)`,

with `rho<1/64`, `c=1-rho`, and spectral matrix

`[[0,1,0],[1,0,0],[0,0,1]]`.

Every leaf transverse leverage is `2/m<1/61`, but every exact regression-clean reservoir has at most four points and determinant at most `24/m^2`, so the partner's exact-regression `L^infinity` route necessarily deteriorates with `m`.

The new theorem is insensitive to that obstruction. For every `m`, every `rho<1/64`, and arbitrary cap-one source laws,

`boxed:
 ||p_Q||_p <= p (sqrt(2)/sqrt(1-rho))^(1-1/p)
 <= p (sqrt(128/63))^(1-1/p),  p>1.`                                 (7.1)

Thus the harmonic survivor is uniformly controlled in every finite `L^p`; what remains genuinely unpaid is only the endpoint upgrade `p<infinity -> p=infinity`. This is a much thinner analytic target than the previous raw parabolic-trace formulation.

## 8. New first unpaid implication

The first unpaid implication is now

`QFORM-DIFFUSE-PARABOLIC-ENDPOINT-LOG-REMOVAL-v1`:

> In the fully overlapping exact-null near-coloop survivor, use the `dW^2` curvature together with the ORIGINAL product-linear provenance of `(T,Y,W)` to upgrade the universal finite-p estimate
>
> `||p_Q||_p <= p A^(1-1/p)`
>
> to one universal `L^infinity` bound, uniformly as `c -> 1`, without taking a raw `sup_w`, requiring an exact regression-clean reservoir, replacing product provenance by only a joint/conditional density cap, or using moments/support regularity.

The three controls that any proof must survive are now especially explicit:

1. `Q=2HY` shows the logarithm is real if parabolic curvature is not spent;
2. the fragmented fixed-dimensional target family shows a raw mixed-slice supremum can diverge while the true output remains uniformly bounded;
3. the harmonic partner family shows a uniformly good exact regression-clean reservoir need not exist.

A successful next mechanism should therefore be judged by whether it removes the single logarithm in (4.2) while respecting all three controls.

## 9. Scope and status

Proved in this run:

- `QFORM-INDEPENDENT-HYPERBOLIC-LP-ENDPOINT-v1`, including absolute continuity and a complete dimension-free `L^p` estimate for every finite `p`;
- the exact-null rank-three near-coloop corollary (3.6), uniform over arbitrary orientation and arbitrary same-bank contamination;
- the near-linear interval bound (4.2) and exponential high-density-set bound (4.4);
- sharpness of the `O(p)` endpoint order before third curvature is used;
- a quantitative application of the newest completed account02/B10 theorem, giving (6.3) on an exact target-valid fragmented family.

Not proved:

- a universal `L^infinity` bound for the fully overlapping harmonic/diffuse endpoint;
- arbitrary exact rank three;
- the full owner QFORM conjecture with additional spectrum;
- continuity for the new all-finite-`L^p` branch.

Accordingly: `FULL_EXACT_RANK3_OPEN`, `FULL_QFORM_OPEN`, `QFORM-CONTINUOUS-REPRESENTATIVE_OPEN`.

No scheduler/task/cadence changes, email, push notification, cross-account authentication, paid/remote model call, public research release, or permission expansion were used.
