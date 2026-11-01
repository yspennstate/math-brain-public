# T228: an explicit nonlinear SGD model with a nonzero teacher

Version 1, 23 October 2026. A09 extension and verification.

Source candidate: `campaign/proofs/T228_EXPLICIT_CLOSURE.md`, Version 1,
SHA256 `9d0ef065e10642dbc8967870bdc3f368300424659f9316456355775264133287`.
This document proves the extension rather than assuming that the zero-teacher
symmetry or input-label independence survives. It retains the existing T228
forward-excursion positivity mechanism, credited in Section 10.

## 1. Model and theorem

Fix

```text
δ = 1/1000,  σ(z) = z + δ tanh(z),
θ ∈ [−1,1],  η ∈ [99/100,101/100],  b = 1.
```

Let `(A_k,E_k)` be iid pairs of independent standard normal variables, set
`Y_k = σ(A_k θ) + E_k`, and use the unmodified squared sample loss and SGD map

```text
fθ(x;A,E) = (σ(Ax) − σ(Aθ) − E)²/2,
Ψθ(x) = x − η A σ'(Ax)(σ(Ax) − Y),
X_(k+1) = Ψθ,k(X_k).
```

The parameters are fixed along a trajectory. The labels are not independent of
the inputs when `θ ≠ 0`.

**Theorem.** For every such fixed `(η,θ)`:

1. The actual smooth random maps satisfy

   ```text
   E Lip(Ψθ) < q := 99010707/100000000 = 0.99010707 < 1.
   ```

   In particular they contract on average, including in the logarithmic sense.
   The maps are nonaffine almost surely.
2. There is exactly one invariant probability `π_(η,θ)`, including among laws
   without an assumed first moment. It has a finite first moment and, for every
   deterministic initial point `x`,

   ```text
   W₁(Law(X_n^x), π_(η,θ)) ≤ q^n W₁(δ_x, π_(η,θ)).
   ```

   Its support is all of `R`.
3. There is a unique positive solution `α = α(η)` of

   ```text
   hη(α) := E|1−ηA²|^α = 1,
   ```

   and `1 < α < 2`. The exponent is independent of the teacher `θ`.
4. There is a finite strictly positive constant `C_(η,θ)` such that

   ```text
   lim_(t→∞) t^α π_(η,θ)({x: |x|>t}) = C_(η,θ) ∈ (0,∞).
   ```

   The same limit and constant hold with `|x−θ|` in place of `|x|`. For `p>0`,
   both the `p`th absolute moment and the `p`th absolute estimation-error moment
   are finite exactly when `p<α`. Their second moments are infinite.

With `X∼π_(η,θ)` independent of the fresh pair `(A,E)`, the constant is

```text
C_(η,θ) = E[|Ψθ(X)|^α − |(1−ηA²)X|^α] /
          (α E[|1−ηA²|^α log|1−ηA²|]).                         (1)
```

The expectation in the numerator is an absolutely integrable coupled
difference. It is not a subtraction of two separately finite expectations.

For `θ=0`, the invariant law is symmetric and each one-sided tail has constant
`C_(η,0)/2`. **No one-sided tail limit or equality of one-sided constants is
asserted here for a fixed nonzero teacher.** In fact the stationary law for a
nonzero teacher is not symmetric about zero; Section 9 proves this directly.

The concrete choice `θ=1, η=1` is a nonzero-signal example covered by the
theorem. The contraction bound is uniform on the stated rectangle; no uniform
lower bound on `C_(η,θ)` is claimed.

## 2. Actual derivative, label dependence, and uniform remainder

Write `z=Ax`, `t=tanh(z)`, and `u=sech²(z)`. Then

```text
σ'(z)=1+δu,   σ''(z)=−2δut,
Ψθ'(x)=1−ηA² H(z,Y),
H(z,Y)=(1+δu)²−2δut(z+δt−Y).
```

Since `|t|≤1`, `0≤u≤1`, and `|z|u≤1`, expansion gives

```text
|H−1|
≤ 2δu + δ²u² + 2δ|z|u|t| + 2δ²u t² + 2δu|t||Y|
≤ 4δ + 3δ² + 2δ|Y|.
```

For example, `|z|u≤1` follows from
`cosh²(z)=1+sinh²(z)≥1+z²≥|z|`. Consequently, with

```text
M=1−ηA²,  ξ=|M|,
Lθ=ξ+ηA²(4δ+3δ²+2δ|Y|),
```

the mean value theorem on the whole real line yields

