Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-10 progress-extrapolation — sharp Hessian stability, spectral-variance gap, and dyadic-packet rigidity

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run remains on P24's exact frozen pair, preserves the productive NM13-10 successor chain, does not reopen the posted Agresti--Veraar Problems 4--5 package, and uses a different mechanism from the immediately preceding best-N/little-endpoint argument: exact stability of the Bellman Hessian contraction.

New theorem status: **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW** for the stability theorem below. The parent full critical endpoint remains **PARTIAL / OPEN**.

## 0. Short handoff and fixed theorem before/after

The exact frozen source realization remains

- `X_0=H^{-1}(Torus)`;
- `X_{1/2}=L^2(Torus)`;
- `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)`;
- one real Brownian driver and `beta=1`;
- after the source-scale transform,
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`,
  with input and output measured in `L^p(Omega x (0,T);L^2(Torus))`.

Retained predecessor facts:

1. the strong fixed-pair endpoint is `r_*=3`, with `p=3` excluded;
2. the exact subcritical stochastic-input norm is
   `R_p=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, with `(3-p)R_p -> 4`;
3. for
   `||F||_{Z_{3,alpha}(T)}=sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`,
   the full-spectrum bracket is
   `2/3 <= alpha_*(T) <= 1`;
4. the exact additive saddle witness gives the conditional lower operator norm `4/9` at a possible `alpha=2/3` endpoint;
5. every dyadic spectral block has the critical `2/3` endpoint, finite arbitrary collections of `N` dyadic blocks satisfy the `529 N^(1/6)` endpoint estimate, and every full-spectrum output lies in the little logarithmic endpoint `Z^o_{3,1}`.

**Fixed strong endpoint before:** `r_*=3`, endpoint excluded.  
**Fixed strong endpoint after:** `r_*=3`, endpoint excluded.

**Full critical exponent bracket before:** `[2/3,1]`.  
**Full critical exponent bracket after:** `[2/3,1]`.

**Conditional full-pair `alpha=2/3` lower constant before/after:** `4/9 -> 4/9`.

The gain below is therefore a mechanism theorem, not a source-level exponent change.

---

## 1. Complete retained proof of the reported `[2/3,1]` bracket

### 1.1 Exact subcritical norm

For `p>=2`, define

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

The sharp semigroup Hessian estimates are

`D Psi_p(z)[-Az]=-||z||^p`,

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]
 <=(p-1)||z||^(p-2)||y||^2`,

and, by Hessian Cauchy--Schwarz,

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]|
 <=(p-1)||z||^(p-1)||y||`.

For a stopped finite-dimensional approximation set

`I=E int_0^T ||Z||^p dt`, `J=E int_0^T ||Y||^p dt`,
`delta=(3-p)/2`.

Ito's formula gives

`delta I
 <=(p-1)I^((p-1)/p)J^(1/p)
   +(p-1)/2 I^((p-2)/p)J^(2/p)`.

With `R=(I/J)^(1/p)`, this becomes

`delta R^2 <=(p-1)R+(p-1)/2`.

The positive root is

`R <= [(p-1)+sqrt(2(p-1))]/(3-p)
    = 1/(sqrt(2/(p-1))-1)=:R_p`.

The retained one-shell neutral-feedback witness attains this asymptotically on a fixed physical horizon through high-frequency scaling, so the norm is exact. Rationalization gives `(3-p)R_p ->4`.

### 1.2 Positive `Z_{3,1}` endpoint

Let `F=||T_TY||_2` on `Omega x (0,T)` and `ell=log(T/s)`. Finite-measure embedding gives

`F^*(s) <= R_p s^(-1/p) T^(1/p-1/3)||Y||_3`.

For `0<=ell<=3`, choose `p=2`. For `ell>=3`, choose

`p=3-3/ell`.

Then `R_p<=4ell/3` and

`ell(1/p-1/3)=1/p<=1/2`.

Hence

`s^(1/3)F^*(s)/(1+ell)
 <=(1+sqrt(2))||Y||_3`,

