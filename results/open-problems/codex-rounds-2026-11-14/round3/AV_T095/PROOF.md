# Characteristic lengths for the Gamma crossing argument

This is a conditional derivation of the three lemmas in the characteristic-length section of OpenAI, *Strict convexity and differentiability of the planar exponential first-passage limit shape* (September 24, 2026), at repository revision `4eaee87548250b2682affda7d05d947c05554bae`. The local source is [source-scales.tex](source-scales.tex). The rare-fast-crossing and localized-travel assertions stated below are hypotheses here. Thus the conclusion does not prove differentiability or verify the whole manuscript.

## Hypotheses and notation

Give the unoriented nearest-neighbor edges of Z² independent Gamma(shape κ, rate λ) weights, where κ, λ > 0. Write P for their product law. Fix b ∈ [−1,1], u = (1,b), r(z) = z₂ − bz₁, and m₀ = μ(u) > 0, where μ is the deterministic time-constant norm. Let

\[
 f_+(z)=m_0z_1+a_+r(z),\qquad
 K=100(1+|a_-|+|a_+|).
\]

Only finiteness of a₋ and a₊ and the stated crossing inputs will be needed. Set H₊(P₀) = τ(P₀) − f₊(ΔP₀) for a finite path P₀; costs include every traversal.

For s ≥ 1 and a positive integer n, let

\[
 D(s,n)=\{z\in\mathbb Z^2:-n\le z_1\le2n,\ |r(z)|\le8s\}.
\]

Let E(s,n) be the event that some finite path from column 0 to column n has every vertex in D(s,n) and cost strictly below m₀n + Ks. Its endpoints may be any vertices on these columns inside D(s,n).

The two inputs, as stated in [source-crossings.tex](source-crossings.tex), are:

1. **Rare-fast crossings.** The probability that such a path in D(s,n) has H₊ < −s tends to zero whenever s → ∞ and n/s → ∞. This is the manuscript's `df:cr:rare-fast`, with A = 1, R = 8, and ε = 1. Denote this event by F(s,n).
2. **Localized travel.** For any fixed D, η, δ > 0, uniformly over deterministic lattice endpoints p,q with |q−p| ≤ Dt, the probability tends to one as t → ∞ that a path from p to q has cost at most μ(q−p)+ηt and stays within Euclidean distance δt of [p,q]. This is `df:cr:local-travel`.

## Conditional conclusion

For s = 2ᵏ,

\[
 \mathbb P(E(s,s^3))\longrightarrow0.
\]

For every fixed C > 0, uniformly over integers 1 ≤ n ≤ Cs,

\[
 \mathbb P(E(s,n))\longrightarrow1\quad(s\to\infty).
\]

Consequently, for any q₀ ∈ (0,1), for all sufficiently large k there is a first dyadic integer Lₖ with P(E(2ᵏ,Lₖ)) ≤ q₀. These lengths satisfy Lₖ ≤ 2³ᵏ and Lₖ/2ᵏ → ∞. Every smaller dyadic l has P(E(2ᵏ,l)) > q₀. There is an infinite set of indices K₀ such that, at each k ∈ K₀,

\[
 L_{k-j}\ge2^{-4j}L_k\qquad(0\le j\le k-k_0).
\]

Here k₀ is any index from which the lengths exist. No monotonicity of E(s,n) in n is asserted or used.

## Proof

### 1. The deterministic change of weights

Take n = s³. Choose a fixed η₀ > 0 so that

\[
 \eta_0m_0>K+16|a_+|+1.
\]

Set δ = η₀s/n = η₀/s² and α = 1−δ. For all sufficiently large s, 0 < δ ≤ 1/2. Multiply each internal edge weight of D(s,n) by α and leave every other edge unchanged. Let Q be the law of the resulting environment.

If P₀ witnesses E(s,n) before the change, then Δx(P₀)=n and |r(ΔP₀)| ≤ 16s, because each endpoint has transverse coordinate in [−8s,8s]. After the change its defect is strictly below

\[
 \begin{aligned}
 \alpha(m_0n+Ks)-m_0n-a_+r(\Delta P_0)
 &\le (K-\eta_0m_0+16|a_+|)s
       -\eta_0K\frac{s^2}{n}\\
 &<-s.
 \end{aligned}
\]

The same path remains in D(s,n), so it witnesses F(s,n) in the changed environment. The scaling counts repeated traversals correctly: every occurrence of every internal edge receives the same factor α. Thus

