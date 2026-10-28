"""Package a source-complete, explicitly conditional assembly; no theorem promotion."""
from pathlib import Path
import json,hashlib,re,datetime,copy
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parents[1]
OLD=A/'runs/20261022T231100Z-account03-A099-candidate-assembly'
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
primary=rd(R/'out/EXACT_RECONSTRUCTION.json');pilot=rd(R/'out/PILOT.json')
assert primary['status']==pilot['status']=='PASS'
assert primary['Boolean_tables']==256 and primary['policies']==3072 and primary['seconds']<55
assert primary['positive_first'] and primary['later_returns'] and primary['old_nonconstant']
assert hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest() in rd(R/'out/FROZEN_SPEC_V2.json')['helper_version']
paths={
 'A085':TEAM/'agents/A085/runs/20261022T234859Z-account03-A085-certificate-adversary',
 'A096':TEAM/'agents/A096/runs/20261023T010221Z-account03-A096-live-gap-ledger',
 'A097':TEAM/'agents/A097/runs/20261023T021120Z-account03-A097-cross-route-transfer',
 'A098':TEAM/'agents/A098/runs/20261023T031803Z-account03-A098-resource-reallocation'}
src={a:rd(p/'CLAIMS.json') for a,p in paths.items()}
claims=rd(OLD/'CLAIMS.json');ids={c['claim_id']:c for c in claims}
review_source=next(c for c in src['A085'] if c['claim_id']=='A099-PRESCRIBED-EXIT-SOURCE-RESET')
our=ids[review_source['claim_id']]
assert all(our[k]==review_source[k] for k in ['version','exact_statement','hypotheses','statement_sha256'])
our['review_records']+=review_source['review_records']
our['status']='ONE_A085_SCOPED_ACCEPTANCE_INTEGRATED_AUDITS_OPEN'
new_specs=[('A085','A085-POSTQUERY-EXIT-DIRECT-SOURCE-RESET','sec:exitfloor8'),
 ('A096','A096-SELECTIVE-FRONTIER-LIKELIHOOD-TRANSFER','thm:floorfront8'),
 ('A096','A096-ARBITRARY-EXIT-FRONTIER-SAME-ANCESTOR','sec:exitfloor8'),
 ('A097','A097-ORIGINAL-SOURCE-CANONICAL-RETURN-COMMUTATION','thm:repeat8')]
new=[]
for author,cid,label in new_specs:
 c=copy.deepcopy(next(x for x in src[author] if x['claim_id']==cid))
 for other in ['A097','A098']:
  for match in src[other]:
   if match['claim_id']==cid:
    assert all(match[k]==c[k] for k in ['version','exact_statement','hypotheses','statement_sha256'])
    for rec in match['review_records']:
     if rec not in c['review_records']:c['review_records'].append(rec)
 conditional=cid in ['A085-POSTQUERY-EXIT-DIRECT-SOURCE-RESET','A096-ARBITRARY-EXIT-FRONTIER-SAME-ANCESTOR']
 c['review_records'].append({'reviewer':'A099','run_id':R.name,'timestamp':stamp,
  'verdict':'HOLDS_CONDITIONAL_ON_EXACT_PRIOR_LIVE_SUBSTITUTIONS' if conditional else 'HOLDS_AT_EXACT_SUPPLIED_REFERENCE_SCOPE',
  'proof':str(R/'STAGE8_ADDITIONS.tex')+' '+label,
  'method':'Independent full analytic reconstruction; own prime-log disintegration and finite butterfly/physical-edge checker; no author checker imported',
  'validation':str(R/'out/EXACT_RECONSTRUCTION.json'),
  'scope':'No substantive repair; all complete terminals and old debits retained. Supplied-reference theorem only; not either integrated FEI audit. Point-family applications retain their named prior live substitutions.',
  'contributed_repair':False})
 c['status']='SOURCE_COMPLETE_CONDITIONAL_POINT_APPLICATION_INTEGRATED_AUDITS_OPEN' if conditional else 'SCOPED_INDEPENDENT_RECONSTRUCTIONS_HOLD_UNIVERSAL_SUPPLIER_OPEN'
 assert cid not in ids;claims.append(c);ids[cid]=c;new.append(c)