so `alpha_*(T)<=1`.

### 1.3 Negative obstruction below `2/3`

On one exact Fourier shell, scaled time gives

`dZ=-Z ds+(Z+Y)dB`.

After a finite-cost OU seed, work on a fixed positive-probability event with `1<=Z_1<=2`, and use the progressive near-critical feedback

`Y=gamma Z`, `0<gamma<<1`.

Set

`sigma=1+gamma`, `q=sigma^2-1`, `d=1+sigma^2/2`,

so

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`.

Take

`L_gamma=log(1/gamma)/(2gamma)`.

The feedback input has `||Y||_3=gamma^(-1/3+o(1))`. If

`kappa=2d/sigma^2`, `t_*=L_gamma-2sqrt(L_gamma)`, `x=dt_*`,

then the Gaussian exponent satisfies the exact saddle identity

`(x+dt)^2/(2sigma^2 t)-kappa x
 =d^2(t-t_*)^2/(2sigma^2 t)`.

A Mills lower bound integrated on a `sqrt(L_gamma)` window yields a spacetime tail `m_x >= c exp(-kappa x)` at output level comparable to `exp(x)`. The exact identities

`1-kappa/3=2q/(3sigma^2)`,

`q-(1-kappa/3)d=2q^2/(3sigma^2)`

and `q^2L_gamma ->0`, `q sqrt(L_gamma)->0` imply

`||Z||_{Z_{3,alpha}}/||Y||_3
 >= c gamma^(alpha-2/3)[log(1/gamma)]^(-alpha)(1+o(1))`.

This diverges for every `alpha<2/3`. Exact shell scaling transfers the witness to every fixed physical horizon. Therefore `alpha_*(T)>=2/3`, proving the retained bracket.

---

## 2. New exact Hessian-defect identity

Write

`x_s=e^{-sA}z`, `r_s=||x_s||`,

and, when `r_s>0`, define the spectral probability measure

`mu_{z,s}({lambda_n})=||P_n x_s||^2/r_s^2`,

where `P_n` projects onto the full eigenspace of `A` with eigenvalue `lambda_n`. Put

`q_s=E_{mu_{z,s}} lambda`,
`m_s=E_{mu_{z,s}} sqrt(lambda)`,
`V_s=q_s-m_s^2=Var_{mu_{z,s}}(sqrt(lambda))`.

For the scalar map `phi(x)=||x||^p`,

`D^2 phi(x)[h,h]
 =p||x||^(p-2)||h||^2
  +p(p-2)||x||^(p-4)<x,h>^2`.

Taking `h=A^(1/2)x_s` gives

`D^2 phi(x_s)[A^(1/2)x_s,A^(1/2)x_s]
 =p r_s^p [q_s+(p-2)m_s^2]`.

Since

`d/ds r_s^p = -p q_s r_s^p`,

we have

`p int_0^infinity q_s r_s^p ds = ||z||^p`.

Therefore

`D^2 Psi_p(z)[A^(1/2)z,A^(1/2)z]
 =||z||^p+p(p-2)int_0^infinity m_s^2 r_s^p ds`.

Subtracting this from `(p-1)||z||^p` and using the previous integral identity yields the exact stability formula

`boxed{
 (p-1)||z||^p
 -D^2 Psi_p(z)[A^(1/2)z,A^(1/2)z]
 =Delta_p(z)
}`

with

`boxed{
 Delta_p(z)
 =p(p-2) int_0^infinity
    Var_{mu_{z,s}}(sqrt(lambda)) ||e^{-sA}z||^p ds.
}`                                                        (2.1)

Thus `Delta_p(z)>=0`; for `p>2`, equality holds exactly when the spectral measure is supported on one eigenspace. This is the sharp equality/stability statement behind the predecessor Hessian contraction.

For `p=3`, (2.1) becomes

`Delta_3(z)=3 int_0^infinity V_s r_s^3 ds`.

The same spectral variance is the local covariance quantity appearing in the preceding common-Brownian Hellinger/decoherence calculation, so (2.1) gives a direct Bellman--covariance bridge.

---

## 3. Effective-gap maximal-regularity inequality

Expand the noise Hessian exactly in the transformed equation. The `zz` term is now not merely bounded by `(p-1)||Z||^p`; by (2.1), it equals that quantity minus `Delta_p(Z)`.

After stopping/localization and taking expectations,

`E Psi_p(Z_T)
 +delta I_p
 +(1/2)D_p
 <=(p-1)I_p^((p-1)/p)J_p^(1/p)
  +(p-1)/2 I_p^((p-2)/p)J_p^(2/p)`,                    (3.1)

where

`I_p=E int_0^T ||Z||^p dt`,
`J_p=E int_0^T ||Y||^p dt`,
`D_p=E int_0^T Delta_p(Z_t) dt`,
`delta=(3-p)/2`.

When `I_p>0`, define the dimensionless average spectral defect

`kappa_p=D_p/I_p`.

With

`R_p(Y)=(I_p/J_p)^(1/p)`,

(3.1) implies the exact effective-gap inequality

`boxed{
 (delta+kappa_p/2) R_p(Y)^2
 <=(p-1)R_p(Y)+(p-1)/2.
}`                                                        (3.2)

Consequently

`R_p(Y)
 <=[(p-1)+sqrt((p-1)^2+2(p-1)(delta+kappa_p/2))]
   /[2(delta+kappa_p/2)].`                                (3.3)

For `kappa_p=0`, (3.3) is exactly the sharp predecessor norm `R_p`. Any positive spectral variance therefore acts as an additional coercive gap.

At `p=3`, whenever the stopped cubic quantities are finite, (3.2) reads

`(kappa_3/2)R_3(Y)^2 <=2R_3(Y)+1`,

hence

`R_3(Y) <= [2+sqrt(4+2kappa_3)]/kappa_3`.

So strong cubic maximal regularity fails only through trajectories whose average Bellman spectral variance collapses to zero.

---

## 4. New data-dependent extrapolation bound at critical quantiles

Let `ell=log(T/s)>=6` and choose

`p_ell=3-3/ell`, `delta=3/(2ell)`.

For `5/2<=p<3`, one has `0<=kappa_p<=p-2<=1`; hence

`epsilon=delta+kappa_p/2 <=1`.

If `b=p-1<=2`, the positive root in (3.3) obeys

`epsilon R <= [b+sqrt(b^2+2b epsilon)]/2
 <=1+sqrt(2)`.

Therefore

`R_p(Y)
 <= 2(1+sqrt(2)) ell/(3+kappa_p ell)`.

Finite-measure embedding gives

`s^(1/3)F^*(s)
 <= exp(ell(1/p-1/3))R_p(Y)||Y||_3`.

Since `ell(1/p-1/3)=1/p<=1/2`,

`boxed{
 s^(1/3)F^*(s)
 <= 8 ell/(3+kappa_{p_ell} ell) ||Y||_3.
}`                                                        (4.1)

The executed checker verifies the sharper prefactor before rounding:

`2(1+sqrt(2))sqrt(e)=7.96073050459...<8`.

This is a new full-spectrum extrapolation mechanism applied directly to the unresolved endpoint. In particular, any branch satisfying

`kappa_{p_ell} >= c ell^(-2/3)`

already obeys

`s^(1/3)F^*(s) <= (8/c) ell^(2/3)||Y||_3`,

which is the critical exponent. Thus the only remaining difficult branch has

`kappa_{p_ell}=o(ell^(-2/3))`.

Exact one-shell states have `kappa=0`, so this does not by itself close the parent endpoint; it must be combined with the already-proved critical one-band/comparable-band estimate.

---

## 5. Dyadic-packet rigidity from the same defect

The effective gap is not merely abstract. Small `Delta_p` quantitatively forces spectral concentration.

Let the dyadic projections be

`Q_j=1_[2^j,2^(j+1))(A)`,

and for a fixed nonzero state `z` put

`theta_j=||Q_jz||^2/||z||^2`.

Define the nonadjacent dyadic pair mass

`P(z)=sum_{j<k, k-j>=2} theta_j theta_k`.

### 5.1 Pairwise lower bound

Write the exact eigenspace masses as `c_n=||P_nz||` and `a_n=sqrt(lambda_n)`. From the variance expansion,

`Delta_p(z)
 =p(p-2) sum_{n<m}(a_n-a_m)^2
   int_0^infinity
     c_n^2 c_m^2 e^{-2(a_n^2+a_m^2)s}
     r_s^(p-4) ds`.

Because `A>=I`, `r_s<=||z||e^{-s}`. Hence for `2<p<=3`,

`r_s^(p-4) >= ||z||^(p-4)e^{(4-p)s}`,

and therefore each pair contributes at least

`p(p-2)||z||^p theta_n theta_m
 (a_n-a_m)^2/[2(a_n^2+a_m^2)-(4-p)].`

If two eigenvalues lie in dyadic blocks whose indices differ by at least two, then their square-root ratio is at least `sqrt(2)`. Since

`g(x)=(x-1)^2/[2(1+x^2)]`

is increasing for `x>=1`,

`g(x)>=g(sqrt(2))=(3-2sqrt(2))/6`.

Thus, for `5/2<=p<3`,

`boxed{
 Delta_p(z)/||z||^p >= c_* P(z),
 c_*=5(3-2sqrt(2))/24
     =0.0357443490112... .
}`                                                        (5.1)

### 5.2 Three-block packet concentration

Let `J,J'` be independent dyadic-block indices with law `theta`. Then

