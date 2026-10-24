Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# C0032 — self-decomposable log-stable law, a monotone physical tail invariant for alpha <= 1, and rational holonomic-complexity blow-up

Target: Charles Bordenave and Djalil Chafaï, *Around the circular law*, Probability Surveys 9 (2012), arXiv:1109.3343v4, heavy-tailed limiting law `mu_alpha`; underlying scalar characterization from Charles Bordenave, Pietro Caputo and Djalil Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, CMP 307 (2011), arXiv:1006.1713v5.

Status of source target after this artifact: **PARTIAL / OPEN**.  The all-alpha physical density has not been reduced to a standard closed expression.  The results below are exact structural theorems and do not change the already-saturated frozen metric `M_jet=+infinity`.

Methods executed here: **B9 / B13 / B27**.

## 1. Recalled exact normal form

Put

```text
beta = alpha/2 in (0,1),
c_beta = Gamma(1-beta),
C_beta = Gamma(1-beta) Gamma(1+beta).
```

Let `S,S'` be independent positive beta-stable random variables normalized by

```text
E exp(-t S) = exp[-c_beta t^beta].
```

Write `T=SS'`.  The preceding R7-06 reductions proved the exact one-dimensional representation

```text
q_beta(a) = E[T/(a+T)],
R_beta(a) = a [q_beta(a)/C_beta]^(1/beta),
Q_beta(R_beta(a)) = q_beta(a),
```

where

```text
Q_beta(r) = 1 - mu_alpha{|z|^2 <= r}
```

and `R_beta:(0,infinity)->(0,infinity)` is a smooth increasing bijection.  The physical planar density is

```text
g_alpha(sqrt(R_beta(a))) = -q_beta'(a)/(pi R_beta'(a)).
```

Equivalently, if `E_1,E_2` are independent Exp(1) variables and

```text
W_beta = SS' E_1/E_2,
X_beta = log W_beta,
```

then

```text
P(X_beta <= log a) = 1-q_beta(a).                    (1.1)
```

The exact moment-generating function on `-1<Re(s)<beta` is

```text
M_beta(s) := E exp(s X_beta)
 = c_beta^(2s/beta)
   Gamma(1-s/beta)^2 Gamma(1+s)/Gamma(1-s).          (1.2)
```

The previous run used (1.2) only as a transform/quantile representation.  B9 asks whether it places `X_beta` in a canonical infinitely-divisible class.

## 2. B9 RANDOMIZE — exact Levy-Khintchine law of the residual quantile variable

### Theorem 2.1 — `X_beta` is self-decomposable for every `0<beta<1`

For every `0<beta<1`, `X_beta` is infinitely divisible and self-decomposable.  With full linear compensation, its cumulant generating function is

```text
log M_beta(s)
 = m_beta s
   + Integral_R (exp(sx)-1-sx) nu_beta(dx),           (2.1)
```

where

```text
m_beta = (2/beta)(log c_beta + gamma_E) - 2 gamma_E,
```

and the Levy measure is absolutely continuous:

```text
nu_beta(dx)
 = 1_{x>0}  k_{beta,+}(x) dx/x
   + 1_{x<0} k_-(|x|) dx/|x|,                         (2.2)
```

with

```text
k_{beta,+}(x) = 2/(exp(beta x)-1) - 1/(exp(x)-1),
k_-(x)        = 1/(exp(x)-1),               x>0.      (2.3)
```

Moreover `k_{beta,+}` and `k_-` are strictly decreasing on `(0,infinity)`.  Hence (2.2) is precisely the canonical Levy-density shape for a real self-decomposable law.

#### Proof

Use Malmsten's formula

```text
log Gamma(1+z)
 = -gamma_E z
   + Integral_0^infinity
       [exp(-zx)-1+zx]/[x(exp(x)-1)] dx.              (2.4)
```

From (1.2),

```text
log M_beta(s)
 = (2s/beta) log c_beta
   + 2 log Gamma(1-s/beta)
   + log Gamma(1+s)
   - log Gamma(1-s).                                  (2.5)
```

Apply (2.4) to each Gamma term.  In the two `Gamma(1-s/beta)` terms change variables `x=beta y`.  They contribute the positive-jump kernel

```text
2/[y(exp(beta y)-1)].
```

The term `-log Gamma(1-s)` subtracts

```text
1/[y(exp(y)-1)]
```

from the positive-jump kernel.  The term `log Gamma(1+s)` contributes, after reflecting `y=-x`, the negative-jump kernel

