from pathlib import Path
import json
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf-8-sig')
s=s.replace('No proof of theta(pc,Z^d)=0 for all d>=3 was found or constructed.', 'No independent proof of theta(pc,Z^d)=0 for all d>=3 was constructed. A public formal proof CLAIM was subsequently located; see section 7. Its existence changes the source-status leads but its full certificate has not been replayed in this workspace.')
s+='''

## 7. Later-discovered public critical-site proof claim (important status caveat)

The read-only historical repository report research7_2026-09-17/R7-06/screens/2026-09-18T200200Z__G0001_external_formal_resolution_reconciliation.md pointed to Ahmed Bou-Rabee's public page https://nitromannitol.github.io/site-percolation-7d3f2/ and https://github.com/nitromannitol/percolation-after-anthropic. Both were fetched successfully on 2026-10-11, along with the final declaration, verification note, independent statement comparator, and 28-page accompanying manuscript.

The current public final declaration is:

```lean
theorem site_no_percolation_at_critical (d : ℕ) (hd : 3 ≤ d) :
    thetaSite d (criticalProbSiteI d) = 0 := by
  haveI : NeZero d := ⟨by omega⟩
  exact ExactCommonQAssembly.site_no_percolation_at_criticality hd
```

It is SITE-specific, and discharges the displayed NeZero instance internally. The comparator reconstructs the model using Set(Fin d -> integers), product independent Bernoulli measures, the Hasse graph of the coordinatewise product order (the undirected nearest-neighbour lattice), and clusters of the open origin. The critical parameter is the infimum of the positive-percolation parameters in [0,1], with {1} added. Those definitions match the intended model at statement level. The comparator challenge deliberately has a `sorry`, while the separate solution imports the claimed final theorem and applies it; the challenge is NOT a locally checked proof and is not included among checked claims here.

The project README says the development is unconditional, has no custom axioms, and its final declarations depend only on propext, Classical.choice and Quot.sound. It pins Lean 4.32.0, Mathlib and the Anthropic bond-percolation dependency. Its approximately 100,800 lines/226 modules plus 247 dependency modules have not been rebuilt or individually proof-audited here. Downloading final declarations and authors' verification reports does not by itself verify all these dependencies. Our local Lean 4.33.1 algebra check is separate and cannot validate the external theorem. Public CI metadata is retained as supporting evidence, not represented as a local kernel replay.

The 28-page docs/kn-results.pdf concerns the finite Kozma–Nitzan inequalities; it does not state the exact G0001 finite-tail theorem. The public headline theorem is critical extinction, not the same quantified tail statement. Consequently the user-defined SOLVED_IN_LITERATURE criterion is not met by that source.

Conditional consequence, fully proved: **if** this public critical-site theorem is accepted as a valid theorem, then G0001 follows immediately and the limit is exactly (d-1)/d at every p with theta(p)>0. Indeed the critical-site theorem makes the antecedent false at pc; by monotonicity it is false below pc as well; therefore any percolating p is strictly greater than pc, and source equation (1.5) gives the limit. This is the converse direction of section 1. No bond/site transfer is needed in this implication.

This is a substantial resolution lead. This audit's PARTIAL verdict does not assert that the problem remains open in current literature; it means no unconditional full proof was independently accepted by this audit. The remaining mathematical endpoint and the remaining certification task must be distinguished: independently proving critical site extinction is one route; validating the external certificate would supply that endpoint as an external theorem and resolve the conditional consequence. We do not promote the historical report's KNOWN_EXTERNAL_FORMAL label to a verified verdict.

## 8. Check of an earlier shape reduction and a failed comparison route

The earlier report research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T191000Z__G0001_boundary_score_local_uniqueness_reduction.md contains a useful exact reduction that we independently checked, rather than assuming truncated finite-cluster tails are monotone in p.

Let partial K be the FULL exterior vertex boundary of a finite connected K (including boundaries of holes). For 0<p<r<1 define

s_*(p,r)=log(r/p)/log((1-p)/(1-r)).

If 0<=s<s_*(p,r), let kappa=log(r/p)-s log((1-p)/(1-r))>0. Then

P_p(n<=|C(0)|<infinity, |partial C(0)|<=s|C(0)|)<=exp(-kappa n).

Complete proof: The exact-cluster event C(0)=K fixes all k=|K| sites of K open and all b=|partial K| boundary sites closed; it leaves every other site free. Its probability is p^k(1-p)^b. Dividing by the corresponding probability at r gives exp[-k log(r/p)+b log((1-p)/(1-r))]. For b<=sk this is at most exp(-kappa k)<=exp(-kappa n). Sum this inequality over the countably many eligible finite connected K containing 0. The corresponding exact-cluster events at r are pairwise disjoint, so their total probability is at most one. This proves the bound without any monotonicity or critical hypothesis. Differentiating numerator and denominator at r=p (both vanish with positive denominator derivative) yields lim_{r downarrow p}s_*(p,r)=(1-p)/p. Thus every fixed s<(1-p)/p admits such a comparison parameter r.

If theta(pc)>0, Theorem 1.2 says L(pc)=0. For every s<(1-pc)/pc, the high-full-boundary part of the tail must also have logarithmic liminf zero. To check this conclusion carefully: the low-boundary part is exponentially small by the previous bound. If the high-boundary part had positive logarithmic liminf, both parts would be eventually bounded by a stretched exponential with a common positive exponent, and their sum would too (absorb the factor two by decreasing the exponent). That contradicts L(pc)=0. The high-boundary tail tends to zero; hence its logarithmic liminf is at least zero, so its failure to be positive means it is zero. Its positivity along the relevant subsequence follows from the same comparison with the strictly positive total tail.

This explains a failed route: directly comparing F_p(n) with F_r(n) cannot work by monotonicity. Even the singleton probability p(1-p)^(2d) rises and then falls, with derivative (1-p)^(2d-1)[1-(2d+1)p]. The event {n<=|C(0)|<infinity} is not increasing. The exact probability ratio controls compact/low-boundary clusters but leaves highly exposed clusters; it does not supply the missing critical upper bound. This verified reduction is prior work, not a new endpoint proof.
'''
p.write_text(s,encoding='utf8')
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8')
s+='''

## Later primary-source status lead: critical SITE extinction

The historical reconciliation report at origin/master:research7_2026-09-17/R7-06/screens/2026-09-18T200200Z__G0001_external_formal_resolution_reconciliation.md claims a public September 5 resolution. We fetched the cited homepage, companion page, repository metadata, README, Hypergraph/FinalCriticality.lean, VERIFICATION.md, recursive source tree, comparator challenge/solution, workflow metadata, and docs/kn-results.pdf/tex. Files and complete requests are saved locally.

Ahmed Bou-Rabee, *Percolation after Anthropic*, public formal Lean development, https://github.com/nitromannitol/percolation-after-anthropic ; companion page https://nitromannitol.github.io/site-percolation-7d3f2/ . The formal declaration KNAll.Site.site_no_percolation_at_critical states thetaSite d (criticalProbSiteI d)=0 for d>=3 with only d and the numerical lower-bound binder. It applies its ExactCommonQAssembly theorem. The independent comparator's product site measure, graph and cluster definitions were inspected and match the intended model at statement level. Authors' verification claims are retained, but the full dependency chain has not been independently rebuilt here.

This is a SITE resolution claim, so it must not be discarded as a bond-only result. It would imply G0001 by the complete argument in ATTEMPT.md sections 1 and 7 if verified. It does not satisfy this task's strict SOLVED_IN_LITERATURE rule: the numbered theorem with the full finite-tail implication has not been found. The downloaded 28-page finite-inequality manuscript does not state that theorem. Accordingly record it as a substantive lead with certification pending, and do not assert current openness from the older intake label.

Also read and rechecked the earlier boundary-score/local-uniqueness artifact at origin/master:research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T191000Z__G0001_boundary_score_local_uniqueness_reduction.md. Its exact parameter comparison is proved in ATTEMPT.md section 8; it leaves the high-boundary sector.

Full HTML of Tran–Nguyen confirms Theorem 1.1 is convergence of critical SITE parameters under local graph convergence. Diskin et al.'s proof explicitly selects q in (pc,p) and further smaller supercritical parameters; that mechanism cannot be applied at pc from theta(pc)>0 alone. Neither source gives the complete target statement.

Additional query log entries (including all later fetches):

'''
# Original followup_log starts with third round; including duplicates is explicit and harmless.
if Path('followup_log.jsonl').exists():
 for line in Path('followup_log.jsonl').read_text().splitlines():s+='- '+line+'\n'
