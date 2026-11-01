Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-10 progress-extrapolation — full-spectrum little logarithmic endpoint via best spectral N-term approximation

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run stays on P24's exact frozen semigroup pair, preserves the productive NM13-10 successor chain, does not reopen the posted Problems 4--5 package, and uses a different mechanism from the preceding blockwise square-function theorem: best spectral N-term approximation plus endpoint closure.

New theorem status: **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW** for the exact frozen pair. The original strong endpoint and the exponent bracket remain **PARTIAL / OPEN**.

## 0. Short handoff and fixed theorem before/after

The frozen source realization is unchanged:

- `X_0=H^{-1}(Torus)`;
- `X_{1/2}=L^2(Torus)`;
- `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)`, `beta=1`;
- one real Brownian driver;
- transformed stochastic-input equation
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`;
- input and output measured in `L^p(Omega x (0,T);L^2(Torus))` after the source-scale transform.

The P24/source theorem and productive successor facts retained here are:

1. `r_*=3` for this fixed pair and the strong endpoint is excluded;
2. the exact subcritical stochastic-input norm is
   `C_p^g(T)=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, with `(3-p)C_p^g(T)->4`;
3. for
   `||F||_{Z_{3,alpha}(T)}=sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`,
   the full-spectrum critical bracket is `2/3<=alpha_*(T)<=1`;
4. the exact additive saddle witness gives the conditional lower norm `4/9` at a possible `alpha=2/3` endpoint;
5. every dyadic spectral block has the critical `2/3` endpoint, and the preceding run glued any `N` arbitrary dyadic blocks with
   `||T_TY||_{Z_{3,2/3}} <529 N^(1/6)||Y||_3`.

**Fixed strong endpoint before:** `r_*=3`, endpoint excluded.  
**Fixed strong endpoint after:** `r_*=3`, endpoint excluded.

**Full critical exponent bracket before:** `[2/3,1]`.  
**Full critical exponent bracket after:** `[2/3,1]`.

**Conditional full-pair `alpha=2/3` lower constant before/after:** `4/9 -> 4/9`.

The new gain is not an exponent change. It is a strictly stronger **full-spectrum endpoint target space** at the existing logarithmic exponent `1`: every output belongs to the little logarithmic endpoint, and there is an explicit best-N spectral approximation inequality. This is an unrestricted theorem for every progressive `L^3` input on the exact frozen pair, not a sufficient condition imposed on the source theorem.

---

## 1. Recovered proof of the reported `[2/3,1]` bracket

This section records the essential complete proof chain so the new argument does not reset or silently assume the baseline.

### 1.1 Exact subcritical norm

For `p>=2`, define the semigroup Bellman functional

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

The sharp `1/p`-weighted Hessian calculation gives

`D Psi_p(z)[-Az]= -||z||^p`,

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y]
 <=(p-1)||z||^(p-2)||y||^2`,

and Hessian Cauchy--Schwarz gives

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]|
 <=(p-1)||z||^(p-1)||y||`.

For the stopped finite-dimensional equation set

`I=E int ||Z||^p`, `J=E int ||Y||^p`, `delta=(3-p)/2`.

Ito's formula and Holder yield

`delta I <=(p-1) I^((p-1)/p)J^(1/p)
             +(p-1)/2 I^((p-2)/p)J^(2/p)`.

If `R=(I/J)^(1/p)`, then

`delta R^2 <=(p-1)R+(p-1)/2`.

The positive root is

`R <=[(p-1)+sqrt(2(p-1))]/(3-p)
    =1/(sqrt(2/(p-1))-1)=:R_p`.

The frozen one-shell neutral-feedback witness gives the reverse inequality in the high-frequency fixed-horizon limit, so this is the exact stochastic-input norm for every `2<=p<3`. Rationalization immediately gives `(3-p)R_p->4`.

### 1.2 Positive logarithmic endpoint

Let `F=||T_TY||` on `Omega x (0,T)` and write `L=log(T/s)`. The finite-measure embedding and the exact subcritical norm give

