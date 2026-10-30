from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

run=Path(__file__).resolve().parents[1]
agent=run.parents[1]
repo=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
campaign=Path(r'~\brain_workers\FEI100_20261011')
protocol=json.loads((repo/'EXECUTION_PROTOCOL.json').read_text())
now=datetime.now(timezone.utc).isoformat()
def sha(data): return hashlib.sha256(data).hexdigest()
def save(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

statement=('For the fixed-scale formal queue label component C_lab=sum_{A nonempty} fhat(A)^2 min_tau |F_tau(A)| log2 k at lambda=1/k: '
 'odd majority n=2a+1,t=a+1 in its prime DNF has E min|F|=1+T_n, k=binom(n-1,t-1), I=n*binom(n-1,t-1)/2^(n-1), '
 'T_n=P(|S|>t), so C_lab/I~sqrt(pi*n/2); every exact DNF of majority has read at least this k and formal C_lab>=log2 k. '
 'Its minimum allocation pressure among minimum-count assignments is zero except |A|=n, with mean W_n*(t-1)*log2(t/(t-1)) (zero for n=1). '
 'Disjoint tribes w,s with z=2^-w,q=1-(1-z)^s has prime k=1,C_lab=0,allocation=0,E|F|=4*s*z*(1-z)^s,I=2*s*w*z*(1-z)^(s-1); '
 'full-cell C_lab=4*q*(1-q)*log2(2^(ws)*q). '
 'For any Boolean core g on m declared bits with q=P(g=-1)>0 and r>=1 fresh point controls p=2^-r, F=1+A_r(g-1) has '
 'v=4*p*q*(1-p*q),I(F)=p*(I(g)+2*r*q), and full-cell C_lab=v*log2(2^m*q). '
 'For an odd majority core its prime activated DNF has E|F|=2*p-p^2+p*T_m,k=binom(m,(m+1)/2); '
 'for activated prime tribes it has E|F|=4*p*q^2*(1-p)+4*p*s*z*(1-z)^s,k=s. '
 'At r=ceil(2*log2(m+1)) activated majority label/I diverges as Theta(sqrt(m)) despite I and minority probability tending to zero. '
 'Majority and activated majority are single regular gates, removing these formal label and allocation charges. '
 'These statements refute uniform payment of this fixed-scale DNF label expression, not FEI or payment by an optimized complete reference. '
 'Equal full-cell single-root witnesses with identical rank laws sum to N*2^(-Lambda)*lambda*pi, refunding log2 N at lambda=1/N while retaining selected-run root rarity -log2 pi.')

claim={
 'claim_id':'A015-FIXED-SCALE-MINTERM-BARRIER','version':1,'exact_statement':statement,
 'hypotheses':['Uniform finite Boolean cube','Entropy and logarithms in bits','Specified full-cell or canonical prime DNF as stated',
               'Formal charged label component at lambda=1/k; not actual optimized output cost','Point controls fresh and independent',
               'Asymptotics use odd majority m->infinity and stated r; tribes comparisons use w->infinity,s*2^-w->lambda in (0,infinity)'],
 'statement_sha256':sha(statement.encode()),'contributors':['A015/fleet05'],
 'proof_source':{'path':str(run/'REPORT.md'),'supporting_derivation':str(run/'MINTERM_BARRIERS.tex'),
                 'validation':['out/validation.json','out/symbolic_validation.json']},
 'proof_dependencies':[],
 'review_records':[{'reviewer':'A015','method':'Author analytic derivation plus integer FWHT/Fraction and direct-Walsh formal-log reconstruction',
                   'verdict':'AUTHOR_CHECKED_NOT_INDEPENDENT_REVIEW','exact_assertions':46747}],
 'status':'AUTHOR_PROVED_SCOPED_DIAGNOSTIC_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],
 'refutes':['Dimension-independent C_lab<=K I for all exact DNFs at fixed global scale lambda=1/k',
            'A bounded used-gate count by itself pays the fixed-scale minterm label cost',
            'Sparse activation alone pays the fixed-scale full-cell dimension charge'],
 'first_unproved_line':None,
 'next_consumers':['A011','A012','B03','A086','A094','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save(run/'CLAIMS.json',[claim])

next_action=('Reconstruct A012\'s proposed complete posterior-erased activated-literal code, keeping v*log2 Z, '
             'root rarity and core entropy; then compare its refund with the single-regular-gate activated-majority reference. '
             'A086/A094 independently review the scoped obstruction before another broad B03 candidate.')
progress={
 'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B03','packet_id':'A015',
 'gap_id':'G-J-COST-MINTERM-LABEL','attempt_id':'A015-minterm-barrier-1',
 'method':'Whole-set covering counts; exact derivative/tribes spectra; activation sector decomposition; finite root multiplicity refund',
 'mathematical_delta':'Exact label costs on majority, tribes and arbitrary sparse activations; majority fixed-scale C_lab/I diverges after optimal whole-set assignment; grouped regular gate removes it. Subset pressure separated. Root/posterior/normalization obligations retained.',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF',
 'mathematical_status':'SCOPED_PACKET_AUTHOR_PROVED_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':['Threshold 38pp Theorem A@local-current-source (only actual H/I baseline comparison)',
                        'Threshold 38pp Proposition 5.5 and fixed-scale refinement@local-current-source (interface)',
                        'Threshold 38pp Proposition 8.9@local-current-source (independently reconstructed baseline)',
                        'A076-STRUCTURED-SPECTRA@1 (calibration identified; not an assumed proof premise)'],
 'claims_created_or_changed':['A015-FIXED-SCALE-MINTERM-BARRIER@1'],
 'source_artifacts':['REPORT.md','MINTERM_BARRIERS.tex','COMPRESSION_REQUIREMENTS.md','code/check.py','code/symbolic.py',
                     'out/FROZEN_SPEC.json','out/SYMBOLIC_SPEC.json','out/validation.json','out/symbolic_validation.json','out/SOURCES.json'],
 'next_consumers':['A011','A012','B03','A086','A094','B20'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review and supervisor adoption/mirror copying pending; no local save blocker',
             'Universal complete representation/reference cost <=K I remains unproved'],
 'packet_ids':['A015']}
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
save(run/'PROGRESS.json',progress)
save(run/'PACKET_DELTA.json',progress)

paths=[(repo/x,'Full protocol' if x=='EXECUTION_PROTOCOL.json' else 'Campaign intake and scoped registry/dispatch inspection')
       for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json',
                 'PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [(supp/x,'Supplement intake, minterm/normalization/activation guards')
          for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += [(supp/'baseline'/'current-threshold-paper.tex','Regularity definition, Theorem A, full Section 5 interface, activation source')]
paths += [(campaign/'context'/x,'Selected theorem and relevant interfaces; not full independent proof audit') for x in
          ['threshold_paper_38pp.txt','threshold_paper_29pp_earlier_version.txt',
           'percolation_spectral_pivotal_entropy_30pp.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt']]
paths += [(campaign/'BOARD.md','Board read at stage start'),(campaign/'claude'/'B03'/'STREAM_NOTES.md','Lead v1 read at start and rechecked'),
          (supp/'sources'/'OVERLAPPING_PRODUCT_NOTE.md','Full correction/scope read; no reliance on false subadditivity')]
paths += [(p,'Historical scope/heading intake, no theorem dependency') for p in (repo/'runs').rglob('REPORT.md')]
paths += [(p,'Existing first report read; consume gap instead of duplicating baseline')
          for a in ['A012','A076'] for p in (campaign/'agents'/a).rglob('REPORT.md')]
save(run/'out'/'SOURCES.json',[{'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size,'read_scope':scope}
                              for p,scope in paths])

report=run/'REPORT.md'
text=report.read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']: assert '## '+field in text
text=text.replace('Additional symbolic checks and persistence receipts, if present, are separately pinned below/out; independent review has not occurred.',
 '''A second frozen validation (`out/SYMBOLIC_SPEC.json`) runs `python -X utf8 runs\\20261011T225533Z-fleet05-A015-minterm-barrier-analysis\\code\\symbolic.py`. It passed **5,021 additional exact assertions** in 1.127855 seconds: all 810 activation entropy identities and balanced specializations are checked in a formal log2-prime basis, tribes entropy and majority level entropy are checked exactly, minimum allocation pressure is compared by rational products on all 38 nonempty sets at n=3,5, and closed majority/Wallis identities are checked at all 64 odd dimensions through 127 without truth-table escalation. Total exact assertions: **46,747**. Direct Walsh sums supply a different computational reconstruction from the first FWHT helper; this is author verification, not independent review.''')
text=text.replace("consume A012's paid posterior refund", "reconstruct A012's proposed posterior refund")
report.write_text(text,encoding='utf-8')

(agent/'STATUS.md').write_text('STATE: A015 minterm barrier packet complete locally: exact fixed-scale label obstructions and regular-gate repair; 46,747 exact assertions PASS; review pending; full FEI OPEN.\nNEXT: A086/A094 review; reconstruct A012 proposed posterior-erased activation code with root rarity, v log Z and core entropy retained, then transfer to grouped activated majority.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(now+': Exact pilot 866 cases / 41,726 assertions PASS in 1.526478 s. Symbolic entropy/allocation/closed-form check 5,021 assertions PASS in 1.127855 s. Prime majority labels diverge after one/two-gate assignment, tribes prime labels vanish, and sparse activation retains majority barrier; equal-root multiplicity can refund labels but leaves root rarity in that selected-run sum. Saved all protocol files and scoped handoff, no independent review/mirror claim.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('Odd majority n=2a+1,t=a+1: min used prime terms=ceil(|S|/t), E count=1+P(|S|>t), fixed-scale labels/I~sqrt(pi*n/2). Minimum allocation pressure is zero off the full set and mean W_n*(t-1)log2(t/(t-1)). Grouping into one regular gate removes the label charge.\n')
    f.write('Fresh point activation F=1+A_r(g-1), p=2^-r,q=P(g=-1): v=4pq(1-pq), I=p(I(g)+2rq), nonempty-data mass=p Var(g), control-only mass=4p q^2(1-p). Full-cell labels/I=4q(1-pq)log2(2^m q)/(I(g)+2rq). Padding is a direct code-artifact test.\n')
    f.write('Tribes prime DNF has k=1 and zero label/allocation charge; full satisfying cells instead give v log2(2^(ws)q). Activated majority is regular with controls before data. Equal full-cell one-root witnesses refund log N by summation, but retaining pi=2^-d exposes the remaining selected-run rarity bill d.\n')

assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert json.loads((run/'out'/'validation.json').read_text())['exact_assertions']==41726
assert json.loads((run/'out'/'symbolic_validation.json').read_text())['exact_assertions']==5021
files=[p for p in run.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']+[agent/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipts={'saved_at_utc':now,'scope':'local readback only','protocol_fields_checked':True,
          'packet_delta_byte_equal_progress':True,'independent_review':False,'supervisor_adoption':False,'mirror_verified':False,
          'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in files]}
save(run/'out'/'RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','files_hashed':len(files),'total_exact_assertions':46747,
                  'claim_fields':'exact protocol match','progress_fields':'exact protocol match',
                  'report_fields':'all seven present','mirror_verified':False},indent=2))
