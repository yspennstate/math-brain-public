"""One frozen exact Boolean counterexample to necessity of channel admission."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime,time
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; root=A.parents[1]
(R/'out').mkdir(parents=True,exist_ok=True)
def put(p,s): p.write_text(s,encoding='utf-8',newline='')
def dump(p,x):put(p,json.dumps(x,indent=2)+'\n')
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
dump(R/'out/FROZEN_SPEC.json',dict(helper_version='stage.py exact direct-character and butterfly Walsh, v1',family='a=pointdefect2; G=z,H=1; dummy DATA d; exact controller reference, source R=(1/2,1/2) on z with d empty',domain='one actual Boolean function on four variables; query dummy d then prescribe sector odds1/2 on z row, true odds3/4 on empty row',case_count=1,symmetry='none',arithmetic='Fraction and prime-log vectors; strict signs by 1<log2(3)<2',memory_estimate_MB=40,max_runtime_seconds=60,automatic_escalation=False))
start=time.monotonic(); receipts=[]; board=''
for p in (root/'BOARD.md',root/'claude/B06/STREAM_NOTES.md',A/'STATUS.md',root/'agents/A029/LEARNED.md'):
 s=p.read_text(encoding='utf-8-sig');receipts.append(dict(path=str(p),sha256=sha(p)))
 if p.name=='BOARD.md':board=s
dump(R/'out/context_receipts.json',receipts)
put(R/'out/board_frontier.txt','\n'.join(x for x in board.splitlines() if any(y in x for y in ('- A028 ','- A029 ','- A056 ','- A096 ','- A097 '))))
def fw(t):
 v=list(map(F,t));step=1
 while step<len(v):
  for k in range(0,len(v),2*step):
   for j in range(k,k+step):x,y=v[j],v[j+step];v[j],v[j+step]=x+y,x-y
  step*=2
 return tuple(x/len(v) for x in v)
def direct(t):return tuple(sum(F(t[x])*(-1 if (x&s).bit_count()%2 else 1) for x in range(len(t)))/len(t) for s in range(len(t)))
def fac(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def add(*vs):
 d={}
 for v in vs:
  for p,x in v.items():d[p]=d.get(p,F())+x
 return {p:x for p,x in d.items() if x}
def scale(v,x):return {p:x*z for p,z in v.items() if x*z}
def lg(x):return add({p:F(v) for p,v in fac(x.numerator).items()},{p:-F(v) for p,v in fac(x.denominator).items()})
def KL(p,q):
 assert sum(p)==sum(q)==1
 return add(*(scale(lg(x/y),x) for x,y in zip(p,q) if x))
def enc(v):return {str(p):str(x) for p,x in v.items()}
a=(-1,1,1,1)
f=tuple((1 if not(x&4) else -1) if a[x&3]==1 else 1 for x in range(16))
w=fw(f);assert w==direct(f);P=tuple(x*x for x in w)
assert sum(P)==1 and all(P[s]==0 for s in range(8,16))
assert tuple(P[:8])==(F(1,16),)*4+(F(9,16),)+(F(1,16),)*3
H=add(*(scale(lg(x),-x) for x in P if x));I=sum(F(s.bit_count())*x for s,x in enumerate(P))
assert H=={2:F(4),3:-F(9,8)} and I==F(5,4)
Q0=(F(1,8),)*4+(F(1,8),F(1,8),F(1,8),F(1,8))+(F(0),)*8
# Q0 is v8 true-odds reference: empty-data row all1/8; z row empty3/8, others1/24.
Q0=(F(1,8),)*4+(F(3,8),)+(F(1,24),)*3+(F(0),)*8
Q1=(F(1,8),)*4+(F(1,4),)+(F(1,12),)*3+(F(0),)*8
D0=KL(P,Q0);D1=KL(P,Q1);C=add(D1,scale(D0,-1));T={2:F(1)}
assert D0=={2:-F(1),3:F(3,4)}
assert D1=={2:-F(7,4),3:F(21,16)}
assert C=={2:-F(3,4),3:F(9,16)}
Z=add(T,scale(D0,-1));S=add(T,scale(D1,-1))
assert S=={2:F(11,4),3:-F(21,16)}
# Exact lower bound: log2(3)<2, hence S>11/4-42/16=1/8.
assert F(11,4)-2*F(21,16)==F(1,8) and 3<4
# Source-G posteriors on z row: alpha=1, rho=3/4, b=1/4.
lo,hi=F(3,16),F(7,16);ell=F(1,2)
assert ell>hi
assert KL((F(1,4),F(3,4)),(F(1,2),F(1,2)))=={2:-F(1),3:F(3,4)}
assert add(C,S)==Z
for branch in (0,1):
 child=tuple(f[x|(branch<<3)] for x in range(8));pc=tuple(x*x for x in direct(child))
 assert pc==P[:8] and KL(pc,Q1[:8])==D1
# Dummy query has zero true entropy loss and zero output E/O; BOTH children have full CE H+D1.
assert add(H,D1,T,scale(D1,-1))==add(H,T)
# Original real rate4 and an explicitly booked old debit1/8 still admit H+T.
U=4*I;old=F(1,8);reserve=add({2:U-old},scale(add(H,T),-1))
assert reserve=={2:-F(1,8),3:F(9,8)}
assert -F(1,8)+F(9,8)==1 and 3>2
result=dict(status='PASS',cases=1,truth=list(f),squared_spectrum=list(map(str,P)),H=enc(H),I=str(I),T=enc(T),original_D=enc(D0),target_D=enc(D1),row_cost=enc(C),original_Z=enc(Z),remaining_S=enc(S),strict_slack_certificate='S=11/4-(21/16)log2(3)>1/8 since3<4',admissible_channel_interval=list(map(str,(lo,hi))),prescribed_odds=str(ell),outside_image=True,full_dummy_children_checked=2,original_U=str(U),old_debit=str(old),original_admission_reserve=enc(reserve),reserve_certificate='reserve=-1/8+(9/8)log2(3)>1 since3>2',seconds=time.monotonic()-start)
dump(R/'out/exact_certificate.json',result)
proof='''# Exact admission is broader than the common-channel image

All quantities are in bits. Retain v9 source/controller references and their OWN physical inheritance, all old debits, output erasure/outcome refunds, and both complete child/terminal bills. In binary v8 notation let T=Wdata+gamma Da, Z=Wdata-D(q||r), Cvac=D(Bern(V)||Bern(beta)). For ANY prescribed sector odds ell_t with finite true-law KL, leaving data marginal r and inherited nonempty shape B fixed, chain rule gives

    Dstar=D8+C, C=sum_t q_t D(Bern(b_t)||Bern(ell_t)),
    T-Dstar=Z+gamma Cvac-C.

Consequently exact nodewise admission into the SAME account is equivalent to C<=Z+gamma Cvac. The v9 common-channel construction proves the stronger sufficient condition C<=Z, but its posterior image is NOT a necessary payment condition. If every target along a finite adaptive mixed tree satisfies this exact nodewise admission, the unchanged physical T-supermartingale telescopes to full path plus terminal CE<=Hroot+Troot. This is a supplied-account extension, not an initial influence-price theorem or a positive-part reset bound.

Actual Boolean strict separation: a(y1,y2)=-1 only at00; G(z,d)=z,H(z,d)=1; f=(1-c)G+cH, c=(1-a)/2. Original Ra=Pa is uniform on four control sets; Rg=Rh is uniform on z's two sets with zero dummy-d mass. Thus Da=0,T=W=1. The actual spectrum is 1/16 on each of four empty-data controller rows, 9/16 on (empty,z), 1/16 on the other three z rows, and zero on sets containing d. H=4-(9/8)log2(3), I=5/4. Query dummy DATA d first: zero entropy and output E/O costs; the original source/controller references, actual source branch normalizers1/2, and both full child spectra are unchanged.

Now prescribe ell=1/2 on the z row, retaining true ell=3/4 on the empty-data row and the original true nonempty shape. On z, alpha=1,rho=3/4,b=1/4, so the common-channel image is [3/16,7/16]; the target1/2 lies outside. Nevertheless C=(9/16)log2(3)-3/4 and Z=2-(3/4)log2(3), so S=Z-C=11/4-(21/16)log2(3)>1/8, certified by3<4. Target D=(21/16)log2(3)-7/4<T=1. Both changed child bills are fully charged from the SAME unused Z; no new supplier, JS bank, controller liability, quota or constant is introduced. An original real U=4I=5 with an explicitly reserved old debit1/8 admits H+T with reserve=-1/8+(9/8)log2(3)>1, certified by3>2. This is one exact paid example outside v9's image, not a necessary stopping-class target and not a universal FEI proof.

The first unsupported universal line remains a noncircular O(I) original reference/account supplier for arbitrary Boolean cores, or a required compatible target whose exact admission fits that original unused account. Merely increasing the allowed reset class does not supply it. The v9 necessity wording must therefore stay scoped: outside the IMAGE does not imply outside the AVAILABLE KL budget. Existing v9 proofs remain valid; no independently accepted assertion is refuted.
'''
put(R/'DERIVATION.md',proof)
prior=load(R.parent/'20261023T122923Z-fleet03-A028-stopping-tree-payment/CLAIMS.json')[0]
statement='The v9 common posterior-channel image is sufficient but not necessary for SAME-account binary sector payment. Exact nodewise admission for arbitrary finite-KL odds with fixed data marginal and inherited controller shape is C<=Z+gamma Cvac. The unchanged T-supermartingale pays every finite mixed tree of such admitted targets. The explicit Boolean dummy-DATA example in DERIVATION.md has prescribed odds1/2 outside [3/16,7/16], yet S>1/8 and original U=4I=5 with old debit1/8 remains valid. This scope clarification supplies neither a required class target nor a universal initial influence price.'
first='Universal influence-priced ORIGINAL source/reference admission for arbitrary Boolean cores remains unproved; a prescribed necessary stopping-class target has not been supplied here.'
claim=dict(claim_id='A028-POSTERIOR-IMAGE-NOT-NECESSARY',version=1,exact_statement=statement,hypotheses=['Original v9/v8 source and controller references, physical inheritance, old bookings, actual normalizers and both full terminals retained.','Every node target has finite true-law KL and C<=Z+gamma Cvac; the inequality is a hypothesis, not supplied by a universal theorem.'],statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A028'],proof_source=['DERIVATION.md','out/exact_certificate.json'],proof_dependencies=[{'claim':prior['claim_id']+'@9','scope':'Supplied-reference T-supermartingale only; new chain-rule admission and direct-character witness rederived here.'}],review_records=[],status='NARROW_SCOPE_CLARIFICATION_AUTHOR_CHECKED; PEER_REVIEW_PENDING; FULL_FEI_OPEN',supersedes=[],refutes=[{'statement':'Outside the common posterior-channel image implies unaffordable from the original account.','scope':'Potential inference only; v9 asserts sufficiency and its exact theorem remains valid.','witness':'out/exact_certificate.json'}],first_unproved_line=first,next_consumers=['A029','A056','A094','A096'])
dump(R/'CLAIMS.json',[claim])
next_action='A029/A096 prescribe a REQUIRED compatible arbitrary-core target; test exact C<=Z+gamma Cvac from CURRENT unused ORIGINAL T after all old debits/full terminals. Channel-image failure alone is insufficient. Initial O(I) source admission remains open.'
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B06',packet_id='A028',gap_id='C019',attempt_id='A028-final-exact-admission-clarification',method='KL chain rule plus one frozen actual Boolean direct-character/butterfly certificate; strict signs by integer inequalities.',mathematical_delta='Strictly broadened supplied-account target admission beyond v9 common-channel image: exact C<=Z+gamma Cvac; actual post-DATA outside-image target paid SAME T, old4I quota/debit and BOTH full child bills. Universal initial source price unchanged.',deliverable_status='COMPLETE_LOCAL; REVIEW_AND_SUPERVISOR_PUBLICATION_PENDING',mathematical_status='SCOPED_EXACT_RESULT; FULL_FEI_OPEN',claim_versions_used=[prior['claim_id']+'@9'],claims_created_or_changed=[claim['claim_id']+'@1'],source_artifacts=receipts,next_consumers=claim['next_consumers'],next_action=next_action,stagnant_substantive_attempts=0,blockers=[first,'Fresh wake degraded: attachment lock failure and stale owner model/state/dream; personalized context freshness unverified.','Campaign deadline14:49UTC limits this to one exact case; persistence may complete after deadline because foreground startup is slow.','Independent review and supervisor publication pending; no remote save claimed.'],packet_ids=['A028'])
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
headings=['exact target, quantifiers, hypotheses and units','sources actually read, revisions and theorem locators','complete derivation or exact first unsupported line','executed validation with domain, arithmetic, commands and outputs','proof dependencies and changed downstream conclusions','one next mathematical action and independent reviewer','actual persistence receipts or precise save blocker']
parts=[statement+' All units bits. See hypotheses in CLAIMS.json.','BOARD.md, B06 notes, own prior STATUS and v9 proof/interface, A029 LEARNED; source hashes in out/context_receipts.json and selected frontier in out/board_frontier.txt. Earlier protocol and campaign materials retained from preceding stage. Fresh wake flagged attachment-render lock failure and stale contextual sources; those notes are not proof premises.',proof,'Frozen spec precedes computation. python -X utf8 code/stage.py: one actual four-variable Boolean truth table, direct-character versus butterfly exact Walsh equality, rational prime-log KL identities, both dummy-DATA children, exact outside-image comparison and integer sign/admission certificates. Output out/exact_certificate.json. Pilot is the entire one-case job, 40MB estimate, max60seconds, no symmetry/GPU/escalation; no job above300MB. Source startup latency is not counted as mathematical evidence.','Consumes v9 supplied T-supermartingale only. New scope clarification is narrow, avoids claiming a new broad universal candidate, and does not infer peer acceptance. Actual witness distinguishes affordability from channel feasibility. The original universal supplier and mandatory target are still missing.',next_action+' Reviewer A029/A094; handoff is this saved source, no external message.','Four protocol files, code and outputs saved in own A028 run; STATUS two lines and WORKLOG/LEARNED updated. No shared source touched. Read-back schema/hash receipts in out/validation.json. Supervisor publication unverified. No new heavy job, governor restart, shared lock manipulation, or other agent shutdown.']
report='# A028 final stage: exact affordability beyond posterior-channel image\n\n'+'\n\n'.join('## '+h+'\n\n'+s for h,s in zip(headings,parts))
report+='\n\nUniversal bridge: C019 supplied-reference admission is strictly enlarged beyond the v9 common-channel image, with unchanged original T and an actual paid post-DATA witness retaining old4I quota, debit and both full child bills. The universal influence-priced initial supplier is not advanced or claimed, and a necessary stopping-class target remains unspecified. The shortest next route is to price such a REQUIRED arbitrary-core target by exact unused KL capacity, rather than treating channel-image failure as insolvency or doing another optional-reset enumeration.\n'
put(R/'REPORT.md',report)
put(A/'STATUS.md','STATE: Final A028 stage saved exact outside-channel SAME-T affordability witness and necessary/sufficient nodewise KL admission; original quota/debits/both child bills retained; peer review pending; universal FEI OPEN.\nNEXT: '+next_action+'\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name,text in [('WORKLOG.md',stamp+' final stage: certified actual Boolean post-dummy-DATA odds1/2 outside channel [3/16,7/16] but SAME T has S>1/8; exact4I quota and old1/8 remain. General nodewise admission C<=Z+gamma Cvac is sufficient for all mixed trees, necessary for local S>=0. Source supplier/required class target/FEI remain open; saved '+R.name),('LEARNED.md','Exact affordability is broader than v9 common-channel feasibility. For fixed r,B, Dstar=D8+C and T-Dstar=Z+gamma Cvac-C. Outside-image targets can consume ORIGINAL unused KL slack. Actual a=pointdefect2,G=z,H=1,dummy d, Ra=Pa,Rg=Rh=uniform-on-z: target z odds1/2 outside [3/16,7/16], S=11/4-(21/16)log2(3)>1/8; H=4-(9/8)log2(3),I=5/4,T=1. A missing required target or universal O(I) initial source is not fixed by this clarification.')]:
 with (A/name).open('a',encoding='utf-8',newline='') as out:out.write('\n'+text+'\n')
protocol=load(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert result['seconds']<60
dump(R/'out/validation.json',dict(status='PASS',exact_case=True,two_Walsh_implementations_equal=True,integer_sign_certificates=True,both_dummy_children=True,protocol_fields_exact=True,packet_delta_identical=True,status_two_lines=True,full_fei='OPEN',saved_utc=stamp))
dump(R/'out/manifest.json',{str(p.relative_to(R)):sha(p) for p in R.rglob('*') if p.is_file() and p.name!='manifest.json' and '__pycache__' not in p.parts})
print(json.dumps(dict(status='PASS',cases=1,outside_image_paid=True,slack_lower_bound='strictly >1/8',I=str(I),full_fei='OPEN',saved_utc=stamp)))