save(R/'CLAIMS.json',claims)
# Original author hash conventions are not silently normalized.
hashes=[]
for c in new+[our]:
 choices=[('raw',c['exact_statement'])]
 for name in ['statement','exact_statement']:
  for ascii_mode in [False,True]:
   for sep in [None,(',',':')]:choices.append((str((name,ascii_mode,sep)),json.dumps({name:c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,ensure_ascii=ascii_mode,separators=sep)))
 matches=[name for name,t in choices if hashlib.sha256(t.encode('utf-8')).hexdigest()==c['statement_sha256']]
 assert matches,c['claim_id']
 hashes.append({'claim_id':c['claim_id'],'sha256':c['statement_sha256'],'matching_original_conventions':matches})
save(R/'out/HASH_CONVENTIONS.json',hashes)

annex=(R/'STAGE8_ADDITIONS.tex').read_text(encoding='utf-8').replace('\tfrac',r'\tfrac')
(R/'STAGE8_ADDITIONS.tex').write_text(annex,encoding='utf-8')
tex=(OLD/'CANDIDATE_MANUSCRIPT.tex').read_text(encoding='utf-8').replace('assembly version 7','assembly version 8')
tex=tex.replace('Universal\nfresh-reference payment remains a separate open account.',
 'For every supplied Boolean source satisfying an occupied-support likelihood\nfloor, arbitrary repeated returns to its original marginal followed by\nfinal vacuum calibration are now paid with no reset-count surcharge.\nUniversal source pricing and changed nonempty-profile payment remain open.')
tex=tex.replace('below is an additional scoped argument, pending independent review.',
 'below has an A085 independent scoped acceptance; the full integrated\ncandidate still awaits both audits.')
tex=tex.replace('This closes only the specified exit-root transaction and its\nsource continuation. Arbitrary incoming profiles, a different\nprescribed reference after queries already executed in an exit,\nand a cheap initial reference for every Boolean source remain\nunpaid.',
 'This proposition closes the specified exit-root transaction and its\nsource continuation. Section~\\ref{sec:suppliedreturn} extends it to\narbitrary exit queries and repeated original-source canonical returns\nunder a supplied likelihood floor. Arbitrary incoming profiles, changed\nnonempty-profile references and a cheap initial source for every Boolean\nfunction remain unpaid.')
tex=tex.replace(r'\section{Dependencies, review and sources}',annex+'\n'+r'\section{Dependencies, review and sources}')
assert tex.count(r'\begin{conjecture}')==4
assert r'\input{' not in tex and r'\include{' not in tex
assert not re.search(r'Theorem~\\ref\{(?:lem|prop|cor):',tex)
labels=re.findall(r'\\label\{([^}]+)\}',tex);refs=re.findall(r'\\ref\{([^}]+)\}',tex)
assert len(labels)==len(set(labels)), 'duplicate labels'
assert not set(refs)-set(labels),set(refs)-set(labels)
assert all(ord(ch)>=32 or ch in '\r\n\t' for ch in tex)
for env in ['proof','lemma','theorem','proposition','conjecture']:
 assert tex.count('\\begin{'+env+'}')==tex.count('\\end{'+env+'}'),env
(R/'CANDIDATE_MANUSCRIPT.tex').write_text(tex,encoding='utf-8')

dag=rd(OLD/'out/PROOF_DEPENDENCIES.json');nodes={n['claim_id']:n for n in dag['nodes']}
for c,(_,_,label) in zip(new,new_specs):
 node={'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256'],
  'proof_dependencies':[d['claim_id'] for d in c['proof_dependencies']],'tex_label':label}
 assert node['claim_id'] not in nodes;dag['nodes'].append(node);nodes[node['claim_id']]=node
visited=set();active=set()
def walk(k):
 assert k in nodes,('missing dependency',k)
 assert k not in active,('cycle',k)
 if k in visited:return
 active.add(k)
 for dep in nodes[k]['proof_dependencies']:walk(dep)
 active.remove(k);visited.add(k)