```text
1/[|y|(exp(|y|)-1)].
```

The linear pieces combine to `m_beta s`.  This gives (2.1)-(2.3).

Near zero,

```text
k_{beta,+}(x) = (2/beta-1)/x + O(1),
k_-(x)        = 1/x + O(1),
```

so the compensated Levy integral is locally finite; at infinity both kernels decay exponentially.

Positivity of `k_{beta,+}` is immediate from `0<beta<1`.  Also

```text
k_-'(x) < 0.
```

Using

```text
exp(t)/(exp(t)-1)^2 = 1/[4 sinh^2(t/2)],
```

we obtain

```text
k_{beta,+}'(x)
 = - beta/[2 sinh^2(beta x/2)]
   + 1/[4 sinh^2(x/2)].                               (2.6)
```

For `u>0`, convexity of `sinh` and `sinh(0)=0` imply

```text
sinh(beta u) <= beta sinh(u).
```

Therefore

```text
sinh^2(beta u) <= beta^2 sinh^2(u) < 2 beta sinh^2(u),
```

which is exactly the strict negativity of (2.6).  The standard one-dimensional characterization of self-decomposability is that the Levy density is `k(x)/|x|`, with the canonical function increasing on the negative ray and decreasing on the positive ray.  Thus `X_beta` is self-decomposable. QED.

This is stronger than merely saying that (1.2) is a characteristic function: the final inverse in the BCC radial law is the quantile of a canonical self-decomposable distribution with an explicit Levy measure.

### Theorem 2.2 — exact Thorin-class arithmetic split

Under the standard one-dimensional Thorin-class characterization (the radial canonical functions in the Levy measure are completely monotone),

```text
X_beta belongs to the Thorin class T(R)
    iff beta = 1/q for some integer q >= 2.            (2.7)
```

#### Proof

The negative canonical function is always completely monotone because

```text
k_-(x) = Sum_{n>=1} exp(-n x).                         (2.8)
```

On the positive ray,

```text
k_{beta,+}(x)
 = 2 Sum_{n>=1} exp(-beta n x)
   - Sum_{m>=1} exp(-m x).                             (2.9)
```

Thus `k_{beta,+}` is the Laplace transform of the locally finite signed atomic measure

```text
eta_beta = 2 Sum_{n>=1} delta_{beta n}
           - Sum_{m>=1} delta_m.                       (2.10)
```

If `beta=1/q`, every negative atom at the integer `m` coincides with the positive atom indexed by `n=qm`; its net coefficient is `2-1=1`, while all remaining atoms have coefficient `2`.  Hence `eta_beta` is positive and `k_{beta,+}` is completely monotone.

Conversely, if `1/beta` is not an integer, the atom at rate `1` in (2.10) has coefficient `-1`.  If `k_{beta,+}` were completely monotone, Bernstein's theorem would represent it as the Laplace transform of a positive measure.  Uniqueness of the Laplace transform for locally finite measures with finite exponential transforms would force that positive measure to equal `eta_beta`, impossible because `eta_beta({1})=-1`.  This proves (2.7). QED.

This arithmetic split is sharper than the earlier rational/irrational D-finite split: rational indices `beta=p/q` with `p>1` are self-decomposable but not in `T(R)`.

### Corollary 2.3 — reciprocal-integer indices are finite log-gamma convolutions

If `beta=1/q`, let `G_{j,k}` (`1<=j<=q-1`, `k=1,2`) be mutually independent Gamma(`j/q`,1) variables and let `E_+,E_-` be independent Exp(1), independent of them.  Then

```text
X_{1/q}
 =_d 2q log[Gamma(1-1/q)/q]
      + log(E_+/E_-)
      - Sum_{j=1}^{q-1} [log G_{j,1}+log G_{j,2}].     (2.11)
```

Indeed Gauss multiplication gives

```text
Gamma(1-q s)
 = q^(-q s) Gamma(1-s)
   Product_{j=1}^{q-1}
      Gamma(j/q-s)/Gamma(j/q),                         (2.12)
```

and substituting (2.12) into (1.2) produces exactly the MGF of the right side of (2.11).

For `alpha=1` (`beta=1/2`), this specializes to one logistic variable plus two negative log-Gamma(1/2) variables and an explicit shift.  This does not yield an elementary quantile, but it places the simplest interior case in a fully classical finite convolution family.

**B9 outcome:** successful.  The residual inverse distribution is self-decomposable for all indices, lies in the Thorin class exactly at reciprocal-integer beta, and has a finite log-gamma decomposition there.  None of these canonical-class identifications supplies a standard closed quantile for arbitrary beta, so source closure does not follow.

