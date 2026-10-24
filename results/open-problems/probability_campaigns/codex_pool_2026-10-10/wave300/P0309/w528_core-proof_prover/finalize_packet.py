import datetime, json, pathlib, subprocess

ROOT=pathlib.Path(__file__).resolve().parent
validation=json.loads((ROOT/'VALIDATION.json').read_text(encoding='utf-8'))
assert validation['result']=='PASS' and validation['full_target_proved'] is False
assert validation['compute_gate']['status']=='consumed'
bundle=json.loads((ROOT/'bundle_001.json').read_text(encoding='utf-8'))
inbox=pathlib.Path('~/math-brain-inbox/w528')
target=inbox/'bundle_001.json'
assert target.parent.resolve()==inbox.resolve()
mesh='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
receipt=subprocess.run(['python','-X','utf8',mesh,'assert','--agent','w528','--resource',str(inbox)],capture_output=True,text=True,encoding='utf-8',errors='replace')
(ROOT/'INBOX_LEASE_ASSERT.json').write_text(json.dumps({'exit_code':receipt.returncode,'stdout':receipt.stdout,'stderr':receipt.stderr},indent=2)+'\n',encoding='utf-8')
assert receipt.returncode==0,'No live covering write lease; publication stopped.'
inbox.mkdir(parents=True,exist_ok=True)
payload=(ROOT/'bundle_001.json').read_bytes()
now=datetime.datetime.now(datetime.timezone.utc)
if target.exists():
    assert target.read_bytes()==payload,'Existing bundle differs; preserving it.'
    publication='ALREADY_PRESENT_IDENTICAL'
else:
    part=inbox/('bundle_001.w528.'+now.strftime('%Y%m%dT%H%M%S%fZ')+'.part')
    assert part.parent.resolve()==inbox.resolve()
    with part.open('xb') as out:
        out.write(payload);out.flush()
    part.rename(target)
    publication='ATOMIC_PART_RENAME'
assert target.read_bytes()==payload

life=json.loads((ROOT/'BUNDLE_LIFECYCLE.json').read_text(encoding='utf-8'))
life.update({'submitted':True,'submitted_utc':now.isoformat(),'submission_path':str(target),'publication_method':publication,'reviewed':False,'ingested':False,'retrievable':False})
(ROOT/'BUNDLE_LIFECYCLE.json').write_text(json.dumps(life,indent=2)+'\n',encoding='utf-8')
publish={'submission_path':str(target),'method':publication,'entries':len(bundle['entries']),'relations':len(bundle['relations']),'local_bytes_equal_published_bytes':True,'submitted_utc':now.isoformat(),'store_integration_run':False,'live_store_write_by_worker':False,'final_referee_review':'PENDING'}
(ROOT/'PUBLISH_RECEIPT.json').write_text(json.dumps(publish,indent=2)+'\n',encoding='utf-8')

hook={
    'id':'riesz-defect-moments-w528-01','area':'math','event':'PreToolUse',
    'cue':'A 3D Coulomb/Riesz proof infers volume-uniform absolute defect-interaction summability from charge neutrality alone, without vanishing dipoles or collective screening.',
    'fire_when':'Neutral particle-displacement defects are treated as absolutely summable in 3D Coulomb, with no first-moment or screening hypothesis.',
    'silent_when':'Both charge dipoles vanish with uniformly bounded radii/moments, or the proof explicitly supplies a collective, conditionally renormalized screening estimate.',
    'text':'For 3D Riesz defects, neutrality alone gives only r^(-s-2); absolute sums can diverge for 0<s<=1. Check both dipoles or a collective screening estimate before applying a contour bound.',
    'evidence':'w528/ATTEMPT.md L4-L5; w528/VALIDATION.json: 762 checks, exact cone controls; w529/PEER_VERDICT.jsonl KEEP L1-L6; memory scar perceptron_proof_open_gaps_fleet_2026_07_12.',
    'proposer':'w528'
}
assert len(hook['text'])<=300
hook_dir=ROOT/'proposals';hook_dir.mkdir(exist_ok=True)
hook_text=json.dumps(hook,ensure_ascii=False)+'\n'
(hook_dir/'math-w528.jsonl').write_text(hook_text,encoding='utf-8')
patch_dir=ROOT/'patches';patch_dir.mkdir(exist_ok=True)
live='~/primary_directive/hooks1000/proposals/math-w528.jsonl'
patch='--- a/'+live+'\n+++ b/'+live+'\n@@ -0,0 +1 @@\n+'+hook_text
(patch_dir/'01_math_w528_hook.diff').write_text(patch,encoding='utf-8')

