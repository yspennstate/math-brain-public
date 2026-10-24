Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-10 progress-extrapolation — critical Doob–Hardy additive saturator at the logarithmic `2/3` boundary

Source: Antonio Agresti and Mark Veraar, *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3.

Frozen P24 pair, unchanged throughout this run:

- one real Brownian driver;
- `X_0=H^{-1}(Torus)`;
- `X_{1/2}=L^2(Torus)`;
- `X_1=H^1(Torus)`;
- `A=Lambda=I-partial_x^2`;
- `B=Lambda^(1/2)` (equivalently beta=1);
- source equation `du + Au dt = f dt + (Bu+g)dW`, zero initial condition;
- source output norm `L^p(Omega;L^p(0,T;X_1))`, with stochastic input `g` in `L^p(Omega;L^p(0,T;gamma(R,X_{1/2})))=L^p(Omega x (0,T);L^2)`.

The already-posted Agresti–Veraar Problems 4–5 package is not reopened, imported, renamed, or used.

## 0. Handoff, fixed theorem, and exact before/after quantities

The old NM13-10 intake/admission worker is historical. Under `operations/PROGRESS20_2026-09-20.md`, this slot was redirected to P24's extrapolation line and has since made a productive successor chain on this exact pair. I preserve that chain rather than restarting it:

1. P24 proved for `B=beta Lambda^(1/2)` the exact strong family endpoint
   `r_*(beta)=1+2/beta^2`, endpoint excluded. Thus at beta=1,
   `r_*=3` and `(A,B) notin SMR_{3,0}`.
2. NM13-10 recovered the full Bellman proof and sharpened the stochastic-input constant to the exact subcritical value
   `C_p^g(T)=R_p=1/(sqrt(2/(p-1))-1)` for `2<=p<3`, with `(3-p)R_p -> 4`.
3. NM13-10 proved the positive critical rearrangement estimate `T_T:L^3 -> Z_{3,1}(T)` and proved that ordinary weak `(3,3)` fails.
4. NM13-10 constructed a source-valid one-shell near-critical feedback witness showing no `L^3 -> Z_{3,alpha}(T)` estimate for any `alpha<2/3`, hence
   `2/3 <= alpha_*(T) <= 1`.
5. The immediately preceding run proved that exponent `2/3` is sharp inside a broad deterministic nonnegative proportional-feedback class, but did not move the full endpoint bracket.

Here

`||F||_{Z_{3,alpha}(T)}
 := sup_{0<s<T} s^(1/3) F^*(s)/(1+log(T/s))^alpha`,

with rearrangement taken on `Omega x (0,T)`.

**Fixed strong source endpoint before:** `r_*=3`, endpoint `p=3` excluded.

**Fixed strong source endpoint after:** `r_*=3`, endpoint `p=3` excluded.

**Full critical rearrangement bracket before:** `2/3 <= alpha_*(T) <= 1`.

**Full critical rearrangement bracket after:** `2/3 <= alpha_*(T) <= 1`.

Thus this run makes **no source-level endpoint movement** and does not relabel a witness theorem as Agresti–Veraar Problem 3.

The demonstrated mechanism gain is different and quantitative: an explicit **progressive additive input**, with no state feedback at all, exactly saturates the critical `2/3` scaling from below. It also forces a nonzero lower bound on any possible `Z_{3,2/3}` endpoint norm constant.

Status: **EXPLICIT SOURCE-VALID WITNESS THEOREM PROVED / SELF-CHECKED; full critical endpoint remains PARTIAL and any full candidate awaits independent review.**

---

## 1. Essential recovered dependency: exact one-shell reduction

Let `phi_n` be an `L^2`-normalized Fourier eigenvector,

`Lambda phi_n=lambda_n phi_n`, `lambda_n=1+n^2 -> infinity`.

Take `f=0` and a stochastic input of the form

`g_n(t)=y_n(t) phi_n`.

The solution remains in this eigenspace, `u_n(t)=x_n(t)phi_n`, and obeys

`dx_n = -lambda_n x_n dt + sqrt(lambda_n)x_n dW_t + y_n(t)dW_t`,
`x_n(0)=0`.                                                   (1.1)

