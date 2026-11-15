# One input: a uniform cumulant bound and a resummed width expansion

Fix one nonzero deterministic input. Assume independent Gaussian weights, zero biases, width n in each hidden layer, and weight variance 2/n at every hidden propagation. Gaussianity is an assumption here; weight variance alone does not specify this problem. Let the first-layer preactivation variance be q>0. With the usual first-layer scaling, q=2||x||²/n₀.

Count depth by d, the number of ReLU propagation steps after the first Gaussian layer. Thus the preactivation layer numbered L has d=L−1. All statements below use this convention explicitly. Let Z=(Z₁,…,Zₘ) denote any fixed finite collection of distinct preactivation coordinates at that layer, and let G be a standard Gaussian vector in Rᵐ.

The results concern one input, and also any collection of positive scalar multiples of that input by ReLU homogeneity. They do not establish the theorem for general distinct inputs.

## 1. Exact moments before taking a depth limit

Let

Y=2 max(g,0)²,  g∼N(0,1),
Fₙ=(Y₁+⋯+Yₙ)/n,
Qₙ,d=∏_{ℓ=1}^d Fₙ,ℓ,

where all variables on the right are independent, and Qₙ,₀=1. Then

(1)  Z ≍ √(q Qₙ,d) G,

with G independent of Qₙ,d. To see this, condition on a preactivation layer with conditional variance K. Its coordinates can be generated as √K times fresh independent standard Gaussians. The next layer has conditional variance

(2/n)∑ᵢ max(√K gᵢ,0)² = K Fₙ.

Fresh independent weights give fresh independent Gaussian coordinates. Iterating proves (1), including trajectories that hit zero. In particular Var(Zᵢ)=q exactly.

For j≥1, symmetry of g gives

(2)  μⱼ:=E Yʲ = 2^{j−1}(2j−1)!!.

Write λⱼ=κⱼ(Y), and let Πⱼ be the set of partitions of {1,…,j}. The cumulant formula for a sample mean gives the polynomial

(3)  aⱼ(z)=∑_{π∈Πⱼ} (∏_{B∈π} λ_{|B|}) z^{j−|π|},
     a₀(z)=a₁(z)=1.

Indeed κᵣ(Fₙ)=λᵣ/n^{r−1}, and the moment–cumulant identity gives (3) at z=1/n. Hence, exactly for every positive integer n and nonnegative integer d,

(4)  E Qₙ,dʲ = aⱼ(1/n)^d,
     E Zᵢ^{2j}/qʲ = (2j−1)!! aⱼ(1/n)^d,
     E Zᵢ^{2j+1}=0.

The first factors are

a₂(z)=1+5z,
a₃(z)=1+15z+44z²,
a₄(z)=1+30z+251z²+558z³.

There is an independent exact formula for checking them. Conditional on B∼Bin(n,1/2), Fₙ has the law (2/n)χ²_B, with χ²₀=0. Therefore

(5)  aⱼ(1/n)=(2/n)ʲ 2^{−n}∑_{b=0}^n binom(n,b)∏_{s=0}^{j−1}(b+2s).

In particular this formula includes the atom P(Fₙ=0)=2^{−n}.

All λⱼ are positive. For |s|<1/4 the moment generating function of Y is

M(s)=[1+(1−4s)^{−1/2}]/2.

Differentiation and rationalization give

(6)  (log M)'(s) = [1−√(1−4s)]/[2s(1−4s)]
                 = [∑_{a≥0} Cₐsᵃ]/(1−4s),

where Cₐ=binom(2a,a)/(a+1) are the Catalan numbers. Thus

(7)  λⱼ=(j−1)!∑_{a=0}^{j−1} Cₐ4^{j−1−a}>0.

This yields λ₁=1, λ₂=5, λ₃=44 and λ₄=558. In particular all coefficients of aⱼ are nonnegative.

Define the scalar variance cumulant

(8)  Γₖ(n,d):=κₖ(Qₙ,d)
    =∑_{π∈Πₖ} w(π) ∏_{B∈π} a_{|B|}(1/n)^d,
     w(π)=(-1)^{|π|−1}(|π|−1)!.

For every tuple of output indices i₁,…,i₂ₖ,

(9)  κ(Z_{i₁},…,Z_{i₂ₖ})/qᵏ
     = Γₖ(n,d) ∑_{pairings P of {1,…,2k}}∏_{{a,b}∈P} δ_{iₐi_b}.

