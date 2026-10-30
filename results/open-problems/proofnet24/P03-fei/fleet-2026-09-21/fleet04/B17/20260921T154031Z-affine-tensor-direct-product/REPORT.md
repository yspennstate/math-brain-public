# B17 FEI creative run — exact tensor additivity of affine-character influence and a no-amplification theorem

**Run:** `20260921T154031Z-B17-auto11`  
**Status:** **PARTIAL. Full uniform-cube Fourier entropy-influence remains OPEN / NOT PROVED.**  
**Brain label:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-side brain context was used.  
**Live role:** FEI new proof mechanisms.  
**Scientific source recovered at entry:** `yspennstate/math-open-problems` master `606eb5a033dff5458380d69c00481fe7d6b5112b`, followed by a freshness check immediately before delivery.

## 1. Named universal obstruction and why this is a different method

The preceding fleet04/B17 run introduced the affine/character orbit cost

\[
J_{\mathrm{aff}}(f)=\min_{(v_1,\dots,v_n)\text{ basis}}\sum_i
\frac{1-|\mathbb E_x f(x)f(x+v_i)|}{2},
\]

proved that it is exactly the minimum influence inside the invertible-linear-input/Walsh-character orbit of `f`, and reformulated FEI as `H(f) <= C J_aff(f)`.

That leaves a natural amplification question:

> Can tensor powers of a hard Boolean function become cheaper after **cross-block** affine mixing, so that one obtains a larger `H/J_aff` ratio (or a stronger recursive seed) than any individual factor?

This is not a cosmetic question. A tensor product lives on a much larger vector space, so its optimizing basis may contain directions with nonzero projections into several factors. A priori those mixed directions could defeat factor-by-factor basis minimization.

This run proves that they cannot. The mechanism is a direct-product theorem using (i) multiplicativity of Boolean autocorrelation and (ii) a determinant/Laplace-expansion partition lemma for bases of a direct sum. It is a composition/comparison argument, not another finite search or another local phase-cancellation estimate.

No publication-priority or novelty claim is made.

## 2. Exact direct-product theorem

Let `f:F_2^n->{+1,-1}` and `g:F_2^m->{+1,-1}`. Write

\[
c_f(v)=\mathbb E_x f(x)f(x+v),\qquad
j_f(v)=\frac{1-|c_f(v)|}{2}.
\]

For the disjoint product

\[
h(x,y)=f(x)g(y),
\]

one has

\[
c_h(v,w)=c_f(v)c_g(w).
\]

Hence, with `a=j_f(v)` and `b=j_g(w)`,

\[
\begin{aligned}
j_h(v,w)
&=\frac{1-|c_f(v)c_g(w)|}{2}\\
&=a+b-2ab.
\end{aligned}
\tag{2.1}
\]

Since `0<=a,b<=1/2`,

\[
j_h(v,w)\ge a,\qquad j_h(v,w)\ge b.
\tag{2.2}
\]

### Lemma 2.1 — basis partition in a direct sum

Let `B` be any basis of `V direct-sum W`, with `dim V=n`, `dim W=m`. Then there is a partition

\[
B=B_V\sqcup B_W,\qquad |B_V|=n,\quad |B_W|=m,
\]

such that the `V`-projections of `B_V` form a basis of `V`, and the `W`-projections of `B_W` form a basis of `W`.

**Proof.** Put the vectors of `B` as columns of an invertible `(n+m)x(n+m)` matrix `M`, with the first `n` rows corresponding to `V`. Expand `det M` by Laplace expansion across those first `n` rows. Over `F_2`,

\[
1=\det M=\sum_{\substack{S\subseteq B\\|S|=n}}
\det(M_{V,S})\,\det(M_{W,B\setminus S}).
\]

At least one summand is `1`. For that `S`, both minors are nonsingular. Take `B_V=S` and `B_W=B\setminus S`. ∎

### Theorem 2.2 — exact tensor additivity

