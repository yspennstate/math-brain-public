import json
from pathlib import Path
from save_result import save

ROOT=Path(__file__).resolve().parent
save('P0218','max-influence-city-founding-rate','Verified founding-rate bound at the critical immigration parameter',
'''In the Aldous-Huang max-influence city model on the unit square, with alpha=1, beta>0 and c0>0, let M_t be the number of cities and let their positive populations sum to t. With I(y,t)=c0*max_i N_i(t)*|y-x_i|^(-beta), a uniform new arrival founds a city with probability 1/(1+I(y,t)). Its conditional founding probability is at least 1/[2*(1+K*t*M_t^d)], where d=max(beta/2-1,0) and K=(2*pi)^(beta/2)*c0. Consequently almost surely liminf M_t/(log t)^(min(1,2/beta))>0. This includes the boundary beta=2 and beta<2 as well as beta>2.''',
'''For u>0 the set {y:I(y,t)>u} is contained in the union of M_t disks, the ith having area pi*(c0*N_i/u)^(2/beta). Clipping to the unit square and disk overlap only reduce the area. Put q=2/beta>0. If q<=1, concavity gives sum_i N_i^q<=M_t^(1-q)*t^q. If q>=1, each N_i/t is in [0,1], so sum_i (N_i/t)^q<=sum_i N_i/t=1. Together these give sum_i N_i^q<=M_t^max(1-q,0)*t^q. Thus the area is at most pi*(c0/u)^q*M_t^max(1-q,0)*t^q. Choose u=K*t*M_t^max(beta/2-1,0). Substitution makes this bound exactly 1/2. On the complement, the founding chance is at least 1/(1+u). Integrating over the uniform arrival position yields the displayed lower bound. The new-city indicator changes M_t by one, while a join changes it by zero, so the conditional count-process lemma, whose proof also holds for d=0, applies. Its exponent 1/(d+1) is min(1,2/beta), giving the stated almost sure lower bound. The cached primary paper, Section 2, equations (1)-(3) and rules (i)-(ii), explicitly defines the max influence and founding probability and permits alpha=1.''',
['The unit-square max-influence model defined above','alpha=1 and beta>0','A uniform arrival at each integer step and total population t','c0>0 is fixed'],
'This gives a lower logarithmic city-count order, not a matching upper bound, a limiting constant, or balanced city population sizes. Independent audit is pending.')

save('P0024','one-hole-exclusion-source-restriction','The source excludes one-hole long-term counterexamples',
'''SOURCE RESTRICTION, not a newly proved theorem: Burdzy's cached author problem page, Problem 5(i), states that a bounded smooth-domain counterexample with positive-probability limsup |X_t-Y_t|>0 must have at least two holes, attributing this to Burdzy, Chen and Jones (2006). Thus the annular finite-time expansion in this packet cannot settle that long-term question. The full theorem and precise bibliographic record still need to be checked in the referenced paper.''',
'''The public author page cached on 2026-09-06 says: "then it must have at least two holes" (text.txt:120-123). The earlier lines formulate the smooth connected planar domain problem and allow initial points in its closure. Our annulus has exactly one hole. This row records and applies the source's stated restriction; it does not reproduce or claim to have checked the cited paper's full proof. Its exact available reference is Burdzy, Chen and Jones (2006), as cited in that page. The distinct finite-time deterministic expansion remains correct.''',
['The scope and restrictions stated on the cached author page','The annulus has one hole'],
'Historical primary-source status evidence. The referenced full theorem, exact title and journal details remain a literature-check task; no claimed open-problem solution follows.',label='source-status',kind='concept')

# Tighten scope notes after checking the primary max-influence model definition.
rows=[json.loads(line) for line in (ROOT/'results.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
for row in rows:
    if row.get('slug')=='critical-immigration-logarithmic-lower-bound':
        row['statement']=row['statement'].replace('K>0,d>0','K>0,d>=0').replace('Under the earlier city-model founding estimate at alpha=1 and beta>2, d=beta/2-1, giving exponent 2/beta.','For the verified alpha=1, beta>0 city model, d=max(beta/2-1,0), giving exponent min(1,2/beta).')
        row['assumptions']=[assumption.replace('K>0 and d>0','K>0 and d>=0') for assumption in row['assumptions']]
        row['limitations']='The primary model definition and the spatial founding-rate bound are checked in max-influence-city-founding-rate.md, so the lemma supplies an almost-sure lower bound for the alpha=1, beta>0 Aldous-Huang model. It gives no matching upper bound or comparable city populations.'
    if row.get('slug')=='annular-skoro-distance-expansion':
        row['limitations']='Finite-time deterministic expansion is compatible with eventual Brownian contraction. The cached author page excludes one-hole domains as long-term counterexamples (see one-hole-exclusion-source-restriction.md). No positive long-time limsup is established.'
    if row.get('slug') in {'critical-immigration-logarithmic-lower-bound','annular-skoro-distance-expansion'}:
        path=Path(row['proof_path'])
        text=f'# {row["problem_id"]}: {row["title"]}\n\nLabel: {row["label"]}; author checked only. Independent audit: PENDING w347.\n\n{row["statement"]}\n\nAssumptions: '+ '; '.join(row['assumptions'])+f'\n\n{row["proof_text"]}\n\nLimits: {row["limitations"]}\n\nExisting card: {row["to_existing_logical"]}\nSource snapshot: {row["source_path"]}:{row["source_line"]}\n'
        path.write_text(text,encoding='utf-8')
(ROOT/'results.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows),encoding='utf-8')
