from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
BASE=AGENT.parents[1]
old=ROOT.parent/'20261021T201341Z-fleet03-A076-threshold-and-tribes-controls'
protocol_path=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=read(protocol_path);v=read(ROOT/'out'/'validation.json');pilot=read(ROOT/'out'/'pilot.json')
assert v['status']==pilot['status']=='PASS'
assert v['counts']['two_point_roots']==828 and v['counts']['one_point_roots']==66
assert v['counts']['root_queries']==3414 and v['counts']['mixed_nodes']==140 and v['counts']['mixed_leaves']==146
assert v['assertions']==12792
sources=[(protocol_path,'protocol revision2026-10-11-execution-v2; entire rules'),
 (BASE/'BOARD.md','stage-start team board'),(BASE/'claude'/'B16'/'STREAM_NOTES.md','v2 stream direction'),
 (old/'POINT_CARRIER_PROOF.md','section7 common-event private price11 and point special case'),
 (BASE/'agents'/'A077'/'runs'/'20261021T230123Z-fleet03-A077-sparse-defect-towers'/'PROOF.md','sections1-9, correlated spectrum and mean-sector price12'),
 (BASE/'agents'/'A077'/'runs'/'20261021T230123Z-fleet03-A077-sparse-defect-towers'/'REVIEW_A076.md','scoped acceptance of A076 v7 section7 only'),
 (BASE/'agents'/'A078'/'runs'/'20261022T211614Z-fleet03-A078-coding-and-padding'/'PROOF.md','original signed account, stopped identities and concrete donor; entire proof')]
# Latest A028/A029 derivations were read for context, not invoked as axioms.
for agent in ('A028','A029'):
    candidates=sorted((BASE/'agents'/agent/'runs').glob('*/DERIVATION.md'))
    if candidates:sources.append((candidates[-1],'context: signed JS/structural-ledger distinction; not an assumed theorem'))
manifest={'saved_at_utc':now,'scope':'Files actually consulted this stage; older campaign/paper baseline was read in prior stages, not newly claimed here. Hashes bind the consulted current source bytes; no remote revision asserted.','sources':[]}
for path,locator in sources:
    assert path.is_file(),str(path)
    manifest['sources'].append({'path':str(path),'sha256':sha(path),'locator':locator})
dump(ROOT/'SOURCE_MANIFEST.json',manifest)
consumers=['A028','A029','A077','A078','A092','A094','B16','B20']
newstatements=[
 ' Stage8: For every d>=1 and every pair of correlated Boolean profiles V,W on one independent uniform private cube, the Boolean wrapper equal to V at shared vertex0, W at vertex e1, and +1 elsewhere has signed collision Xi=e sum_nonempty([g(v+w)+g(v-w)]/2-g(v)-g(w)) in[-4e,0], e=2^-d, g(t)=-t^2 log2(t^2). With T=e[H(V)+H(W)] and R=de[Var(V)+Var(W)], each private query obeys Delta H<=Delta T+release_R+12Inf+Delta Xi. Each nonseparating shared query obeys Delta H<=6Inf; the separating query obeys Delta H<=release_R+9Inf. Its actual influence is2e Pr(V!=W), and its full empty-private erasure is Phi((1-eq)^2,e^2c^2)+(1/(2e)-1)Phi(e^2q^2,e^2c^2), q=2-EV-EW,c=EV-EW. All shared endpoints and constant profiles are included. These shared clauses require the outside carrier to be constant +1.',
 ' Stage8: For the preceding constant-outside two-point wrapper, one original unused donor B>=4e_o after all old debits funds EVERY finite adaptive mixed private/shared stopping tree. Before separation use K_v=e_v[B/e_o-Xi_o/e_o+Xi_v/e_v], zero on killed two-point events; at separation freeze K_parent in both children and all their descendants, including constant leaves. E K_leaf>=B-4e_o. With complete terminal spectra and inherited T retained, H(F_o)-E H(F_leaf)+E(R_leaf+K_leaf)<=T_o-E T_leaf+R_o+B+12P_private+6P_gate+9P_separator. For original V=y*b_k, k>=4 even, W=y(1-2 point(z=0,x=0)), m>=2, S=e_o(3k/2+5), retain D0 and FIRST4e_o debit, B=S-D0-4e_o. If D0<=S-8e_o the mixed continuation leaves E K>=S-D0-8e_o>=3e_o-D0, without new descendant source certificates. This is a continuation theorem with supplied original donor and retained input/terminal entropy, not universal donor eligibility or full FEI.'
]
claims=read(old/'CLAIMS.json')
for c,extension in zip(claims,newstatements):
    c['version']=8;c['exact_statement']+=extension
    c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
    c['hypotheses'].append('Stage8: constant +1 outside shared vertices0 and e1, arbitrary correlated profiles on disjoint uniform private cube; bits. Original donor B admission explicit; original old debit preserved; finite adaptive no-repeat physical histories with all terminal siblings and inherited input entropy retained. Nonconstant outside carriers excluded from the new mixed/shared clauses.')
    c['proof_source'].update({'stage8':str(ROOT/'MIXED_TWO_POINT_PROOF.md'),'stage8_locator':'sections1-6 equations1-11; original account7, shared payments3/6 and full stopped inequality10','stage8_validation':str(ROOT/'out'/'validation.json'),'stage8_mixed_ledger':str(ROOT/'out'/'MIXED_LEDGER.json')})
    c['proof_dependencies'].extend([c['claim_id']+'@7 (retained prior material and one-point price11)', 'A077 stage6 PROOF sections6-8 mean-sector estimate, reconstructed independently in stage8 section1', 'A078 20261022T211614Z PROOF original collision account and donor; scoped independently reconstructed in REVIEW_A078.md'])
    c['review_records'].append({'claim_version':7,'reviewer':'A077/fleet03','verdict':'HOLDS_AT_SCOPED_COMMON_EVENT_PRIVATE_TRANSFER','source':str(sources[5][0]),'scope':'POINT_CARRIER_PROOF.md section7 inequality7, exact profile identity, private telescope and reserve conservation ONLY; not whole bundle or shared payment','substantive_repair':False})
    c['review_records'].append({'claim_version':8,'status':'AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW','requested_reviewers':['A077','A078','A028','A092','A094'],'formal_scope':'No Lean formalization claimed; rational finite certificates plus complete analytic proof supplied.'})
    c['status']='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW';c['supersedes']=[c['claim_id']+'@7'];c['first_unproved_line']=None;c['next_consumers']=consumers
    assert set(c)==set(p['required_per_run']['claim_fields'])