All odd joint cumulants vanish. One derivation uses the formal moment series: conditional Gaussianity gives E exp(u·Z)=E exp(q Qₙ,d |u|²/2), interpreted coefficient by coefficient. Its formal logarithm has kth term κₖ(Qₙ,d)(q|u|²/2)ᵏ/k!. Extracting a degree-2k coefficient gives (9). Only finitely many moments are needed for any such coefficient; no analytic moment generating function is assumed. For a repeated single coordinate, (9) becomes

(10)  κ₂ₖ(Zᵢ)/Var(Zᵢ)ᵏ=(2k−1)!! Γₖ(n,d).

## 2. Connected diagrams and a uniform bound valid at all widths

For each of d layers choose a partition σℓ of the k labelled vertices. Each block e with |e|≥2 is a hyperedge, colored by its layer. Edges within a layer are disjoint. Give it weight λ_{|e|}n^{−(|e|−1)}. Singleton blocks contribute 1. Define the cost of the whole configuration to be

h=∑_{edges e}(|e|−1).

Then Γₖ(n,d) is exactly the sum of these weights over configurations whose union is connected. Here is the cancellation that proves this assertion. Expand each factor in (8) using (3). A fixed colored configuration occurs in the term indexed by π precisely when every edge is contained in a block of π. Equivalently, π must coarsen its connected-component partition. If the configuration has r components, its total coefficient is

∑_{p=1}^r S(r,p)(-1)^{p−1}(p−1)!,

where S(r,p) is a Stirling number. This is 1 for r=1 and 0 for r>1: its exponential generating function in r is log(exp x)=x. Thus precisely the connected configurations remain, each with coefficient 1.

An edge on r vertices reduces the number of connected components by at most r−1. Consequently a connected configuration has h≥k−1. Each layer has cost at most k−1. Therefore

(11)  Γₖ(n,d)=∑_{h=k−1}^{d(k−1)} Pₖ,h(d)n^{−h},

where Pₖ,h(d)≥0. An empty sum is zero. For fixed d this is an exact finite expansion in 1/n.
For each fixed h the coefficient is a polynomial in d of degree at most h: expand each aⱼ(z)^d using binomial coefficients, and note that obtaining degree h in z uses at most h nonconstant factors in total.

Here is an explicit bound on every coefficient that also controls growing d. Put

(12)  Sₖ(u)=∑_{r=2}^k binom(k,r)λᵣ u^{r−1},
      exp Sₖ(u)=∑_{h≥0} sₖ,h uʰ.

For d≥1,

(13)  Pₖ,h(d) ≤ dʰ sₖ,h.

To prove it, let a configuration contain m edges with total cost h. Since every edge has size at least two, m≤h, and d^{−h}≤d^{−m}. After dividing its coefficient weight by dʰ, bound it by ∏ₑ λ_{|e|}/d. Drop both connectivity and the disjointness constraint inside layers. Each possible edge e can now occur independently at most once per layer. The resulting generating polynomial is

∏_{e⊂[k], |e|≥2} [1+λ_{|e|}u^{|e|−1}/d]^d.

Coefficient by coefficient, (1+x/d)^d ≤ exp x, since binom(d,j)/dʲ≤1/j!. Multiplying these inequalities proves (13).

Fix c>0 and take any R>c, for example R=max(1,2c). With t=d/n≤c, equations (11)–(13) imply, for every integer H≥k−2,

(14)  0 ≤ Γₖ(n,d)−∑_{h=k−1}^{H}Pₖ,h(d)n^{−h}
          ≤ exp(Sₖ(R)) (t/R)^{H+1}.

Coefficients past the degree in (11) are defined to be zero. Indeed the left side is at most ∑_{h>H}sₖ,h tʰ, and tʰ≤Rʰ(t/R)^{H+1}. In particular

(15)  Γₖ(n,d) ≤ R^{−(k−1)}exp(Sₖ(R)) (d/n)^{k−1}.

This is uniform in all integers 1≤d≤cn and n≥1, without a large-width threshold. Moreover (14) tends to zero geometrically in H uniformly over this range. This is a convergent cost expansion for each fixed k; it is not a truncation error tending to zero with n when H and positive t are fixed.

