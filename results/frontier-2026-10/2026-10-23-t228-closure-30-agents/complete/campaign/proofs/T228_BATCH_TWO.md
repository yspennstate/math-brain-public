# T228: an explicit batch-two nonlinear Gaussian regression regime

Version 1, 23 October 2026. A22 author proof.

**Status: author proof awaiting independent audit.** This file is not an
independent acceptance or a registry closure. The planned independent audit
is A29.

Source: `campaign/proofs/T228_NONZERO_TEACHER.md`, Version 1, SHA256
`f95fa6fade82ba0dca4dab8e311fc61bb57b3267f3953b465c94228cb1315933`.
The present proof changes the batch size and learning-rate interval. It
rechecks the resulting multiplier, actual derivative, conditional Gaussian
transition, and complete-step joint law. The radial renewal and excursion
arguments retain the provenance stated in Section 10.

## 1. Averaged loss, fresh batch law, and theorem

Fix

```text
δ=1/1000,  σ(z)=z+δ tanh(z),  θ∈[−1,1],
b=2,      η∈[11/10,6/5].
```

For each step k, draw the complete batch

```text
W_k=(A_(k,1),E_(k,1),A_(k,2),E_(k,2)),
```

with all four entries independent standard normal variables. The batches
are iid across k and independent of the initial state. Set
`Y_(k,i)=σ(A_(k,i)θ)+E_(k,i)`. Thus the two input-label pairs are iid,
but each label is dependent on its own input when `θ≠0`.

The loss is the average of two unmodified squared sample losses:

```text
fθ(x;A,E) = (σ(Ax)−σ(Aθ)−E)²/2,
fbarθ,2(x;W) = [fθ(x;A₁,E₁)+fθ(x;A₂,E₂)]/2,
Ψθ,2(x) = x−(η/2)Σ_(i=1)^2 Aᵢ σ'(Aᵢx)[σ(Aᵢx)−Yᵢ],
X_(k+1) = Ψθ,2,k(X_k).
```

This is one simultaneous gradient update using the averaged batch loss,
not a composition of two batch-one updates. Parameters remain fixed along
a trajectory. Define

```text
T=(A₁²+A₂²)/2 ∼ Exp(1),
M=1−ηT=1−(η/2)(A₁²+A₂²),   ξ=|M|,
h_(η,2)(p)=Eξ^p=∫₀∞ |1−ηt|^p e^(−t)dt,
q₂=2170021/2500000=0.8680084<1.
```

**Theorem.** For every fixed permitted `(η,θ)`:

1. The actual smooth random maps are nonaffine almost surely and satisfy
   `E Lip(Ψθ,2)<q₂`. In particular, their mean logarithmic Lipschitz
   constant is finite and negative.
2. There is exactly one invariant probability law `π_(η,θ,2)`, including
   among laws without any assumed moment. It has full support on `R` and
   a finite first moment. For every deterministic initial state x,

   ```text
   W₁(Law(X_n^x),π_(η,θ,2))
   ≤ q₂^n W₁(δ_x,π_(η,θ,2)).
   ```

3. The equation `h_(η,2)(α)=1` has exactly one positive solution,
   `α=α(η,2)∈(1,2)`. It does not depend on θ.
4. There is a finite strictly positive constant `C_(η,θ,2)` such that

   ```text
   lim_(t→∞) t^α π_(η,θ,2)({x:|x|>t}) = C_(η,θ,2)∈(0,∞).
   ```

   The same limit and constant hold with `|x−θ|` in place of `|x|`.
   For p>0, the stationary pth absolute moment and pth absolute
   estimation-error moment are finite exactly when `p<α`. Both second
   moments are infinite.

With `X∼π_(η,θ,2)` independent of the fresh complete batch W, the constant is

```text
C_(η,θ,2)
= E[|Ψθ,2(X)|^α−|MX|^α] / (α E[ξ^α log ξ]).                 (1)
```

The numerator is an absolutely integrable coupled difference; its terms
are not separately integrable. A concrete nonzero-teacher example is
`θ=1, η=6/5, b=2`, with the same nonlinear activation and the same
standard Gaussian input and additive-noise distributions as the batch-one
source. No positive lower bound uniform in the parameters is asserted
for the tail constant.