```text
Lip(Ψθ) ≤ Lθ.                                                  (2)
```

This is a bound on the actual global Lipschitz constant of the nonlinear map.
It is not merely a bound on its asymptotic multiplier.

The changed mixed label moment must keep the dependence between `A` and `Y`.
Using `|tanh v|≤|v|`,

```text
|Y| ≤ (1+δ)|θ||A| + |E|,
E[A²|Y|]
≤ (1+δ)|θ| E|A|³ + E[A²|E|]
= (1+δ)|θ|·2√(2/π) + √(2/π)
≤ (3+2δ)√(2/π) < 3+2δ = 3.002.                               (3)
```

Only the second summand uses independence, namely independence of `A` and
the additive noise `E`. No factorization of `E[A²|Y|]` is made.

For the remainder, the exact identity

```text
σ'(z)(σ(z)−Y)=z+δzu+(1+δu)(δt−Y)
```

implies

```text
Ψθ(x)=Mx+Rθ(x),
sup_(x∈R)|Rθ(x)| ≤ Bθ := η|A|[δ+(1+δ)(δ+|Y|)].                (4)
```

In particular, uniformly on the parameter rectangle,

```text
Bθ ≤ (101/100)|A|[δ+(1+δ)(δ+(1+δ)|A|+|E|)].
```

Both `Bθ` and `Lθ` have moments of every positive order. Their envelopes are
polynomials in `|A|` and `|E|`; the same is true of the label envelope. Neither
`Bθ` nor `Y` needs to be independent of `M`.

The sample map is genuinely nonlinear. At zero its derivative is
`1−ηA²(1+δ)²`, whereas its derivative tends to `1−ηA²` as `|x|→∞`
whenever `A≠0`; the terms containing `u` or `zu` vanish. These two values
differ for every `A≠0`, an event of probability one.

## 3. Exact contraction arithmetic and the exponent

Let `φ` be the standard normal density. Splitting at `|A|=1`, and using
`(aφ(a))'=(1−a²)φ(a)`, gives

```text
E|1−A²| = 4φ(1) = 4/√(2πe) < 97/100.
```

This strict inequality needs no quadrature: `π>157/50` and `e>1359/500`
give

```text
(97/100)² · 2(157/50)(1359/500) − 16
= 7532467/125000000 > 0.
```

The pointwise inequality
`|1−ηA²|≤|1−A²|+|η−1|A²` now yields `Eξ<98/100`.
Combining this with (2)–(3) and `EA²=1`,

```text
E Lip(Ψθ) ≤ E Lθ
< 98/100 + (101/100)[4/1000 + 3/10^6 + (2/1000)(1501/500)]
= 98/100 + (101/100)(10007/10^6)
= 99010707/10^8
= 0.99010707 < 1.                                             (5)
```

The margin is exactly `1−q=989293/10^8=0.00989293`. Jensen gives
`E log Lip(Ψθ)≤log E Lip(Ψθ)<log q<0`, with an extended negative
expectation also sufficient. The envelope itself has a finite negative log
expectation: putting `c₀=4δ+3δ²<1`, one has
`Lθ≥|1−ηA²|+c₀ηA²≥c₀`, while `log⁺Lθ≤Lθ`.

The distribution of `M=1−ηA²` is absolutely continuous. Its only zeros as a
function of `A` are `±η^(−1/2)`, where the derivative is nonzero. Hence

```text
P(ξ=0)=0,
E|log ξ|<∞,
E[ξ^p |log ξ|]<∞  for every p>0.
```

Local logarithmic integrability proves the assertions near the two roots;
Gaussian decay proves them at infinity. The law of `log ξ` is absolutely
continuous and thus nonarithmetic. Jensen also gives
`E log ξ≤log Eξ<0`.

The function `hη(p)=Eξ^p` is finite for all `p≥0`, has strictly convex
logarithm, and satisfies

```text
hη(0)=1,   hη(1)<0.98<1,
hη(2)=1−2η+3η² ≥ 1−2(99/100)+3(99/100)²
                    =19603/10000=1.9603>1.
```

The last inequality uses that the polynomial is increasing on the chosen
interval. Moreover `P(ξ>1)>0`, so `hη(p)→∞` as `p→∞`.
Strict log-convexity gives exactly one positive root `α∈(1,2)`, with
`hη(p)<1` for `0<p<α`. Its tilted logarithmic mean

```text
mα := E[ξ^α log ξ]
```

