# Reciprocal degrees and the final comparison

Source: OpenAI, *Optimal-order mixing of the Thorp shuffle*, September 26, 2026, Sections 5–7, saved as [optimal-source.tex](optimal-source.tex). This note checks the representation-theoretic completion, assuming the averaged-marginal estimate of Proposition 4.2. It concerns n = 2^d only.

## 1. Reciprocal degrees

For a partition λ of s, let f^λ be its number of standard Young tableaux, equivalently the degree of the corresponding complex irreducible representation of S_s. We use the tableau interpretation and hook-length formula as the classical inputs stated in the source. Write p(u) for the number of partitions of u and

\[
R(s)=\sum_{\substack{\lambda\vdash s\\\lambda\notin\{(s),(1^s)\}}}(f^\lambda)^{-1}.
\]

We verify Lemma 5.1 by giving, for integers K ≥ 1 and s ≥ max(16,4K), the following majorant:

\[
\begin{split}
R(s)\le B(s,K):={}&2\sum_{u=1}^{K}\frac{p(u)}{\binom{s-u}{u}}
 +2\sum_{u>K}e^{3\sqrt u}3^{-u}\\
&+e^{3\sqrt s}2^{-\lfloor s/16\rfloor}
 +e^{3\sqrt s}(e/4)^s. \tag{1}
\end{split}
\]

The infinite tail in this bound is a convergent scalar series. The order of limits will be s → ∞ with K fixed, followed by K → ∞.

### Partition count

For u ≥ 1 set x = exp(−1/√u). Nonnegative coefficients and the partition generating product give

\[
p(u)x^u\le\prod_{j\ge1}(1-x^j)^{-1}.
\]

Taking logarithms of the product, expanding −log(1−z), and rearranging nonnegative sums gives

\[
\log\prod_{j\ge1}(1-x^j)^{-1}
 =\sum_{r\ge1}\frac1{r(e^{r/\sqrt u}-1)}
 \le\sqrt u\sum_{r\ge1}r^{-2}\le2\sqrt u.
\]

The first inequality uses e^y−1 ≥ y. For the last, 1+Σ_{r≥2}r^(−2) ≤ 1+∫_1^∞ y^(−2)dy = 2. Since x^(−u) = exp(√u),

\[
p(u)\le e^{3\sqrt u}. \tag{2}
\]

In particular e^(3√u)3^(−u) is summable: once √u ≥ 6/log 3 its exponent is at most −u log 3/2, and the remaining tail is bounded by a geometric series.

### Long row or column

