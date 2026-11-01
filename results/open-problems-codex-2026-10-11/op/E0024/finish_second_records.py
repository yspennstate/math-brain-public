from pathlib import Path
import json
p=Path('SECOND_ATTEMPT.md');s=p.read_text();s=s.replace('1+2sqrt(g(1-g) and','1+2sqrt(g(1-g)) and');p.write_text(s,encoding='utf8')
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8');s+='''
## Renewed attempt: sources and searches (2026-10-12)

Read Hu-Sun-Wang arXiv:1903.00050v3 again: Theorem 1.1(i), PDF p.3, transfers (H) under local path-law absolute continuity; Theorem 4.5, PDF p.14, is the exact Levy triplet test; Remark 4.6 and Corollary 4.8, PDF p.15, check drift-integral finiteness and state only (H_m) for general symmetric references, with a density condition for promotion to (H). These are neighbouring theorems, not an unrestricted product solution.

Mamoru Kanda, Notes on energy for space-time processes over Levy processes, Nagoya Mathematical Journal 122 (1991), 63-74, DOI 10.1017/S0027763000003536. Retrieved OpenAlex W1500198325 and its Cambridge PDF, saved kanda_original.pdf and kanda_original.txt. Checked resolvent-density assumptions at printed p.65/PDF p.3 and Corollary of Lemma 2.1 at printed p.66/PDF p.4. It proves positive-measure energy monotonicity in lambda and under domination. It does not provide monotonicity for complex slices.

Crossref found Shizuo Kakutani, On Equivalence of Infinite Product Measures, Annals of Mathematics 49(1) (1948), starting p.214, DOI 10.2307/1969123. This was a Hellinger-method lead; no theorem from the unfetched paper is used in the proof. The required Levy-law criterion comes directly from fetched Hu-Sun-Wang Theorem 4.5.

Brain queries: "Hunt hypothesis Kanda energy complex measures approximation resolvent"; "Hu Sun Wang local absolute continuity Hunt hypothesis symmetric Levy"; "Kakutani Hellinger equivalence product Poisson measures"; "Glover Rao subordination Hunt hypothesis". Returned relevant cards describe energy and Hellinger distance, but none proves the missing assertion; irrelevant matches were not used.

New HTTP ledger entries follow; full URLs and responses are also in search_log.json. No exact literature solution was identified. B4 is a written derivation here, not SOLVED_IN_LITERATURE and not claimed novel.
'''
for r in json.loads(Path('search_log.json').read_text()):
 if r['service_query'] in ['openalex_symmetric_H','crossref_kakutani','openalex_absolute_H','kanda_original_pdf','kanda_metadata']:
  s+=f"\n- {r['date']} -- {r['service_query']}: {r['url']} -- {r['status']}; {r.get('file','no response file')}.\n"
p.write_text(s,encoding='utf8')
claims=[
('An independent product with (H) transfers (H) under coordinatewise finite-horizon path-law absolute continuity; local equivalence preserves product (H) in both directions.','proved','SECOND_ATTEMPT.md B1-B2','Reference PRODUCT (H) must be known; reference factor (H) alone does not establish it.','Product Radon-Nikodym derivative verified on rectangles and by pi-lambda; source Theorems 1.1 and 4.5 used with all starting points and raw sigma-fields.'),
('Minimum Hellinger cost of a Levy jump measure nu to a symmetric Levy measure is J=(1/4) integral (sqrt(g)-sqrt(1-g))^2 d(nu+nu^-), attained by rho_*=(sqrt(g)+sqrt(1-g))^2 (nu+nu^-)/4.','proved','SECOND_ATTEMPT.md B4','Characterizes symmetric reference measures, not (H).','Common dominating measure proof covers singular and infinite measures; finite identity and optimum Lean-checked, exit 0, no sorryAx.'),
('A Levy process (a,Q,nu) admits a symmetric Levy reference locally dominating its finite-horizon laws exactly when J(nu)<infinity and a+integral_{|x|<1}x(nu-rho_*) belongs to Range(Q).','proved','SECOND_ATTEMPT.md B4','Bare (H) does not imply this criterion; reference product full (H) remains separate.','Absolute convergence by Hellinger Cauchy-Schwarz; symmetric correction has zero vector integral; source triplet criterion checked on PDF p.14.'),
('Asymmetric stable Levy processes with 0<alpha<1 and unequal positive/negative intensities satisfy (H) but are not locally absolutely continuous to any symmetric Levy reference.','proved','SECOND_ATTEMPT.md B3-B4','Not a counterexample to E0024; stable products satisfy (H).','Infinite lower Hellinger cost from paired intensities; extra singular mass and Gaussian/drift changes accounted for.'),
('Independent Hellinger-small and correctly compensated infinite-activity perturbations of symmetric stable reference factors have a product satisfying (H).','proved_special_case','SECOND_ATTEMPT.md B2','Only the stated perturbation class; no novelty claimed.','Explicit K_i=1+theta_i*x near zero has finite cost; reference product in Rao class; drift verified.'),
('Under A1 density hypotheses, smoothing a compact positive finite-energy measure in a symmetric partner coordinate makes product energy vanish at each fixed Gaussian scale when the other factor satisfies (H).','proved','SECOND_ATTEMPT.md A1','Removing smoothing uniformly in lambda is unproved.','Kanda original corollary checked; four dominated positive measures bound complex slices; integrable Gaussian multiplier.'),
('For each fixed measure in A1, vanishing product energy is equivalent to uniform vanishing of its Gaussian-smoothing residual energy over lambda>=1.','proved','SECOND_ATTEMPT.md A2','This per-measure uniformity is not proved from bare factor (H).','Exact multiplier bound, bounded-lambda comparison and Fourier triangle inequality.'),
('For a fixed (H) skew-Cauchy/Brownian product, no process-dependent constant bounds all higher smoothing-residual energies by residual 1-energy for all positive smooth probability inputs.','counterexample','SECOND_ATTEMPT.md A3','Counterexample to uniform inequality only, not (H) or per-measure approximation.','Positive Gaussian-modulated family; full asymptotic proof gives ratio (1/pi)log T; 40-point Gauss-Hermite checks.')]
with Path('CLAIMS.jsonl').open('a',encoding='utf8') as f:
 for claim,status,loc,gap,checks in claims:f.write(json.dumps({'problem_id':'E0024','claim':claim,'status':status,'proof_location':loc,'remaining_gap':gap,'checks':checks},ensure_ascii=False)+'\n')
print('Saved literature update and 8 new claims.')
