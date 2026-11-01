# T228: finite-time moments, exact moment growth, and Wasserstein convergence

23 October 2026. Companion to `T228_EXPLICIT_CLOSURE.md`, Version 2,
SHA256 `a1dbdbb1e99a85749143f44dd8b7d7e264fb550d285c5667f69f1a35ff87c38f`.

This note derives moment dynamics for the actual nonlinear recursion. It
does not replace its update by an affine recursion. The exact stationary
tail and its constant are used only where expressly indicated. In
particular, the explicit second-moment lower bound and independent
stationary infinite-variance proof in Section 5 do not depend on the
implicit renewal theorem or on stationary tail positivity.

## 1. Model, notation, and conclusions

Fix `d=10^{-3}`, `η∈[0.99,1.01]`, and a deterministic `X_0=x_0∈R`. With
independent fresh standard normals `(A_{n+1},E_{n+1})`, use

```text
s(z) = z+d tanh(z),
X_{n+1} = Ψ_{n+1}(X_n),
Ψ(x) = x−η A s'(Ax)(s(Ax)−E).
```

The source establishes the following bounds and stationary conclusions:

```text
M = 1−η A²,                 ξ = |M|,
Ψ(x) = Mx+R(x),             |R(x)|≤B for every x,
B = η|A|[d+(1+d)(d+|E|)],
E Lip(Ψ) < q = 0.98606303 < 1,
h(p) = E ξ^p,              h(α)=1,       1<α<2,
h_2 := h(2) = 1−2η+3η² ∈ [1.9603,2.0403].
```

The variables `B` and `ξ` have all positive moments. The unique invariant
law `π` has finite moments exactly below `α`, is symmetric, and satisfies

```text
lim_{t→∞} t^α π(|x|>t) = C_η ∈ (0,∞).
```

Write `m_p(n)=E|X_n|^p` and
`μ_α=E[ξ^α log ξ]∈(0,∞)`. Then:

1. Every `m_p(n)` is finite for every finite `n` and every `p>0`.
2. If `0<p<α`, then `m_p(n)→∫|x|^p π(dx)<∞`.
3. If `p≥α`, then `m_p(n)→∞`.
4. More precisely, `m_α(n)/n→α μ_α C_η>0`.
5. For every `p>α`, there is `K_p(x_0,η)∈(0,∞)` such that
   `m_p(n)/h(p)^n→K_p(x_0,η)`.
6. In particular, `E X_n² ~ K_2(x_0,η) h_2^n`. The same asymptotic holds
   for `Var(X_n)`.

There is also a completely explicit second-moment lower bound. Define

```text
N = min{n≥0 : q^n |x_0|≤50}.
```

Thus `N=0` if `|x_0|≤50`, and otherwise
`N=ceil(log(|x_0|/50)/(−log q))`. For every integer `k≥0`,

```text
E X_{N+k}² ≥ h_2^k E X_N²
              +(39/100)(h_2^k−1)/(h_2−1)
            ≥ (39/100)((1.9603)^k−1)/0.9603.                 (1)
```

All constants in (1), including the definition of `N`, are uniform over
the stated learning-rate interval.

## 2. Finite-time finiteness and convergence of subcritical moments

The current state is independent of the fresh pair `(M,B)`, although
`M` and `B` need not be independent of one another. For `0<p≤1`,
subadditivity gives

```text
m_p(n+1) ≤ h(p)m_p(n)+E B^p.
```

For `p≥1`, Minkowski's inequality gives, with
`a_p=h(p)^{1/p}` and `b_p=(E B^p)^{1/p}`,

```text
||X_{n+1}||_p ≤ a_p ||X_n||_p+b_p.                         (2)
```

These inequalities inductively prove finite-time finiteness for every
positive order, starting from a deterministic initial value.

For every `0<r<α`, `h(r)<1`. The usual bound on the power of a sum gives
a drift inequality

```text
E[|Ψ(x)|^r] ≤ λ_r |x|^r+D_r,     λ_r<1,
```

and hence `sup_n m_r(n)<∞`. For `r≤1`, the displayed subadditivity
inequality already supplies this drift. For `r>1`, use
`(a+b)^r≤(1+ε)a^r+C_{r,ε}b^r` with `(1+ε)h(r)<1`.

Fix `p<α` and choose `r∈(p,α)`. The uniform `r`-moment bound makes
`{|X_n|^p}` uniformly integrable, since for every `T>0`,

```text
E[|X_n|^p ; |X_n|>T] ≤ T^{p−r} sup_j m_r(j).
```

Together with weak convergence to `π`, this proves the asserted
convergence of the `p`-th absolute moments.

## 3. Why the divergent moments diverge along the entire sequence

Let `p≥α`. The exact positive stationary tail implies
`∫|x|^p π(dx)=∞`, including at the endpoint `p=α`. For each `K>0`, the
function `f_K(x)=min(|x|^p,K)` is bounded and continuous, so weak
convergence gives

```text
liminf_{n→∞} m_p(n)
  ≥ lim_{n→∞} E f_K(X_n)
  = ∫ f_K(x) π(dx).
```

