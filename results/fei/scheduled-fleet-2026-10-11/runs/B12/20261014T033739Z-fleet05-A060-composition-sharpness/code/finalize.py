from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,datetime

R=Path(__file__).resolve().parents[1]; A=R.parents[1]; B=A.parents[1]
protocol_file=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_file.read_text(encoding='utf-8'))
def write(name,obj):
    p=R/name; p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def receipt(p): return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def latest(agent): return sorted((B/'agents'/agent/'runs').glob('*'))[-1]
def shash(s,h): return hashlib.sha256(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode()).hexdigest()
sources=[protocol_file,B/'BOARD.md',B/'claude/B12/STREAM_NOTES.md',A/'STATUS.md']
sources += [latest(agent)/f for agent,fs in [('A059',['PROOF.md','PRIORITY_PROOF.md','CLAIMS.json']),('A087',['PROOF.md']),('A091',['POINT_CONTROL_PAYMENT.md','CLAIMS.json'])] for f in fs]
sources.append(A/'runs/20261014T004659Z-fleet05-A060-composition-sharpness/code/check.py')
write('out/SOURCE_RECEIPTS.json',{'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'note':'Save-time receipts for actually read sources; BOARD read at supervisor snapshot 2026-10-14 03:35 UTC; STATUS before this finalizer update.','sources':[receipt(p) for p in sources]})
checks={s:json.loads((R/'out'/('CHECK_'+s+'.json')).read_text(encoding='utf-8')) for s in ['pilot','main','reproduce']}
total=sum(c['assertions'] for c in checks.values()); assert total==2600
cv=json.loads((R/'out/CONTINUUM_CERTIFICATE.json').read_text(encoding='utf-8'))
g=cv['maximum_interval']; assert g['lo_num']*1000>4872*g['den']; assert g['hi_num']*1000<4873*g['den']

source_claim=next(c for c in json.loads((latest('A091')/'CLAIMS.json').read_text(encoding='utf-8')) if c['claim_id']=='A091-POINT-CONTROLLER-RESIDUAL-AND-BOUNDARY')
source_hash=source_claim['statement_sha256']
source_claim['review_records'].append({'reviewer':'A060','run_id':R.name,'verdict':'ACCEPT_AT_STATED_SCOPE_NO_SUBSTANTIVE_REPAIR','scope':'All source point-controller, exact terminal profile and stopped/resolved-boundary assertions at fresh-point/disjoint-core scope; inherited U and unresolved controller entropy remain unpaid.','proof':'REVIEW_A091.md','source_statement_sha256':source_hash,'source_file_sha256':receipt(latest('A091')/'CLAIMS.json')['sha256'],'validation':'Complete integer Walsh spectra, direct character reproduction, exact gate decrement and fine/coarse release; original scalar price and terminal profile independently reconstructed.'})
source_claim['status']='INDEPENDENTLY_REVIEWED_ACCEPTED_AT_STATED_SCOPE'
source_claim['proof_source']={'run_id':str(latest('A091')),'path':'POINT_CONTROL_PAYMENT.md','local_review':'REVIEW_A091.md'}
source_claim['statement_sha256']=shash(source_claim['exact_statement'],source_claim['hypotheses'])

s='For every actual live fresh point activation F=1+A_r(u-1), r>=1, uniform Boolean core u on a disjoint cube and entropy in bits, the single-core controller residual obeys 0<=D-kappa_coarse<=K_pt Inf, with EXACT optimal K_pt=12-(9/2)log2(3). Here q=2^-r, m=Eu, kappa_coarse=q(1-m^2); equality is attained by r=3,u=-1. For activation of an internal exclusive independent-core controller P, using its original fine-state reserve instead gives D-kappa_fine<=Gamma Inf, with EXACT optimal Gamma=max_(0<z<=1)[4-4z+Ppair(z)/z], Ppair(z)=eta((1-z)^2)+eta(z^2)-eta((1-2z)^2)/2. Its unique maximizing z lies in (1/8,1/4), satisfies Gprime(z)=0, and Gamma has certified rational enclosure in (4.872,4.873). The actual six-bit controller P negative on five-bit indices 0,...,6 and activated by one fresh point bit has z=7/32, kappa_fine=0 and residual ratio G(7/32)>K_pt, so the coarse sharp constant cannot be substituted into the fine-state ledger without its qL correction. Actual terminal Fourier entropy and influence are retained. Under tensor-closed additive per-factor ledger rules no fixed additive slack lowers either sharp constant or repairs this fine/coarse substitution.'
h=['Finite uniform physical cube; actual Boolean signs; every live remaining point block is fresh and disjoint from the actual remaining core/inner-controller cube; r>=1. Failed point branches are constant +1.', 'Coarse reserve uses the entire current core variance. Fine reserve uses actual exclusive-state probabilities and variances of disjoint independent Boolean data cores, constants allowed; internal controller entropy is not assumed paid.', 'D is actual Fourier entropy decrement across the queried physical gate bit, Inf its physical flip probability. eta(x)=x log2(1/x), zero terms omitted; z=0 is handled without division.', 'Sharp fine constant is a supremum over actual finite Boolean functions: dyadic internal negative measures approximate the unique continuum maximizer. Tensor statements require additive per-factor ledgers and tensor-closed hypotheses, not a different canonical single-core representation.']
new={'claim_id':'A060-SHARP-POINT-CONTROLLER-LEDGER-CONSTANTS','version':1,'exact_statement':s,'hypotheses':h,'statement_sha256':shash(s,h),'contributors':['A060'],'proof_source':{'run':R.name,'path':'PROOF.md','validation':['out/CHECK_main.json','out/CHECK_reproduce.json','out/CONTINUUM_CERTIFICATE.json']},'proof_dependencies':[{'claim_id':source_claim['claim_id'],'version':1,'scope':'Point residual and terminal interface independently accepted here; exact optimization self-contained.'},{'source':'A059 20261014T025828Z PROOF.md equations (1),(5)','scope':'Fine/coarse reserve convention and retained terminal difference independently reconstructed; no dependence on ordered-priority payment theorem.'},'Elementary entropy packets, exact Walsh/edge identities, logarithm derivative concavity and integer/rational sign certificates.'],'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Unversioned proposed substitution of single-core K_pt into the fine exclusive-state outer-point residual without the qL correction; actual six-bit witness.','Unversioned fixed-additive improvement of these sharp constants on tensor-closed additive-ledger rules.'],'first_unproved_line':None,'next_consumers':['A091','A090','A059','A057','A087','A064','B12','B20']}
write('CLAIMS.json',[source_claim,new])

next_action='Test the first out-of-priority later point query while an earlier core/fallback remains live, deriving exact fine R release and retained terminal profile; use A059 interrupted-priority formula as baseline and forbid coarse K_pt without qL. A091 primary/A090 alternate review the sharp constants and six-bit scope guard.'
p={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B12','packet_id':'A060','gap_id':'C019-controller-terminal-compatible-reserve','attempt_id':'A060-stage4-point-controller-constant-and-ledger-scope','method':'Independently accept existing point/terminal interface; compute actual full decrement rather than bound JS; prove scalar concavity and integer endpoint signs; certify fine-state maximum and a Boolean scope falsifier; direct character reproduction.','mathematical_delta':'Same-ledger single-core point-controller constant improves from 3+2/ln2 to exact K_pt=12-(9/2)log2(3). Fine-state point coefficient is instead sharp Gamma in (4.872,4.873); actual six-bit fine ratio exceeds K_pt. This is a coefficient improvement that survives tensorization, while fixed additive repairs do not. No universal FEI constant or arbitrary terminal payment is proved.','deliverable_status':'COMPLETE_SAVED_LOCALLY','mathematical_status':'SHARP_LOCAL_CONTROLLER_CONSTANTS_PROVED; C019_GENERAL_CONTROLLER_TERMINAL_PAYMENT_AND_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':source_claim['claim_id'],'version':1,'source_statement_sha256':source_hash,'review':'Independent acceptance at source stated scope; not a substantive repair.'},{'source':'A059 PROOF 20261014T025828Z','scope':'Fine/coarse qL and unresolved terminal grouping convention only.'}],'claims_created_or_changed':[{'claim_id':source_claim['claim_id'],'version':1,'change':'source statement preserved; independent review appended locally'},{'claim_id':new['claim_id'],'version':1,'change':'new narrow sharp-constant and necessary-ledger-scope bundle'}],'source_artifacts':['INTAKE.md','PROOF.md','REVIEW_A091.md','out/FROZEN_SPEC.json','out/SOURCE_RECEIPTS.json','code/check.py','code/a060_math.py','out/CHECK_pilot.json','out/CHECK_main.json','out/CHECK_reproduce.json','out/CONTINUUM_CERTIFICATE.json'],'next_consumers':new['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['No access or save blocker. Arbitrary internal-controller/repeated-fallback residual and inherited U plus actual unresolved terminal H-U-R still require one nonreused physical account. New sharpness review, adoption and mirrors unverified.'],'packet_ids':['A060']}
write('PROGRESS.json',p); (R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())

report=f'''# exact target, quantifiers, hypotheses and units

A060 B12 composition sharpness, stage 2026-10-14 03:37 UTC. Determine the exact controller coefficient at every actual live fresh point-activation query, and whether it survives replacing the single-core reserve by the original finer exclusive-state reserve. Uniform finite cubes, Boolean signs, entropy and KL in bits. Sharp local constants and the fine/coarse scope boundary are PROVED LOCALLY; full FEI and arbitrary controller-plus-terminal payment remain OPEN.

# sources actually read, revisions and theorem locators

Read full BOARD supervisor snapshot 2026-10-14 03:35 UTC, B12 STREAM_NOTES v2 (2026-10-11 23:30 UTC), own STATUS and full execution protocol revision {protocol['revision']}. Read latest A059 PROOF and PRIORITY_PROOF (20261014T025828Z), A087 PROOF (20261014T020842Z), A091 POINT_CONTROL_PAYMENT and CLAIMS (20261014T013816Z), and A059 CLAIMS. Sources are pinned in out/SOURCE_RECEIPTS.json. Earlier required campaign/paper readings remain in previous runs; no new external theorem or literature priority assertion is used. Own prior-stage exact rational utility is copied as a060_math.py and pinned; no source-author checker is imported.

A091 already pays point controllers, A087 already pays killed/independent children, and A059 already pays interrupted ordered priority controls. These closures are consumed rather than repeated. The source-independent review comes before the new narrow sharpness certificate, respecting the protocol/lead review cap. The stale original lead directions remain consistent with this current composition-sharpness target.

# complete derivation or exact first unsupported line

PROOF.md gives the exact entropy decrement D=2qV+2(q-2q^2)a^2+Ppair(z), z=q(1-m), rather than estimating its JS component. The single-core release is qV. Scalar derivative concavity, the exact endpoint inequalities 7^126>3^60*2^256 and 7^49>2^80*3^36, and elementary r=1,2 bounds prove

    0<=D-kappa_coarse<=K_pt Inf,
    K_pt=12-(9/2)log2(3), approximately 4.86766874675.

This is EXACT optimal: three point controls with constant core -1 attain equality. The actual successful terminal is a two-control point defect, whose entropy remains in D. The improvement from A091's 3+2/ln2 is about 1.01772 in the influence coefficient; it is not just an additive adjustment.

For the original fine-state reserve, the missing qL release from grouping the inner controller changes the optimum. The exact sharp coefficient is Gamma=max G(z), G(z)=4-4z+Ppair(z)/z. Strict concavity gives its unique maximizer in (1/8,1/4); 40 certified rational derivative bisections and a concave tangent bound enclose Gamma in (4.872,4.873), approximately 4.87232107178. A six-bit actual Boolean controller negative on internal indices 0,...,6 yields G(7/32)>K_pt with fine release zero. Its coarse release is 175/512, so the ratios differ by exactly 25/16. Actual terminal entropy H(P_internal)/2 and the full physical influence are retained. Importing K_pt into that finer ledger without qL is false.

The same witnesses tensorize for explicitly additive per-factor ledgers, so fixed additive slack cannot lower the sharp coefficients or repair the false substitution. A different canonical product representation or per-factor overhead is outside that conclusion. REVIEW_A091 independently accepts the original point-controller/profile/stopped-boundary claim without repair; the new stronger constants do not alter source authorship.

First unsupported universal line: pay arbitrary internal-controller/repeated-fallback residual and inherited U together with the actual unresolved terminal H-U-R from one unspent physical reserve. Neither optimized local coefficient resolves it, and the six-bit scope witness is not an FEI counterexample.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json precedes every search/check. Commands from this run: python -X utf8 code/check.py pilot; main; reproduce. Pilot: all 16 two-bit Boolean cores at gate widths 1,2,3, {checks['pilot']['assertions']} exact assertions PASS in {checks['pilot']['seconds']:.6f}s. Main: all 16 cores at widths 1,...,5, {checks['main']['assertions']} assertions PASS in {checks['main']['seconds']:.6f}s. Independent direct-character reproduction: widths 1,2,3 and the fine witness, {checks['reproduce']['assertions']} assertions PASS in {checks['reproduce']['seconds']:.6f}s. Every live gate coordinate is checked; no symmetry quotient or random sample. The six-bit fine witness is independently constructed and its complete root/child entropy reproduced. Total {total} exact assertions PASS, over 80 distinct coarse roots plus one fine root; pilot/reproduction revisit declared cases deliberately.

All spectra, physical edge influence, terminal identities and inequalities use integer transforms, exact Fraction probabilities, prime-log coefficient vectors and denominator-cleared integer-power signs. The continuum certificate uses 80 positive rational atanh terms with tail 2*z^161/[161*(1-z^2)] after range reduction. Forty derivative signs isolate the unique maximizer; strict concavity supplies the global bridge and tangent upper bound. Outward 100-bit dyadic endpoints are saved; no floating-point sign is used. Finite cases do not extrapolate to the theorem.

Memory estimate 100 MB, measured peak unclaimed. No >300 MB job or memok-gated launch was required. Jobs ran sequentially under the frozen 55-second cap, with no dimension escalation, assertion failure or precision escalation.

# proof dependencies and changed downstream conclusions

A091-POINT-CONTROLLER-RESIDUAL-AND-BOUNDARY@1 receives independent ACCEPT_AT_STATED_SCOPE without repair. Complete original statement and authorship remain unchanged; only this run's exported review/status changes. The improved point coefficient substitutes into the SAME coarse U,R stopped ledger, leaving its data coefficient and actual terminal profile unchanged. A059's fine/coarse qL identity is reconstructed and preserved: its fine outer-point step may use Gamma, but not K_pt without that correction. The interrupted/repeated-fallback and ordered-priority rate is not replaced by either constant.

A091/A059/A057/A064 should distinguish a quantitative coefficient gain from a different reserve debit. A087 can attach the sharp point constant only at the fresh point/coarse geometry; arbitrary killed-child, independent-child, shared-data and out-of-order repeated-core geometries do not inherit it automatically. No shared registry, other agent, brain or remote repository was modified. Downstream adoption and new independent acceptance are not observed.

# one next mathematical action and independent reviewer

{next_action} This removes the exact point-profile ambiguity before attacking the next controller geometry. Retain both actual children and terminal entropy; do not replace the fallback by an independent copy or repeatedly fund the variance bank.

# actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS, byte-identical PACKET_DELTA, proof/review, frozen spec, code and exact outputs are saved only in this assigned run. STATUS has two lines; WORKLOG/LEARNED append dated mathematical facts. out/SCHEMA_VALIDATION.json checks protocol keys, claim hashes and compatibility; out/PERSISTENCE_RECEIPT.json records local readback lengths and SHA256. Every file is below 20 MB. No local save blocker. New theorem review, registry adoption, supervisor copying, mirror verification and public release remain unverified.

# Universal bridge

This stage moves C019 stopping-tree payment at the composition-sharpness interface by improving the same single-core point-controller coefficient from 3+2/ln2 to exact K_pt=12-(9/2)log2(3), and sharpening the finer point-gate coefficient to Gamma in (4.872,4.873) while certifying an actual six-bit obstruction to conflating the two ledgers. The coefficient gains survive tensorization, whereas fixed additive repairs do not. Arbitrary internal/repeated-fallback queries, inherited U and unresolved actual terminal H-U-R remain unpaid; no universal FEI constant follows. NEXT tests the first later priority query with an earlier live fallback under its original fine reserve, the shortest new compatibility step because point-gate constants are now exhausted and another isolated point class would not address the remaining universal payment.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A060 stage4 saved: exact sharp coarse point residual K=12-(9/2)log2(3); fine optimum in (4.872,4.873), six-bit scope counterexample; A091 independently accepted; 2600 exact checks PASS; FEI OPEN.\nNEXT: A091/A090 review; test first out-of-priority later control with earlier live fallback, original fine R release and retained terminals; coarse K cannot replace fine debit without qL.\n',encoding='utf-8')
log='\n2026-10-14 03:37 UTC stage '+R.name+': Read new board and A059/A087/A091 sources. Independently accepted A091 point/profile theorem without repair. Exact actual decrement yields sharp coarse K=12-(9/2)log2(3), equality r3 core-1. Fine outer-point optimum Gamma in(4.872,4.873), actual six-bit G(7/32)>coarseK; fine/coarse release ratios differ25/16 with terminal H(P)/2 retained. Concavity plus 40 rational bisections certificates; 2600 exact assertions PASS including direct-character reproduction. Fixed additive slack cannot repair under additive tensor rules. Full FEI remains open; saved locally, review/adoption/mirror pending.\n'
if R.name not in (A/'WORKLOG.md').read_text(encoding='utf-8'):
    with (A/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(log)
lesson='\n2026-10-14 03:37 UTC ('+R.name+'): Point activation q=2^-r,m=Eu,a=1-m,z=qa,V=1-m² has exact D=2qV+2(q-2q²)a²+Ppair(z). Coarse releaseqV gives ratio2+(1/q-4)z+Ppair/z and EXACT uniform sharp K=12-(9/2)log2(3), r3/u=-1. Fine releaseqVbar instead has sharp Gamma=max[4-4z+Ppair/z]~4.87232107178 at unique z~.22944127608. q=.5, five-bit P negativeindices0..6 gives six-bit fine ratio>coarseK, kfine0,kcoarse175/512, difference25/16; terminalH(P)/2 remains. A059 qL grouping correction is essential. Fixed additive improvements disappear only for tensor-closed additive factor-ledger rules. Point gate constants do not automatically transfer to repeated-fallback/out-of-order/shared-data geometry. A091 source original3+2/ln2 valid independently reviewed, not repaired; improved coefficients are additional A060 results.\n'
if R.name not in (A/'LEARNED.md').read_text(encoding='utf-8'):
    with (A/'LEARNED.md').open('a',encoding='utf-8') as f: f.write(lesson)

required=protocol['required_per_run']
assert set(p)=={k.split(' (')[0] for k in required['progress_fields']}
for c in [source_claim,new]:
    assert set(c)==set(required['claim_fields'])
    assert c['statement_sha256']==shash(c['exact_statement'],c['hypotheses'])
assert all('# '+h in report for h in required['report_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
write('out/SCHEMA_VALIDATION.json',{'status':'PASS','protocol_fields':'exact claim keys and normalized progress keys','statement_hashes':'PASS','packet_compatibility':'byte-identical','report_fields':'all present','rolling_status':'two lines','assertions':total,'new_review_status':'pending','remote_mirror':'unverified'})
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
write('out/PERSISTENCE_RECEIPT.json',{'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'local readback only','artifacts':[receipt(p) for p in files],'rolling':[receipt(A/f) for f in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'saved_files':len(files),'schema':'PASS','assertions':total,'report':str(R/'REPORT.md'),'fine_maximum_approx_only':[g['lo_num']/g['den'],g['hi_num']/g['den']]}))