There is also a uniform lower bound. If d≥2(k−1), choose a labelled spanning tree on k vertices and put its k−1 pair edges in distinct layers. There are k^{k−2} such trees (the Prüfer sequence bijection has k^{k−2} sequences) and (d)_{k−1} distinct layer assignments for each tree. These are admissible configurations of weight 5^{k−1}n^{−(k−1)}. Since (d)_{k−1}≥(d/2)^{k−1}, they give the lower bound k^{k−2}(5/2)^{k−1}t^{k−1}. If 1≤d<2(k−1), use instead one hyperedge containing all k vertices, at any one layer. Its total contribution is dλₖn^{−(k−1)}≥λₖ[2(k−1)]^{−(k−2)}t^{k−1}. All other contributions are nonnegative by (7). Thus, with

(16)  Aₖ=min{k^{k−2}(5/2)^{k−1}, λₖ/[2(k−1)]^{k−2}}>0,

we have the explicit two-sided estimate

(17)  Aₖ(d/n)^{k−1} ≤ Γₖ(n,d)
       ≤ R^{−(k−1)}exp(Sₖ(R))(d/n)^{k−1}.

The Gaussian layer d=0 has Γₖ=0 for k≥2 and is handled separately.

The first fixed-depth coefficients are

(18)  P₂,₁(d)=5d,
      P₃,₂(d)=75d²−31d,
      P₄,₃(d)=2000d³−1860d²+418d.

They can be checked without enumerating diagrams. From (8),

Γ₂=a₂^d−1,
Γ₃=a₃^d−3a₂^d+2,
Γ₄=a₄^d−4a₃^d−3a₂^{2d}+12a₂^d−6,

where the argument is 1/n. The coefficient of z² in Γ₃ is 44d+150 binom(d,2). The coefficient of z³ in Γ₄ is

558d+4890d(d−1)+15000 binom(d,3)−375 binom(2d,3),

which simplifies to (18). At d=1 these give respectively λ₂, λ₃ and λ₄, as they must.

## 3. An all-orders expansion in 1/n at fixed effective depth

The cost expansion retains depth-dependent coefficients. A different expansion sums the depth powers first. It has coefficients depending only on t=d/n and a remainder tending to zero with n uniformly for bounded t.

Fix k≥2. Write aⱼ(z)=1+∑_{h=1}^{j−1} cⱼ,h zʰ and define the explicit positive radius

(19)  rₖ=min( {1} ∪
      {(2(k−1)cⱼ,h)^{−1/h}: 2≤j≤k, 1≤h≤j−1, cⱼ,h>0} ).

Let

Wₖ=∑_{π∈Πₖ}(|π|−1)!,
Hⱼ(z)=log(aⱼ(z))/z,
Hⱼ(0)=5 binom(j,2),

using the logarithm that is zero at aⱼ(0)=1; H₀=H₁=0. The following functions are analytic on a neighborhood of |z|≤rₖ:

(20)  Cₖ(z,t)=∑_{π∈Πₖ}w(π) exp(t∑_{B∈π}H_{|B|}(z)),
      Bₖ,m(t)=[zᵐ] Cₖ(z,t).

For every p≥0, c>0, integer n≥2/rₖ, and integer 0≤d≤cn, with t=d/n,

(21)  Γₖ(n,d)=∑_{m=0}^p n^{−m}Bₖ,m(t)+Eₖ,p(n,t),

(22)  |Eₖ,p(n,t)| ≤ (4kWₖ/rₖ) t exp(kc/rₖ) (nrₖ)^{−(p+1)}.

All constants are finite, specified by finite sums and polynomials, and independent of n and d. The estimate is deliberately conservative.

For completeness, verify the analytic bound. From (19), each cⱼ,h rₖʰ≤1/[2(k−1)], so ∑ₕcⱼ,h rₖʰ≤1/2. For |z|≤rₖ,

|aⱼ(z)−1|≤|z|/(2rₖ).

The convergent series for log(1+u) then gives |log aⱼ(z)|≤2|aⱼ(z)−1|≤|z|/rₖ, so |Hⱼ(z)|≤1/rₖ, including the removable point zero. The closed disk stays away from zeros of aⱼ, so the functions are analytic on a slightly larger open set. In each partition sum, |∑H|≤k/rₖ. For complex x,y, the integral identity eˣ−eʸ=(x−y)∫₀¹e^{y+s(x−y)}ds gives

