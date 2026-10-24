"""Check the finite certificates, save protocol deliverables and current handoff."""
from continue_spent import *
import hashlib,datetime

def main():
    run=ROOT.name;folder=ROOT.parents[1]
    rows=json.loads((ROOT/'out/CONTINUATION_CASES.json').read_text(encoding='utf-8'))
    rep=json.loads((ROOT/'out/REPRODUCTION.json').read_text(encoding='utf-8'))
    result=json.loads((ROOT/'out/RESULTS.json').read_text(encoding='utf-8'))
    ck(len(rows)==rep['cases']==60)
    ck({(r['terminal'],r['block'],r['coordinate']) for r in rows}=={(b,j,i) for b in range(2) for j in range(1,6) for i in range(6)})
    positive=[];allocations=[]
    for r,rr in zip(rows,rep['cases_detail']):
        ck((r['terminal'],r['block'],r['coordinate'])==(rr['terminal'],rr['block'],rr['coordinate']))
        ck(r['required_T'][0]>0 and r['mean_full_B'][0]>0)
        ck(all(c['S'][0]>0 and F(c['I'])>0 and c['V'][0]>=0 for c in r['children']))
        need=rr['selected_only_shortfall']
        ck(need[0]>0 or need[1]<0)
        if need[0]>0:positive.append((r['terminal'],r['block'],r['coordinate']))
        B=r['mean_full_B'];T=r['required_T']
        if r['terminal']==0:
            # Incoming D=S_parent exactly by the previous minimal transfer.
            # Therefore T=D+e=average S_child exactly: use capacities in full.
            booked=[c['S'] for c in r['children']];remaining=[(0,0),(0,0)]
            overlaps(avg(booked),T)
        else:
            ck(sub(B,T)[0]>0)
            booked=[mul(div(T,B),c['S']) for c in r['children']]
            remaining=[sub(c['S'],d) for c,d in zip(r['children'],booked)]
            ck(all(a[0]>0 for a in remaining))
        old=[mul(div(r['incoming_debit'],T),a) for a in booked]
        new=[mul(div(r['e'],T),a) for a in booked] if r['e'][0]>=0 else None
        overlaps(avg(old),r['incoming_debit'])
        if new is not None:overlaps(avg(new),r['e'])
        allocations.append(dict(terminal=r['terminal'],block=r['block'],coordinate=r['coordinate'],booked=booked,old=old,new=new,remaining=remaining))
    ck(len(positive)==36)
    witness=rep['cases_detail'][0]['selected_only_shortfall']
    ck(witness[0]*1000>31*Q and witness[1]*125<4*Q)
    info=dict(exact_checks=engine.tests,selected_only_failures=36,
       failures_by_terminal={str(b):sum(t[0]==b for t in positive) for b in (0,1)},
       witness_shortfall_interval=witness,witness_shortfall_rational_bounds=['31/1000','4/125'],
       all60_full_children_strictly_positive=True,all60_full_children_nonconstant=True,
       allocations=allocations)
    (ROOT/'out/FINAL_VALIDATION.json').write_text(json.dumps(info,indent=2)+'\n',encoding='utf-8')
    statement=('For F=J(g^6) on six disjoint uniform six-bit blocks, with g negative exactly on {0,1,2}, '
      'h negative exactly on {0,1,2,4,8,16,32,6,17,40} and J(x)=-h(x xor1), retain the rate4 '
      'A089 prefix block0 original coordinates2=0,0=0,3=b, and its exact minimal sibling-transfer debit. '
      'All60 next-query alternatives (b in {0,1}, block j in {1,...,5}, coordinate i in {0,...,5}) '
      'have two nonconstant full children with positive S4 and admit same-debit full-capacity payment. '
      'Exactly36 alternatives fail corrected-newly-queried-core-only payment. For b=0,j=1,i=0 '
      'the required mean debit minus mean corrected selected capacity lies strictly between31/1000 '
      'and4/125 bits. No universal child-eligibility or FEI bound is asserted.')
    h=hashlib.sha256(statement.encode()).hexdigest()
    next_action=('A089/A072 derive a component-level noncircular payment after the now saturated terminal '
      'has funded another physical core query; keep every old label, both full children and root reaches. '
      'A074/A092 independently reproduce the60-case census and36 owner shortfalls. Do not renew the other-owner reserve.')
    claims=[dict(claim_id='A071-SPENT-SIBLING-NEXT-QUERY-CENSUS',version=1,exact_statement=statement,
      hypotheses=['uniform physical cube','disjoint six-bit cores','fixed rate4','specified original prefix and minimal A089 debit','all entropy in bits','60 alternatives are separate choices'],
      statement_sha256=h,contributors=['A071'],proof_source=['REPORT.md','code/continue_spent.py','code/reproduce_spent.py','out/FINAL_VALIDATION.json'],
      proof_dependencies=['explicit Boolean tables','exact Shannon occupied-block chain rule','A089 stage6 minimal-transfer allocation reconstructed locally'],
      review_records=[dict(reviewer='A071 second implementation',status='INTERNAL_REPRODUCTION_ONLY',artifact='out/REPRODUCTION.json')],
      status='EXACT_FINITE_CERTIFICATE_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=['candidate selected-newly-queried-core-only continuation; no attributed source theorem'],
      first_unproved_line='For arbitrary Boolean cores and retained histories, inherited component constraints guarantee nonnegative full child capacities and enough unused transferred reserve.',
      next_consumers=['A089','A072','A074','A075','A092','B15','B20'])]
    (ROOT/'CLAIMS.json').write_text(json.dumps(claims,indent=2)+'\n',encoding='utf-8')
    progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=run,stream='B15',packet_id='A071',
      gap_id='B15-ARBITRARY-CORE-BIASED-ADMISSION',attempt_id='A071-stage17-spent-sibling-next-query',
      method='Frozen60 labelled physical queries; exact centered expansion and independent product-law orthogonal moment transform; same rate4 and actual inherited debit.',
      mathematical_delta='All60 full-capacity continuations certified;36 corrected-new-core-only failures, including explicit shortfall in(31/1000,4/125) bits; no universal closure.',
      deliverable_status='COMPLETE_LOCAL; independent review and supervisor adoption pending',
      mathematical_status='EXACT_FINITE_CERTIFICATE; FULL_FEI_OPEN',
      claim_versions_used=['A089 stage6 minimal sibling transfer@1 reconstructed at specified prefix','A072/A074 transfer reports coordination only'],
      claims_created_or_changed=['A071-SPENT-SIBLING-NEXT-QUERY-CENSUS@1'],
      source_artifacts=['FROZEN_SPEC.json','REPRODUCTION_SPEC.json','out/SOURCE_PINS.json','out/RESULTS.json','out/REPRODUCTION.json','out/FINAL_VALIDATION.json'],
      next_consumers=claims[0]['next_consumers'],next_action=next_action,stagnant_substantive_attempts=0,
      blockers=['Universal inherited signed-component eligibility remains open.','Independent reviewer acceptance and remote persistence unverified.'],packet_ids=['A071'])
    for name in ['PROGRESS.json','PACKET_DELTA.json']:(ROOT/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
    report=f'''# exact target, quantifiers, hypotheses and units

The prescribed search space falsifies corrected-new-core-only continuation after an actual sibling transfer. It also certifies a complete finite full-capacity repair: all60 labelled next queries pass, and exactly36 require more than the corrected newly queried core reserve. Full FEI remains OPEN. This is an exact finite certificate, pending independent review; it is not Lean-checked.

Let S(f)=4I(f)-H(f), with Fourier entropy in bits and uniform physical coordinates. Define g=-1 exactly on{{0,1,2}} in the six-bit cube, h=-1 exactly on{{0,1,2,4,8,16,32,6,17,40}}, J(x)=-h(x xor1), and F=J(g,g,g,g,g,g) on36 physical bits. The prefix queries block0 original bits2,0,3; retain the first two answers0,0 and either third answer b. Each resulting parent has33 physical bits. Query any of30 labelled coordinates in blocks1..5:60 alternatives, each with two32-bit full children. No full36-bit truth table is materialized.

# sources actually read, revisions and theorem locators

The execution protocol2026-10-11-execution-v2 is read in full, along with current BOARD supervisor snapshot2026-10-21 20:01 UTC, B15 lead v2 (still2026-10-11), A071 STATUS/LEARNED and previous substantive run20261014T090502Z. The lead's old n5 census target is already settled in A071's earlier runs; dispatch therefore consumes the new A089 dependency rather than repeating it. A07220261014T124911Z REPORT and A074 board status establish coordination context, not proof premises. A08920261021T154748Z REPORT and its third_query.py, repair.py, reproduce.py, arithmetic.py and check.py supply the exact prefix/account interface. Three helpers are copied locally, source-byte hashes pinned in out/SOURCE_PINS.json; no other agent source executable is run or modified.

Campaign README/CURRENT_STATUS, registry structures, packet index, stream actions, campaign plan and supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and sources were inspected as read-only background. Threshold38pp Proposition7.1 equations67--70 supplies the known disjoint-composition context; the earlier threshold version and both percolation texts were inspected but no literature theorem is a needed proof premise here. The paper text contains legacy cp1252 bytes; a failed UTF8 excerpt read is a reader error, not mathematical evidence. The successful cp1252 excerpt recovers the proposition. No web, publication, git or shared-index write is performed. The user's current23 October deadline supersedes older protocol dates.

# complete derivation or exact first unsupported line

Write H(F)=sum_j q_j H(g_j)+C and I(F)=sum_j q_j I(g_j), retaining all six cores. The coefficient proof groups each physical Fourier set by its occupied block mask. Given mask T, the nonempty spectrum within each occupied core is independent, so H(F)=H(mask)+sum_j q_j[H(g_j)-h2(Var(g_j))]. Also P(j occupied)=q_j Var(g_j), yielding the influence identity. Endpoint-constant cores contribute zero conditional entropy and zero influence and do not delete the other cores. Both implementations check exact Parseval and physical influences.

For any query let e=H(parent)-mean H(children)-4Inf_query. Exact physical influence telescoping gives mean S(children)=S(parent)+e. If D is the inherited booked debit, the outgoing mean must be T=D+e. Thus mean S(children)-T=S(parent)-D exactly. This identity does not establish child positivity; that is checked separately on every finite case here.

Reconstruct the actual old bookings: the first active child receives2e1, the second children receive D_b=(2e1+e2)U_b/mean(U), and the third query is original coordinate3 in second child0. For third children c=0,1 put U_c=q0 S(g0^c), M_c=S(full_c)-U_c. Here M0<0, U1=0, M1>0. The corrected selected capacity is V0=U0+M0=S(full_0), V1=0. Let tau=D_0+e3-V0/2>0. The minimal transfer books debit V0 in terminal0 and2tau in terminal1. Both third terminals keep unconditional reach1/8; the untouched root terminal has reach1/2 and opposite second terminal reach1/4. All those stopped terminals and previous bookings remain unchanged.

At a next query in block j define raw selected U_c=q_j S(core_j^c), signed remainder M_c=S(full_c)-U_c, corrected V_c=U_c-max(0,-M_c), and W_c=max(0,M_c). All120 full children are nonconstant with S>0, all V>=0, and all required T>0. In terminal0 the incoming debit equals its entire S, so T=mean S(children) exactly. Book each child's complete S and leave exactly zero; this follows algebraically, not from an interval equality tolerance. In terminal1, T<mean S(children) strictly; book T*S_child/mean S and leave strictly positive surplus. Each denominator is certified positive. Split every outgoing debit d into old label (D/T)d and new label (e/T)d; their means are exactly D and e, so no incoming label is renewed or erased. Earlier root labels inside D retain their original proportional split. The corresponding exact rational interval diagnostics are saved in FINAL_VALIDATION.

The stronger selected-new-core-only rule would require T<=mean V. It fails in36 cases ({info['failures_by_terminal']} by terminal). An explicit witness is terminal0, block1, original coordinate0. Both newly queried core children and both full terminal functions are nonconstant. The certified shortfall T-mean V is strictly between31/1000 and4/125 bits (display approximately0.03143122879562068); required debit is approximately0.1730582045892605, and the full child S values are approximately0.2084672421416167 and0.1376491670369043. Decimal displays carry no sign authority. This refutes a candidate stronger continuation, not A089's result: A089 explicitly leaves the next owner interface open.

First unsupported universal line: inherited signed component information guarantees positive full child capacity and enough unused transferable reserve for arbitrary cores and histories. The allocation formula alone cannot prove this premise; calling an already computed full S a new selected-core reserve would be circular for FEI. The exact saturated-child invariant supports further conditional transport, but arbitrary child positivity is unpaid.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC precedes the pilot: helper version/source pins, actual Boolean tables, domain60, no symmetry reduction, completeness scope, rational arithmetic,100MB estimated memory and55s runtime cap. The two-case pilot uses{json.loads((ROOT/'out/PILOT.json').read_text(encoding='utf-8'))['runtime_seconds']:.3f}s. Full continue_spent.py uses{result['runtime_seconds']:.3f}s and records{result['engine_checks']} engine checks. REPRODUCTION_SPEC precedes reproduce_spent.py, which uses independent direct core character sums and a tensor product-law centered-moment transform; it checks47 distinct states, all60 alternatives and{rep['engine_checks']} recorded engine checks in{rep['runtime_seconds']:.3f}s. Both paths agree on all full H/I and36 selected-owner shortfalls. They share only the explicitly audited bounded-log primitive, not the spectrum construction. This is internal reproduction, not independent reviewer acceptance.

Arithmetic is arbitrary integers/Fractions and192-bit outward fixed-point log bounds. Range reduction puts log arguments in[1,2]; z=(a-b)/(a+b)<=1/3. The80-term atanh sum has remaining absolute natural-log error at most18/[8(161)3^161], and every arithmetic rounding is outward. No floating-point comparison decides a sign. Boundary core biases0 and1 are handled by zero occupied mass; positive denominators, nonconstant full children and exact finite-domain coverage are checked. Search-space coverage is complete only for the60 labelled choices; it is neither all histories nor an n-dimensional truth-table census. General affine coordinate mixing is not an influence symmetry and is not used.

Commands from A071: python -B -X utf8 runs/{run}/code/continue_spent.py --pilot; then continue_spent.py; then reproduce_spent.py; then persist_stage.py. Exact outputs and witness bounds are in out/. All jobs are serial, each below55s mathematical runtime and expected100MB; no job over300MB is planned, so the memok gate is not needed. There is no GPU, automatic dimension/rate escalation, detached job or new worker. The compute snapshot reports status ok and no intervention in the last hour; its ledger was read, no running work was stopped. Brain wake warns of stale personal notes, disclosed to the user and not used as premises. One read-only math recall supplies no stronger payment theorem. No shared task checklist or brain is mutated under the explicit A071-only write boundary.

# proof dependencies and changed downstream conclusions

Only the explicit Boolean definitions, disjoint-spectrum chain rule and reconstructed prefix bookings are mathematical dependencies. The new finite claim is internally reproduced and awaits A074/A092 review. It advances the A089 spent-sibling interface without changing its rate or taking fresh root credit. It demonstrates why corrected newly queried capacity is still inadequate even after every full terminal is affordable. It changes no universal C018/C019 theorem and gives no FEI counterfamily.

# one next mathematical action and independent reviewer

{next_action} The useful next step is a signed component-level criterion or conserved account invariant on the already saturated path; another unconstrained seed/rate sweep would not establish arbitrary eligibility. A074/A092 should challenge all old labels, both full child entropies, zero remainder identity and root reach weights.

# actual persistence receipts or precise save blocker

The four protocol files, code, frozen specs, exact outputs, witness bounds and local manifest are saved inside A071; STATUS has exactly two lines and WORKLOG/LEARNED retain the durable result. out/MANIFEST.json gives hashes and sizes, excluding itself; SCHEMA_VALIDATION records exact field sets and identical PROGRESS/PACKET_DELTA. All files are below20MB. Remote supervisor copy, registry adoption, independent acceptance and mirror verification remain unverified. No outside research mutation or deletion is performed.

# Universal bridge

This stage moves C019 stopping-tree payment through every prescribed next query after an actual sibling transfer: all60 full continuations retain the same rate4 debit and complete terminals, while36 exactly refute corrected-new-core-only payment. It supplies a saturated-child conservation invariant and an explicit positive shortfall, but no dimension-independent FEI constant. The unpaid bridge is noncircular child eligibility from inherited signed components under further transfers. NEXT attacks that precise obstacle on the existing spent account, rather than adding another isolated root class bound.
'''
    (ROOT/'REPORT.md').write_text(report,encoding='utf-8')
    (folder/'STATUS.md').write_text('STATE: A071 stage17 saved:60 SAME-rate4 spent-sibling next queries certified;36 corrected-new-core-only failures;47 independent states;FEI OPEN, review pending.\nNEXT: A089/A072 derive component eligibility on saturated transported account;A074/A092 review60 cases,old labels,both full terminals;no renewed reserves.\n',encoding='utf-8')
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    for name,text in [('WORKLOG.md',f'{now} | Stage17 consumes A089 spent sibling:60 alternatives all full children positive;36 selected-only shortfalls; independent product-moment47 states. Exact certificate saved in{run}; universal eligibility remains open.'),('LEARNED.md',f'{now} | After A089 minimal third-query transfer at rate4, all60 other-core next queries are full-capacity feasible but36 fail corrected-newly-queried-core-only debit. Witness b0,j1,i0 has shortfall in(31/1000,4/125) bits. If incoming D=S(parent), then mean S(children)=D+e, so full child allocation leaves exactly zero. This invariant is conditional on child nonnegativity; it does not prove FEI. Keep old debit2tau on the charged sibling and both full terminals.')]:
        with (folder/name).open('a',encoding='utf-8',newline='') as f:f.write('\n'+text+'\n')
    protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
    expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids');ck(set(progress)==expected)
    ck(set(claims[0])==set(protocol['required_per_run']['claim_fields']))
    ck((ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes())
    validation=dict(progress_fields_exact=True,claim_fields_exact=True,delta_identical=True,status_two_lines=len((folder/'STATUS.md').read_text(encoding='utf-8').splitlines())==2,statement_hash=h)
    (ROOT/'out/SCHEMA_VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
    manifest={}
    for p in ROOT.rglob('*'):
        if p.is_file() and p.name!='MANIFEST.json':
            ck(p.stat().st_size<20_000_000);manifest[str(p.relative_to(ROOT))]=dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    (ROOT/'out/MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(files=len(manifest),claim=claims[0]['claim_id'],failures_by_terminal=info['failures_by_terminal'],schema=validation)))

if __name__=='__main__':main()
