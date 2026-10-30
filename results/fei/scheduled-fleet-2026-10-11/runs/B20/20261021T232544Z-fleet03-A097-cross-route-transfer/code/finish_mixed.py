from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1];OUT=RUN/'out'
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def wr(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
v=rd(OUT/'MIXED_VALIDATION.json');assert v['status']=='PASS' and v['prefix_nodes']==376
claims=rd(RUN/'CLAIMS.json');c=claims[1]
c['claim_id']='A097-MIXED-ACTIVE-CONTROL-RESET-SAME-ANCESTOR'
c['exact_statement']='For every a>=1,b>=0,r>=2 and F=1-2A_a+2A_(a+b+r), supply a normalized finite-cost source reference with c_raw<=C0 I(1-2A_a), C0>=0. Start with its empty-calibrated A097 complete floor. On the surviving edited branch, allow arbitrary interleavings and stopping of A096 canonical active resets and control queries while r_current>=2. Every control-on child resets to the A097 floor built from the SAME current source reference with r reduced by one; every active on-child uses the specified marginal/calibrated source floor or explicit final point boundary. ALL complementary children retain their COMPLETE inherited references, and allow arbitrary no-reset continuations. The expected sum of all booked erasures and complete terminal cross entropies is <=W_root+8(r-1)e_root<=(2C0+10)I(F)-12e_root, where W_root=c_cal+10e_root(a+b+r) and e_root=2^(1-a-b-r). This spends only the original ancestor quota: its reserve is at least5a*2^(b+r)e_root and 5*2^r>=8(r-1)+12. Structural source reference permits SAME initial rate18. Independent untouched terminals retain full additive cost. This excludes dummy-data resets, renewed canonical resets in complementary off-branches, arbitrary non-point sources and unrelated channel/code bills; full FEI remains OPEN.'
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
c['hypotheses']=['Uniform negative-cell point edit, a>=1,b>=0,r>=2 at ancestor','Normalized finite-cost original source reference and certified c_raw<=C0 I_g, C0>=0','Reset phase stays on surviving edited branch: active queries or control queries with current r>=2; explicit final active boundary ends that branch','Every off-branch keeps full inherited reference; further continuations there are no-reset only','Bits, ideal CE and ordinary influence; full normalizers retained; original quota never renewed']
c['proof_source']['files']+=['code/check_mixed.py','out/FROZEN_MIXED_SPEC.json','out/MIXED_VALIDATION.json']
wr(RUN/'CLAIMS.json',claims)
for file in ['PROGRESS.json','PACKET_DELTA.json']:
 p=rd(RUN/file);p['attempt_id']='stage17-mixed-active-control-original-bank';p['method']='Actual-control likelihood payment plus invariant reach*e=e_root and original exponential reserve; independent reconstruction of A096 active resets'
 p['mathematical_delta']='ALL eligible active/control mixed reset orders paid at SAME original rate2C0+10 (18 structurally), reserve>=5a*2^(b+r)e_root, cumulative extra<=8(r-1)e_root, remaining>=12e_root; A096 v1 independently HOLDS;9649 single-control plus13239 mixed-check assertions PASS'
 p['claims_created_or_changed']=[claims[0]['claim_id']+'@1 independent HOLDS',c['claim_id']+'@1'];p['source_artifacts']+=['out/MIXED_VALIDATION.json']
 p['next_action']='Price one actual dummy-data exposure, or a canonical reset in a retained control-off branch, from SAME remaining original bank after mixed active/control debits; retain complete off-terminals and current source-reference marginal'
 wr(RUN/file,p)
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('# A097: one control reset from the same original bank','# A097: mixed active/control resets from the same original bank')
needle='## sources actually read, revisions and theorem locators'
extra='The same theorem extends to EVERY eligible interleaving of active resets and control queries while r_current>=2 on the surviving edited branch. DERIVATION7 proves complete ledger<=W_root+8(r_root-1)e_root<=K I(F_root)-12e_root; complementary branches retain their inherited references and admit no-reset continuations. This is the final scope; the one-control proof below is its local substitution.\n\n'
report=report.replace(needle,extra+needle)
needle='## proof dependencies and changed downstream conclusions'
extra=('Mixed-order strengthening: python -X utf8 runs/'+RUN.name+'/code/check_mixed.py independently replays every active/control TYPE order and stopping prefix in its frozen domain, using the same direct-character primitives.48 roots,376 prefix nodes,376 active steps,'+str(v['control_steps'])+' control steps,'+str(v['checks'])+' exact predicates PASS in'+str(round(v['runtime_seconds'],3))+'s. These are additional checks, not a replacement count for the9649 single-control assertions. No asymmetric label-permutation exhaustiveness is claimed. The full quantifiers follow by the analytic weighted-charge induction.\n\n')
report=report.replace(needle,extra+needle)
start=report.index('## one next mathematical action and independent reviewer');end=report.index('## actual persistence receipts',start)
report=report[:start]+'''## one next mathematical action and independent reviewer

Price one actual dummy-data exposure or a canonical reset inside an already retained control-off branch from the SAME remaining original reserve, after all mixed active/control debits. Keep every full inherited terminal and the current source-reference marginal. A096 primary independent reviewer; A094/A086 alternates; A098/A099/B20 consume. This changes the source-reference geometry, so it is the first unpaid step after the mixed-order theorem.

'''+report[end:]
start=report.index('## Universal bridge')
report=report[:start]+'''## Universal bridge

C024 history transfer and C019 stopping payment now cover EVERY eligible active/control interleaving on the surviving edited branch, not just A096 active-only histories, at unchanged original rate2C0+10 (18 structurally). The exact off-reference likelihood costs<11e and erasure<12e leave extra<8e per control; reach*e=e_root and the original reserve>=5a*2^(b+r)e_root pay all r-1 eligible controls with>=12e_root left. Every old debit and complete complementary terminal remains. Universal FEI improvement is zero: dummy-data resets, renewed canonical resets inside off-branches and generic priced source references remain open. NEXT attacks that actual change of source-reference marginal with the same diminished bank, rather than extending another isolated entropy class result.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(ROOT/'STATUS.md').write_text('STATE: A097 stage17 saved: A096 active-reset v1 independently HOLDS; ALL eligible mixed active/control reset orders paid SAME rate18, >=12e original reserve;9649 single + '+str(v['checks'])+' mixed exact checks PASS; FEI OPEN, new review pending.\nNEXT: A096/A094/A086 review; price actual dummy-data exposure or off-branch canonical reset from SAME remaining source bank, retaining all mixed debits and full terminals.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for fn,line in [('WORKLOG.md','Stage17 strengthened before close: ALL eligible active/control orders paid from original rate18 reserve, since reach*e=e_root and5*2^r>=8(r-1)+12.48 roots/376 prefixes/'+str(v['checks'])+' exact assertions PASS. Next dummy-data or off-branch reset.'),('LEARNED.md','Mixed-order extension: every control reset while current r>=2 costs<8e beyond current W; every active reset does not increase W. Reach*e=e_root under either on-query. At most r_root-1 control charges are paid by original reserve>=5a*2^(b+r)e_root, since5*2^r-8(r-1)>=12 for r>=2. Thus all such mixed orders and stopping cuts retain>=12e_root at SAME rate18; off-branches retain inherited full references and only no-reset continuations. Dummy-data query changes R marginal and remains unpaid.')]:
 with (ROOT/fn).open('a',encoding='utf-8') as f:f.write('\n'+stamp+' '+line+'\n')
# Derive reported count from executed output rather than hard-coded draft text.
for file in ['PROGRESS.json','PACKET_DELTA.json']:
 p=rd(RUN/file);p['mathematical_delta']=p['mathematical_delta'].replace('13239 mixed-check',str(v['checks'])+' mixed-check');wr(RUN/file,p)
assert rd(RUN/'PROGRESS.json')==rd(RUN/'PACKET_DELTA.json')
assert len((ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipt=rd(OUT/'PERSISTENCE_RECEIPTS.json');receipt['at']=stamp;receipt['files']=[]
for p in RUN.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  data=p.read_bytes();assert len(data)<20_000_000
  receipt['files'].append({'path':str(p.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
wr(OUT/'PERSISTENCE_RECEIPTS.json',receipt)
print(json.dumps({'status':'MIXED_STRENGTHENING_SAVED','new_claim':c['claim_id'],'mixed_checks':v['checks'],'files':len(receipt['files'])}))
