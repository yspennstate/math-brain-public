# T336: literature boundary, polynomial-branch obstruction, and a normalization escape

Date: 23 October 2026. Author/reviewer: A28. No subagents. This report addresses
the literal uniform-over-all-real-labels approximation requirement and the
architecture restrictions under which a proposed obstruction is valid. It
also derives the requested exact layer-normalization construction. It does
not claim novelty, impossibility for general transformers, or a learning
theorem.

**Findings.** The obstruction is valid for finite affine/product/ReLU circuits
with a Gaussian parameter head and no input-dependent division, normalization,
or non-polynomial input features. It already applies to the continuous
rank-one kernel `k(x,x')=xx'`. Its proof does not require stabilizing activation
patterns along rays. It does not extend merely by calling an architecture
"semialgebraic": rational maps and layer normalization are counterexamples to
that terminology. An exact selective-layer-normalization plus product circuit
can compute the same posterior, and can compute every posterior for a known
finite-rank polynomial-feature GP. Ordinary transformer wiring remains a
separate implementation question.

## 1. Primary literature and exact locators

All PDFs below were opened or downloaded from primary author, publisher,
proceedings, or arXiv sources and their relevant statements read. PDF page
numbers mean printed page numbers unless otherwise indicated.

| ID | Primary source | Relevant locator and boundary |
|---|---|---|
| P1 | Telgarsky, [Benefits of depth in neural networks](https://proceedings.mlr.press/v49/telgarsky16.pdf), COLT 2016 | Definition 2.1, p.3; Lemma 2.3, p.4. Its specified gate class uses polynomial pieces selected by polynomial sign tests and includes ReLU, maximum and sum-product computations. This supplies established structural context, not the GP/KL conclusion below. |
| P2 | Telgarsky, [Neural networks and rational functions](https://proceedings.mlr.press/v70/telgarsky17a/telgarsky17a.pdf), ICML 2017 | Theorem 1.1, PDF p.1; Proposition 1.5, PDF p.2. Rational functions with denominators bounded away from zero admit compact-domain ReLU approximation; reciprocal approximation has quantitative resource restrictions. Compact coefficient approximation does not give uniform accuracy after multiplication by arbitrary labels. |
| P3 | Yun et al., [Are Transformers universal approximators of sequence-to-sequence functions?](https://arxiv.org/pdf/1912.10077v2), 25 February 2020, ICLR 2020 | Section 3, Theorems 2-3, p.4, and the definition of `d_p` immediately above. The metric is `L^p`, `1≤p<∞`, with compact support/domain. This is not a uniform-KL theorem over unbounded labels. |
| P4 | Ba, Kiros and Hinton, [Layer Normalization](https://arxiv.org/pdf/1607.06450v1), 21 July 2016 | Section 3, equation (3), p.2, with normalization equation (2). The mean and variance are over coordinates of one example. Section 4 below defines explicitly the added fixed epsilon convention used here. |
| P5 | Vaswani et al., [Attention Is All You Need](https://arxiv.org/pdf/1706.03762v5), 6 December 2017 | Section 3.1, p.3, uses residual connections followed by LayerNorm; Section 3.2.1, equation (1), p.4, uses softmax of scaled dot products. The original architecture is outside the polynomial-only circuit restriction. |
| P6 | Akyürek et al., [What learning algorithm is in-context learning? Investigations with linear models](https://arxiv.org/pdf/2211.15661v3), 17 May 2023, ICLR 2023 | Lemma 1, p.4; Theorem 2, p.5; Appendix C.6, Lemma 8, pp.24-25, equations (128)-(131). Close precedent: arithmetic primitives, ridge/Sherman-Morrison updates, and LayerNorm used for division. Its displayed division construction uses large constants and approximation, so it cannot simply be cited as a finite-constant uniform-all-label guarantee. |
| P7 | Müller et al., [Transformers Can Do Bayesian Inference](https://arxiv.org/pdf/2112.10510v7), 13 August 2024 revision of ICLR 2022 paper | Equation (2), Insight 1 and Corollary 1.1, p.4. Prior-data negative log likelihood corresponds to prior-averaged forward KL, up to a parameter-independent term. This objective differs from a supremum over datasets. |
| P8 | Rasmussen and Williams, [Gaussian Processes for Machine Learning, Chapter 2](https://gaussianprocess.org/gpml/chapters/RW2.pdf), MIT Press, 2006 | Weight-space posterior, equations (2.8)-(2.11), pp.9-11; GP predictive equations (2.22)-(2.24), p.16; scalar versions (2.25)-(2.26), p.17. These identify the posterior being represented. |
| P9 | Knill, [Cauchy-Binet for Pseudo-Determinants](https://arxiv.org/pdf/1306.0062v3), 18 June 2014 | Theorem 7 and Corollary 8, p.16. The ordinary-determinant polynomial identity sums products of matching minors, including the empty minor. Taking both matrices equal gives the sum of squares used below. No pseudo-inverse or pseudo-determinant is needed for the construction. |
| P10 | Boullé, Nakatsukasa and Townsend, [Rational neural networks](https://proceedings.neurips.cc/paper/2020/file/a3f390d88e4c41f2747bfa2f1b5f87db-Paper.pdf), NeurIPS 2020 | Section 2, equation (1), PDF p.2, defines trainable rational activations; Section 3 gives compact-domain approximation results. Rational gates are an established alternative architecture, not polynomial branches. |

The most directly relevant earlier constructive paper is P6. Its architecture
uses softmax and GeLU, with LayerNorm in the feed-forward sublayer (equations
(3)-(7), pp.2-3). Appendix C.6 explicitly ends with approximate scalar
division. The large-constant domination in that displayed argument is not
uniform as the numerator becomes arbitrarily large. This observation limits
what may be inferred for the present quantifiers; it is not a review of every
claim or possible implementation in that paper.

## 2. A precise obstruction and a short proof

Fix `s>0`, let `W~N(0,1)`, set `f(t)=Wt`, and observe
`Y=f(x)+ε` with `ε~N(0,s)` independent of `W`. The covariance kernel
`k(t,t')=tt'` is continuous and positive semidefinite. For `x∈[1,2]` and
query `t*=1`, the latent posterior is

```text
P_(x,y) = N(m(x,y),v(x)),
m(x,y)=xy/(x²+s),       v(x)=s/(x²+s).
```

For a fresh noisy response, replace the variance by `s+s/(x²+s)`; the mean
is unchanged. Both variances are positive and bounded on `[1,2]`.

Consider a fixed finite directed acyclic circuit whose input coordinates
are polynomial functions of `(x,y)` and whose gates are affine maps,
multiplication, and ReLU. Fixed coefficients such as `1/N` or `1/sqrt(d)`
are allowed. Fixed positional encodings for a fixed sequence length are
constants. Finite heads, residual sums, unnormalized dot-product attention,
and entrywise-ReLU attention with only fixed scaling all fit this model.
The circuit outputs a Gaussian mean `μ(x,y)`. Its variance head may be
arbitrary, provided it returns a finite positive variance `w(x,y)`.

**Claim.** The supremum of either Gaussian KL direction over
`x∈[1,2], y∈R` is infinite for every such finite mean circuit.

First, the mean is pointwise selected from a finite list of polynomials
`P₁(x,y),...,P_J(x,y)`. This follows directly by induction through the
finite circuit: affine combinations and products preserve a finite list,
and a ReLU replaces each possible polynomial by either that polynomial or
zero. It is not necessary to describe the sets on which the choices occur.

Let `a_j(x)` be the coefficient of `y` in `P_j(x,y)`. Each

```text
g_j(x)=(x²+s)a_j(x)−x
```

is a nonzero polynomial. Otherwise a polynomial `a_j` would satisfy
`(x²+s)a_j(x)=x` identically, impossible by degree (including the zero
polynomial case). Each `g_j` has finitely many real zeros. Choose a single
`x₀∈(1,2)` outside the finite union of these zero sets.

For every branch `j`,

```text
P_j(x₀,y)−[x₀/(x₀²+s)]y
```

is a nonconstant polynomial in `y`, since its linear coefficient is
nonzero. Its absolute value tends to infinity as `y→+∞`. There are only
finitely many branches, so the minimum of these absolute differences also
tends to infinity. Therefore

```text
|μ(x₀,y)−m(x₀,y)|→∞ as y→+∞,
```

regardless of how activation branches switch. This is stronger and simpler
than proving a common eventual activation region along the ray.

To pass from mean error `e=μ−m` to KL, the direct scalar Gaussian formula
gives

```text
KL(N(m,v) || N(μ,w))
 = (1/2)[log(w/v)+(v+e²)/w−1]
 ≥ (1/2)log(1+e²/v),
```

because the expression is minimized over all `w>0` at `w=v+e²`.
For the other direction,

```text
KL(N(μ,w) || N(m,v))
 = e²/(2v)+(1/2)[w/v−1−log(w/v)]
 ≥ e²/(2v).
```

Both lower bounds diverge on the fixed ray. Inflating the learned variance
cannot rescue a finite uniform forward-KL bound; a separate variance cap
is unnecessary for this obstruction.

For exactly `N>1` observations, fix `N−1` design locations and labels zero,
and vary one location `x` and its label `y`. If the fixed squared locations
sum to `c`, the query-one posterior mean is `xy/(x²+s+c)`, and the same
argument applies. One may choose a nontrivial subinterval avoiding the
fixed locations if distinct design points are required.

### Quantifiers and restrictions that must remain explicit

- The conclusion is for each fixed finite circuit, even if its size depends
  on the desired tolerance. It does not prevent pointwise convergence as
  size grows, prior-averaged consistency, or approximation on bounded labels.
- A continuum of variable design inputs is essential to this proof. At a
  fixed design the exact regression coefficient is just a real constant.
- An arbitrary nonlinear embedding or preprocessing operation can invalidate
  the finite-polynomial-list premise. In particular, normalizing inputs or
  precomputing a reciprocal must not be hidden in preprocessing.
- The KL step uses a Gaussian output family. Small KL between arbitrary
  distributions does not generally control the difference of their means.
  The proof as written does not cover every density or mixture head.
- A finite uniform error bound does not force an arbitrary predictor to equal
  the target everywhere: bounded additive errors are possible. What the
  polynomial-branch argument forces on an unbounded ray is the exact linear
  coefficient, which this restricted class cannot supply for all designs.

## 3. Architecture distinctions

| Operation or model | Covered by the obstruction? | Reason |
|---|---|---|
| Affine/product/ReLU circuit; fixed-size sums and averages | Yes | Finite polynomial output list |
| Unnormalized linear attention or ReLU attention scaled by fixed `1/N` | Yes | Matrix products and ReLU preserve that list |
| ReLU scores divided by their input-dependent row sum | No | This is a rational operation despite the ReLU name |
| Softmax attention | No | Exponentials and input-dependent normalization are outside the proof |
| LayerNorm or RMSNorm | No | Input-dependent reciprocal square roots are outside the proof |
| Reciprocal or general rational gate | No | It can represent the required coefficient directly |
| GeLU, sigmoid, tanh, or data-dependent sinusoidal features | No | These are not finite polynomial pieces; another argument would be required |
| Fixed positional sine/cosine values at fixed token positions | Yes | They are constants in the data variables |
| Adaptive computation with unbounded number of steps | No | No single finite list of polynomial branches is guaranteed |

Softmax is excluded from the obstruction; this alone is neither an exact
construction nor a proof of uniform approximation for a standard softmax
transformer. For example, compactly approximating the coefficient with
nonzero error and multiplying by `y` still has unbounded absolute error.

The term **semialgebraic** must not replace **finite polynomial pieces**.
The target itself has the semialgebraic graph
`(x²+s)z=xy`. Rational gates and positive-denominator square-root
normalization are also semialgebraic in the usual graph-based sense.
P1 deliberately defines a narrower gate family with polynomial pieces.

## 4. An exact rank-one LayerNorm construction

Use the following explicit convention, with fixed `ε_LN≥0`, unit gain and
zero bias:

```text
LNε(v)_i = (v_i−mean(v)) /
           sqrt[(1/d)Σ_j(v_j−mean(v))²+ε_LN].
```

Choose fixed positive constants `λ,c` satisfying
`c²+2ε_LN=λ²s`. Such constants always exist: for example, take `c=1` and
`λ²=(1+2ε_LN)/s`. Normalize the four-coordinate vector

```text
v=(λx,−λx,c,−c).
```

It has zero mean and normalization denominator

```text
D_LN²=(λ²x²+c²)/2+ε_LN=λ²(x²+s)/2.
```

Let `a=λx/D_LN` and `b=c/D_LN` be its first and third normalized
coordinates. Ordinary multiplication and fixed affine scaling give

```text
(λ/(2c))ab = x/(x²+s),
(sλ²/(2c²))b² = s/(x²+s).
```

Multiplying the first result by an unnormalized bypassed label `y` gives
the exact posterior mean. The second gives the exact latent variance;
adding `s` gives the noisy predictive variance. Every equality holds for
every real `x,y`, with finite fixed constants and any fixed nonnegative
normalization epsilon.

The permitted wiring is a label-independent normalized coefficient branch,
product gates, and a raw-label bypass to the final readout. This wiring
condition matters. Merely inserting LayerNorm into a conventional network
does not make an untouched label available to later computations. In a
pre-LN attention block, the value map may see only normalized labels; in a
post-LN architecture, a final normalized state followed by a fixed affine
head is bounded. Neither can be silently substituted for the stated circuit.

## 5. Exact finite-rank polynomial-feature GP construction

### 5.1. Model and permitted computation

Fix `N≥1`, feature dimension `r≥1`, and known noise variance `s>0`.
Let `φ:R^p→R^r` be a known polynomial feature map and use the zero-mean GP

```text
f(x)=φ(x)^T w,    w~N(0,I_r),
k(x,x')=φ(x)^Tφ(x'),
y_i=f(x_i)+ε_i,  ε_i iid N(0,s).
```

Write `Φ∈R^(N×r)` for the design matrix and `Φ*∈R^(Q×r)` for `Q` query
feature rows. Use a finite circuit with fixed real constants, affine maps,
products and one selectively applied LayerNorm. Only the design and query
features enter that LayerNorm branch; labels remain on a separate exact
linear readout path. The output is the mean and covariance of a Gaussian
predictive distribution. No online inversion or division gate is assumed.

Set

```text
H=sI_r+Φ^TΦ,    D=det H>0,    A=adj(H).
```

The familiar weight-space Gaussian calculation gives

```text
μ*=Φ* H^(−1) Φ^T y,
V_latent=sΦ* H^(−1) Φ*^T,
V_noisy=sI_Q+V_latent.
```

The task is therefore to produce `1/D`, since `H`, `A`, and the remaining
numerators are polynomial functions of the inputs. The noisy covariance is
positive definite even when the latent query covariance is singular.

### 5.2. A positive constant plus squares

For `k=1,...,min(N,r)` and index sets `I⊆[N]`, `J⊆[r]` with
`card(I)=card(J)=k`, define

```text
q_(I,J)=s^((r−k)/2) det(Φ_(I,J)).
```

Expanding `det(sI_r+Φ^TΦ)` in its principal minors and applying
Cauchy-Binet to each such Gram minor gives

```text
D=s^r+Σ_(k=1)^min(N,r) Σ_(I,J) s^(r−k)[det(Φ_(I,J))]²
 =s^r+Σ_(ℓ=1)^(M−1) q_ℓ²,                         (S1)
M=Σ_(k=0)^min(N,r) binom(N,k)binom(r,k)=binom(N+r,r).
```

The `k=0` term is the empty minor and contributes `s^r`. The last equality
is Vandermonde's identity. Formula (S1) is also the specialization of P9's
ordinary-determinant identity to `Φ/sqrt(s)`, multiplied by `s^r`.

Every `q_ℓ` is a polynomial in the input features, with a fixed real
coefficient depending on the known `s`. There are no data-dependent square
roots in preparing these channels. All determinant minors can be evaluated
by the finite Leibniz formula using only products, signs and sums.

### 5.3. Epsilon calibration and exact reciprocal

Take normalization width `d_L=2M` and fixed

```text
λ²=(1+Mε_LN)/s^r.
```

Apply `LNε` to

```text
v=(λq₁,−λq₁,...,λq_(M−1),−λq_(M−1),1,−1).
```

The mean is exactly zero. Its normalization denominator satisfies

```text
D_LN²=[λ²Σq_ℓ²+1]/M+ε_LN
     =λ²[s^r+Σq_ℓ²]/M
     =λ²D/M.
```

Let `z` be the normalized coordinate corresponding to the constant `+1`.
Then

```text
ρ=(λ²/M)z²=1/D.                                    (S2)
```

This is exact for every design, not an asymptotic approximation with a
large constant. The numerator calibration accounts for epsilon explicitly.
It also works at `ε_LN=0`, because the `±1` channels prevent zero variance.

If the normalizer must have a larger width `d_L≥2M`, append zero channels
and instead use

```text
λ²=(1+(d_L/2)ε_LN)/s^r,
D_LN²=(2λ²/d_L)D,
ρ=(2λ²/d_L)z².
```

Appending other nonzero registers, including labels, is not innocuous: it
changes the variance and destroys (S2) unless their contribution is included
in a new proven identity. The specified projection into a dedicated block
is part of the architecture.

### 5.4. Exact Gaussian output and a size bound

Compute the adjugate by polynomial cofactor formulas. With (S2), output

```text
μ*=ρ Φ* A Φ^T y,
V_latent=sρ Φ* A Φ*^T,
V_noisy=sI_Q+sρ Φ* A Φ*^T.                         (S3)
```

These agree exactly with the GP posterior for all real labels and all real
design/query inputs. Thus the Gaussian KL is zero, including uniformly over
all labels, for this explicitly enriched circuit class. Exactness is a
statement in real arithmetic; it is not a claim about floating-point error.

A simple explicit upper bound is enough to make finiteness reviewable. If
each coordinate of `φ` has at most `T` monomials of total degree at most
`d_φ`, its feature arithmetic costs `O((N+Q)rT max(1,d_φ))`. A sequential
Leibniz product evaluation for the nonempty minor channels uses at most

```text
Σ_(k=1)^min(N,r) binom(N,k)binom(r,k) k! max(k−1,0)
```

binary multiplication gates, plus affine sums and scalings. This is at
most `r r! M`. Forming `H` uses `O(Nr²)` operations; all its adjugate
cofactors use `O(r² r!)` by the same elementary method. Final matrix products
cost `O(Nr+Qr²+Q²r)` operations. Thus one coarse arithmetic bound is

```text
O((N+Q)rT max(1,d_φ)
  + r r! binom(N+r,r) + Nr² + r²r!
  + Nr + Qr² + Q²r),
```

with one normalization block of width `2 binom(N+r,r)` and polynomial
depth bounded by a sequential scheduling of these gates. This is polynomial
in `N` for each fixed `r`; no favorable bound jointly in growing `N,r` is
claimed. The constants `s` and `ε_LN` are known and fixed. A variable unknown
noise parameter would require a separate construction.

The cofactor and minor computations can be much smaller in particular
feature families. The bound above intentionally uses only elementary,
explicit division-free arithmetic, not an unproved efficient determinant
primitive.

### 5.5. Transformer compilation boundary

Sections 4–5.4 establish the stated arithmetic circuit with a designated
design-only normalization vector. This was a sufficient circuit interface,
not a proof that a projected-normalization primitive is necessary.
The completed `followup/T336_architecture_compiler.md` by A24 supplies a
stronger implementation: fixed-position residual ReLU attention with one
ordinary full-token pre-LayerNorm feed-forward residual sublayer. A scratch
token contains the minor pairs, special constant pair, and an immutable
position/balance pair. The feed-forward selector takes the difference of
the special normalized coordinates; that difference is identically zero
on source tokens, even though their normalization denominators see labels.
Raw source labels therefore remain untouched until the exact final linear
combination. No projected-normalization primitive is needed.

That compiler uses `λ²=(4+Dε_LN)/(2s^r)` at full embedding width `D`, because
the two constant pairs contribute four to the scratch squared norm. If `z`
is the normalized special-coordinate difference, it recovers the reciprocal
determinant as `λ²z²/(2D)`. These constants replace the simpler circuit
calibration when the additional registers are present; they do not alter
the determinant/SOS identity above. The cited compiler version has SHA256
`8dbb67bbc8609cb86b0a1fb888f61c64abf36b07c8ebfc0464b0d0e5a4adf175`.

The architecture boundary remains substantive. The compiler normalizes only
one specified feed-forward sublayer; its attention and other arithmetic
blocks are not pre-normalized. It is not a theorem for every-layer pre-LN,
post-LN, or softmax transformers. Exact coefficient computation and an exact
label-linear readout permit the all-real-label statement. Replacing their
final multiplication or routing by an approximation can restore unbounded
error.

## 6. What the literature comparison supports

The restricted obstruction is a direct consequence of established polynomial
gate structure and Gaussian formulas. P2 already makes clear that rational
functions are good compact-domain approximation targets for ReLU networks;
the unbounded label multiplier changes the required quantifiers. P3 does not
supply that change. P7's actual training objective is an average under the
prior, and can converge without convergence of the uniform supremum.

The constructive route also uses familiar ingredients: Gaussian linear
conditioning, determinant/adjugate formulas, Cauchy-Binet, and normalization
as an arithmetic operation. P6 is a particularly close precedent for
LayerNorm-based division and transformer ridge regression. This audit does
not establish that the particular paired-channel SOS implementation is new.

No claim about uniform learning from finite pretraining samples follows from
the exact representability in (S3). In particular, a trained coefficient
branch can be merely close to the exact one, and any nonzero coefficient
error may still make uniform KL infinite on unbounded labels. Prior-averaged
learning guarantees require their own statistical argument; A30 is treating
that question separately.

## 7. Source pins and checks

Downloaded primary PDF byte hashes (SHA256):

| ID | SHA256 |
|---|---|
| P1 | `d6ed34b06cca0b63e814309add254d2bc45a0066c40726d29f7c880ba02c2eba` |
| P2 | `ec4892f6bd9c5598cc7620bab650d4e492e0dec31c2c43d460bc1af952ed1b4b` |
| P3 | `9d1fd7ccf36a7600bfae1dc94b1cc69e6cc1302dd4bc2bfbfa6089ed532071ce` |
| P4 | `c464f839fb8d59f7fde92f9b4caa67c2d1f2f196b88f93fb60502249df0aaef7` |
| P5 | `bfaaec89262875f927cf1b38b2da2d775f3309b7bea3537f29b606ca67e79065` |
| P6 | `18f2a209349c75ec84b74f2b72d32d96e12a86ebad97f47602a9bd8ce4c24ca4` |
| P7 | `9736e7789e7f4b7dd7401b6017602be87410eb15c1b11f94065d88ba7fec5a9b` |
| P8 | `33eb573e1a15abbc04191cc57f74076e1df83024d14b934eebfac3b30a3f57ce` |
| P9 | `0a10d76bf619c39c911333e47f003f1efb1504c09a0bc648489488f6ee137e5a` |
| P10 | `42b0f56ad2b0dafda667c1263b44b1c050b76fc3804756ed355c237d126d36f7` |

The PDFs and text extractions used for inspection are under
`/tmp/a28_t336_sources/`. The pinned registry input is
`a02/T336_REGISTRY.json`, SHA256
`a62961f2c1f30287356a73e9609430d437e93ba42a85aaad85908fdbd2d5f7d6`;
its broad wording does not specify the restricted gate family or Gaussian
readout needed for the obstruction. I also visually checked the rendered
pages containing P4 equation (3), P6 Lemma 8, and P9 Theorem 7/Corollary 8
against their text extractions.

As a supplementary check, exact rational arithmetic verified (S1), the minor
count, the epsilon calibration and both unpadded/padded reciprocal formulas
in 96 cases with `1≤N,r≤4`, several positive rational noise variances,
`ε_LN∈{0,1/100000,7/3}`, and two block widths. These finite checks do not
replace the algebraic proof above.

Search coverage was targeted to polynomial/ReLU circuit structure, rational
approximation, transformer universality, LayerNorm division, constructive
in-context ridge regression, GP posterior formulas, and the all-minors
Cauchy-Binet identity. No exhaustive priority search or certification of
absence of prior work was performed.