is finite and positive. Positivity follows, for example, by comparing the
derivative of `log hη` at `α` to its strictly positive secant slope from
`p=1` to `p=α`. All these quantities depend on `η` and not on `θ`.

## 4. Invariance, uniqueness, convergence, and lower moments

At zero,

```text
Ψθ(0)=η(1+δ)A Y,
E|Ψθ(0)|<∞.
```

Fresh-step coupling and (5) contract Wasserstein distance of order one by
at most `q`. The Markov operator maps the complete space of probability
laws with finite first moment into itself. The contraction mapping theorem
therefore supplies an invariant law `π=π_(η,θ)` in that space and the
displayed geometric convergence bound.

To remove a possible hidden moment restriction from uniqueness, couple a
chain from any finite random initial value `Z` with a chain from zero, using
the same independent fresh steps. Then

```text
|X_n^Z−X_n^0| ≤ |Z| ∏_(j=1)^n Lθ,j → 0  almost surely.
```

Indeed the expectation of the product is `(ELθ)^n≤q^n`; Markov's inequality
and Borel–Cantelli show that the product tends to zero. If `Z` had any
invariant probability law, bounded Lipschitz test functions and dominated
convergence would identify it with `π`. No moment of `Z` is used.

For every `0<p<α`, (4) gives a moment drift. For `p≤1`,

```text
E|Ψθ(x)|^p ≤ hη(p)|x|^p + E Bθ^p.
```

For `p>1`, use
`(a+b)^p≤(1+ε)a^p+C_(p,ε)b^p`, choosing `ε>0` so that
`r_p=(1+ε)hη(p)<1`. Thus in both cases

```text
E|Ψθ(x)|^p ≤ r_p |x|^p + d_p,    r_p<1, d_p<∞.
```

The chain started from zero has uniformly bounded `p`th moments. Its weak
convergence to `π` and the lower semicontinuity of `|x|^p` imply
`Eπ|X|^p<∞`.

## 5. Changed conditional mean and explicit compact minorization

Conditional on `A=a`, the fresh additive noise remains standard normal and

```text
Ψθ(x) = μθ(x,a) + η a σ'(ax) E,
μθ(x,a)=x−η a σ'(ax)[σ(ax)−σ(aθ)].                            (6)
```

This conditional mean includes the teacher term. For `a∈[1,2]`, `|x|≤R`,
and all permitted parameters, its absolute value is at most

```text
D_R := R + 4(101/100)(1+δ)²(R+1),
```

because `|σ(v)|≤(1+δ)|v|`. The conditional standard deviation is in

```text
[s_min,s_max] := [99/100, 2(101/100)(1+δ)].
```

For any finite `R,T>0`, the conditional density at every `|y|≤T` is
therefore at least

```text
d_(R,T) := [s_max√(2π)]^(-1)
           exp(−(T+D_R)²/(2s_min²)) > 0.
```

After integrating over `a∈[1,2]`, with
`ε_(R,T):=P(1≤A≤2)d_(R,T)>0`, one obtains

```text
Pθ(x,F) ≥ ε_(R,T) Leb(F∩[−T,T]),   |x|≤R.                    (7)
```

In particular every nonempty open interval has positive transition
probability from every point. Stationarity then gives it positive `π` mass.
The support of `π` is the whole real line. This check also supplies the
uniform compact-to-annulus transition used in the positivity proof.

## 6. Exact absolute-tail limit and its integrable-difference formula

