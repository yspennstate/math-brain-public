# B13 FEI block-profile route: coordinate product-rigidity theorem

Status: **PARTIAL toward full FEI. Full Friedgut--Kalai FEI remains OPEN.**

Run focus: APPROACH 2/13 (block-influence/correlation profiles and two-sided Booleanity constraints). This note does not rerun the settled read-once certificate and makes no novelty claim; prior-art status of the lemma below is unverified.

## 1. Universal coordinate rigidity

Let `f:{-1,+1}^n -> {-1,+1}` and let `X` be its spectral sample,

`P[X=S] = \hat f(S)^2`.

Fix a coordinate `i`, write `X_i=1_{i in X}` and `X_{-i}` for all the other spectral membership bits, and let

`q_i = P[X_i=1] = Inf_i(f)`.

### Theorem (spectral independence in one coordinate is rigid)

If `X_i` is independent of `X_{-i}`, then

`q_i in {0, 1/2, 1}`.

Equivalently, for every Boolean function and every coordinate with

`Inf_i(f) notin {0,1/2,1}`,

one has the strict two-sided Booleanity constraint

`I(X_i ; X_{-i}) > 0`.

This is dimension-free and uses Booleanity essentially.

### Proof

The cases `q_i=0,1` are already allowed, so suppose `0<q_i<1`.

Let `y in {-1,+1}^{n-1}` denote the variables other than `i`. For `R subseteq [n]\{i}`, let

`W_{R,0} = 2^n \hat f(R)`,   `W_{R,1} = 2^n \hat f(R union {i})`.

These are integers. Define the two Walsh polynomials on the `(n-1)`-cube

`A(y)=sum_R W_{R,0} chi_R(y)`,

`B(y)=sum_R W_{R,1} chi_R(y)`.

Fourier inversion gives

`f(y,+1)=2^{-n}(A(y)+B(y))`,

`f(y,-1)=2^{-n}(A(y)-B(y))`.

Both values on the left are signs. Hence

`|A(y)+B(y)|=|A(y)-B(y)|=2^n`.

Subtracting the squares yields `A(y)B(y)=0`. Therefore at each `y` exactly one of `A(y),B(y)` is nonzero, and the nonzero value has absolute value `2^n`.

Let

`a = #{y: B(y)=0}` and `b = #{y: A(y)=0}`.

Then `a+b=2^{n-1}`. Moreover `B(y)` is nonzero exactly when the two restrictions of `f` across the `i`-edge disagree, so

`q_i = Inf_i(f) = b/2^{n-1}`.

Now use the assumed independence of `X_i` and `X_{-i}`. For every `R`,

`P[X_{-i}=R,X_i=1] = q_i P[X_{-i}=R]`,

`P[X_{-i}=R,X_i=0] = (1-q_i) P[X_{-i}=R]`.

Since these probabilities are `W_{R,1}^2/2^{2n}` and `W_{R,0}^2/2^{2n}`, respectively,

`W_{R,1}^2 = (q_i/(1-q_i)) W_{R,0}^2`                                           (1)

for every `R`. In particular the two coefficients vanish together. Since `0<q_i<1`, at least one pair is nonzero, so from (1)

`r := sqrt(q_i/(1-q_i)) = |W_{R,1}|/|W_{R,0}|`

is rational. Write `r=u/v` with positive coprime integers `u,v`.

Parseval on the `(n-1)`-cube and (1) give

`sum_y B(y)^2 / sum_y A(y)^2 = u^2/v^2`.

But the pointwise Booleanity conclusion above gives

`sum_y B(y)^2 / sum_y A(y)^2 = b/a`.

Thus `b/a=u^2/v^2`. Because `u,v` are coprime, there is a positive integer `k` such that

`b=k u^2`,   `a=k v^2`.

Consequently

`2^{n-1}=a+b=k(u^2+v^2)`.