`F^*(s) <= R_p s^(-1/p) T^(1/p-1/3)||Y||_3`.

For `0<=L<=3`, choose `p=2`. Since `R_2=1+sqrt(2)` and `exp(L/6)/(1+L)<=1` on this interval,

`s^(1/3)F^*(s)/(1+L) <=(1+sqrt(2))||Y||_3`.

For `L>=3`, choose `p=3-3/L`. Then `R_p<=4L/3`, while

`L(1/p-1/3)=1/p<=1/2`.

Hence

`s^(1/3)F^*(s)/(1+L)
 <=(4sqrt(e)/3) L/(1+L)||Y||_3
 <(1+sqrt(2))||Y||_3`.

Therefore

`||T_TY||_{Z_{3,1}(T)} <=(1+sqrt(2))||Y||_3`,

so `alpha_*(T)<=1`.

### 1.3 Negative obstruction below `2/3`

On one exact Fourier shell, scaled time gives

`dZ=-Z ds+(Z+Y)dB`.

A finite-cost OU seed gives a fixed positive-probability event on which `1<=Z_1<=2`. On that event run the progressive near-critical feedback

`Y=gamma Z`, `0<gamma<<1`.

Set

`sigma=1+gamma`, `q=sigma^2-1`, `d=1+sigma^2/2`.