## 3. B13 FIND WHAT ONLY INCREASES — a physical tail-elasticity theorem for `alpha<=1`

The self-decomposable classification alone does not force an increasing hazard rate.  A stronger shape theorem is available on half of the stable-index range through Thomas Simon's multiplicative-strong-unimodality theorem.

Simon proves that a positive beta-stable law is multiplicatively strongly unimodal exactly when

```text
beta <= 1/2.                                           (3.1)
```

His criterion, combined with Ibragimov's strong-unimodality theorem, means that for `beta<=1/2` the random variable `log S` has a log-concave density.  The logistic variable

```text
L = log(E_1/E_2)
```

also has the strictly log-concave density

```text
f_L(x)=1/[4 cosh^2(x/2)].
```

Therefore, for `beta<=1/2`,

```text
X_beta = log S + log S' + L                            (3.2)
```

has a log-concave density, because convolution preserves log-concavity.

Define the auxiliary hazard/elasticity

```text
lambda_beta(a)
 := -a q_beta'(a)/q_beta(a).                           (3.3)
```

By (1.1), if `x=log a`, then

```text
q_beta(e^x)=P(X_beta>x),
```

and `lambda_beta(e^x)` is exactly the ordinary hazard rate of `X_beta` at `x`.  The survival function of a log-concave density is log-concave (for example by Prekopa's theorem applied to the half-line integral), hence its negative logarithmic derivative is nondecreasing.  Therefore:

### Theorem 3.1 — monotone hazard coordinate

For every

```text
0<beta<=1/2   (equivalently 0<alpha<=1),
```

`lambda_beta(a)` is nondecreasing on `(0,infinity)`.  Its endpoint values are

```text
lambda_beta(a) -> 0      as a downarrow 0,
lambda_beta(a) -> beta   as a -> infinity.             (3.4)
```

The right endpoint follows from the already proved exact asymptotic

```text
q_beta(a)
 = const * a^(-beta) [beta log a + O(1)].              (3.5)
```

The left endpoint follows from `q_beta(a)->1` and the continuous density of `X_beta` tending to zero at `-infinity`.

Now pass to the physical squared-radius tail `Q_beta(r)`.  Since

```text
log R_beta(a)
 = log a + beta^(-1)[log q_beta(a)-log C_beta],
```

we have

```text
d log R_beta / d log a
 = 1-lambda_beta/beta
 = (beta-lambda_beta)/beta.                            (3.6)
```

Define the completely physical logarithmic tail elasticity

```text
E_beta(r)
 := - d log Q_beta(r) / d log r
  = - r Q_beta'(r)/Q_beta(r).                          (3.7)
```

Using `Q_beta(R_beta(a))=q_beta(a)` and (3.6),

```text
E_beta(R_beta(a))
 = beta lambda_beta(a)/(beta-lambda_beta(a)).          (3.8)
```

The map `lambda -> beta lambda/(beta-lambda)` is increasing on `[0,beta)`.  Hence:

### Theorem 3.2 — monotone physical invariant

For every `0<alpha<=1`,

```text
E_beta(r) = -r Q_beta'(r)/Q_beta(r)
```

is nondecreasing from `0` to `+infinity` as `r` runs from `0` to `+infinity`.  Equivalently,

```text
t -> log Q_beta(exp(t))                                (3.9)
```

is concave on the real line.

In ordinary radius `rho`, let

```text
Qbar_alpha(rho)=1-mu_alpha{|z|<=rho}=Q_beta(rho^2).
```

Since

```text
-Qbar_alpha'(rho)=2 pi rho g_alpha(rho),
```

the invariant becomes

```text
H_alpha(rho)
 := -rho Qbar_alpha'(rho)/Qbar_alpha(rho)
  = 2 pi rho^2 g_alpha(rho)/Qbar_alpha(rho)
  = 2 E_beta(rho^2).                                   (3.10)
```

Thus `H_alpha` is nondecreasing for every `0<alpha<=1`.  In particular the physical tail is geometrically log-concave:

```text
Qbar_alpha(rho_1^theta rho_2^(1-theta))
 >= Qbar_alpha(rho_1)^theta Qbar_alpha(rho_2)^(1-theta)
```

for `rho_1,rho_2>0` and `0<=theta<=1`.

This is a genuine shape theorem for the BCC physical law, not an auxiliary-coordinate monotonicity statement.

### Exact limitation of this route

Simon also proves that the positive stable law ceases to be multiplicatively strongly unimodal when `beta>1/2`.  Therefore the log-concavity proof above stops exactly at `alpha=1`.  This does **not** prove that `X_beta` or `H_alpha` fails to be log-concave/monotone for `alpha>1`: convolution with the second log-stable term and the logistic term could restore log-concavity.  No such restoration theorem is proved here.

**B13 outcome:** successful restricted theorem.  It supplies a monotone physical invariant and geometric tail concavity throughout `0<alpha<=1`, but the mechanism does not presently cover `1<alpha<2`, so it does not close C0032.

## 4. B27 SWAP THE QUANTIFIERS — rational explicit formulas cannot have uniformly bounded holonomic complexity near an irrational index

Earlier R7-06 work proved:

1. if `beta=p/q` is rational in lowest terms, the auxiliary transform `q_beta(a)` is D-finite and satisfies an explicit polynomial-coefficient ODE obtained from a finite Mellin shift;
2. if `beta` is irrational, `q_beta(a)` is not D-finite.

B27 asks whether the rational ODEs might nevertheless stabilize into one uniformly bounded family as `p/q` tends to an irrational beta.  They cannot.

### Definition 4.1 — auxiliary holonomic complexity

Let `h(beta)` be the least integer `N` such that a nonzero relation

```text
Sum_{j=0}^m P_j(a) d^j/da^j q_beta(a) = 0             (4.1)
```

exists with

```text
m <= N,
deg P_j <= N for every j.
```

Set `h(beta)=infinity` if no such relation exists.

For rational `beta=p/q` in lowest terms, the explicit preceding Mellin-shift equation has order at most `2q` and polynomial degree at most `p`, hence

```text
h(p/q) <= 2q.                                          (4.2)
```

For irrational beta, the preceding non-D-finiteness theorem says `h(beta)=infinity`.

### Lemma 4.2 — local-uniform continuity in the stable index

Fix a compact `J subset (0,1)` and a compact `A subset (0,infinity)`.  For every fixed derivative order `j`,

```text
(beta,a) -> q_beta^(j)(a)
```

is continuous on `J x A`.

#### Proof

The exact Mellin transform is

```text
hat q_beta(s)
 = c_beta^(2s/beta)
   Gamma(s) Gamma(1-s/beta)^2 / Gamma(1-s),
       0<Re(s)<beta.                                   (4.3)
```

Choose a vertical inversion line `Re(s)=c` with `0<c<min J`.  Stirling's formula gives uniform exponential decay on that line; the net Gamma factor decays like

```text
exp[-pi |Im(s)|/beta]
```

up to a polynomial factor, uniformly for beta in `J`.  Multiplication by powers of `s` generated by any fixed number of `a`-derivatives preserves integrability.  Dominated convergence in the Mellin inversion formula therefore gives joint continuity, locally uniformly in `a`, for every fixed derivative order. QED.

### Theorem 4.3 — holonomic complexity blows up at every irrational index

Let `beta_0` be irrational in `(0,1)` and let `beta_n` be any sequence of rational numbers converging to `beta_0`.  Then

```text
h(beta_n) -> infinity.                                 (4.4)
```

#### Proof

Assume otherwise.  Then some subsequence has `h(beta_n)<=N` for a fixed finite `N`.  For each member of this subsequence choose an annihilating operator (4.1) with order and polynomial degrees at most `N`.  Pad missing coefficients with zero and normalize the finite coefficient vector of all `P_j` to Euclidean norm one.

These normalized coefficient vectors lie on a compact sphere in a fixed finite-dimensional vector space.  Pass to a further subsequence on which every coefficient converges.  The limiting polynomial tuple `(P_0,...,P_N)` is nonzero because the coefficient-vector norm remains one.

By Lemma 4.2, for every compact positive `a`-interval and every `j<=N`,

```text
q_{beta_n}^(j)(a) -> q_{beta_0}^(j)(a)
```

locally uniformly.  Passing to the limit in the exact ODEs gives

```text
Sum_{j=0}^N P_j(a) q_{beta_0}^(j)(a) = 0
```

for all `a>0`.  This is a nontrivial polynomial-coefficient linear ODE for `q_{beta_0}`, contradicting the established non-D-finiteness at irrational beta.  Therefore (4.4) holds. QED.

This proves that the increasing denominator in the rational Meijer-G/ODE formulas is not merely a bad choice of representation: **some finite linear holonomic complexity must diverge along every rational approximation of every irrational index.**  The existing explicit construction has `h(p/q)<=2q`; the theorem does not claim the matching lower rate `h(p/q)>=c q`.

### Differential-algebraic boundary

The original B27 question was intentionally broader than D-finiteness.  Rational physical tails are known from the preceding work to be D-algebraic, not necessarily D-finite.  The compactness argument above cannot rule out a uniformly bounded *nonlinear* differential-algebraic schema at irrational beta, because no non-D-algebraicity theorem is currently available for irrational `q_beta` or the physical `Q_beta`.  This is the exact surviving gap of B27; it is not papered over by the holonomic theorem.

**B27 outcome:** successful for the entire linear holonomic class, unresolved for nonlinear D-algebraicity.  Rational special-function formulas provably become unboundedly complex as one approaches any irrational index.

## 5. What these three methods change

The remaining BCC inverse is now more tightly classified:

- all indices: it is the quantile of an explicit **self-decomposable** law with canonical Levy density (2.2)-(2.3);
- reciprocal-integer beta: that law is in the **Thorin class** and is a finite convolution of standard log-gamma/logistic variables;
- `alpha<=1`: the corresponding physical BCC tail has the monotone invariant (3.10) and is geometrically log-concave;
- rational beta: the auxiliary exact formula is holonomic, but its minimal bounded order/degree complexity cannot remain bounded near any irrational beta;
- irrational beta: the previous non-D-finiteness obstruction remains in force.

None of these facts supplies an accepted all-index closed inverse.  They do, however, rule out two tempting simplifications: self-decomposability does not magically provide a named quantile, and rational Meijer-G formulas cannot converge to an irrational-index formula within any fixed finite holonomic template.

## 6. Dated literature/source checks — 2026-09-19

1. Charles Bordenave and Djalil Chafaï, *Around the circular law*, arXiv:1109.3343v4 / Probability Surveys 9 (2012), remains the source carrying the statement that the heavy-tailed limiting law is not known explicitly.
2. Charles Bordenave, Pietro Caputo and Djalil Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, arXiv:1006.1713v5 / CMP 307 (2011), remains the underlying PWIT/stable characterization.
3. Thomas Simon, *Multiplicative strong unimodality for positive stable laws*, Proc. AMS 139 (2011), arXiv:1002.4977, proves that positive beta-stable laws are MSU iff `beta<=1/2` and records the equivalence between MSU of a positive variable and strong unimodality of its logarithm.
4. I. A. Ibragimov, *On the Composition of Unimodal Distributions* (1956), supplies the classical strong-unimodality/log-concavity characterization.
5. The self-decomposable Levy-density criterion and the Thorin-class completely-monotone canonical-density criterion are classical; Bondesson's 1992 monograph and modern Levy-process references record them.  These ingredients are not claimed as new.
6. Fresh bounded searches on 2026-09-19 for the BCC heavy-tailed circular density, explicit `mu_alpha`, and 2024-2026 follow-up formulas did not surface a later all-radius source-matching closed density.  This is **negative evidence only**, not a novelty or openness certificate.

No novelty claim is made from a search miss.  The exact Levy calculation, Thorin arithmetic split, physical tail-elasticity theorem, and rational-complexity theorem above are derivations in this campaign and require independent audit before any external novelty claim.

## 7. Exact failures / gaps

1. Self-decomposability and even Thorin membership do not furnish a standard quantile function.
2. The physical monotone-invariant proof currently covers only `0<alpha<=1`; Simon's MSU mechanism fails beyond `beta=1/2`.
3. Holonomic complexity is proved to diverge near irrational beta, but nonlinear D-algebraicity at irrational indices is unresolved.
4. The source word “explicit” remains informal.  The existing exact Mellin/Stieltjes parameterization, direct nonlocal physical equation, and certified inversion are not unilaterally promoted here to source closure.
5. No independent P26 or distinct OTHER-track audit exists for C0032, and no closure paper package is claimed.

## 8. Suggested next mathematical attacks

Because the frozen `M_jet` metric has already saturated and this run is the third post-STUCK1 ordinary no-movement run, the **next** R7-06 iteration is required by protocol to be STUCK2 thinking-only rather than another ordinary research triple.  The exact STUCK2 blocker should be the all-index inverse/explicitness boundary, with the new information that self-decomposability, low-index log-concavity, and rational holonomicity do not remove it.

If STUCK2 authorizes one final recovery, the three next ordinary methods should be chosen there and must differ from B9/B13/B27.
