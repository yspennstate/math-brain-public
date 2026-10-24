from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,datetime

R=Path(__file__).resolve().parents[1]; A=R.parents[1]
B=A.parents[1]
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
def write(name,obj):
    p=R/name; p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def digest(p): return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def latest(a): return sorted((B/'agents'/a/'runs').glob('*'))[-1]

source=[protocol_path,B/'BOARD.md',B/'claude'/'B12'/'STREAM_NOTES.md',A/'STATUS.md']
source += [latest(a)/f for a,fs in [('A057',['REPORT.md','PROOF.md']),('A091',['REPORT.md','OVERLAP_INTERFACE.md']),('A056',['REPORT.md']),('A058',['REPORT.md']),('A078',['REPORT.md']),('A038',['REPORT.md']),('A059',['REPORT.md','PROOF.md','CLAIMS.json'])] for f in fs]
write('out/SOURCE_RECEIPTS.json',{'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'note':'Save-time byte receipts for actually read sources; board read snapshot was 2026-10-14 00:40 UTC. A060 STATUS pinned before this finalizer updates it.','sources':[digest(p) for p in source]})
results={mode:json.loads((R/'out'/f'checks_{mode}.json').read_text(encoding='utf-8')) for mode in ['pilot','main','reproduce']}
boundary={mode:json.loads((R/'out'/f'boundary_{mode}.json').read_text(encoding='utf-8')) for mode in ['pilot','main']}
total=sum(x['assertions'] for x in results.values())+sum(x['assertions'] for x in boundary.values())
assert total==1763
fixture=next(x for x in results['main']['tables'] if x['r']==4)['residual_per_spent_influence']
assert Q(fixture['lo_num'],fixture['den'])>4
assert Q(fixture['hi_num'],fixture['den'])<Q(41,10)
write('out/FIVE_BIT_STRICT_CERTIFICATE.json',{'statement':'Even r=4, hence five physical inputs, has (D_y-R_drop-U_drop)/Inf_y>4 and <41/10.','certificate':fixture,'checks':'Exact integer comparison lo_num>4*den, 10*hi_num<41*den; endpoints outward-rounded from certified rational logs.'})

src=json.loads((latest('A059')/'CLAIMS.json').read_text(encoding='utf-8'))[0]
source_claim_hash=src['statement_sha256']
src['review_records'].append({'reviewer':'A060','run_id':R.name,'verdict':'ACCEPT_AT_STATED_SCOPE','scope':'Exact U,R controller/data identities and signed DATA inequality (6); no universal payment of controller/terminal residual or blanket review of every bundled assertion.','proof':'REVIEW_A059.md; critical actual spectra independently reconstructed by direct character sums and integer FWHT.','source_statement_sha256':source_claim_hash,'source_file_sha256':hashlib.sha256((latest('A059')/'CLAIMS.json').read_bytes()).hexdigest()})
src['proof_source']={'run':str(latest('A059')),'path':'PROOF.md','locators':'Sections 1-3 for scoped review; source statement and whole-claim pending status preserved'}

statement='For even r>=4, q=2^-r and the actual Boolean F(z,y)=(-1)^(sum paired z_i z_(i+1))+(y-1)1[z=0], querying its independent dictator core gives U_drop=0, R_drop=qr, Inf_y=q and signed residual E_r=D_yH-R_drop. It satisfies (19/6)q/ln2 <= 3/ln2-E_r/q <= 8q/((1-4q)ln2). Therefore A059\'s signed DATA coefficient 3/ln2 is sharp for its stated ledger and independent-core class. For disjoint tensor copies with the additive per-factor U,R ledger, no K<3/ln2 can hold with a fixed additive constant. Separately, the balanced shared-core fair mux of u=x and v=x(1-2*1[w=0]) has nominal R=1 and actual controller influence 2^-t, hence no finite control-only funding of that same reserve survives removal of the independence hypothesis; actual root/terminal Fourier entropy and influence are retained in the proof.'
hyp=['Uniform finite physical cubes, Boolean sign outputs, entropy in bits; bent construction has even r>=4 and one independent dictator core, constants allowed as exclusive selector states.', 'Tensor conclusion refers to tensor-closed payment rules using additive per-factor U,R; it does not assume the canonical single-core ledger of a product is additive.', 'The independence boundary has integer t>=1, one shared physical bit x and fresh private w; it deliberately falls outside the independent-core theorem and refutes only an extension retaining the same nominal reserve.']
def statement_hash(s,h): return hashlib.sha256(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode()).hexdigest()
new={'claim_id':'A060-SIGNED-DATA-DRIFT-SHARPNESS','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':statement_hash(statement,hyp),'contributors':['A060'],'proof_source':{'run':R.name,'path':'PROOF.md','additional':'INDEPENDENCE_BOUNDARY.md; out/checks_main.json; out/checks_reproduce.json; out/boundary_main.json'},'proof_dependencies':[{'claim_id':src['claim_id'],'version':src['version'],'scope':'Naming and interpretation of U,R and existing inequality, independently accepted at the exact signed-data scope in REVIEW_A059.md; sharpness proof self-contained.'},'Elementary quadratic Walsh product, exact point indicator coefficients, absolutely convergent logarithm series and its rational geometric tail.'],'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Unversioned proposed lowering of the same signed DATA drift coefficient below 3/ln2; fixed additive repair under a tensor-closed additive ledger.','Unversioned extension R<=K I_ctrl for all shared balanced cores retaining the nominal selector variance reserve.'],'first_unproved_line':None,'next_consumers':['A059','A057','A038','A058','A064','A091','A090','B12','B20']}
# Preserve original source status, exact statement, authorship and source digest.
write('CLAIMS.json',[src,new])

next_action='Price A059 equation (7) controller residual D_ctrl-kappa together with actual terminal H-U-R using a single unspent physical account; the signed DATA coefficient and independent-control reserve cannot be improved without changing the ledger. A091 primary/A090 alternate review sharpness and tensor scope.'
p={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B12','packet_id':'A060','gap_id':'C019-exclusive-controller-signed-terminal-payment','attempt_id':'A060-stage3-sharp-signed-data-v1','method':'Consume A038/A059 reserve results, independently reconstruct signed DATA drift, prove an exact all-even-dimension bent-point saturation with geometric error and an actual balanced shared-core reserve boundary; exact finite and direct-character checks.','mathematical_delta':'The coefficient 3/ln2 in the existing full signed DATA drift is optimal, even beta^2=core influence=1; a five-bit case already exceeds 4. Fixed additive slack cannot improve it in a tensor-closed additive payment rule. Independence is essential for the same control-only variance-reserve funding: R/I_ctrl=2^t with one shared balanced data bit. No universal FEI constant improves.','deliverable_status':'COMPLETE_SAVED_LOCALLY','mathematical_status':'SCOPED_SHARPNESS_PROVED_LOCALLY; C019_CONTROLLER_TERMINAL_PAYMENT_AND_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':src['claim_id'],'version':src['version'],'source_statement_sha256':source_claim_hash,'review_scope':'U,R identities and signed DATA bound only'}],'claims_created_or_changed':[{'claim_id':new['claim_id'],'version':1,'change':'new narrow sharpness and scope certificate'},{'claim_id':src['claim_id'],'version':src['version'],'change':'scope-limited independent review record; whole-claim status unchanged'}],'source_artifacts':['INTAKE.md','PROOF.md','INDEPENDENCE_BOUNDARY.md','REVIEW_A059.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/FROZEN_BOUNDARY_SPEC.json','code/check.py','code/boundary.py','out/checks_main.json','out/checks_reproduce.json','out/boundary_main.json','out/FIVE_BIT_STRICT_CERTIFICATE.json'],'next_consumers':new['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['No local access/save blocker. Universal unpaid line is controller residual plus actual retained terminal entropy from nonreused influence. Independent acceptance of new sharpness, supervisor adoption and remote mirrors unverified.'],'packet_ids':['A060']}
write('PROGRESS.json',p); (R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())

report=f'''# exact target, quantifiers, hypotheses and units

A060 B12 composition sharpness, stage 2026-10-14 00:46 UTC. For every even r>=4 prove necessity of the coefficient 3/ln2 in A059's full signed DATA drift for its U,R ledger, retaining actual terminal spectra. Determine whether a fixed additive improvement disappears under tensorization, and which independence hypothesis is necessary for the same selector reserve. Inputs are uniform physical bits, outputs signs, all entropy and KL in bits. Both targets are closed locally by proofs and exact certificates; full FEI and C019 controller/terminal payment remain OPEN. No universal constant improves.

# sources actually read, revisions and theorem locators

Read BOARD snapshot 2026-10-14 00:40 UTC, B12 STREAM_NOTES v2 (still dated 2026-10-11 23:30 UTC), own STATUS and full execution protocol revision {protocol['revision']}. Read A091 stage3 REPORT/OVERLAP_INTERFACE; A057 stage3 REPORT/PROOF Sections 1-5; A056/A058/A078 stage3 REPORTs. Adaptive follow-up read A038 and A059 stage3 REPORTs, then full A059 PROOF and CLAIMS. out/SOURCE_RECEIPTS.json pins actual files. Previous required campaign/paper reading remains in earlier runs; no new external theorem or literature priority assertion is used.

A056 already pays distinct-core shared controls; A058 already pays privately indexed shared parities; A078 already refutes unrestricted shared-data local pricing. A038 and A059 already extend the reserve through arbitrary interleaving and prove sharp factor 2. We did not repeat those results. This stage consumes the new A059 signed cancellation and independently reviews its critical local inequality before adding narrow sharpness certificates, respecting the broad-claim review cap.

# complete derivation or exact first unsupported line

PROOF.md defines actual F=b+(y-1)C, where b is paired quadratic bent and C a point indicator on r controls. Its Fourier sectors are sigma*sqrt(q)-q and q, with exact sign multiplicities. The y children are b and b-2C. Direct formulas yield D_y=qr+[T(2)/2-T(1)]/ln2, U_drop=0 and R_drop=qr. The convergent rational logarithm series proves

    (19/6)q/ln2 <= 3/ln2-(D_y-qr)/q
                         <= 8q/((1-4q)ln2).

Thus the signed DATA residual per spent influence approaches 3/ln2. The five-bit r=4 certificate already lies strictly between 4 and 41/10. The core beta=1 and beta^2=Inf_core=1, so replacing singleton squares by influence offers no discount. The actual terminal entropy is r-T(2)/(2ln2), and root influence is r(1/2+q)+q; H/I tends to 2, not infinity.

For disjoint products equipped with the additive per-factor ledger, the residual, reserve, influence spent and terminal entropy are additive. Tensorization therefore removes a fixed additive slack in that payment rule; a different canonical single-core representation or per-factor overhead is outside that conclusion. INDEPENDENCE_BOUNDARY.md supplies balanced distinct u=x and v=x(1-2A_t), nominal R=1 but I_ctrl=2^-t, with exact physical root and terminal costs. The missing covariance is identified explicitly. This does not refute the stated independent-core theorem or assert large collision entropy.

REVIEW_A059.md reconstructs the exact biased empty-row cancellation, cap envelope, raw row JS-Hellinger estimate and U,R martingales independently. It accepts the signed DATA inequality and exact reserve identities at stated scope, with no repair. No broad acceptance or payment of the controller/terminal residual is inferred. First unsupported universal line: the actual signed sum of D_ctrl-kappa and actual retained terminal H-U-R admits one nonreused physical influence payment.

# executed validation with domain, arithmetic, commands and outputs

Both frozen specs were saved before their jobs. Commands from this run: python -X utf8 code/check.py pilot; main; reproduce; python -X utf8 code/boundary.py pilot; main. Bent tables use even r=2,4,6,8; compressed all-dimensional certificates use r=4,6,8,10,12,16,24,32,64. Direct character reproduction uses r=2,4,6, independent of FWHT. Tensor products are checked as actual Boolean tables for one, two and three r=2 factors. Shared-core boundary exhausts the eight declared t=1,...,8 fixtures and directly reproduces t=1,...,4. No sampling or unjustified symmetry quotient is used; large r uses proved multiplicities and convergent rational series, not oversized truth tables.

Integer Walsh and direct character sums, rational physical edge counts, exact prime-log entropy identities, and 40-term rational atanh enclosures with tail 2*z^81/[81*(1-z^2)] establish all signs. Compressed residuals additionally have a separately proved rational geometric tail. Outputs are outward-rounded 100-bit dyadic endpoints checked against the exact bounds. No floating-point result is used as proof.

All {total} checker assertions PASS. Bent pilot: {results['pilot']['assertions']} assertions, {results['pilot']['seconds']:.6f}s; main: {results['main']['assertions']}, {results['main']['seconds']:.6f}s; direct reproduction: {results['reproduce']['assertions']}, {results['reproduce']['seconds']:.6f}s. Boundary pilot: {boundary['pilot']['assertions']}, {boundary['pilot']['seconds']:.6f}s; main: {boundary['main']['assertions']}, {boundary['main']['seconds']:.6f}s. A separate integer endpoint check certifies the five-bit ratio>4. Memory estimate 90 MB, peak unmeasured; no >300 MB job or memok-gated launch occurred. All dimensions and domains were frozen, jobs sequential and below 55 seconds. The boundary terminal coefficient was corrected during drafting before any boundary execution; no failed mathematical assertion or domain escalation occurred.

# proof dependencies and changed downstream conclusions

Sharpness and the scope boundary are proved from actual Boolean tables and elementary convergent series. A059-INTERLEAVED-BIASED-STOPPING-RESERVE@1 names the ledger and bound; its relevant local inequality is reconstructed here. Source exact statement, authorship and whole-claim pending status remain unchanged, with only a scoped local review record added in this run's CLAIMS. No other agent files or shared registries are modified. A038's interleaved reserve/factor-2 sharpness is explicitly credited rather than claimed again.

A059/A057/A064 should keep 3/ln2 unless they strengthen the debit or change the ledger; a fixed additive constant will not improve a tensor-closed additive rule. A058/A097 must replace the nominal reserve or fund its covariance from shared data when removing independence. These are source-bound handoffs, not observed downstream adoption. Universal FEI is still open.

# one next mathematical action and independent reviewer

{next_action} The mandatory adverse fixture is F=b+(y-1)C with the exact bent/one-flip terminal pair. A058 can test the covariance boundary against its nonlinear shared-slice extension. Improving the already sharp DATA coefficient or repeating the paid independent-core reserve is no longer productive.

# actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and byte-identical PACKET_DELTA, complete proofs/review, frozen specs, code and exact outputs are saved only inside this assigned run. STATUS has two lines; WORKLOG and LEARNED append dated facts. out/SCHEMA_VALIDATION.json checks protocol keys and compatibility; out/PERSISTENCE_RECEIPT.json records observed file lengths and SHA256 readback receipts. Files stay below 20 MB. No local save blocker. New independent review, registry adoption, supervisor copying, mirrors and public release remain unverified.

# Universal bridge

This stage moves C019 stopping-tree payment at the lead-named composition sharpness interface by proving that the existing signed DATA coefficient 3/ln2 cannot be reduced in its current ledger, quantitatively within 8q/((1-4q)ln2) of sharpness, and by isolating the necessary independent-core reserve hypothesis with an actual balanced family R/I_ctrl=2^t. It closes no universal FEI case and pays no controller or terminal residual; both actual terminal spectra and the exclusive influence telescope remain explicit. NEXT attacks exactly A059's remaining D_ctrl-kappa plus terminal H-U-R account, because the DATA and reserve constants are now exhausted and the shortest route to full FEI is a new shared payment mechanism rather than another isolated class estimate.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A060 stage3 saved: signed DATA coefficient 3/ln2 proved sharp with exact error; five-bit ratio>4; shared balanced cores refute nominal control-reserve funding; 1763 exact checks PASS; FEI OPEN.\nNEXT: A091/A090 review; price A059 D_ctrl-kappa plus actual terminal H-U-R from one unspent physical reserve; improving the current DATA coefficient cannot work.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-14 00:46 UTC stage '+R.name+': Consumed A038/A059 interleaved-reserve results; avoided repeating sharp factor 2. Independently reconstructed A059 signed DATA cancellation. Bent point replacement attains 3/ln2 with rational geometric error; actual five-bit case exceeds 4. Tensor-closed additive-ledger fixed overhead cannot repair a lower coefficient. Balanced one-shared-bit cores give nominal R/I_ctrl=2^t with actual costs retained. 1763 assertions PASS including direct-character reproduction. Full controller/terminal payment remains open. All outputs saved locally; independent review and supervisor/mirror adoption unverified.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-14 signed DATA sharpness: F=b_r+(y-1)1[z=0], paired quadratic bent even r>=4, q=2^-r. U_drop=0,R_drop=qr,Inf_y=q. Signed residual E obeys (19/6)q/ln2 <=3/ln2-E/q <=8q/((1-4q)ln2). Therefore A059 coefficient3/ln2 is optimal even beta=1; r4 already E/q>4. Terminal b/b-2C entropy remains ~r; I=r(.5+q)+q, H/I->2. Fixed additive slack cannot lower this coefficient for tensor-closed rules using additive per-factor ledgers; a different canonical product representation is not covered. Reserve hypothesis: balanced u=x,v=x(1-2A_t), fair selector, nominal R=1, actual I_ctrl=2^-t; covariance restores the missing edge term. Root I=1+(t+1)2^-t and H->0, so no FEI disproof. A038/A059 already proved interleaved reserve conservation and sharp control factor2; do not repeat. Current universal gap is controller residual plus retained terminal H-U-R with one exclusive influence account.\n')

claim_keys=set(protocol['required_per_run']['claim_fields'])
progress_keys={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
assert set(p)==progress_keys
for c in [src,new]: assert set(c)==claim_keys
assert new['statement_sha256']==statement_hash(new['exact_statement'],new['hypotheses'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all('# '+s in report for s in protocol['required_per_run']['report_fields'])
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
write('out/SCHEMA_VALIDATION.json',{'status':'PASS','progress_keys':'exact normalized protocol field set','claim_keys':'exact protocol field set','compatibility_bytes':'identical','new_statement_digest':'PASS','source_statement_digest_preserved':source_claim_hash,'report_fields':'all present','rolling_status_lines':2,'checker_assertions':total})
files=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
write('out/PERSISTENCE_RECEIPT.json',{'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'local readback only; independent acceptance/adoption/mirror unverified','artifacts':[digest(p) for p in files],'rolling':[digest(A/f) for f in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'schema':'PASS','checker_assertions':total,'saved_files':len(files),'five_bit_ratio_bounds_approx_only':[float(Q(fixture['lo_num'],fixture['den'])),float(Q(fixture['hi_num'],fixture['den']))],'report':str(R/'REPORT.md')}))