\[
\boxed{J_{\mathrm{aff}}(f\otimes g)=J_{\mathrm{aff}}(f)+J_{\mathrm{aff}}(g).}
\tag{2.3}
\]

**Proof. Upper bound.** Take optimal bases `(v_1,...,v_n)` for `f` and `(w_1,...,w_m)` for `g`. The embedded vectors

\[
(v_1,0),\dots,(v_n,0),(0,w_1),\dots,(0,w_m)
\]

form a basis of `F_2^{n+m}`, and because `c_g(0)=c_f(0)=1`,

\[
j_h(v_i,0)=j_f(v_i),\qquad j_h(0,w_j)=j_g(w_j).
\]

Therefore `J_aff(h)<=J_aff(f)+J_aff(g)`.

**Proof. Lower bound.** Let `B` be an arbitrary basis of the product space and partition it as in Lemma 2.1. Using (2.2),

\[
\begin{aligned}
\sum_{(v,w)\in B}j_h(v,w)
&\ge
\sum_{(v,w)\in B_V}j_f(v)
+
\sum_{(v,w)\in B_W}j_g(w)\\
&\ge J_{\mathrm{aff}}(f)+J_{\mathrm{aff}}(g).
\end{aligned}
\]

Minimize over `B`. ∎

By induction,

\[
\boxed{
J_{\mathrm{aff}}\!\left(\bigotimes_{r=1}^k f_r\right)
=
\sum_{r=1}^k J_{\mathrm{aff}}(f_r).
}
\tag{2.4}
\]

## 3. Consequence: affine mixing cannot amplify the FEI ratio of a tensor product

For disjoint products the squared Fourier law is a product distribution, hence

\[
H(f\otimes g)=H(f)+H(g).
\tag{3.1}
\]

Together with Theorem 2.2,

\[
\frac{H(f\otimes g)}{J_{\mathrm{aff}}(f\otimes g)}
=
\frac{H(f)+H(g)}{J_{\mathrm{aff}}(f)+J_{\mathrm{aff}}(g)},
\tag{3.2}
\]

whenever the denominator is nonzero. Therefore the product ratio is a weighted average of the factor ratios:

\[
\boxed{
\frac{H(f\otimes g)}{J_{\mathrm{aff}}(f\otimes g)}
\le
\max\left\{
\frac{H(f)}{J_{\mathrm{aff}}(f)},
\frac{H(g)}{J_{\mathrm{aff}}(g)}
\right\}.
}
\tag{3.3}
\]

In particular, for every `k>=1`,

\[
\frac{H(f^{\otimes k})}{J_{\mathrm{aff}}(f^{\otimes k})}
=
\frac{H(f)}{J_{\mathrm{aff}}(f)}.
\tag{3.4}
\]

So **tensor power followed by an arbitrary cross-block invertible linear change and arbitrary Walsh-character twist cannot create a stronger FEI counterexample than the original factor**.

This directly closes one search branch left open by the preceding affine-orbit normalization: the exponentially larger `GL(kn,2)` orbit of a tensor power gives no additional denominator discount.

### Current hard seed

The preceding exact Numaro-seed calculation gave

\[
J_{\mathrm{aff}}(F)=I(F)=\frac{261}{128}.
\]

Therefore

\[
J_{\mathrm{aff}}(F^{\otimes k})=k\frac{261}{128}.
\tag{3.5}
\]

No balanced affine/character representative of `F^{\otimes k}` can have smaller influence, because `J_aff` is the minimum over the larger unrestricted orbit.

Thus direct tensoring of the current hard seed cannot improve its affine-normalized denominator. The recursive lower-bound score used for a balanced seed,

\[
\frac{H(F)}{I(F)-1},
\]

also does not benefit from first tensoring: with the standard balanced tensor power its corresponding value is

\[
\frac{kH(F)}{kI(F)-1},
\]

which decreases with `k` whenever `I(F)>1`.

## 4. Why the absolute value / character folding is structurally necessary

Define the *unfolded* linear-basis cost

