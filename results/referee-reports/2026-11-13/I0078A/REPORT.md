NO_PROGRESS

# I0078: number rigidity, transport, and negative-exponent Riesz gases

The precise conjecture for the interval-background limits in the source is not settled by this work. There is a relevant 2026 theorem: **periodic** thermodynamic limits have finite square-integrable lattice matching at every positive inverse temperature. It rules out the proposed positive-temperature threshold for that periodic construction. It does not identify those limits with the source's construction; the 2026 paper explicitly leaves that identification open. Consequently, substituting periodic limits would not be a counterexample to the source conjecture.

No new large-beta or small-beta direction for the source's limits is proved here. The classification is therefore NO_PROGRESS, rather than PARTIAL or RESOLVED_IN_LITERATURE. The distinction between the two constructions is essential to this classification.

## 1. Exact source and statement

The arXiv listing identifies **David Dereudre and Rafaël Digneaux**, *Rigidity of one-dimensional point processes via optimal transport*, **arXiv:2510.17257 [math.PR]**. The second author's initial is R., not T.

| Version | Submission time in the listing | Verified PDF length | Relevant locations |
|---|---|---:|---|
| [2510.17257v1](https://arxiv.org/abs/2510.17257v1) | Monday, 20 October 2025, 07:44:55 UTC | 24 pages, numbered 1–24 | Theorem 2.2 p.7; Theorems 2.7–2.8 p.9; Conjecture 2.9 p.10 |
| [2510.17257v2](https://arxiv.org/abs/2510.17257) | Monday, 21 September 2026, 14:48:09 UTC | 26 pages, numbered 1–26 | Theorem 2.1 p.8; Theorems 2.6–2.7 p.10; Conjecture 2.8 p.10 |

The listing supplies the title, authors, identifier, versions and submission times. The page counts above were checked against the actual PDF streams; the v1 abstract listing does not itself state a page count. Page-marked text and listing text for both versions are saved in `sources/`.

The requested v1 statement is:

> For −1 < s < 0, there exists β₀(s) > 0, decreasing in s, such that for β > β₀(s) we have Wass₁(Pₛ,ᵦ, Lebℝ) < +∞, whereas for 0 < β < β₀(s) we have Wass₁(Pₛ,ᵦ, Lebℝ) = +∞.

This is Conjecture 2.9, p.10. **The 2026 version changes “decreasing” to “increasing”** and renumbers the statement as Conjecture 2.8, still on p.10. It continues to present the transition as conjectural. Neither version specifies behavior at β = β₀(s). This report does not silently replace the v1 wording by the corrected wording.

### What Pₛ,ᵦ denotes

Put a = −s. For −1 < s < 0, we have 0 < a < 1 and the source uses

\[
 g_s(r)=-|r|^{-s}=-|r|^a.
\]

On Λₙ = [−n/2,n/2], with exactly n particles γ, its neutral Hamiltonian is

\[
 H_{n,s}(\gamma)=\frac12\iint_{\Lambda_n^2}g_s(x-y)\nu(dx)\nu(dy),
 \qquad \nu=\gamma-\operatorname{Leb}|_{\Lambda_n}.
\]

The three contributions are particle-particle interaction, particle-background interaction, and background self-energy, with the background of density one. The particle-particle term is a sum over **unordered** pairs. The finite law is

\[
 P_{n,s,\beta}(d\gamma)=Z_{n,s,\beta}^{-1}
       e^{-\beta H_{n,s}(\gamma)}\operatorname{Bin}_{n,\Lambda_n}(d\gamma).
\]

The construction then tiles ℝ by length-n intervals, puts independent copies of this finite law in different tiles, and shifts the tiled configuration by an independent uniform variable on a length-n interval. Pₛ,ᵦ denotes an accumulation point of these stationary laws in the **local topology**, tested against local measurable functions with at most linear growth in the local particle count. It has intensity one. This is v1 §1.2 p.5, equations (17)–(20) and Theorem 2.7 p.9; existence is proved in §5.3, pp.17–18.

**It is not defined there by periodic pair interactions.** Nor is uniqueness proved: the source explicitly allows more than one accumulation point and does not prove convergence of the whole sequence. Thus Pₛ,ᵦ is not a uniquely identified law in this range. Any assertion for “the” gas must specify its selection or apply to every such limit.

The alternative potential |r|⁻ˢ/s is gₛ(r)/a. At inverse temperature β_alt for that alternative convention, the corresponding inverse temperature in the source convention is β_DD = β_alt/a. The neutral background must be retained when changing conventions; the naked infinite pair sum is not a definition of the gas.

### What Wass₁ means

It is an expected transport cost **per unit length**, allowing a joint stationary coupling of the laws and a jointly translation-covariant coupling q of their realizations:

\[
 \mathsf{Wass}_1(P,R)=\inf\mathbb E
       \int_{[0,1]\times\mathbb R}|x-y|\,q(dx,dy).
\]

For R = Lebℝ the second marginal is deterministic Lebesgue measure. This is equivalent to the two-level, expanding-window formulation in v1 equation (6), p.6; the stationary-coupling representation is justified by Erbar–Huesmann–Jalowy–Müller, Proposition 1.2, PDF p.4. It is not the total transport cost between two infinite measures, and not an ordinary Wasserstein distance between probability measures on ℝ.

Let Pℤ be the law of ∑ⱼδⱼ₊ᵤ with U uniform on [0,1). Centered unit cells give Wass₁(Pℤ,Lebℝ) = 1/4. The triangle inequality therefore makes finiteness to Lebℝ equivalent to finiteness to Pℤ. In one dimension, v1 Lemma 1.6, p.7, turns finite cost into an ordered stationary lattice matching with integrable displacements. Conversely, such a matching immediately bounds the cost by the mean absolute displacement.

## 2. What the literature actually establishes

All page references below are **PDF page numbers in the saved texts**, unless journal pages are explicitly specified. Search and access date: 13 November 2026.

| Paper and exact location | Result relevant here; restriction that matters |
|---|---|
| Dereudre–Digneaux v1, Theorem 2.2 p.7; Lemma 1.6 p.7 | Finite Wass₁(P,Pℤ) implies number rigidity and a cyclic factor. The proof of number rigidity is pp.10–11. This is sufficient, not necessary; Remark 2.3 p.8 gives failure of the converse. |
| Same, Theorem 2.7 p.9 | Existence of interval-background accumulation points for −2 < s < 0, all β > 0; no uniqueness claim. |
| Same, Theorem 2.8 p.9; Lemma 5.7 pp.18–20; §5.8 pp.20–21 | For −2 < s ≤ −1 and every β > 0, every gas constructed there has finite Wass₂ to Pℤ, bounded interval counting variance, number rigidity and a cyclic factor. This does not include −1 < s < 0. |
| [Boursier, *Optimal local laws and CLT for the circular Riesz gas*, 2112.05881v6](https://arxiv.org/abs/2112.05881), Theorem 1 p.3, Theorems 2–3 pp.4–5, Corollary 1 p.5 | Gap and count concentration, variance expansion and counting CLT for **0 < s < 1**. Mesoscopic interval variance grows as a positive constant times Lˢ. Indicators satisfy the required fractional Sobolev condition in this positive-s range. These hypotheses exclude the present negative-s range. |
| [Boursier, *Decay of correlations and thermodynamic limit for the circular Riesz gas*, 2209.00396v5](https://arxiv.org/abs/2209.00396), Theorem 1 p.3, Theorems 3–4 pp.3–4, Corollary 1.1 p.4 | Positive-exponent circular gases: gap covariance decay with exponent 2−s, convergence of the microscopic process, and for 0 < s < 1, Var N(0,L] = σ²Lˢ + o(Lˢ), σ² = cot(πs/2)/(2βπs), in that paper's ordered-pair energy normalization. No negative-s theorem. |
| [Lewin, *Coulomb and Riesz gases: The known and the unknown*, 2202.09240](https://arxiv.org/abs/2202.09240), §IV.C pp.45–49, Theorem 40 p.47; §VI.B and Figure 5 pp.67–68 | Periodic thermodynamic functions and discussion of the expected negative-s phase diagram. The equality of periodic and container thermodynamic functions in (115) is stated for s > max(0,d−2); it supplies no identification of the point-process limits at negative s in d = 1. Even equality of free-energy values would not, alone, identify limiting laws. |
| [Lelotte, *Phase transitions in one-dimensional Riesz gases with long-range interaction*, 2309.08951](https://arxiv.org/abs/2309.08951), §3 pp.13–20, especially §3.2.1 pp.15–17 | Numerical evidence for fluid/quasisolid/crystal regimes at −1 < s < 0. The small-wave-number exponent is estimated numerically and the screening argument is formal. No theorem proving a temperature transition or a number-variance asymptotic. |
| [Leblé–Serfaty, *Large Deviation Principle for Empirical Fields of Log and Riesz Gases*, 1502.02970](https://arxiv.org/abs/1502.02970), interaction range p.2; Theorem 1 p.4; Corollary 1.2 p.5 | Empirical-field LDP and free-energy variational characterization of Sineβ. The Riesz case has max(0,d−2) ≤ s < d; it does not provide a negative-s number-variance law or ensemble identification here. |
| [Dereudre–Hardy–Leblé–Maïda, *DLR equations and rigidity for the Sine-beta process*, 1809.03989](https://arxiv.org/abs/1809.03989), Theorem 1.1 pp.4–5 | Number rigidity and canonical DLR equations for Sineβ, β > 0. Number rigidity does not assert finite lattice displacement. |
| [Erbar–Huesmann–Leblé, *The one-dimensional log-gas free energy has a unique minimiser*, 1812.06929v1](https://arxiv.org/abs/1812.06929v1), Theorem 1 and Corollary 1.1 p.2 | Uniqueness of the free-energy minimizer, namely Sineβ. In the journal version, CPAM 74 (2021), 615–675, these are Theorem 1.1 and Corollary 1.2, journal p.617. This is not a theorem that Sineβ has finite Wass₁ to Lebesgue. |
| [Huesmann–Sturm, *Optimal transport from Lebesgue to Poisson*, 1012.3845](https://arxiv.org/abs/1012.3845), Theorem 1.1 p.2 and discussion pp.2–3 | Existence/uniqueness of optimal equivariant transport when the cost is finite; the quadratic case is an allocation into cells. Corollary 1.4 p.5 gives the one-dimensional unit-intensity Poisson threshold p < 1/2, so in particular its L¹ and L² costs are infinite. Published in Ann. Probab. 41 (2013), 2426–2478. |
| [Huesmann, *Optimal transport between random measures*, 1206.3672](https://arxiv.org/abs/1206.3672), Theorem 1.1 p.2 | General stationary random-measure transport framework; absolutely continuous source and finite cost yield an optimal map under the stated assumptions. Journal: AIHP Probab. Stat. 52 (2016), 196–232. |
| [Huesmann, arXiv:1510.03601](https://arxiv.org/abs/1510.03601), Theorem 1.1 p.2, Theorem 1.3 p.2; proof of 1.3 pp.7–8 | The L¹ obstruction is unbounded E|N[0,L)−L|. The variance criteria in Theorem 1.1 concern 0 < p < 1 and include CLT/regularity assumptions for the lower bound. Examples on p.2 give infinite L¹ cost for Sineβ, despite logarithmic variance and number rigidity. The arXiv title has the typo *Tranport estimates for random measures in dimension one*; the journal title is *Transport cost estimates for random measures in dimension one*, ECP 21 (2016), paper 46. |
| [Dereudre–Vasseur, *Number-Rigidity and β-Circular Riesz gas*, 2104.09408](https://arxiv.org/abs/2104.09408), Theorem 1.11 p.8 | For d−1 < s < d, constructs a circular limit whose inside count, given the exterior, has all nonnegative integer values with positive probability. Thus a non-rigid limit exists; in d = 1 this is 0 < s < 1, not the negative-s range. |
| [Ghosh–Peres, *Rigidity and tolerance in point processes: Gaussian zeros and Ginibre eigenvalues*, 1211.2381](https://arxiv.org/abs/1211.2381), Theorem 6.1 pp.13–14 | A vanishing-variance criterion for smooth linear statistics gives rigidity of the corresponding inside statistic. This is not a bounded-variance criterion for sharp interval counts, and not an L¹ transport theorem. |
| [Aizenman–Goldstein–Lebowitz, *Bounded fluctuations and translation symmetry breaking in one-dimensional particle systems*, math-ph/0007022](https://arxiv.org/abs/math-ph/0007022), Theorem 2.1 pp.7–8; Theorem 3.1 pp.14–15; construction pp.16–18 | Tight discrepancy gives a stationary primitive and a cyclic factor; the discussion of L¹-bounded discrepancies gives an integrable primitive. Tightness alone does not give its first moment. |
| [Dereudre–Flimmel–Huesmann–Leblé, *(Non)-hyperuniformity of perturbed lattices*, 2405.19881](https://arxiv.org/abs/2405.19881), Theorems 1–2 p.2 | In d = 1, integrable dependent lattice displacements imply hyperuniformity; square-integrable displacements imply bounded number variance. The second-moment condition for the latter implication is sharp. |
| [Huesmann–Müller, *Gap metrics for stationary point processes and quantitative convexity of the free energy*, 2509.08659v1](https://arxiv.org/abs/2509.08659v1), Theorem 1.5 p.4 | Uniqueness of free-energy minimizers for logarithmic and positive-exponent 0 < s < 1 Riesz interactions. Its gap metric and exponent range do not identify the negative-s ensembles or settle their positional matching cost. |
| [Touzo–Le Doussal–Schehr, *Spatio-temporal fluctuations in the passive and active Riesz gas on the circle*, 2411.01355](https://arxiv.org/abs/2411.01355), §II.A.1, equation (8), p.7; discussion p.8 | The weak-noise linearized theory predicts bounded negative-s displacements. The low-temperature expansion is not an all-temperature proof for the nonlinear Gibbs measure. |

### The relevant 2026 citing paper

[**Yan Ru Pei, *Uniform displacement bounds and Gibbs limits for periodic one-dimensional Riesz gases*, arXiv:2609.28503v1**](https://arxiv.org/abs/2609.28503v1), submitted **15 September 2026, 01:55:59 UTC**, **21 pages**. The manuscript is dated 14 September 2026. It cites Dereudre–Digneaux v1 as reference [5].

Its Theorem 1.1, p.2, proves, for the particle-Palm periodic ensemble with 0 < a = −s < 1,

\[
 \mathbb EY_i=i,\qquad \mathbb E|Y_i-i|^2\le C_a/\beta
\]

uniformly in N and i, together with exponential tails. Theorem 1.2, p.3, passes this to **every periodic subsequential limit**, retaining an ordered stationary matching

\[
 \xi=\sum_{j\in\mathbb Z}\delta_{j+U+q_j},\qquad
 \mathbb E q_0^2\le K=C_a/\beta.
\]

Thus Wass₂(Pper,Pℤ) ≤ √K and Wass₁(Pper,Lebℝ) ≤ √K + 1/4 at every β > 0. Corollary 1.4, p.3, proves

\[
 \sup_I\operatorname{Var}\xi(I)
 \le \bigl(2\sqrt{2K+\sqrt K}+1/2\bigr)^2.
\]

Theorem 1.3, p.3, also gives canonical Gibbs equations for the full-line interaction. It does not prove uniqueness. Its introduction, p.1, explicitly distinguishes its periodic approximants from the source's interval-background approximants and leaves equality of the resulting ensembles open. The canonical Gibbs property alone is not that equality.

Accordingly, a version of the conjecture formulated **only for these periodic limits** is resolved in the literature: there is no positive β₀ separating finite and infinite cost. This restricted conclusion must not be promoted to the source's Pₛ,ᵦ.

Exact-identifier, author-pair, title and conjecture searches located this relevant 2026 citing paper. No further primary paper deciding Conjecture 2.9 for the interval construction was located. This is a search result, not a claim of exhaustive citation indexing.

### Answer to the counting-variance question

| Construction/range | What can be asserted |
|---|---|
| Source's interval-background gas, −1 < s < 0 | The argument in §3.1 below gives Var N(0,L] ≤ Cₛ,ᵦL¹⁺ˢ for every β > 0. No bounded-variance theorem or sharp asymptotic for these limits was found. In particular, an asymptotic cL⁻ˢ with c > 0 is impossible for s < −1/2. |
| Pei's periodic limits, −1 < s < 0, every β > 0 | Uniformly bounded interval variance, by Corollary 1.4. No growth as L⁻ˢ or log L. Boundedness is an upper bound, not convergence to a positive constant along every sequence of lengths. |
| Source's limits, −2 < s ≤ −1, every β > 0 | Uniformly bounded interval variance and finite Wass₂, Theorem 2.8. |
| Sineβ, s = 0, every β > 0 | Logarithmic counting variance; infinite Wass₁ to Lebesgue. |
| Boursier's circular limit, 0 < s < 1, every β > 0 | Variance asymptotic σ²Lˢ and a nondegenerate counting CLT; hence infinite Wass₁. |

In particular, **L⁻ˢ is not a printed negative-s variance law that one may import from Boursier**. There the exponent is s > 0. The regularity of interval indicators also changes at s = 0, preventing direct analytic continuation of the count theorem.

## 3. Checked arguments and attempted routes

### 3.1 A variance upper bound for the actual source construction

The following consequence of the printed energy estimates can be proved for **every** source limit, without replacing its approximants. Novelty of this general Fourier estimate is not claimed. It does not give either L¹ direction of Conjecture 2.9.

Fix −1 < s < 0 and β > 0. Put a = −s and

\[
 C_s=2\Gamma(1+a)\sin(\pi a/2)>0,\quad
 A_s=\frac1{(a+1)(a+2)},\quad B_s=\frac{2^{2-s}}{C_s}.
\]

Then

\[
 \boxed{\operatorname{Var}_{P_{s,\beta}}N(0,L]
 \le B_s(\beta^{-1}+A_s)L^{1+s}\quad(L>0).}
\]

**Proof.** First, the cell comparison underlying source Lemma 5.2, pp.16–17, gives

\[
 Z_{n,s,\beta}\ge e^{-n(1+\beta A_s)}.
\]

Indeed, restrict ordered particles to their respective unit cells. Their normalized product-cell law has expected neutral energy nAₛ: different-cell contributions cancel against the background after averaging, and each cell contributes ½∬[0,1]²|x−y|ᵃ dx dy = Aₛ. The binomial probability factor is n!/nⁿ ≥ e⁻ⁿ, and Jensen gives the bound. Since f(β)=−log Z is concave with f(0)=0,

\[
 \mathbb E H_{n,s}=f'(\beta)\le f(\beta)/\beta
 \le n(\beta^{-1}+A_s).
\]

This argument, also used for equation (62), source p.20, is valid throughout −2 < s < 0; it does not require s ≤ −1.

For a fixed configuration set ν=γ−Leb|Λₙ, extended by zero outside Λₙ. Source equation (49), p.16, reads

\[
 H_{n,s}=\frac{C_s}{4\pi}\int_{\mathbb R}|\widehat\nu(k)|^2|k|^{s-1}\,dk.
\]

Let χL=1[0,L]. Its transform satisfies

\[
 |\widehat\chi_L(k)|^2\le\min(L^2,4/k^2),\qquad
 |\widehat\chi_L(k)|^2|k|^{1-s}\le 2^{1-s}L^{1+s}.
\]

For the last inequality, set q=|k|L and split at q=2. On q ≤ 2 use q¹⁻ˢ; on q ≥ 2 use 4q⁻¹⁻ˢ. Both are bounded by 2¹⁻ˢ precisely in the present range −1 < s < 0. Plancherel therefore gives the deterministic estimate

\[
 \int_{\mathbb R}|(\chi_L*\nu)(x)|^2\,dx
 \le B_s L^{1+s}H_{n,s}.
\]

It remains to check the boundaries and the limit. In the stationary tiling law, a length-L observation interval lies in one tile except for a fraction L/n of the uniformly shifted observation locations, for n > L. On the interior locations its discrepancy is one of the convolutions above (up to translating or reversing χL). For the bounded local function

\[
 F_M(\xi)=\min\{(\xi((0,L])-L)^2,M\}
\]

we thus have

\[
 \mathbb E_{P^{\rm stat}_{n,s,\beta}}F_M
 \le B_s L^{1+s}\frac{\mathbb E H_{n,s}}n+\frac{ML}{n}.
\]

Local convergence along the defining subsequence applies to F_M. Send n → ∞ **at fixed M**, then M → ∞. This yields the boxed inequality because the limiting intensity is one. Truncation avoids any unproved uniform integrability assertion at tile boundaries. This completes the proof.

For s < −1/2 the exponent 1+s is strictly smaller than −s. Consequently this bound excludes Var N(0,L] ∼ c(s,β)L⁻ˢ with c(s,β) > 0 in that half of the interval. It does not exclude logarithmic growth or bounded variance.

A further checked consequence of Huesmann's Theorem 1.1(i), p.2, is finite mean transport cost with exponent q for every

\[
 0<q<\frac{1-s}{2}<1.
\]

Choose q < p < (1−s)/2. The bound gives √Var N(0,n] · nᵖ⁻¹ → 0, so the theorem applies. Since the endpoint q=1 is outside this interval for every fixed s > −1, this does not establish finite Wass₁, even at large β. It establishes hyperuniformity and subunit transport moments for all source limits, not a new temperature regime in the conjecture.

### 3.2 The primitive is not the discrepancy pinned at zero

Write D(t) = ξ((0,t])−t for t ≥ 0 and use signed counts for t < 0. A stationary primitive is a field C(t), possibly on a stationary extension, satisfying

\[
 D(t)=C(t)-C(0).
\]

The anchored field D has D(0)=0; requiring D itself to be stationary would incorrectly exclude nontrivial examples. Finite transport needs an integrable choice of the unanchored field or, equivalently, an integrable stationary ordered matching. Tightness without moment control does not establish this.

For any stationary transport of finite mean cost c from Lebesgue to ξ, the expected mass crossing a deterministic cut is at most c. To see the normalization, integrate crossing mass over all cut locations: a transported pair (x,y) contributes |x−y|, exactly its cost. Stationarity turns this into a per-unit-length identity. The discrepancy of an interval is the difference of its two boundary currents, so

\[
 \mathbb E|\xi((0,L])-L|\le 2c.
\]

Taking the infimum over transports proves the first-moment obstruction in Huesmann's Theorem 1.3. Conversely, Aizenman–Goldstein–Lebowitz's stationary-primitive construction, pp.16–18, retains integrability when these first moments are uniformly bounded; monotone allocation from that primitive gives finite L¹ cost. This also explains why **uniformly bounded counting variance is sufficient**, by Cauchy–Schwarz. There is no additional tail assumption needed after a uniform second-moment bound has actually been proved.

For completeness, a direct second-moment construction checks that last assertion. If supₜ E D(t)² ≤ V, let

\[
 A_T=\frac1T\int_0^T D(t)\,dt.
\]

Then ||A_T||₂ ≤ √V. If θₕ shifts the configuration to the left by h, the cocycle identity gives, for fixed h > 0,

\[
 A_T\circ\theta_h=A_T-D(h)+R_{T,h},\qquad
 \|R_{T,h}\|_2\le 2h\sqrt V/T.
\]

Take a weakly convergent subsequence in L², with limit A. Then D(h) = A−A∘θₕ. Set C(t)=−A∘θₜ. The identity holds first at rational times simultaneously and then with the right-continuous counting version. F(t)=t+C(t) is nondecreasing with integer jumps. Its generalized inverse allocates each unit interval between successive values of F to its corresponding particle. This allocation is translation covariant; its mean absolute cost is E|C(0)| ≤ √V, by the crossing-area identity. Unit density in each ergodic component follows from D(t)/t → 0 and the ergodic theorem. Thus no particles or Lebesgue mass are left unmatched.

What is missing is a uniform bound V for the source's −1 < s < 0 limits. The estimate in §3.1 grows as L¹⁺ˢ and does not provide one.

### 3.3 Divergent variance alone is insufficient

A useful counterexample to that inference, **not to the Riesz conjecture**, is a mixture of stationary clustered lattices. Let M be integer-valued with P(M=m)=c m⁻ᵖ, 2 < p < 3. Conditional on M=m, put mass m at each point of mℤ+Uₘ, with Uₘ uniform on [0,m). This is a stationary intensity-one point process in the counting-measure convention permitted by the source.

Sending each centered cell of length m to its central atom costs m/4 per unit length. Hence its L¹ cost is at most E M/4 < ∞. Conditional on M=m, with r the fractional part of L/m,

\[
 \operatorname{Var}(N(0,L]\mid M=m)=m^2r(1-r).
\]

For m > L this equals mL−L². Summing over m > 2L gives a lower bound of order L³⁻ᵖ. The upper bound follows by using m²/4 for m ≤ L and mL for m > L. Therefore Var N(0,L] is of order L³⁻ᵖ and diverges, although the L¹ cost is finite. The conditional mean is always L, so no variance-of-the-conditional-mean term was omitted.

To infer infinite cost from v(L)=Var N(0,L] → ∞, a nondegeneracy statement is needed. For example, if D(L)/√v(L) has a nondegenerate Gaussian weak limit, its probability of exceeding some fixed positive magnitude is bounded below. Consequently E|D(L)| ≥ c√v(L) → ∞. Uniform integrability is needed for a precise first-moment asymptotic, **not** for this lower bound. Another sufficient condition is E D(L)⁴ ≤ C v(L)², since Hölder then gives E|D(L)| ≥ √v(L)/√C. No such negative-s growing-variance theorem for the source process was found.

### 3.4 Rechecking the periodic all-temperature proof

The load-bearing part of Pei's proof was followed rather than inferred from its abstract:

1. The periodic kernel has curvature
   \[
   g_N''(r)=a(1-a)\sum_{\ell\in\mathbb Z}|r+\ell N|^{a-2}>0,
   \quad 0<r<N.
   \]
   The image series and its normalization are checked in §2.1, pp.4–5.
2. On the ordered particle-Palm chamber the Gibbs density is log-concave. Cyclic symmetry makes every gap's mean equal to one. A length-R arc of k gaps obeys E R² ≤ 2k² and E R²⁻ᵃ ≤ 2⁽²⁻ᵃ⁾/² k²⁻ᵃ: Lemma 2.1 p.5.
3. The grounded Hessian is a conductance Laplacian and its inverse diagonal is an effective resistance. The preceding bound controls **expected reciprocal conductance**. A fixed deterministic flow, admissible in every realization, gives E R_c(0,i) ≤ Bₐ R_w(0,i), wᵢⱼ=d_N(i,j)ᵃ⁻²: Lemma 2.2 p.6. This avoids the invalid replacement of E[Hess⁻¹] by (E Hess)⁻¹.
4. The deterministic Laplacian eigenvalues are bounded below by a constant times (min(m,N−m)/N)¹⁻ᵃ. Hence its resistance is bounded by a constant times
   \[
   \frac1N\sum_{m=1}^{\lfloor N/2\rfloor}(N/m)^{1-a}=O_a(1).
   \]
   The exponent of m in the sum is a−1 > −1: pp.6–7.
5. Convex-domain Brascamp–Lieb, with the truncated chambers removed in the stated order, bounds Var Yᵢ by β⁻¹E R_c. Log-concavity gives exponential tails: pp.7–9.
6. Joint extraction of labels, displacements and phase prevents loss of distant labels and preserves the selected process limit: pp.9–10.
7. For the ordered matching, all segments crossing a cut point in the same direction. If B segments cross, their lattice origins imply B(B−1)/2 ≤ sum of the absolute crossing displacements. Stationarity gives E of that sum = E q₀² and E B = E|q₀|. Thus E B² ≤ 2K+√K. Comparing currents at the interval endpoints and adding the lattice variance ≤ 1/4 gives Corollary 1.4: Lemma 3.1 and its proof, p.11.

These steps prove a printed result for the periodic ensemble. They supply no new direction for the source's ensemble. In particular, Pei's low-temperature restriction on a Fourier-amplitude lower bound is separate from the all-temperature matching bound.

### 3.5 Exponents and the two failed source-gas routes

The harmonic calculation around the lattice has springs of order |i−j|⁻²⁻ˢ. The displacement stiffness is therefore

\[
 \lambda(k)\asymp |k|^{1+s},\qquad
 \mathbb E|\widehat u(k)|^2\asymp\beta^{-1}|k|^{-1-s}.
\]

For −1 < s < 0 the infrared integral ∫₀¹ k⁻¹⁻ˢ dk = 1/(−s) is finite. The corresponding smooth density structure factor behaves as |k|²/λ(k) = |k|¹⁻ˢ. Its contribution to the sharp-count variance is bounded; the infrared correction has scale Lˢ, not growth L⁻ˢ. At s = 0 the integral is logarithmic. For 0 < s < 1 its cutoff gives Lˢ growth. The signs agree with the rigorous positive-s theorem, the log-gas endpoint, and the periodic negative-s theorem. Extending a low-temperature harmonic approximation to all temperatures of the source gas would nevertheless require a nonlinear estimate.

A direct repetition of the source's energy argument also stops at a precise point. For neutral charges its Riesz energy has Fourier weight |k|ˢ⁻¹, whereas the quadratic transport/discrepancy energy has weight |k|⁻². Their ratio is

\[
 |k|^{-2}/|k|^{s-1}=|k|^{-1-s},
\]

which is unbounded near k = 0 for −1 < s < 0. An extensive expected-energy bound therefore does not by itself give an extensive quadratic transport bound. Multiplying the energy by a large fixed β does not remove this infrared loss.

There is also a concrete obstruction to transferring Pei's proof to the source finite gas. In the ordered interval chamber the Hessian is

\[
 L_c+\operatorname{diag}\left[
 a\{(x_i+n/2)^{a-1}+(n/2-x_i)^{a-1}\}\right],
\quad c_{ij}=a(1-a)|x_i-x_j|^{a-2}.
\]

It is positive, so convexity is available. However, the background and walls destroy the cyclic re-rooting symmetry used to set every expected gap equal to one. The needed uniform arc-moment/resistance estimate for these nonperiodic finite laws has not been proved here. Invoking the periodic estimate at this point would assume the missing comparison.

For the proposed small-beta direction, convergence to Poisson as β ↓ 0 at fixed finite volume would not establish a statement at fixed β > 0 in infinite volume. The order of limits matters. The all-positive-beta periodic theorem already shows why that shortcut is unreliable. No lower bound on the source's mean absolute discrepancy was obtained.

## 4. Computation as a check

The code uses the periodic ensemble, with s = −1/2 and **g(r) locally −√|r|**, in the same unordered-pair normalization as Pei and the source. It does not simulate the interval-background construction.

`code/periodic_check.py` ran at nice 10, with one BLAS/OpenMP thread, on N = 32,64,128 and β = 0.25,4. For each pair it used lattice and uniform initializations, 1200 Metropolis sweeps, 400 discarded sweeps, and 100 measurements per chain. Elapsed time was about 62 seconds; memory was far below 4 GB. The saved chains are too short to certify mixing.

The kernel was evaluated from the convergent image-kernel expansion

\[
 g_N(r)-g_N(0)=N^a\left[-t^a-
 2\sum_{j\ge1}\binom a{2j}\zeta(2j-a)t^{2j}\right],
 \quad t=d_{\mathbb T_N}(r,0)/N\le1/2,
\]

truncated at j = 18. This is not a minimum-image approximation to the interaction.

For each configuration, the counting variance was integrated over the observation origin without Monte Carlo sampling of that origin. For L ≤ N/2 and geodesic pair distances dᵢⱼ,

\[
 \operatorname{Var}_{\rm origin}N[0,L]
 =L-L^2+\frac2N\sum_{i<j}(L-d_{ij})_+.
\]

Both starts averaged together give:

| N | β | L=1 | L=2 | L=4 | L=8 | L=16 |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 0.25 | 0.7958 | 1.3085 | 1.8813 | 2.2449 | 2.4342 |
| 64 | 0.25 | 0.7941 | 1.3090 | 1.9039 | 2.4311 | 2.7721 |
| 128 | 0.25 | 0.7851 | 1.2884 | 1.8681 | 2.3583 | 2.6248 |
| 32 | 4 | 0.3952 | 0.4535 | 0.4893 | 0.5154 | 0.5249 |
| 64 | 4 | 0.4013 | 0.4543 | 0.4971 | 0.5162 | 0.5276 |
| 128 | 4 | 0.3996 | 0.4557 | 0.4895 | 0.5154 | 0.5306 |

The high-beta data flatten over these lengths. Low-beta data show stronger residual growth on the accessible scales. Neither behavior proves an asymptotic law; the table cannot distinguish eventual saturation from slow growth and cannot identify the two infinite-volume ensembles. In particular, no power-law exponent was fitted and presented as evidence of a proof.

Independent checks in `code/audit_checks.py`:

- Compared the periodic kernel against 40-digit Hurwitz-zeta evaluation at 15 points across three volumes: maximum absolute error 1.32×10⁻¹³. The 18-term versus 14-term grid check was 3.35×10⁻¹¹ or less.
- Verified the spatial variance formula independently by exact integration over its 2N jump locations. A unit lattice gives zero for integer L and 1/4 for half-integer L.
- Compared grounded Laplacian inverse diagonals with the Fourier resistance formula at N = 16,32,64 and a = 1/4,1/2,3/4: maximum difference 6.44×10⁻¹⁵; all satisfied the printed deterministic upper bound.
- Checked the interval-background Hessian against finite differences in a separate six-particle example: maximum entry error 9.45×10⁻⁷.
- Verified the deterministic convolution/energy inequality in §3.1 in 36 cases, using exact integration of the piecewise affine finite-volume discrepancy and the real-space energy. Also compared the two Gamma-function formulas for Cₛ. These numerical checks supplement the Plancherel proof; they do not replace it.

Raw measurements, block diagnostics and final configurations are in `data/mc_*.npz`; tabulated measurements are in `data/periodic_variance.csv`. Block errors are diagnostics, not rigorous confidence intervals. Resource settings, seeds and checks are recorded in JSON. Reproduce with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 code/periodic_check.py` and then `python3 code/audit_checks.py`, from a shell already at nice 10 or greater.

## 5. What remains

The bound Var N(0,L] ≤ Cₛ,ᵦL¹⁺ˢ and the resulting finite q-moments for q < (1−s)/2 are genuine deductions for the source construction, but do not prove either requested L¹ direction. A proof of that conjecture would need, for example, an integrable stationary displacement/primitive estimate for its limits, or a theorem transferring the periodic estimate to those limits. A proof of infinite cost would need unbounded mean absolute discrepancy for those limits. Neither was established here. Neither the monotonicity correction in v2, nor finite-size behavior, nor the periodic canonical Gibbs equations closes that gap.

Twenty full source texts, plus seven arXiv listings, are saved as plain text. `data/source_manifest.json` records source URLs, PDF page counts, hashes of the transient PDF bytes, and hashes of the retained texts. PDF bytes were parsed in memory and never written as files; no PDFs, scans or page images are retained. Some extraction warnings concern rotated text or fonts; the main statements were cross-checked against arXiv HTML where available, and ambiguous formulas were re-derived as described above. Literature reading focused on the relevant hypotheses, statements and proof sections; no claim is made to have checked every proof in the entire bibliography.

Task: “Open problem I0078” — received 13 November 2026, approximately 16:32 Asia/Tbilisi (UTC+4).