|Cₖ(z,t)−Cₖ(0,t)|≤(2kWₖ/rₖ)t exp(kc/rₖ)

on the circle |z|=rₖ and 0≤t≤c. Apply Cauchy's coefficient estimate to this difference. The tail after degree p at z=1/n is bounded by the displayed constant times

∑_{m=p+1}^∞(nrₖ)^{−m}≤2(nrₖ)^{−(p+1)}.

This proves (22), including t=0. Finally, for positive real z=1/n,

exp(tHⱼ(1/n))=exp(d log aⱼ(1/n))=aⱼ(1/n)^d,

so Cₖ(1/n,d/n)=Γₖ(n,d), proving (21).

There is an explicit coefficient recipe at every order. Write

log aⱼ(z)=∑_{r≥1} ℓⱼ,r zʳ,
hπ,r=∑_{B∈π}ℓ_{|B|,r+1}  (r≥0).

Then

(23)  Bₖ,m(t)=∑_{π∈Πₖ}w(π)e^{thπ,0}
      ∑_{ν₁+2ν₂+⋯+mνₘ=m} ∏_{r=1}^m (t hπ,r)^{νᵣ}/νᵣ!.

For m=0 the inner expression is 1. The recipe follows by multiplying the ordinary exponential series for each power zʳ. In particular all Bₖ,m are entire functions of t.

## 4. The first correction and the two small parameters

The first two coefficients of log aⱼ are

(24)  ℓⱼ,₁=5 binom(j,2),
      ℓⱼ,₂=−(25/2)binom(j,2)−31binom(j,3).

Indeed the z² coefficient of aⱼ is 44binom(j,3)+75binom(j,4), corresponding respectively to a triple and two pairs. Subtracting half the square of the z coefficient gives

44binom(j,3)+75binom(j,4)−(25/2)binom(j,2)²
=−(25/2)binom(j,2)−31binom(j,3).

Put Sᵣ(π)=∑_{B∈π}binom(|B|,r). Then

(25)  Bₖ,₀(t)=∑π w(π)e^{5tS₂(π)},
      Bₖ,₁(t)=t∑π w(π)e^{5tS₂(π)}[-(25/2)S₂(π)−31S₃(π)].

For example,

B₂,₀=e^{5t}−1,
B₂,₁=−(25/2)t e^{5t};

B₃,₀=e^{15t}−3e^{5t}+2,
B₃,₁=(t/2)[−137e^{15t}+75e^{5t}];

B₄,₀=e^{30t}−4e^{15t}−3e^{10t}+12e^{5t}−6,
B₄,₁=t[−199e^{30t}+274e^{15t}+75e^{10t}−150e^{5t}].

The error after these two terms is bounded by (22) with p=1, namely

(26)  |Γₖ−Bₖ,₀(t)−Bₖ,₁(t)/n|
       ≤ 4kWₖ exp(kc/rₖ) t/(rₖ³ n²).

There is a separate graph interpretation of the leading resummed coefficient:

(27)  Bₖ,₀(t)=∑_{connected simple graphs H on [k]}(e^{5t}−1)^{|E(H)|}.

Expand e^{5tS₂(π)} as the product of 1+(e^{5t}−1) over pairs within blocks of π. The same component-partition cancellation used in Section 2 gives (27). Trees have the fewest edges, k−1, so

(28)  Bₖ,₀(t)=k^{k−2}(5t)^{k−1}+Oₖ(tᵏ) as t↓0.

The exact fixed-depth coefficient Pₖ,k−1(d) has leading large-d term k^{k−2}5^{k−1}d^{k−1}. To verify this directly, a cost-(k−1) configuration has at most k−1 edges. Only pair trees have exactly k−1 edges. For each such tree, admissible layer assignments are proper edge colorings with d colors, a polynomial of degree k−1 with leading coefficient 1: start with d^{k−1} arbitrary assignments and exclude equal colors on incident edges by inclusion–exclusion. Every imposed equality lowers the degree. Every configuration with a larger hyperedge has fewer edges and therefore lower degree in d.

Thus the ordinary fixed-d expansion uses 1/n with polynomial coefficients in d; the size estimates for its terms use t=d/n. At fixed positive t, the Gaussian-centered hierarchy is not asymptotic in n: even the fourth normalized cumulant has a nonzero limit. The resummed expansion (21) is an asymptotic expansion in 1/n uniformly on every finite interval 0≤t≤c. Its zeroth term is already non-Gaussian.

