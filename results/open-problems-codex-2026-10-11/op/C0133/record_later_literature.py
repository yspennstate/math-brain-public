from pathlib import Path
import json
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8')
s+='''

## Verified d=1 special-case theorem (not a full solution of C0133)
Gideon Amir, Noam Berger and Tal Orenshtein, *Zero–one law for directional transience of one dimensional excited random walks*, Annales de l’Institut Henri Poincaré, Probabilités et Statistiques **52**(1) (2016), 47–57, DOI: 10.1214/14-AIHP615; arXiv:1304.7287v2. The arXiv PDF is paper_zeroone.pdf, text paper_zeroone.txt.

Theorem 1.3, arXiv PDF p. 3, verbatim (mathematical layout linearized):
> Theorem 1.3. Let µ be a stationary ergodic (with respect to the Z-shift θ) and elliptic probability measure on the space Ω of cookie environments. Then P_0(lim_{n→∞} X_n/n = v) = 1 for some deterministic v ∈ [−1, 1].

Application, line by line:
1. IID whole stacks on Z give a stationary ergodic law for the Z-shift.
2. The source's (EL) in d=1 is exactly µ((0,1)^{Z×N})=1 (use countability to combine the individual almost-sure conditions).
3. Hence Theorem 1.3 gives X_n/n→v almost surely, with no bounded-stack or uniform-ellipticity requirement.
4. On {|X_n|→∞}^c there is a finite R and a sequence n_k→∞ with |X_{n_k}|≤R. Therefore v=lim X_{n_k}/n_k=0 on this event.
5. A direction ℓ∈R\\{0} is a scalar; multiplying by it yields X_n·ℓ/n→0 on that event.

This covers d=1 under exactly the relevant hypotheses. It does not cover d≥2, so the overall verdict remains PARTIAL and not SOLVED_IN_LITERATURE. The LLN implication in line 4 is an explicit argument here, not a claim that the article states the whole Problem 4.7.

## Other inspected leads
- Gideon Amir and Tal Orenshtein, *Excited Mob*, Stochastic Processes and their Applications (2016), DOI 10.1016/j.spa.2015.09.007; arXiv:1307.6052v2. Downloaded/read introductory results and Section 4. Theorem 4.3, PDF p. 15, states a one-dimensional LLN under (SE). We use the elliptic theorem of Amir–Berger–Orenshtein instead, whose hypotheses match directly and avoid relying on typographical issues in the earlier preprint.
- Cong-Dan Pham, *Monotonicity and regularity of the speed for excited random walks in higher dimensions*, Electronic Journal of Probability **20** (2015), DOI 10.1214/EJP.v20-3522; arXiv:1311.6158v3. Downloaded/read model description and Theorem 1.1, PDF pp. 1–4. Only excitation in coordinate e_1, with all transverse transition probabilities fixed at 1/(2d), and LLN for d≥6. This is a restricted model and does not cover arbitrary cookies in Problem 4.7. The transverse component is itself a lazy simple walk and in these dimensions is transient, so the relevant returning event is null.
- Rafael Santos, *An excited random walk counter-example*, Bulletin of the Brazilian Mathematical Society, New Series **52** (2021), 1194–1201, DOI 10.1007/s40863-021-00214-7; arXiv:1909.03159v1 (preprint title *An important excited random walk counter-example*). Downloaded and read. Constructs a stationary/ergodic environment with zero speed and infinite mean cookie count. It is not a nonzero-speed returning counterexample, and its correlated renewal environment is not IID across sites. Crossref gives inconsistent volume metadata (16); the DOI/preprint identify the item. No conclusion relies on that volume field.
'''
# Add exact metadata references for relevant citation leads, transparently metadata-only.
seen={};
for fn in ['openalex_citing_published.json','openalex_citing_arxiv.json']:
 d=json.loads(Path(fn).read_text());s+='\nOpenAlex '+fn+': indexed total '+str(d['meta']['count'])+'; returned '+str(len(d['results']))+' (all fit in one page).\n'
 for r in d['results']:seen[r['id']]=r
s+='\n### Citation leads reviewed at metadata/abstract level only\n'
for r in seen.values():
 if any(t in r['title'].lower() for t in ['markovian','periodic','excursion','local memory','horizontal','balanced']):
  authors=', '.join(a['author']['display_name'] for a in r['authorships']);bib=r.get('biblio',{});journal=(r.get('primary_location') or {}).get('source') or {}
  s+='- '+authors+', *'+r['title']+'*, '+str(r['publication_year'])+', '+str(journal.get('display_name',''))+', '+json.dumps(bib)+', '+str(r.get('doi'))+'. Model-specific result; no exact-hypothesis solution verified.\n'
for f in ['search_log_4.json','search_log_5.json']:
 if Path(f).exists():
  d=json.loads(Path(f).read_text());s+='\nAdditional request '+f+': `'+json.dumps(d,ensure_ascii=False)+'`\n'
s+='\nAdditional read-only math-store recall during the proof attempt: “martingale bounded increments Azuma strong law”. Its scalar Azuma card was checked by the direct moment-generating-function proof in ATTEMPT.md; no brain/store writes occurred.\n'
p.write_text(s,encoding='utf8')
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8')
s+='''

## 7. Full d=1 case via a verified later theorem (proved special case)
Use Amir–Berger–Orenshtein Theorem 1.3, whose exact statement and source are in LITERATURE.md. IID stacks are stationary and ergodic under the Z-shift. For completeness, ergodicity follows by approximating any invariant event A in probability by an event C depending on finitely many site stacks: for large shifts h, C and θ_h C are independent. Since θ_h A=A modulo null sets, |P(A)−P(C)^2|≤2P(A△C), and |P(A)^2−P(C)^2|≤2P(A△C). Let the approximation error go to zero to get P(A)=P(A)^2. Finite-cylinder events approximate product-measurable events by the usual monotone-class argument. Stationarity follows directly from identical independent coordinates.

Source (EL) is precisely ellipticity in that theorem, since the site/index collection is countable. The theorem gives a deterministic limiting speed v for X_n/n almost surely. On T^c, by the definition of not tending to infinity, choose a finite R with infinitely many n satisfying |X_n|≤R. Select increasing such n_k; then X_{n_k}/n_k→0, while convergence of the whole sequence makes this limit v. Thus v=0 there, and multiplying by any scalar ℓ proves the required directional conclusion. If P_0(T^c)=0 the conclusion is of course vacuous; no positive-probability recurrence assumption was used. No recurrence/transience dichotomy or uniform ellipticity was needed.

This uses a published theorem as an input; its nontrivial LLN proof is not reproduced here. It proves the full one-dimensional special case, not the higher-dimensional open question.
'''
p.write_text(s,encoding='utf8')
with Path('CLAIMS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'problem_id':'C0133','claim':'C0133 holds in d=1 for IID elliptic infinite cookie stacks, by Amir–Berger–Orenshtein Theorem 1.3 and a bounded return subsequence.','status':'proved_special_case','proof_location':'ATTEMPT.md, Section 7; LITERATURE.md, verified theorem quote','remaining_gap':'No result here for arbitrary signed-drift stacks in d>=2.','checks':['Source theorem checked in arXiv:1304.7287v2, PDF p.3; exact hypotheses mapped; deterministic subsequence argument written in full.']})+'\n')
print('saved d=1 theorem mapping and literature leads')
