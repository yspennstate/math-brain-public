# T228: equal one-sided tail constants with a nonzero teacher

Version 1, 23 October 2026. A23 optional strengthening.

Source model: `campaign/proofs/T228_NONZERO_TEACHER.md`, read at SHA256
`f95fa6fade82ba0dca4dab8e311fc61bb57b3267f3953b465c94228cb1315933`.
The present proof uses its actual-map remainder bound, existence and full
support of the stationary law, and multiplier-moment calculations. It does
not assume that a fixed nonzero-teacher law is symmetric.

## 1. Strengthened conclusion

Fix

```text
δ = 1/1000,  σ(z) = z + δ tanh(z),
θ ∈ [−1,1],  η ∈ [99/100,101/100].
```

For independent standard normals `A,E`, put

```text
Y = σ(Aθ) + E,
Ψθ(x) = x − η A σ'(Ax)[σ(Ax) − Y],
M = 1 − ηA².
```

Let `π = π_(η,θ)` be the unique invariant probability and let
`α = α(η) ∈ (1,2)` solve `E|M|^α = 1`. If `X` has law `π`, then

```text
lim_(t→∞) t^α P(X>t)
  = lim_(t→∞) t^α P(X<−t)
  = C_(η,θ)/2 ∈ (0,∞),                                    (S1)
```

where `C_(η,θ)` is exactly the absolute-tail constant in the source model.
Both conclusions also hold with `X−θ` in place of `X`. In particular, the
one-sided tails have ratio tending to one even for a fixed nonzero teacher.
This is an asymptotic assertion; it does not make the invariant law symmetric.

## 2. Primary theorem used and its complete hypothesis list