Set

`s=lambda_n t`,
`B_s=sqrt(lambda_n)W_{s/lambda_n}`,
`Z_s=sqrt(lambda_n)x_n(s/lambda_n)`,
`Y_s=y_n(s/lambda_n)`.                                       (1.2)

Brownian scaling gives the exact lambda-free SDE

`dZ_s=-Z_s ds+(Z_s+Y_s)dB_s`, `Z_0=0`.                       (1.3)

Moreover

`||u_n(t)||_{H^1}=sqrt(lambda_n)|x_n(t)|=|Z_{lambda_n t}|`,  (1.4)

and

`int_0^T E|y_n(t)|^3dt
 = (1/lambda_n) int_0^(lambda_n T) E|Y_s|^3ds`.              (1.5)

Thus one-shell scaled constructions are exact source constructions; there is no easier substituted operator here.

The P24 endpoint obstruction can already be read from the homogeneous part of (1.3). If `Y=0` after a nonzero pulse, then

`Z_s=Z_1 exp(-(3/2)(s-1)+(B_s-B_1))`,

and

`E(|Z_s|^p|F_1)=|Z_1|^p exp((p/2)(p-3)(s-1))`.              (1.6)

Hence the p-th moment decays for `p<3`, is conserved at `p=3`, and grows for `p>3`; high physical frequencies turn a fixed `T` into scaled horizon `lambda_nT`, proving endpoint failure at and above 3. This is the exact frozen source endpoint being preserved.

---

## 2. Essential recovered dependency: why the current full bracket is `[2/3,1]`

The exact subcritical stochastic-input norm recovered in the preceding chain is

`C_p^g(T)=R_p=1/(sqrt(2/(p-1))-1)`, `2<=p<3`,              (2.1)

with

`(3-p)R_p -> 4`.                                            (2.2)

The positive critical logarithmic estimate follows by optimizing the subcritical bound at each distribution scale. If `F=T_TY`, Chebyshev at exponent `p<3` gives

`s^(1/p)F^*(s) <= R_p ||Y||_p`.

On the finite measure space `Omega x (0,T)`, `||Y||_p <= T^(1/p-1/3)||Y||_3`. Writing `L=log(T/s)` and taking `3-p` proportional to `1/L` yields

`s^(1/3)F^*(s) <= C(1+L)||Y||_3`,                           (2.3)

so `T_T:L^3 -> Z_{3,1}(T)`.

Conversely, the earlier near-critical one-shell occupation witness showed that for every `alpha<2/3`, one can find source-valid progressive inputs for which

`||T_TY||_{Z_{3,alpha}(T)}/||Y||_3 -> infinity`.            (2.4)

Thus the genuine unresolved quantitative endpoint before this run is exactly

`alpha_*(T) in [2/3,1]`.                                    (2.5)

The present run attacks the lower boundary itself rather than repeating either argument.

---

## 3. New theorem: critical Doob–Hardy additive saturator

Work first in the exact scaled one-shell equation (1.3), writing the Brownian motion again as `W`:

`dZ_s=-Z_s ds+(Z_s+Y_s)dW_s`, `Z_0=0`.                     (3.1)

Define the critical stochastic exponential

`M_s=exp(W_s-3s/2)`.                                        (3.2)

Then Ito gives

`dM_s=-M_s ds+M_s dW_s`,                                   (3.3)

and, crucially,

`E M_s^3=E exp(3W_s-9s/2)=1`.                              (3.4)

Choose the progressive additive input

`Y_s=M_s`.                                                   (3.5)

This input does not depend on `Z` and uses no state feedback.

