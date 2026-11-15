PARTIAL

I0014 verdict: PARTIAL — CLT proved with the added hypothesis ρ*(1)<1; a uniform upper-variance estimate proved for all 0<β<1. The original extension remains unresolved.
I0013 verdict: PARTIAL — source identification and scalar asymptotics checked; no verified Aⱼ, B_τ, d, or explicit counterexample region.

# Open problems I0013 and I0014

Neither unrestricted open problem is resolved here. In particular, the requested exact statements of Bradley’s Theorem 1 and Proposition 0 and the tracking of their constants remain incomplete because their full text could not be obtained. The checked partial results and source limitations are set out below.

## Source identification and conventions

Muneya Matsui, *Can we further improve the central limit theorem for stationary ρ-mixing sequences ?*, arXiv:2609.04638v1, [listing](https://arxiv.org/abs/2609.04638v1). The arXiv listing gives **Fri, 4 Sep 2026 02:17:01 UTC**, one author, and only v1. The PDF itself displays **September 7, 2026** on p.1. The phrase “(with related open problems)” is not part of the listing's title. The full paper is saved as text in sources/matsui_2026v1.txt; its TeX text is in sources/matsui_2026v1_tex.txt. The listing links CC BY 4.0; attribution: Muneya Matsui, arXiv:2609.04638v1. No PDF or page image is stored.

All numbered references below initially follow Matsui's bibliography. All page numbers for Matsui are printed PDF pages, matching the 1-based form-feed sections in the saved text. The paper defines log x = log₂ x, log⁺ x = log₂(x∨1), [x] = floor(x), and aₙ ≪ bₙ to mean aₙ=O(bₙ), p.1. In particular, ≫ is a lower comparison up to a positive constant, not a ratio tending to infinity. Natural logarithms will be written ln when auditing constants.

Let X=(Xₜ)ₜ∈ℤ be real and strictly stationary, Sₙ=Σₜ₌₁ⁿXₜ, and σₙ²=Var(Sₙ). The maximal correlation coefficient is

ρ(n)=sup{|Corr(f,g)|: f∈L²(σ(Xₜ:t≤0)), g∈L²(σ(Xₜ:t≥n)), Var(f)Var(g)>0}.

The common assumptions (1.1), p.1, are E X₀=0, E X₀²<∞, σₙ→∞, and ρ(n)→0. Their variance consequence is σₙ²=n h(n) with h slowly varying; there is no assumption that σₙ²∼c n or that h is bounded below.

## Exact corollary and open questions

Here is Corollary 2.3, p.4, with mathematical typography restored from the TeX and wording preserved:

> Let $(X_t)$ be a strictly stationary sequence satisfying (1.1) and let $\alpha>0$ and $\beta\in(1/2,1)$. Assume either $(a)$ or $(b)$.
>
> $(a).\qquad (a1)\quad \mathbb E X_0^2(\log^+|X_0|)^{2\alpha}<\infty,$
>
> $\phantom{(a).\qquad}(a2)\quad \rho(n)\leq\alpha(\log n)^{-1}\quad\text{for every $n$ sufficiently large}.$
>
> $(b).\qquad (b1)\quad \mathbb E X_0^2\exp\big[2\alpha(2\log^+|X_0|)^{1-\beta}/(1-\beta)\big]<\infty,$
>
> $\phantom{(b).\qquad}(b2)\quad \rho(n)\leq\alpha(\log n)^{-\beta}\quad\text{for every $n$ sufficiently large}.$
>
> Then $S_n/\sigma_n\stackrel d\to N(0,1)$ as $n\to\infty$.

I0014, Remark 2.5(i), p.5:

> “It seems difficult to extend Corollary 2.3 $(b)$ to the region $\beta\in(0,1/2)$.”

Thus I0014 asks whether the same moment constant and mixing upper bound suffice when 0<β<1/2, with all of (1.1). The endpoint β=1/2 is also excluded by the printed corollary but is not included in this quoted open range.

I0013 is **Remark 2.4(ii), pp.4–5**, not Remark 2.5. It concerns ρ(n) approximately α/(log₂ n), α>0, and E[X₀²(log₂⁺|X₀|)^γ]<∞, γ>0. The corollary guarantees the CLT for γ≥2α. Its exact question and qualification are:

> “Since Corollary 2.3 ensures that the CLT holds in the region $\gamma\geq 2\alpha$, a natural subsequent question is: in which subspace of $\gamma<2\alpha$ can one construct a counterexample to the CLT (see Figure 1 (A)). We merely note that, in light of Theorem 1 and Proposition 0 of [3], the constant $d$ appears to depend on $A_j$ and $B_\tau$ defined therein, and a further analysis of these constants is required.”

The preceding setup in that remark writes ρ(n)=α(log₂(n∨2))⁻¹. Since ρ≤1, this equality cannot be imposed for every n when α>1. Rates or bounds for sufficiently large n are the meaningful formulation unless coefficients are capped at small lags. An upper bound supplied by a counterexample construction should not be replaced by asymptotic equality without proof.

## Main theorem as printed

Theorem 2.2, pp.3–4: fix δ∈(0,1), assume (1.1), let g:[0,∞)→[0,∞) be nondecreasing and E[X₀²g(|X₀|)]<∞. Choose q₀ positive, nonincreasing, slowly varying with Σᵢq₀(2ⁱ)¹ᐟ²<∞. With 0<ε₁<ε₂<1 let

h_lower(n)=c₂ exp(−Σᵢ₌₁^⌊(1−ε₁)log₂n⌋ρ(2ⁱ)/(1−ε₂)),

ℓ_lower(n)=h_lower(n)⁴q₀(n), uᵢ=⌊2ⁱℓ_lower(2ⁱ)⌋,

h_δ(n)=exp(5Σᵢ₌₁^⌊log₂n⌋ρ(2ⁱ)^{2/(2+δ)}),

h_d(n)=exp(−2Σᵢ₌ₖ₀^⌊log₂n⌋log{1−ρ(uᵢ)}),

where k₀ is large enough that ρ(uᵢ)<1. If

(2.7)  g(n¹ᐟ²[h_δ(n)h_d(n)^{(2+δ)/4}]^{−1/δ}) ≫ h_d(n),

then Sₙ/σₙ⇒N(0,1). The log in h_d is transcribed as printed; the paper's base-2 convention makes its use alongside exp require separate checking.

## I0014: exact failure points in the printed proof

The proof of Corollary 2.3(b) is on pp.14–16. Its first restriction occurs on p.15 after (3.25):

ρ(uᵢ)≤αi^{−β}+C i^{−2β}.

The Taylor bound for −ln(1−ρ) adds another quadratic error. To obtain (3.26) with a bounded multiplicative constant the proof uses Σᵢ i^{−2β}<∞. This holds exactly for β>1/2. Below it the correction grows like r^{1−2β}/(1−2β), where r=⌊log₂n⌋; at β=1/2 it grows like ln r.

The second restriction occurs on pp.15–16 in the threshold shift. Write a=2/(2+δ). The shift eₙ is bounded by C(log₂n)^{1−aβ}, and the lost exponent satisfies Eₙ≤C(log₂n)^{1−β−aβ}+C(log₂n)^{−β}. Making it tend to zero requires

δ<(4β−2)/(1−β).

No positive δ satisfies this when β≤1/2. Both are variance/truncation and moment-comparison errors; the first is already present before the final CLT argument. Their failure does not prove that the CLT fails.

## I0014: a proved extension under an extra dependence hypothesis

**Conditional proposition.** Assume (1.1), the exact moment and rate in Corollary 2.3(b), and any β∈(0,1/2). Add the explicit hypothesis

r := ρ*(1) < 1,

where ρ*(1) is the supremum of maximal correlation between σ(Xᵢ:i∈A) and σ(Xⱼ:j∈B), over all finite nonempty disjoint index sets A,B⊂ℤ. These sets may interlace. Then Sₙ/σₙ⇒N(0,1). In fact finite second moments and ordinary ρ(n)→0 suffice under this extra hypothesis; the displayed weighted moment and rate are unnecessary for this subclass.

This is an established stronger hypothesis, not an answer to I0014 under ordinary ρ-mixing. A direct proof is included so that no unverified quantitative lemma from the 2026 paper is needed. The variance bound is the one in Bradley–Jurek (2015), Appendix Lemma 6.2, author PDF p.15, traced there to Bradley (1992), Lemma 2.1, and Bradley's book, Vol.1, Lemma 8.21.

**Variance bound, with constants proved.** For centered square-integrable variables Y₁,…,Yₙ obtained by coordinatewise measurable transformations of X, put V=E(ΣYᵢ)² and Q=ΣE Yᵢ². Split {1,…,n} by independent fair coin flips into A and B, using this only as an algebraic average over the 2ⁿ partitions. For each fixed partition,

|Cov(Σ_A Yᵢ,Σ_B Yᵢ)|≤(r/2)[Var(Σ_A Yᵢ)+Var(Σ_B Yᵢ)].

Empty parts give zero covariance and cause no problem. Averaging over the partitions gives

E_partition Cov(Σ_A Yᵢ,Σ_B Yᵢ)=(V−Q)/4,

E_partition[Var(Σ_A Yᵢ)+Var(Σ_B Yᵢ)]=(V+Q)/2.

Taking the absolute value after averaging yields |V−Q|≤r(V+Q), hence

c Q≤V≤C Q,  c=(1−r)/(1+r),  C=(1+r)/(1−r).  (E1)

This is a deterministic covariance proof; no random simulation is used.

**Bounded approximation.** Let Zₜ,K=Xₜ1{|Xₜ|≤K}−E[X₀1{|X₀|≤K}], and Rₜ,K=Xₜ−Zₜ,K. Write Uₙ,K=Σₜ₌₁ⁿZₜ,K, Vₙ,K=Σₜ₌₁ⁿRₜ,K and sₙ,K²=Var(Uₙ,K). All transformed mixing coefficients are bounded by the original ones. Set v=E X₀²>0; positivity follows from σₙ→∞. By (E1),

σₙ²≥c n v,

E Vₙ,K²≤C n E[X₀²1{|X₀|>K}].

Consequently, with ε_K²=(C/(c v))E[X₀²1{|X₀|>K}],

supₙ ||Vₙ,K||₂/σₙ≤ε_K→0.  (E2)

For all sufficiently large fixed K, Var(Z₀,K)>0, since Z₀,K→X₀ in L². Again by (E1), sₙ,K²≥c n Var(Z₀,K)→∞. The bounded stationary sequence Zₜ,K has every finite moment and is ρ-mixing. Ibragimov's CLT therefore gives Uₙ,K/sₙ,K⇒N(0,1) for each such fixed K.

Minkowski's inequality gives |sₙ,K−σₙ|≤||Vₙ,K||₂. Thus

||Sₙ/σₙ−Uₙ,K/sₙ,K||₂
≤||Vₙ,K||₂/σₙ+|sₙ,K−σₙ|/σₙ≤2ε_K.

For any real t the difference of the two characteristic functions is at most 2|t|ε_K, by |e^{iu}−e^{iv}|≤|u−v| and Cauchy–Schwarz. First let n→∞ at fixed K, then K→∞. The characteristic function tends to exp(−t²/2), proving the conditional proposition.

Ordinary ρ(n) controls two ordered half-lines, while ρ*(1) controls arbitrary disjoint sets. The original logarithmic rate does not supply this extra hypothesis. No claim of a new CLT or of a resolution of the unrestricted question is made here.

## I0014: an upper-variance bound that does not require β>1/2

The upper comparison can be separated from the lower-variance obstruction. The following elementary bound was derived and checked here; no novelty is claimed.

**Variance-envelope lemma.** Suppose a stationary sequence has ρ(n)≤α(log₂n)^{−β} for sufficiently large n, with α>0 and 0<β<1. There exists K depending only on the mixing bound such that, for every centered Yₜ=f(Xₜ) with E Y₀²<∞ and every n≥2,

Var(Σₜ₌₁ⁿYₜ)≤K n E Y₀² exp{[α/(1−β)](log₂n)^{1−β}}.  (E3)

The same K works for all such f, including tail truncations. No variance-divergence assumption for Y is needed.

**Proof.** Normalize ||Y₀||₂=1; the zero-variance case is trivial. Put a(m)=||Σₜ₌₁ᵐYₜ||₂, bⱼ=2^{−j/2}a(2ʲ), Mⱼ=max₀≤ᵢ≤ⱼbᵢ. Binary decomposition and stationarity give, for 1≤u≤2ʲ,

a(u)≤Σ_{i≤floor(log₂u)}2^{i/2}Mⱼ≤D√u Mⱼ,

where D=√2/(√2−1). Fix s>2 and for sufficiently large j put pⱼ=floor(2ʲj^{−s})≥1. Compare two adjacent blocks of length 2ʲ with two blocks separated by pⱼ observations. Their difference consists of two blocks of length pⱼ, so the L² triangle inequality and the definition of maximal correlation give

a(2^{j+1})≤√{2(1+ρ(pⱼ))} a(2ʲ)+2a(pⱼ).

Consequently,

b_{j+1}≤[√{1+ρ(pⱼ)}+√2 D j^{−s/2}]Mⱼ,

and the bracket is ≥1, so it also bounds M_{j+1}/Mⱼ. Since √{1+ρ}≥1 and ln(1+x)≤x,

ln M_r≤C+(1/2)Σ_{j<r}ρ(pⱼ)+√2 D Σ_{j<r}j^{−s/2}.

Now log₂pⱼ≥j−s log₂j−1. For large j this lies in [j/2,j]. By the mean value theorem,

ρ(pⱼ)≤αj^{−β}+C(log j)j^{−β−1}.

The second term is summable for every β>0, as is j^{−s/2}. Finally Σ_{j<r}j^{−β}≤r^{1−β}/(1−β)+C. Thus M_r²≤C exp{αr^{1−β}/(1−β)}. Applying the binary-decomposition bound once more to n proves (E3), after adjusting K for finitely many small n and rescaling Y. Every inequality is uniform in f.

This gives an upper bound for tail variances with the correct leading coefficient throughout the requested β-range. It does not give a sufficiently sharp lower bound for σₙ², nor the CLT at the critical moment without an added hypothesis. The two losses identified in the printed proof remain unresolved under ordinary ρ-mixing alone.

## I0013: what the counterexample criterion actually establishes here

Reference **[3]** is Richard C. Bradley, *The central limit question under ρ-mixing*, Rocky Mountain Journal of Mathematics **17**(1) (March 1987), **95–114**, [DOI](https://doi.org/10.1216/RMJ-1987-17-1-95). Its published sequel is *Corrections to “The central limit question under ρ-mixing”*, **17**(4) (December 1987), **891–892**, [DOI](https://doi.org/10.1216/RMJ-1987-17-4-891). Crossref records for both are saved in data/. Bradley's own 2005 survey, reference [20], printed p.137, records the correction (abbreviated there as p.891). Matsui's bibliography omits it.

**Access limitation.** The original text of [3] and its correction were not obtained. Project Euclid repeatedly returned challenge HTML at the article, PDF, download, and legacy URLs; the publisher's RMMC page links back there. No exact transcription of Theorem 1 or Proposition 0, no formulas for Aⱼ or B_τ, and no numerical value of d can therefore be certified from this investigation. The statement below is only an analysis of the single displayed condition Matsui attributes to [3], not a substitute for the missing theorem or its construction. In particular, no explicit counterexample parameter region is proved here.

Matsui, Remark 2.4(ii), p.4, attributes to [3, Theorem 1], condition (1.5), the requirement

q(√n exp{−(d/2)Σₖ₌₁ⁿτ(k)/k})=o(n),  d>0.  (B1)

Take τ(k)=α/log₂(k∨2). A harmless globally defined moment function with the required asymptotic behavior is

q(x)=x²(1+log₂⁺x)^γ,  x≥0, γ>0.

It is nondecreasing, vanishes at zero, has the same integrability at infinity as Matsui's x²(log₂⁺x)^γ, and is submultiplicative: log₂⁺(xy)≤log₂⁺x+log₂⁺y and 1+u+v≤(1+u)(1+v). This verifies one commonly used moment-function property, but the missing original theorem may impose further conditions, which are not assumed verified.

**Exact asymptotic for (B1), under the displayed exp convention.** Let r=log₂n. Integral comparison gives

T(n):=Σₖ₌₁ⁿτ(k)/k=α ln(2) ln r+C_τ+o(1).  (B2)

To check the constant: for k≥2, 1/[k log₂k]=ln(2)/[k ln k], whose integral is ln(2) ln ln k. The difference between the sum and the integral tends to a finite constant because the integrand is decreasing and its unit-interval integral errors are summable.

Set xₙ=√n exp{−dT(n)/2}. Then

xₙ²/n=exp(−dC_τ)r^{−dα ln2}(1+o(1)),

log₂xₙ=r/2−(dα/2)ln r−dC_τ/(2 ln2)+o(1),

and therefore

q(xₙ)/n∼2^{−γ}exp(−dC_τ)r^{γ−dα ln2}.  (B3)

Thus **the literal displayed scalar condition** (B1) holds exactly when γ<dα ln2; at equality the ratio tends to the strictly positive constant 2^{−γ}exp(−dC_τ), and above it the ratio diverges. If one instead uses τ(k)=a/ln(k∨2), the threshold is γ<d a. If the original theorem uses a different exponential base or redefines d, the coefficient must be converted accordingly. The original source is needed to settle that normalization.

Matsui writes γ/α<d without ln2. Under his explicitly declared base-2 log and the usual exp=eˣ, this omits a factor. It can be absorbed into an unspecified d, but it matters when the task is precisely to calculate d. Even after such a conversion, retaining an unspecified d is only a restatement of the existing obstruction. Dependence d=d(Aⱼ,B_τ,…) cannot be replaced by a chosen constant, and positivity of d for each τ does not by itself show that αd is arbitrarily large as α varies.

**Certified region for Bradley counterexamples in this report:** none beyond the source's qualitative existence statements. The calculations (B2)–(B3) are proved analytic implications; they do not verify the construction, its constants, its marginal moments, its mixing coefficient, or failure of the normalized CLT. The unrestricted region below γ<2α remains unresolved here.

## Literature: verified results, attribution, and scope

The distinction between an original theorem inspected here and a theorem quoted by Matsui matters. Missing primary theorem pages are left missing below.

| Work | Result and location | What it supplies, and what it does not |
|---|---|---|
| I. A. Ibragimov (1975), *A note on the central limit theorems for dependent random variables*, Theory Probab. Appl. 20(1), 135–141; Russian original, Teor. Veroyatnost. i Primenen. 20(1), 134–140; [DOI](https://doi.org/10.1137/1120011), [original journal record](https://www.mathnet.ru/eng/tvp2996) | Matsui labels the cited results Theorems 1 and 2. The web-extracted Russian original numbers them Theorem 2.1, p.135, and Theorem 2.2, p.136; see the distinction below. | Under (1.1), σₙ²=n h(n), h slowly varying. The CLT holds if either E|X₀|^{2+δ}<∞ for some δ>0 or Σₖρ(2ᵏ)<∞. The dyadic summability condition is Ibragimov's classical condition, not a separate theorem first due to Peligrad. |
| M. Peligrad (1987), *On the central limit theorem for ρ-mixing sequences of random variables*, Ann. Probab. 15(4), 1387–1394; [DOI](https://doi.org/10.1214/aop/1176991983) | Theorem 1, quoted as Matsui's Theorem 1.2, p.2; Corollaries 1 and 2, quoted as Matsui's Corollary 1.3, p.2. Original theorem-level pages unavailable here. | With g nondecreasing, (1.1), E[X₀²g(|X₀|)]<∞, and g(√n)≳exp{[2/(1−η)]Σ_{k≤floor(log₂n)}ρ(2ᵏ)} for some η∈(0,1), the CLT holds. This trades moment integrability for a nonsummable dyadic rate. |
| R. C. Bradley Jr. (1980), *A remark on the central limit question for dependent random variables*, J. Appl. Probab. 17(1), 94–101; [publisher](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/remark-on-the-central-limit-question-for-dependent-random-variables/47352085A224E622F9C94E7D3E406092), [DOI](https://doi.org/10.2307/3212927) | Publisher abstract inspected. Theorem 1 and Corollary 2 are cited in Matsui, Remark 2.5(ii), p.5; their full original statements were not obtained. | Existence of a strictly stationary sequence with finite second moments, divergent partial-sum variance, and ρ(n)→0, whose sums have non-Gaussian subsequential limits. This is a counterexample to omitting all rate/moment strengthening, not to Corollary 2.3(b). |
| R. C. Bradley (1987), [3], plus its correction | Bibliography and archived original publisher listing verified. Theorem 1, condition (1.5), and Proposition 0 are identified by Matsui, Remark 2.4(ii), pp.4–5. Full original statements and their individual pages **not verified**. | This is the requested construction underlying Aⱼ, B_τ and d. Its exact constants remain an outstanding dependency, not a result of this report. |
| M. Peligrad (1982), *Invariance principles for mixing sequences of random variables*, Ann. Probab. 10(4), 968–981; [DOI](https://doi.org/10.1214/aop/1176993718) | Matsui cites it for uniform integrability in the summable case, p.13; Bradley–Jurek, author PDF p.15, identifies its Lemma 3.4 for an upper variance estimate. | The invariance-principle and variance-inequality background. No use is made here of an uninspected sharp constant. |
| Q.-M. Shao (1988), *Remark on the invariance principle for ρ-mixing sequences of random variables*, Chinese Ann. Math. Ser. A 9(4), 409–412; Q.-M. Shao (1989), *On the invariance principle for ρ-mixing sequences of random variables*, Ser. B 10(4), 427–433; [1989 publisher record](https://camath.fudan.edu.cn/cambcn/ch/reader/view_abstract.aspx?file_no=10B401&flag=1) | Matsui, Remark 3.4, pp.12–13, compares his moment estimate with Shao (1988), Lemma 1, and Shao (1989), Lemma 2. The 1989 PDF is scanned with no text layer; its theorem pages were not read here. | Invariance principles combining moments and mixing rates, and moment-inequality predecessors to Matsui's Lemma 3.3. No assertion that these solve the new borderline questions. |
| Q.-M. Shao (1995), *Maximal inequalities for partial sums of ρ-mixing sequences*, Ann. Probab. 23(2), 948–965; [DOI](https://doi.org/10.1214/aop/1176988297) | Bibliographic identification; original theorem statements unavailable here. | Rosenthal-type maximal inequalities. A maximal inequality for interlaced ρ* cannot be substituted for one for ordinary ρ without checking the dependence hypothesis. |
| S. A. Utev (1990), *Central limit theorem for dependent random variables*, in *Probability Theory and Mathematical Statistics*, Vol.2, VSP/Mokslas, 519–528 | Theorem 4.1, restated and explicitly corrected in Bradley–Jurek (2015), Appendix Theorem 6.4, author PDF pp.15–16. This is distinct from Utev's 1990 paper on φ-mixing arrays. | A triangular-array Lindeberg CLT under uniform Σₘρ_array(2ᵐ)<∞ and a positive lower comparison of total variance with the sum of individual variances. Its hypotheses do not follow in the nonsummable dyadic regime at issue here. |
| M. Peligrad and S. Utev (1997), *Central limit theorem for linear processes*, Ann. Probab. 25(1), 443–456; [DOI](https://doi.org/10.1214/aop/1024404295) | Theorem 2.2(b) identified by Peligrad–Sang's author text as a finite-variance result for linear arrays under a dyadically summable ρ rate; original theorem-level page not verified here. | Weighted/linear-process CLTs; does not settle the critical nonsummable case. Do not confuse its title and year with their 2006 paper below. |
| S. Utev and M. Peligrad (2003), *Maximal inequalities and an invariance principle for a class of weakly dependent random variables*, J. Theor. Probab. 16(1), 101–115; [publisher DOI](https://doi.org/10.1023/A:1022278404634) | Its interlaced-correlation maximal estimate is restated in Merlevède–Peligrad–Utev (2006), Theorem 10, p.8, with constants D(q,N,r). | For q≥2 and ρ*(N)≤r<1, E max_{j≤n}|Σ_{i≤j}Xᵢ|^q≤D[ΣᵢE|Xᵢ|^q+(ΣᵢE Xᵢ²)^{q/2}]. The interlaced assumption is stronger than the target's ordinary ρ decay. |
| F. Merlevède, M. Peligrad and S. Utev (2006), *Recent advances in invariance principles for stationary sequences*, Probability Surveys 3, 1–36; [author/journal text](https://arxiv.org/abs/math/0601315v2) | Theorem 10, p.8; §4.2.1(a), pp.14–15; Theorem 11, pp.10–11 | Primary survey by the theorem authors; explains the dyadic summability condition and projective alternatives. The sufficient projective condition Σₙ n^{-3/2}||E(Sₙ|F₀)||₂<∞ is not guaranteed merely by ρ(n)=O((log n)^{−β}) with β<1. |
| M. Peligrad and S. Utev (2006), *Central limit theorem for stationary linear processes*, Ann. Probab. 34(4), 1608–1622; [reprint](https://arxiv.org/abs/math/0509682v2) | Theorem 1, reprint p.2; Corollary 7, reprint p.11. Reprint expressly differs in pagination from the journal. | A projective CLT for linear processes with square-summable coefficients. Corollary 7 assumes Σₖ∫₀^{ᾱ(k)}Q²(u)du<∞. This quantitative tail/dependence condition is not implied by the critical assumptions in the question. |
| R. C. Bradley and Z. J. Jurek (2015), *On a central limit theorem for shrunken weakly dependent random variables*, Houston J. Math. 41, 621–638; [author text](https://www.math.uni.wroc.pl/~zjjurek/bradZjj3.pdf) | Appendix Lemma 6.2, author p.15; Theorem 6.4, author p.16 | Convenient primary restatements of variance bounds and array CLTs, used above with explicit source-typo cautions below. |

The Russian original of Ibragimov was subsequently inspected through the web tool's text extraction, saved as sources/ibragimov_1975_web_extract.txt. Theorem 2.1 (p.135) gives the variance dichotomy and the finite-(2+δ)-moment CLT when σₙ²→∞. Theorem 2.2 (p.136) gives continuity of the spectral density under Σₘρ(2ᵐ)<∞ and states its CLT with the additional condition f(0)≠0, yielding σₙ²∼2πf(0)n. This is the original statement; the broader combined formulation above is explicitly Matsui's restatement. No equivalence between f(0)>0 and variance divergence is silently asserted. The extraction is visibly imperfect OCR, so formulas were cross-checked with the readable theorem wording and not used to compute sharp constants.

For clarity, Peligrad's two logarithmic corollaries, in Matsui's notation (p.2), require respectively

E[X₀²(log₂⁺|X₀|)^{2α/(1−ε)}]<∞,  ρ(n)≤α(log₂n)^{−1},

or, for 0<β<1,

E[X₀² exp{[2α/((1−β)(1−ε))](2log₂⁺|X₀|)^{1−β}}]<∞,  ρ(n)≤α(log₂n)^{−β},

for some ε∈(0,1), with rate bounds eventually and all of (1.1). These are established positive results with coefficient slack; adding such slack would only recover a known theorem.

The normalized formulation of Utev's array criterion is as follows. For centered row variables ξₙ,ᵢ, let vₙ²=Var(Σᵢξₙ,ᵢ)>0. Require liminfₙvₙ²/ΣᵢEξₙ,ᵢ²>0 and, for each ε>0,

vₙ^{−2}ΣᵢE[ξₙ,ᵢ²1{|ξₙ,ᵢ|>εvₙ}]→0,

together with Σₘρ_array(2ᵐ)<∞. Then Σᵢξₙ,ᵢ/vₙ⇒N(0,1). Bradley–Jurek specifically reports the erroneous variance formula in Utev's original (4.3). Its own displayed (6.2) uses ε without vₙ, which is not scale invariant unless the rows are already normalized; the scale-invariant condition above is the one used here. The alternative array hypothesis involving ρ* and ordinary strong mixing is not the same as ordinary ρ-mixing alone.

## Source audit affecting a sharp-constant argument

Several source issues are worth isolating because this task concerns constants, not merely orders of magnitude.

1. Matsui declares log=log₂ on p.1, but uses the natural-log Taylor expansion −log(1−x)=x+x²/2+⋯ on p.14. Literally −log₂(1−x)=−ln(1−x)/ln2. Hence the printed bound leading to (3.26) has a missing 1/ln2 if all occurrences of log obey the declared convention. Products in Lemma 3.2, p.9, are also converted to exp(sum log) without the corresponding factor. This is an inconsistency to repair before treating numerical constants as certified, not a disproof of the intended CLT.
2. The paragraph after Theorem 2.2, p.4, claims that (2.7) implies (1.3). That direction would not establish that the new theorem includes Peligrad's; the required direction is the converse. Its displayed comparisons alone do not establish that converse.
3. Equation (3.23), p.14, prints supₙE|Sₙ/σₙ|^{2+δ}<∞ after bounding the truncated sum Sₙ,₁. Under the theorem's moment hypothesis the untruncated (2+δ)-moment need not even exist. An iid symmetric tail P(|X|>x) proportional to x^{−2}exp{−K(ln x)^p}, with 0<p<1 and K sufficiently large, has the required stretched-log weighted second moment but no moment of order 2+δ. Thus (3.23) needs the truncation subscript; it cannot be used literally. The following uniform-integrability argument can be intended for the truncated sums.
4. In the proof of Theorem 2.2, p.13, the choice ℓ_upper≤ℓ_lower is followed by the claim u_dagger≥u_star, with u_dagger=floor(2ⁱℓ_upper) and u_star=floor(2ⁱℓ_lower). These are opposite inequalities. Uniformity in the truncation level also needs attention because Lemma 3.1's displayed constant depends on X. Neither issue is used in the direct conditional proof above.
5. Remark 2.5(ii), p.5, first writes a power-log moment E[X₀²(log⁺|X₀|)^γ], but the ensuing β+γ=1 comparison uses the stronger stretched-exponential moment E[X₀²exp{(log⁺|X₀|)^γ}]. These must not be conflated. In the latter parametrization γ=1−β and the coefficient threshold quoted by the paper is α≤γ2^{−(γ+1)} for 0<γ<1/2. Extending I0014 below β=1/2 corresponds to γ>1/2 in that parametrization. I0013 instead uses γ as the exponent of a power of log, and has decay exponent β=1.

All five issues were checked against both the PDF text and TeX, not inferred solely from HTML rendering.

## Search for later work

Search date: **13 November 2026**. The versioned arXiv listing still shows only v1. Searches used the exact title, arXiv identifier, Matsui with ρ-mixing and extension/borderline terms, the Bradley construction title and correction, and the classical authors with logarithmic rates. Results and access status are recorded in data/literature_search.txt.

No inspected printed result was found that resolves I0013's numerical counterexample region or removes β>1/2 under the original I0014 hypotheses. This is a search result, not a claim of exhaustive coverage. Bradley's *On the central limit question for strictly stationary, reversible Markov chains*, arXiv:2508.12951v2, revised **10 March 2026 17:08:46 UTC**, is recent related work on strong/absolute mixing and reversibility, not a later resolution of Matsui's September questions. Its listing and abstract were inspected; its full theorem statements were not used. The 2003 and 2006 interlaced/projective results explain the added-hypothesis proposition, not the unrestricted borderline.

## Verification and outstanding work

Analytic checks: rederived both β restrictions directly from (3.25)–(3.28); independently integrated the sum in (B2); checked the equality case in (B3); derived the random-partition covariance identities without a probabilistic approximation; and checked the dyadic upper-variance recursion and its interpolation for arbitrary n.

Computational checks: `python3 code/check_inequalities.py` uses rational arithmetic for the β,δ exponents; symbolic algebra for the finite-partition identities and submultiplicativity; and 80-decimal arithmetic for the log-base constant. Results are in data/inequality_checks.json. It uses one process, library threads capped at one, and inherited nice 10. A successful run used 59,228,160 bytes of peak resident memory, far below 4 GB; the JSON records the most recent run. This macOS sandbox rejected attempts to lower RLIMIT_AS and RLIMIT_DATA; the check records measured RSS rather than claiming a working OS memory cap. No simulations were run.

For example, at β=1/2 the shift exponent is exactly δ/[2(2+δ)]>0. The natural-log Taylor bound fails if read as a bound on −log₂(1−x): at x=10⁻⁶ the latter is about 1.44269576224×10⁻⁶, while the printed right side is about 1.00000050000×10⁻⁶. Computation checks these constants only; the proofs above establish the general claims.

The full original [3] and its correction are still needed to state Theorem 1 and Proposition 0 exactly, track Aⱼ and B_τ, and verify an explicit admissible d. No such computation or counterexample is claimed. The unrestricted extension in I0014 is also not proved or refuted. The proved conditional CLT requires the additional interlaced bound ρ*(1)<1, and the unconditional progress consists of (E3) and the exact identification of the source proof's two β barriers.

Task: “Open problems I0013 and I0014” — started 13 November 2026, 14:27 Asia/Tbilisi (+04).