The source is Alsmeyer, Brofferio and Buraczewski,
*Asymptotically linear iterated function systems on the real line*,
[arXiv:2102.02299v2](https://arxiv.org/pdf/2102.02299v2), dated 6 October 2021.
Use Theorem 2.1, printed pp. 6–7, in its irreducible case, and Proposition
8.1, printed p. 36. The following is the exact theorem call, using new
notation `A_-`, `A_+` for the paper's two slopes and `J_n` for its sign chain.

| Source requirement | Specialization checked below |
|---|---|
| Standing (1), (4): iid continuous random maps and `sup_x abs(Ψ(x)−Λ(x))≤B`, `B≥1` | `Λ(x)=Mx`; use `B=1∨Bθ` from (S2). |
| Case 1: `p_{−,+}>0` and `p_{+,−}>0` | Both equal `P(M<0)>0`. |
| (12): `ρ(κ)=1` for some `κ>0` | `ρ(s)=E abs(M)^s`, `κ=α`. |
| (13): `E[abs(A_±)^κ log(abs(A_±))]<∞`, `EB^κ<∞` | We verify absolute logarithmic integrability and all positive moments of `B`. |
| (14): for every `h>0` and `a_-,a_+∈R`, `P_{πhat(κ)}(log(abs(A_(J_0)))−a_(J_1)+a_(J_0)∈hZ)<1` | Positive-multiplier self-loops verify this in Section 5. |
| A stationary probability `ν` | Take `ν=π`. |
| Proposition 8.1: unbounded support of `ν` | In fact `supp π=R`. |

Theorem 2.1 gives finite nonnegative limits `C_+`, `C_-` and its equation
(16), `u_+(κ)C_-=u_-(κ)C_+`. Proposition 8.1 makes both positive under the
last row. The vectors `u,v` are normalized by `u_-+u_+=1` and `u^T v=1`.
No independence between the slopes and `B` is assumed in this call.

## 3. Actual maps, moments and stationarity

The full tuples `(Ψθ,k,M_k,Bθ,k)` are iid because the input/noise pairs are
iid. The tuples may have dependence among their components. The maps are
smooth, hence satisfy the continuity requirement. The exact remainder
calculation in Section 2 of the source model gives

```text
sup_(x∈R) |Ψθ(x)−Mx|
≤ Bθ := η|A|[δ+(1+δ)(δ+|Y|)].                              (S2)
```

Set `B=1∨Bθ`; this includes the paper's convention `B≥1`. The estimate

```text
|Y| ≤ (1+δ)|θ||A| + |E|
```

shows that `B` is bounded by a fixed polynomial in `|A|,|E|` on the
parameter rectangle. Thus `EB^p<∞` for every `p>0`. Internal dependence
between `B`, `M`, and the input-dependent label is harmless.

The multiplier has density

```text
f_M(m) = exp(−(1−m)/(2η)) / sqrt(2πη(1−m)),   m<1,         (S3)
```

and zero density for `m>1`. In particular `P(M=0)=0`, both signs have
positive probability, and the density is bounded near zero. The integral
of `|m|^α |log|m|| f_M(m)` is finite near zero because `α>0`, at the
upper endpoint `m=1` because its density singularity is integrable, and at
`−∞` because of exponential decay. Therefore

```text
E[|M|^α |log|M||] < ∞.                                   (S4)
```

The source model proves `E Lip(Ψθ)<q<1`, `E|Ψθ(0)|<∞`, and consequently
existence and uniqueness of `π`. Its support argument can be checked
directly here: conditional on `A=a≠0`,

```text
Ψθ(x) = x−ηaσ'(ax)[σ(ax)−σ(aθ)] + ηaσ'(ax)E.
```

The conditional variance is strictly positive because `σ'≥1`. Hence the
one-step transition puts positive mass on every nonempty open interval
from every `x`. Integrating that statement against a stationary probability
gives `π(I)>0` for each such interval `I`, so `supp π=R`. This verifies
the positivity proposition's support hypothesis on both sides.

## 4. Sign matrix, Perron normalization and positive drift

Use the state order `(−,+)` and define, for `s≥0`,

```text
d_s = E[|M|^s 1_{M>0}],
o_s = E[|M|^s 1_{M<0}],
hη(s) = d_s + o_s.
```

Since both asymptotic slopes are exactly the same random variable,
`A_-=A_+=M`, the paper's matrix (8) becomes

```text
P(s) = [[d_s, o_s],
        [o_s, d_s]].                                      (S5)
```

Every entry is finite and positive. Its eigenvalues are `d_s+o_s` and
`d_s−o_s`, with `|d_s−o_s|<d_s+o_s`. Thus its Perron spectral radius is
`ρ(s)=hη(s)` and the normalized eigenvectors are

```text
u(s) = (1/2,1/2)^T,    v(s) = (1,1)^T.                    (S6)
```

In particular `πhat(α)=(u_-v_-,u_+v_+)^T=(1/2,1/2)^T`.
The condition `ρ(α)=1` is the already established multiplier equation.
For completeness, the source model verifies

```text
hη(1)<0.98<1,
hη(2)≥1.9603>1,
hη(s)<1 for 0<s<α,
ρ'(α)=E[|M|^α log|M|]=mα ∈ (0,∞).                        (S7)
```

Thus the strict intermediate-moment contraction used in the source's
positivity proof is present. Also `P(0)` is an actual stochastic matrix,
since `P(M=0)=0`; there is no killing state to address.

The vector in (S6) describes the sign chain of the linear approximation.
It is not a claim that `Pπ(X>0)=1/2`, or that the actual stationary law
is invariant under reflection.

## 5. The Markov additive nonarithmetic condition, including phase offsets

Let `J_0∈{−1,1}`, chosen independently of the fresh step, and put

```text
J_1 = J_0 sign(M),    Z_1 = log|M|.
```

For arbitrary `h>0` and phase offsets `a_-,a_+`, consider the lattice event

```text
H = {Z_1 − a_(J_1) + a_(J_0) ∈ hZ}.                       (S8)
```

On `{M>0}`, the transition is a self-loop: `J_1=J_0`. The offsets
therefore cancel, and `H` reduces there to `{log M∈hZ}`. Conditional
on `M>0`, formula (S3) and the change of variable `m=e^z` give an
absolutely continuous law of `log M` on `(-∞,0)`. Since `hZ` is
countable,

```text
P_{πhat(α)}(H ∩ {M>0}) = 0,
P_{πhat(α)}(H) ≤ P(M<0) < 1.                             (S9)
```

This verifies the precise phase-offset condition (14); it does not merely
appeal to nonarithmeticity of the unconditional scalar `log|M|`.

There is no distinction left unresolved between the original and tilted
versions of the condition. In this model, because `v≡1` and `ρ(α)=1`,
the one-step change of measure has density `|M|^α`. It is strictly positive
almost surely and preserves absolute continuity on the self-loop event.
Under the tilted law, the positive-multiplier probability is `d_α>0`, so
the same argument bounds the lattice probability by `o_α=1−d_α<1`.
This is also the Markov additive nonarithmetic formulation discussed in
the source's Section 4.3, printed pp. 22–23.

## 6. One-sided limits, positivity and identification of the constant

All hypotheses in Section 2 have now been verified. Apply Theorem 2.1
with `κ=α` and `ν=π`. Its relation between the two limiting constants
and (S6) give

```text
(1/2)C_- = (1/2)C_+,  hence C_-=C_+ =: c.                (S10)
```

Apply Proposition 8.1 to the full-support stationary measure to obtain
`c>0`. This application needs only unbounded support in addition to the
theorem's situation; the full-support verification above is stronger.

For every `t>0`, the tail events are disjoint and

```text
P(|X|>t) = P(X>t) + P(X<−t).
```

Consequently `C_(η,θ)=C_++C_-=2c`, proving (S1). This also gives a
second positivity check using the already positive absolute-tail constant
in the source model, without relying on any symmetry.

With `X` independent of a fresh `(A,E)`, its existing integrable-difference
formula now reads

```text
c = E[|Ψθ(X)|^α − |MX|^α] / (2α mα).                     (S11)
```

The numerator is the expectation of a single coupled integrable
difference. It must not be split into two infinite expectations. Its
integrability is verified in Section 6 of the source model.

Finally, fixed translation preserves either one-sided constant:
`P(X−θ>t)=P(X>t+θ)` and
`P(X−θ<−t)=P(X<−(t−θ))`, while
`t/(t±θ)→1`. Thus the asserted limits for estimation error follow.

## 7. Scope and integration into the source model

This proof establishes an optional strengthening for each fixed parameter
pair in the stated rectangle. It requires no extra symmetry assumption,
and no independence between the multiplier and the nonlinear remainder.
It makes no uniform lower-bound claim for the tail constant.

The nonzero-teacher symmetry obstruction in Section 9 of the source
model remains valid. Reflection relates the laws at opposite teachers;
it does not preserve the fixed nonzero-teacher model. Equal limiting
one-sided constants coexist with the lack of exact symmetry. The mechanism
here is the Perron relation for the irreducible sign chain of the common
asymptotic slope.

If this strengthening is adopted, the source model's disclaimer declining
to assert one-sided limits can be replaced by (S1), with a citation to this
argument and the primary theorem. Its statement that the nonzero-teacher
law is not symmetric should be retained. No source-model file was changed
in this task.
