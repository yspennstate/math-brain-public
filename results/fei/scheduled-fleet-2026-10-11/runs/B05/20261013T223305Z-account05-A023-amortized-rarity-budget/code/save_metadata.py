"""Save protocol metadata and verify persisted exact certificates; no search."""
import copy
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
ROOT = RUN.parents[1]
TEAM = ROOT.parents[1]
RID = RUN.name
PREV = ROOT / 'runs/20261012T010933Z-account05-A023-amortized-rarity-budget'
PROTO = Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))
def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
def digest(path):
    raw = path.read_bytes()
    return {'path':str(path), 'bytes':len(raw), 'sha256':hashlib.sha256(raw).hexdigest()}

protocol = read(PROTO)
consumers = ['A021','A022','A025','A028','A029','A064','A087','A094','B05','B20']
old = next(c for c in read(PREV/'CLAIMS.json') if c['claim_id'].startswith('A023-OVERLAP'))
claim = copy.deepcopy(old)
claim.update(version=2, proof_source=str(RUN/'REPORT.md'),
    review_records=[], supersedes=[{'claim_id':old['claim_id'],'version':1}],
    next_consumers=consumers,
    proof_dependencies=[{'claim_id':old['claim_id'],'version':1,
        'source':str(PREV/'REPORT.md'),
        'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
        'role':'Preserved version-1 scope only; new separator theorem independently derived.'}])
claim['exact_statement'] += (
    ' Additional one-separator theorem: for all independent fresh point blocks W,U,V '
    'of widths L,R,T>=1, one fair bit X and independent balanced Boolean g, let '
    'A=XU OR XV OR WUV, F=1+A(g-1), p=2^-L,q=2^-R,r=2^-T, '
    'beta=q+r-qr,eta=pqr,pi=(beta+eta)/2,e=beta-eta. Query X first, then '
    'resolve WUV or U OR V, stopping at a constant or g. Every descendant control '
    'node is strictly threshold-4-good; no root-goodness is assumed. '
    'd_X=e/2, Jrem=[(L+R+T)eta+R q(1-r)+T r(1-q)]/2, '
    'I(F)=d_X+Jrem+pi I(g), terminal entropy=pi H(g). '
    'The root face cost is exactly Jrem+e I(g)/2 and '
    'Q_bad<=Jrem+pi I(g)=I(F)-d_X. One marked reserve, consumed before '
    'descent and never renewed, proves H(F)<=(5+2/ln2)(d_X+Jrem)'
    '+pi H(g)+e I(g)/2. Retained genuine minority/KL bill is <=5(d_X+Jrem)'
    '+pi H(g)+e I(g)/2; adding its 3mu/ln2 allowance replaces 5 by 5+3/ln2. '
    'If H(g)<=C0 I(g), H(F)<=max(5+2/ln2,C0+1)I(F). '
    'For g=z times a fair selector between any bent sign on even k>=4 '
    'bits and its one-vertex flip, H(F)<8I(F), retained J+terminal<=5I(F), '
    'and full sufficient KL ledger<10I(F), uniformly in L,R,T,k. '
    'This does not assert repeated-separator reserve ownership or arbitrary-core FEI.')
claim['hypotheses'] = old['hypotheses'] + [
    'The additional separator subtheorem uses a balanced independent core, a single fair physical separator, and disjoint fresh positive point blocks; earlier subtheorems keep their own original hypotheses.',
    'The additional unconditional terminal family uses an independent balancing sign z; all terminal entropy is retained.'
]
canonical = json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':'))
claim['statement_sha256'] = hashlib.sha256(canonical.encode()).hexdigest()

src21 = TEAM/'agents/A021/runs/20261013T214613Z-account05-A021-rare-core-asymptotics'
reviewed = copy.deepcopy(read(src21/'CLAIMS.json')[0])
reviewed['review_records'].append({'reviewer':'A023',
    'source':str(RUN/'REVIEW_A021_WITNESS.md'),
    'verdict':'HOLDS_WITNESS_AND_BALANCED_CONTROL_TRANSFER_ONLY',
    'scope':'Actual five-bit bad-root witness, exact prime-log sign, and arbitrary balanced-core transfer of controller B and d only.',
    'excluded':'No independent acceptance of tensor-prefix exposure, inclusion-exclusion census, 680-case closure, or full dependency chain.',
    'repair_supplied':False})