\[
 \mathbb P(E(s,n))\le Q(F(s,n)).
\]

### 2. The likelihood cost

The density of one original weight is

\[
 p(t)=\frac{\lambda^\kappa}{\Gamma(\kappa)}t^{\kappa-1}e^{-\lambda t},
 \quad t>0.
\]

A scaled weight ατ has density q(t) = α⁻¹p(t/α), so

\[
 R(t)=\frac{q(t)}{p(t)}
 =\alpha^{-\kappa}e^{-\lambda(\alpha^{-1}-1)t}.
\]

Both densities are positive on (0,∞), including when κ < 1. Hence there is no change of support. Direct integration yields

\[
 \begin{aligned}
 \mathbb E_P R(\tau)^2
 &=\alpha^{-2\kappa}\frac{\lambda^\kappa}{\Gamma(\kappa)}
   \int_0^\infty t^{\kappa-1}e^{-\lambda(2/\alpha-1)t}\,dt\\
 &=\alpha^{-2\kappa}(2/\alpha-1)^{-\kappa}
 =[\alpha(2-\alpha)]^{-\kappa}
 =(1-\delta^2)^{-\kappa}.
 \end{aligned}
\]

Let M be the number of distinct internal unoriented edges. There are 3n+1 possible integer columns. Each column contains at most 16s+2 vertices, independently of the phase of bz₁. The sum of internal degrees is at most four times the vertex count, and counts each internal edge twice. Therefore

\[
 M\le2(3n+1)(16s+2)\le2(4n)(18s)=144ns
 \qquad(n,s\ge1).
\]

The product Radon–Nikodym derivative depends on these M distinct edges, regardless of how often a witnessing path traverses them. Independence gives

\[
 \mathbb E_P\left(\frac{dQ}{dP}\right)^2
 =(1-\delta^2)^{-\kappa M}.
\]

For 0 ≤ x ≤ 1/4,

\[
 -\log(1-x)=\int_0^x\frac{dt}{1-t}
 \le\frac{x}{1-x}\le\frac43x\le2x.
\]

Using x = δ², the likelihood second moment is at most

\[
 \exp(2\kappa M\delta^2)
 \le\exp\left(288\kappa\eta_0^2\frac{s^3}{n}\right)
 =\exp(288\kappa\eta_0^2).
\]

All constants are fixed with respect to s. They need not be small.

Cauchy–Schwarz and the rare-fast input now imply

\[
 \mathbb P(E(s,s^3))
 \le Q(F(s,s^3))
 \le e^{144\kappa\eta_0^2}\mathbb P(F(s,s^3))^{1/2}
 \longrightarrow0,
\]

because s³/s = s² → ∞. The support f₊ and norm μ in F remain those of the original law P. No shape theorem or uniform estimate for Q has been invoked.

### 3. A second derivation of the probability cost

Let S be the sum of the M original weights. The Gamma convolution identity gives S ∼ Gamma(κM,λ); it follows directly by multiplying the Laplace transforms \((\lambda/(\lambda+t))^\kappa\). For a Laplace argument t ≥ 0 this identity follows from the same density integral with rate λ+t.

The product likelihood is

\[
 \frac{dQ}{dP}=\alpha^{-\kappa M}
        e^{-\lambda(\alpha^{-1}-1)S}.
\]

Taking its square and evaluating the single Laplace transform of S gives

\[
 \alpha^{-2\kappa M}
 \left(\frac{\lambda}{\lambda+2\lambda(\alpha^{-1}-1)}\right)^{\kappa M}
 =[\alpha(2-\alpha)]^{-\kappa M}.
\]

This agrees with the coordinate calculation. As an independent scale check, its logarithm is κM(δ²+O(δ⁴)); M = O(ns) and δ = O(s/n), giving O(s³/n). The cancellation of the linear δ term is essential. At n = s³ this stays bounded; n of order s² would only give an O(s) upper bound and would not support the same probability-transfer argument without a rate for P(F).

### 4. Uniformly likely short crossings

Fix C > 0. First consider any sequence with n → ∞ and 1 ≤ n ≤ Cs. Put q = (n,⌊bn⌋). Then q = nu+te₂ with −1 < t ≤ 0, whence

\[
 \mu(q)\le m_0n+\mu(e_2),\qquad |q|\le3n.
\]

Use localized travel at scale n with D = 3, error η₁ = K/(4C), and a fixed radius parameter