`Pr(|J-J'|>=2)=2P(z)`.

Averaging over `J`, there exists some block index `j(z)` such that

`sum_{|k-j(z)|>=2} theta_k <=2P(z)`.

Equivalently, if `Pi_j=Q_{j-1}+Q_j+Q_{j+1}` (with the obvious boundary convention),

`inf_j ||(I-Pi_j)z||^2/||z||^2
 <=2P(z)
 <=(2/c_*) Delta_p(z)/||z||^p.`                            (5.2)

The numerical factor is

`2/c_*=55.9529003976...`.

Integrating (5.2) along the stochastic trajectory gives

`boxed{
 [E int ||Z_t||^p d_3(Z_t)^2 dt]/I_p
 <=(2/c_*) kappa_p,
}`                                                        (5.3)

where

`d_3(z)^2=inf_j ||(I-Pi_j)z||^2/||z||^2`.

Thus small effective defect means that, in `||Z||^p`-weighted spacetime average, the solution lies close to some three-adjacent-dyadic-block packet. The packet center may depend on `(omega,t)`; that moving center is precisely what remains uncontrolled.

---

## 6. Near-extremizer stability of the exact subcritical norm

Let `R_p^*` denote the exact sharp norm

`R_p^*=1/(sqrt(2/(p-1))-1)`.