Use Jelenković–Olvera-Cravioto, *Implicit Renewal Theory and Power Tails on
Trees*, [arXiv:1006.3295v5](https://arxiv.org/abs/1006.3295v5), Theorem 3.1,
printed page 5 of the [primary PDF](https://arxiv.org/pdf/1006.3295).
Its `N=1` specialization applies to `R₀=|X|`, `C₁=ξ`, independent by
construction. It is the general discrepancy theorem, not an assertion
restricted to affine fixed-point equations.

The full hypothesis checklist is:

| Renewal input | Verification in this model |
|---|---|
| Nonnegative coefficient, positive with positive probability | `ξ>0` almost surely. |
| Nonarithmetic logarithmic coefficient | `log ξ` has an absolutely continuous law, Section 3. |
| `Eξ^α=1` | Definition and uniqueness of `α`, Section 3. |
| `0<E[ξ^α log ξ]<∞` | The positive finite number `mα`, Section 3. |
| `Eξ^γ<∞` for some `0≤γ<α` | Take `γ=0`; the expectation is one. |
| Independence of `R₀` and `ξ` | The stationary input is chosen independently of the fresh step. |
| `ER₀^p<∞` for all `0<p<α` | Section 4. |
| Weighted absolute discrepancy is integrable | The coupled bound immediately below. |

Set `U=|Ψθ(X)|` and `W=|MX|=ξ|X|`. Stationarity gives `U` the law of
`R₀`, and (4) gives `|U−W|≤Bθ`. Tonelli's theorem gives

```text
∫₀∞ t^(α−1)|P(R₀>t)−P(ξR₀>t)|dt
≤ E|U^α−W^α|/α.
```

Since `1<α<2`, the mean value theorem and subadditivity at exponent `α−1`
give the explicit envelope

```text
|U^α−W^α|
≤ α Bθ(W+Bθ)^(α−1)
≤ α[Bθ^α + Bθ ξ^(α−1)|X|^(α−1)].                            (8)
```

The right side is integrable: the stationary moment of order `α−1` is
finite, `X` is independent of the step, and `E[Bθ ξ^(α−1)]<∞` follows
from the polynomial Gaussian envelopes. The latter is a joint moment;
independence of `Bθ` and `ξ` is neither asserted nor needed.

The cited theorem yields a limit `C_(η,θ)∈[0,∞)`. Applying signed Fubini to
the same absolutely integrable coupled difference gives formula (1). The
argument has not yet established strict positivity, which is proved next.

## 7. Strict positivity with the nonzero-teacher joint coefficient law

All the bounds below use `Bθ` from (4), including its teacher-dependent
label. The full steps `(A_j,E_j)` are iid, so their images `(ξ_j,Bθ,j)`
are iid. Within a pair the two components can be dependent. In this scalar
model no rotation argument or teacher symmetry is used to obtain iid pairs.

### 7.1. Forward radial inequality and joint tilt

Put

```text
S₀=0,  S_n=Σ_(j=1)^n log ξ_j,
V_n=Σ_(j=1)^n exp(−S_j)Bθ,j.
```

Repeated reverse triangle inequalities give, pathwise,

```text
|X_n| ≥ exp(S_n)(|X₀|−V_n).                                  (9)
```

Tilt the law of each complete step by `ξ^α` and call the iid product law
`Q`. This is a probability law because `Eξ^α=1`. On the first `n` complete
steps its density relative to the original law `P` is `exp(αS_n)`.
For a stopping time `τ` and a stopped event `F`, summing over `{τ=n}` gives

```text
P(F,τ<∞)=E_Q[exp(−αS_τ) 1_{F,τ<∞}].                         (10)
```

No infinite-path absolute continuity or uniform-integrability claim is
needed. Under `Q`, the increment `Z=log ξ` satisfies
`E_Q|Z|<∞`, `E_QZ=mα>0`. Thus `S_n→∞` almost surely under `Q`.

Fix `β=1/2`. Since `1<α<2`,

```text
r := E_Q exp(−βZ)=hη(α−β)<1.                                 (11)
```

### 7.2. A positive survival probability

The process `exp(−βS_n)` is a nonnegative supermartingale under `Q`.
Stopping at the first time an independent walk reaches `(-∞,−1]`, truncated
at time `n`, gives

```text
Q(inf_(n≥0) S_n ≤ −1) ≤ exp(−β).
```

Because `Q(Z>1)>0`, a first increment above one followed by a fresh walk
that never reaches `−1` proves

```text
p₊ := Q(S_j>0 for every j≥1)
≥ p₀ := Q(Z>1)(1−exp(−β)) > 0.                              (12)
```

The event `Z>1` has positive probability because the Gaussian input is
unbounded and the tilt has a strictly positive density where `ξ>0`.

### 7.3. Uniformly tight overshoots

Let `τ_u=inf{n≥1:S_n>u}` for `u≥0` and `O_u=S_(τ_u)−u`.
The positive drift makes `τ_u` finite `Q`-almost surely. Chernoff's bound
and (11) give

```text
Σ_(n≥0) Q(S_n≤1) ≤ K_U := exp(β)/(1−r).
```

If `I=(a,a+1]` and `ν_I` is its first entry time, then, conditional on
`S_(ν_I)∈I`, a later visit to `I` entails a fresh-walk displacement at most
one. The strong Markov property therefore gives the translated occupation
bound

```text
U(I):=Σ_(n≥0)Q(S_n∈I)≤K_U.
```

Partitioning `(-∞,u]` into `(u−k−1,u−k]`, and dropping the restriction of
no earlier crossing, now gives, for `z≥0`,

```text
Q(O_u>z)
≤ Σ_(n≥1) E_Q[1_{S_(n−1)≤u} Q(Z>u+z−S_(n−1))]
≤ K_U Σ_(k≥0)Q(Z>z+k)
≤ K_U[Q(Z>z)+∫_z∞Q(Z>v)dv] → 0.                            (13)
```

The final bound is independent of `u` and tends to zero because `E_QZ⁺`
is finite.

### 7.4. Summable discounted teacher-dependent remainders

Using subadditivity at exponent `β=1/2` and then independence of a step
from its past,

```text
E_Q[(Σ_(j≥1)e^(−S_j)Bθ,j)^β]
≤ Σ_(j≥1) r^(j−1) E_Q[ξ^(−β)Bθ^β]
= E_P[ξ^(α−β)Bθ^β]/(1−hη(α−β)) < ∞.                        (14)
```

The numerator is the correct joint moment. It is finite because `α−β>0`
and both factors have all positive polynomial moments under `P`; there is
no inverse-multiplier singularity. Thus
`V_∞=Σ_(j≥1)e^(−S_j)Bθ,j<∞` almost surely under `Q`.

### 7.5. Excursions and the finite-stopping-time likelihood ratio

Choose `z≥0` so that the supremum in (13) is at most `p₀/4`, then choose
`K≥1` so that `Q(V_∞>K/2)≤p₀/4`. These choices are made before the
tail threshold `t`.

For `t>4K`, set `u=log(t/K)` and use the stopped event

```text
F_u={τ_u<∞, S_j>0 for 1≤j≤τ_u, V_(τ_u)≤K/2, O_u≤z}.
```

The union bound, (12), and the two preceding choices show
`Q(F_u)≥p₀/2`. On this event, for every initial point with
`2K≤|y|≤4K`, (9) implies

```text
|X_j| ≥ (3K/2)e^(S_j)>K  for 1≤j≤τ_u,
|X_(τ_u)| > (3K/2)(t/K) > t.
```

Thus it forces a hit of `D_t={|x|>t}` before the central interval
`C=[−K,K]`. On `F_u`, `S_(τ_u)≤u+z`. Equation (10) consequently gives

```text
inf_(2K≤|y|≤4K) P_y(τ_(D_t)<τ_C)
≥ (p₀/2)e^(−αz)(K/t)^α.                                    (15)
```

The hitting times in (15) start at time one; the initial annulus lies
outside both sets. Under `P`, `τ_u` need not be almost surely finite;
equation (10) already restricts to its finite-crossing event.

### 7.6. Stationary last-exit transfer

For disjoint Borel sets `C,D`, let `τ_C^+=inf{n≥1:X_n∈C}`. In a
stationary chain, the events specifying the last visit to `C` before time
`N`, among paths with `X_N∈D`, are disjoint. Consequently

```text
π(D)
≥ ∫_C π(dx) Σ_(j=1)^N P_x(X_j∈D, j<τ_C^+)
→ ∫_C π(dx) E_x[Σ_(j≥1)1_{X_j∈D,j<τ_C^+}]
≥ ∫_C π(dx) P_x(τ_D<τ_C^+).                                 (16)
```

The limit uses monotone convergence. This is an unnormalized stationary
integral; no return-time or regeneration factor is omitted.

Take `C=[−K,K]` and `J={2K≤|y|≤4K}`. Equation (7) with `R=K,T=4K`
gives

```text
inf_(x∈C) Pθ(x,J) ≥ δ_K := 4K ε_(K,4K)>0.
```

The Markov property at the first step, followed by (15), gives for `x∈C`

```text
P_x(τ_(D_t)<τ_C^+)
≥ δ_K(p₀/2)e^(−αz)K^α t^(−α).
```

Full support yields `π(C)>0`. Applying (16) therefore proves

```text
π(D_t) ≥ c_(η,θ) t^(−α),
c_(η,θ):=π(C)δ_K(p₀/2)e^(−αz)K^α>0,  t>4K.
```

Together with Section 6, this establishes `C_(η,θ)≥c_(η,θ)>0`.

## 8. Exact moment threshold and the nonzero-signal example

For a nonnegative random variable `R` and `p>0`,
`ER^p=p∫₀∞t^(p−1)P(R>t)dt`. The strictly positive tail limit makes
the integral diverge for every `p≥α`; Section 4 proves finiteness below
`α`. A bounded translation preserves the limit, since for `t>|θ|`,

```text
P(|X|>t+|θ|) ≤ P(|X−θ|>t) ≤ P(|X|>t−|θ|).
```

Thus the same constant and moment threshold describe estimation error.

For the explicit nonzero teacher `θ=1`, the labels are
`Y=A+δ tanh(A)+E`. They contain a nonconstant input-dependent signal, with

```text
E[AY]=1+δ E[A tanh(A)]>1.
```

More generally the population risk has the unique minimizer `θ`:

```text
Fθ(x)=E fθ(x;A,E)
     =1/2+(1/2)E[σ(Ax)−σ(Aθ)]²
     ≥1/2+(1/2)(x−θ)².
```

The inequality uses `σ'≥1` and `EA²=1`, and equality at `x=θ` proves
uniqueness of the minimizer. Thus `θ=1` is a genuine nonzero regression
teacher, not a renamed zero-signal model.

At the concrete learning rate `η=1`, the same exact arithmetic sharpens
(5) to

```text
E Lip(Ψ₁) < 97/100 + 10007/10^6 = 0.980007,
h₁(1)=4/√(2πe)<0.97,  h₁(2)=2.
```

Its stationary estimation error has the strictly positive exact tail
`t^(−α(1))`, where `α(1)∈(1,2)` is the unique solution of
`E|1−A²|^α=1`.

## 9. What symmetry does and does not survive

The exact reflection identity is

```text
Ψ_(−θ,A,−E)(−x)=−Ψ_(θ,A,E)(x).
```

Because the additive noise is symmetric and the invariant law is unique,
`π_(η,−θ)` is the reflection of `π_(η,θ)`. At `θ=0` this makes one law
symmetric and gives both one-sided constants `C_(η,0)/2`. It also gives
`C_(η,−θ)=C_(η,θ)` for the absolute tails. At fixed `θ≠0`, reflection
changes the model parameter; it is not a symmetry of that model.

One can even rule out exact symmetry about zero when `θ≠0`. Stationarity
and the finite first moment imply

```text
0=E[A σ'(AX)(σ(AX)−σ(Aθ))],                                 (17)
```

after averaging out the fresh mean-zero additive noise. Both terms are
integrable by `σ'≤1+δ`, `|σ(v)|≤(1+δ)|v|`, and `Eπ|X|<∞`.
If `π` were symmetric, the expectation of
`A σ'(AX)σ(AX)` would be zero, because its integrand is odd in `X` for
each fixed `A`. The other term
`A σ'(AX)σ(Aθ)` has the strict sign of `θ` almost surely when `A≠0`.
This contradicts (17). Thus the nonzero-teacher invariant law is not
symmetric about zero. Equal asymptotic one-sided constants would require
a separate signed-tail argument and are not inferred here from the
absolute-tail theorem.

## 10. Exact checks, provenance, and scope

The exact rational checks were executed with Python `fractions.Fraction`:

| Quantity | Exact value |
|---|---|
| Conservative mixed-label bound | `3+2δ=1501/500=3.002` |
| Derivative perturbation after expectation | `4δ+3δ²+2δ(3+2δ)=10007/10^6=0.010007` |
| Uniform contraction bound | `99010707/10^8=0.99010707` |
| Contraction margin | `989293/10^8=0.00989293` |
| Bound at `η=1` | `980007/10^6=0.980007` |
| Minimum of `hη(2)` on the interval | `19603/10000=1.9603` |
| Squared rational normal-bound margin | `7532467/125000000>0` |

These arithmetic checks support the displayed exact identities; no numerical
simulation or quadrature substitutes for a probability argument.

The forward tilted-walk and stationary last-exit mechanism comes from the
existing T228 work of `claude-b1e26540`, specifically
`rows/T228/claude_b1e26540/T3_STEP3.md` (local supplied copy:
`a01/claude_b1e26540/T3_STEP3.md`). This document rechecks it with the changed
`Y`, `Bθ`, complete-step tilt, and conditional Gaussian mean. It adds a
direct exponential-supermartingale proof of a positive survival probability
and spells out the stopped change of measure and finite-horizon last-exit
sum. No discovery credit is reassigned.

The sole external exact-tail theorem used here is the cited
Jelenković–Olvera-Cravioto Theorem 3.1, checked directly in its primary arXiv
PDF; the arXiv HTML renders the same statement as Theorem 2 in Section 3.
The main source candidate and its earlier T228 sources are credited for
the original example and proof strategy. This extension establishes a
concrete nonzero-teacher parameter regime. It does not assert a theorem
for arbitrary step sizes, arbitrary nonlinear networks, or first-in-the-
literature priority.