\[
 0<\delta_0\le\min\{1/4,1/(2C)\}.
\]

With probability tending to one, this gives a path from 0 to q with cost at most

\[
 \mu(q)+\eta_1n\le m_0n+\mu(e_2)+Ks/4<m_0n+Ks
\]

for sufficiently large s. Its tube has x-coordinates in [−δ₀n,n+δ₀n] ⊂ [−n,2n]. The segment [0,q] has r-coordinates in [−1,0], and the Euclidean Lipschitz constant of r is √(1+b²) ≤ √2. Hence every vertex in the tube has

\[
 |r|\le1+\sqrt2\delta_0n
 \le1+\frac{\sqrt2}{2}s<8s
\]

for sufficiently large s. This path witnesses E(s,n).

For a sequence of bounded n, say n ≤ N, choose for each n a fixed coordinate path from 0 to (n,⌊bn⌋) with 0 ≤ x ≤ n. The finitely many chosen paths have bounded transverse extent. Each has finite cost almost surely, so their maximum cost is a finite random variable. The allowance Ks tends to infinity, so all these paths satisfy the required cost and localization bounds with probability tending to one.

To see uniformity, suppose it failed. There would be sᵢ → ∞, integers 1 ≤ nᵢ ≤ Csᵢ, and ε > 0 with P(E(sᵢ,nᵢ)) ≤ 1−ε. The integer sequence nᵢ has either a bounded subsequence or a subsequence tending to infinity. Each possibility contradicts the corresponding preceding argument. This proves the joint uniform limit.

### 5. First dyadic thresholds

Fix q₀ ∈ (0,1). For all sufficiently large k, the cubic estimate gives P(E(2ᵏ,2³ᵏ)) ≤ q₀. Thus the nonempty set of acceptable dyadic integers has a least element Lₖ, and Lₖ ≤ 2³ᵏ.

If Lₖ/2ᵏ did not tend to infinity, some subsequence would have Lₖ ≤ C2ᵏ for a fixed C. The uniform short-crossing result would then imply P(E(2ᵏ,Lₖ)) → 1 along that subsequence, contrary to its being at most q₀ < 1. Every dyadic l < Lₖ has probability greater than q₀ by minimality. This argument does not assume a monotone crossing probability.

### 6. Record scales and the endpoint input

Define Aₖ = Lₖ2⁻⁴ᵏ. Then 0 < Aₖ ≤ 2⁻ᵏ → 0. A positive sequence tending to zero has infinitely many strict running minima: otherwise its last running minimum would be a positive lower bound for all later terms. At a record index k, for 0 ≤ j ≤ k−k₀,

\[
 L_k2^{-4k}\le L_{k-j}2^{-4(k-j)}.
\]

Multiplication by 2⁴⁽ᵏ⁻ʲ⁾ gives exactly Lₖ₋ⱼ ≥ 2⁻⁴ʲLₖ. Writing Lₖ = 2ᵐ gives m ≤ 3k and m−k → ∞.

For the meshes in the earlier endpoint argument, let J be fixed and J ≤ j ≤ ⌈(m−1)/4⌉. If lⱼ = 2ᵐ⁻⁴ʲ⁻¹ > 1, the record comparison yields

\[
 l_j=2^{-4j-1}L_k\le\tfrac12L_{k-j}<L_{k-j}.
\]

At the terminal mesh lⱼ = 1, the same strict inequality eventually holds because k−j ≥ k/4−1 → ∞ and Lₕ/2ʰ → ∞. Thus each grid crossing trial has probability greater than q₀ by the definition of Lₖ₋ⱼ. Its use requires no monotonicity of Lₖ.

## Boundary checks

All arguments are for a fixed κ,λ > 0 and fixed supporting data. Uniformity as κ or λ varies is not needed. The likelihood identity remains valid for κ < 1, where the density is unbounded near zero. The coefficient 16 in the tilt is the full endpoint transverse range 8s−(−8s). The factor 144 in the final Cauchy–Schwarz estimate is half the exponent bound 288 for the second moment. Translation of the finite region changes neither its edge-count bound nor the product-law calculation.

The two crossing hypotheses remain unproved here. Conditional on them, no defect was found in the characteristic-length reduction or in its record-scale interface with endpoint extensions. The finite-region tilt relies on the Gamma likelihood; no corresponding assertion for every continuous law follows from this derivation.
