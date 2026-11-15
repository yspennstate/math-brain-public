PARTIAL

# F0137: nonzero drift and spatial regeneration estimates for RWDE

The conjecture is not resolved here. No proof covering all nonzero drifts, including in dimension at least three, was found in the sources checked through 13 November 2026. Perrel–Sabot 2025 still assumes (T′).

This report supplies an explicit sufficient region strictly larger than (6.1), with a complete finite-box argument and an identified published renormalization theorem as input. This makes the existing Bouchet–Ramírez–Sabot small-backward-weight theorem quantitative; it is not claimed as a new ballisticity theorem. It also proves unconditional divergence of first-renewal moments at and above κ, derives a moment result without (T) for later regeneration intervals in d ≥ 3, and gives a finite exact certificate reduction. The general unconditioned first-renewal problem remains open in this work. Simulations retain time censoring and distinguish provisional renewal candidates from actual renewal times.

## 1. Exact statement and definitions

Put
\[
a_i=\alpha_i,\quad b_i=\alpha_{i+d},\quad t_i=a_i+b_i,\quad
\delta_i=a_i-b_i,\quad
S=\sum_{j=1}^{2d}\alpha_j=\sum_{i=1}^d t_i,
\]
\[
d_\alpha=(\delta_i)_{i=1}^d,\qquad D=\|d_\alpha\|_1,\qquad
\kappa=2S-\max_i t_i.
\]
The mean environment has drift \(d_\alpha/S\); the source uses the unnormalized vector \(d_\alpha\).

