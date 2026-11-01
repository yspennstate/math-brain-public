"""Save the completed source-bound stage and verify local byte receipts."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
ROOT=AGENT.parents[1]
RID=RUN.name
PROTOCOL=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')

def read(path):
    return path.read_text(encoding='utf-8')

def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding='utf-8',newline='\n')

def save(path,value):
    write(path,json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    protocol=json.loads(read(PROTOCOL))
    tests={name:json.loads(read(RUN/'out'/f'{name}.json')) for name in ['PILOT','QUADRATIC','CUBIC','INDEPENDENT','SCALAR']}
    assert all(v['status']=='PASS' for v in tests.values())
    total=sum(tests[x]['exact_assertions'] for x in ['QUADRATIC','CUBIC','INDEPENDENT','SCALAR'])
    assert tests['QUADRATIC']['cases']==32768 and tests['CUBIC']['cases']==8800 and tests['INDEPENDENT']['cases']==32768
    stamp=datetime.now(timezone.utc).isoformat()
    sources=[(PROTOCOL,'all rules and exact schemas'),
      (ROOT/'BOARD.md','startup B01 and relevant agent rows; mutable board snapshot hash'),
      (ROOT/'claude'/'B01'/'STREAM_NOTES.md','all B01 lead notes'),
      (ROOT/'agents'/'A052'/'runs'/'20261023T120425Z-fleet03-A052-critical-source-structure'/'ALIGNMENT_PROOF.md','Sections1--7; analytic reconstruction in REVIEW_A052.md'),
      (ROOT/'agents'/'A052'/'runs'/'20261023T120425Z-fleet03-A052-critical-source-structure'/'CLAIMS.json','claim version and exact scope'),
      (ROOT/'agents'/'A055'/'runs'/'20261023T112023Z-fleet03-A055-extremal-obstruction-referee'/'PROOF.md','Sections1--5; Sections1--3 independently reconstructed'),
      (ROOT/'agents'/'A055'/'runs'/'20261023T112023Z-fleet03-A055-extremal-obstruction-referee'/'CLAIMS.json','claim version and exact scope'),
      (AGENT/'runs'/'20261023T035753Z-fleet03-A005-noncircular-endpoint-referee'/'DERIVATION.md','prior-stage paid-pair embedding, previously independently accepted by A055')]
    receipts=[]
    for path,scope in sources:
        data=path.read_bytes()
        data.decode('utf-8')
        receipts.append(dict(path=str(path),sha256=sha(data),bytes=len(data),scope=scope))
    save(RUN/'out'/'SOURCE_RECEIPTS.json',dict(observed_utc=stamp,sources=receipts))
    write(RUN/'out'/'PREVIOUS_STATUS.txt',read(AGENT/'STATUS.md'))
    deps=['A005-PAID-PAIR-WEAK-AFFINE-CORE-HARDNESS@1: prior DERIVATION Sections2--6, already independently accepted by A055',
          'A055-SIMULTANEOUS-ABSOLUTE-CHILD-BANK-COLLAPSE@1: PROOF Sections1--3, scoped independent acceptance without repair in REVIEW_A055.md',
          'Elementary conditional Fourier entropy, physical-edge XOR identity, and minimum distance of F2 polynomials; fully proved here']
    used=deps+['A052-FINITE-PHASE-ORIGINAL-PAIR-ALIGNMENT@1: contextual endpoint; analytic scope independently accepted in REVIEW_A052.md; not needed for the phase-gap proof']
    statement=('For every finite uniform Boolean sign f, delta=P(f=-1), integer d>=1, K>=0 and phase q=(-1)^P of F2 degree<=d with r essential physical coordinates, H(qf)-H(f)<=r, I(qf)-I(f)>=r(2^(1-d)-4delta), and D_K(qf)-D_K(f)<=-r[K(2^(1-d)-4delta)-1]. If K>2^(d-1) and delta<(2^(1-d)-1/K)/4, f is globally deficit-optimal under all degree<=d output phases; if input-affine-influence-minimal, it is globally optimal in the joint affine/phase orbit. For each fixed K>max(2^(d-1),16/5) and epsilon>0, FEI(K) on full-span affine minima that are globally optimal in this joint finite orbit, have I<epsilon, an explicitly paid ORIGINAL pair, and N_A*<epsilon and abs(S_A*)<epsilon for EVERY proper original block is equivalent to full FEI(K) at SAME K. The reviewed Q-times-tensor-seed whole-product activation supplies this admission with H/I tending to the canonical seed ratio, at least the original seed ratio. A violating seed also yields own-ratio orbit optimality eventually, yet its paid-pair reserve remains strictly negative with relative terminal debt bounded away from zero. An explicit degree k+max(2,deg(g)) output phase erases activation and improves D eventually for a violating seed; unrestricted-degree optimality is not claimed. In particular fixed cubic-phase optimality at K>4 does not remove the arbitrary rare-core obstruction; exact nonnegative smaller-child reserves remain unproved in this embedding.')
    claim=dict(claim_id='A005-RARE-CORE-BOUNDED-PHASE-NORMAL-FORM',version=1,exact_statement=statement,
      hypotheses=['Finite uniform Boolean signs, entropy bits, actual complete signed Walsh spectrum',
        'Phase degree is multilinear F2 polynomial degree, not Fourier degree; essential-coordinate count r is physical in the current chart',
        'Joint orbit optimality requires actual input-affine influence minimality; no history bank is renewed',
        'Endpoint equivalence uses fixed K>max(2^(d-1),16/5), fixed finite d, and the previously reviewed complete paid-pair embedding',
        'All original block reaches, full child entropies and affine minima are retained; N_A* is expected positive terminal debt',
        'Positive seed deficit statements are conditional; no high-K positive seed or full FEI disproof is asserted'],
      statement_sha256=sha(statement.encode('utf-8')),contributors=['fleet03/A005'],
      proof_source=['PROOF.md Sections1--6','code/check.py','code/independent.py','out/QUADRATIC.json','out/CUBIC.json','out/INDEPENDENT.json','out/SCALAR.json'],
      proof_dependencies=deps,review_records=[],status='AUTHOR_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_AGENT_REVIEW',
      supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A052','A055','A051','A002','A090','A094','B20'])
    save(RUN/'CLAIMS.json',[claim])
    next_action='A052/A055 independently reconstruct the phase gap, then prove what EXACT nonnegative smaller-child reserves add to signed cubic alignment to force one ORIGINAL pair funded by UNUSED independent quotient rank from the SAME bank; all mixed rows retained.'
    progress=dict(protocol_revision=protocol['revision'],run_id=RID,stream='B01',packet_id='A005',
      gap_id='C019-CRITICAL-ORIGINAL-PAIR-LOWER-FUNDING',attempt_id='A005-stage20-bounded-phase-normal-form-admission',
      method='Independent A052/A055 analytic reviews; conditional Fourier-label entropy bound plus Reed-Muller minimum distance and physical influence overlap bound; apply reviewed whole-product activation',
      mathematical_delta=f'Fixed-degree phase normal form does not exclude arbitrary rare cores. Cubic K>4 threshold delta<(K-4)/(16K); joint orbit maximum and own-ratio admission retain ORIGINAL paid pair and all-block small absolute banks. Explicit growing-degree activation eraser identifies limit. {total} exact assertions PASS; universal FEI constant gain0.',
      deliverable_status='COMPLETE_LOCAL_VERIFIED',mathematical_status='FULL_FEI_OPEN; new endpoint theorem author-proved and exact-validated; independent-agent review pending',
      claim_versions_used=used,claims_created_or_changed=[claim['claim_id']+'@1'],
      source_artifacts=['PROOF.md','REVIEW_A052.md','REVIEW_A055.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/QUADRATIC.json','out/CUBIC.json','out/INDEPENDENT.json','out/SCALAR.json'],
      next_consumers=claim['next_consumers'],next_action=next_action,stagnant_substantive_attempts=0,
      blockers=['Exact nonnegative complete smaller-child reserves still fail for arbitrary-seed activation; high-K genuine-critical original-pair funding remains unproved',
        'New theorem independent-agent acceptance, registry adoption and supervisor remote copying not verified',
        'Brain self-care degraded/unverified: wake owner model99.8h, state84.4h and dream35.1h stale; personal context and memory consolidation affected',
        'Compute snapshot remained stale at2026-10-23 13:57:59 local; no fresh governor admission or current capacity inferred; no heavy job used'],packet_ids=['A005'])
    save(RUN/'PROGRESS.json',progress)
    (RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
    fields=protocol['required_per_run']['report_fields']
    paragraphs=[
      'Determine whether an arbitrary Boolean seed survives A052\'s new global cubic-phase/affine normal form. PROOF.md proves the more general finite degree d phase gap, with all entropy in bits and physical influence. At fixed K>4, delta<(K-4)/(16K) grants cubic-phase optimality automatically to an input-affine minimum. Apply this to the SAME rare-core root and ORIGINAL paid pair; no displayed-child criticality or new bank is assumed.',
      'EXECUTION_PROTOCOL.json rev2026-10-11-execution-v2; startup BOARD.md, B01 STREAM_NOTES.md and own stage19 STATUS. A052 ALIGNMENT_PROOF Sections1--7 and CLAIMS@1; A055 stage19 PROOF Sections1--5 and CLAIMS@1; prior A005 paid-pair DERIVATION Sections2--6. Exact source hashes and locators are in out/SOURCE_RECEIPTS.json. Earlier campaign/paper baseline remains as read in prior stages; it was not re-advertised as a new reading. The owner\'s revised14:49UTC campaign deadline governs over the older protocol date.',
      'PROOF.md is the complete argument: preserve outside Fourier marginal under a phase using r inputs, bound conditional entropy gain by r; use derivative XOR to lower-bound influence gain by I(q)-4delta*r; use nonzero F2-polynomial minimum distance to get I(q)>=2^(1-d)r. This yields strict deficit loss r[K(2^(1-d)-4delta)-1]. The joint affine orbit follows without replacing the root. Reviewed activation gives SAME-K endpoint equivalence, ratio limit and negative exact terminal reserve. Section6 supplies the explicit growing-degree eraser. FIRST UNSUPPORTED UNIVERSAL LINE: exact nonnegative complete smaller-child reserves plus signed cubic alignment force unused independent quotient-rank payment on one ORIGINAL pair of a genuine high-K least-dimensional witness. No proof of that line is supplied.',
      f'Frozen spec out/FROZEN_SPEC.json precedes all jobs; preflight changed cubic K8 to16 before execution because the former had zero strict margin. Pilot:11 cases,99 assertions PASS in {tests["PILOT"]["seconds"]:.3f}s. Main:all2048 quadratic phases on all16 point roots (32768 cases,{tests["QUADRATIC"]["exact_assertions"]} assertions,{tests["QUADRATIC"]["seconds"]:.3f}s);275 prescribed cubic phases on all32 five-bit point roots (8800 cases,{tests["CUBIC"]["exact_assertions"]} assertions,{tests["CUBIC"]["seconds"]:.3f}s). Separate direct-character helper:all256 three-bit Boolean roots times128 quadratic phases (32768 cases,{tests["INDEPENDENT"]["exact_assertions"]} assertions,{tests["INDEPENDENT"]["seconds"]:.3f}s). Two scalar checks certify point8 gap>1/256 and new quadratic phase gap>3/4 at K15/4,k10000. Total {total} exact mathematical assertions, excluding pilot. Commands: python -X utf8 -B code/check.py pilot; quadratic; cubic; and python -X utf8 -B code/independent.py. Integer spectra/edges and Fraction logarithm enclosures; floats only report elapsed seconds. Each run<55s, estimated memory<30MB; no job>300MB, no GPU or detached work. Finite cubic orbit is NOT fully enumerated; the general theorem is analytic.',
      'New A005-RARE-CORE-BOUNDED-PHASE-NORMAL-FORM@1 depends on the already reviewed paid-pair embedding and A055\'s all-block guard, not on an FEI assumption. REVIEW_A055 independently accepts Sections1--3 without repair, excluding its huge finite certificate. REVIEW_A052 independently accepts finite-source normalization, original singleton/pair mixed-row costs, full-bank invariance and bent corollary, excluding census/maximality numerics. These are scoped analytic reviews, not new acceptance of the entire dependency chain. New theorem independent-agent review remains pending. The cubic condition is valid but cannot by itself exclude the rare-core failure; exact child eligibility must contribute essentially.',
      next_action+' A052 and A055 are the requested independent reviewers and consumers; this local source-bound request sends no external message.',
      'All requested products are saved under this run only. out/PERSISTENCE_RECEIPTS.json records SHA256 and sizes; out/VERIFY.json records readback, schema, claim-hash and compatibility checks. STATUS is exactly two lines; WORKLOG and LEARNED appended. Supervisor copying, remote mirrors and brain ingestion remain UNVERIFIED; no git or shared-tree write was made. Brain self-care is degraded/unverified: owner context and memory consolidation remain affected. Stale governor data was not treated as current resource permission.'
    ]
    report='# A005 stage20: rare cores already satisfy bounded-degree phase optimality\n\n'
    report+='\n\n'.join('## '+field+'\n\n'+text for field,text in zip(fields,paragraphs))
    report+='\n\n**Universal bridge.** C019 critical original-pair payment is sharpened by eliminating a new false escape hatch: at fixed K>4, global cubic-phase/affine optimality still admits the SAME arbitrary rare core, paid original pair and simultaneously tiny absolute child banks. The universal constant improves by0; exact nonnegative smaller-child reserves and independent unused quotient-rank funding remain essential. NEXT isolates how those exact reserves strengthen signed pair alignment, the shortest surviving route to full FEI rather than another isolated function class.\n'
    write(RUN/'REPORT.md',report)
    handoff=f'''A005 stage20 | {stamp}
NEW: {claim['claim_id']}@1. Cubic phase global deficit maximum is automatic for an affine minimum with delta<(K-4)/(16K), K>4. All fixed-degree phase normal forms admit SAME arbitrary rare-core/paid-pair embeddings. Exact terminal nonnegativity remains the obstruction.
PROOF.md Sections1--3: review phase-marginal entropy bound, physical XOR cost, polynomial minimum distance, joint finite orbit. Sections4--6: reviewed-seed application, own-ratio version and growing-degree eraser. Actual quadratic extension of point8 certificate has gap>3r/4 at K15/4.
A052/A055: independently reconstruct new proof; then supply the missing implication from exact nonnegative complete smaller-child reserves to UNUSED quotient-rank payment on an ORIGINAL pair at high K. Normal form alone cannot do it.
SCOPED ACCEPTANCES: A052 analytic finite-phase alignment including ORIGINAL pair, no repair; A055 Sections1--3 all-block guard/application, no repair. See REVIEW files for exclusions.
VALIDATION: {total} exact assertions PASS; no high-K counterexample or full FEI proof. All products local; remote copying and new theorem independent-agent review pending. Brain self-care degraded/unverified.
'''
    write(RUN/'HANDOFF.txt',handoff)
    write(AGENT/'STATUS.md',f'STATE: A005 stage20 saved: cubic-phase normal form at K>4 admits SAME arbitrary paid rare core; {total} exact checks PASS; scoped A052/A055 reviews HOLD; FEI OPEN.\nNEXT: A052/A055 review new phase gap, then prove EXACT nonnegative smaller-child reserves force ORIGINAL-pair unused quotient-rank payment from SAME bank.\n')
    additions={
      'WORKLOG.md':f'\n{stamp} | stage20 {RID}: consumed cubic phase endpoint; independently reconstructed A052 analytic original-pair alignment and A055 all-block guard without repair. Proved phase entropy gain<=r, influence gain>=r(2^(1-d)-4delta), hence rare activated arbitrary seeds already globally joint phase/affine optimal at K>2^(d-1). SAME original paid pair, all-block approximate reserves and ratio limits survive. Exact child nonnegativity still fails; growing-degree eraser identifies degree limit. {total} exact assertions PASS, pilot99 excluded; new independent-agent review and supervisor copying pending. Brain self-care degraded; no heavy compute.\n',
      'LEARNED.md':'\n'+stamp+' | Phase admission: for delta=P(f=-1), deg_F2(q)<=d and r essential physical q coordinates, H(qf)-H(f)<=r because outside Fourier marginal is preserved; I(qf)-I(f)>=r(2^(1-d)-4delta). Thus gamma=K(2^(1-d)-4delta)-1>0 makes f a global degree-d phase maximum, also joint affine maximum if input-affine I-minimal. Cubic K>4 threshold delta<(K-4)/(16K). Rare whole-product activation already satisfies it without changing the ORIGINAL pair/bank, so signed cubic stationarity alone does not fix negative exact child reserves. Output phase(1+A)*P_G erases activation at degree k+deg(P_G), explaining failure for unbounded phase degree. A052 analytic pair cost factor1/4 and A055 all-block guard independently reconstructed without repair; numerical censuses outside these review scopes.\n'
    }
    for name,text in additions.items():
        with (AGENT/name).open('a',encoding='utf-8',newline='\n') as handle:
            handle.write(text)
    assert len(read(AGENT/'STATUS.md').splitlines())==2
    required=protocol['required_per_run']
    expected_progress={x.split(' (')[0] for x in required['progress_fields']}
    assert set(progress)==expected_progress
    assert set(claim)==set(required['claim_fields'])
    assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
    assert sha(claim['exact_statement'].encode('utf-8'))==claim['statement_sha256']
    for field in fields:
        assert '## '+field+'\n' in report
    excluded={'out/PERSISTENCE_RECEIPTS.json','out/VERIFY.json'}
    records=[]
    for path in sorted(RUN.rglob('*')):
        if path.is_file() and path.relative_to(RUN).as_posix() not in excluded:
            data=path.read_bytes()
            assert len(data)<20_000_000
            records.append(dict(root='run',path=path.relative_to(RUN).as_posix(),bytes=len(data),sha256=sha(data)))
    for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
        data=(AGENT/name).read_bytes()
        records.append(dict(root='agent',path=name,bytes=len(data),sha256=sha(data)))
    save(RUN/'out'/'PERSISTENCE_RECEIPTS.json',dict(observed_utc=stamp,files=records,scope='LOCAL bytes only; no remote/mirror/brain acceptance receipt'))
    for record in records:
        path=(RUN if record['root']=='run' else AGENT)/record['path']
        assert sha(path.read_bytes())==record['sha256']
    verification=dict(status='PASS',files_verified=len(records),mathematical_assertions=total,pilot_assertions_excluded=99,
      schemas='exact protocol keys',compatibility='PROGRESS and PACKET_DELTA byte-identical',
      claim_statement_sha='PASS',status_line_count=2,remote='UNVERIFIED',brain_selfcare='DEGRADED_UNVERIFIED',observed_utc=stamp)
    save(RUN/'out'/'VERIFY.json',verification)
    print(json.dumps(verification))

if __name__=='__main__':
    main()
