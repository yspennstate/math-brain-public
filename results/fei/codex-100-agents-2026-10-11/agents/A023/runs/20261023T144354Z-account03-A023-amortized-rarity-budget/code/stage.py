"""A023 final source-admission diagnostic; all research writes stay in A023."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,hashlib,datetime,time,importlib.util
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
OLD=ROOT/'runs/20261023T122018Z-account03-A023-amortized-rarity-budget'
(RUN/'out').mkdir(parents=True,exist_ok=True)
def read(p):return Path(p).read_text(encoding='utf-8')
def write(p,t):Path(p).write_text(t,encoding='utf-8',newline='\n')
def save(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
proof='''# Influence-priced smoothing, and the unpaid initial entropy

All logs are base2. For EVERY Boolean g on any finite uniform cube, write P_g for its squared Fourier law, J=I(g), and u for the uniform law on frequency subsets. If J>0 put epsilon=min(1/2,J/4) and q_g=(1-epsilon)P_g+epsilon*u. If J=0 put q_g=P_g. Then

0<=K_g=KL(P_g||q_g)<=J,
H(g)<=CE(P_g,q_g)<=H(g)+I(g).

Proof: q_g>=(1-epsilon)P_g, so K_g<=-log2(1-epsilon). For0<J<=2, integrate1/(1-t)<=2 on[0,epsilon], obtaining K_g<=2epsilon/ln2<J because ln2>1/2. The latter follows by integrating1/t>1/2 on[1,2]. For J>=2, K_g<=1<=J. For J0 the assertion is exact. Positive J gives a full-support reference; constants use their exact point law. No fixed positive smoothing floor is admitted at constants.

## Persistent first-mark conversion through arbitrary adaptive DATA histories

Let a finite physical restriction tree query previously unqueried coordinates of arbitrary g, and stop at an arbitrary adapted frontier. Let F be an event first declared on a prefix-free set of tree nodes and then retained on descendants: a path marks at most once. Let q_old,h be ANY already supplied reference, finite on the support of P_h. On marked histories prescribe the actual CURRENT influence-tuned q_h above, including after each subsequent data query. Off marked histories keep q_old. Both full KLs remain in

D_h=K_new,h-K_old,h=CE_new,h-CE_old,h<=I(g_h).

At first marking charge D_h. On each realized later edge charge D_child-D_parent; these realized differences telescope PATHWISE to terminal D, with no clipping and no fresh descendant allowance. Their CONDITIONAL EXPECTATIONS are E[D_child|h]-D_h; those expected node charges telescope only AFTER reach weighting. A conditional average increment is not claimed to telescope on an individual realized path. Therefore

E[1_F D_terminal]<=E[1_F I(g_terminal)]<=I(g).

The last inequality is an actual physical influence ledger: I(g_h)=Inf_i(g_h)+(I(g_h|i0)+I(g_h|i1))/2. Multiplying by reaches and summing gives E I(terminal)=I(g)-sum_nodes reach*Inf_query. The marked part is no greater because influence is nonnegative. Thus one ORIGINAL extra coefficient of I(g) pays every such terminal conversion from any supplied OLD reference. This is a universal CONVERSION theorem. It does not supply the old cross-entropy or create unused credit inside an already exhausted old4I account. A purported unchanged4I extension would still have to exhibit its unused original margin.

## Fixed half-smoothing cannot be the universal initial supplier

This corroborates the fixed-mixture obstruction already noted by A029 on the current BOARD; it is not claimed as a new general no-go. For the actual Boolean point-defect family g_n=1 except at one vertex, delta=2^-n, n>=3,

P(empty)=(1-2delta)^2>=9/16; I(g_n)=2n delta.

For q_half=(P+u)/2, q_half(empty)<=(1+delta)/2<=9/16. Hence CE(P,q_half)>=(9/16)log2(16/9)>9/32, since(16/9)^2>2. Thus CE(P,q_half)/I(g_n)>9*2^n/(64n), unbounded. This is an initial-reference counterexample, NOT an FEI counterexample. In fact its entropy/influence is bounded; no such conclusion about FEI follows from the inflated reference cost.

The influence-tuned rule removes this artificial constant floor: K<=I even on this low-influence family. Its initial price remains H+K, so it does not solve the source problem.

## Exact universal bridge and first unsupported line

Existence of an absolute K with CE(P_g,q_g)<=K I(g) for EVERY Boolean g is EQUIVALENT to full FEI, with constants shifting by at most1: CE>=H gives FEI(K); FEI(C) gives CE<=H+I<=(C+1)I. This is an equivalence, not a new sufficient hypothesis asserted true. The first unsupported universal line is H(g)<=C I(g), or a NONCIRCULAR structural construction paying the equivalent initial CE. Influence-priced reset overhead alone cannot prove it. The new result prices conversion without a unit floor and specifies exactly what initial payment is still missing.

Compared with stage21, its bound>153/256 is neither changed nor generalized for free: that was a particular original4I account. This stage supplies a distinct generic one-additional-I conversion tariff. The original stage21 theorem and negative quarter-branch remain untouched. Independent-person review is pending.
'''
write(RUN/'PROOF.md',proof)
spec={'helper_version':'stage22-v1; exact FWHT versus direct character sums; prime-log helper pinned 20261014 check_block.py','family':'all Boolean tables on n0..3; current influence-tuned smoothing and every physical coordinate query','domain':'pilot n0..2 (22 tables), full n0..3 (278 tables); no dimension escalation; no search starts after2026-10-23T14:49:00Z','case_count':{'pilot':22,'full':278,'full_query_nodes':804},'symmetry':'none','arithmetic':'rational spectra/influences and prime-log vectors, rigorously enclosed signs; separate direct character reconstruction','memory_estimate_mb':100,'max_runtime_seconds':60,'deadline_behavior':'save explicit SKIPPED_CAMPAIGN_END or INCOMPLETE without extrapolating checks; analytic proof persists regardless'}
save(RUN/'out/FROZEN_SPEC.json',spec)
start=time.perf_counter();deadline=datetime.datetime(2026,10,23,14,49,tzinfo=datetime.timezone.utc)
hp=ROOT/'runs/20261014T022245Z-account05-A023-amortized-rarity-budget/code/check_block.py'
sp=importlib.util.spec_from_file_location('exact_logs',hp);h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
checks=0;rows=[];query_nodes=0
def ck(ok):
 global checks
 assert ok
 checks+=1
 assert time.perf_counter()-start<60
def fw(t):
 a=list(t);k=1
 while k<len(a):
  for j in range(0,len(a),2*k):
   for i in range(j,j+k):a[i],a[i+k]=a[i]+a[i+k],a[i]-a[i+k]
  k*=2
 return a
def profile(t):
 N=len(t);n=N.bit_length()-1;a=fw(t);P={s:Q(v*v,N*N) for s,v in enumerate(a) if v}
 direct={}
 for s in range(N):
  z=sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t))
  if z:direct[s]=Q(z*z,N*N)
 ck(P==direct and sum(P.values())==1)
 influences=[Q(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range(n)];J=sum(influences,Q(0));ck(J==sum((p*s.bit_count() for s,p in P.items()),Q(0)))
 eps=min(Q(1,2),J/4);C={};H={}
 for s,p in P.items():
  q=(1-eps)*p+eps/Q(N);h.lg(C,q,-p);h.lg(H,p,-p)
 K=h.add((1,C),(-1,H));ck(h.sign(K)>=0);ck(h.sign(h.add((1,h.rational(J)),(-1,K)))>=0)
 return J,influences,K
status='SKIPPED_CAMPAIGN_END'
if datetime.datetime.now(datetime.timezone.utc)<deadline:
 status='PASS'
 for n in range(4):
  for truth in range(1<<(1<<n)):
   if datetime.datetime.now(datetime.timezone.utc)>=deadline:status='INCOMPLETE_DEADLINE';break
   t=[1-2*((truth>>x)&1) for x in range(1<<n)];J,ii,K=profile(t)
   for i in range(n):
    children=[]
    for v in [0,1]:children.append(profile([t[(x% (1<<i))+v*(1<<i)+(x//(1<<i))*(1<<(i+1))] for x in range(1<<(n-1))]))
    ck(J-(children[0][0]+children[1][0])/2==ii[i]);query_nodes+=1
   rows.append({'n':n,'truth':truth,'I':str(J),'KL':{str(p):str(c) for p,c in K.items() if c}})
  if n==2:save(RUN/'out/pilot_validation.json',{'status':'PASS' if len(rows)==22 else status,'tables':len(rows),'checks':checks,'elapsed_seconds':time.perf_counter()-start})
  if status!='PASS':break
 if status=='PASS':ck(len(rows)==278 and query_nodes==804)
validation={'status':status,'tables':len(rows),'query_nodes':query_nodes,'checks':checks,'elapsed_seconds':time.perf_counter()-start,'all_dimensional_proof':'PROOF.md; not extrapolated from finite checks','independent_person_review':'PENDING'}
save(RUN/'out/validation.json',validation);save(RUN/'out/rows.json',rows);save(RUN/'out/sign_certificates.json',list(h.SIGNS.values()))
oldclaims=json.loads(read(OLD/'CLAIMS.json'));c=oldclaims[0];assert c['version']==9
c['version']=10
c['exact_statement']+=' VERSION10 UNIVERSAL CONVERSION DIAGNOSTIC: For EVERY Boolean g, influence-tuned q=(1-epsilon)P_g+epsilon*uniform with epsilon=min(1/2,I(g)/4), or q=P_g when I=0, satisfies0<=KL(P_g||q)<=I(g). On ANY finite adaptive DATA restriction tree with one persistent first-mark event per path and ANY supplied old reference, full signed conversion D=Knew-Kold at first marking plus descendant signed increments telescopes to terminal D; expected total conversion<=I(g_root). This costs one additional ORIGINAL influence coefficient and does not assert it is unused inside the prior4I bank. Fixed half-smoothing initial CE/I is unbounded on actual point defects, corroborating current A029 fixed-mixture obstruction. Initial CE for the tuned rule is between H and H+I, so a universal O(I) initial supplier for this rule is EXACTLY FEI-equivalent up to one constant unit; it is NOT established. All previous scoped statements remain unchanged.'
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest();c['hypotheses'].append('Version10 conversion only: arbitrary Boolean source, finite adaptive physical DATA tree, old reference already supplied, one persistent first mark per path; extra ORIGINAL coefficient I pays conversion and is not reused from old4I.')
c['proof_source']=str(RUN/'PROOF.md');c['proof_dependencies']=[{'claim_id':c['claim_id'],'version':9,'source':str(OLD/'CLAIMS.json'),'status':'Earlier scopes preserved only; new elementary conversion proof is self-contained.'}];c['review_records']=[];c['status']='AUTHOR_PROOF_INDEPENDENT_REVIEW_PENDING';c['supersedes']=[{'claim_id':c['claim_id'],'version':9,'scope':'Preserve earlier scopes; add universal conversion tariff and exact remaining-admission equivalence.'}];c['first_unproved_line']=None
save(RUN/'CLAIMS.json',oldclaims)
nextaction='Produce a noncircular influence-priced INITIAL source reference for arbitrary indecomposable Boolean g. Influence-tuned signed reset cost is now <=one ORIGINAL I; do not mistake CE=H+O(I) for the unpaid initial O(I) supplier. A028/A029/A030/A087/A094 audit the universal conversion tariff and supplier equivalence.'
pr=json.loads(read(OLD/'PROGRESS.json'));pr.update(run_id=RUN.name,attempt_id='A023-22-influence-tuned-first-mark-and-initial-supplier-barrier',method='Influence-dependent smoothing; persistent signed full-KL difference; physical influence supermartingale; explicit initial-admission equivalence',mathematical_delta='Universal conversion overhead <=one additional ORIGINAL influence coefficient, including arbitrary adaptive DATA descendants; fixed unit smoothing floor removed. Exact initial tuned-reference O(I) price is FEI-equivalent and remains unpaid. Prior >153/256 original4I theorem unchanged. Finite validation:'+status+'.',mathematical_status='AUTHOR_PROOF; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',claim_versions_used=[{'claim_id':c['claim_id'],'version':9,'source':str(OLD/'CLAIMS.json'),'status':'Earlier scopes retained, not used to supply an arbitrary new source.'}],claims_created_or_changed=[{'claim_id':c['claim_id'],'version':10}],source_artifacts=['REPORT.md','PROOF.md','CLAIMS.json','code/stage.py','out/FROZEN_SPEC.json','out/validation.json','out/rows.json','out/sign_certificates.json','out/PERSISTENCE_RECEIPTS.json'],next_action=nextaction,blockers=['Initial arbitrary-source cross-entropy O(I) supplier remains FEI-equivalent and unproved.','Independent-person review and supervisor mirror/adoption unverified.','Fresh brain wake failed attachment write lock; personal context freshness unverified.'],stagnant_substantive_attempts=0)
save(RUN/'PROGRESS.json',pr);write(RUN/'PACKET_DELTA.json',read(RUN/'PROGRESS.json'))
report=f'''# exact target, quantifiers, hypotheses and units

EVERY Boolean g, any finite adaptive DATA tree, one persistent first-mark event per path, any already supplied old reference. New current reference uses epsilon=min(1/2,I(g_h)/4). Full signed conversion overhead is at most ONE additional ORIGINAL I(g), not a renewed per-descendant donor. Bits throughout. This does not establish initial CE=O(I), nor reuse the old4I margin. Stage21's scoped bank>153/256 is unchanged.

# sources actually read, revisions and theorem locators

Read BOARD dated2026-10-23 14:39UTC, B05 STREAM_NOTES v2, own STATUS and prior stage21 results. The board's A029 fixed-mixture obstruction is recognized as prior context; the point-defect corroboration here is not a new no-go claim. A028/A030 now also identify original source admission as unpaid. New proof uses only Gibbs, an elementary logarithm integral, and the physical influence restriction identity. The old A021 R-sign concern is not used: no A021 remainder sign enters this proof. Source trees remain read-only; the stream lead's retired local-price no-go is not re-proved.

# complete derivation or exact first unsupported line

PROOF.md contains the all-dimensional proof. Since q>=(1-epsilon)P, K<=-log2(1-epsilon)<=I. Full D=Knew-Kold<=I_current. First-mark charge and signed descendant increments telescope to terminal D. Exact physical influence partition gives E I_terminal<=I_root, so total conversion<=I_root. For point defects fixed-half CE>9/32 while I=2n2^-n, proving the artificial initial unit floor fails. Influence-tuned CE lies between H and H+I; its initial absolute influence price is FEI-equivalent up to1. FIRST UNSUPPORTED universal line remains the noncircular initial supplier, not the conversion tariff. Both full KLs and every negative increment are retained.

# executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes checks: pilot22 tables(n0..2), full278(n0..3),804 physical query nodes, exact rational arithmetic and certified prime-log signs, FWHT versus direct characters,100MB estimate and60s cap. No dimension escalation or jobs after campaign cutoff. Actual result:{status}; tables{len(rows)},query nodes{query_nodes},assertions{checks},elapsed{validation['elapsed_seconds']:.6f}s. If SKIPPED/INCOMPLETE, no exhaustive validation is claimed: the analytic proof is independent of enumeration. Command: python -X utf8 runs\\{RUN.name}\\code\\stage.py. No job exceeds the300MB gate; memory estimate is not a measured peak. The proof's universal scope comes from derivation, not these finite cases. Same-author independent representation is not independent-person review.

# proof dependencies and changed downstream conclusions

Same candidate version9->10, preserving earlier scopes. The new universal conversion proof is self-contained and does not import an initial source from version9. It replaces the unit reset floor by an influence-sized floor, at the explicit price of ONE additional original coefficient. It cannot be inserted into a depleted same4I account without an unused payer. Existing prior >153/256 class theorem is neither withdrawn nor silently strengthened. Independent review remains pending; no full FEI theorem or actual unbounded H/I family is claimed.

# one next mathematical action and independent reviewer

{nextaction}

# actual persistence receipts or precise save blocker

Four protocol files, proof, frozen spec, code and actual validation outputs saved locally. Final schema, statement digest, compatibility bytes, two-line STATUS and artifact hashes are checked below. Supervisor publication/mirror and independent-person adoption remain unverified. Fresh brain wake exited1 with attachment-write-lock timeout and stale owner-model/state/dream notes; brain self-care and personal-context freshness remain degraded/unverified. No shared service, governor or lock was altered; no git, messaging or other-agent writes were performed.

**Universal bridge:** This advances C019/C024 by proving an all-source first-mark conversion tariff<=one ORIGINAL I through arbitrary adaptive DATA histories, with current influence-dependent smoothing and full signed old/new KLs. It removes the fixed unit floor while preserving one-use ownership; the prior exact >153/256 class account is unchanged. The initial cross-entropy is still H+O(I), so its absolute initial supplier is precisely FEI-equivalent and unpaid. NEXT targets that noncircular original admission directly, rather than repeating descendant conversions or adding another isolated finite class. Full FEI remains OPEN.
'''
write(RUN/'REPORT.md',report)
write(ROOT/'STATUS.md','STATE: A023 stage22 author proof: universal influence-tuned signed first-mark conversion<=one additional ORIGINAL I, all adaptive DATA descendants; fixed unit floor removed; initial supplier remains FEI-equivalent/unpaid; stage21 >153/256 unchanged; review/FEI OPEN.\nNEXT: Noncircular influence-priced INITIAL reference for arbitrary core; CE=H+O(I) is not payment. A028/A029/A030/A087/A094 review universal conversion tariff; supervisor publication unverified.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{stamp} stage22: arbitrary-source influence-tuned smoothing epsilon=min(1/2,I/4) has full KL<=I. Persistent first-mark signed conversion on ANY finite adaptive DATA tree costs<=one extra ORIGINAL I via actual influence supermartingale. NOT a free same4I addition. Fixed-half point-defect barrier corroborates A029; initial tuned CE price is FEI-equivalent and unpaid. Exact finite validation {status}: {len(rows)} tables/{checks} checks. Prior bank>153/256 unchanged. Wake degraded: attachment write lock timeout, stale personal notes.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\n2026-10-23 stage22: q=(1-epsilon)P+epsilon*u with epsilon=min(1/2,I/4), q=P when I0, gives0<=KL<=I. For any persistent first-mark event and arbitrary finite adaptive DATA frontier, full D=Knew-Kold signed telescope has expected cost<=I_root, using E I_leaf<=I_root. This is one EXTRA original coefficient, not unused same4I credit. Initial CE lies in[H,H+I], hence its O(I) supplier is FEI-equivalent. Fixed-half CE has artificial unit floor: actual n-bit point defects have CE>9/32,I=2n2^-n. Full FEI remains unpaid; do not turn a priced conversion into initial admission.\n')
fields=json.loads(read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')))['required_per_run']
assert set(c)==set(fields['claim_fields']);assert set(pr)=={s.split(' (')[0] for s in fields['progress_fields']}
assert all('# '+s in report for s in fields['report_fields']);assert len(read(ROOT/'STATUS.md').splitlines())==2
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json'];assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt={'status':'PASS_LOCAL','files':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],'rolling':[{'path':str(ROOT/n),'sha256':hashlib.sha256((ROOT/n).read_bytes()).hexdigest()} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],'review':'PENDING','mirror':'UNVERIFIED'}
save(RUN/'out/PERSISTENCE_RECEIPTS.json',receipt)
for a in receipt['files']:assert hashlib.sha256((RUN/a['path']).read_bytes()).hexdigest()==a['sha256']
print(json.dumps({'status':'PASS_LOCAL_ARTIFACT','claim_version':10,'validation':validation,'files_hash_checked':len(files),'full_FEI':'OPEN','review':'PENDING','mirror':'UNVERIFIED'}))