save(RUN/'CLAIMS.json',[reviewed,claim])

sources=[PROTO,TEAM/'BOARD.md',TEAM/'claude/B05/STREAM_NOTES.md',
    TEAM/'claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport/REPORT.md',
    src21/'REPORT.md',src21/'DERIVATION.md',src21/'CLAIMS.json',
    TEAM/'agents/A028/runs/20261012T011208Z-account05-A028-stopping-tree-payment/DERIVATION.md',
    PREV/'OVERLAP_GOOD_NODE_PROOF.md',PREV/'REPORT.md',PREV/'CLAIMS.json']
sources += sorted((TEAM/'agents/A022/runs').glob('20261013*/REPORT.md'))
save(RUN/'out/source_receipts.json', {'scope':'Read provenance; not independent acceptance',
    'files':[digest(p) for p in sources]})

signs=read(RUN/'out/sign_certificates.json')
for entry in signs:
    if entry.get('exact_equal'):
        assert not entry['vector'] and not entry['bad']
        continue
    lo,hi=Q(entry['lower']),Q(entry['upper'])
    assert lo<=hi
    assert (lo>0) if entry['bad'] else (hi<0 or lo==hi==0)
rows=read(RUN/'out/results.json')
for row in rows:
    p,q,r=(Q(1,2**row[v]) for v in ['L','R','T'])
    beta,eta=q+r-q*r,p*q*r
    pi,e=(beta+eta)/2,beta-eta
    rem=((row['L']+row['R']+row['T'])*eta+row['R']*q*(1-r)+row['T']*r*(1-q))/2
    assert Q(row['pi'])==pi
    assert Q(row['root_d'])==e/2
    assert Q(row['remaining_control_reserve'])==rem
    assert Q(row['control_I'])==e/2+rem
    ig=Q(row['terminal_I'])/pi
    assert Q(row['root_face_credit'])==rem+e*ig/2
    assert Q(row['bad_credit'])==(Q(row['root_face_credit']) if row['root_bad'] else 0)
    assert Q(row['bad_credit'])<=rem+Q(row['terminal_I'])
    assert Q(row['minority_mass_sum'])<=Q(row['control_I'])
assert len(rows)==35 and len(signs)==38
validation=read(RUN/'out/validation.json')
assert validation['checks']==729
# ln 2 = 2 atanh(1/3) > 2(1/3+(1/3)^3/3)=56/81.
assert 2*(Q(1,3)+Q(1,81))==Q(56,81)
assert 5+2*Q(81,56)<8 and 5+3*Q(81,56)<10
save(RUN/'out/constant_certificate.json',{'ln2_lower':'56/81',
    'proof':'positive atanh series at 1/3, first two terms; remaining terms strictly positive',
    'reciprocal_ln2_upper':'81/56','entropy_rate_upper':str(5+2*Q(81,56)),
    'full_KL_rate_upper':str(5+3*Q(81,56))})

artifacts=['REPORT.md','SEPARATOR_RESERVE_PROOF.md','REVIEW_A021_WITNESS.md',
    'code/check_separator.py','code/save_metadata.py','out/FROZEN_SPEC.json',
    'out/results.json','out/witness.json','out/sign_certificates.json',
    'out/validation.json','out/source_receipts.json','out/constant_certificate.json']