## 2. The actual derivative and the dependent-label moment

For `z=Aᵢx`, put `t=tanh(z)` and `u=sech²(z)`. Direct differentiation gives

```text
σ'(z)=1+δu,  σ''(z)=−2δut,
H(z,Y)=(1+δu)²−2δut(z+δt−Y),
Ψθ,2'(x)=1−(η/2)Σ_(i=1)^2 Aᵢ² H(Aᵢx,Yᵢ).
```

Using `|t|≤1`, `u≤1`, and `|z|u≤1`, expand H to obtain

```text
|H(z,Y)−1| ≤ 4δ+3δ²+2δ|Y|.
```

The bound `|z|u≤1` follows from
`cosh²(z)=1+sinh²(z)≥1+z²≥|z|`. Therefore the global mean value theorem
gives

```text
Lip(Ψθ,2) ≤ Lθ,2
:= ξ+(η/2)Σ_(i=1)^2 Aᵢ²[4δ+3δ²+2δ|Yᵢ|].                  (2)
```

Every input-label mixed moment is evaluated with its dependence retained:

```text
|Yᵢ|≤(1+δ)|θ||Aᵢ|+|Eᵢ|,
E[Aᵢ²|Yᵢ|]
≤(1+δ)|θ| E|Aᵢ|³+E[Aᵢ²|Eᵢ|]
=[2(1+δ)|θ|+1]√(2/π)
≤(3+2δ)√(2/π)<3+2δ=1501/500.                              (3)
```

The equality in the second term uses independence of Aᵢ and Eᵢ, not
independence of Aᵢ and Yᵢ. Taking expectations of the sum in (2) requires
only its identical marginal sample laws; it does not factor a label from
its input. Since `EAᵢ²=1`,

```text
E Lθ,2 < h_(η,2)(1)+η[4δ+3δ²+2δ(3+2δ)]
        = h_(η,2)(1)+η(10007/10^6).                         (4)
```

## 3. Exact contraction certificate and the changed exponent

The normal joint density in polar coordinates gives
`P((A₁²+A₂²)/2>t)=e^(−t)` for t≥0. Thus T really has the unit-rate
exponential law. Integrating its positive part gives

```text
h_(η,2)(1)=E(1−ηT)+2E(ηT−1)_+
          =1−η+2ηe^(−1/η).                                 (5)
```

This expression is strictly increasing throughout the required interval.
Indeed,

```text
d/dη h_(η,2)(1)=−1+2e^(−1/η)(1+1/η)
              >−1+2(1/3)(11/6)=2/9>0.                    (6)
```

Here `η>1` implies `e^(−1/η)>e^(−1)>1/3`, while `η≤6/5` implies
`1+1/η≥11/6`. The elementary inequality `e<3` follows by comparing
the exponential series from k=2 onward with
`1/k!≤1/2^(k−1)`, with strict inequality for k≥3.

The following exact Taylor lower bound avoids any numerical quadrature:

```text
e^(5/6)>Σ_(k=0)^4 (5/6)^k/k!=71449/31104>25/11,
71449/31104−25/11=8339/342144>0.
```

Consequently `e^(−5/6)<11/25`, and (5)–(6) imply

```text
h_(η,2)(1)≤h_(6/5,2)(1)
         =−1/5+(12/5)e^(−5/6)
         <−1/5+(12/5)(11/25)=107/125.                       (7)
```

Combining (4) and (7) yields the exact uniform certificate

```text
E Lip(Ψθ,2)≤E Lθ,2
<107/125+(6/5)(10007/10^6)
=2170021/2500000=q₂<1,
1−q₂=329979/2500000=0.1319916.                              (8)
```

For p=2, use `ET=1` and `ET²=2`:

```text
h_(η,2)(2)=1−2η+2η²
          ≥1−2(11/10)+2(11/10)²
          =61/50>1.                                        (9)
```

The polynomial is increasing on this interval because `4η−2>0`.
The density of ξ on x>0 is