## 5. The limiting law, including the zero-factor issue

For clarity the limiting law can be proved directly, without inferring a distribution from its moments. Suppose d/n→t∈[0,∞), and put δₙ,ℓ=Fₙ,ℓ−1. Formula (3) gives

Eδ=0,
Eδ²=5/n,
Eδ⁴=75/n²+558/n³.

By Markov's inequality and a union bound,

P(max_{ℓ≤d}|δₙ,ℓ|>1/2)
≤16d(75/n²+558/n³)→0.

This also removes all zero factors with probability tending to one. On the complementary event, the logarithmic Taylor series gives

|log(1+δ)−δ+δ²/2|≤(2/3)|δ|³.

Cauchy–Schwarz gives E|δ|³≤√[(5/n)(75/n²+558/n³)]=O(n^{−3/2}). The expectation of the sum of the Taylor remainder bounds is consequently O(d n^{−3/2})→0. Also

E∑ℓδₙ,ℓ²=5d/n→5t,
Var(∑ℓδₙ,ℓ²)=d(50/n²+558/n³)→0.

If t>0, the independent sum ∑ℓδₙ,ℓ converges to N(0,5t) by the Lyapunov central limit theorem: its sum of third absolute moments is O(d n^{−3/2})→0 and its total variance tends to 5t>0. If t=0, its variance tends to zero, so it converges to zero in probability instead. Combining these facts on the event above, and ignoring its vanishing-probability complement, proves

(29)  Qₙ,d ⇒ Q_t=exp(√(5t)N−5t/2),  N∼N(0,1).

Independence in (1) and continuity of multiplication now yield

(30)  Z ⇒ √q G exp(√(5t)N/2−5t/4),  G independent of N.

This is a Gaussian scale mixture with log-normal variance, not a log-normal scalar preactivation. Its moments agree with (25): E Q_tʲ=exp(5t binom(j,2)). For any t>0,

(31)  lim κ₄(Zᵢ)/Var(Zᵢ)²=3(e^{5t}−1)>0.

There is no finite positive breakdown value of t for (21): it holds for every fixed finite c. Likewise Bₖ,₀(t), for fixed k, is a finite sum of exponentials and its Taylor series in t has infinite radius. Gaussian leading-order asymptotics require t→0; retaining a positive t does not preserve them, however small that fixed t is. These are different assertions from convergence of a cumulant series in source variables. For t>0, the limiting scalar law has

E Zᵢ^{2j}=qʲ(2j−1)!! exp(5t binom(j,2)),

and its moment generating function is infinite at every nonzero real argument: conditioning on Q_t gives E exp(q u²Q_t/2), and a log-normal variable has infinite positive exponential moments, as is seen by integrating exp(a exp(x)−(x+5t/2)²/(10t)) over x. The moment/source series has zero radius. Thus fixed-k results do not justify a convergent density expansion retaining arbitrarily high cumulants.

## 6. Relation to the literature and scope

The exact one-input product representation and the normal-times-log-normal limit are established background, rather than novelty claims here. Boris Hanin, *Random Fully Connected Neural Networks as Perturbatively Solvable Hierarchies*, [arXiv:2204.01058](https://arxiv.org/abs/2204.01058), JMLR 25 (2024), Appendix B.2.1 and Appendix D, discusses both. Corollary 8 gives low-order depth growth while allowing the width-error constants to depend on depth.

Mihai Nica and Janosch Ortmann, *Para-Gaussian Approximations of Random Deep Neural Networks*, [arXiv:2610.37388](https://arxiv.org/abs/2610.37388), October 2026, develops fourth-cumulant approximations and recursions. Section 1.6.2 distinguishes small depth-to-width ratio from positive-ratio limits. The full PDF opened in this session was marked v1; the arXiv page reports v2.

The checkable quantitative contribution here is (14), (17), and especially the all-orders resummed expansion (19)–(23), with the explicit first correction (25)–(26). No novelty priority is asserted for these elementary consequences of the exact one-input representation. A general multi-input conditional covariance is a random matrix, not a scalar independent product; neither its uniform cumulant hierarchy nor its positive-ratio joint limiting law is established by this argument.
