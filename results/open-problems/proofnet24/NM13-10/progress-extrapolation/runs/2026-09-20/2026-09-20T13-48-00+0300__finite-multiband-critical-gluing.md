Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.**

# NM13-10 progress-extrapolation — finite multiband critical gluing with only N^(1/6) loss

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, current LIVE20 mapping. This run stays on P24's exact frozen semigroup pair, preserves all productive NM13-10 successors, does not reopen Problems 4--5, and changes method from the preceding Rayleigh-quotient excursion proof to a rearrangement square-function/gluing argument.

New theorem status: **CANDIDATE_FULL / SELF-CHECKED / PENDING INDEPENDENT REVIEW** as a finite/countable multiband theorem. The unrestricted full-spectrum parent remains **PARTIAL**.

## 0. Short handoff; fixed theorem before and after

The exact P24 realization remains

- `X_0=H^{-1}(Torus)`;
- `X_{1/2}=L^2(Torus)`;
- `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)` with `beta=1`;
- one real Brownian driver;
- transformed stochastic-input equation
  `dZ=-AZ dt+A^(1/2)(Z+Y)dW`, `Z(0)=0`;
- stochastic input/output measured in `L^p(Omega x (0,T);L^2(Torus))`.

The P24 handoff records the source Problem 3 wording: if `(A,B) in SMR^bullet_{p,0}` for some `p>=2`, does one have `(A,B) in SMR^bullet_{r,0}` for all `r>2`, or at least for some larger range? P24's family disproves the pair-independent all-r alternative and freezes the present pair at the exact endpoint below; it does not settle the remaining arbitrary-pair quantitative interpretation.

Retained predecessor mathematics:

1. P24: for `(Lambda,beta Lambda^(1/2))`, `r_*(beta)=1+2/beta^2`, endpoint excluded. Hence for `beta=1`, `r_*=3` and `(A,B) notin SMR_{3,0}`.
2. NM13-10: exact full frozen-pair subcritical stochastic-input norm
   `C_p^g(T)=1/(sqrt(2/(p-1))-1)`, `2<=p<3`, with `(3-p)C_p^g(T)->4`.
3. NM13-10: full critical spacetime bracket
   `2/3 <= alpha_*(T) <= 1` for
   `||F||_{Z_{3,alpha}(T)}=sup_{0<s<T} s^(1/3)F^*(s)/(1+log(T/s))^alpha`.
4. NM13-10: the additive exact saddle witness gives the conditional full-pair endpoint lower constant `4/9` at `alpha=2/3`.
5. NM13-10: every single eigenspace has the exact critical exponent `2/3` for arbitrary progressive forcing; the immediately preceding run extended that to every comparable spectral band `lambda_0 I <= A <= K lambda_0 I`, with
   `||T_TY||_{Z_{3,2/3}} <=65 sqrt(K)||Y||_3`.

**Fixed strong endpoint before:** `r_*=3`, endpoint excluded.  
**Fixed strong endpoint after:** `r_*=3`, endpoint excluded.

**Full-spectrum critical bracket before:** `[2/3,1]`.  
**Full-spectrum critical bracket after:** `[2/3,1]`.

**Conditional full-pair endpoint lower constant before/after:** `4/9 -> 4/9`.

No restricted theorem below is relabeled as the source theorem. The strict gain is that arbitrarily separated active bands can now be glued at the critical `2/3` exponent with a loss depending only on the number/energy profile of active dyadic bands, not on their spectral separation. In particular the unresolved two-separated-active-band obstruction is removed.

---

## 1. Complete recovered proof of the reported full-pair bracket

This section records the essential proof rather than treating `[2/3,1]` as a black-box inherited number.

### 1.1 Exact subcritical norm

For `p>=2`, on the transformed Hilbert coordinate define

`Psi_p(z)=int_0^infinity ||e^{-sA}z||^p ds`.

The sharp `1/p`-weighted Hessian calculation from the predecessor runs gives

`D Psi_p(z)[-Az]=-||z||^p`,

`D^2 Psi_p(z)[A^(1/2)y,A^(1/2)y] <=(p-1)||z||^(p-2)||y||^2`,