Let L = max(λ_1,λ'_1). Transpose if necessary to make the first row have length L, and put u = s−L. Transposition preserves f^λ. Suppose 1 ≤ u ≤ s/4, so L ≥ 3u.

Place 1,…,u in the first u boxes of the top row. Choose u labels from the remaining L labels {u+1,…,s}; put the chosen labels, increasingly in row order, into the lower diagram of size u. Fill the remaining top-row boxes increasingly with the unused labels. The lower diagram has no column beyond u, since its total size is u. Every entry below the top row is larger than u, and row order makes all lower row and column inequalities hold. Thus every choice gives a standard tableau. Different choices give different tableaux, proving

\[
f^\lambda\ge\binom Lu
 =\prod_{j=0}^{u-1}\frac{L-j}{u-j}
 \ge(L/u)^u\ge3^u. \tag{3}
\]

The product inequality follows term by term from L ≥ u. For a fixed u, a diagram with a top row of length s−u is specified by its lower partition of u, so there are at most p(u) such shapes. Allowing the transpose gives at most 2p(u); ties and double counts only enlarge this upper bound.

For u ≤ K use the binomial bound in (3). For u > K use its 3^u bound and (2). This gives the first two terms of (1), even when the summation tail is extended beyond s/4. For each fixed positive u, binom(s−u,u) tends to infinity.

### Neither row nor column is very long

Suppose u > s/4 and L ≥ s/8. Let b = floor(s/16), so b ≥ 1, L ≥ 2b and u ≥ b. Retain the whole top row and the first b lower boxes in row order. This is a Young subdiagram: every row before the last retained row is complete, and the final partial row is no longer than the row above it. Hence the retained boxes form an order ideal for tableau inequalities.

Apply the same construction as in (3) with lower size b. Its binomial choice uses the L labels remaining after reserving 1,…,b on top. It gives at least binom(L,b) ≥ (L/b)^b ≥ 2^b tableaux of the retained diagram. Every such tableau extends to the original diagram: fill the omitted boxes with consecutive larger labels in row order. Because the retained diagram is an order ideal, this creates no reversed inequality. Therefore

\[
f^\lambda\ge2^{\lfloor s/16\rfloor}. \tag{4}
\]

There are at most p(s) shapes in this class, giving the third term of (1).

Finally suppose L < s/8. A hook at any box has length at most λ_1+λ'_1−1 ≤ 2L−1 < s/4. The hook-length formula yields

\[
f^\lambda>\frac{s!}{(s/4)^s}\ge(4/e)^s. \tag{5}
\]

Here log(s!) = Σ_{j=1}^s log j ≥ ∫_1^s log y dy ≥ s log s−s, proving the factorial lower bound used in (5). Since 4/e > 1, (2) gives the fourth term of (1).

These classes cover all shapes except u = 0, namely the row and column.

### Limit and uniformity

For fixed K the finite first sum in (1) tends to zero. The last two terms also tend to zero, because their logarithms are respectively

\[
3\sqrt s-\lfloor s/16\rfloor\log2,
\qquad 3\sqrt s-s\log(4/e),
\]

and both have a negative linear term. Thus

\[
\limsup_{s\to\infty}R(s)
 \le2\sum_{u>K}e^{3\sqrt u}3^{-u}\longrightarrow0.
\]

Consequently R(s) → 0. For s ≥ 2 the row and column are distinct and each has degree one, so the full reciprocal sum tends to 2. Each finite initial sum is finite, proving

\[
C_1:=\sup_{s\ge1}\sum_{\lambda\vdash s}(f^\lambda)^{-1}<\infty.
\]

At s = 1 the row and column coincide and the full sum is 1. No numerical value for C_1 has been computed or assumed.

## 2. From the marginal estimate to one common trimmed law

Assume Proposition 4.2: for μ = q_d^(200d), the expected TV error of a uniform ordered list of 7n/8 labels is at most ε_n, where

\[
\varepsilon_n=\frac{n^{3/2}}2
 \sqrt{(31/32)^{198d}+32e^{-n/256}}=O(n^{-5/2}).
\]

For d ≥ 3 choose a uniform ordered partition into eight blocks M_a of size n/8. Each complement is a uniform subset of size 7n/8; ordering it does not change its marginal TV distance. The expected sum of eight errors is at most 8ε_n, so some fixed partition has total error δ_n ≤ 8ε_n.

Let H_a permute labels in M_a and fix every other label. Two permutations g and g' agree on the complement of M_a exactly when g' = gh with h ∈ H_a. Thus the relevant marginal is the law of the coset gH_a. Put u_a = |H_a|/|S_n|. Remove every coset with μ(C) > 2u_a, for all a, and let E be the common retained set. For a removed coset,

\[
\mu(C)<2(\mu(C)-u_a).
\]

The sum of positive excesses over cosets is exactly marginal TV, so the removed mass r = μ(E^c) obeys r ≤ 2δ_n ≤ 16ε_n. For sufficiently large n, M = μ(E) = 1−r ≥ 1/2. The conditional law ν = μ(·|E) satisfies

\[
\|\mu-\nu\|_{\rm TV}=r,
\qquad \nu(gH_a)\le4u_a. \tag{6}
\]

The TV identity follows directly: outside E the absolute difference sums to r; inside E it sums to (1/M−1)M = r. A removed coset has no retained mass; every other coset had original mass at most 2u_a, giving the common cap in (6).

## 3. The Fourier input and its normalization

For an irreducible unitary representation ρ of degree D write ν̂(ρ) = Σ_g ν(g)ρ(g). The eight-block orbit argument gives

\[
\|\widehat\nu(\rho)\|_{\rm op}\le A D^{-5/16},
\qquad A=\sqrt{32C_1}. \tag{7}
\]

Here is the dependence on the degree lemma. Restrict ρ to the product of the eight block groups. Each tensor type has product dimension at most D, so assign its full isotypic component to a factor of degree at most D^(1/8). This makes an orthogonal decomposition into eight invariant spaces E_a. For a vector u_a in E_a, the orbit span W_a under H_a has dimension at most

\[
\sum_{\pi:\,\dim\pi\le D^{1/8}}(\dim\pi)^2
\le D^{3/8}\sum_{\pi\in\widehat H_a}(\dim\pi)^{-1}
\le C_1D^{3/8}.
\]

Multiplicity does not change the first bound: in an isotypic component V_π ⊗ A_π the orbit of one vector lies in the image of End(V_π) under Q ↦ (Q⊗I)u, which has dimension at most (dim π)^2. Equivalent copies must be grouped before summing.

The translated projection P_{ρ(g)W_a} is constant on gH_a. Its uniform average is (dim W_a/D)I by irreducibility and trace. The cap (6) bounds its ν-average by four times that uniform average. Cauchy–Schwarz therefore gives

\[
|\langle z,\widehat\nu(\rho)u_a\rangle|^2
\le4C_1D^{-5/8}\|z\|^2\|u_a\|^2.
\]

Taking square roots, summing over a and using Σ_a ||u_a|| ≤ √8 ||Σ_a u_a|| gives (7). This independently recovers the exponent (3/8−1)/2 = −5/16 and A² = 4·8C_1 = 32C_1.

For any probability σ on G = S_n, finite-group orthogonality gives

\[
4\|\sigma-U_G\|_{\rm TV}^2
 \le\sum_{\rho\ne\mathbf1}D_\rho
       \|\widehat\sigma(\rho)\|_{\rm HS}^2. \tag{8}
\]

To check the normalization, put a(g) = σ(g)−1/|G|. Cauchy–Schwarz says ||a||_1² ≤ |G|Σ_g |a(g)|². The regular character identity makes the latter equal to Σ_ρ D_ρ||Σ_g a(g)ρ(g)||_HS². The trivial transform vanishes; uniform measure has zero transform on every other irreducible. Here HS² is the ordinary unnormalized trace. Thus no factor of |G| is missing in (8).

## 4. Eight factors and sign

Convolution multiplies Fourier matrices. Since ||B||_HS² ≤ D||B||_op² and operator norm is submultiplicative, (7) gives

\[
\begin{split}
\sum_{\rho\ne\mathbf1,\mathrm{sgn}}D_\rho
 \|\widehat\nu(\rho)^8\|_{\rm HS}^2
&\le A^{16}\sum_{\rho\ne\mathbf1,\mathrm{sgn}}
 D_\rho^{2-16(5/16)}\\
&=A^{16}\sum_{\rho\ne\mathbf1,\mathrm{sgn}}D_\rho^{-3}
\le A^{16}R(n)\longrightarrow0. \tag{9}
\end{split}
\]

The exponent can also be checked by first bounding each eighth power's operator norm by A^8D^(−5/2), then squaring and multiplying by D twice: once from HS comparison and once from regular multiplicity. This gives D^(−5+2) = D^(−3). No normality or self-adjointness of ν̂(ρ) is used.

The degree-one sign representation cannot be handled by R(n). Conditional on all shuffle coins except one in the last physical step, flipping that coin transposes two output positions, reversing the sign. The two choices have equal probability, so μ̂(sgn) = 0. Trimming may destroy this cancellation, but

\[
|\widehat\nu(\mathrm{sgn})|
 =\frac1M\left|\sum_{g\notin E}\mu(g)\mathrm{sgn}(g)\right|
 \le\frac r{1-r}. \tag{10}
\]

A second bound follows from (6): a function bounded by one changes expectation by at most twice TV, so |ν̂(sgn)| ≤ 2r. Either bound tends to zero; (10) is the source's bound. Its contribution after eight factors is |ν̂(sgn)|^16.

Finally, left or right convolution by any probability is a TV contraction. Expanding μ^(*8)−ν^(*8) as a telescoping sum of eight terms gives TV at most 8r. Combining (8)–(10) proves the checkable conditional estimate

\[
\|\mu^{*8}-U_G\|_{\rm TV}
 \le8r+\frac12\sqrt{(32C_1)^8 R(n)
                  +\left(\frac r{1-r}\right)^{16}}. \tag{11}
\]

In particular, when 16ε_n < 1, substitution of r ≤ 16ε_n gives the valid, possibly loose bound

\[
\|q_d^{*(1600d)}-U_G\|_{\rm TV}
 \le128\varepsilon_n+
 \frac12\sqrt{(32C_1)^8R(n)
       +\left(\frac{16\varepsilon_n}{1-16\varepsilon_n}\right)^{16}}
 \longrightarrow0. \tag{12}
\]

The common trimmed law needs n sufficiently large that M ≥ 1/2 for (7); (12) is asserted in that range. Estimate (1) can replace R(n) in this bound. Each μ factor is 200d physical shuffles, so eight factors give 1600d. At those endpoints the cyclic coordinate frame equals the physical frame. Translating the initial permutation preserves TV from uniform.

## 5. Boundary cases and limits of the check

The tableau construction was checked at u = 1, u = s/4, L = s/8 and b = floor(s/16); the inequalities keep the required numbers of top and lower boxes. The middle-case retained diagram remains a Young diagram even when its last row is partial. Self-transpose shapes only cause harmless overcounting. Small s are excluded from the displayed majorant and handled by finiteness, including the coincident row/column at s = 1.

The sign coefficient of ν need not vanish; (10) expressly allows a trim correlated with parity. The Fourier calculation uses matrix norms rather than treating matrices as character scalars. All eight caps refer to one law ν, rather than eight differently conditioned laws. These are necessary distinctions in the completion.

No defect was found in the checked degree argument or in the completion conditional on Proposition 4.2 and the classical representation facts stated above. This is a local analytic audit, not a Lean build, an independent proof certificate for the complete preprint, or an argument for any non-dyadic deck size. The constants C_1 and A are finite but have not been numerically bounded here.