Suppose

`R_p(Y) >= theta R_p^*`, `0<theta<=1`.

From (3.2) and the exact root identity for `R_p^*`,

`kappa_p
 <=2(p-1)(theta^(-1)-1)/R_p^*
  +(p-1)(theta^(-2)-1)/(R_p^*)^2.`                        (6.1)

Hence every fixed positive fraction of a sharp subcritical extremizer has

`kappa_p=O(3-p)` as `p up to 3`.

A particularly clean quantitative consequence is obtained at `theta=1/2`. For `5/2<=p<3`,

`kappa_p <=(5/2)delta`, `delta=(3-p)/2`.

Combining with (5.3),

`boxed{
 R_p(Y)>=R_p^*/2
 =>
 [E int ||Z||^p d_3(Z)^2]/I_p
 <70(3-p).
}`                                                        (6.2)

So any family carrying even half of the exact `(3-p)^(-1)` blow-up becomes asymptotically concentrated in a moving three-block packet as `p up to3`.

This is a full-pair necessary rigidity theorem, not a restrictive sufficient condition imposed on the source theorem.

---

## 7. Connection to the unresolved critical endpoint

The preceding chain now gives a sharp dichotomy for any attempted full-spectrum endpoint proof or counterexample.

1. **Variance-rich branch.** If `kappa_{p_ell}` is at least order `ell^(-2/3)`, (4.1) already gives the desired `ell^(2/3)` critical quantile scale.

