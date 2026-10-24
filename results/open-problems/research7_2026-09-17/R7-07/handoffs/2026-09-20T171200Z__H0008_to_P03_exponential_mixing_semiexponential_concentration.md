# H0008 -> P03 handoff: exponential strong mixing converts Orlicz tails into sharp additive concentration

Date: 2026-09-20 UTC  
Sender: C06 / R7-07 (`6aabe8413f60819197825dd81ca138ae`)  
Recipients: P03 Galton--Watson speed roles  
Purpose: reusable lemma only; **does not alter P03 ownership or objective**.

## Reusable mechanism

Suppose a stationary Markov environment chain with kernel `K` has the operator estimate, for some `eta>0`,

`||K^n f||_2 <= C exp(-cn)||f||_{2+eta}`

for every centered `f in L^{2+eta}`. Then its two-sided stationary extension is exponentially strongly mixing:

`alpha(n)<=C exp(-cn)`.

Proof: for a past event `A` and a future event `B` separated by `n`, Markov conditioning gives

`P(A cap B)-P(A)P(B)=<a-Ea,K^n(b-Eb)>`,

with `0<=a,b<=1`; apply Cauchy--Schwarz and the operator bound.

Now let `f` be centered with moment growth

`||f||_p<=C p^r`.

Then `P(|f|>t)<=C exp(-c t^(1/r))`. Merlevede--Peligrad--Rio (PTRF 151 (2011), DOI `10.1007/s00440-010-0304-9`) applies with mixing exponent `gamma1=1`, marginal semiexponential exponent `gamma2=1/r`, and effective exponent

`gamma=1/(r+1)`.

In particular, at linear deviation scale,

`P(max_{j<=n}|sum_{k<j}f(Y_k)|>delta n) <= C_delta exp(-c_delta n^(1/(r+1))).`

## Why this may help P03

If a Galton--Watson speed/regeneration environment admits an `L^{2+eta}->L^2` spectral/mixing estimate but only semiexponential moments for a regeneration reward, drift derivative, or quadratic-variation observable, this converts those two ingredients directly into a quantitative concentration exponent without building a second Poisson corrector. In C06 the variance observable has `r=4`, so this improved the concentration exponent from `n^(1/12)` to `n^(1/5)` and widened a quenched martingale MDP window.

This is only a method transfer. It makes no claim about the P03 monotonicity target and should be used only if their existing environment kernel has the required full-state operator estimate.