\[
K_{\mathrm{lin}}(f)
=
\min_{(v_1,\dots,v_n)\text{ basis}}
\sum_i q_f(v_i),
\qquad
q_f(v)=\frac{1-c_f(v)}2.
\tag{4.1}
\]

Unlike `J_aff`, this quantity is **not additive** under products, because negative correlations in two factors can multiply to a positive correlation and make a mixed direction unexpectedly cheap.

The exact checker found the following nontrivial Boolean counterexample.

Take the three-bit function, in lexicographic integer order,

\[
f=(1,-1,-1,-1,1,1,1,1),
\]

and the two-bit function

\[
g=(1,-1,1,1).
\]

Then exact rational computation gives

\[
K_{\mathrm{lin}}(f)=\frac54,\qquad
K_{\mathrm{lin}}(g)=1,
\]

but

\[
\boxed{
K_{\mathrm{lin}}(f\otimes g)=2
<
\frac94
=
K_{\mathrm{lin}}(f)+K_{\mathrm{lin}}(g).
}
\tag{4.2}
\]

An optimizing product-space basis has unfolded directional costs

\[
\frac14,\frac14,\frac12,\frac12,\frac12.
\]

For the same two factors, folding restores exact additivity:

\[
J_{\mathrm{aff}}(f)=\frac34,\qquad
J_{\mathrm{aff}}(g)=1,\qquad
J_{\mathrm{aff}}(f\otimes g)=\frac74.
\tag{4.3}
\]

This counterexample shows that the absolute value in `j_f(v)`, equivalently the ability to twist by a Walsh character, is not just a convenient normalization. It removes a real sign-cancellation pathology that otherwise appears under tensor products.

## 5. Exact stress tests and boundaries

The accompanying standard-library checker uses exact `Fraction` arithmetic.

It exhaustively tested every globally-sign-normalized three-bit Boolean function (128 functions) against every globally-sign-normalized two-bit Boolean function (8 functions), for

\[
128\times8=1024
\]

distinct product pairs. For every pair it recomputed all directional autocorrelations, solved both minimum-weight binary-matroid basis problems by exact greedy rank, formed the five-bit product, and verified

\[
J_{\mathrm{aff}}(f\otimes g)=J_{\mathrm{aff}}(f)+J_{\mathrm{aff}}(g)
\]

exactly.

Boundary checks:

- a one-bit character has `J_aff=0`, consistent with twisting it to a constant;
- the three-bit one-point defect has `J_aff=3/4`, equal to ordinary influence;
- the two-bit quadratic phase `(-1)^(x_1 x_2)` has `J_aff=1`, while its spectral entropy is `2`, recovering the class ratio `2`.

Checker SHA-256:

`b75c3916534e17ebeae9b7e7ed756e345d7118e2a1cd1988da7d9290dd79073b`

Recorded output SHA-256:

`f801de98ec177614f538e3b9ac40b3119e39df276bf6949ba7d562e32d594136`

These finite checks are stress tests only; Theorem 2.2 is proved analytically above.

## 6. What this rules out, and the next mechanism

**Ruled out:** tensor-power amplification followed by arbitrary affine mixing and character twisting. Cross-block basis vectors do not beat the sum of the factor orbit minima.

**Also ruled out as a tensor-stable surrogate:** the unfolded basis cost `K_lin`; exact Boolean sign cancellation makes it strictly subadditive.

**Still open:** full FEI.

The next B17 mechanism should therefore leave at least one of the two operations used in the theorem:

1. leave disjoint tensor product, e.g. use a genuinely interacting outer composition whose autocorrelation is not multiplicative; or
2. leave affine/character gauge transformations, e.g. a controlled nonlinear phase transformation whose entropy cost and influence gain can both be quantified.

A particularly concrete target is to search for a nonlinear transformation `T` for which `H(Tf)` is explicitly comparable to `H(f)` but whose optimized directional disagreement is genuinely smaller than `J_aff(f)`. The direct-product theorem proves that no amount of linear cross-block mixing can provide that gain.

**Full FEI remains OPEN / NOT PROVED.**