Hence `u^2+v^2` is a power of two. If one of `u,v` is even and the other odd, `u^2+v^2` is an odd integer greater than one, impossible. If both are odd, `u^2+v^2 == 2 (mod 4)`, so the only possible power of two is `2`, forcing `u=v=1`. Therefore `r=1`, hence `q_i=1/2`. This proves the theorem. QED.

## 2. Exact classification of product spectral laws

### Corollary

If the entire spectral law is a product law, then every spectral marginal belongs to `{0,1/2,1}`.

Let

`A={i:q_i=1}`,   `J={i:q_i=1/2}`.

The spectral law is then uniform on the affine coordinate subcube

`A triangle T`,  `T subseteq J`.

After multiplying `f` by the character `chi_A` and deleting coordinates with `q_i=0`, the remaining Boolean function on `J` has flat Walsh spectrum:

`|\hat g(T)| = 2^{-|J|/2}` for every `T subseteq J`.

Thus `g` is bent. In particular `|J|` is even (unless `J` is empty), because the unnormalised Walsh coefficients have magnitude `2^{|J|/2}` and are integers.

So the Boolean functions with exactly independent spectral membership bits are, up to irrelevant variables, multiplication by a character, and global sign, precisely bent functions on an even number of active half-marginal coordinates.

This explains the previous exact `n<=4` enumeration without promoting that enumeration to a proof. The observed counts decompose exactly as the classification predicts:

- `n=2`: 4 character cases plus 4 bent classes modulo global sign = 8;
- `n=3`: 8 character cases plus `C(3,2)*2*4=24` two-variable bent extensions = 32;
- `n=4`: 16 character cases plus `C(4,2)*4*4=96` two-variable bent extensions plus 448 four-variable bent classes modulo global sign = 560.

## 3. What this rules out for FEI

An arbitrary product random subset with tiny independent marginals has entropy

`H(X)=sum_i h(q_i)`

and can have `H(X)/E|X|` arbitrarily large as the marginals go to zero. The theorem shows that this canonical obstruction cannot be an exact Boolean spectral sample: exact independence with a genuinely nondeterministic coordinate forces marginal `1/2`, not a tiny marginal.

Thus Booleanity imposes a genuine two-sided correlation tax. In information form,

`q_i notin {0,1/2,1}  =>  I(X_i;X_{-i})>0`.

The remaining universal gap is **quantitative stability**. Strict positivity alone does not imply FEI. Writing total correlation

`TC(X)=sum_i h(q_i)-H(X)=D(P_X || product_i Bern(q_i))`,

FEI would follow from a dimension-free mechanism forcing enough total correlation whenever many marginals are small. A concrete sufficient target is to find a universal `C` and, for every Boolean spectral sample, an ordering `pi` such that

`sum_k I(X_{pi(k)} ; X_{pi(1)},...,X_{pi(k-1)})`

`    >= sum_k [ h(q_{pi(k)}) - C q_{pi(k)} ]_+ .`                      (2)

The left side is exactly `TC(X)`. The exact theorem above settles the zero-defect endpoint behind (2), but gives no dimension-free modulus away from independence. The integer-divisibility argument is inherently non-robust: a near-product law need not make the Walsh magnitude ratios exactly rational squares with a common ratio. That is the next obstruction to overcome, rather than another exact-product enumeration.

## 4. Next move on this route

Try to robustify the coordinate proof by replacing exact ratio equality

`|W_{R,1}|/|W_{R,0}| = constant`

with a weighted dispersion inequality for the log-ratios. The natural dispersion is exactly the mutual information `I(X_i;X_{-i})`. The desired next lemma is a Boolean lower bound on this dispersion in terms of the distance of `q_i` from `{0,1/2,1}`, with a summation rule compatible with total correlation rather than the generally larger sum `sum_i I(X_i;X_{-i})`.

No such quantitative bound is proved here. Therefore this run is **PARTIAL**, and full FEI remains **OPEN**.
