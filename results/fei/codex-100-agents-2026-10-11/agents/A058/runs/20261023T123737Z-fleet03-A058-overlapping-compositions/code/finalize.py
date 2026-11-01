from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict
import hashlib,json,time

R=Path(__file__).resolve().parents[1];AR=R.parents[1]
P=AR/'runs/20261023T065216Z-fleet03-A058-overlapping-compositions'
start=time.perf_counter()
def dump(name,obj):(R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
@lru_cache(None)
def fac(n):
    d={};p=2
    while p*p<=n:
        while n%p==0:d[p]=d.get(p,0)+1;n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def add(*items):
    v=defaultdict(Q)
    for scale,w in items:
        for p,c in w.items():v[p]+=scale*c
    return {p:c for p,c in v.items() if c}
@lru_cache(None)
def H(tt):
    v=defaultdict(Q);N=len(tt)
    for t in range(N):
        a=Q(sum(y*(-1 if (x&t).bit_count()%2 else 1) for x,y in enumerate(tt)),N);p=a*a
        if not p:continue
        for prime,c in fac(p.denominator).items():v[prime]+=p*c
        for prime,c in fac(p.numerator).items():v[prime]-=p*c
    return {p:c for p,c in v.items() if c}
def I(tt):
    n=(len(tt)-1).bit_length()
    return Q(sum(tt[x]!=tt[x^(1<<i)] for x in range(len(tt)) for i in range(n)),len(tt))
def cut(tt,j,b):return tuple(y for x,y in enumerate(tt) if x>>j&1==b)
def affine(tt):
    supp=[x for x,y in enumerate(tt) if y]
    if not supp:return False
    L={x^supp[0] for x in supp}
    return all(x^y in L for x in L for y in L)
def compose(a,b,act):return tuple(a[x&1] if act[x>>1] else b[x&1] for x in range(2*len(act)))
cores=[tuple(-1 if m>>x&1 else 1 for x in range(2)) for m in range(4)]
identities=sourcechecks=forkchecks=0
for mask in range(256):
    act=tuple(mask>>x&1 for x in range(8))
    if sum(act)!=4:continue
    hs=H(tuple(1-2*y for y in act))
    for a in cores:
        for b in cores:
            delta=Q(sum(x!=y for x,y in zip(a,b)),2)
            f=compose(a,b,act);flat=compose(a,b,(0,1))
            assert add((Q(1),H(f)),(Q(-1),H(flat)))=={p:delta*c for p,c in hs.items() if delta*c}
            identities+=1
for k in [1,2,3]:
    N=1<<k
    for mask in range(1,(1<<N)-1):
        act=tuple(mask>>x&1 for x in range(N))
        if not affine(act):continue
        alpha=Q(sum(act),N);r=(alpha.denominator).bit_length()-1
        for a in cores:
            for b in cores:
                f=compose(a,b,act);delta=Q(sum(x!=y for x,y in zip(a,b)),2);Ee=I(tuple(x*y for x,y in zip(a,b)))
                for j in range(k):
                    a0,a1=cut(act,j,0),cut(act,j,1)
                    if a0==a1:continue
                    g,h=cut(f,j+1,0),cut(f,j+1,1)
                    J=Q(sum(x!=y for x,y in zip(g,h)),len(g));Bg=4*J+I(tuple(x*y for x,y in zip(g,h)))
                    assert Bg>=2*alpha*Ee+4*alpha*(r+1)*delta;sourcechecks+=1
                    if any(a0) and any(a1):
                        assert H(g)==H(f)==H(h);forkchecks+=1
        assert time.perf_counter()-start<60
maj=tuple(int(x.bit_count()<=1) for x in range(8));phase=tuple(1-2*y for y in maj)
assert H(phase)=={2:Q(2)} and I(phase)==Q(3,2)
act=tuple(int((x&1) and maj[x>>1]) for x in range(16))
a=(1,1);b=(1,-1);f=compose(a,b,act);g=cut(f,1,1);h=cut(f,1,0)
B=4*Q(sum(x!=y for x,y in zip(g,h)),len(g))+I(tuple(x*y for x,y in zip(g,h)))
assert B==Q(9,4)
assert H(f)=={2:Q(9,2),3:Q(-9,8)}
old=add((Q(1),H(f)),(Q(-1,2),H(g)),(Q(-1,2),H(h)))
assert old=={2:Q(3),3:Q(-9,8)} and 2**24>3**9
assert H(g)=={2:Q(3)} and H(h)=={}
assert time.perf_counter()-start<60
ind={'status':'PASS','nonflat_identities':identities,'actual_source_admissions':sourcechecks,'both_live_actual_entropy_equalities':forkchecks,'majority_phase':{'H':'2','I':'3/2','squared_spectrum':'four atoms1/4'},'positive_nonflat_fixture':{'B':'9/4','3B':'27/4','parent_D':'9/2-(9/8)log2(3)','old_debit':'3-(9/8)log2(3)','reached_child_bill':'3/2','old_debit_sign':'2^24>3^9'},'arithmetic':'direct character sums, Fraction prime-log forms, actual physical branch product edge counts','elapsed_seconds':time.perf_counter()-start,'independent_agent_review':False}
dump('out/INDEPENDENT_VALIDATION.json',ind)

protocolpath=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocolpath.read_text(encoding='utf-8-sig'))
main=json.loads((R/'out/EXACT_VALIDATION.json').read_text(encoding='utf-8'))
statement='For arbitrary Boolean A,B on a common finite uniform data cube and independent selectors, an affine activation a=1_{Lz=c} of codimension r>=1 has the same coherent entropy overhead D=H(B+a(A-B))-alpha H(A)-(1-alpha)H(B) as an r-bit point activation. For every nonzero physical column j of L, its ACTUAL original ticket B_j=4Inf_j(F)+I(F_j+ F_j-) dominates the v8 flat ticket, so ONE original3B_j pays all signed coherent costs of every adaptive physical stopping tree with both complete inherited cores/terminals retained. Every query with TWO surviving affine targets has exactly zero coherent debit, even after a positive old prefix debit. For an arbitrary indicator a of probability alpha=2^-r, EXACTLY D_a=D_flat+Pr(A!=B)[H(1-2a)-H(point_phase_r)], with nonnegative tax. For a fresh outer bit t gating a_child of probability p=2^-r, that tax is halved and the ORIGINAL source is pI(AB)+4p delta+delta I(1-2a_child). The sufficient selector-surplus condition H(s)-H(point_phase_r)<=6[I(s)-2rp] admits the whole continuation at SAME original price3. The nonflat majority-on3-bits selector satisfies it unconditionally and gives an actual positive-old-debit nonflat continuation for ALL A,B. The condition is not asserted universally, and full FEI remains open.'
c=json.loads((P/'CLAIMS.json').read_text(encoding='utf-8'))[0]
c.update(version=9,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),hypotheses=['finite uniform cubes, Boolean A,B share arbitrary data, selector coordinates independent of data','affine admission: full-row-rank binary L and designated nonzero physical column','nonflat identity: activation probability2^-r, r>=1','nonflat price3 admission requires explicitly supplied surplus condition; majority fixture verified unconditionally','ONE original allocation before signed debits; both inherited core entropies and all true terminals retained'],proof_source=['PROOF.md','code/exact_affine_tax.js','code/finalize.py','out/EXACT_VALIDATION.json','out/INDEPENDENT_VALIDATION.json'],proof_dependencies=['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@8 author proof: point activation D_r<=3B_flat; independent review pending','explicit coherent selector posterior; Fourier transform of affine-subspace indicators; physical edge counting','selector entropy tensorization lower bound I(s)>=2rp; no universal selector FEI assumption'],review_records=[{'reviewer':'A091','status':'PENDING; primary; no message sent'},{'reviewer':'A090','status':'PENDING; alternate; no message sent'}],status='AUTHOR_PROOF_WITH_EXACT_CERTIFICATES; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',supersedes=['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@8 (extends; retains earlier source scope)'],refutes=['Exploratory zero-tax extension from affine to arbitrary selector spectra: majority selector A1,Bx has D3 versus flat D2, tax1'],first_unproved_line='Original physical-surplus admission outside the explicitly supplied criterion is unproved; no universal selector FEI/surplus inequality is asserted. Complete inherited core FEI is also unpaid.',next_consumers=['A091','A090','A057','A059','A060','B12','B20'])
assert set(c)==set(protocol['required_per_run']['claim_fields']);dump('CLAIMS.json',[c])
p=json.loads((P/'PROGRESS.json').read_text(encoding='utf-8'))
p.update(run_id=R.name,attempt_id='substantive-stage9-affine-and-nonflat-original-source',method='affine quotient source admission; exact general selector entropy tax; original physical-surplus pays majority continuation after positive debit',mathematical_delta='Closed all affine TWO-surviving-branch histories at SAME original3B; proved exact nonflat entropy tax; paid genuine majority nonflat child after positive old debit for arbitrary A,B from ORIGINAL larger physical surplus. No renewal, inherited cores/terminals retained.',deliverable_status='COMPLETE_LOCAL; supervisor copy and independent review unverified',mathematical_status='author proof and exact finite certificates; general nonflat surplus admission and full FEI OPEN',claim_versions_used=['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@8'],claims_created_or_changed=['A058-ANCHORED-OVERLAP-POSTERIOR-LEDGER@9'],source_artifacts=['PROOF.md','FROZEN_SPEC.json','NONFLAT_SPEC.json','INDEPENDENT_SPEC.json','out/EXACT_VALIDATION.json','out/INDEPENDENT_VALIDATION.json','out/SOURCE_RECEIPTS.json'],next_action='Price a necessary nonflat child OUTSIDE the sufficient surplus criterion from SAME actual remaining ORIGINAL account after old prefix debit, using full existing slack and both terminals; prove a wider influence-owned admission or give an exact obstruction. Free affine forks and already covered data telescopes are not new payment.',stagnant_substantive_attempts=0,blockers=['independent review pending','general nonflat ORIGINAL-source admission outside supplied surplus criterion','arbitrary inherited core FEI unpaid','brain self-care degraded: stale personal model/state/latest dream; not used as proof premises'],packet_ids=['A058'])
fields=set(protocol['required_per_run']['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids');assert set(p)==fields
dump('PROGRESS.json',p);dump('PACKET_DELTA.json',p)
# Correct the NEXT target: arbitrary physical data restrictions are already covered by the signed ledger.
proof=(R/'PROOF.md').read_text(encoding='utf-8')
proof=proof.replace('NEXT must expose an actual DATA bit of the paid nonflat child while retaining the current normalized spectrum, SAME diminished original account, old prefix debit and both full terminals; another free affine fork does not address the universal obstruction.','NEXT must pay a necessary nonflat child OUTSIDE the sufficient surplus criterion from the SAME actual remaining ORIGINAL account after the old prefix debit, using the full existing slack and both terminal bills, or certify that admission fails. Physical data telescopes are already covered; another free affine fork does not address the universal obstruction.')
(R/'PROOF.md').write_text(proof,encoding='utf-8')

sections={
'exact target, quantifiers, hypotheses and units':'Uniform finite cubes, entropy in bits, arbitrary overlapping Boolean cores A,B and independent selectors. v9 proves original3B admission for every affine selector activation and every nonzero physical root column. Queries with TWO surviving affine targets cost zero coherently, even after an actual positive debit. An exact nonflat-selector tax and a physical-surplus criterion pay a genuine majority child from the SAME original account. Both complete inherited core entropy bills and actual terminals remain; full FEI is OPEN.',
'sources actually read, revisions and theorem locators':'Current STATUS; BOARD B12 A056-A060 and A091/A096/A097 updates; B12 STREAM_NOTES v2 dated2026-10-11 23:30 UTC. The complete execution protocol was inherited from earlier stages and read by the schema checker at its actual path. v8 point-source proof and claims are inherited dependencies, not new independent review. The v8 all-depth source is author-proved with independent review pending. Basic affine Fourier flatness is standard and reconstructed here; no priority claim. Current brain wake warns that personal model/state and latest dream are stale; they are not proof inputs. No new paper audit or external literature claim is made.',
'complete derivation or exact first unsupported line':'PROOF.md sections1-3 derive the coherent selector posterior, quotient-column physical source B_j>=B_flat, and exact zero debit at two-live affine forks. Section4 proves the arbitrary-selector identity D_a=D_flat+delta[H(selector phase)-H(flat phase)]. Section4b shows that adding one outer selector halves the tax; the ORIGINAL larger root source has additional cash delta[I(selector phase)-2rp]. Criterion H(s)-H(flat)<=6[I(s)-2rp] pays the full nonflat tax at price3 without restoring spent cash. The majority phase has H2,I3/2, so this gives an unconditional necessary nonflat continuation for arbitrary A,B. With A1,Bx the old debit is3-(9/8)log2(3)>0 and the later reached nonflat bill is3/2. The first unpaid universal line is ORIGINAL surplus admission for a necessary nonflat child outside the supplied criterion. That criterion is NOT asserted universally; arbitrary complete A,B FEI remains unpaid.',
'executed validation with domain, arithmetic, commands and outputs':f'All three specs were frozen before their computations. code/exact_affine_tax.js computational body executed in functions.exec V8:27136 exact tax identities for106 selector profiles of sizes1,2,4 and all256 two-bit core pairs; geometry examined65812 masks at k1..4, identified368 proper affine sets, checked1162 relevant queries including674 two-live forks and488 one-live queries. All256 arbitrary core pairs checked for ORIGINAL majority surplus and unchanged old debit. Main total{main["assertions"]} exact assertions PASS in{main["elapsed_ms"]}ms. Arithmetic: integer Walsh/physical edge counts and exact prime-log coefficient equality at scale65536; no floating log sign. Independent python -X utf8 code/finalize.py uses actual truth tables, direct character sums and Fraction entropy vectors:1120 balanced-selector tax identities plus actual source admissions/free-fork checks on every affine profile at k1..3 with all16 one-bit core pairs; out/INDEPENDENT_VALIDATION.json contains counts and positive-old-debit fixture. This is a second implementation by A058, not independent-agent review. Majority H is exactly2, from FOUR squared atoms1/4, and I3/2; neither is rounded. No GPU, >300MB job, dimension escalation or Lean acceptance claim. One source-save patch was rejected because it attempted delete/add of the same path in one patch; separate scoped operations saved the source, and final hashes verify it.',
'proof dependencies and changed downstream conclusions':'Extends the existing umbrella claim to respect the review cap. v8 supplied all-depth point D<=3B; v9 adds physical affine-source admission, true branching closure and an explicit nonflat bill. The ORIGINAL larger physical owner pays the majority tax after actual prefix debit, with at least delta/2 of that incremental allocation left. This is not a new descendant bank or deletion of inherited terminal entropy. General selector FEI or the surplus criterion would still need a proof; importing either unconditionally would overstate the result. Physical data restriction telescopes are already covered and are not presented as a new next payment.',
'one next mathematical action and independent reviewer':'A091 primary, A090 alternate; independent review PENDING. NEXT: pay one necessary nonflat selector child outside the sufficient surplus criterion from the SAME actual remaining original cash after positive prefix debit, using the full unused slack and both terminal bills; prove a wider physical-energy admission or give its exact Boolean obstruction. Avoid another affine-only case or a constant optimization.',
'actual persistence receipts or precise save blocker':'All research artifacts and rolling edits are inside A058. Four protocol files, proof, frozen specs, executable helpers and exact outputs are saved; statement SHA and protocol schemas are checked; PACKET_DELTA equals PROGRESS with packet_ids=[A058]. out/MANIFEST.json binds bytes; out/SOURCE_RECEIPTS.json binds source versions. STATUS is exactly two lines; dated WORKLOG/LEARNED entries appended. Local save does not prove supervisor copying, remote adoption or independent acceptance. No git, mail, brain writes, GPU, background jobs or other agents\' mutations. Brain wake remains degraded on stale personal model/state/dream notes.'}
report='# A058 stage9: original source pays affine forks and a nonflat child\n\n'+''.join('## '+title+'\n\n'+sections[title]+'\n\n' for title in protocol['required_per_run']['report_fields'])
report+='Did: saved author proof, exact identities and actual physical-source receipts. Stopped: own finite computations completed normally; no running work killed. Left running: no owned research jobs.\n\n## Universal bridge\n\nC019 stopping-tree payment advances through all genuine affine forks and an actual NONFLAT majority continuation AFTER a positive old debit: the SAME original3B account pays, both complete inherited core/terminal bills remain, and no descendant reserve is renewed. The arbitrary-selector extra bill is now exactly delta times selector Fourier-entropy excess; the majority bill is funded by unused ORIGINAL physical surplus with at least delta/2 left. General admission outside the supplied surplus criterion and arbitrary inherited-core FEI remain open. NEXT targets that unadmitted necessary nonflat bill using the full diminished original cash, because this is the precise ownership step toward full FEI; free affine forks or already telescoping data restrictions cannot remove it.\n'
(R/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A058 stage9 saved: ALL affine forks + genuine nonflat majority child paid SAME original3B after positive old debit; exact tax identity;34599 main checks PASS; independent checks PASS; review pending, FEI OPEN.\nNEXT: A091/A090 review v9; pay necessary nonflat child OUTSIDE supplied surplus criterion from SAME actual remaining ORIGINAL cash/full slack, old debit and BOTH full terminals retained; no renewed bank.\n'
(AR/'STATUS.md').write_text(status,encoding='utf-8')
entry='v9: all affine selector activations admit SAME original3B via quotient rank;674 two-live forks exact zero cost. General tax D_a-D_flat=delta[H(1-2a)-H(flat)] nonnegative. One outer gate halves tax; ORIGINAL source surplus delta[I(s)-2rp] pays when entropy excess<=6 surplus. Majority H2,I3/2 passes; genuine nonflat bill paid after old positive debit, incremental reserve>=delta/2.34599 main assertions and independent direct-character checks PASS. General nonflat admission and inherited core FEI OPEN.'
for name in ['WORKLOG.md','LEARNED.md']:
    pth=AR/name;old=pth.read_text(encoding='utf-8') if pth.exists() else ''
    if R.name not in old:
        with pth.open('a',encoding='utf-8') as out:out.write('\n2026-10-23 | '+R.name+' | '+entry+'\n')
paths=[protocolpath,Path(r'BOARD.md'),Path(r'claude\B12\STREAM_NOTES.md'),P/'PROOF.md',P/'CLAIMS.json']
dump('out/SOURCE_RECEIPTS.json',[{'path':str(x),'sha256':hashlib.sha256(x.read_bytes()).hexdigest(),'scope':'bytes at finalize; mutable board may advance'} for x in paths])
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
assert len((AR/'STATUS.md').read_text().splitlines())==2
manifest=[]
for x in sorted(R.rglob('*')):
    if x.is_file() and x.name not in ['MANIFEST.json','FINALIZE.json']:
        data=x.read_bytes();assert len(data)<20_000_000
        manifest.append({'path':str(x.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
dump('out/MANIFEST.json',manifest)
result={'status':'PASS','manifest_files':len(manifest),'statement_sha256':c['statement_sha256'],'independent':ind,'protocol_fields':'PASS','independent_review':'PENDING','remote_copy':'UNVERIFIED','full_FEI':'OPEN'}
dump('out/FINALIZE.json',result)
assert all(hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in manifest)
assert hashlib.sha256(json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))[0]['exact_statement'].encode()).hexdigest()==c['statement_sha256']
assert all('## '+title in (R/'REPORT.md').read_text(encoding='utf-8') for title in protocol['required_per_run']['report_fields'])
print(json.dumps(result))
print('REOPENED REPORT, STATUS AND ALL MANIFEST HASHES PASS')