for k in nodes:walk(k)
assert len(dag['open_leaves'])==4
dag['history_transfer_delta']='Supplied first-frontier and repeated ORIGINAL-source canonical returns closed at exact scope. Changed conditional nonempty profile and universal influence-priced supplier remain open.'
save(R/'out/PROOF_DEPENDENCIES.json',dag)
next_action='A097 with A050/A046: prescribe ONE changed conditional-nonempty reference after a paid non-point query; record old quarter/debits, incoming full Q, actual vacuum refund and both full terminals; pay its weighted shape-minus-KL bill from SAME unused original bank. A085 challenges; A094/A073 review.'
p=rd(R/'PROGRESS.json');p.update(deliverable_status='COMPLETE_SINGLE_SOURCE_PROTOCOL_AND_SCOPED_REVIEWS',
 mathematical_status='SUPPLIED_REFERENCE_CHAIN_RECONSTRUCTED_UNIVERSAL_FEI_OPEN',
 mathematical_delta=f"Assembled complete supplied-reference first-frontier and repeated-original-source-return proofs. Added independent exact-scope reconstructions, adopted A085 scoped review of A099 v7, preserved original versions/hashes. Arbitrary canonical exit trees fit SAME18 with>=7e_root, conditional on named live/source premises; narrower18e and61e/4 policy reserves retained. {primary['exact_assertions']} exact assertions PASS; {primary['positive_first']} positive first resets, {primary['old_nonconstant']} old nonconstant terminal occurrences. Changed nonempty profile and universal supplier remain OPEN; no universal constant improvement.",
 claims_created_or_changed=[{'claim_id':c['claim_id'],'version':c['version']} for c in new+[our]],
 source_artifacts=[str(R/f) for f in ['CANDIDATE_MANUSCRIPT.tex','STAGE8_ADDITIONS.tex','out/SOURCE_RECEIPTS.json','out/EXACT_RECONSTRUCTION.json','out/SHAPE_CONTROL.json','out/PROOF_DEPENDENCIES.json']],
 next_action=next_action,stagnant_substantive_attempts=0,
 blockers=['Universal influence-priced source/likelihood-floor supplier open','Changed conditional nonempty-profile payment from old bank open','Both integrated whole-candidate audits pending','Remote supervisor copy unverified'])
for c in new:
 if not any(d['claim_id']==c['claim_id'] for d in p['claim_versions_used']):p['claim_versions_used'].append({'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']})