progress=dict(protocol_revision=protocol['revision'],run_id=RID,stream='B05',packet_id='A023',
    gap_id='G-R-MISMATCH-FIRST-REVELATION',attempt_id='A023-3-separator-reserve',
    method='Independent bad-root witness reconstruction; exact physical boundary partition; one-use separator reserve with retained terminals',
    mathematical_delta='Partial independent A021 witness/balanced-transfer review; infinite three-event overlap family has Q_bad<=I-d_X, H<8I on balanced bent-surgery cores, retained J<=5I and full sufficient ledger<10I; 35 roots and 729 exact assertions.',
    deliverable_status='COMPLETE_LOCAL_ARTIFACT',
    mathematical_status='SCOPED_THEOREM_PROVED_LOCALLY; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
    claim_versions_used=claim['proof_dependencies'],
    claims_created_or_changed=[{'claim_id':reviewed['claim_id'],'version':reviewed['version'],'change':'Partial review record only'},
        {'claim_id':claim['claim_id'],'version':2}],
    source_artifacts=artifacts,next_consumers=consumers,
    next_action='Replace X by a multi-bit point separator; track the remaining physical reserve at each reached layer and prove disjoint consumption or certify a growing deficit, retaining all terminal entropy.',
    stagnant_substantive_attempts=0,
    blockers=['Arbitrary-depth ownership of separator reservations is unproved.',
        'Universal terminal entropy certificate is unproved; scoped new theorem awaits independent review.'],
    packet_ids=['A023'])
save(RUN/'PROGRESS.json',progress)
save(RUN/'PACKET_DELTA.json',progress)
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
expected=set(protocol['required_per_run']['progress_fields'])
expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
for c in read(RUN/'CLAIMS.json'):
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:
    assert '\n# '+field+'\n' in '\n'+report
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')

(ROOT/'STATUS.md').write_text(
    'STATE: A023 stage 3 complete: one-use separator reserve proves Q_bad<=I-d_X and H<8I on infinite balanced three-event bent-surgery family; 729 exact checks; A021 witness partial review HOLDS; independent theorem review pending; FEI OPEN.\n'
    'NEXT: Replace the one-bit separator by a multi-bit point block and track remaining reserve per reached layer; A087/A094 independently review boundary ownership, descendant goodness and terminal quantifiers.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-13 22:33 UTC stage ('+RID+'): Read updated BOARD, B05 direction and A021/A022/A028 new results. Independently reconstructed the actual bad x0 witness and balanced-control transfer, without accepting the whole A021 compound claim. Avoided repeating the 680-case census. Proved unbounded XU OR XV OR WUV separator family using a once-marked remaining-control/core reserve; c_X=Jrem+e I(g)/2, all descendants good, terminal pi H(g) retained. H<8I on balanced bent-surgery cores; retained J<=5I, full ledger<10I. Frozen 35 roots completed 729 exact assertions in 0.220162 seconds; 38 rational sign certificates. Extended existing overlap claim v2; universal repeated-separator ownership remains the first gap. Saved protocol artifacts and rolling files locally.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-13: For A=X(U OR V) OR WUV with one fair X and disjoint point blocks, balanced core, beta=q+r-qr, eta=pqr, pi=(beta+eta)/2, e=beta-eta, d_X=e/2 and Jrem=(J(WUV)+J(U OR V))/2. The difference indicator D=(U OR V)-WUV satisfies J(D)=2Jrem exactly because its two boundary contributions are disjoint. Root face credit is Jrem+e I(g)/2<=I(F)-d_X. Descendant point/union queries are good. Reserve one rate unit of remaining physical control influence and one terminal-core unit for this root only, delete those units before descent; this gives H<=max(5+2/ln2,C0+1)I if Hcore<=C0 Icore. A balanced bent-surgery core gives H<8I, retained J<=5I, full ledger<10I. This is NOT permission to recreate the reserve at every ancestor. Source A021 bad-root witness is genuine and B,d transfer across arbitrary balanced cores; face price still depends on core influence. Thirty-five zero-bad separator fixtures do not prove universal root-goodness.\n')
files=[p for p in RUN.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20*1024*1024 for p in files)
save(RUN/'out/artifact_check.json',{'status':'PASS','exact_sign_certificates':len(signs),
    'saved_roots_checked':len(rows),'protocol_schemas':'PASS','report_fields':'PASS',
    'compatibility_copy_identical':True,'file_size_limit':'PASS',
    'review_status':'New theorem pending independent review; source claim review partial only'})
save(RUN/'out/artifact_receipts.json',{'scope':'Local persistence only; no remote mirror/adoption/review receipt',
    'files':[digest(p) for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='artifact_receipts.json'],
    'rolling':[digest(ROOT/p) for p in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'status':'PASS','claim_version':2,'roots':len(rows),
    'sign_certificates':len(signs),'schemas':'PASS','rolling_files':'SAVED'}))
