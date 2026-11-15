PARTIAL

# D0071 — the golden-mean lower bound for cubic transitive graphs

Date of literature check: 13 November 2026. The general question remains open in the latest primary source found. This report records later partial results and exact computations, not a new proof of the conjecture. The proof attempt on an additional candidate class does not close the lower-bound gap.

## 1. Exact source and question

The reference is Geoffrey R. Grimmett and Zhongyang Li, **“Self-Avoiding Walks and Connective Constants,”** in *Sojourns in Probability Theory and Statistical Physics — III: Interacting Particle Systems and Random Walks, A Festschrift for Charles M. Newman*, edited by Vladas Sidoravicius, Springer Proceedings in Mathematics & Statistics **300** (2019), **215–241**, DOI [10.1007/978-981-15-0302-3_8](https://doi.org/10.1007/978-981-15-0302-3_8). The publisher gives first online publication as 18 October 2019. The preprint is [arXiv:1704.05884](https://arxiv.org/abs/1704.05884), submitted 19 April 2017; v2 is dated 11 July 2019. Thus “2017 survey” identifies the preprint, while 2019 is the book publication year.

In **Section 3.2, Question 3.4, PDF/author-page 13**, in both arXiv versions, the exact question is:

> Is it the case that μ(G) ≥ φ for G ∈ G₃?

Here φ=(1+√5)/2=1.6180339887… . The definitions in Section 2.1, pp. 8–9, make G₃ the class of **infinite, connected, simple, vertex-transitive graphs of degree 3**. In expanded form the question is therefore:

**Does every infinite, connected, simple, vertex-transitive cubic graph G satisfy μ(G)≥(1+√5)/2?**

For a fixed root o, cₙ counts n-edge walks with no repeated vertex, and μ(G)=lim cₙ^(1/n). The existence theorem applies more broadly to quasi-transitive graphs, but Question 3.4 does not. The distinct notation Q₃ in Section 3.1 concerns quasi-transitive cubic graphs. The cited page 13 is the author/preprint pagination; it is not a claim about page 13 of the Springer volume.

Plain-text sources: [v1](sources/survey_1704.05884v1.txt), [v2](sources/survey_1704.05884v2.txt). Each contains explicit PDF-page separators.

### Why the hypotheses matter

Replacing transitivity by quasi-transitivity makes the assertion false. Here is an explicit simple cubic example with μ=1. Start with the double ray, with vertices indexed by Z. At each vertex attach, by one edge, a fresh copy of K₄ in which one edge has been subdivided; join the attachment edge to the new subdivision vertex. Every vertex now has degree 3, the graph is connected and quasi-transitive, and the attached pieces have five vertices. A SAW from a backbone vertex may enter an attached piece only as its final excursion: returning would revisit its attachment vertex. Its backbone segment is monotone in one of the two directions, and its final excursion has uniformly bounded length and finitely many possibilities. Hence cₙ is bounded above by a constant independent of n and bounded below by 2, so μ=1. This is not a counterexample to Question 3.4. The failure under quasi-transitivity is already discussed in Grimmett–Li, *Bounds*, pp. 6–7, Figure 4.1.

## 2. Literature first: verified results

Page references below are to the saved PDF version unless explicitly identified as journal pages. This avoids conflating preprint and journal pagination.

### 2.1 Grimmett–Li, *Cubic graphs and the golden mean*

The definitive publication is *Discrete Mathematics* **343**(1) (2020), article **111638**, 32 pages, DOI [10.1016/j.disc.2019.111638](https://doi.org/10.1016/j.disc.2019.111638), [arXiv:1610.00107](https://arxiv.org/abs/1610.00107). Submitted to arXiv 1 October 2016; accepted arXiv v4 dated 15 August 2019. The journal article was available online in September 2019. The saved [published text](sources/cubic_published.txt) is used for theorem numbering.

Theorem 1.2, p. 2, summarizes partial results, not a full resolution. The detailed results are:

| Result | Exact relevant scope and conclusion | Pages |
|---|---|---|
| Theorem 3.1(b) | G∈G₃ has a **transitive graph height function** ⇒ μ(G)≥φ. The acting subgroup in that height function must be transitive, not merely quasi-transitive. | statement p. 4; proof p. 7 |
| Theorem 3.1(a) | Cubic quasi-transitive G with the specified harmonic-function inequalities (3.2)–(3.3), i.e. G∈Q_harm, has μ(G)≥φ. | definitions p. 3; statement p. 4; proof pp. 6–7 |
| Theorem 3.1(c),(d) | Further sufficient conditions on a real function, respectively a harmonic function, involving girth and inequalities (3.4)–(3.5). These are additional conditional criteria, not all quasi-transitive cubic graphs. | statement p. 4; proof pp. 7–8 |
| Theorem 6.3 | A height function (h,H), H normal and of finite index in a transitive Γ, can be averaged to a transitive height function **if** the chosen coset representatives have uniformly bounded displacement (6.2). | pp. 9–10 |
| Corollary 6.4 | For a strong height function on a Cayley graph, the preceding conclusion holds **if** the chosen representatives have finite conjugacy classes, condition (6.3). | p. 10 |
| Theorem 6.6 | If Γ acts transitively and a height-function subgroup H fits into an exact sequence 1→K→Γ→H→1 with K finite, the graph has a transitive height function. | p. 10 |
| Theorem 8.1 | The specified first Grigorchuk Cayley graph with generators {a,b,c}, equivalently deleting d from {a,b,c,d}, satisfies μ≥φ. The relations and generator choice are in Section 8. | setup pp. 14–15; theorem p. 15; proof pp. 15–17 |
| Theorem 9.1 | Every infinite transitive TLF-planar cubic graph satisfies μ≥φ. TLF means that the planar embedding has no vertex accumulation point in the plane in question. | theorem p. 17; proof through p. 24 |
| Theorem 10.1 | Every Cayley graph of degree at least 3 of a **finitely presented two-ended group** satisfies μ≥φ. | theorem p. 25; proof pp. 25–26 |
| Theorem 10.2 | Partial results for finitely generated groups with infinitely many ends, specified below. | statement p. 25; proof pp. 28–31 |

For the harmonic criterion, put m(u) at a neighbor maximizing h(x)−h(u), and Mᵤ=h(m(u))−h(u), using the paper's choices of m and the third-neighbor map q. Its exact inequalities are

Mₘ₍ᵤ₎−Mᵤ < min{Mᵤ,M_qm(u)},

2M_qm(u) > Mₘ₍ᵤ₎−Mᵤ+M_mqm(u).

For the girth criteria, writing γ=⌈(g−1)/2⌉, (3.4) requires h(qm(u))>h(u) and h(mqm(u))>h(m(u)); (3.5) requires h((qm)^γ q(u))>h(u), at every u. Theorem 3.1(c) assumes (3.4)–(3.5); part (d) assumes harmonicity, (3.2), and (3.5). Remark 3.2, p. 4, gives convenient sufficient bounds on M: 2A<Mᵤ≤3A implies both harmonic inequalities. In particular constant positive M satisfies them.

**First Betti number:** a surjection Γ→Z gives a group height function, which is transitive for the left regular action. Thus all cubic Cayley graphs of a finitely generated group with infinite abelianization are covered; finite presentability is unnecessary for this elementary implication. The survey states its finitely presented version in Theorem 3.7 and the paragraph following it, p. 14. The first Betti number here is the rank of the free abelian part of Γ/[Γ,Γ], not simply the cycle rank of some finite quotient graph. Positivity of the latter alone is not the stated theorem.

The exact distinctions in **Theorem 10.2**, p. 25, are material. Let m≥3 be the minimum size of a symmetric generating set:

- If m≥4, every Cayley graph has μ≥√3>φ.
- If m=3 and Γ is an HNN extension, every Cayley graph has μ≥φ.
- If Γ=H*₍C₎K has a generating set S⊆H∪K with |S|=3, there **exists** a minimal such set S′ of size 3 whose Cayley graph has μ≥φ.
- For an amalgamated product there exists a minimal generating set whose Cayley graph has μ≥φ.

The last two are existential generating-set results. They do not settle every cubic Cayley graph of a group with infinitely many ends. Remark 10.7, p. 31, explicitly acknowledges this limitation. The introduction of the 2026 paper cites “10.2” for the two-ended result; the original published article places that result at **10.1**.

Small-girth bounds, all for infinite simple transitive cubic graphs, are exactly:

- **Theorem 7.1, p. 10:** if g=3, x₁≤μ≤x₂, where x₁⁻²+x₁⁻³=1/√2 and x₂⁻²+x₂⁻³=1/2; x₁≈1.529 and x₂≈1.769, and the upper bound is sharp.
- **Theorem 7.2, p. 11:** if g=4, 12^(1/6)≤μ≤1/ζ, where 2ζ²(1+ζ+ζ²)=1; the upper bound, about 1.900, is sharp.
- **Theorem 7.3, p. 11:** for degree d and girth g, the sharp upper bound is the connective constant of K₂*⋯*K₂*C_g, with d−2 copies of K₂. It is 1/ζ, where (d−2)M₁/(1+M₁)+M₂/(1+M₂)=1, M₁=ζ and M₂=2(ζ+⋯+ζ^(g−1)).

The survey's Theorems **3.5–3.7**, pp. **13–14**, give the small-girth lower bounds, TLF-planar result, and transitive-height result respectively. None establishes the conjecture for all girths or all graphs.

### 2.2 Bounds, monotonicity, locality, and height functions

| Primary source | Theorem, pages, and what it supplies |
|---|---|
| Grimmett–Li, *Bounds on connective constants of regular graphs*, *Combinatorica* 35 (2015), 279–294; [arXiv:1210.6277](https://arxiv.org/abs/1210.6277), [text](sources/bounds_1210.6277.txt) | Theorem **1.1**, p. **1**, and **4.1(a)**, p. **6**: √(d−1)≤μ≤d−1 for infinite connected simple d-regular transitive graphs. For d=3 this gives √2, which is less than φ. Theorem **4.2**, p. **7**, makes the upper inequality strict when a cycle occurs. |
| Grimmett–Li, *Strict inequalities for connective constants of transitive graphs*, *SIAM J. Discrete Math.* 28 (2014), 1306–1333; [arXiv:1301.3091](https://arxiv.org/abs/1301.3091), [text](sources/strict_1301.3091.txt) | Theorem **3.2**, p. **5**, gives strict increase on adding edges under the stated finite-coset-property automorphism condition. Theorem **3.8**, p. **10**, treats normal-subgroup directed quotients, with its type-1/type-3 or additional type-2 hypotheses; it is not an unqualified statement for arbitrary graph maps. Theorem **3.12**, p. **13**, treats free actions with symmetric quotient. Corollary **4.1**, p. **14**, gives the new-relator inequality for the stated finitely presented Cayley setting; Corollary **4.3**, p. **15**, gives increase on adding a generator. These compare constants; they do not supply φ without a suitable comparison graph. |
| Grimmett–Li, *Locality of connective constants*, *Discrete Math.* 341 (2018), 3483–3497; [arXiv:1412.0150](https://arxiv.org/abs/1412.0150), [text](sources/locality_1412.0150.txt) | Bridge theorem **4.3**, p. **11**: β=μ when a unimodular graph height function exists. Locality theorem **5.1**, p. **12**: if Gₙ have unimodular height functions with uniformly bounded parameters d(h)≤D and r(h,H)≤R, and rooted agreement radii K(G,Gₙ)→∞, then μ(Gₙ)→μ(G). The limit graph need not itself be assumed in that uniformly bounded height class. There is no general height-free locality theorem here. |
| Grimmett–Li, *Connective constants and height functions for Cayley graphs* (journal title uses “of Cayley graphs”), *Trans. Amer. Math. Soc.* 369 (2017), 5961–5980; [arXiv:1501.00476](https://arxiv.org/abs/1501.00476), [text](sources/height_1501.00476.txt) | Theorem **4.1**, pp. **7–8**, and Remark **4.2**, p. **8**, identify group-height existence with a nonzero integer null vector of the relator coefficient matrix, equivalently positive first Betti number. Theorem **5.1**, pp. **10–11**, constructs harmonic unimodular graph height functions for the stated derived-series class, including finitely generated virtually solvable groups. These height functions need not be transitive. |
| Grimmett–Li, *Self-avoiding walks and amenability*, *Electron. J. Combin.* 24(4) (2017), P4.38; [arXiv:1510.08659](https://arxiv.org/abs/1510.08659), [text](sources/amenability_1510.08659.txt) | Theorem **4.1**, p. **7**: every locally finite Cayley graph of an infinite finitely generated elementary amenable group has a harmonic strong graph height function. Theorem **5.1**, p. **8**: the specified Grigorchuk Cayley graph admits no graph height function. Theorem **6.2**, pp. **9–10**, gives μ≥(d−1)^((1+cλ)/2), c=d(d−1)/(d−2)², with λ the spectral bottom of I−P for simple random walk. |

Consequently **“virtually solvable,” “has a strong graph height function,” and “has a graph height function” must not be substituted for “has a transitive graph height function” in the golden-mean theorem**. They give bridge/locality tools; an extra numerical or geometric argument is still required. The finite-conjugacy and displacement conditions above are examples of additional hypotheses that do suffice. In the cubic spectral bound, λ≥(2log₂φ−1)/6≈0.0647473 suffices for μ≥φ. This does not handle every nonamenable graph, and gives only √2 on an amenable graph, where λ=0. The exponent in this formula was also checked against the arXiv TeX in memory.

### 2.3 Later work, 2017–2026

**All two-ended graphs in the question.** Agelos Georgakopoulos and Alex Wendland, [*A study of 2-ended graphs via harmonic functions*, arXiv:2304.13317](https://arxiv.org/abs/2304.13317) (2023), **Theorem 1.3, p. 3**, proof **pp. 9–10**, extends the earlier two-ended Cayley case to all two-ended vertex-transitive graphs of degree at least 3. Their **Theorem 1.4, p. 3**, constructs a cubic two-ended transitive graph that is not a Cayley graph, so the extension has new scope. [Text](sources/ends_2304.13317.txt).

Pagination/hypothesis caution: the displayed Theorem 1.3 literally says “Every 2-ended vertex-transitive graph”; the adjacent discussion excludes the double ray, whose μ=1. This report uses the degree-at-least-3/cubic consequence, for which that omission causes no ambiguity. No claim is made for the double ray.

**General Grigorchuk groups.** Geoffrey R. Grimmett, [*Connective constants of Grigorchuk graphs*, arXiv:2608.19349v2](https://arxiv.org/abs/2608.19349v2), submitted 19 August 2026, revised 7 October 2026. **Theorem 1.2, p. 2**, gives the golden-mean conclusion for the three-generator general-Grigorchuk Cayley graphs, with strict inequality when the defining sequence contains all three symbols. **Theorem 3.1(b),(c), pp. 6–7**, provides the quantitative form. [Text](sources/grigorchuk_2608.19349v2.txt).

More precisely, encode ω by the generator-section columns 0=(Π,Π,I), 1=(Π,I,Π), 2=(I,Π,Π), as in (2.3), p. 4. Delete one of bω,cω,dω from the four-generator set. Let δ be the generator whose initial column entry is I, and let β,σ be the other two:

- Deleting δ: γ≤μ<γ′, with γ≈1.635 the reciprocal of the positive root of 2x⁴(1+x²)(1+x)²=1. Here γ′≈1.895 is the reciprocal root of B(1+D+D²+D³)=1, with B=2x²(1+x²), D=2x³.
- Deleting z∈{β,σ}: φ≤μ<γ″≈1.892, with the same root equation but B=x²(1+x)², D=x²(1+x²). The lower inequality is strict if there exists k≥1 for which z_k(ω)=I.

In particular all three choices have μ>φ if ω contains 0,1,2 at least once; infinitely frequent occurrence is not the stated strictness condition. Remark **3.2**, p. **7**, identifies the earlier first-group result as only the deletion-of-d special case of (b).

Another necessary qualification: the paper writes Ω={0,1,2}^N₀ and states its summary with all ω∈Ω, but actual automorphism groups for constant ω have a trivial generator and two coinciding generators. For example at ω=000… one has dω=1 and bω=cω; the simple graph after deleting d is a double ray, not cubic. We use these results only for **genuinely cubic** generator sets; sequences containing all three symbols avoid this degeneracy. The loosely phrased “all ω” statement must not be used to infer φ for that collapsed graph. This is outside D0071's domain, not a counterexample to D0071.

The paper states on **p. 2** that the general question remains open. Thus the 2026 result is **PARTIAL**, not a full literature resolution.

Other requested leads were checked as follows:

| Work | Relevant result and relation to D0071 |
|---|---|
| Christian Lindorfer, *A general bridge theorem for self-avoiding walks*, *Discrete Math.* 343(12) (2020), 112092; [arXiv:1902.08493](https://arxiv.org/abs/1902.08493), [text](sources/lindorfer_1902.08493.txt) | **Theorem 3.2, p. 5:** for any graph height function, μ=max{β(h),β(−h)}. This removes the unimodularity requirement from that bridge representation, but neither constructs a missing height function nor proves the numerical bound φ. |
| Christoforos Panagiotis, *Self-avoiding walks and polygons on hyperbolic graphs*, [arXiv:1908.00127](https://arxiv.org/abs/1908.00127); *J. Graph Theory* (2024), DOI 10.1002/jgt.23087; [text](sources/panagiotis_1908.00127.txt) | **Theorems 1–4, pp. 2–3**, concern walk/polygon growth separation and ballisticity. **Proposition 3.3, p. 6**, gives μ(H(3,k))≥2(k−5)/(k−4) for k≥7. This is quantitative information for cubic hyperbolic tessellations, already within the TLF-planar class. |
| Florian Lehner, Christian Lindorfer, Christoforos Panagiotis, *Self-avoiding walk is ballistic on graphs with more than one end*, [arXiv:2403.13121](https://arxiv.org/abs/2403.13121); *Forum Math. Sigma* 13 (2025), e179 | In the saved arXiv text, **Theorem 1.3, p. 3**, gives μⁿ≤cₙ≤Cμⁿ and exponential ballisticity on transitive graphs with infinitely many ends; **1.1–1.2**, same page, give the broader quasi-transitive statements with the end-action hypothesis. These are not lower bounds μ≥φ. [Text](sources/ballistic_2403.13121.txt). |
| Lorenz A. Gilch and Sebastian Müller, *Counting self-avoiding walks on free products of graphs*, *Discrete Math.* 340(3) (2017), 325–332; [arXiv:1509.03209](https://arxiv.org/abs/1509.03209), [text](sources/gilch_muller_1509.03209.txt) | **Theorem 3.3, p. 6:** μ=1/z*, where Σᵢ Mᵢ(z*)/(1+Mᵢ(z*))=1 and Mᵢ counts nonempty rooted SAWs in the factors. **Corollary 3.4**, same page, gives algebraicity for finite factors. The formula underlies the sharp girth upper bounds, not a resolution for arbitrary cubic graphs. |
| Nathalie Aubrun and Nicolás Bitar, *Self-Avoiding Walks on Cayley Graphs Through the Lens of Symbolic Dynamics*, *Electron. J. Combin.* 31(4) (2024), P4.24; [arXiv:2402.13944](https://arxiv.org/abs/2402.13944), [text](sources/cayley_2024.txt) | **Theorem C, p. 4**, excludes graph height functions on Cayley graphs of infinite finitely generated torsion groups. The finite forbidden-word viewpoint is useful computationally. It does not prove the golden-mean conjecture. |
| Benjamin Grant and Zhongyang Li, *Self-avoiding walks on cubic graphs and local transformations*, [arXiv:2601.12571v2](https://arxiv.org/abs/2601.12571v2) (2026), [text](sources/transform_2601.12571.txt) | **Theorem 3.3, pp. 5–6**, gives the substitution identity μ(G)⁻¹=g(μ(G₁)⁻¹) for the specified symmetric three-port replacements; **Theorem 3.5, pp. 8–9**, gives the bipartite versions. These extend Fisher-type transformations to further quasi-transitive graphs. They are not a lower bound for every cubic transitive graph. |

Searches combining Bonato with the specified terms found no pertinent universal bound. The Bonato result returned concerns linked polymers in the simple cubic **lattice**, which has degree 6, rather than cubic degree-3 transitive graphs. It is not used as evidence here. A negative search is not a proof of absence. The primary 2026 open-status statement is the stronger evidence for retaining the problem as open.

## 3. Proof attempt and the remaining obstruction

### 3.1 A checked Fibonacci construction, and why it is not new

Suppose Γ=⟨a,b,c⟩, where a,b,c are distinct nonidentity involutions, and there is a homomorphism onto D∞=⟨r,s | r²=s²=1⟩ with a↦r, b↦s, c↦1. Form words by taking an alternating sequence a,b,a,b,… and optionally inserting a single c between successive letters or at the end.

Every nonempty factor containing an a or b projects to a nonempty alternating word in r,s, which is nonidentity. A factor containing only c is a single c and is also nonidentity. No nonempty factor represents 1 in Γ, so every such word is a SAW in the Cayley graph. Distinct label words give distinct rooted walks because the three generators are distinct. Their length generating series has denominator 1−x−x²; equivalently count them by successive blocks a or ac, then b or bc, and so on. Their growth rate is φ. Thus μ≥φ.

All steps of this argument hold without amenability, unimodularity, or finite presentability. However it is **already covered by printed Theorem 3.1(a)** of *Cubic*: the Cayley graph of D∞ on {r,s} is a double ray; pull back its integer coordinate h. At every vertex the three increments are {−1,0,+1}. Hence h is harmonic and M≡1, so (3.2)–(3.3) hold. This is a checked reproof of an existing sufficient condition, not a new class.

It also rules out Hanoi as an uncovered example. Grigorchuk–Šunić, [*Schreier spectrum of the Hanoi Towers group on three pegs*](https://arxiv.org/abs/0711.0068), **p. 4**, records an infinite-dihedral quotient of the Hanoi Towers group H. [Text](sources/hanoi_spectrum.txt). The generators are a=(1,1,a)(01), b=(1,b,1)(02), c=(c,1,1)(12).

To check the necessary images of the generators rather than assume them, use the two genuine Hanoi relations

`babcbabcacbcbabcbaca = 1`,

`babcbacabacacbcabaca = 1`.

Both are verified by full wreath recursion in `code/audit.py`. If all three images in D∞ were nonidentity, they would be reflections x↦−x+A, −x+B, −x+C. These two relations impose −4A+8B−4C=0 and −8A+4B+4C=0, hence A=B=C. Such images cannot generate D∞. Therefore at least one generator maps to identity; the other two must be distinct reflections. After relabelling, the checked construction applies. This supplies the application of the existing harmonic criterion; no Hanoi novelty is claimed.

### 3.2 The additional candidate: IMG(z²+i)

Let I be the group of automorphisms of the rooted binary tree generated by

a=(1,1)(01), b=(a,c), c=(b,1),

and take its Cayley graph X with these three generators. They are distinct nonidentity involutions, so X is simple, connected, transitive and cubic. It is infinite: Section 3.4 of D’Angeli–Donno, *Self-similar groups and finite Gelfand pairs*, *Algebra Discrete Math.* 2007(2), 54–69, **PDF pp. 10–11 / journal pp. 63–64**, proves spherical transitivity from this recursion. The action has orbits of size 2ᵏ at every level. [Text](sources/dangeli_donno_2007.txt).

Bux–Pérez, [*On the growth of iterated monodromy groups*, arXiv:math/0405456](https://arxiv.org/abs/math/0405456), **Theorem 25, p. 14**, proves subexponential growth of I; see also the intermediate-growth statement at **Theorem 6.7, p. 33** in Grigorchuk–Šunić's [survey text](sources/hanoi_branching_2007.txt). Thus this is an amenable example, so the spectral improvement above does not help. Its group abelianization is finite since it is generated by three involutions; there is no homomorphism I→Z. No specific golden-mean theorem for X was found. This is a candidate beyond the explicitly listed families, **not a claim that every possible harmonic or height-function criterion has been disproved for X**.

It is not one of the standard three-generator Grigorchuk Cayley graphs of the 2026 theorem: those have a commuting pair of nontrivial involutions, hence a 4-cycle, whereas the certified enumeration below gives girth 8 for X.

Here the direct Fibonacci attempt fails at a precise point. The relations

(ac)⁴=(ab)⁸=(bc)⁸=1

are printed on **journal p. 63 / PDF p. 10** of D’Angeli–Donno and independently checked by the code. The otherwise allowed word (ab)⁸ closes after 16 edges. Therefore the alternating-a,b language in Section 3.1 is not a language of SAWs on X.

There cannot even be a quotient onto D∞ of the required kind: the images of a,b,c must be identities or reflections. If one image is identity, the finite-order relations on its pairs force both other images to be identities. If all three images are reflections, the finite order of each pair product forces their reflection parameters equal. Neither case generates D∞. So this particular route is unavailable, not merely unverified.

The remaining alternatives were checked for missing hypotheses. Unimodularity alone supplies no scalar height function. A bridge theorem supplies μ=β or max{β+,β−} **after** a suitable height function has been constructed; it does not construct one or prove β≥φ. Submultiplicativity of cₙ provides upper bounds, not the Fibonacci lower recurrence. The constants in a ballisticity theorem do not supply a specified numerical value of μ. None closes the gap here.

**Outcome of the attempted proof:** no new lower bound μ(X)≥φ, and no counterexample, was obtained. The rigorous bound supplied by the universal theorem and this computation is

**√2 ≤ μ(X) < 1.992661.**

Proving μ(X)≥φ still requires a globally self-avoiding family with sufficient exponential growth, or another lower-bound argument. Even a solution for X would leave the unrestricted cubic transitive question to be proved.

## 4. Exact computations and their limits

All runs used one thread, niceness 10, and no worker agents. The largest measured resident set was about 322 MB. No PDF, image, scan, publication or push was made. All downloaded PDFs were held in memory only, immediately converted to page-labelled plain text, then discarded.

The controls are the ladder Z□K₂ and the standard cubic lamplighter Cayley graph C₂≀Z on {toggle,t,t⁻¹}. Both are covered in print; the lamplighter height is lamplighter position. Ordinary Baumslag–Solitar groups BS(m,n), m,n≠0, are torsion-free: they are HNN extensions of Z, and a cyclically reduced word containing a stable letter has nontrivial powers by the HNN normal form; any remaining finite-order element would be conjugate into Z. A symmetric generating set of odd cardinality requires a nonidentity involution. Consequently these groups admit no simple cubic Cayley graph with a finite symmetric generating set; their usual Cayley graphs have degree 4. A cubic replacement would need to be declared as a different graph. Hyperbolic triangle-reflection Cayley graphs are within the TLF-planar case. The first Grigorchuk group is also covered, as explained above.

### 4.1 Selected exact counts

Complete counts, including every n from 0 to the stated maximum, are in `data/*.csv` and `data/*.json`.

| Graph | n | cₙ | cₙ/cₙ₋₁, evidence only | √(cₙ/cₙ₋₂), evidence only |
|---|---:|---:|---:|---:|
| IMG(z²+i) | 8 | 382 | 1.989583333 | 1.994785… |
| IMG(z²+i) | 16 | 95,328 | 1.992725… | 1.992904671 |
| IMG(z²+i) | 28 | **373,782,420** | **1.992637832** | **1.992657990** |
| Hanoi | 20 | 1,572,744 | 1.999847412 | 1.999923… |
| Hanoi | 28 | **402,491,448** | **1.999911396** | **1.999913485** |
| Lamplighter | 24 | **22,276,916** | **1.984309316** | **1.984517897** |
| Ladder | 28 | **2,542,460** | **1.618020288** | **1.618046739** |

For Hanoi, cₙ=3·2^(n−1) for 1≤n≤19 and the first cycles have length 20. For IMG the first deviation is at n=8. These relatively high ratios suggest values well above φ, unlike the ladder control. **They do not certify a lower bound above φ or rule out slower eventual growth.** The exact upper bounds below leave the whole interval down to √2 open for IMG. In that rigorous sense these finite series do not determine whether its μ is near φ.

### 4.2 Why the counts are exact on the infinite graphs

`code/saw_counts.py` directly enumerates visited-vertex paths for the ladder and lamplighter, and uses canonical full-tree automorphisms for Hanoi through n=18. The larger counts use a separate finite-language method:

1. Enumerate every freely reduced word u of length at most 14 and its group action.
2. For every pair u,v with equal action, record the freely reduced identity word uv⁻¹. Every freely reduced identity word of length ≤28 is captured: split it into two halves of length ≤14.
3. For Hanoi the action is represented on the full tree. In a freely reduced word, two consecutive distinct generators cannot both contribute to the same first-level section. Thus section lengths contract to at most the ceiling of half the word length, eventually reaching the distinct singleton generators; recursive hash-consing gives exact equality. For IMG only, a depth-10 tree action proposes equalities. **Every candidate collision is then checked in the infinite group** by recursively expanding all sections until their finite closure is exhausted. If any reachable section has nonidentity root permutation, reject it. If all reachable permutations are identity, the original word fixes every finite tree word, so is identity. Section lengths never increase, so the closure is finite; there is no depth cutoff in this check. All 46,506 distinct candidate identity words passed.
4. Build an Aho–Corasick automaton forbidding aa,bb,cc and the captured identity factors. A label word is a SAW exactly when none of its nonempty factors is identity. Consequently its counts are **exact through length 28**. Beyond that they are upper counts only. Minimal-factor filtering for IMG leaves 10,588 forbidden identity words; Hanoi retains 4,200 words, including redundant ones.

A finite **Schreier vertex orbit** is never used as a substitute for a Cayley graph. The finite action represents entire group permutations, and even those equalities are independently checked before use. True equalities cannot be missed by passing to a finite action; checking every false-equality candidate removes the other possible error.

### 4.3 Rigorous upper bounds, not ratios posing as bounds

Submultiplicativity gives μ≤cₙ^(1/n), hence μ≤minₙ cₙ^(1/n), as well as the elementary cubic upper bound 2. A ratio cₙ/cₙ₋₁ is not generally an upper or lower bound.

For the finite forbidden-word automaton with nonnegative transition matrix A, all SAWs are accepted, so μ is at most the language growth rate. Take v=Aᵏ1. The code computes exact integer p,q with

qAv ≤ pv, v≥0, v₀>0.

Then, for n≥k,

(Aⁿ1)₀=(A^(n−k)v)₀≤(p/q)^(n−k)v₀,

which proves μ≤p/q. Zero entries in v are allowed; their Av entries must also vanish and are checked. This is a finite-memory upper-bound certificate, in the spirit of transfer-matrix/Kesten-type methods; no general ratio-limit theorem is assumed.

Exact numerators and denominators, plus reconstruction parameters, are saved in [IMG certificate](data/img_certificate.json) and [Hanoi certificate](data/hanoi_language_certificate.json). Outward rounding is checked by integer cross multiplication:

- **IMG:** μ≤1.9926601597029538… < **1.992661**.
- **Hanoi:** μ≤1.999913514820392… < **1.999914**.

Only for Hanoi, whose peg permutations act transitively on the three edges at the root, the CSV also gives the valid block bound μ≤(cₙ/3)^(1/(n−1)). No average-first-edge formula is asserted for the non-edge-transitive examples.

## 5. What was checked, reproducibility, and status

The [download manifest](data/source_manifest.json) records source URLs, dates, page counts, PDF SHA-256 hashes computed in memory, and retained-text hashes. Numbered-statement indexes in `data/` locate the main theorems without depending on a web snippet. PDF extraction occasionally warned about rotated text or fonts; the decisive equations were checked against surrounding arguments, an independent source, or TeX rather than trusting garbled formatting.

Run from this directory, in an environment with Python 3, `requests` and `pypdf`, and inherited niceness at least 10:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/saw_counts.py hanoi --n 18
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/saw_counts.py lamplighter --n 24
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/saw_counts.py ladder --n 28
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/hanoi_language.py --half 14 --block 200
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/img_counts.py --half 14 --depth 10 --block 200
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/audit.py
```

The independent audit checks every retained identity word with full recursion; brute-forces all SAWs through n=12 by testing every suffix rather than using the counting automaton; compares Hanoi's two enumeration methods through n=18; checks the ladder counts against the Fibonacci formula; reconstructs the integer matrix certificates; checks source hashes; and checks the folder for prohibited PDFs and paper images. Results are saved in [data/audit.json](data/audit.json).

**Final status: PARTIAL.** The literature extends the surveyed result to all two-ended cubic transitive graphs and to general Grigorchuk cubic Cayley graphs under the qualifications above. No full resolution was found; the October 2026 primary source still calls the general problem open. No new proof for an uncovered class and no cubic transitive counterexample is claimed. The additional IMG example has exact finite counts and a certified upper bound, while its golden-mean lower bound remains unproved here.

Task: “Open problem D0071,” received 13 November 2026, approximately 13:16 Asia/Tbilisi.