p['next_consumers']=['A097','A096','A098','A050','A046','A085','A094','A073','B20']
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
report=f'''# A099 candidate assembly version8

## exact target, quantifiers, hypotheses and units

Assemble the strongest source-complete surviving FEI implications while retaining every universal leaf as a conjecture. For EVERY finite Boolean g, given auxiliary subprobability D with D(0)=m=P_g(0), finite c=CE(P_g,D), normalized complete S,Q with S>=D, Q(0)>=m and Q(T)>=gamma D(T) for nonempty T, 0<gamma<=1, reconstruct arbitrary finite adaptive query/reset-tree payment <=c+(1-m^2)log2(1/gamma). Resets use the SAME original S marginal and FINAL vacuum calibration. Physical reaches, ordinary influence and bits throughout. Changed nonempty profiles, raw uncalibrated returns and arbitrary source replacement are excluded. Full FEI OPEN; neither whole-candidate independent audit is supplied by this stage.

## sources actually read, revisions and theorem locators

At intake read current BOARD (03:54 UTC snapshot), old B20 STREAM_NOTES v2 and own STATUS. Followed the lead's one-source assembly direction; its old point-source task is already consumed. Execution-v2 read in full; deadline23 October14:49UTC is the current owner's extension of static protocol dates. Prior campaign registries, supplement, papers and runs were read in preceding stages and retained as prior source intake, not represented as fresh global audits. New complete mathematical reads: A09620261023T010221Z DERIVATION1--5/REPORT/CLAIMS; A09720261023T021120Z DERIVATION1--4/REPORT/CLAIMS; A08520261022T234859Z PROOF1--5/REPORT/CLAIMS; A09820261023T031803Z REVIEW1--6/REPORT/CLAIMS. Own v7 manuscript, claim ledger and DAG are the baseline. A050/A079 STATUS locates the next supplied non-point transaction without accepting those papers' full chains. out/SOURCE_RECEIPTS.json pins21 actual UTF-8 source files. No source or campaign tree is modified.

## complete derivation or exact first unsupported line

STAGE8_ADDITIONS.tex, integrated literally in CANDIDATE_MANUSCRIPT.tex, supplies complete proofs: subprobability occupied-fiber disintegration; first-frontier vacuum AM-GM bound; finite physical total variance; calibration absorption with possibly NEGATIVE affine vacuum coefficient; constant/zero-normalizer support guards; first-reset antichain pruning and continuation. Its general theorem has no point-source hypothesis. Every later original-source calibrated return is current-reference calibration and costs minus binary KL, with ZERO reset-count/depth surcharge. m is already squared mean, so1-m^2 means1-(E g)^4.

The annex independently reconstructs A085's direct-source one-inside-query policy, including a1 constant boundary and dummy/control full-terminal branches, and A096's occupied-support floor/13e original-bank application. Same original K=2C0+10 (18 structurally) retains>=7e_root for arbitrary exit trees and repeated canonical returns, CONDITIONAL on exact previous live/source claims. Prior immediate-source18e and one-query61e/4 reserves refer to narrower policies, not corrected constants. A085's scoped HOLDS review of our v7 exit conversion is adopted without rewriting its statement/hash. A098's independent reviews and our reconstructions apply only at the exact supplied-reference scope, not universal source payment.

First unsupported universal line: construct an influence-priced useful source/likelihood floor for EVERY Boolean function, or pay an ACTUAL changed conditional-nonempty profile from the named unused original bank after a paid non-point query. The exact signed liability is (1-z)E_(P+)log2(Q+/R+) - D_Ber(z||Q(0)); original-source absorption cancels only the unchanged-profile case. Both full terminals, all ghost mass, actual normalizers, old quarter booking and every erasure remain mandatory. All FOUR universal conjectures are preserved verbatim. No new broad candidate or duplicate ID is created; the shape identity reuses the existing signed-reset interface.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec precedes computation. Original pilot:6879 assertions PASS but zero positive first resets. The explicit V2 amendment changed ONLY incoming Q residual placement from uniform to the true conditional nonempty spectrum before any primary evaluation; dimensions, case counts, policies and caps unchanged. Original pilot bytes retained. Revised pilot command: `python -B -X utf8 code/check.py --pilot`; {pilot['exact_assertions']} checks,16 labelled two-bit functions,64 source/floor instances,192 policies PASS in{pilot['seconds']:.3f}s. Revised pilot still has no positive first resets at n2; only primary provides that failure-control coverage.

Primary: `python -B -X utf8 code/check.py`; ALL256 labelled three-bit functions,1024 source/floor instances,3072 declared deterministic adaptive policies; {primary['exact_assertions']} exact assertions PASS in{primary['seconds']:.3f}s. It exercises{primary['positive_first']} strictly positive FIRST resets,{primary['later_returns']} later returns,{primary['old_nonconstant']} old nonconstant terminal occurrences and{primary['queries']} actual query transactions. These are occurrences, not distinct Boolean counterexamples. No symmetry reduction or claim to enumerate all adaptive trees. Analytic proofs supply all dimensions and arbitrary finite histories.

Independent checker imports NO author checker. Integer butterfly Walsh spectra, separately counted physical pivotal edges, exact Fraction complete laws/marginals, exact prime-log cancellations and18-term rational atanh intervals check normalization, support, subprobability/normalized disintegration, refunds, all complete tree bills and later-law equality. After binary range reduction z=(x-1)/(x+1) is in[0,1/3]; ln(x)=2sum_(k<18)z^(2k+1)/(2k+1) plus remainder in[0,2z^37/(37(1-z^2))]; log2 division is outward by positive ln2 bounds. No floating sign tests. A separate actual parity3 query leaves two nonconstant parity2 children: changing occupied reference probability1/2 to1/3 costs log2(3)-1>1/2, certified by rational interval and independently by9>8. This falsifies only free arbitrary shape change, not FEI.

Estimated checker memory120MB, observed peak unmeasured; frozen55s cap met, no >300MB job, GPU, heavy search, compiler or detached work. Current shared compute snapshot reports memory distress and926MB available; do not stop others' work. Further execution is lightweight packaging only. No Lean or PDF compilation is claimed. This is source-complete analytic proof with exact finite validation, not a formal certificate. No compiler source is presented as executed.

## proof dependencies and changed downstream conclusions

Original claim versions, statements, hypotheses and hashes are preserved. CLAIМS has22 records; DAG has40 nodes and four unchanged universal leaves. Exact chain: entropy/KL disintegration and total variance -> A096 first-frontier -> A097 canonical-return extension. The point application additionally uses exact A097 source-bank, A096 active and A097/A073 nonactive substitutions already reconstructed in v7, plus A085 occupied floor. These dependencies are checked acyclic. A099 independently reconstructs both supplied-reference theorems without repair; A098's existing exact-scope review is preserved. No status infers either complete FEI-chain audit. The previously requested post-query exit and repeated canonical-return liabilities are retired only at their delivered scopes; actual changed nonempty-profile pricing stays OPEN. Universal constant improvement:zero.

## one next mathematical action and independent reviewer

{next_action} A098/A099 consume this concrete signed transaction after review, rather than another vacuum-only return identity or enlarged point-source census. No external message or supervisor adoption is asserted.

## actual persistence receipts or precise save blocker

The four exact-schema protocol files, standalone CANDIDATE_MANUSCRIPT.tex, STAGE8_ADDITIONS.tex, code and exact outputs are local. PROGRESS/PACKET_DELTA are byte-identical. Final schema/hash/DAG/label/readback results are out/FINAL_VALIDATION.json; actual byte receipts are out/PERSISTENCE_RECEIPTS.json. Rolling STATUS is two lines; WORKLOG/LEARNED append dated results. No local save blocker, git, mail, intentional brain write, other-agent mutation or detached research job. No PDF/rendering acceptance is claimed. Supervisor copying, canonical adoption and remote mirrors remain UNVERIFIED. Brain self-care is degraded/unverified: wake rendering failed and the owner-model/state-of-mind sources are stale; personalization continuity remains affected, and those notes are not proof premises.

## Universal bridge

C024 history transfer feeding C019/C018 advances to a single source-complete assembly for arbitrary repeated SAME-original-source canonical resets under the supplied likelihood floor, at ZERO additional reset cost and with every old debit and full terminal retained. Its exact point-family corollary keeps SAME18 and>=7e_root for the broader policy; no universal constant improves. The original-source return identity is closed at its scoped theorem level, while universal source/likelihood pricing, actual changed nonempty-profile payment and both full-candidate audits remain open. NEXT prices the missing shape-minus-vacuum term on an already paid non-point source from its diminished original owner: that is the precise hereditary liability this universal bridge still lacks, rather than another isolated class entropy result.
'''.replace('CLAIМS','CLAIMS')
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text(f'STATE: A099 v8 source/protocol saved: complete supplied-floor -> arbitrary repeated original-source canonical-return chain reconstructed; {primary["exact_assertions"]:,} exact checks PASS; original hashes/scoped reviews retained; full FEI OPEN.\nNEXT: A097/A050/A046 price ONE genuine nonempty-profile change after paid non-point query with SAME old debits/both full terminals; A085 challenges, A094/A073 review; universal supplier and two integrated audits open.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+f': v8 finalized: supplied-reference first-frontier and arbitrary original-source return chains independently reconstructed and assembled, A085 v7 scoped review adopted. {primary["exact_assertions"]} exact checks PASS,192 positive first resets and1024 old nonconstant terminal occurrences. Revised incoming-profile pilot explicitly frozen; no count aggregation. Actual nonempty-profile toll remains unpaid; no new broad candidate. No compiler/heavy/background work; low-memory snapshot reported; supervisor mirror unverified.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+': Supplied arbitrary-Boolean transfer is now source-complete: subprobability D=m delta0+N, normalized S>=D, incoming Q>=m delta0+gamma N pays arbitrary first frontier by c+(1-m^2)log2(1/gamma). Calibration absorption Cal(M Cal(S,z),w)=Cal(MS,w) retains ghosts and allows negative affine vacuum coefficient; constant paths use explicit delta0. After first reset every SAME-original-source final-calibrated return is minus binary KL, so no reset/depth tax. This retires only canonical-return liability, not actual changed nonempty profile. The latter costs (1-z)E_(P+)log(Q+/R+) minus actual vacuum KL and must be paid from SAME diminished owner. A096/A097 exact hashes unchanged; A098 and A099 reviews do not accept universal source construction or full FEI integration. Distinct special-policy reserves18e,61e/4,7e all use same K=18.\n')
protocol=rd(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
required=protocol['required_per_run'];assert all(set(c)==set(required['claim_fields']) for c in claims)
assert set(p)=={x.split(' (')[0] for x in required['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert p['packet_ids']==['A099'] and len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all('## '+x in report for x in required['report_fields'])
assert report.rsplit('## Universal bridge',1)[1].strip()
assert len(claims)==22 and len(nodes)==40
save(R/'out/FINAL_VALIDATION.json',{'status':'PASS','claims':len(claims),'DAG_nodes':len(nodes),'universal_conjectures':4,
 'exact_assertions':primary['exact_assertions'],'labels':len(labels),'all_references_resolved':True,
 'new_broad_candidates':0,'full_FEI':'OPEN','whole_candidate_independent_audits':'BOTH_PENDING','formal_certificate':False,
 'PDF':'NOT_BUILT','remote_mirror':'UNVERIFIED','brain_selfcare':'DEGRADED_UNVERIFIED'})
receipts=[]
for q in list(R.rglob('*'))+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']:
 if q.is_file() and q.name!='PERSISTENCE_RECEIPTS.json':
  raw=q.read_bytes();assert len(raw)<20_000_000
  receipts.append({'path':str(q),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save(R/'out/PERSISTENCE_RECEIPTS.json',{'at':stamp,'artifacts':receipts,'supervisor_remote_copy':'UNVERIFIED'})
for rec in receipts:assert hashlib.sha256(Path(rec['path']).read_bytes()).hexdigest()==rec['sha256']
print(json.dumps({'status':'PASS','claims':len(claims),'DAG_nodes':len(nodes),'exact_assertions':primary['exact_assertions'],'saved_byte_readbacks':len(receipts),'full_FEI':'OPEN'}))
