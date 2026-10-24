"""Prepare review-only mathematical artifacts in w400; never ingest a live store."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def dump(name, value):
    p = ROOT/name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')


def main():
    src = json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    if src['primary_statement']['source_id'] == 'arxiv:1007.0575v2':
        src['related_chordal_statement'] = src['primary_statement']
    src['primary_statement'] = {
        'source_id':'arxiv:2205.07318v1', 'url':'https://arxiv.org/pdf/2205.07318',
        'author':'Geoffrey R. Grimmett', 'title':'Selected problems in probability theory',
        'locator':'Question 2.2, printed page 3 (PDF index 2)',
        'statement_in_own_words':'Choose uniformly among n-step vertex-self-avoiding paths on the hexagonal lattice starting at the origin, with no prescribed endpoint. The question asks whether their suitably rescaled curves converge weakly to SLE with parameter 8/3.',
        'short_source_quote':'a uniformly distributed n-step SAW from the origin',
        'unspecified_in_source':['Exact spatial normalization','Parametrization or curve topology','Which SLE variant and stopping rule represent the finite free-endpoint curve'],
        'scope_decision':'Do not silently substitute the critical variable-length boundary-to-boundary conjecture. The present work proves elementary conditional identities and explicit obstructions to that substitution, not the full scaling conjecture.',
        'proof_status':'question in the primary source; current openness UNKNOWN'
    }
    src['local_recovery'] = {
        'ranking':'RANKING_2026-09-07.csv line 547: tier 5, attempted_un; not a current-status receipt.',
        'team_o':'Targeted TEAM_BOARD grep found related C0095/C0096 lanes, not an exact P0003 row.',
        'prior_attempts':'Read the exact prior P0003 attempt from the live store in read-only mode: finite-domain conditional law with the tip retained, explicitly no tightness or conformal-invariance conclusion, and fixed remaining length distinguished. Exact P0003 grep in named H/I attempt directories returned no match; this is not evidence that no owner solution exists.',
        'lean':'The named annotated ranking repeats attempted_un; no actual P0003 theorem/axiom receipt recovered.',
        'math_store':'STORE_BEFORE.json records the exact live P0003 problem and prior-attempt rows from a read-only connection. The problem statement agrees with Grimmett Question 2.2.',
        'paired_proof':'Read w399 STATEMENT_FOR_ADVERSARY.md, APPROACH_DISTINCT.md and three named lemma files after independent derivations were saved. Audited actual derivations, not another review.',
        'owner_solved_retired':'No verified complete owner solution/retirement receipt recovered by the authorized targeted checks; current openness therefore remains UNKNOWN.'
    }
    src['independent_review'] = 'Requested w401 by mesh msg-36273611b9; pending independent proof check.'
    dump('SOURCE_STATUS.json', src)
    rows = [
      {'id':'P0003-w400-004','exact_statement':'Conditioning a normalized positive-fugacity law on one feasible length n gives a uniform law on the n-step paths in the same underlying path collection. This does not remove a prescribed endpoint or domain restriction.',
       'assumptions':['finite path collection','weight of every path equals x^length with x>0','positive number of paths at length n'],
       'proof_or_counterexample':'Every path surviving the condition has weight x^n; cancellation leaves the reciprocal of the number of surviving paths. Changing the path collection is an additional operation.',
       'remaining_gap':'Transfer from related chordal ensemble to the exact whole-lattice rooted/free-endpoint target.'},
      {'id':'P0003-w400-005','exact_statement':'A common weak joint shape/length limit and identical discrete length marginals do not determine conditional shape laws at one prescribed length.',
       'assumptions':['n even','L_n uniform on {1/n,...,1}','X_n=0 except at L_n=1/2','two sequences have X_n=+1 or -1 at that atom'],
       'proof_or_counterexample':'Each joint law has total variation distance 1/n from the zero-feature law with the same length marginal. Those base laws converge by Riemann sums to (0,U), U uniform on [0,1]. Both joint laws have that same limit, while their laws conditioned on L_n=1/2 have X=+1 and X=-1 respectively.',
       'remaining_gap':'This is an abstract transfer obstruction, not evidence that actual honeycomb SAW fails to converge.'},
      {'id':'P0003-w400-006','exact_statement':'Positive exponents alpha_n tending to zero can make derivative-power probe processes tend to constants and their raw drift residuals tend to zero without identifying the Loewner variance as 8/3.',
       'assumptions':['deterministic capacity-parametrized Loewner driver W=0','three initial slit probes (x,s)=(1,1),(-1,1),(1,3)','alpha_n=1/n','a local interval before hull contact with uniformly bounded derivative jets and h-prime bounded away from zero'],
       'proof_or_counterexample':'The bounded log-derivative implies exp(alpha_n log h-prime) tends uniformly to 1. The raw relative drift is alpha_n(-4c/3+u^2/2), initially alpha_n times (9/8,9/8,33/32), but the driver has variance rate zero. At n=128 raw residual <1/100 while the residual divided by alpha_n is 9/8. The fixed-positive-alpha lemma is not contradicted.',
       'remaining_gap':'The SAW limit input must supply a fixed positive common exponent, or errors after the exponent normalization; independent check pending.'},
      {'id':'P0003-w400-007','exact_statement':'If for every bounded continuous f a selected-length numerator equals h_delta rho Q(f)+o(h_delta) and its conditioning probability equals h_delta rho+o(h_delta), with h_delta>0 and rho>0, then its conditional laws converge weakly to Q.',
       'assumptions':['common metric curve space','Q a Borel probability measure','h_delta>0 tends to zero','rho>0 fixed','the two stated relative local asymptotics at the selected discrete length'],
       'proof_or_counterexample':'Divide the two asymptotics; the denominator is positive eventually and the ratio tends to Q(f) for every bounded continuous test function.',
       'remaining_gap':'No such conditional local limit is established here for actual SAW.'}
    ]
    existing = {json.loads(line)['id'] for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line}
    with (ROOT/'CLAIMS.jsonl').open('a',encoding='utf-8') as out:
        for r in rows:
            if r['id'] in existing:
                continue
            r.update(source={'source_id':'owner-own-work:'+r['id'],'license':'owner-own-work','path':'ATTEMPT.md'}, independent_reviewer='w401 (requested, pending)', independent_check_state='not checked', status='proved special case' if r['id'] != 'P0003-w400-007' else 'sketch')
            out.write(json.dumps(r,ensure_ascii=False)+'\n')
    base = {'namespace':'probability.self_avoiding_walk','kind':'concept','proof_text':None,'domain':'probability / self-avoiding walk scaling limits'}
    specs = [
      ('ensemble-guard','saw-fixed-length-and-chordal-ensemble-transfer-guard','Fixed-length SAW needs an explicit ensemble transfer',
       'A proof for the critical variable-length boundary-to-boundary SAW law does not by itself prove convergence for the uniform n-step honeycomb walk rooted at the origin with a free endpoint. In a fixed finite path collection, conditioning fugacity weights x^L on L=n gives uniform n-step weights, but a shrinking conditioning probability can invalidate transfer from a weak mixture limit. A conditional local limit with relative error, as well as endpoint and domain transfer, is an additional premise. This campaign concept is a draft; it is not an SLE convergence proof.',
       ['P0003 exact source is Grimmett Question 2.2 (arXiv:2205.07318)','Related chordal source is Duminil-Copin--Smirnov Conjecture 1 (arXiv:1007.0575)']),
      ('rare-atom','weak-joint-limit-does-not-determine-rare-length-conditioning','Rare prescribed-length conditioning is not determined by a joint weak limit',
       'A weak joint shape/length limit does not determine conditional shape at a prescribed lattice length. For even n, let L_n be uniform on {1/n,2/n,...,1} and let X_n=0 except at L_n=1/2. Choose X_n=+1 there in one sequence and -1 in another. Both joint laws tend to (0,U), where U is uniform on [0,1], and have identical length marginals. Their conditional features at L_n=1/2 are respectively +1 and -1; that atom has mass 1/n. Thus the required transfer must control relative conditional errors, not just a weak mixture limit. Author-derived explicit counterexample; independent review pending.',
       ['n even','The two finite joint laws are exactly the ones stated','No claim that these laws model actual critical SAW']),
      ('exponent-guard','loewner-probe-small-raw-drift-needs-positive-exponent-limit','Loewner probe errors require exponent normalization',
       'Small raw drift of derivative-power Loewner probes does not identify a Brownian variance if their positive exponents tend to zero. With deterministic driver W=0 and alpha_n=1/n, on a local interval with bounded derivative jets and h-prime bounded away from zero, (h-prime)^alpha_n tends uniformly to 1. For slit probes (x,s)=(1,1),(-1,1),(1,3), the initial raw relative drifts are alpha_n times (9/8,9/8,33/32), yet the variance rate is zero. At n=128 the maximum raw drift is 9/1024<1/100, while division by alpha_n leaves 9/8. Require a fixed positive common limiting exponent or exponent-normalized error control. Author-derived obstruction; independent review pending.',
       ['Half-plane capacity equation dg_t/dt=2/(g_t-W_t)','Driver W=0','Stop before a Loewner hull meets a probe','The jets and inverse first derivative are locally bounded']),
      ('relative-transfer','relative-local-limit-suffices-for-fixed-length-conditioning','Relative local limits suffice for fixed-length transfer',
       'A relative local limit is a sufficient fixed-length transfer premise. Let Gamma_delta be curves in a common metric space and let L_delta be an integer length. Suppose Q is a probability law, h_delta>0 tends to zero and rho>0. For every bounded continuous f, assume E[f(Gamma_delta) 1_{L_delta=n_delta}]=h_delta rho Q(f)+o(h_delta), and P(L_delta=n_delta)=h_delta rho+o(h_delta). The conditional laws given L_delta=n_delta then converge weakly to Q, by dividing these asymptotics. This criterion is conditional draft material; its SAW hypotheses are not proved here and independent review is pending.',
       ['The common curve space is metric','Q is a Borel probability law','The specified relative asymptotics hold for every bounded continuous test function','rho>0'])
    ]
    entries = []
    for key, logical, title, statement, assumptions in specs:
        entries.append(dict(base,key=key,logical_name=logical,title=title,statement=statement,assumptions=assumptions,
                            source={'source_id':'owner-own-work:P0003-w400:'+key,'url':'urn:owner-own-work:P0003:w400:'+key,'revision':'2026-10-10 author-derived draft; w401 check pending','license':'owner-own-work','excerpt':None}))
    bundle = {'spec':'mathbrain-draft-v1','author_agent':'w400','bundle_slug':'p0003-conditional-transfer-obstructions-w400-001','entries':entries,
              'relations':[
                  {'from_key':'ensemble-guard','to_key':'rare-atom','kind':'depends_on','rationale':'The guard says a shrinking length condition can invalidate weak-limit transfer; the rare-atom card exhibits identical weak limits and length marginals with opposite conditional features.'},
                  {'from_key':'relative-transfer','to_key':'rare-atom','kind':'semantic_association','rationale':'Relative local asymptotics control exactly the selected conditional numerator and denominator that the rare-atom counterexample leaves undetermined.'},
                  {'from_key':'ensemble-guard','to_key':'exponent-guard','kind':'semantic_association','rationale':'The ensemble guard needs relative conditioning error; the exponent guard needs error after division by alpha. Both explicitly prevent an absolute error from being used after a vanishing normalization.'},
                  {'from_key':'ensemble-guard','to_existing_logical':'math:probability.core:open-problem-p0003-hexagonal-self-avoiding-walk-scaling-limit','kind':'cites','rationale':'The read-only store P0003 statement concerns uniform n-step walks from the honeycomb origin; the guard preserves that exact target when reviewing a related chordal-fugacity argument.'}
              ]}
    dump('drafts/bundle_001.json',bundle)
    audits = [
        {'id':'P0003-w399-three-probe','artifact':'~/brain_workers/w399/LEMMA_THREE_PROBE.md','verdict':'KEEP_CONDITIONAL','why':'Independent Taylor and Ito derivation agrees; determinant, inverse and bounds are checked by exact diagnostics. Semimartingale regularity, common fixed positive exponent, valid stopped conformal maps, local invertibility and global coverage must remain explicit. This is not a complete SAW proof.'},
        {'id':'P0003-w399-exponent-passage','artifact':'~/brain_workers/w399/LEMMA_THREE_PROBE.md','verdict':'MISSING_PREMISE_FOR_SAW','why':'A positive mesh-dependent alpha may tend to zero. The deterministic-driver counterexample shows that raw drift convergence alone is insufficient. Supply a fixed positive common limiting alpha or error control after division by alpha.'},
        {'id':'P0003-w399-exact-target','artifact':'~/brain_workers/w399/STATEMENT_FOR_ADVERSARY.md','verdict':'SCOPE_LIMIT','why':'The packet explicitly studies the related critical chordal ensemble. Grimmett Question 2.2 and the live P0003 card concern fixed length and a free endpoint. Full-target credit needs a conditional local-limit, endpoint and domain transfer; preserve the packet as a related conditional specialization.'}
    ]
    (ROOT/'AUDIT_VERDICTS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in audits),encoding='utf-8')
    dump('BRAIN_HANDOFF.json',{'author':'w400','prepared':True,'draft_local':'drafts/bundle_001.json','submitted':False,'reviewed':False,'ingested':False,'retrievable':False,'independent_reviewer':'w401','review_request':'msg-36273611b9','formal_check_receipt':None,'live_store_writes':False,'next':'Submit the four concept drafts under a narrow inbox claim; reviewer checks the original proofs before integration.'})
    print(json.dumps({'claim_rows_added':len(rows),'draft_entries':len(entries),'audit_rows':len(audits),'source_target':'Grimmett Question 2.2','status':'review draft prepared'}))


if __name__ == '__main__':
    main()