The right side increases to infinity as `K→∞`. Therefore
`m_p(n)→∞`, not merely an unbounded subsequence. This is the
bounded-truncation form of the Portmanteau argument. It does not require
monotonicity of the moments, and it does not exchange an unbounded
moment with a weak limit.

This step uses the stationary moment threshold established by the
source. The explicit second-moment proof below is independent of that
threshold.

## 4. A bounded-remainder norm lemma and exact supercritical growth

The following elementary fact is useful beyond this model. Suppose
`p≥1`, `a=(E|M|^p)^{1/p}>1`, and `b=(E B^p)^{1/p}<∞`. Independence
of the new multiplier from the current state and the two triangle
inequalities yield

```text
| ||X_{n+1}||_p − a||X_n||_p | ≤ b.                       (3)
```

The remainder may depend on both the state and the complete new step;
no independence between `M`, `B`, and `R(X_n)` is used. In particular,
(3) holds for the genuinely nonlinear update here.

Set `u_n=||X_n||_p`. Then

```text
|a^{−(n+1)}u_{n+1}−a^{−n}u_n| ≤ b a^{−(n+1)}.
```

The right side is summable. Thus `a^{−n}u_n` converges to a finite
`ℓ_p≥0`, and summing its remaining increments gives the stronger bound

```text
|u_n−ℓ_p a^n| ≤ b/(a−1)                 for every n.       (4)
```

If `u_n` is unbounded, (4) forces `ℓ_p>0`. Equivalently, after any
index `J` with `u_J>b/(a−1)`, direct iteration gives

```text
u_{J+k} ≥ a^k[u_J−b/(a−1)]+b/(a−1),     k≥0.             (5)
```

The upper inequality in (3) also gives

```text
u_n ≤ a^n[|x_0|+b/(a−1)]−b/(a−1).                        (6)
```

For this model, `p>α` implies `p>1` and `h(p)>1`. Section 3 gives
`u_n→∞`, so `ℓ_p>0`. Raising the normalized norm to the `p`-th power
proves

```text
m_p(n)/h(p)^n → K_p := ℓ_p^p ∈ (0,∞).                    (7)
```

For `p=2`, write `a=√h_2` and `b=(E B²)^{1/2}`. If
`c=d(2+d)`, the explicit envelope yields

```text
b² = η²[c²+2c(1+d)√(2/π)+(1+d)²],
b ≤ η[c+(1+d)] ≤ 1.01303101.
```

Thus (4) gives
`E X_n² = K_2 h_2^n + O(h_2^{n/2})`; a valid explicit bound for the
absolute error is

```text
2√K_2 [b/(√h_2−1)] h_2^{n/2}+[b/(√h_2−1)]².
```

In particular the eventual lower rate can be the exact factor `h_2`,
which is stronger than any prescribed rate `ρ<h_2`.

## 5. Explicit uniform lower bound without a stationary-tail input

Here the Gaussian label noise supplies positive forcing that survives
the small nonlinear perturbation. Put `z=Ax`, `u=sech²(z)`, and
`t=tanh(z)`. Separate the label from the deterministic part of the step:

```text
Ψ(x) = Mx−T(A,x)+η A(1+du)E,
T(A,x) = η A d[zu+(1+du)t].
```

The inequalities `|z|u≤1` and `|t|≤1` imply

```text
|T(A,x)| ≤ η d(2+d)|A|.                                  (8)
```

Conditionally on `A` and `x`, the label term has mean zero and variance
`η² A²(1+du)²`. Since `1+du≥1`, averaging the conditional square,
discarding `T²≥0`, and using (8) gives

```text
E[Ψ(x)²] ≥ h_2 x²−c_η |x|+η²,
c_η = 2η d(2+d) E[|M||A|].                               (9)
```

Cauchy–Schwarz and `E A²=1` yield
`E[|M||A|]≤√h_2<1.43`. Therefore, uniformly in `η`,

```text
c_η < 2(1.01)(0.001)(2.001)(1.43)
    = 0.0057800886 < 0.006.                               (10)
```

We also need a uniform first-moment bound. At zero,
`Ψ(0)=η(1+d)AE`, so independence of the two standard normals gives

```text
E|Ψ(0)| = η(1+d)(2/π) < 13/20.
```

Average Lipschitz contraction consequently implies

```text
E|X_n| ≤ q^n|x_0|+(13/20)(1−q^n)/(1−q)
       < q^n|x_0|+47,                                    (11)
```

because `(13/20)/(1−q)<47`. With `N` defined in Section 1, (11)
gives `E|X_n|<97` for every `n≥N`. Applying (9) to the random
state, which is independent of the fresh step, gives

```text
E X_{n+1}²
  ≥ h_2 E X_n²−c_η E|X_n|+η²
  > h_2 E X_n²−(0.006)(97)+(0.99)²
  = h_2 E X_n²+0.3981
  ≥ h_2 E X_n²+39/100,                    n≥N.            (12)
```