For \(d_\alpha\cdot\ell>0\), the overview's first renewal time is
\[
\tau_1=\inf\{n\ge1:\ \forall i<n\le j,\quad
 X_i\cdot\ell<X_n\cdot\ell\le X_j\cdot\ell\}.
\]
Definition 5, [arXiv:1601.08219](https://arxiv.org/abs/1601.08219), PDF p. 18, defines \((T)_\gamma\), \(0<\gamma<1\), as directional transience together with
\[
\exists c>0:\quad
E_0\exp\left(c\left(\max_{0\le n\le\tau_1}|X_n|\right)^\gamma\right)<\infty.
\tag{1}
\]
Condition \((T')\) means (1) for every \(\gamma\in(0,1)\). Theorem 6, p. 18, gives
\[
(T)_\gamma\text{ for some }\gamma
\quad\Longrightarrow\quad
\left(E_0[\tau_1^s]<\infty\ \Longleftrightarrow\ s<\kappa\right),\quad s>0.
\tag{2}
\]
The sufficient condition in Theorem 7 is exactly
\[
\boxed{\sum_{i=1}^d|\alpha_i-\alpha_{i+d}|>1.}
\tag{6.1}
\]
Corollary 2 and the conjecture are on p. 19. The source actually conjectures \((T')\) for every nonzero drift, stronger than one exponent \(\gamma\).

The published overview, Ann. Fac. Sci. Toulouse 26 (2017), 463–509, renumbers these as Definition 6.1 (p. 485), Theorems 6.3 and 6.5 (p. 486), and Corollary 6.6 plus the conjecture (p. 487). Both versions are retained as text.

### Spatial versus temporal control

For unit \(u\), let \(T_L^u=\inf\{n:X_n\cdot u\ge L\}\) and \(\widetilde T_{-bL}^u=\inf\{n:X_n\cdot u\le-bL\}\). The equivalent slab condition requires a neighborhood \(V\) of \(\ell\) such that for every \(u\in V\) and \(b>0\),
\[
\limsup_{L\to\infty}L^{-\gamma}
 \log P_0(\widetilde T_{-bL}^u<T_L^u)<0.
\tag{3}
\]
Campos–Ramírez Theorem 2.4, arXiv PDF p. 9, supplies the elliptic equivalence and transfer to the positive hemisphere of the asymptotic direction. See also Sznitman 2002, Theorem 1.1 and Corollary 1.5, journal pp. 515–521. The neighborhood quantifier matters.

A two-vertex trap may keep the walk alternating for a huge time while its radius remains one. Finite traps therefore obstruct time moments and prevent importing uniformly elliptic conclusions. Their existence alone does not contradict \((T)_\gamma\): BRS examples satisfy \((T')\) even when \(\kappa<1\). The missing spatial estimate concerns large backward/lateral excursions before renewal, rather than the already understood time penalty of a local trap. “Large weights” in the trap mechanism means large realized internal transition probabilities relative to exits; large absolute Dirichlet parameters are not necessary.

## 2. Literature audit

PDF pages below refer to the particular retained text, marked page by page in sources/. The manifest records URLs, retrieval times and hashes. Sections 4–6 of the requested overview were read throughout, arXiv pp. 11–19.

| Reference | Exact theorem/section and PDF page checked | What it does; why it does not settle F0137 |
|---|---|---|
| Sabot–Tournier, arXiv:1601.08219; published 2017 | Propositions 1–2, p. 11; Theorems 1–5, pp. 12–17; Definition 5, Theorems 6–7, p. 18; Corollary 2, p. 19 | Distinguishes the known d ≥ 3 velocity classification from the missing spatial/higher-moment estimate. |
| Bouchet–Ramírez–Sabot, Bernoulli 22 (2016), 969–994, [DOI 10.3150/14-BEJ683](https://doi.org/10.3150/14-BEJ683), arXiv:1310.6281 | Theorem 1, reprint p. 4; Remarks 4–5, pp. 5–6; Theorem 5 and Remark 8, p. 8; Proposition 10, p. 15; proof §4.2, pp. 23–26 | Renewal tails given a polynomial spatial criterion; verifies that criterion with one sufficiently small backward weight. Remark 8 explicitly distinguishes d ≥ 3 ballisticity from \((T')\). |
| Fribergh–Kious, PTRF 165 (2016), 795–834, [DOI 10.1007/s00440-015-0646-4](https://doi.org/10.1007/s00440-015-0646-4), arXiv:1404.2060 | Theorems 2.1–2.2, pp. 7–8; Theorem 3.1, p. 8; Theorem 3.2, pp. 10–11; Proposition 5.1, p. 25; proofs §§5.1–5.3 | Refines local trapping criteria, while retaining \((E)_0\) and \((P)_M\) as hypotheses. Does not verify \((P)_M\) for arbitrary Dirichlet drift. |
| Campos–Ramírez, PTRF 160 (2014), 189–251, [DOI 10.1007/s00440-013-0527-7](https://doi.org/10.1007/s00440-013-0527-7), arXiv:1212.4020 | Theorem 1.1, p. 3; Theorem 2.4, p. 9; proof chain §3 | Under \((E)_0\), \((P)_M\) is equivalent to \((T')\). Dirichlet laws satisfy \((E)_0\). Equivalence does not verify either condition for all parameters. BRS Remark 1 corrects the seed constant. |
| Berger–Drewitz–Ramírez, CPAM 67 (2014), 1947–1973, [DOI 10.1002/cpa.21500](https://doi.org/10.1002/cpa.21500), arXiv:1206.6377 | Theorem 1.6 and Corollary 1.7, p. 4; Propositions 2.1 and 2.3, pp. 5–6; §§2–4 | Finite polynomial seed implies \((T')\), initially under uniform ellipticity. Dirichlet application needs CR/BRS. |
| Guerra–Ramírez, CPAM 73 (2020), 2087–2103, [DOI 10.1002/cpa.21877](https://doi.org/10.1002/cpa.21877), arXiv:1809.02011 | Hypotheses §2, p. 2; Theorem 2.1, p. 3; proof §3 | Proves \((T')\Rightarrow(T)\) for i.i.d. uniformly elliptic environments. This is a different conjecture; Dirichlet laws are not uniformly elliptic. |
| Perrel–Sabot, [arXiv:2501.06767v1](https://arxiv.org/abs/2501.06767) (2025) | §2.2.2, pp. 7–8; Theorems 2.3–2.4, p. 8; §2.2.4 and Conjecture 1, p. 9; Lemma 6.1, p. 25 | Theorem 2.3 assumes \((T')\) and \(\kappa>1\). The paragraph before Conjecture 1 expects the spatial assumption to be redundant. Lemma 6.1 explicitly uses it for spatial localization. |
| Tournier, EJP 14 (2009), 431–451, [DOI 10.1214/EJP.v14-609](https://doi.org/10.1214/EJP.v14-609), arXiv:0801.2875 | Published Theorems 1–3, p. 435; Corollaries 4–5 and Theorem 6, pp. 435–436; proofs §§3–4, pp. 436–449; Proposition 12, p. 449 | Finite-graph integrability and the L1 drift condition (6.1), by integration by parts. Published numbering differs from the old preprint. |
| Bouchet, EJP 18 (2013), article 58, [DOI 10.1214/EJP.v18-2109](https://doi.org/10.1214/EJP.v18-2109), arXiv:1205.5709 | Retained arXiv Theorems 1, 2, 5, pp. 3–5; invariant-law and ergodic proofs §§3–4 | Acceleration gives nonzero physical-time speed and directional classification in d ≥ 3, not the spatial stretched-exponential estimate. The overview's published Theorem 2.4 citation uses different numbering. |
| Sabot, Ann. Probab. 41 (2013), 722–743, [DOI 10.1214/11-AOP699](https://doi.org/10.1214/11-AOP699), arXiv:1007.2565 | Theorems 1–2, reprint pp. 4–5; invariant-density and flow proofs | Nonzero velocity for \(\kappa>1,d_\alpha\ne0\) in d ≥ 3; positive speed does not imply the needed tail bound. |
| Poudevigne–Auboiron, EJP 29 (2024), article 51, 1–66, [DOI 10.1214/23-EJP945](https://doi.org/10.1214/23-EJP945), arXiv:1909.03866 | Retained preprint Theorem 1, p. 4; Proposition 1.2.1, p. 2; Lemma 2.1.2 and proof, pp. 8–9; trap decomposition | Stable limit without \((T)\), for \(\kappa<1\). Finite mean range is weaker than stretched-exponential radius control. Section 5 derives a precise later-interval consequence. |
| Perrel, [arXiv:2404.06502](https://arxiv.org/abs/2404.06502) (2024) | §1.3, pp. 6–7; Theorem 6, p. 8; trap definition, p. 9; Lemma 17, p. 30 | Stable fluctuations for \(1<\kappa<2\) assume \((T)\); §1.3 describes the general spatial conjecture as unproved. |
| Ramírez–Ribeiro, EJP 27 (2022), [DOI 10.1214/22-EJP856](https://doi.org/10.1214/22-EJP856), arXiv:2107.00113 | Theorems 1–2, pp. 4 and 6; §2 | Sharper local trapping criteria, with the polynomial spatial condition still assumed. |

Earlier Enriquez–Sabot (arXiv:math/0503713) and Sabot–Tournier (arXiv:0905.3917) were also read for their drift and reversal arguments. The latter's Proposition 1, p. 3, is the finite-graph reversal identity, not a slab tail estimate. Sznitman 2002, [DOI 10.1007/s004400100177](https://doi.org/10.1007/s004400100177), is retained; its equivalence proof and appendix were checked. Direct retrieval of Sznitman 2001 failed at Project Euclid and an attempted IMS mirror, so its full original proof was not independently read here. Its relevant equivalence is checked through the retained 2002 paper and CR's elliptic formulation. Retrieval failures are recorded rather than represented as reading.

### 2016–2026 follow-up search

An OpenAlex forward-citation query for the published overview returned 24 records, including duplicates and citations in other models. The raw response and screening are saved in data/. This is a bounded search, not a claim of an exhaustive census. It was supplemented by arXiv searches for 1601.08219, Dirichlet ballisticity, nonzero drift, \((T)\), \((T')\), renewal times, Perrel and Sabot, and by the authors' publication pages.

The relevant rough-path follow-ups retain spatial assumptions: Lopusanschi–Orenshtein, arXiv:1812.01403, Theorem 5.5, PDF p. 10, uses the known drift region; Orenshtein, arXiv:2101.05222, §2.3, pp. 5–6, improves moment requirements while retaining the spatial hypothesis. The 2023 Devulder–Diel–Zeng survey concerns estimation and Dirichlet laws on decomposable graphs. Orenshtein–Sabot, arXiv:1804.01406, introduction p. 2, explicitly notes that reversal/invariant-law methods do not provide Sznitman spatial estimates. The 2024 first-passage paper arXiv:2310.17123 proves a zero-temperature reversal identity. The 2025 ⋆-ERRW and 2026 ⋆-VRJP papers concern mixing representations, not general lattice slab estimates. The October 2026 citing paper arXiv:2610.36326 studies random operators and quantum walks on locally tree-like graphs.

A broad-search hit, arXiv:2601.06751, was checked against its primary abstract: arXiv withdrew it for unverifiable authorship/affiliation. It is excluded. Search hits about 2026 uniformly elliptic directional-transience/velocity claims also exclude Dirichlet laws and are not resolutions of F0137. No applicable all-drift theorem was located, for d = 2 or d ≥ 3.

## 3. Exactly what (6.1) omits

Fix \(t_i>0\). The coordinates
\[
a_i=(t_i+\delta_i)/2,\qquad b_i=(t_i-\delta_i)/2,\qquad |\delta_i|<t_i
\tag{4}
\]
are bijective. The directionally transient parameters omitted by (6.1) are exactly
\[
\boxed{\{\alpha>0:\ 0<\|d_\alpha\|_1\le1\}.}
\tag{5}
\]
For d = 2 this is a punctured diamond in the drift plane, intersected with \((-t_1,t_1)\times(-t_2,t_2)\). For d = 3 it is a punctured octahedron intersected with the corresponding rectangular box.

There is no uniform fraction on the entire unbounded parameter space. Two specified slice measures give exact quantities.

**Fixed pair sums.** The omitted fraction of the drift box, equivalently of the α slice by the constant Jacobian in (4), is
\[
F_d(t)=\frac{\sum_{A\subseteq\{1,\ldots,d\}}(-1)^{|A|}
 (1-\sum_{i\in A}t_i)_+^d}{d!\prod_i t_i}.
\tag{6}
\]
In particular,
\[
F_2=\frac{1-(1-t_1)_+^2-(1-t_2)_+^2+(1-t_1-t_2)_+^2}{2t_1t_2},
\]
\[
F_3=\frac{1-\sum_i(1-t_i)_+^3+\sum_{i<j}(1-t_i-t_j)_+^3
 -(1-t_1-t_2-t_3)_+^3}{6t_1t_2t_3}.
\]
Proof: in each sign orthant intersect the simplex \(\sum z_i\le1\) with \(0<z_i<t_i\). Inclusion–exclusion of the caps \(z_i\ge t_i\), followed by translation, gives each term in (6), divided by d!. Divide by the orthant-box volume. Boundaries and zero drift have zero volume.

**Fixed total S.** Under normalized Lebesgue measure on \(\{\alpha>0:\sum\alpha_i=S\}\), \(D/S\) has the Beta(d,d) law. The exact omitted fraction is 1 for S ≤ 1 and for S > 1 is
\[
d=2:\ 3S^{-2}-2S^{-3},\qquad
d=3:\ 10S^{-3}-15S^{-4}+6S^{-5}.
\tag{7}
\]
Proof: in each sign orthant write \(z_i=|a_i-b_i|\), \(m_i=\min(a_i,b_i)\). The Jacobian is constant and \(2\sum m_i+\sum z_i=S\). At \(\sum z_i=r\), the two simplex-volume factors are proportional to \(r^{d-1}\) and \((S-r)^{d-1}\). Normalizing gives Beta(d,d); integration proves (7).

| S | Omitted fraction d = 2 | d = 3 |
|---:|---:|---:|
| S ≤ 1 | 1 | 1 |
| 2 | 1/2 | 1/2 |
| 4 | 5/32 | 53/512 |
| 10 | 7/250 | 107/12500 |

For d = 2, \(\kappa=2(t_1+t_2)-\max(t_1,t_2)\); for d = 3, \(\kappa=2(t_1+t_2+t_3)-\max_i t_i\). Since \(\kappa>S>D\) for positive weights in d ≥ 2, all \(\kappa\le1\) parameters are omitted by (6.1). Conversely the omitted set has arbitrarily large κ and arbitrarily small nonzero drift: take every weight A except \(\alpha_1=A+\epsilon\), with \(0<\epsilon\le1\). Then \(D=\epsilon\), \(\kappa=(4d-2)A+\epsilon\).

Tournier's integration-by-parts proof puts the auxiliary Kalikow drift in
\[
\frac{d_\alpha-\operatorname{conv}\{\pm e_i\}}{S-1}\quad(S>1).
\tag{8}
\]
The convex hull is the L1 unit ball. For D > 1, the sign vector of δ separates with positive margin D−1. For D ≤ 1, this enclosure contains zero. Thus the proof loses its uniform drift bound there; this does not prove that Kalikow's condition or \((T')\) fails there.

## 4. The local trap obstruction, with complete proofs

### Proposition A: unconditional divergence at the endpoint

For every \(d_\alpha\cdot\ell>0\),
\[
E_0[\tau_1^s]=\infty\qquad(s\ge\kappa),
\tag{9}
\]
without a \((T)\) assumption.

Proof. Fix i. The random variables \(p=\omega(0,e_i)\) and \(q=\omega(e_i,0)\) are independent, with laws Beta(\(a_i,S-a_i\)) and Beta(\(b_i,S-b_i\)). The event \(A_n\) of alternating \(0,e_i,0,\ldots,e_i,0\) for the first 2n steps has exact annealed probability
\[
P_0(A_n)=E[(pq)^n]
 =\frac{(a_i)_n(b_i)_n}{(S)_n^2}
 \sim\frac{\Gamma(S)^2}{\Gamma(a_i)\Gamma(b_i)}
 n^{-(2S-a_i-b_i)}.
\tag{10}
\]
Here \((a)_n\) is the rising factorial; the asymptotic follows from the gamma-ratio asymptotic.

On \(A_n\), no positive-time strict record is successful by 2n. If \(e_i\cdot\ell>0\), its first visit is followed by a return below it; subsequent visits are not strict records. If \(e_i\cdot\ell\le0\), there is no positive-height record. Thus \(A_n\subseteq\{\tau_1>2n\}\). Choose i maximizing \(t_i\). The resulting \(cn^{-\kappa}\) tail lower bound and the tail-integral formula for moments prove (9), including equality. ∎

For the pair \(K=\{0,e_i\}\), the same computation gives
\[
P_0(T_K>2n)=\frac{(a_i)_n(b_i)_n}{(S)_n^2}.
\tag{11}
\]
The odd tails lie between adjacent even tails. Hence
\[
E_0[T_K^s]<\infty\ \Longleftrightarrow\ s<2S-t_i.
\tag{12}
\]
A second derivation uses \(U=1-p,V=1-q\): their small-value exponents are \(S-a_i,S-b_i\), and
\((U+V)/2\le1-pq\le U+V\). This gives the same threshold for the quenched Green function \(1/(1-pq)\).

Two vertices minimize the finite-trap outgoing weight. For a finite vertex set A let \(n_i(A)\) count its components on lines parallel to \(e_i\). Its outgoing weight is \(\beta_A=\sum_i t_i n_i(A)\). If A contains an edge parallel to \(e_j\), then \(n_j\ge1\) and \(n_i\ge2\) for i ≠ j, since that edge's endpoints lie on different i-parallel lines. Thus \(\beta_A\ge2S-t_j\ge\kappa\). A maximizing-direction pair attains κ. Tournier's finite-graph theorem turns these cut weights into integrability thresholds. This does not bound how many traps or how large a spatial excursion occur before renewal.

## 5. A moment equivalence without (T) for later intervals

Let \(\sigma_k\) be the renewals in Poudevigne's retained preprint and \(Y=\sigma_2-\sigma_1\), an ordinary interval after the first. For d ≥ 3, nonzero drift with the chosen coordinate pointing forward, and \(0<\kappa<1\),
\[
\boxed{E[Y^s]<\infty\ \Longleftrightarrow\ s<\kappa.}
\tag{13}
\]
This is a consequence of published results, without \((T)_\gamma\), not a new assertion about the unconditioned first interval. We keep the paper's convention: its printed p. 2 uses a strict future inequality; the overview uses a weak future inequality. No transfer between conventions is being silently assumed.

Proof. Poudevigne Theorem 1 gives \(n^{-1/\kappa}\sigma_n\Rightarrow Z\), a nondegenerate positive κ-stable variable. Proposition 1.2.1 supplies independent identically distributed later increments, independent of the initial piece. With \(\phi(t)=E[e^{-tY}]\) and σ₁ finite almost surely,
\[
E[e^{-\sigma_1/n^{1/\kappa}}]\,\phi(n^{-1/\kappa})^{n-1}
 \longrightarrow E[e^{-Z}]=e^{-C},\qquad C>0.
\]
The first factor tends to one. Taking logarithms yields
\(n(1-\phi(n^{-1/\kappa}))\to C\). Monotonicity and squeezing t between consecutive values \(n^{-1/\kappa}\) give
\[
1-\phi(t)\sim Ct^\kappa,\quad t\downarrow0.
\tag{14}
\]
For \(0<s<1\), Tonelli and substitution \(u=ty\), followed by integration by parts, give
\[
E[Y^s]=\frac{s}{\Gamma(1-s)}
 \int_0^\infty (1-\phi(t))t^{-s-1}\,dt.
\tag{15}
\]
The integral converges at infinity and, by (14), converges at zero for s < κ and diverges at s = κ. Since Y ≥ 1, all s > κ moments also diverge. ∎

The first interval disappears under stable scaling simply because it is finite almost surely. That does not control any of its moments. Therefore (13) does not prove (2) for the unconditioned τ₁. For d ≥ 3 and κ > 1, the known ballisticity theorem does give first-moment integrability, as recorded in overview §6, p. 17, and hence the moments \(0<s\le1\). The sharp higher moments still need additional work.

## 6. Explicit sufficient region larger than (6.1)

The following is a quantitative version of BRS Theorem 5. Distinguish +e₁, set \(a=\alpha_1,b=\alpha_{1+d}\), and fix every weight except b. Put
\[
A=\sum_{j\ne1+d}\alpha_j,\quad S_*=A+1,\quad
p=a/S_*,\quad M=15d+6.
\]
Choose \(0<r<\min_{j\ne1+d}\alpha_j\), and define
\[
\eta_*=\max_{j\ne1+d}
 \frac{\Gamma(S_*)\Gamma(\alpha_j-r)}
      {\Gamma(S_*-r)\Gamma(\alpha_j)},\qquad
C=3^{121d^4+3001d(1+r^{-1}\log\eta_*)^2},
\]
\[
L=\left\lceil\max\{2,C,(M+1)/p^2\}\right\rceil,\qquad
\epsilon=\min\{1,a/(4L^{M+1})\}.
\tag{16}
\]

### Proposition B

If \(0<b\le\epsilon\), then \((T')\) holds in e₁ and in every \(\ell\) with \(d_\alpha\cdot\ell>0\), and (2) follows. The union of (6.1) and (16), over signed coordinate choices, is a strictly larger explicit sufficient region.

Proof. Use \(B=(-L,L)\times(-W,W)^{d-1}\cap\mathbb Z^d\), \(W=70L^3\). Let \(q_B\) be the annealed probability of exiting outside the front \(x_1=L\). We prove
\[
q_B\le\frac{Lb}{a+b}+\exp(-p^2W/2).
\tag{17}
\]

Before the first −e₁ step, axial layers are visited in increasing order and are virgin upon arrival. At each vertex in a new layer, split its Dirichlet vector into axial total H, axial ratio R, and normalized transverse probabilities V. The independent gamma representation gives \(R\sim\mathrm{Beta}(a,b)\) independently of (H,V). The layer trajectory before its first axial departure uses only H and V, even if vertices are revisited. The eventual departing sign therefore has backward probability b/(a+b), conditional on arrival and the prior layers.

The layer departure exists almost surely. On an infinite fresh-vertex sequence, independent positive axial hazards prevent perpetual survival; on a finite visited set a positive minimum hazard prevents it. Alternatively the known directional transience for b < a rules out permanent confinement to a layer. There are at most L fresh layers before a front exit. Summing the probability of the first backward departure at each layer bounds the probability of any backward step before box exit by \(Lb/(a+b)\). An earlier lateral exit only reduces this event.

On a lateral exit with no backward step, the first hitting points of transverse sup-norm levels \(k=0,\ldots,W-1\) are W distinct fresh vertices. Before exposing each one's outgoing environment, its next step has annealed probability \(a/(A+b)\ge p\) of being +e₁. Use independent uniforms for these fresh exposures, padding with unused independent uniforms if the box exploration stops early. Thus the W success indicators dominate independent Bernoulli(p) variables. This domination is unconditional, not a claimed independence after conditioning on lateral exit.

Fewer than L forward steps can occur on a lateral exit with no backward step. Consequently that event implies \(\mathrm{Bin}(W,p)\le L\). Since \(L\le pW/2\), Hoeffding bounds its probability by \(\exp(-p^2W/2)\), proving (17).

We now check the admissible seed scale. For every forward/transverse j ≠ 1+d,
\[
E[\omega(0,e_j)^{-r}]
=\frac{\Gamma(A+b)\Gamma(\alpha_j-r)}
       {\Gamma(A+b-r)\Gamma(\alpha_j)}
\le\eta_*.
\tag{18}
\]
Indeed b ≤ 1 and \(\Gamma(x)/\Gamma(x-r)\) increases for x > r, since its log derivative is \(\psi(x)-\psi(x-r)>0\). BRS Eq. (1.1), PDF p. 3, uses these forward-half-space inverse moments in the polynomial seed constant; the corrected constant is bounded by
\[
\frac23\,3^{120d^4+3000d(r^{-1}\log\eta_*)^2}<C.
\]
Thus L is admissible. Full-direction \((E)_0\) also holds because b > 0. The forward bound is essential: using a seed constant based on the smallest parameter over *all* directions would wrongly make it blow up as b decreases.

By (16), the first term of (17) is at most \(Lb/a\le1/(4L^M)\). Also
\[
35p^2L^3\ge35(M+1)L^2>\log2+M\log L,
\]
so its second term is at most \(1/(2L^M)\). Hence \(q_B\le3/(4L^M)<L^{-M}\).

This verifies BRS Definition 1's effective \((P)_M\) condition. The published renormalization input is CR Theorem 1.1 with the seed correction in BRS Remark 1, implying \((T')\). The finite-box estimate and parameter checks above are complete; that established renormalization theorem is not reproved here. CR Theorem 2.4 transfers each exponent to the positive hemisphere of the asymptotic direction \(d_\alpha/|d_\alpha|\). Overview Theorem 6 yields (2). ∎

This proof also avoids two typographical pitfalls in the extracted BRS argument: the ratio law is Beta(a,b), and the seed constant is *bounded uniformly* as b decreases, not literally independent of b.

For a strict enlargement take \(a=1/4\), all transverse weights \(1/10\), and b as in (16). Then \(D=1/4-b<1\). In d = 2, \(\kappa=0.65+b<1\); in d = 3, \(\kappa=1.05+b>1\). The constants are conservative: with r = 0.05, an explicit smaller example has \(\log_{10}b\) approximately −24,795,926 in d = 2 and −53,703,430 in d = 3. These are mathematical examples, not the simulated parameters.

### Limits of reversal and acceleration

Swapping opposite weights preserves S, D and κ, as do coordinate reflections and permutations. Applying these symmetries to (6.1) cannot enlarge its region. Finite-graph time reversal uses
\(\check\omega(y,x)=\pi^\omega(x)\omega(x,y)/\pi^\omega(y)\).
Reversing a path introduces correlated stationary endpoint factors; it does not identify fixed-origin slab probabilities after those factors are dropped.

Local acceleration preserves the ordered sequence of vertices and all spatial exit events. Positive physical-time speed of the accelerated process therefore does not supply a stretched-exponential spatial regeneration estimate for that sequence.

## 7. Exact finite-certificate reduction

For a finite path with outgoing counts \(n_{x,j}\), \(n_x=\sum_j n_{x,j}\), independent Dirichlet integration gives
\[
P_0(\text{path})=\prod_x
 \frac{\prod_j(\alpha_j)_{n_{x,j}}}{(S)_{n_x}}.
\tag{19}
\]
Equivalently multiply the urn predictive probabilities
\((\alpha_j+n_{x,j})/(S+n_x)\). These are rational for rational parameters.

Enumerate paths stopped at first exit from a fixed finite box B or at N steps. Let \(f_N,b_N,r_N\) be their total front-exit, bad-exit, and survival probabilities. Then
\[
f_N+b_N+r_N=1,\qquad b_N\le q_B\le b_N+r_N=1-f_N=:u_N.
\tag{20}
\]
The upper bounds decrease to \(q_B\). To prove convergence, fix an environment: choose from every interior vertex a path out of B of length at most K. The minimum of these finitely many positive path probabilities is some \(\varepsilon(\omega)>0\). The strong Markov property bounds survival for mK steps by \((1-\varepsilon(\omega))^m\). Bounded convergence then gives \(r_N\to0\) annealed.

A finite certificate
\[
L\ge c_0,\quad \widetilde L\le70L^3,\quad u_N<L^{-M},\quad M=15d+6
\tag{21}
\]
therefore proves \((T')\) by CR/BRS. If an admissible box has \(q_B<L^{-M}\), some finite N certifies it. Dovetailing admissible boxes and N is a complete semidecision procedure for the *strict* finite-box criterion at rational α. A seed bound as in (16), using full-direction inverse moments when appropriate, makes admissibility explicit. This is a precise reduction, not a completed certification of small-drift parameters. A uniform proof of (21) for all nonzero drifts is still missing.

The toy exact enumeration in code/ is far below c₀ and certifies no new point. For \(\alpha=(11/20,1/2,1/2,1/2)\), L = W = 1 gives \(q_B=30/41\). For L = W = 2, \(u_N\) decreases from 0.928019 at N = 2 to 0.759438 at N = 8. Independent quenched-matrix averaging over 50,000 environments agrees with all four exact finite-horizon front probabilities within 0.55 Monte Carlo standard errors.

## 8. Numerical evidence

Each replicate samples an independent fixed environment lazily: a site's Dirichlet vector is sampled once and reused. This is RWDE, not a random walk in the mean environment. Directions are ordered (+e₁,…,+e_d,−e₁,…,−e_d).

| Model | α | D | κ | Replicates per width |
|---|---|---:|---:|---:|
| d2_moderate | (.55,.50,.50,.50) | .05 | 3.05 | 1,500 |
| d3_moderate | (.55,.50,.50,.50,.50,.50) | .05 | 5.05 | 1,500 |
| d2_trapping | (.10,.08,.08,.08) | .02 | .50 | 500 |
| d3_trapping | (.07,.05,.05,.05,.05,.05) | .02 | .52 | 500 |

All four lie outside (6.1); Proposition B does not certify them. Slabs are infinite in transverse directions. Stop at \(x_1=\pm L\), or cap at 300,000 steps for moderate models and 100,000 for trapping models. Widths are 4,8,16,32,64, independently replicated.

| Model | Backward counts at the five widths | Censored counts |
|---|---|---|
| d2_moderate | 673, 533, 385, 150, 35 | 0, 0, 0, 0, 0 |
| d3_moderate | 636, 529, 280, 85, 4 | 0, 0, 0, 0, 0 |
| d2_trapping | 153, 98, 22, 1, 0 | 30, 107, 264, 420, 490 |
| d3_trapping | 108, 43, 8, 0, 0 | 16, 38, 89, 210, 312 |

For B backward and C unresolved runs out of n, bracket the true exit probability between the probability of backward exit by the cap and that of not exiting forward by the cap. The recorded 95% interval uses a one-sided Clopper–Pearson lower endpoint for B and upper endpoint for B+C, each with error probability .025. These are pointwise intervals, not simultaneous across widths.

At L = 64:

| Model | B/n | 95% interval including censoring |
|---|---:|---:|
| d2_moderate | .02333 | [.01631,.03230] |
| d3_moderate | .002667 | [.000727,.006814] |
| d2_trapping | 0 | [0,.99037] |
| d3_trapping | 0 | [0,.66661] |

Descriptive least-squares fits of \(-\log(B/n)\) to \(a+cL^\gamma\), on the five uncensored moderate widths, have RMS residuals:

| Model | γ = 1/2 | γ = 3/4 | γ = 1 |
|---|---:|---:|---:|
| d2_moderate | .1669 | .0772 | .0527 |
| d3_moderate | .4402 | .2778 | .1314 |

The moderate examples are compatible with exponential-looking finite-scale decay, and thus with stretched-exponential upper bounds. These fits do not estimate asymptotic γ, test a neighborhood of directions, or prove (T). The trapping cases are inconclusive at large widths: discarding censored runs would give misleading evidence. See [slab_exits.svg](data/slab_exits.svg).

### Renewal-tail observations

For a trajectory through H, define \(\widehat\tau_H\) as the first strict positive-time height record not followed by a lower height *up to H*, and use H+1 if none exists. Pathwise \(\widehat\tau_H\le\tau_1\): if τ₁ ≤ H it is a candidate, and otherwise the bound is automatic. The proxies increase with H and eventually equal τ₁ on a directionally transient path, since every earlier false record eventually gets invalidated. At a finite horizon there is no certificate that a candidate survives forever.

There are 600 trajectories per moderate model and 300 per trapping model, with common-path horizons 10,000,30,000,100,000. At H = 100,000 the empirical proxy tails are:

| Model | >100 | >1,000 | >10,000 | >30,000 |
|---|---:|---:|---:|---:|
| d2_moderate | .8583 | .6667 | .2783 | .0750 |
| d3_moderate | .8333 | .6417 | .1250 | .00333 |
| d2_trapping | .7333 | .6733 | .5567 | .5100 |
| d3_trapping | .6600 | .5233 | .3667 | .2400 |

These estimate lower bounds on the actual renewal tails. The confidence lower endpoints transfer to true-tail lower bounds; the proxy upper endpoints do not transfer to true-tail upper bounds. Horizon monotonicity was checked for every replicate. No first-renewal tail exponent is claimed. See [renewal_proxies.svg](data/renewal_proxies.svg) and the raw proxy CSV.

A separate 200,000 samples per model of isolated two-vertex traps check (11); stable evaluation uses log(1−U), log(1−V) rather than subtracting a near-one product. The results are in data/pair_trap_tail.csv. They check the local exponent, not the full regeneration tail.

### Reproduction and checks

The C++ seed is 13720261113; auxiliary Python seed 20261113137; independent quenched-check seed 13799881. The main simulation took 448,009,502 steps, one thread, nice 10, 25.84 seconds wall time, and about 29 MB peak resident memory on this Mac. Its largest environment had 59,868 vertices. Auxiliary computations also use one numerical thread and stay far below 4 GB.

Checks include Dirichlet marginal means against α/S (largest standardized discrepancy 2.32 over 20 marginals), exact path mass conservation, independent quenched-matrix comparison, isolated trap survival against (11), and the parameter-volume formulas against 200,000 uniform samples per fixed-total slice (largest discrepancy 1.68 standard errors). These audit code and algebra; the proofs do not depend on numerical checks.

Run in order: compile code/rwde_sim.cpp with clang++ -O2 -std=c++17 to code/rwde_sim; run it, then code/analyze.py, code/finite_certificate.py, code/verify.py and code/plot.py. Set OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1 and VECLIB_MAXIMUM_THREADS=1. The scripts retain an inherited nice value ≥ 10 and set nice 10 if necessary. The plots are original vector data plots, not source-page images.

code/fetch_text.py reads PDF bytes in memory and converts via pdftotext stdin/stdout. Only plain text is retained in sources/. No PDFs or paper images were saved. No subagents, publication or pushes occurred. All research files are within this directory.

## 9. Remaining gap

For omitted parameters outside established sufficient regions, no uniform seed estimate, spatial regeneration tail bound, or counterexample was obtained. Proposition A settles the necessary endpoint obstruction. Equation (13) concerns later i.i.d. intervals, not the unconditioned first interval. Proposition B is an explicit enlargement derived from existing literature. None resolves \((T')\) for all nonzero drifts. The computations do not decide it.

Task: “Open problem F0137”, received approximately 2026-11-13 09:06 Asia/Tbilisi; the prompt itself supplies no clock time.