> **Theorem NM10-AVP3-CRITICAL-DOOB-HARDY-SATURATOR-07.**
> Fix `T>0`. For the exact frozen pair `(Lambda,Lambda^(1/2))`, there is a sequence of one-mode progressive additive inputs `g_n` with
> 
> `||g_n||_{L^3(Omega x (0,T);L^2)}^3=T`,                  (3.6)
> 
> and thresholds `R_n`, with output `F_n=||u_n||_{H^1}`, such that, writing
> `m_n=mu{F_n>R_n}`,
> 
> `liminf_n R_n^3 m_n / (lambda_n^2 T^3) >= 8/9`          (3.7)
> 
> in the equivalent scaled normalization made explicit below, and consequently for every `alpha>=0`,
> 
> `liminf_n (lambda_nT)^(alpha-2/3)
>   ||F_n||_{Z_{3,alpha}(T)}/||g_n||_3
>  >= (8/9)^(1/3)(2/9)^alpha`.                             (3.8)
> 
> In particular:
> 
> 1. every `alpha<2/3` fails, now by an explicit progressive additive input with no feedback;
> 2. at the critical exponent,
> 
> `liminf_n ||F_n||_{Z_{3,2/3}(T)}/||g_n||_3
>  >= 2^(5/3)/9 = 0.3527557893...`.                        (3.9)
> 
> Therefore, if the unresolved full endpoint estimate
> `T_T:L^3 -> Z_{3,2/3}(T)` is true, its norm is at least `2^(5/3)/9` under this normalization.

The theorem does **not** prove existence at `alpha=2/3`; it supplies a critical saturating family and a quantitative lower constant.

---

## 4. Exact factorization: the critical transform is elementary

Set

`H_s=Z_s/M_s`.                                              (4.1)

The product rule gives

`d(MH)=H dM+M dH+d[M,H]`.                                  (4.2)

If

`dH_s=dW_s-ds`,                                             (4.3)

then using (3.3),

`H dM+M dH+d[M,H]`

`=(-MH ds+MH dW)+(-M ds+M dW)+M ds`

`=-M H ds+M(H+1)dW`,                                       (4.4)

which is exactly (3.1) with `Y=M`. Since `H_0=0`,

`H_s=W_s-s`.                                                (4.5)

Therefore the solution is explicit:

`Z_s=M_s(W_s-s)
    =exp(W_s-3s/2)(W_s-s)`.                                (4.6)

This factorization explains why the witness is critical. The multiplier `M` is precisely the cubic exponential martingale, while the quotient acquires a deterministic drift of size one.

A useful more general identity, reserved for the next attack, is the following. If

`Y_s=M_s F_s`                                               (4.7)

for a progressive scalar `F`, then the same product calculation gives

`dH_s=F_s(dW_s-ds)`.                                       (4.8)

Under the p=3 exponential tilt with density proportional to `M_L^3`, Girsanov changes `W_s-3s` into Brownian motion, so (formally, and rigorously after finite-horizon localization)

`dH_s=F_s(dW_s^Q+2ds)`.                                   (4.9)

At the same time

`E_P int_0^L |M_sF_s|^3ds = E_Q int_0^L |F_s|^3ds`         (4.10)

when written with the consistent terminal-density/conditional-density version of the tilt. Thus the unresolved positive endpoint has a Hardy-martingale structure; `F=1` is the simplest extremizing direction. The theorem below uses only the explicit P-calculation (4.6), so no change-of-measure subtlety enters its proof.

---

## 5. Transfer to an exact source input on the torus

For eigenvalue `lambda_n`, set on the original physical interval `[0,T]`

`g_n(t)
 = exp(sqrt(lambda_n)W_t-(3/2)lambda_n t) phi_n`.           (5.1)

This is progressive and takes values in `X_{1/2}=L^2`. Under the scaling (1.2), it becomes exactly `Y_s=M_s`.

The input norm is exact:

`E ||g_n(t)||_2^3
 = E exp(3sqrt(lambda_n)W_t-(9/2)lambda_n t)
 = 1`,                                                       (5.2)

so

`||g_n||_3^3=T`.                                            (5.3)

The scalar coefficient of the solution is also explicit. From (4.6),

`x_n(t)=lambda_n^(-1/2)
 exp(sqrt(lambda_n)W_t-(3/2)lambda_n t)
 (sqrt(lambda_n)W_t-lambda_n t)`.                          (5.4)

Hence the source output amplitude is

`F_n(t):=||u_n(t)||_{H^1}
 = |Z_{lambda_n t}|`.                                       (5.5)

