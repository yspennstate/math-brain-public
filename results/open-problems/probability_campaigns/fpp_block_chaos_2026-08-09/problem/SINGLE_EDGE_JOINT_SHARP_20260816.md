# Target mass and outside uncertainty have a sharper joint constant

Date: 2026-08-16  
Status: exact edge-level inequality proved; independent audit required before use

Companions:

* `SINGLE_EDGE_TARGET_MASS_SHARP_MONOTONE_20260816.md`, SHA-256
  `7b3039d5d74283d582bc996333bba27da81bb7569104c592088c06f91f14e68c`;
* `SINGLE_EDGE_OUTSIDE_UNCERTAINTY_20260816.md`, SHA-256
  `4118c45e48cf41d68779e27e4177f21f876c6b78f265a3efbba9ffb70c866658`.

The two companion estimates separately give the coefficients `1/9` and
`3/32` for the conditional target mass and outside uncertainty of one edge.
Those separate constants cannot be attained by the same decreasing threshold
profile.  Optimizing the two pieces together preserves the sharp `1/9`
coefficient and improves `3/32` to `64/729`.

This remains a single-coordinate estimate.  Its uncertainty term is not known
to be at the passage-time variance scale, and no block or revealment estimate is
claimed here.

## 1. Uniform threshold representation

Let iid edge weights have density `rho` on `[a,b]`, with

`rho(t)>=alpha>0` almost everywhere.                              (1)

For a fixed edge `e`, let `T_e` be the usual outside threshold: the canonical
geodesic uses `e` exactly when `w_e<T_e`, up to the null tie event.  Put

`q_e(t)=P(T_e>t),`

where the probability averages the outside environment, and let

`p_e=P(e in gamma),`

`r_e=E[q_e(w_e)(1-q_e(w_e))].`                                  (2)

If `w_e'` is an independent replacement and

`z_e=(X^e-X)^+,`

the exact resampling identity is

`z_e=1_(w_e'>w_e) integral_(w_e)^(w_e') 1_(t<T_e)dt.`            (3)

Use the generalized quantile of `F` and set

`q(u)=q_e(F^(-1)(u)),       0<u<1.`                             (4)

The exact second-moment kernel from the companions, followed only by the two
lower-density bounds, gives

`E[z_e^2]
 <=alpha^(-2) T(q),`

`T(q)=2 integral_(0<u<v<1) u(1-v)q(v)du dv.`                   (5)

Every decreasing `[0,1]`-valued `q` is the survival function of a random
variable `Tau in [0,1]`.  With

`g(t)=t^3/3-t^4/4,`                                            (6)

Tonelli turns (5) into

`T(q)=E[g(Tau)].`                                              (7)

Moreover, for iid copies `Tau_1,Tau_2`,

`p_e=integral_0^1 q(u)du=E[Tau],`

`r_e=integral_0^1 q(u)(1-q(u))du
    =E[(Tau_1-Tau_2)^+]
    =(1/2)E|Tau_1-Tau_2|.`                                    (8)

Thus the joint edge problem is an exact two-point inequality on `[0,1]`.

## 2. Sharp joint threshold lemma

**Lemma.** For every random variable `Tau in [0,1]`,

`E[g(Tau)]
 <=(1/9)(E Tau)^2+(64/729)E[(Tau_1-Tau_2)^+].`                 (9)

Neither coefficient can be decreased while the other is held fixed.

**Proof.** It is enough to prove, for every `0<=x<=y<=1`,

`g(x)+g(y)-(2/9)xy <=(64/729)(y-x).`                           (10)

Indeed, applying (10) to iid `Tau_1,Tau_2` and averaging gives twice (9).

Put `d=y-x` and

`phi(t)=t^2(3t-2)^2.`                                         (11)

The identity

`g(t)=t^2/9-phi(t)/36`                                       (12)

shows that the left side of (10), divided by `d>0`, is

`d/9-[phi(x)+phi(y)]/(36d).`                                 (13)

If `d<=64/81`, expression (13) is at most

`d/9<=64/729.`                                               (14)

Suppose instead that `d>=64/81`.  Then

`x<=1-d<=17/81<1/3,       y>=d>2/3.`                         (15)

Since

`phi'(t)=4t(3t-2)(3t-1),`                                   (16)

`phi` is increasing on `[2/3,1]`.  Hence `phi(y)>=phi(d)`, and
(13) is at most

`d/9-phi(d)/(36d)
 =d^2/3-d^3/4
 =g(d)/d.`                                                   (17)

Finally,

`64/729-g(d)/d
 =((9d-8)^2(9d+4))/2916>=0.`                                (18)

This proves (10).  The case `d=0` follows directly from

`g(x)-x^2/9=-phi(x)/36<=0.`                                 (19)

The first coefficient in (9) is sharp for deterministic `Tau=2/3`, because
`g(2/3)=(2/3)^2/9`.  To see that the second is sharp with `1/9` fixed, take

`P(Tau=8/9)=epsilon,       P(Tau=0)=1-epsilon.`               (20)

As `epsilon` tends to zero,

`[E g(Tau)-(E Tau)^2/9]/E[(Tau_1-Tau_2)^+]
 ->g(8/9)/(8/9)=64/729.`                                    (21)

QED

## 3. FPP consequence

Combining (5), (7)--(9) yields the jointly sharp edge ledger

`E[z_e^2]
 <=alpha^(-2)[p_e^2/9+(64/729)r_e].`                         (22)

The uncertainty coefficient satisfies

`64/729=(2048/2187)(3/32)<3/32,`                            (23)

so (22) strictly improves the result obtained by adding the two separately
sharp companion bounds.  The gain is about `6.36%` in the `r_e` coefficient.

The exact ANOVA identity remains

`r_e=p_e-E[q_e(w_e)^2]
    =p_e(1-p_e)-Var(q_e(w_e)).`                              (24)

Consequently

`sum_e E[z_e^2]
 <=alpha^(-2)[(1/9)sum_e p_e^2+(64/729)sum_e r_e].`          (25)

The first sum is the squared-influence target.  The second can still be as
large as a path-length scale under the available bounds.  The improvement in
(22) therefore sharpens the local ledger but does not close the aggregate FPP
variance problem.

## 4. Independent break checks

1. If `Tau=t` is deterministic, `r_e=0` and (9) reduces to
   `g(t)<=t^2/9`; the difference is exactly `phi(t)/36`.
2. For constant `q=c`, equivalently `Tau` Bernoulli on `{0,1}` with mean `c`,
   the exact value is `T(q)=c/12`.  Substitution in (9) gives a valid, generally
   non-sharp inequality.
3. The polynomial in (18) has a double zero at `d=8/9`, agreeing with the
   limiting sharpness construction (20).
4. Equation (10) was also checked on a `2001 x 2001` deterministic grid; its
   largest observed ratio was at `(x,y)=(0,0.889)`, within `5e-9` of
   `64/729`.  This numerical check is not used in the proof.
5. The two reciprocal density factors in (5) each cost `alpha^(-1)`; no density
   upper bound is used.
6. Sharpness in (9) means the Pareto pair `(1/9,64/729)` is exact.  It does not
   say that a single nondegenerate threshold law attains both coefficients.

pointwise split at `d=64/81`, and the limiting sharpness calculation before
this note is used as a campaign dependency.