progress={
    'event':'P0309 w528: seven scoped auxiliary proofs and the dipole/repair obstruction saved; six w529 KEEP verdicts; 762 bounded checks; DRAFT 9 entries/11 relations submitted; full Gibbs phase unproved.',
    'agent':'w528','row':'S1.P0309.w528','evidence':'~/brain_workers/w528/REPORT.md',
    'dispatch_state':'STAGED_FOR_COORDINATOR','reason':'Worker write scope allows its own folder and the explicitly named draft inbox; progress-page and global-hook mutations are staged for the reviewer.'
}
(ROOT/'PROGRESS_OUTBOX.jsonl').write_text(json.dumps(progress)+'\n',encoding='utf-8')

report=f'''Prepared P0309's exact source/prior-attempt digest, seven auxiliary proofs, and one explicitly unproved reconstruction input G. The original target remains unresolved; current openness is UNKNOWN.

The useful change is a precise defect-interaction boundary: in 3D Coulomb, neutral dipoles have a divergent absolute pair sum, while uniformly bounded dipole-free blocks have a summable bound. Actual displaced particles carry dipoles. A Gibbs repair must also preserve configuration volume; exact collapse to lattice sites cannot satisfy a finite pushforward-density bound.

Measurement command: python -X utf8 run_validation.py. {validation['total_checks']} checks passed, including 81 exact fourth-derivative identities, 124 rational atomic controls, and finite cone/shell controls. The run used {validation['compute_gate']['runtime_cpu_seconds']:.4f} CPU seconds, {validation['compute_gate']['runtime_wall_seconds']:.4f} wall seconds, and {validation['compute_gate']['peak_python_allocation_bytes']} peak traced allocation bytes under a fresh 5-second/16-MiB gate. For the stated Coulomb examples, R16-to-R32 decay exponents were {validation['measurements']['dipole_observed_decay_exponent_R16_to_R32']:.6f} for neutral dipoles and {validation['measurements']['quadrupole_observed_decay_exponent_R16_to_R32']:.6f} for dipole-free quadrupoles; their analytic exponents are 3 and 5. This compares different explicit hypotheses and measures no full-gas or recall improvement.

w529 independently kept L1-L6. Referee w530 received the packet (msg-2a4ca6fe94); its verdict and L7 review remain pending. These checks are not a formal proof of G.

Submitted DRAFT: {target.as_posix()} ({len(bundle['entries'])} entries, {len(bundle['relations'])} relations). Submitted, reviewed, ingested, and retrievable are separate in BUNDLE_LIFECYCLE.json. No worker store integration or live-store write occurred.

Application: after the required mathematical reviews, the validating coordinator may integrate the named DRAFT. Apply patches/01_math_w528_hook.diff to add the staged hook at its named live proposal path, preserving any existing file; run the hook's pair audit before deployment. PROGRESS_OUTBOX.jsonl is the one-line progress-page event for coordinator dispatch. Both global writes remain staged within the worker's write boundary.

Risk: dropping the first-moment hypotheses, the repair-map entropy bound, or the unperturbed-Gibbs requirement would turn these scoped results into a false full-phase claim. A positive crystalline energy gap, dipole screening, anharmonic coherence, and the Gibbs limit are still unproved inputs.

NEXT: Construct an admissible two-cell repair with an explicit dipole carrier and bound its exact energy loss and pushforward density.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')

review='''Referee w530: the complete reviewable packet is ATTEMPT.md, CLAIMS.jsonl, SOURCE_STATUS.json, P0309_EXTRACT.json, STATEMENT_FOR_ADVERSARY.md, bundle_001.json, RELATIONS_EVIDENCE.jsonl, VALIDATION.json, COMPUTE_GATE.json, PEER_REVIEW_RECEIPT.json, and BUNDLE_LIFECYCLE.json. REPORT.md gives the measured result and application route.

Review L1's Hessian norm, L2's fourth-derivative constant and factor 1/4, L3's uniform moment/radius assumptions, L4's cone lower bound and divergent exponent range, L5's exact moment obstruction, L6's actual-energy and pushforward requirements, and L7's null-image argument. Reject any interpretation that G or a crystalline Gibbs phase has been proved. The proof-repair event definition, energy gain, entropy cost, phase coherence, and genuine Gibbs limit remain inputs to a full route.

w529 kept L1-L6 within scope; PEER_REVIEW_RECEIPT.json records that distinct review. Final review and account-distinctness remain separate questions; no store integration is claimed. Any new mathematical result of referee w530 goes to independent referee w533.

Source fidelity is established only for the dated intake row and cited primary review; neither is a 2026 openness certificate. The deterministic checker proves its stated identities and finite controls, not G. There is no Lean/formal trusted-axiom receipt.

NEXT: Give per-claim KEEP/FIX/DROP verdicts for L1-L7 and an explicit NOT_PROVED verdict for the full target before store integration.
'''
(ROOT/'REVIEW_PACKET.md').write_text(review,encoding='utf-8')
print(json.dumps({'published':publish,'validation_checks':validation['total_checks'],'hook':'proposals/math-w528.jsonl','review_packet':'REVIEW_PACKET.md','G':'UNPROVED'},indent=2))
