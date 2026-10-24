# K-theory / group-ring attack log — 2 October 2026

Status: no complete solution of a famous open problem obtained. This log records active mathematical attacks and verified boundaries; no novelty is asserted for reductions.

## 1. Current sources materially change the candidate landscape

* Wolfgang Lück, Survey on the Farrell–Jones Conjecture, arXiv:2507.11337 (2025), §11. The full conjecture remains open for Out(F_n), n≥3, Thompson F,V,T, general linear groups, torsionfree one-relator groups, and general amenable groups.
  https://arxiv.org/html/2507.11337v1
* Andrew–Guerch–Hughes, Automorphisms of relatively hyperbolic groups and the Farrell–Jones conjecture, Mathematische Annalen (published 16 June 2026), expressly calls Out(F_n) a major remaining open problem.
  https://link.springer.com/article/10.1007/s00208-026-03431-7
* Kun–Thom, Nonsofic wreath products of residually finite groups, arXiv:2608.06222v3 (20 August 2026), establishes concrete nonsofic generalized wreath products and doubles. Hence using “all known groups are sofic” in October 2026 would be incorrect.
  https://arxiv.org/html/2608.06222v3
* Fournier-Facio, A torsion-free non-sofic group, arXiv:2608.02025v2 (14 August 2026), provides finitely presented torsionfree nonsofic examples.
  https://arxiv.org/pdf/2608.02025
* Liu, Kaplansky’s direct finiteness conjecture for the first non-sofic group: unit sums, a stratification, and complete bounded searches, Zenodo 21840947 (August 2026). No direct-finiteness counterexample found. This is a preprint, not a peer-reviewed claim. The PDF was retrieved and read locally.
  https://zenodo.org/records/21840947

## 2. Direct finiteness on the concrete Leavitt unit group

Take R=L_{F_2}(1,2)=F_2<s_0,s_1,t_0,t_1 | t_i s_j=delta_ij, s_0t_0+s_1t_1=1> and G=R^×. The evaluated ring R is not directly finite: t_0s_0=1 while s_0t_0 !=1. G is nonsofic by the August 2026 construction. The famous unresolved question is whether F_2[G] itself is directly finite.

The evaluation map ev:F_2[G]→R is onto because every element of R is a sum of units. Crucial obstacle: ev is far from injective, so the displayed one-sided inverse in R does NOT lift to a one-sided inverse in F_2[G]. Even F_2[free group] surjects onto R.

A direct search must work with formal sums of distinct group elements, not merely sums as elements of R. If a,b satisfy ab=1, augmentations imply |supp(a)| and |supp(b)| odd. Supports of size one are trivial, so both must have size at least three. Existing universal ULIE classifications already rule out rank pairs (3,n), n≤11, and (5,5) over F_2; re-running these would not advance the famous problem.

I investigated whether a ring-theoretic additive section might lift the Leavitt relations. No additive multiplicative section has been constructed; such a section would embed a non-directly-finite ring into a group algebra and immediately settle the conjecture negatively. Unit-sum surjectivity is insufficient, and the formal identity defect is the precise gap.

## 3. A p-adic completion attack and its exact obstruction

For any hypothetical counterexample a,b∈F_p[G], choose finite integer lifts A,B∈Z_p[G] with AB≡1 (mod p). Put E=1−AB∈pZ_p[G]. In the p-adic completion A_G=c_0(G,Z_p), the convergent series V=B sum_{n≥0}E^n satisfies A V=1. Its reverse product reduces to ba, so VA≠1. Thus any positive-characteristic counterexample gives a proper one-sided inverse in this completed algebra with a finite-supported left factor.

This is rigorous, but not a solution: proving direct finiteness of these nonarchimedean group Banach algebras would imply the conjecture. Complex group von Neumann positivity is unavailable. Their coefficient-at-identity trace is cyclic, but trace zero does not presently force an idempotent to vanish. A characteristic-zero dense subalgebra being directly finite does not suffice to show its p-adic completion is directly finite. An attempted lift to complex coefficients fails because p-adically decaying rational coefficients p^n grow in every complex embedding.

## 4. The support-three zero-divisor case over F_2

Sharp classical target: for every torsionfree G and distinct x,y, does (1+x+y)β=0 force β=0? This is the smallest unresolved support case and would be a substantial special case of Kaplansky’s zero-divisor conjecture.

Primary sources:
* Abdollahi–Taheri, arXiv:1612.00934 (2016), prove partner support at least20 overF_2; their abstract states the general support-three case remains under investigation.
  https://arxiv.org/abs/1612.00934
* Bondarenko–Juschenko, The zero divisor conjecture and Mealy automata, arXiv:2402.08625 (2024), prove the invertible-pairing subclass. They do not establish the noninvertible-pairing case.
  https://arxiv.org/abs/2402.08625

Useful exact combinatorial reduction: if β=∑_{b∈B}b and (1+x+y)β=0, then each product in {1,x,y}B appears exactly twice (multiplicity is at most3 and must be even). Hence |B| is even and the 3|B| products pair into a cubic cancellation graph on B. A cancellation a b=a' b' gives b'=a'^{-1}a b, with labels from x±1,y±1,x^{-1}y,y^{-1}x. Every support point has three incident products. The graph’s group labels must satisfy every cycle relation while keeping support points distinct and the ambient group torsionfree.

The hoped-for attack is a universal finite-parity-code obstruction: prove such a finite cubic labelled cancellation graph necessarily forces a torsion relation. However, existing nonunique-product torsionfree groups show that mere finite product cancellation is not enough, and the already-solved invertible pairing case cannot be generalized without controlling noninjective automaton transitions. No universal contradiction has yet been derived.

## 5. A useful but likely standard assembly observation

If H=G *_Γ G, the folding map H→G restricts injectively to both vertex groups. For every virtually cyclic C<G, its inverse image acts on the Bass–Serre tree with virtually cyclic vertex stabilizers. In the torsionfree case they are cyclic, making that inverse image the fundamental group of a graph of cyclic groups, covered by the known graph-of-abelian-groups Farrell–Jones theorem. Thus if G satisfies the relevant coefficient Farrell–Jones conjecture, the usual fibered inheritance criterion can often prove it for the double.

This is not a new theorem claim. It suggests checking FJ on newly constructed nonsofic doubles, but the explicit Kun–Thom ambient groups involve several-variable polynomial/Laurent rings and their FJ status itself is not supplied by the cited paper. Replacing this gap by the blanket assertion “all linear groups satisfy FJ” would be false as a status statement.

## 6. Audit standard trap

For p²=p∈C[G], let q be the orthogonal projection onto its range in C*_r(G). The formula q=pp*[1−(p−p*)²]^{-1} places q in C*_r(G), with qp=p and pq=q. Cyclicity gives τ(p)=τ(q). Faithfulness then gives 0≤τ(p)≤1 and τ(p)∈{0,1} iff p∈{0,1}. Hence trace integrality would prove the complex idempotent conjecture. This is a standard reduction, not a proof: the missing general integrality theorem is itself conjectural, and probabilities/return moments do not currently supply it.
