import pathlib,json
p=pathlib.Path('LITERATURE.md');log=json.loads(pathlib.Path('second_search_log.json').read_text(encoding='utf8'))
text='''

# Second-attempt literature and brain checks, 2026-10-12

The gap itself was queried, read-only, with math_recall.py:

- "Thorisson shift coupling invariant sigma field ergodic absolutely continuous random shift".
- "Kakutani product measures Hellinger equivalence independent stopping times regeneration".
- Linked card read in full: claim_2b15255aa3a9ad0d5f14525fa3513e2c3fed532d5e9ecbdaa534014e943ad3e7, *A randomized forward filling lemma for an ergodic stationary law*.

The first recall returned the candidate Problem 7.5 filling scheme and standard ergodicity cards. The recalled filling lemma transports an invariant law P to a biased law fP; this attempt instead proved the needed opposite transport direction fP to P in ATTEMPT.md, Lemma E. Auxiliary uniform randomness is an explicit assumption of the card and of the newly proved lemma. The second query returned Hellinger definitions and nearby stopping-time cards, but no card proving the proposed stopped-piece compatibility implication. These cards were hints, not verdicts.

New exact references checked:

1. Shizuo Kakutani, *On Equivalence of Infinite Product Measures*, Annals of Mathematics, second series, **49** (1948), no.1, 214–224. DOI 10.2307/1969123. Crossref confirmed title, author, volume, January 1948, and starting page 214. The one-way sufficient domination argument needed here was proved in full independently as Lemma G; no unstated use of the equivalence half of Kakutani's theorem occurs.
2. Hermann Thorisson, *Transforming random elements and shifting random fields*, Annals of Probability **24** (1996), no.4, 2057–2064. DOI 10.1214/aop/1041903217 (Crossref confirmed title, author, volume, date and DOI). The theorem is reproduced as Theorem 5.9 on PDF p.19 in the already downloaded Pitman–Tang paper:

> Theorem 5.9. [83] Let (Z_t; t ∈ R) and (Z'_t; t ∈ R) be two path-measurable processes with a state space (E, E). Then there exists a random time T-hat ∈ R such that theta_{T-hat} Z has the same distribution as Z' if and only if the distributions of Z and Z' agree on the invariant sigma-field I.

Subscripts, prime, theta, hat and sigma-field symbols are transcribed from PDF typography. This is an abstract shift-coupling theorem. It does not prove that the exact P0030 objects agree on the invariant sigma-field; establishing that agreement is the remaining gap. It is therefore a neighbouring-area tool, not SOLVED_IN_LITERATURE for Problems 7.1–7.3. For centered Brownian paths the recentering action can be represented by the trajectory of centered-window states; this attempt's integer filling proof directly uses the recentering action and avoids silently identifying it with raw spatially uncentered path translation.

Second-attempt searches, all by Python urllib from the shell:
'''
for x in log:text+=f"\n- Date {x['date']}; service/query `{x['service']}`; status `{x['status']}`; request {x['url']} ; raw response {x['file']}.\n"
text+='''
The combined arXiv forward-Brownian/Kakutani/Hellinger/absolute-continuity query returned no entries. Crossref searches found the two classical references above, rather than a new paper resolving the source questions. This second attempt establishes additional special cases by combining known tools and a fully checked filling argument; no novelty or full literature-solution claim is made.
'''
p.write_text(p.read_text(encoding='utf8')+text,encoding='utf8')
p=pathlib.Path('CLAIMS.jsonl')
new=[
 dict(problem_id='P0030',claim='Replacing one iid finite-mean killed-hitting Brownian piece by an untruncated first-hit-of-minus-one piece of infinite mean still gives 2BM after a finite random shift on an extension.',status='proved_special_case',proof_location='ATTEMPT.md, Example L',remaining_gap='Only a dominated finite exception is handled; no conclusion for arbitrary infinite exceptional sequences or the unrestricted compatibility hypotheses.',checks=['Reference T_0=min(tau,Exp(1)) has positive finite mean; both rules are stopping times in normal Brownian filtrations.','Full stopped-pair density f=e^T times indicator(endpoint=-1) verified by conditioning on the independent exponential time.','Affinity E exp(-tau/2)=e^-1 proved by bounded stopped exponential martingale.','Actual first-hitting mean is infinite by reflection tail; original backward half stays positive near zero and is not BM at that join.','Theorems H/J supply the finite shift despite infinite actual mean.']),
 dict(problem_id='P0030',claim='Independent stopped Brownian piece laws repeating with a finite period and finite positive total mean duration per period give 2BM after a shift.',status='proved_special_case',proof_location='ATTEMPT.md, Periodic finite-mean control',remaining_gap='Periodicity is additional; arbitrary nonperiodic laws are not treated by grouping.',checks=['Group one period into a stopped Brownian piece by finite strong-Markov gluing.','Grouped pieces are iid with finite positive mean, so source Theorem 5.1 applies.']),
 dict(problem_id='P0030',claim='A bounded nonperiodic growing-sign-block stopping-rule likelihood probe showed no density-collapse signal through 128 backward unit increments; this is finite numerical evidence only.',status='numerical_evidence',proof_location='ATTEMPT.md, Supplementary bounded-rule likelihood probe; second_likelihood_probe.json',remaining_gap='No uniform integrability, BBM, continuous-path domination or exact shift is proved for the nonperiodic test family.',checks=['Exact finite likelihood recurrence derived by conditioning on duration 1 versus 2 and unobserved Gaussian increments.','500 normal-reference samples at N=16,64,128; growing-block estimated second moments 1.1222,1.1088,1.1395.','Constant, periodic and square-summable proved controls included; results and seed saved.'])]
p.write_text(p.read_text(encoding='utf8')+''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in new),encoding='utf8')
print('appended literature and',len(new),'claims')