Then

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`

and the cubic moment grows as `exp(3qt)`. Choose

`L_gamma=log(1/gamma)/(2gamma)`.

The feedback input has

`||Y||_3 = gamma^(-1/3+o(1))`.

For the occupation lower bound put

`kappa=2d/sigma^2`, `t_*=L_gamma-2sqrt(L_gamma)`, `x=d t_*`.

The Gaussian exponent satisfies the exact saddle identity

`(x+dt)^2/(2sigma^2 t)-kappa x
 =d^2(t-t_*)^2/(2sigma^2 t)`.

A Mills lower bound integrated on a `sqrt(L_gamma)` saddle window gives a spacetime tail `m_x>=c exp(-kappa x)` at output level comparable to `exp(x)`. The exact identities

`1-kappa/3=2q/(3sigma^2)`,

`q-(1-kappa/3)d=2q^2/(3sigma^2)`

and `q^2L_gamma->0`, `q sqrt(L_gamma)->0` yield

`||Z||_{Z_{3,alpha}}/||Y||_3
 >=c gamma^(alpha-2/3)[log(1/gamma)]^(-alpha)(1+o(1))`.

This diverges for every `alpha<2/3`. Exact Fourier-shell scaling transfers the witness to every fixed physical horizon `T>0`. Thus `alpha_*(T)>=2/3`, and the retained parent bracket is indeed

`2/3 <= alpha_*(T) <=1`.

The sharper additive saddle calculation from the later successor gives the unchanged conditional endpoint norm lower bound `4/9` at `alpha=2/3`.

---

## 2. Essential predecessor used here: finite arbitrary-band critical control

Let

`E_j=1_[2^j,2^(j+1))(Lambda)L^2(Torus)`, `j>=0`,

with orthogonal projections `P_j`. For a finite set `S` of dyadic blocks, `P_S=sum_{j in S}P_j`.

The immediately preceding theorem proves, for every progressive input supported on at most `N` arbitrary dyadic blocks,

`||T_T P_S Y||_{Z_{3,2/3}(T)}
 <529 N^(1/6)||P_S Y||_3
 <=529 N^(1/6)||Y||_3`.                                  (2.1)

For continuity, its mechanism is recalled. Each dyadic block has spectral ratio at most `2`, so the comparable-band excursion theorem gives

`||T_TP_jY||_{Z_{3,2/3}} <=65 sqrt(2) J_j^(1/3)`,

`J_j=E int ||P_jY||^3`.

The exact endpoint space satisfies the dimension-free square-function inequality

`||(sum_j f_j^2)^(1/2)||_{Z_{3,2/3}}
 <=sqrt(33)(sum_j||f_j||_{Z_{3,2/3}}^2)^(1/2)`.

For `N` blocks,

`(sum J_j^(2/3))^(1/2)
 <=N^(1/6)(sum J_j)^(1/3)
 <=N^(1/6)||Y||_3`.

Thus `65 sqrt(66)<529`, proving (2.1). The preceding report contains the complete `sqrt(33)` Hardy--Littlewood integral proof and its executed checker. No spectral-gap factor appears in (2.1).

---

## 3. New full-spectrum endpoint: a strict little logarithmic space

Define

`L_T(s)=1+log(T/s)`, `0<s<T`,

and the little endpoint class

`Z^o_{3,1}(T)
 ={F in Z_{3,1}(T):
   lim_{s downarrow 0} s^(1/3)F^*(s)/L_T(s)=0}`.

This is a strict subspace of `Z_{3,1}`. For example on `(0,T)`, the decreasing function

`h(s)=s^(-1/3)L_T(s)`

belongs to `Z_{3,1}` but not to `Z^o_{3,1}`.

> **Theorem NM10-AVP3-LITTLE-ENDPOINT-14.**
>
> For the exact frozen pair and every progressive
> `Y in L^3(Omega x (0,T);L^2(Torus))`, if `F=||T_TY||_2`, then
>
> `F in Z^o_{3,1}(T)`.
>
> Equivalently,
>
> `lim_{s downarrow 0}
>   s^(1/3)F^*(s)/(1+log(T/s))=0`.                         (3.1)

This is a full-spectrum statement for arbitrary progressive input. It is stronger than the preceding bounded map into `Z_{3,1}`, although it does not yet replace exponent `1` by a uniform smaller exponent.

### 3.1 Best spectral N-term approximation

For `N>=1`, define

`e_N(Y)=inf_{S: |S|<=N} ||(I-P_S)Y||_{L^3(Omega x (0,T);L^2)}`.

Because finite unions of dyadic blocks converge strongly to the identity on `L^2(Torus)` and the projections are contractions, dominated convergence gives

`e_N(Y) ->0`                                                   (3.2)

for every `Y in L^3`.

Fix a finite `S`, `|S|<=N`, and decompose

`Y=Y_S+Y_R`, `Y_S=P_SY`, `Y_R=(I-P_S)Y`.

By linearity of the exact stochastic-input equation,

`T_TY=T_TY_S+T_TY_R`.

Put `F_S=||T_TY_S||_2`, `F_R=||T_TY_R||_2`. Pointwise triangle inequality and the standard rearrangement inequality give

`F^*(s) <=F_S^*(s/2)+F_R^*(s/2)`.                            (3.3)

For the finite-band term, (2.1) gives

`F_S^*(s/2)
 <=529 N^(1/6)||Y||_3 (s/2)^(-1/3)L_T(s/2)^(2/3)`.

For the remainder, the exact unrestricted logarithmic endpoint gives

`F_R^*(s/2)
 <=(1+sqrt(2))||(I-P_S)Y||_3
   (s/2)^(-1/3)L_T(s/2)`.

Since `L_T(s)>=1` and

`L_T(s/2)=L_T(s)+log2 <=(1+log2)L_T(s)`,

(3.3) yields

`s^(1/3)F^*(s)/L_T(s)
 <= A N^(1/6)L_T(s)^(-1/3)||Y||_3
    +B ||(I-P_S)Y||_3`,                                    (3.4)

where

`A=2^(1/3) 529 (1+log2)^(2/3)=946.8084933054...<947`,

`B=2^(1/3)(1+sqrt(2))(1+log2)=5.1500770789...<5.2`.

Taking the infimum over `S` proves the quantitative estimate

`boxed{
 s^(1/3)F^*(s)/L_T(s)
 <=947 N^(1/6)L_T(s)^(-1/3)||Y||_3 +5.2 e_N(Y)
}`                                                               (3.5)

for every `N>=1` and every `0<s<T`.

Now fix `N` and send `s downarrow0`; the first term vanishes. Hence

`limsup_{s downarrow0} s^(1/3)F^*(s)/L_T(s)
 <=5.2 e_N(Y)`.

Finally send `N->infinity` and use (3.2). This proves (3.1).

### 3.2 Closure formulation

The same argument gives a useful structural formulation:

`T_T(L^3)
 subset closure_{Z_{3,1}}
        ( union_{N<infinity} T_T{inputs on at most N dyadic blocks} )
 subset Z^o_{3,1}`.                                          (3.6)

Indeed the global endpoint bound implies

`||T_T(Y-P_SY)||_{Z_{3,1}}
 <=(1+sqrt(2))||(I-P_S)Y||_3`,

so finite-band responses converge in the endpoint norm. The little space is closed in `Z_{3,1}`: if `G_n->G` in `Z_{3,1}`, then

`G^*(s)<=G_n^*(s/2)+(G-G_n)^*(s/2)`

and the second term has normalized limsup bounded by

`2^(1/3)(1+log2)||G-G_n||_{Z_{3,1}}`;

first send `s downarrow0`, then `n->infinity`.

Thus the improvement is not merely pointwise approximation at one quantile: every exact-pair output lies in the closed little endpoint subspace.

---

## 4. New interpolation scale from quantitative spectral approximation

The best-N inequality (3.5) gives an explicit family of intermediate logarithmic exponents.

For `theta>0`, set

`D_theta(Y)=sup_{N>=1} N^theta e_N(Y)`.

Assume `D_theta(Y)<infinity`; this is a quantitative spectral approximation property, not part of the source theorem. Let

`nu=1/(3theta+1/2)=2/(6theta+1)`,

and choose `N=ceil(L_T(s)^nu)`. Since `N<=2L_T(s)^nu`, (3.5) before division by `L_T(s)` gives

`s^(1/3)F^*(s)
 <=947*2^(1/6)||Y||_3 L_T(s)^(2/3+nu/6)
   +5.2 D_theta(Y)L_T(s)^(1-theta nu)`.

The two exponents agree exactly:

`2/3+nu/6 = 1-theta nu
             =(4theta+1)/(6theta+1)=:alpha_theta`.          (4.1)

Therefore

`boxed{
 ||T_TY||_{Z_{3,alpha_theta}(T)}
 <=1063||Y||_3+5.2D_theta(Y),
 alpha_theta=(4theta+1)/(6theta+1)
}`                                                               (4.2)

with

`2/3<alpha_theta<1`, `alpha_theta downarrow2/3` as `theta->infinity`.

Examples:

- `theta=1/4` gives `alpha=4/5`;
- `theta=1/2` gives `alpha=3/4`;
- `theta=1` gives `alpha=5/7`.

This corollary is deliberately labeled a **more restrictive quantitative consequence**, not the Agresti--Veraar source theorem. Its role is to identify exactly how spectral approximation rate converts into endpoint-log improvement.

---

## 5. Necessary spectral complexity for any near log-1 saturation

Estimate (3.5) also gives a converse diagnostic for the still-open unrestricted exponent.

Normalize `||Y||_3=1` and suppose at a quantile `s`

`Q_Y(s):=s^(1/3)F^*(s)/L_T(s) >=eta`, `0<eta<=1`.

For every integer `N` satisfying

`947 N^(1/6)L_T(s)^(-1/3) <=eta/2`,

(3.5) forces

`e_N(Y) >= eta/(10.4)`.                                     (5.1)

Equivalently, one may take any

`N <= (eta/(1894))^6 L_T(s)^2`.

Thus a family that genuinely approaches the full `log^1` growth at finer and finer quantiles cannot remain spectrally simple or even uniformly N-term approximable: a fixed fraction of its `L^3` mass must escape every collection of order `L^2` dyadic bands (up to the explicit constants).

This is the first full-spectrum theorem here that turns the old qualitative phrase "the obstruction must be multiscale" into a quantitative necessary complexity statement. It dovetails with the earlier Hellinger/decoherence theorem: passive unequal scales lose critical cubic coherence at a summable gap-dependent rate, while any hypothetical `alpha=1` saturating family must continually move through an increasing number of active bands. The remaining problem is therefore specifically an **active spectral-escape** problem.

---

## 6. Essential checker

The executed checker

`2026-09-20T14-48-59+0300__little_endpoint_checker.py`

has archived output

`2026-09-20T14-48-59+0300__little_endpoint_checker.out`.

It verifies:

- `A=946.808493305426...<947`;
- `B=5.150077078925...<5.2`;
- the exact balancing identity
  `2/3+nu/6=1-theta nu=(4theta+1)/(6theta+1)`
  for representative `theta` values;
- the `L^2` near-saturation complexity scaling;
- representative rate balances for `theta=1/4,1/2,1`.

The output ends `CHECK_PASS`. The checker is supplementary; the theorem proof above is analytic.

---

## 7. Current literature boundary, checked 20 September 2026

A bounded fresh search found no source-matching resolution of this exact frozen nonsmall multiplicative endpoint.

- Agresti--Veraar arXiv:2501.18561 remains the Problem 3 source.
- Bechtel--Veraar, published 11 July 2025, proves a positive extrapolation interval in the variational setting under its coercivity/symmetry hypotheses; it does not determine this frozen pair's critical rearrangement endpoint.
- Evangelopoulos-Ntemiris--Veraar, published 13 February 2026, develops discrete stochastic maximal regularity and transfers continuous SMR to numerical schemes; it does not address the present state-multiplicative critical endpoint.
- Lorist--van Neerven--Veraar, arXiv:2608.20266 (20 August 2026), concerns Banach-space geometric necessary conditions for SMR, not this endpoint.
- Evangelopoulos-Ntemiris, arXiv:2609.07436 (7 September 2026), concerns fully discrete finite-element/time-discrete elliptic schemes, again a different setting.

This is a bounded literature check, not a worldwide novelty certificate.

---

## 8. Before/after, failed route, residual obstruction, next attack

### Fixed theorem before

`r_*=3`, strong endpoint excluded; full critical bracket `[2/3,1]`; conditional `alpha=2/3` lower norm `4/9`.

### Fixed theorem after

Exactly the same. No reset and no invented source-level endpoint movement.

### Demonstrated mechanism gain

For **every** progressive full-spectrum `L^3` input on the exact pair,

`T_TY in Z^o_{3,1}(T)`

with the explicit best-N estimate (3.5). Quantitative spectral approximation at rate `N^{-theta}` yields the intermediate exponent (4.2), and any family approaching `log^1` growth must exhibit order-`L^2` spectral complexity in the precise sense (5.1).

### Insufficient route preserved

Pure blockwise gluing leaves `N^(1/6)` and cannot uniformly close the full unit ball. The new closure argument extracts a full-spectrum theorem from that route but does not by itself improve the operator-norm exponent below `1`.

### Residual obstruction

Decide whether spectrally escaping active forcing can actually defeat the critical `2/3` endpoint. The necessary bad family is now much narrower: it must keep substantial input mass outside every `O(L^2)`-block approximation at quantile logarithm `L`, while passive cross-scale coherence is already summably short-lived.

### Next attack

Apply the existing critical Hellinger/decoherence kernel directly to the best-N remainder in (3.5). The objective is a covariance-improved estimate for spectrally escaping active families that replaces the residual `5.2 e_N(Y)` term by a quantity decaying with `N` uniformly on the `L^3` unit ball. Such an estimate would immediately turn (3.5) into a uniform exponent `<1`; the target rate needed for the exact `2/3` endpoint is now explicit.

No T05 fallback is triggered: this run produced a new full-spectrum theorem and a quantitative necessary condition for any remaining worst-case family.