and positive-semidefinite Hessian Cauchy--Schwarz gives

`|D^2 Psi_p(z)[A^(1/2)z,A^(1/2)y]| <=(p-1)||z||^(p-1)||y||`.

For the stopped finite-dimensional equation and

`I=E int ||Z||^p`, `J=E int ||Y||^p`, `delta=(3-p)/2`,

Ito therefore yields

`delta I <=(p-1)I^((p-1)/p)J^(1/p)
          +(p-1)/2 I^((p-2)/p)J^(2/p)`.

If `R=(I/J)^(1/p)`, then

`delta R^2 <=(p-1)R+(p-1)/2`.

Solving this quadratic and rationalizing gives exactly

`R <= R_p :=1/(sqrt(2/(p-1))-1)`.

The one-shell neutral progressive feedback from P24/NM13-10 attains the same number in the high-frequency fixed-horizon limit, so

`C_p^g(T)=R_p`, `2<=p<3`, every `T>0`,

and `(3-p)R_p->4`.

### 1.2 Positive critical endpoint `alpha<=1`

Let `F=||T_TY||`, `L=log(T/s)`. Finite-measure embedding and the exact subcritical norm give

`F^*(s) <=R_p s^(-1/p)T^(1/p-1/3)||Y||_3`.

For `0<=L<=3`, choose `p=2`. Since `R_2=1+sqrt(2)` and `e^(L/6)/(1+L)<=1`,

`s^(1/3)F^*(s)/(1+L) <=(1+sqrt(2))||Y||_3`.

For `L>=3`, choose `p=3-3/L`. Then rationalization gives `R_p<=4L/3`, while

`(T/s)^(1/p-1/3)=exp(1/p)<=sqrt(e)`.

Hence

`s^(1/3)F^*(s)/(1+L) <=(4sqrt(e)/3)||Y||_3
                     <(1+sqrt(2))||Y||_3`.

Thus

`||T_TY||_{Z_{3,1}(T)} <=(1+sqrt(2))||Y||_3`,

so `alpha_*(T)<=1`.

### 1.3 Negative critical obstruction `alpha>=2/3`

On one exact Fourier shell, scaled time gives

`dZ=-Z ds+(Z+Y)dB`.

A finite-cost OU seed produces a fixed positive-probability event on which `1<=Z_1<=2`. On that event run the near-critical progressive feedback

`Y=gamma Z`, `0<gamma<<1`.

Put

`sigma=1+gamma`, `q=sigma^2-1`, `d=1+sigma^2/2`.

Then

`Z_{1+t}=Z_1 exp(sigma B_t-dt)`,

and `E|Z_{1+t}|^3` grows as `exp(3qt)`. Choose

`L_gamma=log(1/gamma)/(2gamma)`.

The cubic feedback cost satisfies `||Y||_3=gamma^(-1/3+o(1))` (the seed contributes only a bounded lower-order amount).

For the occupation lower bound set

`kappa=2d/sigma^2`, `t_*=L_gamma-2sqrt(L_gamma)`, `x=d t_*`.

The Gaussian exponent has the exact saddle identity

`(x+dt)^2/(2sigma^2 t)-kappa x
 =d^2(t-t_*)^2/(2sigma^2 t)`.

Integrating a Mills lower bound on the window `t in [t_*,t_*+sqrt(t_*)]` gives a spacetime tail

`m_x >=c exp(-kappa x)`

at output level comparable to `exp(x)`. The exact algebra

`1-kappa/3=2q/(3sigma^2)`,

`q-(1-kappa/3)d=2q^2/(3sigma^2)`

shows that the tail growth matches the feedback third-moment growth to first order, while `q^2L_gamma->0` and `q sqrt(L_gamma)->0`. Therefore

`||Z||_{Z_{3,alpha}}/||Y||_3
 >=c gamma^(alpha-2/3)[log(1/gamma)]^(-alpha)(1+o(1))`.

This diverges for every `alpha<2/3`. Exact Fourier-shell scaling transfers the construction to every fixed physical horizon `T>0`. Thus `alpha_*(T)>=2/3`, proving the retained full-pair bracket

