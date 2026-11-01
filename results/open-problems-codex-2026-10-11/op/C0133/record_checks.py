from pathlib import Path
import json
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8');s=s.replace('Bulletin of the Brazilian Mathematical Society, New Series **52** (2021), 1194–1201','São Paulo Journal of Mathematical Sciences **16** (2022), 1194–1201 (online 22 February 2021)');s=s.replace('Crossref gives inconsistent volume metadata (16); the DOI/preprint identify the item. No conclusion relies on that volume field.','The publication title and volume/year were checked against Crossref: container-title São Paulo Journal of Mathematical Sciences, volume 16, printed December 2022.');s+='\nThe later Project Euclid published-PDF request returned a one-page PDF containing only “Request unsuccessful. Incapsula incident ID”. Although the container parses as a PDF, it is a bot-challenge response, not the article. All theorem quotations in this audit use the verified arXiv copy.\n';p.write_text(s,encoding='utf8')
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8');s+='''

## 8. Exact checks and short counterexample probes
The reproducible script experiments.py uses fractions.Fraction throughout its finite-interval linear systems. For L in {2,3,5,10,20,40}, exact Gaussian elimination of 2u_i−u_{i−1}−u_{i+1}=0 with boundary values 0 and 1 returned u_i=i/L at every site. It also enumerated all 2^12=4096 twelve-step paths, assigning deterministic signed projected drifts b(x,i)=(((x+i) mod 3)−1)/2 for i≤3 and zero for i>3. For every path it verified the time-sum/site-sum identity and |D_12|≤(3/2)#R_12. These computations check finite identities; the written proofs cover arbitrary lengths.

Small counterexample probes used 12 independent Python random.Random seeds, 133000 through 133011, for each of three deterministic homogeneous one-dimensional stack laws (degenerate IID, uniformly elliptic): fair p_i=1/2; periodic p_i=0.8 for odd i and 0.2 for even i; and alternating blocks of lengths 1,4,16,64,… with p_i=0.8,0.2,0.8,0.2,… . Each path ran 100,000 steps. The endpoint X_n/n ranges were respectively [−0.00398,0.00464], [−0.00374,0.01146], and [−0.0263,0.10862]; return-to-zero counts ranged over [63,608], [18,576], and [6,36]. All raw summaries are in experiment_results.json. The code stores only local-time dictionaries and summaries (well below 1 GB), and the actual computation completed in about 6.5 seconds.

No finite sample determines whether |X_n|→∞ or whether an apparent velocity persists. In fact Section 7 already rules out a genuine one-dimensional counterexample under these laws. The growing-block stack is an example of misleading finite-horizon behavior, not numerical evidence against the theorem. The earlier failed exact check was caused by assigning integer matrix entries and then using Python '/' before all entries were Fraction objects; that introduced floating-point entries. The saved script corrects this, and the successful output above uses exact rational coefficients throughout.

## 9. Hostile-referee checklist
- Whole-stack IID versus within-stack independence: only spatial IID is assumed; no step of the reductions requires independence of cookie indices.
- EL versus UEL: no uniform positive lower bound is invoked in Sections 1–5 or 7.
- Returning event: only infinitely many visits to SOME bounded set is used; all-site recurrence is never inferred.
- Martingale filtration: the entire environment is included, so the conditional drift equals the consumed-cookie drift even after the annealed walk has learned environmental information.
- Random times in the adaptive obstruction: starts are stopping times; fresh uniforms justify conditional concentration. Time budgets and failure probabilities are summable since N_k≥k².
- Optional stopping: only bounded stopped positions and almost-sure finite interval absorption are used; no unrestricted integrability assumption on the return time is made.
- Range/budget reduction: it is explicitly conditional, and no unjustified IID law of large numbers over adaptively selected sites is used.
- Literature scope: the d=1 theorem is quoted and mapped; higher-dimensional restricted-coordinate LLNs and the Santos example do not cover the general question.
- Numeric scope: exact finite checks verify algebra; finite simulations do not identify recurrence or asymptotic velocity.
- Formal scope: FiniteChecks.lean checks only the finite harmonic uniqueness and return-gap algebra; it does not formalize the stochastic arguments or solve C0133.

## Final remaining gap
For arbitrary IID elliptic cookie stacks in d≥2 with both positive and negative projected drifts, show that the consumed-cookie sum D_n is o(n) on the event of infinitely many returns to some finite ball, or produce an actual cookie environment violating that conclusion. Neither a sufficiently strong returning-excursion bound nor an applicable regeneration argument has been established. The balanced-cookie case and the complete d=1 case are resolved; the general question is not.
''';p.write_text(s,encoding='utf8')
rows=[json.loads(l) for l in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for r in rows:
 r['checks']=['Full written proof and hostile-referee checklist in ATTEMPT.md; literature inputs explicitly identified.']
 if 'tail 1/(2L)' in r['claim']:r['checks'].append('Exact Fraction Gaussian elimination at L=2,3,5,10,20,40 passed.')
 if 'budget' in r['claim']:r['checks'].append('Exhaustive 4096-path exact drift-grouping and absolute-budget check passed.')
rows.append({'problem_id':'C0133','claim':'Exact rational harmonic profiles and drift-budget grouping checks passed at the finite sizes listed in experiment_results.json.','status':'numerical_evidence','proof_location':'experiments.py; experiment_results.json; ATTEMPT.md Section 8','remaining_gap':'Finite computations do not establish the general stochastic assertion.','checks':['Fraction arithmetic; all 4096 twelve-step paths; exact absorption profiles up to L=40.']})
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf8')
print('saved computation record and referee checklist')