```text
gη(x)=(1/η)e^(−(1+x)/η)
      +1_(0<x<1)(1/η)e^(−(1−x)/η).                         (10)
```

It is bounded near zero and has an exponential tail. Hence ξ>0 almost
surely, `E|log ξ|<∞`, and `E[ξ^p|log ξ|]<∞` for every p>0.
The law of `log ξ` is absolutely continuous and therefore nonarithmetic.
Also `E log ξ≤log Eξ<0`.

The function `log h_(η,2)(p)` is strictly convex because ξ is nonconstant.
It is finite for every p≥0, equals zero at p=0, is negative at p=1 by
(7), and is positive at p=2 by (9). Strict convexity, together with
`P(ξ>1)>0`, gives a unique positive root α in (1,2), with `h_(η,2)(p)<1`
for every `0<p<α`. Its tilted logarithmic mean

```text
mα=E[ξ^α log ξ]
```

is finite and positive. Positivity follows by comparing the derivative
of `log h` at α with the positive secant slope between 1 and α. The
multiplier law and this root depend on η and b=2, but not on the teacher.

## 4. Uniform remainder, logarithmic contraction, and nonaffinity

The single-sample identity

```text
σ'(z)(σ(z)−Y)=z+δzu+(1+δu)(δt−Y)
```

and `|zu|≤1` give the exact affine-plus-remainder decomposition

```text
Ψθ,2(x)=Mx+Rθ,2(x),
sup_(x∈R)|Rθ,2(x)|≤Bθ,2
:=(η/2)Σ_(i=1)^2 |Aᵢ|[δ+(1+δ)(δ+|Yᵢ|)].                 (11)
```

The upper bound is uniform over x and, on the parameter rectangle,

```text
Bθ,2≤(3/5)Σ_(i=1)^2 |Aᵢ|
      [δ+(1+δ)(δ+(1+δ)|Aᵢ|+|Eᵢ|)].
```

Thus `Bθ,2` and `Lθ,2` have moments of all positive orders under a single
polynomial Gaussian envelope uniform in η and θ. The remainder and
multiplier may be dependent within a batch.

At zero, and at the two ends of the line, respectively,

```text
Ψθ,2'(0)=1−(η/2)(1+δ)²(A₁²+A₂²),
lim_(|x|→∞) Ψθ,2'(x)=1−(η/2)(A₁²+A₂²)=M.                 (12)
```

For each nonzero Aᵢ the terms containing `u`, `zu`, or `uYᵢ` vanish;
if Aᵢ=0 its derivative contribution is zero. The two values in (12)
differ whenever `A₁²+A₂²>0`, an event of probability one. Hence the
batch map is nonaffine almost surely, even though each asymptotic slope
equals M.

Write `Kθ,2=Lip(Ψθ,2)`. Equations (2) and (12) imply
`ξ≤Kθ,2≤Lθ,2`. Therefore

```text
E log⁻Kθ,2≤E log⁻ξ<∞,
E log⁺Kθ,2≤E Lθ,2<∞,
E log Kθ,2≤log E Kθ,2<log q₂<0.                            (13)
```

For an alternative lower bound on the envelope itself, put
`c₀=4δ+3δ²∈(0,1)`. Then
`Lθ,2≥|1−ηT|+c₀ηT≥c₀`; its logarithm is integrable as well.

## 5. Invariant law, uniqueness without moments, and lower moments

At zero the batch update is

```text
Ψθ,2(0)=(η/2)(1+δ)Σ_(i=1)^2 AᵢYᵢ,
E|Ψθ,2(0)|<∞.                                             (14)
```

Using the same independent fresh batch for two starting states contracts
their expected distance by at most q₂. Hence the transition operator is
a contraction on the complete Wasserstein-one space of laws with finite
first moment. Equations (8) and (14) give its invariant law π in that
space and the geometric W₁ convergence claimed in the theorem.

For any finite random initial state Z, independent of fresh batches, a
common-batch coupling with the chain from zero satisfies

```text
|X_n^Z−X_n^0|≤|Z|∏_(j=1)^n Lθ,2,j →0 almost surely.
```