2. **Variance-poor branch.** If `kappa_{p_ell}=o(ell^(-2/3))`, (5.3) forces the high-`p` output to lie close, in weighted spacetime average, to a three-adjacent-block packet. Every fixed such packet is already covered by the comparable-band critical theorem.

Therefore the unresolved mechanism is no longer generic multiscale forcing. It is specifically **adaptive migration of a narrow comparable spectral packet across unboundedly many dyadic locations while forcing remains active**.

This meshes with both immediately preceding successor mechanisms:

- the best-N/little-endpoint theorem says near-`log^1` behavior requires spectral escape through more and more dyadic locations;
- the Hellinger/decoherence theorem says passive unequal-scale coherence after forcing is switched off has finite critical memory.

The only route left between these two facts is repeatedly forced packet migration. A source-valid counterexample above `2/3` must implement that mechanism; a positive proof should charge those migrations by cubic input energy.

---

## 8. Essential checks

Executed checker:

`2026-09-20T16-15-24+0300__spectral_variance_stability_check.py`

Archived output:

`2026-09-20T16-15-24+0300__spectral_variance_stability_check.out`

It verifies:

- `g'(x)=(x-1)(x+1)/(1+x^2)^2`, so the separated-shell ratio is minimized at `sqrt(2)`;
- `c_*=5(3-2sqrt(2))/24=0.0357443490112...`;
- `2/c_*=55.9529003976...`;
- the effective-gap quadratic root reduces exactly to the predecessor sharp root when `kappa=0`;
- the critical quantile prefactor is `7.96073050459...<8`;
- representative two-shell exact numerical defect integrals dominate the universal pair lower bound for `p=2.5,2.75,3` and square-root ratios `sqrt(2),2,10`;
- the archive ends `CHECK_PASS`.

The numerical checks support, but do not replace, the analytic proof above.

---

## 9. Literature boundary

A bounded fresh search retained Agresti--Veraar arXiv:2501.18561 as the Problem 3 source. Lorist--van Neerven--Veraar arXiv:2608.20266 studies necessary Banach-geometry conditions for deterministic/stochastic maximal regularity, and Evangelopoulos-Ntemiris--Veraar arXiv:2505.22145 concerns discrete stochastic maximal regularity and numerical/discrete extrapolation. The bounded search did not locate a source-matching resolution of this exact nonsmall multiplicative torus endpoint. This is not a worldwide novelty certificate.

`POSTED.md`'s Agresti--Veraar Problems 4--5 exclusion is respected throughout.

---

## 10. Before/after and next attack

**Source-level before:** `r_*=3` excluded; `2/3<=alpha_*(T)<=1`; conditional critical norm lower bound `4/9`.

**Source-level after:** unchanged.

**Demonstrated mechanism gain:** exact Hessian stability identity (2.1), effective spectral gap (3.2), data-dependent critical quantile improvement (4.1), and the full-pair near-extremizer packet rigidity (6.2).

**Residual obstruction:** a moving three-block packet can migrate through infinitely many dyadic scales. Existing fixed/comparable-band endpoint control does not automatically follow a packet center depending on `(omega,t)`.

**Next attack:** prove an active packet-migration Carleson estimate. Use the common-Brownian Hellinger kernel to charge transitions between separated packet centers, and charge adjacent moves by the cubic input energy/excursion clock. A summable migration charge would combine the variance-rich branch with the comparable-band endpoint and close `L^3 -> Z_{3,2/3}` for the full frozen pair.