No asymptotic approximation has been introduced in either the operator or the source norm.

---

## 6. The critical Gaussian saddle

Let

`L_n=lambda_n T -> infinity`.                               (6.1)

Choose any deterministic sequence `K_n -> infinity` with

`K_n=o(sqrt(L_n))`,                                         (6.2)

and put

`r_n=L_n-K_n sqrt(L_n)`.                                    (6.3)

Then `r_n/L_n ->1`, `r_n>0` eventually, and

`(L_n-r_n)/sqrt(r_n) -> infinity`.                          (6.4)

Define the threshold

`R_n=2r_n exp(3r_n/2)`.                                     (6.5)

For scaled time `s>=r_n`, consider the event

`E_{n,s}={W_s >= (3/2)(s+r_n)}`.                            (6.6)

On this event,

`W_s-s >= s/2+3r_n/2 >=2r_n`,                              (6.7)

and

`W_s-3s/2 >=3r_n/2`.                                       (6.8)

Therefore from (4.6),

`Z_s >= 2r_n exp(3r_n/2)=R_n`.                             (6.9)

Let the scaled spacetime tail measure be

`m_n^sc=int_0^{L_n} P(|Z_s|>R_n) ds`.                      (6.10)

Then

`m_n^sc >= int_{r_n}^{L_n}
 barPhi( (3/2)(s+r_n)/sqrt(s) ) ds`.                        (6.11)

The exponent has the exact saddle identity

`[(3/2)(s+r)]^2/(2s)
 = (9/2)r + (9/8)(s-r)^2/s`.                               (6.12)

This is the decisive calculation. The rare-event cost is `exp(-9r/2)` at the saddle `s=r`, with a window of width `sqrt(r)`.

### 6.1 Exact saddle constant

Fix `K>0`. By (6.4), for all sufficiently large n the interval

`[r_n,r_n+K sqrt(r_n)]`

lies inside `[r_n,L_n]`. Make the change

`s=r_n+u sqrt(r_n)`, `0<=u<=K`.                             (6.13)

Set

`a_n(u)=(3/2)(s+r_n)/sqrt(s)`.                              (6.14)

Uniformly for `u` in a fixed compact interval, `a_n(u)->infinity`, and Mills' asymptotic gives

`barPhi(a_n(u))
 =(1+o(1)) phi(a_n(u))/a_n(u)`.                             (6.15)

By (6.12),

`a_n(u)^2/2
 = (9/2)r_n
   +(9/8)u^2 r_n/(r_n+u sqrt(r_n))`.                        (6.16)

Moreover

`sqrt(r_n)/a_n(u) -> 1/3`.                                 (6.17)

Hence dominated convergence on `[0,K]` yields

`lim_n e^{(9/2)r_n}
 int_{r_n}^{r_n+K sqrt(r_n)}
 barPhi((3/2)(s+r_n)/sqrt(s))ds`

`= (1/(3sqrt(2pi))) int_0^K exp(-9u^2/8)du`.               (6.18)

Now let `K->infinity`. Since

`int_0^infinity exp(-9u^2/8)du=sqrt(2pi)/3`,               (6.19)

we obtain

`liminf_n e^{(9/2)r_n}m_n^sc >=1/9`.                       (6.20)

Because

`R_n^3=8r_n^3 e^{(9/2)r_n}`,                               (6.21)

(6.20) implies

`liminf_n R_n^3 m_n^sc/r_n^3 >=8/9`.                       (6.22)

This is the exact constant checked symbolically and numerically in the accompanying checker.

---

## 7. Physical rearrangement transfer

The physical tail measure of the source output (5.5) is

`m_n:=mu{F_n>R_n}=m_n^sc/lambda_n`.                        (7.1)

For any threshold `R` and `m=mu{|F|>R}`, rearrangement monotonicity gives

`||F||_{Z_{3,alpha}(T)}
 >= R m^(1/3)/(1+log(T/m))^alpha`.                          (7.2)

Using (5.3), (7.1), and `L_n=lambda_nT`, the output/input ratio satisfies

`||F_n||_{Z_{3,alpha}(T)}/||g_n||_3`