`2/3 <=alpha_*(T)<=1`.

The sharper additive saddle calculation retained from a later run gives the conditional norm lower bound `4/9` at the possible `alpha=2/3` endpoint; that constant is unchanged here.

---

## 2. New rearrangement lemma: `Z_{3,2/3}` is dimension-free 2-convex

Write

`L_T(s)=1+log(T/s)`, `0<s<T`,

and

`||f||_Z=sup_{0<s<T} s^(1/3) f^*(s)/L_T(s)^(2/3)`.

Let `f_j>=0` be a finite or countable family and

`F=(sum_j f_j^2)^(1/2)`.

> **Lemma NM10-Z-2CONVEX-13.**
>
> `||F||_Z <=sqrt(33) (sum_j ||f_j||_Z^2)^(1/2)`.

### Proof

Set `a_j=||f_j||_Z`. For every `u in (0,T)`,

`f_j^*(u)^2 <=a_j^2 u^(-2/3)L_T(u)^(4/3)`.

Hardy--Littlewood submajorization gives

`int_0^s F^*(u)^2 du
 =int_0^s (F^2)^*(u)du
 <=sum_j int_0^s f_j^*(u)^2du`.

Since `F^*` is decreasing,

`s F^*(s)^2 <=int_0^s F^*(u)^2du`.

It remains to bound

`I(s)=int_0^s u^(-2/3)L_T(u)^(4/3)du`.

Put `u=s exp(-x)` and `L=L_T(s)>=1`. Then

`I(s)=s^(1/3) int_0^infinity exp(-x/3)(L+x)^(4/3)dx`

and `L+x<=L(1+x)`, so

`I(s)<=C_0 s^(1/3)L^(4/3)`,

where

`C_0=int_0^infinity exp(-x/3)(1+x)^(4/3)dx`.

For `x>=0`,

`(1+x)^(4/3)<=1+(4/3)x+x^(4/3)`.

Indeed, differentiating the difference reduces this to the subadditivity of `t^(1/3)`.

Hence

`C_0 <=3+12+3^(7/3)Gamma(7/3)`.

Now `Gamma(7/3)=(4/9)Gamma(1/3)`. Also

`Gamma(1/3)=int_0^1 t^(-2/3)e^(-t)dt+int_1^infinity t^(-2/3)e^(-t)dt`.

On `[0,1]`, `e^(-t)<=1-t/2`, so the first integral is at most

`3-(1/2)(3/4)=21/8`.

On `[1,infinity)`, `t^(-2/3)<=1`, so the second integral is at most `e^(-1)<3/8`. Therefore `Gamma(1/3)<3`, hence `Gamma(7/3)<4/3`. Finally `3^(1/3)<3/2`, so `3^(7/3)<27/2`, and

`C_0<15+(27/2)(4/3)=33`.

Combining the estimates,

`F^*(s)^2
 <=33 s^(-2/3)L_T(s)^(4/3) sum_j a_j^2`.

Taking the supremum in `s` proves the lemma. Countable families follow by monotone convergence. QED.

The checker gives the actual integral value `C_0=21.093956789864...`; the proof deliberately uses the elementary rigorous envelope `33`.

---

## 3. New theorem: arbitrary finite collections of separated active dyadic bands

Let

`E_j=1_[2^j,2^(j+1))(Lambda)L^2(Torus)`,

with orthogonal projections `P_j`. For progressive `Y`, write

`Y_j=P_jY`, `Z_j=P_jZ`,

and

`J_j=E int_0^T ||Y_j||_2^3 dt`.

Because `A` and `B=A^(1/2)` commute with every `P_j`, each `Z_j` solves the same frozen equation inside `E_j`. The predecessor comparable-band theorem has `K<=2` on `E_j`, hence

`|| ||Z_j||_2 ||_Z <=65 sqrt(2) J_j^(1/3)`.               (3.1)

Orthogonality gives pointwise on `Omega x (0,T)`

`||Z||_2=(sum_j ||Z_j||_2^2)^(1/2)`.