p.write_text(s,encoding='utf8')
p=Path('CLAIMS.jsonl');claims=[json.loads(line) for line in p.read_text().splitlines()]
claims.append({'problem_id':'G0001','claim':'For 0<p<r<1, finite clusters with full boundary/volume ratio at most s<log(r/p)/log((1-p)/(1-r)) have an exponential-in-volume tail.','status':'proved','proof_location':'ATTEMPT.md section 8','remaining_gap':'High-boundary clusters remain; this is checked earlier work, not critical extinction.','checks':'Exact cluster probability ratio and disjoint-event summation; threshold limit by differentiation.'})
claims.append({'problem_id':'G0001','claim':'Accepting the public critical-site-extinction theorem in KNAll.Site.site_no_percolation_at_critical, together with Cerf equation (1.5), implies G0001 and the exact exponent (d-1)/d.','status':'proved','proof_location':'ATTEMPT.md sections 1 and 7 (conditional consequence)','remaining_gap':'The external theorem is a primary-source proof claim whose full certificate was not independently replayed here; this claim is only the implication.','checks':'Final theorem binders and comparator model definitions inspected; no bond/site transfer used; full local certification not claimed.'})
p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in claims),encoding='utf8')
print('Updated source caveat, checked prior reduction, and conditional claim.')