`>= R_n (m_n^sc)^(1/3)
    / [L_n^(1/3)(1+log(L_n/m_n^sc))^alpha]`.               (7.3)

From (6.20),

`m_n^sc >= (1/9-o(1))e^{-(9/2)r_n}`.                       (7.4)

Consequently

`1+log(L_n/m_n^sc)
 <= (9/2)r_n+log(9L_n)+1+o(1)
 = (9/2+o(1))L_n`,                                         (7.5)

because `r_n/L_n->1`. Also (6.22) gives

`R_n(m_n^sc)^(1/3)
 >= (8/9-o(1))^(1/3)r_n`.                                  (7.6)

Substitution in (7.3) yields the quantitative asymptotic

`liminf_n L_n^(alpha-2/3)
 ||F_n||_{Z_{3,alpha}(T)}/||g_n||_3`

`>= (8/9)^(1/3)(2/9)^alpha`.                               (7.7)

For `alpha<2/3`, the right normalization says the unnormalized ratio diverges like at least `L_n^(2/3-alpha)`, so the endpoint estimate fails.

At `alpha=2/3`, (7.7) becomes

`liminf_n ||F_n||_{Z_{3,2/3}(T)}/||g_n||_3`

`>= (8/9)^(1/3)(2/9)^(2/3)
 = 2^(5/3)/9
 = 0.35275578932626656...`.                                (7.8)

This proves the theorem.

---

## 8. Why the `2/3` saddle is structurally critical

The choice of the affine barrier in (6.6) is not arbitrary. Suppose near a saddle at `s=r` we impose an affine barrier whose value there is `q r`. The Gaussian cost has exponent

`q^2 r/2`,                                                  (8.1)

while the cubic output threshold generated by `M_s(W_s-s)` has exponential contribution

`3(q-3/2)r`.                                                (8.2)

Critical cancellation requires

`3(q-3/2)=q^2/2`.                                           (8.3)

Equivalently,

`q^2-6q+9=0`,                                               (8.4)

so

`q=3`                                                        (8.5)

is the unique critical value. Requiring the affine Gaussian exponent itself to have its saddle at `s=r` makes the coefficients on `s` and `r` equal, hence the unique symmetric critical barrier is exactly

`W_s >= (3/2)(s+r)`.                                        (8.6)

Thus the `2/3` witness is not a numerically tuned accident: it is forced by matching the cubic exponential martingale with the Gaussian large-deviation saddle.

There is an equivalent Hardy interpretation. In the general transform `Y=MF`, cubic input energy becomes unweighted `L^3` energy under the critical exponential tilt, while the quotient `H` gains the drift term `2F dt`. For deterministic `F=1`, the drift grows like `t`, whereas the L3 input cost grows like `t^(1/3)`. Their ratio is `t^(2/3)`. This is precisely the logarithmic exponent detected by the physical rearrangement after the rare-event tilt is undone.

This route is genuinely different from the preceding deterministic proportional-feedback occupation theorem: the present control is additive, explicit, and independent of the state.

---

## 9. Essential checker and what it certifies

The accompanying checker

`2026-09-20T07-48-22+0300__critical_doob_saturator_check.py`

was executed before persistence. Its archived output is

`2026-09-20T07-48-22+0300__critical_doob_saturator_check.out`.

It verifies exactly:

1. the saddle identity (6.12);
2. `int_0^infinity exp(-9u^2/8)du=sqrt(2pi)/3`;
3. the limiting tail coefficient `1/9`;
4. the endpoint lower constant
   `(8/9)^(1/3)(2/9)^(2/3)=2^(5/3)/9`;
5. high-precision numerical convergence of the scaled finite-r Gaussian tail integral toward `1/9`.

The archived execution ends `CHECK_PASS`. The checker is a sanity certificate for the finite algebra/numerics; the theorem proof is the analytic argument above.

---

## 10. Literature boundary checked 20 September 2026

The source remains Agresti–Veraar, arXiv:2501.18561 / NoDEA 32 (2025), Problem 3. The currently recovered source asks whether stochastic maximal regularity at one exponent extrapolates to all `r>2`, or at least to a large range, under its exact source conventions.