Applying Lemma NM10-Z-2CONVEX-13 to (3.1) yields the new energy-profile estimate

> **Theorem NM10-AVP3-MULTIBAND-13.**
>
> For every progressive input whose dyadic block energies satisfy
>
> `sum_j J_j^(2/3)<infinity`,
>
> one has
>
> `||T_TY||_{Z_{3,2/3}(T)}
>   <=65 sqrt(66) (sum_j J_j^(2/3))^(1/2)`.               (3.2)
>
> In particular `65 sqrt(66)<529`.

No spectral-separation factor appears in (3.2).

### Finite N-band corollary

If `Y` is supported in at most `N` arbitrary dyadic blocks, then

`(sum_j J_j^(2/3))^(1/2)
 <=N^(1/6)(sum_j J_j)^(1/3)`

by the finite-dimensional embedding `ell^3_N -> ell^2_N`. Pointwise,

`sum_j ||Y_j||_2^3 <=(sum_j ||Y_j||_2^2)^(3/2)`,

so

`sum_j J_j <=E int ||Y||_2^3 =||Y||_3^3`.

Therefore

`||T_TY||_{Z_{3,2/3}(T)}
 <529 N^(1/6)||Y||_3`.                                  (3.3)

For **two arbitrary dyadic bands**, no matter how far apart spectrally,

`||T_TY||_{Z_{3,2/3}(T)} <594||Y||_3`.                  (3.4)

Thus the active two-separated-band critical endpoint is now controlled uniformly in the frequency gap. The previous obstruction cannot already occur in a single unequal pair; any failure of the full `2/3` endpoint must use an unbounded multiscale family or a mechanism not visible after this square-function reduction.

### Finite spectral-ratio corollary

If the spectral support lies in an arbitrary interval `[lambda_min,lambda_max]` with ratio

`K=lambda_max/lambda_min`,

then it intersects at most

`N<=2+ceil(log_2 K)`

dyadic blocks. Hence

`||T_TY||_{Z_{3,2/3}(T)}
 <529 [2+ceil(log_2 K)]^(1/6)||Y||_3`.                  (3.5)

Together with the predecessor direct comparable-band estimate, one may take

`min{65 sqrt(K), 529[2+ceil(log_2 K)]^(1/6)}`

as a valid finite-range endpoint constant. The new dependence is polylogarithmic in spectral condition ratio instead of square-root for wide bands. For the idealized case `K=2^N`, the executed checker confirms that the new coarse bound first beats `65 sqrt(K)` at integer `N=7`; this numerical crossover is only a sanity comparison, not part of the proof.

---

## 4. Why this is a genuine mechanism gain but not source closure

The preceding run controlled one comparable band by an excursion clock and lost `sqrt(K)` across its condition ratio. The present proof changes mechanism completely: it first solves every dyadic block at the critical endpoint, then uses a dimension-free `2`-convexity property of the exact critical rearrangement space. This removes **all dependence on the spectral gaps between blocks**.

The theorem is materially stronger than the predecessor in two ways:

1. arbitrary two widely separated active bands now satisfy the critical `2/3` endpoint with a gap-independent constant;
2. an arbitrary finite range of `N` dyadic scales costs only `N^(1/6)`, equivalently at most a sixth power of the logarithmic spectral ratio, rather than `sqrt(K)`.

But (3.2) exposes the exact remaining defect. The source norm only guarantees

`sum_j J_j <=J`,

whereas the new endpoint bound contains

`(sum_j J_j^(2/3))^(1/2)`.

For an arbitrary `ell^1` energy profile this can diverge. Therefore a statement such as `sum J_j^(2/3)<infinity` is only a **more restrictive sufficient condition** and is not the Agresti--Veraar source theorem. Likewise the `N^(1/6)` factor does not close the unrestricted full-spectrum endpoint.

This calculation is still decisive for the parent problem: it proves that spectral separation itself is no longer an obstruction at any fixed number of active bands. The unresolved issue is specifically a many-band summation problem. To remove the `N^(1/6)`/energy-profile loss one must use information discarded by black-box block gluing, namely the shared-Brownian cross-scale covariance/Hellinger structure developed in the preceding covariance run.