Iteration of (12) proves (1). Combining (1) with the norm lemma proves
the existence and positivity of `K_2` without using the exact-tail
theorem, and even gives

```text
K_2 ≥ h_2^{−N}[E X_N²+(39/100)/(h_2−1)]
    ≥ (39/100)h_2^{−N}/(h_2−1) > 0.                       (13)
```

For example, `x_0=0` has `N=0`, so every finite time satisfies

```text
E X_n² ≥ (39/100)(h_2^n−1)/(h_2−1).
```

The rational arithmetic supporting (10)–(12) is exact; none of these
inequalities comes from a simulation. The use of `1.43` is justified by
`h_2≤2.0403<(1.43)²`.

The same drift independently proves that the stationary second moment
is infinite. Since `π` has finite first moment, stationarity and the
first-moment contraction give `E_π|X|<47`. If its second moment
`v_π` were finite, integrating (9) would yield

```text
v_π ≥ h_2 v_π−c_η E_π|X|+η²
    > h_2 v_π−(0.006)(47)+(0.99)²
    = h_2 v_π+0.6981.
```

This is impossible because `h_2>1` and `v_π≥0`. Thus contraction and
the elementary actual-update drift alone certify `E_π X²=∞`.

## 6. The critical moment has linear, not exponential, growth

Define the one-step integrable difference

```text
g(x) = E[|Ψ(x)|^α−|Mx|^α].
```

For `1<α<2`, the mean-value inequality and subadditivity at exponent
`α−1` give

```text
||Ψ(x)|^α−|Mx|^α|
 ≤ α B(ξ|x|+B)^{α−1}
 ≤ α[B^α+B ξ^{α−1}|x|^{α−1}].                            (14)
```

All coefficients in this bound have finite expectation. The update is
continuous in `x`, and (14) supplies an integrable dominating function
on every compact `x`-interval. Therefore `g` is continuous and
`|g(x)|≤C_0+C_1|x|^{α−1}`.

Choose `r∈(α−1,α)`. The uniform `r`-moment bound from Section 2 and
weak convergence imply

```text
E g(X_n) → ∫g(x)π(dx) = α μ_α C_η =: D_η > 0.             (15)
```

For precision, the expectation convergence follows by first applying
weak convergence to a continuous compact truncation of `g`, and then
using the `r`-moment bound to control the removed tail, of order
`O(T^{−r}+T^{α−1−r})`. The equality and positivity in (15) use the
source's exact-tail formula, whose numerator is the expectation of an
integrable difference.

At every finite time both absolute moments below are finite, so
`h(α)=1` gives the valid identity

```text
m_α(n+1)−m_α(n) = E g(X_n).
```

Summing this identity and applying Cesàro convergence to (15) proves

```text
lim_{n→∞} m_α(n)/n = D_η = α μ_α C_η > 0.                 (16)
```

There is no subtraction of infinite stationary moments in this
argument. Only the stationary expectation of the integrable difference
appears in (15).

## 7. Geometric W1 convergence and infinite stationary variance coexist

Let `Y_0~π`, independent of the fresh steps, and run the two chains with
the same steps. Then `Y_n~π` and

```text
E|X_n−Y_n| ≤ q^n E|x_0−Y_0|.
```

The last expectation is finite because `α>1`. Thus

```text
W1(Law(X_n),π) ≤ q^n ∫|x_0−y|π(dy).                      (17)
```

W1 controls Lipschitz observables and first absolute moments. It does
not control the observable `x²`. Finite-time laws may converge weakly,
and even at the geometric W1 rate (17), while their second moments grow
exponentially. The second powers are not uniformly integrable.

For an additional precise distinction, the extended quadratic transport
cost between `Law(X_n)` and `π` is infinite at every finite `n`. Indeed,
if some coupling `(U,V)` had `U~Law(X_n)`, `V~π`, and
`E|U−V|²<∞`, then

```text
E V² ≤ 2E U²+2E|U−V|² < ∞,
```

contradicting the infinite second moment of `π`. Thus there is no W2
convergence claim.

Symmetry and finite first moment give `E_π X=0`; (17) then gives

```text
|E X_n| ≤ q^n ∫|x_0−y|π(dy).
```

Consequently `(E X_n)²` decays geometrically while `E X_n²` grows
like `K_2 h_2^n`, proving

```text
Var(X_n)/h_2^n → K_2 ∈ (0,∞).
```

## 8. Dependence and scope

Finite-time finiteness, the norm lemma, and the explicit bound (1) use
only the model and the elementary multiplier, remainder, and
contraction bounds. They independently prove explosive second-moment
growth from every deterministic initial point. The same elementary
drift also independently proves infinite stationary second moment.

The full moment threshold, the divergence statement for every `p≥α`,
and the critical slope (16) use the stationary exact-tail conclusions
of the specified source version. This companion does not claim a new
audit of the external implicit renewal theorem, novelty, or a registry
closure action. It supplies a rigorous distinction between finite-time
moment finiteness, convergence of the state laws, and divergence of
their high-order moments.