The nearest verified later work remains different in scope:

- Bechtel–Veraar, published 11 July 2025, proves some `p>2` extrapolation in the variational setting under the symmetry/self-adjoint structure used there; it does not state the present exact critical rearrangement endpoint for the frozen nonsmall pair.
- Evangelopoulos-Ntemiris–Veraar, *Discrete stochastic maximal regularity*, published 13 February 2026, studies temporal numerical/discrete stochastic maximal regularity and extrapolation in that discrete framework.
- Evangelopoulos-Ntemiris, arXiv:2609.07436, submitted 7 September 2026, proves fully discrete stochastic maximal regularity and uniform `H^infinity`-calculus estimates for finite-element/time-discrete second-order elliptic operators.

A bounded current search did not locate a paper stating the explicit theorem above or settling the full `alpha_*(T)=2/3` endpoint for this exact nonsmall state-multiplicative pair. This is a dated bounded search, not a worldwide novelty certificate.

---

## 11. What changed and what did not

### Fixed source theorem

Before:

`r_*=3`, `p=3` excluded.

After:

`r_*=3`, `p=3` excluded.

No movement.

### Full critical rearrangement endpoint

Before:

`2/3 <= alpha_*(T) <=1`.

After:

`2/3 <= alpha_*(T) <=1`.

No movement.

### Demonstrated mechanism gain

Before this run, the `2/3` lower boundary was realized through near-critical state feedback and then shown sharp inside deterministic proportional-feedback controls.

After this run, there is an exact progressive **additive** source input

`g_n(t)=exp(sqrt(lambda_n)W_t-(3/2)lambda_n t)phi_n`,         (11.1)

with fixed cubic input norm and explicit output formula, which:

- reproduces the `alpha<2/3` obstruction without feedback;
- sits exactly at the `alpha=2/3` scale rather than decaying by an extra logarithm;
- forces the quantitative critical lower constant `2^(5/3)/9`;
- exposes a critical Doob/Girsanov-Hardy transform that is a plausible route to the missing positive endpoint.

That is substantive mechanism progress, but it is not a full solution of the parent extrapolation problem.

---

## 12. Residual obstruction and next attack

The most precise unresolved problem on this exact pair is now:

> Does there exist `C_T<infinity` such that every progressive source input `Y` satisfies
> 
> `||T_TY||_{Z_{3,2/3}(T)} <= C_T ||Y||_3`?                (12.1)

If yes, (7.8) gives a concrete lower bound on `C_T` under the present normalization. If no, a counterexample must exploit more than the deterministic `F=1` critical Hardy direction.

The next attack is therefore not another feedback optimization. Use the exact critical transform

`Y=MF`, `Z=MH`, `dH=F(dW-dt)`,                             (12.2)

and the p=3 tilted measure to seek a full arbitrary-progressive weighted Hardy-martingale inequality at logarithmic exponent `2/3`. The decisive issue is whether the cubic energy `int|F|^3` controls the occupation of the tilted martingale-plus-drift quotient uniformly enough to survive undoing the exponential tilt. If a scalar arbitrary-progressive theorem is obtained, the next question is whether it lifts over the self-adjoint spectrum without a dimension/frequency loss.

This run produced a strict mechanism gain, so the PROGRESS20 two-failed-recovery trigger for a T05 covariance/comparison pivot is **not** due.

---

## ledger_delta

A machine-readable ledger delta is saved beside this report as

`2026-09-20T07-48-22+0300__ledger_delta.json`.

Compact human summary:

- fixed strong endpoint: `3 -> 3`, endpoint excluded;
- exact subcritical norm preserved;
- full critical bracket: `[2/3,1] -> [2/3,1]`;
- source-level movement: none;
- new mechanism: critical Doob-Hardy explicit additive saturator;
- new quantitative fact: any finite `Z_{3,2/3}` endpoint norm is at least `2^(5/3)/9` under this normalization;
- status: PARTIAL / explicit source-valid witness theorem self-checked;
- next attack: arbitrary-progressive critical Hardy-martingale estimate, then spectral lift;
- T05 fallback: not due.
