from pathlib import Path
P=Path(__file__).parent
s=r'''# F0085 — rigorous partial answer (2026-10-11)

## Exact target and verdict
Let Ξ be intensity-one homogeneous Poisson centres in R^d, and let 0<α<1 be a constant appetite. The target asks whether unclaimed sites percolate for all sufficiently small α and fail to percolate for all sufficiently large α<1; it asks analogous questions for claimed sites. Percolation means existence of an unbounded connected component, rather than infinitely many points in a bounded component.

VERDICT: PARTIAL. The literature already proves the two small-appetite assertions for d≥2 (FPV Theorem 1.1), and high-dimensional near-one percolation of CLOSED claimed sites (FPV Theorem 1.2). We have not proved near-one absence of unclaimed percolation in any general d≥2, or near-one closed-claimed percolation for all low dimensions. Literature search is bounded and partly rate limited; we do not assert these remain open as a universally verified fact.

This file proves topology/version identification, order consequences, d=1 boundary cases, and a rigorous obstruction to the prior attempted proof. These are elementary consequences and corrections, not claimed as novel solutions of the unresolved regimes.

## Objects and quoted inputs
Use the canonical stable allocation ψ_α of HHP Theorem 24, PDF page 24. For each ξ∈Ξ let T_α(ξ)=ψ_α^{-1}(ξ), let D_α=⋃_ξ T_α(ξ) be the RAW claimed set, U_α=ψ_α^{-1}(∞) the unclaimed set, and E_α=ψ_α^{-1}(∆). Define C_α=closure(D_α), the object FPV calls claimed.

Inputs, all verified in source.txt:
- HHP Theorems 3 and 24: canonical factor version, a.e. uniqueness, open territories and open U_α, E_α Lebesgue-null, canonicalization by essentially constant neighbourhoods.
- HHP Theorem 5: every territory is bounded a.s.; bounded sets meet finitely many territories a.s.
- HHP Theorem 4 and Proposition 20: for 0<α<1 all centres are sated, |T_α(ξ)|=α, and P(0∈U_α)=1−α. At α=1 almost every site is claimed.
- HHP Proposition 22(i), PDF page 21: for α₁≤α₂ and the same Ξ, |x−ψ_{α₁}(x)|≥|x−ψ_{α₂}(x)| for Lebesgue-a.e. x, with distance to ∞ defined as ∞. It applies first to site-optimal allocations, hence to canonical versions by a.e. agreement and uniqueness.

These inputs are established theorems, not newly proved here. All following deductions are given in full. Unless explicitly stated otherwise α is fixed; pairwise almost-sure claims are not promoted to simultaneous claims over an uncountable parameter set.

## Proposition A: the canonical unclaimed set is exactly R^d minus C_α
Proof. If x∈U_α, openness gives a ball B(x,r)⊆U_α. This ball is disjoint from D_α, so x∉closure(D_α). Thus U_α⊆R^d\C_α.
Conversely if x∉C_α, some ball B(x,r) has empty intersection with D_α. Throughout this ball ψ_α takes only the values ∞ and ∆. Since E_α is null, this ball is essentially a subset of ψ_α^{-1}(∞). The defining canonicalization therefore assigns ∞ to x. Canonicalizing a canonical allocation leaves it unchanged: for a non-∆ point its open constant neighbourhood supplies that value; if a ∆ point had an essentially constant neighbourhood the original canonical construction would already assign that value, since the original and canonical versions agree a.e. Thus x∈U_α. Both inclusions prove equality. ∎

This makes FPV Theorem 1.1(ii) applicable to canonical unclaimed sites, with an explicitly proved version-identification step. No a.e. equality of arbitrary sets is being treated as a topological equality.

## Proposition B: monotonicity and one-sided threshold reductions
Fix 0≤α₁≤α₂. Almost surely C_{α₁}⊆C_{α₂} and U_{α₂}⊆U_{α₁}.
Proof. Outside a single null exceptional set, a site claimed at α₁ has finite distance to its assigned centre. The Proposition 22 distance inequality makes its distance at α₂ finite, hence it is claimed at α₂. This proves D_{α₁}\D_{α₂} is null.
If x∈D_{α₁}, it lies in an open territory T_{α₁}(ξ). Every ball about x intersects that territory in a nonempty open set, which has strictly positive Lebesgue measure. Since D_{α₁}\D_{α₂} is null, every such ball intersects D_{α₂}. Therefore x∈C_{α₂}. Taking closure and using closedness of C_{α₂} proves C_{α₁}⊆C_{α₂}. Taking complements and invoking Proposition A proves U_{α₂}⊆U_{α₁}. ∎

Any unbounded connected subset of a subset A of B remains an unbounded connected subset of B. It lies in a connected component of B, which is therefore unbounded. Consequently vacant percolation at α₂ implies vacant percolation at α₁, while claimed-closure percolation at α₁ implies claimed-closure percolation at α₂. These implications hold also for probabilities under the common-centre coupling. The set of α for which vacant percolation has positive probability is downward closed; the analogous claimed set is upward closed. FPV gives a nonempty small interval in the former and a nonempty small interval of nonpercolation in the latter. It remains to prove that the vacant percolation interval has supremum strictly less than one. Monotonicity by itself supplies no such strictness.

## Proposition C: raw canonical claimed sites never percolate
For every fixed finite α in any d≥1 under the HHP geometry hypotheses, every connected component of D_α is bounded a.s.
Proof. Work on the probability-one event on which all territories are open and bounded. Let K⊆D_α be nonempty and connected; choose x∈K and its centre ξ. The subsets K∩T_α(ξ) and K∩⋃_{ζ≠ξ}T_α(ζ) are disjoint, relatively open in K, and together cover K. The first is nonempty. If the second were nonempty these two sets would separate K, contradicting connectedness. Thus K⊆T_α(ξ), a bounded set. Apply this to every component. ∎

The closed union C_α can percolate because it includes interfaces between territories. The original source's a.e. allocation language is not enough to define percolation independently of null-set choices. Proposition C is about the raw canonical version ONLY and is not a refutation of FPV, whose definition explicitly takes closure. The unresolved claimed regime in this report uses C_α.

## Proposition D: one dimension and endpoints
For d=1 and each fixed 0<α<1, both C_α and U_α have only bounded connected components a.s. At α=0, C_0=∅ and U_0=R^d. At α=1, C_1=R^d and canonical U_1=∅ (all d).
Proof in d=1. Define Y_n=Leb(U_α∩[n,n+1)). Translation equivariance makes (Y_n) stationary. Unit translation on a one-dimensional Poisson process is ergodic: its restrictions to half-open unit intervals, translated into [0,1), are independent identically distributed random point configurations, and unit translation is the bilateral iid shift. The allocation is a measurable factor of this shift and therefore ergodic as well. The usual pointwise ergodic theorem applies to bounded variables 0≤Y_n≤1. Fubini and stationarity give E Y_0=∫_0^1 P(x∈U_α)dx=1−α.
Applying the ergodic theorem to the forward and inverse shifts yields, almost surely,
lim_{N→∞} Leb(U_α∩[0,N))/N=1−α,
lim_{N→∞} Leb(U_α∩[−N,0))/N=1−α.
By Proposition A the complementary C_α averages are α>0. Consequently neither U_α nor C_α can contain a half-line: a U_α half-line would force the corresponding C_α average to zero, and a C_α half-line would force the corresponding U_α average to zero.
Every connected subset of R is an interval. Indeed if a<b lie in a connected set and a<t<b does not, its intersections with (−∞,t) and (t,∞) give a separation. An unbounded interval contains a half-line in at least one direction. Thus neither set can have an unbounded connected component.
At α=0 every territory has measure zero. Canonical territories are open, so are empty. The canonical rule assigns every point to ∞; C_0=∅. At α=1 the phase theorem says D_1 has full measure, hence it is dense (every nonempty ball has positive measure). Thus C_1=R^d, and Proposition A gives U_1=∅. ∎

The d=1 conclusion is outside FPV's d≥2 question, so it is recorded only as a boundary special case. The α=1 conclusion does not imply disappearance of vacant percolation strictly below one: nested percolating sets may have empty intersection.

## Proposition E: no deterministic common bound on territory radii
Fix d≥1, 0<α<1, and r_α=(α/v_d)^{1/d}, where v_d is unit-ball volume. Put R_ξ=ess sup{|x−ξ|:x∈T_α(ξ)}. Almost surely sup_{ξ∈Ξ} R_ξ/r_α=∞.
Proof. Fix any positive integer M and choose an integer k>(M+1)^d. Select infinitely many deterministic pairwise disjoint balls B(z_n,r_α), e.g. along one axis with centre spacing 3r_α. Their centre counts are independent Poisson variables with mean α. The event A_n that a ball contains at least k centres has a common probability p>0. The probability that none of the first N balls has A_n is (1−p)^N, tending to zero. Thus almost surely at least one such ball contains k centres.
On the probability-one event that all centres are sated, choose k of those centres ξ₁,…,ξ_k. Suppose every R_{ξ_i}≤M r_α. Outside a null set each corresponding territory lies inside B(ξ_i,M r_α), hence inside the ball with centre z_n and radius (M+1)r_α, allowing closed balls without changing their volume. The k territories are disjoint and each has volume α. Their union therefore has volume kα. But the containing ball has volume v_d((M+1)r_α)^d=(M+1)^d α<kα, a contradiction. At least one radius exceeds M r_α. Intersecting these probability-one events over all positive integers M proves the asserted infinite supremum. ∎

Every individual territory is still bounded a.s.; the supremum across all centres need not be bounded. The proof disproves deterministic-radius domination centred at the same Poisson centres. It does not disprove the dependent random-radius domination in Gouéré or FPV. It also does not supply the prior attempt's missing estimates for exceptional clusters.

## Referee audit and exact checks
1. Null sets versus topology: Proposition A explicitly uses canonicalization. Proposition B uses openness and positive measure of balls, not an invalid passage from arbitrary a.e. inclusion to closure inclusion. Proposition C keeps raw and closed claimed objects separate.
2. Appetite monotonicity: HHP Proposition 22 read directly, with its distance convention; FPV also states C inclusion on PDF page 4. The earlier ledger's claimed failure is false.
3. Positive density is insufficient for percolation in d≥2. Only the order-and-interval property of R is used in Proposition D. No density heuristic proves an unresolved assertion.
4. Endpoints versus a strict near-one interval: Proposition D supplies the endpoint only; no continuity of percolation is assumed.
5. All-centres sated and volume disjointness: verified HHP phase theorem is essential to Proposition E. The positive-probability Poisson cluster argument and countable intersection justify its a.s. statement; no deterministic bound is assumed.
6. Lean scope: Capacity.lean formalizes exactly the real finite-capacity inequality used in Proposition E and complement inclusion used in Proposition B. It does NOT formalize stable allocation existence, ergodic theory, topology, or the full percolation problem. No sorry, axiom declarations, native_decide or umbrella Mathlib import. See lean_check.txt for actual compiler result.
7. No simulation is used as proof. The packing contradiction is exact for every dimension, appetite and integer k satisfying the displayed strict inequality. Finite arithmetic checks in capacity_checks.json are only sanity checks.

## Remaining gap and concrete next directions
For each d≥2, prove or disprove existence of β_d<1 such that U_α has no unbounded connected component a.s. for every β_d<α<1. The paper's small-appetite theorem and α=1 endpoint leave this strict inequality unresolved here. Prove or disprove α_p(d)<1 for the CLOSED claimed set in the low dimensions not covered by FPV's asymptotic theorem. No claim is made about either regime's critical equality.
A route requiring new work is a near-critical finite-box vacant-crossing estimate strong enough, with verified dependence control, to iterate across scales. Vanishing vacant volume 1−α alone does not bound a crossing probability, and the existing individual-territory radius bounds are not enough. No such estimate has been obtained in this attempt.
'''
(P/'ATTEMPT.md').write_text(s,encoding='utf8')
import json
claims=[
('FPV Theorem 1.1 proves both small-appetite percolation assertions for canonical unclaimed and closed claimed sets in each d>=2.','proved_special_case','LITERATURE.md; ATTEMPT.md Proposition A','Near-one vacant and low-dimensional near-one closed-claimed regimes remain unresolved here.','Read full theorem, definitions and proof ending, arXiv PDF pages 3,4,15.'),
('Canonical U_alpha equals R^d minus the closure of canonical raw claimed sites.','proved','ATTEMPT.md Proposition A','','Canonicalization rule checked in HHP Theorem 24.'),
('For each fixed appetite pair alpha1<=alpha2, closed claimed sets increase and canonical unclaimed sets decrease a.s.','proved','ATTEMPT.md Proposition B','','HHP Proposition 22; openness argument; Lean complement-order lemma.'),
('Every component of the raw canonical claimed union is bounded in every dimension for fixed finite appetite.','proved_special_case','ATTEMPT.md Proposition C','Does not apply to closure C_alpha.','Connected-set separation checked using disjoint open bounded territories.'),
('In d=1 and 0<alpha<1 neither closed claimed nor canonical unclaimed sites percolate.','proved_special_case','ATTEMPT.md Proposition D','Does not resolve the d>=2 target.','Bilateral Poisson iid shift, ergodic averages, interval separation proof.'),
('At alpha=0 U is all space; at alpha=1 closed claimed C is all space and canonical U is empty.','proved_special_case','ATTEMPT.md Proposition D','The alpha=1 endpoint does not prove a strict subcritical threshold.','Phase theorem, positivity of ball volume, canonicalization.'),
('For fixed 0<alpha<1 the supremum of territory essential radii divided by r_alpha is infinite a.s.; uniform deterministic centred-ball containment is false.','counterexample','ATTEMPT.md Proposition E','','Independent Poisson cluster events, saturation, exact volume packing; finite inequality in Capacity.lean.')]
with (P/'CLAIMS.jsonl').open('w',encoding='utf8') as f:
 for c,st,loc,g,ch in claims:f.write(json.dumps(dict(problem_id='F0085',claim=c,status=st,proof_location=loc,remaining_gap=g,checks=ch),ensure_ascii=False)+'\n')
checks=[]
for d in range(1,11):
 M=2; cap=(M+1)**d;k=cap+1
 checks.append(dict(d=d,M=M,capacity=cap,k=k,strictly_over_capacity=k>cap))
(P/'capacity_checks.json').write_text(json.dumps(checks,indent=2),encoding='utf8')
print('Saved complete partial proofs, claims, and exact arithmetic sanity checks.')