A useful negative diagnosis also follows: any proof that treats block outputs only through their separate `Z_{3,2/3}` norms and then applies a generic square-function inequality cannot improve (3.2) to the source `L^3` norm uniformly; the mismatch is exactly `ell^2` of the block `L^3` norms versus `ell^3` energy summation. The next proof must therefore be covariance-sensitive rather than another norm-only gluing argument.

---

## 5. Essential checker

The archived checker

`2026-09-20T13-48-00+0300__multiband_squarefunction_checker.py`

was executed before persistence. Its output is archived as

`2026-09-20T13-48-00+0300__multiband_squarefunction_checker.out`.

It verifies:

- `C_0=21.093956789864...<33`;
- `65 sqrt(66)=528.0624963...<529`;
- the two-band rigorous constant is `592.7301112...<594`;
- the elementary bound `21/8+e^(-1)<3` used for `Gamma(1/3)<3`;
- the wide-range comparison against `65 sqrt(K)` for representative `K=2^N`.

The archived execution ends `CHECK_PASS`. The proof of the theorem is analytic; the numerical integral is only a check.

---

## 6. Bounded current literature check

A fresh bounded check on 20 September 2026 found no source-matching resolution of this exact frozen critical rearrangement endpoint.

- Agresti--Veraar, arXiv:2501.18561 / NoDEA 32 (2025), remains the Problem 3 source.
- Bechtel--Veraar, *An extrapolation result in the variational setting: improved regularity, compactness, and applications to quasilinear systems*, published 11 July 2025, proves some `p>2` extrapolation under the variational/coercive symmetry framework; it does not identify the present nonsmall multiplicative critical endpoint.
- Evangelopoulos-Ntemiris--Veraar, *Discrete stochastic maximal regularity*, arXiv:2505.22145, concerns temporal discrete/operator stochastic maximal regularity and discrete extrapolation.
- Lorist--van Neerven--Veraar, *Necessary conditions for deterministic and stochastic maximal regularity*, arXiv:2608.20266, dated 20 August 2026, studies Banach-geometry necessary conditions and canonical test operators, not this exact state-multiplicative torus endpoint.
- Evangelopoulos-Ntemiris, *Fully discrete stochastic maximal regularity and H-infinity-calculus for second-order elliptic operators*, arXiv:2609.07436, dated 7 September 2026, concerns finite-element/time-discrete elliptic schemes.

This is a bounded literature check, not a worldwide novelty certificate.

---

## 7. Residual obstruction and next attack

The parent full-spectrum quantity remains

`2/3 <=alpha_*(T)<=1`.

The new theorem removes both the one-band and fixed-finite-many-band obstructions. The exact remaining target is a **covariance-improved active-band gluing estimate** that replaces

`(sum_j J_j^(2/3))^(1/2)`

by `(sum_j J_j)^(1/3)` without assuming extra spectral summability. The passive Hellinger theorem already gives summable gap decay after forcing stops. The next attack should insert that covariance information into the active square-function distribution estimate, aiming for a cubic/Carleson summation rather than the generic 2-convex `ell^2` summation used here.

Because this run produced a strict theorem-level gain and uniformly solved the two-separated-active-band case, no T05 fallback is triggered.

---

## 8. ledger_delta summary

- fixed strong source endpoint: `3 -> 3`, endpoint excluded;
- full-spectrum critical bracket: `[2/3,1] -> [2/3,1]`;
- new theorem: `N` arbitrary dyadic active bands satisfy the critical `2/3` endpoint with constant `<529 N^(1/6)`;
- two arbitrary separated dyadic bands: critical endpoint constant `<594`, independent of gap;
- finite spectral ratio `K`: new alternative loss `<529[2+ceil(log_2 K)]^(1/6)` versus predecessor `65 sqrt(K)`;
- unrestricted full-spectrum source theorem: still PARTIAL;
- next obstruction: eliminate the block-energy `ell^2`/`ell^3` mismatch using common-noise covariance, not another blockwise norm estimate.