dump(ROOT/'CLAIMS.json',claims)
next_action='Take one nonconstant threshold outside carrier with h(0)=h(e1)=+1 and one actual shared query; compute the complete extra carrier-row entropy bill and test it against the SAME unused original signed surplus while retaining both profiles, original debits and every terminal. A077/A078 independently review stage8 shared inequalities and account freezing first.'
progress={'protocol_revision':p['revision'],'run_id':ROOT.name,'stream':'B16','packet_id':'A076','gap_id':'FEI-B16-A076-INITIAL','attempt_id':'A076-stage8-original-account-through-all-shared-queries','method':'Exact shared gate erasure and separator-sector pairing; self-contained two-point channel bound; original collision account transported as a gate martingale and frozen at separation; complete rational Boolean census and mixed-history ledgers.','mathematical_delta':'Extends A078 private-only original-donor continuation to EVERY finite adaptive mixed physical tree for the constant-outside correlated two-point wrapper, at unchanged maximum continuation price12. Shared gates cost6, separator9 plus SAME R release; old first4e debit and expected unused donor>=3e remain.','deliverable_status':'COMPLETE_LOCAL_PENDING_V8_REVIEW','mathematical_status':'SCOPED_MIXED_HISTORY_AUTHOR_PROOF; NONCONSTANT_CARRIER_AND_UNIVERSAL_DONOR_ADMISSION_OPEN; FULL_FEI_OPEN','claim_versions_used':['A076-STRUCTURED-SPECTRA@7 one-point/common-event theorem, A077 scoped acceptance','A076-TRIBES-PAYMENT-DISCRIMINATION@7 prior ledger retained','A077 20261021T230123Z correlated-profile spectrum and mean-sector payment; independently reconstructed here','A078 20261022T211614Z original account and donor; conditional scoped independent acceptance recorded here','A028/A029 latest signed-JS history ledgers: context, not dependency axioms'],'claims_created_or_changed':[c['claim_id']+'@8' for c in claims],'source_artifacts':['MIXED_TWO_POINT_PROOF.md','REVIEW_A078.md','SOURCE_MANIFEST.json','code/check.py','code/arithmetic.py','code/finalize.py','out/FROZEN_SPEC.json','out/pilot.json','out/validation.json','out/MIXED_LEDGER.json','out/PERSISTENCE_RECEIPTS.json'],'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['New stage8 analytic clauses await independent reconstruction; finite checks do not alone prove all dimensions.','Nonconstant outside carrier shared fibers contain unpaid carrier Fourier amplitudes.','No unrestricted original donor eligibility, arbitrary inherited input FEI certificate, or prescribed terminal-reference conversion is proved.','Remote supervisor adoption and mirror verification not observed.','Brain self-care degraded: stale owner-model/state-of-mind sources; freshness of personalized recall unverified, current explicit instructions used.'],'packet_ids':['A076']}
required=[x.split(' (')[0] for x in p['required_per_run']['progress_fields']]
assert set(progress)==set(required)
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

For every pair of correlated Boolean profiles V,W on the same uniform private cube, and d>=1 independent shared bits, F is V at shared vertex0, W at vertex e1 and +1 elsewhere. Prove a stopped entropy payment across EVERY finite adaptive mixed private/shared physical tree from one original unused donor, with both inherited input bills and all complete terminals retained. Entropy uses bits; e=2^-d. No dimension bound enters the analytic theorem. The explicit donor fixture uses even k>=4,m>=2; tests use k4,m2,d3. This is A076 stage8, extending the existing two bundles rather than opening a third broad candidate.

# sources actually read, revisions and theorem locators

SOURCE_MANIFEST.json binds the protocol, current board and B16 direction, A076 v7 section7, A077's correlated-profile proof and scoped independent acceptance of that section, and A078's current all-private donor proof. A028/A029 signed-JS ledgers were read for context; structural/source payment is still separate. The earlier threshold/percolation papers and campaign baseline were read in earlier stages, not represented as fresh reads here. Current user campaign end2026-10-23 14:49UTC supersedes the protocol's older campaign date. No stale personalized memory supplied a mathematical premise.

# complete derivation or exact first unsupported line

MIXED_TWO_POINT_PROOF.md sections1-6 supplies the complete derivation. Shared activation gates have exact full erasure Phi((1-w)^2,w^2)+2w(1-w), giving Delta H<=6Inf. At the profile separator the nonempty-private erasure is paid by exactly the existing R release; its complete empty-private sector costs at most6Inf, and channel entropy costs at most3Inf. Before separation, K=e_v[B/e_o-Xi_o/e_o+Xi_v/e_v] absorbs signed private collisions and is harmonic at gates. At separation K is frozen in BOTH children and all descendants; it is retained even at constant terminals. This yields equation10 for every finite mixed tree with continuation prices12/6/9 and E K_leaf>=B-4e_o. For the actual original bent donor, retain oldD0 and FIRST4e_o debit; B=S-D0-4e_o and E K_leaf>=S-D0-8e_o>=3e_o-D0. REVIEW_A078.md independently accepts only the prior signed account, physical/reserve identities, conditional telescope and original donor arithmetic, with no repair.

The exact first unsupported universal line is replacing the constant outside carrier by arbitrary nonconstant h in the shared gate/separator formulas, or admitting an arbitrary source without an unused certified original donor. Input and terminal FEI certificates and reference conversion remain unsupplied. Full FEI remains OPEN. New analytic claims are author-proved, awaiting independent review; finite enumeration is not their all-dimensional proof.

# executed validation with domain, arithmetic, commands and outputs

Before execution, out/FROZEN_SPEC.json froze the family, domain, all ordered case counts, exact arithmetic, memory120MB estimate and pilot55/main600-second limits. The inherited helper is pinned by SHA256 {v['arithmetic_helper_sha256']}. Commands from the A076 folder were `python -X utf8 runs\\{ROOT.name}\\code\\check.py --pilot` and `python -X utf8 runs\\{ROOT.name}\\code\\check.py`. Pilot: {pilot['assertions']} exact assertions PASS in {pilot['elapsed_seconds']:.3f}s. Full: {v['assertions']} exact assertions PASS in {v['elapsed_seconds']:.3f}s, {v['counts']['two_point_roots']} two-point roots, {v['counts']['one_point_roots']} one-point roots, {v['counts']['root_queries']} actual root queries. All ordered V,W on n0..2,d1..3; all one-point cores n0..2,r0..2. No symmetry quotient or dimension escalation. Forty small roots have independent direct character-sum and physical-edge reproduction.

All three frozen mixed policies were checked on BOTH x1 children, retaining the initial4e debit:140 internal nodes and146 complete leaves. Full node/terminal H,I,R,K, inherited entropy, full inherited core erasures and separately labeled quarter-scaled data are in out/MIXED_LEDGER.json. Each branch retains expected donor at least3/8 at e_o=1/8. Integer Walsh and Fraction arithmetic produce exact rational-log identities, checked through prime exponents, and inequalities use outward rational atanh-series enclosures. No float sign is accepted. The final identical-domain rerun added the reviewable node ledger; it was justified by that missing output, not a wider search. No job exceeded300MB estimated or required a heavy-memory admission. The read-only governor reported CPU94.6%, available memory2890MB, commit headroom17599MB, disk27.3GB, statusok; no other work was altered. No Lean verification is claimed. All research jobs are finished.

# proof dependencies and changed downstream conclusions

The one-point post-separation private theorem is A076 v7 section7, now independently accepted by A077 at its exact private/conservation scope. The correlated private mean-sector bound is reconstructed in section1 and separately checked on every census root query; A078's original account is reconstructed in REVIEW_A078.md. No newer claim is needed to justify an older one, and no A028/A029 pending structural payment is assumed. A078's remaining shared-query obstruction is closed for the constant-outside two-point family, with the SAME original donor and unchanged maximum continuation price12. This does not establish any universal FEI constant or arbitrary source admission.

# one next mathematical action and independent reviewer

{next_action}

# actual persistence receipts or precise save blocker

All four protocol files, proof, scoped review, frozen specification, exact outputs and reproducible code are saved in this run. STATUS.md is two lines; WORKLOG.md and LEARNED.md are appended. out/PERSISTENCE_RECEIPTS.json records re-read schema/hash verification. Every file is below20MB. No shared index or another agent's files were modified. Git, remote copying, brain writes and remote verification were not performed; supervisor copying remains external. Brain self-care is degraded/unverified because owner-model and state-of-mind sources are stale; personalized recall freshness is affected, not the freshly read instructions or exact certificates.

Universal bridge: This stage moves C024 history transfer and C019 stopping-tree payment from A078's private-only continuation to every finite adaptive mixed physical history of the constant-outside two-point family, preserving one original account, all old debits, input bills and complete terminals at maximum continuation price12; expected residual source remains at least3e_o-D0. Arbitrary nonconstant carrier rows, noncircular universal original-source eligibility, inherited input/terminal certificates and reference conversion remain unpaid. The shortest next route is a nonconstant threshold carrier with a real shared query and the same original source ledger: it directly tests the exact new universal obstruction instead of optimizing another isolated threshold or tribes class constant.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A076 stage8 saved: all adaptive mixed histories for constant-outside correlated two-point family, SAME original donor, prices12/6/9; 12792 exact assertions PASS; independent v8 review pending; FEI OPEN.\nNEXT: Nonconstant threshold outside carrier: pay one actual shared-query carrier-row bill from SAME unused original surplus; A077/A078 review shared payment and frozen-bank handoff.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as fh:fh.write(f'\n{now} stage8 ({ROOT.name}): consumed A077 scoped v7 acceptance and A078 original-donor theorem. Derived gate6, separator9+same R; carried one signed collision account through gates and froze it at separator. Proved every finite mixed history conditionally on original donor. Pilot772/full12792 exact assertions PASS;828+66 roots,3414 queries,3 mixed policies,all siblings. Retained first4e debit and >=3e expected donor. Scoped independent review of A078 account saved. No research job remains running; no git/remote/brain writes. New theorem review pending; nonconstant outside carrier and unrestricted source eligibility open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as fh:fh.write(f'\n{now} stage8: For point activation of ANY disjoint Boolean core, gate B=Phi((1-w)^2,w^2)+2w(1-w), w=actual gate influence; Delta H<6w. For constant-outside two-point correlated profiles, separator influence=2e Pr(V!=W); its nonempty-private erasure uses exactly release_R=e(Var V+Var W), empty-private erasure<=6Inf; total Delta H<=release_R+9Inf. Normalize the OLD collision account by current e before separation; gates double e/Xi on one child and kill the other, preserving the account average. Freeze the carried account in BOTH separator children and ALL later terminals, including constants. B>=4e_original gives expected terminal bank>=B-4e_original through arbitrary finite adaptive mixed trees. This retains original input entropies; it is not an arbitrary-input FEI proof. Nonconstant outside h breaks the gate/empty-sector formulas and is the next unpaid line. See {ROOT.name}/MIXED_TWO_POINT_PROOF.md, new author proof pending independent review.\n')
assert read(ROOT/'PROGRESS.json')==read(ROOT/'PACKET_DELTA.json')
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for c in read(ROOT/'CLAIMS.json'):
    assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
receipt={'saved_at_utc':now,'validation_status':'PASS','schema_progress_exact_fields':True,'schema_claims_exact_fields':True,'packet_delta_equals_progress':True,'rolling_status_two_lines':True,'all_research_jobs_finished':True,'remote_persistence':'NOT_PERFORMED_SUPERVISOR_OWNED','files':[]}
for path in sorted(ROOT.rglob('*')):
    if path.is_file() and '__pycache__' not in str(path):
        assert path.stat().st_size<20_000_000,str(path)
        receipt['files'].append({'path':str(path.relative_to(ROOT)),'bytes':path.stat().st_size,'sha256':sha(path)})
dump(ROOT/'out'/'PERSISTENCE_RECEIPTS.json',receipt)
print(json.dumps({'status':'SAVED_AND_SCHEMA_CHECKED','assertions':v['assertions'],'files':len(receipt['files']),'source_count':len(sources),'claims':[c['claim_id']+'@8' for c in claims]}))