The product tends to zero because its expectation is at most q₂^n;
Markov's inequality and Borel–Cantelli apply for each positive rational
threshold. No moment of Z is needed. If Z has any invariant probability
law, the coupled difference tends to zero and bounded Lipschitz test
functions identify that law with π. This proves uniqueness among all
probability laws.

For `0<p<α`, (11) yields a moment drift. If `p≤1`,

```text
E|Ψθ,2(x)|^p≤h_(η,2)(p)|x|^p+E Bθ,2^p.
```

If p>1, use
`(a+b)^p≤(1+ε)a^p+C_(p,ε)b^p`, with ε>0 chosen so that
`(1+ε)h_(η,2)(p)<1`. Either case gives constants r_p<1 and d_p<∞ with

```text
E|Ψθ,2(x)|^p≤r_p|x|^p+d_p.
```

The chain started from zero has uniformly bounded pth moments. Weak
convergence to π and lower semicontinuity of `|x|^p` give
`Eπ|X|^p<∞` for every `0<p<α`.

## 6. Conditional Gaussian law and explicit compact minorization

Conditional on `(A₁,A₂)=(a₁,a₂)`, the two independent fresh noises give

```text
Ψθ,2(x) ∼ Normal(μθ,2(x,a₁,a₂), sθ,2(x,a₁,a₂)²),
μθ,2=x−(η/2)Σ_(i=1)^2 aᵢσ'(aᵢx)[σ(aᵢx)−σ(aᵢθ)],
sθ,2²=(η²/4)Σ_(i=1)^2 aᵢ²σ'(aᵢx)².                       (15)
```

The conditional mean explicitly includes the input-dependent teacher
signal. If `a₁,a₂∈[1,2]` and `|x|≤R`, then

```text
|μθ,2|≤D_R:=R+(24/5)(1+δ)²(R+1),
s_min:=11/(10√2)≤sθ,2≤(6√2/5)(1+δ)=:s_max.                (16)
```

The mean bound follows from
`|σ(aᵢx)−σ(aᵢθ)|≤(1+δ)|aᵢ|(R+1)` and
`a₁²+a₂²≤8`; the variance bounds use `1≤σ'≤1+δ` and
`2≤a₁²+a₂²≤8`.

For any finite R,H>0, the density in (15) at every `|y|≤H` is at least

```text
d_(R,H)=[s_max√(2π)]^(−1)
         exp(−(H+D_R)²/(2s_min²))>0.
```

Let `p_A=P(1≤A≤2)>0` for a standard normal A. Integrating over both
inputs in `[1,2]` gives, for every Borel F,

```text
Pθ,2(x,F)≥ε_(R,H) Leb(F∩[−H,H]),  |x|≤R,
ε_(R,H)=p_A² d_(R,H)>0.                                    (17)
```

These constants are uniform in the stated parameter rectangle. Every
nonempty open interval consequently has positive transition probability
from every point, and stationarity gives it positive π mass. Thus
`supp π=R`. Equation (17) will also launch the excursions used below.

## 7. Exact radial limit and its coupled-difference constant

