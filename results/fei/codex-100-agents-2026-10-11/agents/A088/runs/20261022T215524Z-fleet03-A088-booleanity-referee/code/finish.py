from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,subprocess,os,re

RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1]
def write(p,s):
    p.parent.mkdir(exist_ok=True,parents=True)
    with p.open('w',encoding='utf-8',newline='\n') as f:f.write(s)
def dump(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def receipt(p):return {'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size}
NOW=datetime.now(timezone.utc).isoformat()
check=json.loads((RUN/'out/CHECK.json').read_text(encoding='utf-8'))
assert check['status']=='PASS' and check['helper_sha256']==sha(RUN/'code/check.py')
assert check['real_phase_count']==8008 and check['clean_states']==7380
source=OWN.parent/'A067/runs/20261021T224913Z-fleet03-A067-hypercontractive-refinement'
review=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert review['claim_id']=='A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK'
assert hashlib.sha256(review['exact_statement'].encode('utf-8')).hexdigest()==review['statement_sha256']
review['review_records'].append({'reviewer':'fleet03/A088','verdict':'HOLDS_AT_EXACT_CANONICAL_PHASE_SCOPE','independent':True,'substantive_repair':False,'source':str(RUN/'PROOF.md'),'validation':str(RUN/'out/CHECK.json'),'method':'Independent integer Walsh/physical edges; separate rational logs; literal real and Boolean scope guards; no source checker imported','note':'Prior A088 family attribution is retained; no source proof repair is supplied.'})
review['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'
def claim(cid,statement,hypotheses,deps,refutes):
    return {'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['fleet03/A088'],'proof_source':str(RUN/'PROOF.md'),'proof_dependencies':deps,'review_records':[],'status':'AUTHOR_PROOF_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':refutes,'first_unproved_line':None,'next_consumers':['A067','A070','A094','A038','A039','A096','B14','B18','B20']}
transport=claim('A088-CANONICAL-CLEAN-HISTORY-SIGNED-TRANSPORT','For every m>=2 in the canonical G_m of A067 v1, let D be the complete initial z entropy decrement and S its actual C=2 child bank. Its residual obeys delta/4<r=S-D<delta(m-1/4)<=7/128<1/16. Keep the edited z=- child and its complete original reference unchanged. For every finite adaptive stopping history querying only Y coordinates of the clean z=+ child, retain all old debit D and both children at every query. With clean reaches normalized to one, E_H=sum reach(Delta H-2 Inf)=2 E(number of live characters at the frontier); the final actual entropy bank equals S+E_H/2 and its combined debit D+E_H/2 leaves EXACTLY r. For the ORIGINAL clean uniform spectral reference, pushed forward through queries without reset, full terminal CE=number of unqueried Y coordinates; E_Q=sum reach(Delta CE-2 Inf)=E(2 I_leaf-CE_leaf), and the full inherited-reference bank equals S+E_Q/2, again leaving exactly r after combined debit D+E_Q/2. Terminal banks and debits remain signed. One first clean query has weighted entropy excess and bank increment 1/2, so a frozen-number withdrawal from r alone fails by more than7/16. No edited-child query or fresh-reference reset is paid.', ['Finite uniform actual Boolean cubes; canonical quadratic bent phase at marked all-zero point','m>=2; one physical z query, then arbitrary clean-child Y-only adaptive history, including partial stopping','The edited child and both full terminal costs are retained; no original bank or reference reset; all prior debits stay booked','References are original actual b,c spectra and the spectral-coordinate pushforward of the uniform clean reference; no new descendant reference is introduced'],[{'claim_id':review['claim_id'],'version':1,'acceptance_source':str(RUN/'PROOF.md')}],['Unregistered frozen numeric residual alone pays the next positive clean-query entropy excess at unchanged rate2'])
phase=claim('A088-FLAT-PHASE-MARKED-JET-SCOPE-DIAGNOSTIC','For a normalized real seed h on 2m uniform bits with flat Walsh coefficients sigma*2^-m and h(0)=1, form the same dummy-w point attachment and define j=1+sum_i h(e_i). Both actual z children and the root have norm one. Their root/edited entropy multiplicities equal the canonical bent multiplicities, while I_X=m+delta*j, and S_h=S+2delta(j-(2m+1)), r_h=r+2delta(j-(2m+1)). Thus the canonical payment extends beyond Booleanity whenever j=2m+1. At m=2 the negative Walsh masks {1,3,5,7,11,15} give a genuinely nonBoolean h with j=4 and both actual children certified H<=2I, but S_h>0 and r_h<0. In the exact8008-phase m=2 domain, child certification holds iff j>=2 and the >delta/4 payment iff j>=5. Actual Boolean seeds b_m*(-1)^Y1 at m=2,3 also have both certified terminals but r_h=r-4delta<0. Therefore flatness plus normalized children plus terminal certificates, or arbitrary Boolean bent phase, cannot replace the canonical incident-edge hypothesis. The original A067 statement is unchanged.', ['Real influence denotes squared physical derivative/Dirichlet energy, not pivotal probability','Uniform real flat phases with h(0)=1; all spectra and entropy include the informative w labels and complete z channel','The displayed real witness is m=2 only; the displayed Boolean tilted witnesses are m=2,3 only','No extension to arbitrary real fields or claim of a Boolean FEI counterfamily'],[],['Unregistered replacement of canonical phase by arbitrary normalized flat phase even with two C2-certified children','Unregistered replacement of canonical phase by arbitrary Boolean bent seed with positive marked point'])
claims=[review,transport,phase]
dump(RUN/'CLAIMS.json',claims)

mem=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30)
dump(RUN/'out/COMPUTE_ADMISSION.json',{'at':NOW,'exit_code':mem.returncode,'stdout':mem.stdout,'stderr':mem.stderr})
lean={'status':'BLOCKED_COMPUTE_ADMISSION','compiler_started':False,'scope':'Only additive cancellation on integers; no entropy or physical statement is formalized','source':receipt(RUN/'code/transport.lean'),'memok_exit_code':mem.returncode}
if mem.returncode==0:
    wrapper=Path(r'lean_check.py')
    text=wrapper.read_text(encoding='utf-8')
    options=re.findall(r'add_argument\([\s\S]{0,320}?(?:\n|\))',text)
    timeout_option=next((flag for flag in ['--timeout','--seconds','--max-seconds'] if any(flag in x for x in options)),None)
    if timeout_option:
        env=os.environ.copy();scratch=RUN/'out/lean_temp';scratch.mkdir(exist_ok=True);env['TEMP']=env['TMP']=str(scratch)
        cmd=[sys.executable,'-X','utf8',str(wrapper),'--file',str(RUN/'code/transport.lean'),'--target','A088_same_owner','--reviewed-sha256',sha(RUN/'code/transport.lean'),timeout_option,'40']
        result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace',env=env)
        write(RUN/'out/LEAN_STDOUT.txt',result.stdout);write(RUN/'out/LEAN_STDERR.txt',result.stderr)
        lean.update({'status':'VERIFIED_TARGET' if result.returncode==0 else 'UNVERIFIED_WRAPPER_RESULT','exit_code':result.returncode,'command':cmd,'stdout':result.stdout[-5000:],'stderr':result.stderr[-1500:],'compiler_started':'admission' not in result.stdout.lower()})
    else:lean['status']='UNVERIFIED_NO_BOUNDED_WRAPPER_OPTION';lean['note']='No compiler launched without a known internal time cap.'
dump(RUN/'out/LEAN.json',lean)

dump(RUN/'out/VALIDATION_REPAIRS.json',{'failed_pilot_executions':2,'observed_failure':'AssertionError: clean query terminal H','cause':'New continuation incorrectly treated character multiplication as adding one bit of Fourier entropy. It shifts labels and adds zero bits.','correction':'Both clean descendants have entropy2m-2; weighted excess and frontier bank increment are1/2, not1/4. Live-character surplus is2.','source_affected':False,'corrected_pilot':json.loads((RUN/'out/CHECK_pilot.json').read_text(encoding='utf-8')),'final_check_sha256':sha(RUN/'out/CHECK.json')})

context=[]
for p in (OWN.parent.parent/'context').glob('*.txt'):
    raw=p.read_bytes()
    try:s=raw.decode('utf-8');encoding='utf-8'
    except UnicodeDecodeError:s=raw.decode('cp1252');encoding='cp1252'
    terms=['Proposition 8.6','Lemma 2.1','shared','Boolean']
    excerpts=[]
    for term in terms:
        loc=s.find(term)
        if loc>=0:excerpts.append({'term':term,'offset':loc,'excerpt':s[max(0,loc-100):loc+500]})
    context.append({**receipt(p),'encoding':encoding,'role':'Retained baseline context, no new theorem premise or full-paper audit','excerpts':excerpts})
dump(RUN/'out/PAPER_CONTEXT.json',context)
critical=[source/'DERIVATION.md',source/'CLAIMS.json',source/'REPORT.md',OWN/'STATUS.md',OWN.parent.parent/'BOARD.md',OWN.parent.parent/'claude/B18/STREAM_NOTES.md']
dump(RUN/'out/CRITICAL_SOURCES.json',[receipt(p) for p in critical])

fields=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
old=json.loads((OWN/'runs/20261014T053751Z-fleet05-A088-booleanity-referee/PROGRESS.json').read_text(encoding='utf-8'))
progress={'protocol_revision':fields['revision'],'run_id':RUN.name,'stream':'B18','packet_id':'A088','gap_id':old['gap_id'],'attempt_id':'A088-resumed-canonical-bank-transport-v1','method':'Independent Boolean/real flat-phase scope audit; exact Walsh/edge and finite-state induction; same-owner signed reference transport','mathematical_delta':'A067 v1 independently HOLDS; canonical clean-child all-history residual preserved with inherited references; sharp finite phase/incident-edge diagnostic; full FEI OPEN.','deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF','mathematical_status':'SCOPED_AUDIT_ACCEPTED_NEW_RESULTS_PENDING_INDEPENDENT_REVIEW_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':review['claim_id'],'version':1,'statement_sha256':review['statement_sha256']}],'claims_created_or_changed':[{'claim_id':x['claim_id'],'version':x['version'],'status':x['status']} for x in claims],'source_artifacts':[str(RUN/'PROOF.md'),str(RUN/'out/CHECK.json'),str(source/'DERIVATION.md')],'next_consumers':['A067','A070','A094','A038','A039','A096','B14','B18','B20'],'next_action':'Expose one actual edited-child Y coordinate or prescribed reset using SAME signed inherited bank, original references, old D and both full terminals; A067/A070/A094 review.','stagnant_substantive_attempts':0,'blockers':['Full FEI and arbitrary-core payment OPEN','Fresh-reference reset and edited-child continuation unpaid','Supervisor copy and mirror adoption unverified'],'packet_ids':['A088']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)

report=f'''# exact target, quantifiers, hypotheses and units

A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK v1 HOLDS at its exact canonical-phase scope for every m>=2. The entire initial flag plus channel is paid from its actual rate-2 terminal bank. Two new scoped author results extend the SAME signed bank through every clean-child adaptive stopping history and identify the exact phase/incident-edge limitation. Entropy and reference cross entropy are bits; real relaxation influence is squared physical derivative energy. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2 in full; current BOARD snapshot22October22:07UTC, B18 notes v2, own rolling files and five substantive prior reports. Eleven later A088 directories contain only .final markers; their count is not mathematical evidence. The current23October14:49UTC endpoint supersedes the archived campaign endpoint. Campaign README/status/next actions, parsed claim/obstruction/packet indices, plan and supplement files supply orientation. Critical source: A067 run20261021T224913Z DERIVATION sections1-5, unchanged CLAIMS statement hash {review['statement_sha256']}. A070's run20261021T173219Z source-bound acceptance of the prior A088 obstruction is consumed as coordination evidence, not a new proof premise. Latest actual A038/A039/A031/A032/A066 reports were inspected to avoid repeating completed generic no-reset work. Context paper text versions were read at scope interfaces only; no fresh paper audit or theorem import is claimed. Source receipts identify exact bytes. One read-only multiwording math recall returned guards, no proof premise. Wake warned of stale personal-context notes; this was surfaced before reliance.

# complete derivation or exact first unsupported line

PROOF sections1-2 independently reconstruct the source four-cell entropy proof and m2/m3 boundaries, then establish the useful upper bound delta/4<r<delta(m-1/4)<=7/128. Section3 preserves the same residual under ALL clean-child physical adaptive histories. Actual clean restrictions have H=2k and I=k+l; characters have zero entropy. The first clean query exposes weighted entropy excess1/2 AND exactly1/2 terminal surplus, so frozen residual withdrawal fails but exact signed transport succeeds. Original clean uniform reference is pushed forward without reset; its full terminal CE equals the number of unqueried data coordinates. Both references, the untouched edited child, old z debit and signed terminal deficits remain. The generic no-reset identity is campaign background; this source-specific continuation is the new application.

Section4 tests the strongest useful flat real relaxation. Norm-one root and both physical z children, a flat seed spectrum, the positive marked point, and even two rate-2 terminal certificates do not ensure payment. The displayed six-negative-mask witness has j=4, positive terminal bank and negative bank-minus-decrement. The full8008-phase census isolates the threshold j. Conversely the source payment DOES extend to nonBoolean flat phases with matching summed incident jet, so its scalar proof is not a new all-phase Boolean mechanism. Actual Boolean affine tilts also refute the unregistered all-bent strengthening at m2,3. None refutes the exact canonical source or FEI.

First unsupported universal line: an actual edited-child Y query or prescribed fresh-reference conversion from this SAME already debited bank with both full terminal laws retained. The clean-history theorem does not certify that step or arbitrary-core FEI. Mathematical rung: analytic proofs and exact finite certificates; new results await independent review. Lean status: {lean['status']}; any verified target concerns integer additive cancellation only.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC precedes computation: roots m1..8 by exact multiplicities, literal roots and both terminals m1..4,7380 clean partial states/19068 physical transitions (all adaptive histories follow by induction),8008 four-bit flat phase assignments, and actual Boolean tilt fixtures m2,3. No symmetry quotient or dimension escalation. Final checker PASS: {check['checks']} exact assertions in {check['runtime_seconds']:.4f}s. Pilot PASS:56 assertions. Two earlier pilot executions caught the new character-entropy mistake; its correction and failure trace are preserved in VALIDATION_REPAIRS. No source claim was repaired. The final code additionally reconstructs the displayed real root/children literally, including norms and Dirichlet energy.

All comparisons use integer/Fraction arithmetic and outward rational log intervals:28 positive atanh terms, tail2z^57/[57(1-z^2)], power-of-two range reduction, and outward dyadic rounding2^-80. Printed decimals are descriptive. Separate literal Walsh and physical-edge paths verify the formulas. No source checker import. The full specification is96MB/180s, pilot60s; actual finite computation is small. Fresh memok result is saved; Lean evidence is recorded separately and no failed/blocked attempt is called a certificate. No GPU, detached worker, trading access, git, mail or other-agent mutation.

Commands from A088:

    python -X utf8 -B runs/{RUN.name}/code/check.py pilot
    python -X utf8 -B runs/{RUN.name}/code/check.py full
    python -X utf8 -B runs/{RUN.name}/code/finish.py

# proof dependencies and changed downstream conclusions

The A067 source statement/version/hash are unchanged, with an independent local HOLDS record and no substantive repair. Its attribution of the earlier A088 family remains; the source proof is independently reconstructed here. Source canonical-phase and all-m boundary hypotheses are essential. New transport uses that accepted source residual and explicit clean bent-factor restrictions. New phase diagnostics are self-contained finite/spectral calculations. No prescribed-reset theorem or universal potential is adopted. Shared registry and remote mirror updates remain unverified.

# one next mathematical action and independent reviewer

A067/A070/A094 should independently reconstruct PROOF sections2-4, particularly negative inherited terminal banks and the full normalized-real witness. Next expose one actual edited-child Y coordinate or one prescribed reference conversion using the SAME remaining bank, old D and both complete terminal laws. The clean branch is already closed for every adaptive history and should not be re-enumerated. The marked-point jet is a mandatory scope guard for any proposed arbitrary-bent extension.

# actual persistence receipts or precise save blocker

Four protocol files, proof, frozen specification, independent code, exact outputs, source/context hashes and validation-repair evidence are saved under the assigned A088 run. The finalizer validates field sets, source statement hashes, required headings, identical progress copies and size limits, and records actual readback receipts. Rolling STATUS has two lines, WORKLOG is appended and LEARNED gains durable scope facts. All research mutations are inside A088. Supervisor copying, remote mirror adoption, registry integration and independent acceptance of the two new results are unverified.

# Universal bridge

C019 and C024 advance by independently accepting the full post-core canonical flag/channel payment and preserving its exact unused residual through every clean-child adaptive history with the ORIGINAL references, old debit and both terminal laws. The phase census identifies why flatness and even certified children cannot replace the source incident-edge hypothesis; the matching-jet real extension shows exactly how far the current argument uses Booleanity. There is no new universal FEI constant. What remains is the edited-child query or prescribed fresh-reference reset from the SAME signed account. NEXT isolates that unpaid branch while retaining the already paid clean-history ledger, the shortest continuation toward a universal restriction payment rather than another controller-width bound.
'''
write(RUN/'REPORT.md',report)
write(OWN/'STATUS.md',f'STATE: A088 resumed stage saved: A067 canonical C2 child-bank independently HOLDS; all clean histories preserve SAME residual/reference;{check["checks"]} exact checks; phase/jet guard; FEI OPEN.\nNEXT: A067/A070/A094 review; query EDITED child or prescribe reset with SAME bank, original references, old D and both full terminals; clean histories closed.\n')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{NOW} — {RUN.name}: A067 canonical-bank v1 independently HOLDS; clean-child all-history signed transport, unchanged incoming reference and old z debit; 8008-phase exact scope census; {check["checks"]} exact checks PASS. Pilot caught/corrected character entropy error (no source repair). Lean {lean["status"]}; full FEI OPEN; remote adoption unverified.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:f.write('\nResumed canonical-bank audit: r=S2-Dz lies between delta/4 and delta(m-1/4)<=7/128. The first clean bent-pair query has weighted entropy excess1/2, and its full terminal bank increases by exactly1/2. Frozen residual withdrawal fails; signed terminal transport preserves r for every clean-child history. Original uniform spectral reference pushes forward to uniform remaining coordinates; retain signed terminal deficits. Characters shift spectra and add ZERO entropy. Flat real h(0)=1 seeds preserve all z-child norms and entropy groups; payment depends on j=1+sum h(e_i). Matching j extends the scalar proof to reals. At m2 negative Walsh masks{1,3,5,7,11,15} give j4, two C2-certified children, positive bank but negative residual. Canonical Boolean phase/nonpivotal marked edges cannot be replaced by arbitrary flat or bent phases; affine Boolean tilt fails m2,3. Edited-child/reference reset remains unpaid.\n')

expected=set(fields['required_per_run']['claim_fields'])
assert all(set(c)==expected for c in claims)
expected_progress={s.split(' (')[0] for s in fields['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all('# '+heading in report for heading in fields['required_per_run']['report_fields'])
for c in claims:assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
paths=[p for p in RUN.rglob('*') if p.is_file() and p.name!='SAVE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in paths)
dump(RUN/'out/SAVE_RECEIPT.json',{'at':datetime.now(timezone.utc).isoformat(),'status':'LOCAL_READBACK_VERIFIED','files':[receipt(p) for p in paths],'rolling':[receipt(OWN/n) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],'remote_copy':'UNVERIFIED','schema_checks':'PASS'})
print(json.dumps({'status':'LOCAL_READBACK_VERIFIED','checks':check['checks'],'lean':lean['status'],'files':len(paths),'phase_guard':check['real_guard']}))