Apply the N=1 specialization of Jelenković–Olvera-Cravioto,
*Implicit Renewal Theory and Power Tails on Trees*,
[arXiv:1006.3295v5](https://arxiv.org/abs/1006.3295v5), Theorem 3.1,
printed page 5 of the [primary PDF](https://arxiv.org/pdf/1006.3295).
Its discrepancy theorem does not assume an affine fixed-point equation.
Take the nonnegative stationary variable `R₀=|X|` and independent
coefficient `C₁=ξ`. The theorem's required inputs are verified as follows:

| Required input | Verification |
|---|---|
| Positive coefficient and nonarithmetic logarithm | ξ>0 almost surely and (10). |
| Moment root | `Eξ^α=1`, Section 3. |
| Positive finite logarithmic mean | `0<mα<∞`, Section 3. |
| Some finite coefficient moment of order γ<α | Take γ=0. |
| Independence of R₀ and the fresh coefficient | X is independent of the complete new batch. |
| All positive stationary moments below α | Section 5. |
| Integrable weighted absolute discrepancy | Bound (18) below. |

Put `U=|Ψθ,2(X)|` and `V=|MX|=ξ|X|`. Stationarity gives U the law
of R₀, and (11) gives `|U−V|≤Bθ,2`. Tonelli and the mean value theorem
yield

```text
∫₀∞ t^(α−1)|P(R₀>t)−P(ξR₀>t)|dt
≤ E|U^α−V^α|/α,
|U^α−V^α|
≤α Bθ,2(V+Bθ,2)^(α−1)
≤α[Bθ,2^α+Bθ,2 ξ^(α−1)|X|^(α−1)].                         (18)
```

The final expression is integrable. The stationary `(α−1)`st moment is
finite; X is independent of the batch; and the joint moment
`E[Bθ,2 ξ^(α−1)]` is finite under the polynomial Gaussian envelope.
No independence of the remainder and multiplier is invoked.

The theorem gives a finite nonnegative limit C. Signed Fubini applied to
the same absolutely integrable coupled difference gives (1). The
following argument establishes strict positivity independently.

## 8. Strict positivity with the fresh complete-batch joint law

Fix η and θ. Write B for `Bθ,2`. The pairs `(ξ_j,B_j)` are iid images
of the complete fresh batches W_j. Their components are generally
dependent; the whole batch is the unit of independence and of tilting.

### 8.1. Radial inequality and complete-batch tilt

Define

```text
S₀=0,  S_n=Σ_(j=1)^n log ξ_j,
V_n=Σ_(j=1)^n e^(−S_j)B_j.
```

Iteration of `|Ψθ,2(x)|≥ξ|x|−B` gives the pathwise bound

```text
|X_n|≥e^(S_n)(|X₀|−V_n).                                   (19)
```

Tilt each complete batch by ξ^α and denote the iid product law by Q.
This is a probability law since `Eξ^α=1`. On the first n batches,
`dQ/dP=e^(αS_n)`. For a stopping time τ and a stopped event F, summing
the finite-horizon identity over `{τ=n}` proves

```text
P(F,τ<∞)=E_Q[e^(−αS_τ)1_(F,τ<∞)].                          (20)
```

There is no assertion of absolute continuity on infinite paths. Under Q,
`Z=log ξ` has integrable absolute value and mean mα>0. Thus `S_n→∞`
Q-almost surely. Fix β=1/2 and set

```text
r=E_Q e^(−βZ)=h_(η,2)(α−β)<1.                             (21)
```

### 8.2. Positive survival and uniform overshoot control

The process `e^(−βS_n)` is a nonnegative Q-supermartingale. Stopping at
the first visit to `(−∞,−1]`, truncated at n, gives
`Q(inf_(n≥0)S_n≤−1)≤e^(−β)`. A first increment greater than 1 followed
by an independent walk that never visits `(−∞,−1]` therefore gives

```text
Q(S_j>0 for every j≥1)
≥p₀:=Q(Z>1)(1−e^(−β))>0.                                  (22)
```

The strict positivity follows from the unbounded support of T and the
positive tilt density on ξ>0.

For u≥0 let `τ_u=inf{n≥1:S_n>u}` and `O_u=S_(τ_u)−u`.
Positive drift makes τ_u finite Q-almost surely. By (21),

```text
Σ_(n≥0) Q(S_n≤1)≤K_U:=e^β/(1−r)<∞.
```

For any interval `I=(a,a+1]`, condition on the first entry into I.
Every later visit to I requires a fresh-walk displacement at most 1.
The strong Markov property therefore gives the translated occupation
bound `Σ_(n≥0)Q(S_n∈I)≤K_U`. Partitioning `(−∞,u]` into intervals
`(u−k−1,u−k]` and dropping any no-earlier-crossing restriction now gives

```text
Q(O_u>z)
≤K_U Σ_(k≥0)Q(Z>z+k)
≤K_U[Q(Z>z)+∫_z∞Q(Z>v)dv] →0  as z→∞.                    (23)
```

The bound is uniform over u≥0, and its right side tends to zero because
`E_Q Z⁺<∞`.

### 8.3. Discounted remainders preserve within-batch dependence

Subadditivity at β=1/2 and independence of a complete batch from its past
give

```text
E_Q[(Σ_(j≥1)e^(−S_j)B_j)^β]
≤Σ_(j≥1) r^(j−1)E_Q[ξ^(−β)B^β]
=E_P[ξ^(α−β)B^β]/[1−h_(η,2)(α−β)]<∞.                     (24)
```

The numerator is a joint moment, not a product of marginal moments.
It is finite by the Gaussian polynomial envelope. Since `α−β>0`,
there is no inverse-multiplier singularity in this P-expectation. Thus
`V_∞=Σ_(j≥1)e^(−S_j)B_j<∞` Q-almost surely.

### 8.4. Uniform positive probability of a large excursion

Choose z≥0 so that (23) is at most p₀/4 for all u≥0, and choose K≥1
so that `Q(V_∞>K/2)≤p₀/4`. Both choices are independent of the eventual
tail threshold. For t>4K set `u=log(t/K)` and define the stopped event

```text
F_u={τ_u<∞, S_j>0 for 1≤j≤τ_u, V_(τ_u)≤K/2, O_u≤z}.
```

Equations (22)–(24) and a union bound give `Q(F_u)≥p₀/2`. For every
initial state y with `2K≤|y|≤4K`, on F_u the radial bound (19) yields

```text
|X_j|≥(3K/2)e^(S_j)>K,  1≤j≤τ_u,
|X_(τ_u)|>(3K/2)(t/K)>t.
```

It therefore forces a visit to `D_t={|x|>t}` before a return to
`C=[−K,K]`. On F_u, `S_(τ_u)≤u+z`. The stopped likelihood ratio (20)
implies

```text
inf_(2K≤|y|≤4K) P_y(τ_(D_t)<τ_C)
≥(p₀/2)e^(−αz)(K/t)^α.                                    (25)
```

The hitting times start at time one, with the initial annulus outside
both C and D_t. No assertion that τ_u is P-almost surely finite is
needed: (20) already restricts to its finite-crossing event.

### 8.5. Stationary last-exit transfer

For disjoint Borel C,D, let `τ_C^+=inf{n≥1:X_n∈C}`. In a stationary
chain, the events specifying the last visit to C before time N among
paths ending in D are disjoint. Thus

```text
π(D)≥∫_C π(dx)Σ_(j=1)^N P_x(X_j∈D,j<τ_C^+).
```

Monotone convergence as N→∞ gives

```text
π(D)≥∫_C π(dx)E_x[Σ_(j≥1)1_(X_j∈D,j<τ_C^+)]
     ≥∫_C π(dx)P_x(τ_D<τ_C^+).                             (26)
```

This is an unnormalized stationary integral; no return-time factor is
missing. Take `C=[−K,K]` and `J={2K≤|y|≤4K}`. Equation (17) gives

```text
inf_(x∈C)Pθ,2(x,J)≥δ_K:=4K ε_(K,4K)>0.
```

Use the Markov property after this first step and then (25). Since full
support implies π(C)>0, (26) yields, for t>4K,

```text
π(D_t)≥c_(η,θ,2)t^(−α),
c_(η,θ,2)=π(C)δ_K(p₀/2)e^(−αz)K^α>0.                      (27)
```

Combining (27) with the existing limit from Section 7 proves
`C_(η,θ,2)≥c_(η,θ,2)>0`.

## 9. Exact moments, genuine teacher, and symmetry scope

For p>0, the identity
`E|X|^p=p∫₀∞t^(p−1)P(|X|>t)dt`, together with the positive tail limit,
forces divergence when p≥α. Section 5 supplies finiteness below α.
For t>|θ|,

```text
P(|X|>t+|θ|)≤P(|X−θ|>t)≤P(|X|>t−|θ|).
```

A bounded shift therefore preserves the tail constant and the moment
threshold.

Averaging the two sample losses leaves the population risk unchanged:

```text
E fbarθ,2(x;W)=E fθ(x;A,E)
=1/2+(1/2)E[σ(Ax)−σ(Aθ)]²
≥1/2+(1/2)(x−θ)².
```

The inequality follows from `σ'≥1` and `EA²=1`; equality at x=θ
shows that θ is the unique population minimizer. For the concrete
teacher θ=1, each label is `Y=A+δ tanh(A)+E`, with
`E[AY]=1+δE[A tanh(A)]>1`. This is a genuine nonzero regression signal.

Reflecting both additive noises gives

```text
Ψ_(−θ,2;A₁,−E₁,A₂,−E₂)(−x)=−Ψ_(θ,2;A₁,E₁,A₂,E₂)(x).
```

Consequently `π_(η,−θ,2)` is the reflection of `π_(η,θ,2)`, and their
absolute-tail constants agree. At θ=0 the invariant law is symmetric,
so each one-sided tail constant is C/2. For a fixed nonzero teacher,
no one-sided limit or equality of one-sided constants is claimed in
this proof.

Indeed the invariant law cannot be symmetric about zero when θ≠0.
Its finite first moment and stationarity imply, after averaging the
fresh noises and the two identical sample marginals,

```text
0=E[Aσ'(AX)(σ(AX)−σ(Aθ))].
```

Both terms are integrable. Under a symmetric law of X the term
`Aσ'(AX)σ(AX)` has expectation zero, since it is odd in X. The other
term `Aσ'(AX)σ(Aθ)` has the strict sign of θ whenever A≠0, a
contradiction. This absence of exact symmetry does not decide whether
a separate signed-tail theorem could give equal asymptotic constants.

## 10. Exact checks, parameter-pair scope, and provenance

`campaign/checks/A22_batch_two_exact.py` verifies the rational arithmetic
in this proof using `fractions.Fraction`. Its saved output is
`campaign/checks/A22_batch_two_exact.out`. In particular:

| Quantity | Exact value |
|---|---|
| Mixed-label upper bound | `3+2δ=1501/500` |
| Derivative perturbation | `4δ+3δ²+2δ(3+2δ)=10007/10^6` |
| Positive exponential-series margin | `71449/31104−25/11=8339/342144` |
| Lower bound used for the derivative in (6) | `2/9` |
| Uniform multiplier first-moment upper bound | `107/125` |
| Uniform actual-map contraction bound | `2170021/2500000` |
| Contraction margin | `329979/2500000` |
| Minimum multiplier second moment | `61/50` |

These are exact certificate checks, not a simulation or a quadrature
substitute for the probability proof.

Combined with the pinned batch-one source, the explicit verified
parameter pairs are

```text
(η,b)∈([99/100,101/100]×{1}) ∪ ([11/10,6/5]×{2}),
θ∈[−1,1].
```

The batch-two part remains an author proof pending independent audit.
This enlarges the discrete minibatch regime by proving a second batch
size with the original Gaussian sample marginals and nonlinear teacher.
It is not a theorem for every batch size, for a continuous batch
parameter, or for every learning rate. In particular, no monotonicity
of the tail index under each increment b→b+1 is asserted or used, and
no index comparison at different learning rates is inferred from the
two displayed regimes.

The existing T228 work of `claude-b1e26540`,
`rows/T228/claude_b1e26540/T3_STEP3.md` (supplied local copy
`a01/claude_b1e26540/T3_STEP3.md`), supplied the forward tilted-walk
and stationary last-exit positivity mechanism. A01 supplied the
explicit batch-one actual-map contraction certificate; A09 supplied
the pinned nonzero-teacher extension and its dependence checks. This
note adapts and rechecks those ingredients for a full two-sample batch,
including its exponential multiplier law and changed conditional
Gaussian variance. It does not reassign discovery credit.

The sole external exact-tail theorem used here is
Jelenković–Olvera-Cravioto, Theorem 3.1, checked directly in the primary
arXiv PDF on 23 October 2026. Its nonnegative-limit conclusion is kept
separate from the proof of strict positivity. No first-in-literature
priority, independent acceptance, or general nonlinear-network theorem
is claimed. No remote write was made.
