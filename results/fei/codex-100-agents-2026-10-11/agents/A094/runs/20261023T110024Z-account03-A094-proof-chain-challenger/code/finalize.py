from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,copy
RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1];BASE=OWN.parents[1]
NOW=datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
    (RUN/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
main=read(RUN/'out/MAIN_RESULTS.json');pilot=read(RUN/'out/PILOT_RESULTS.json')
assert main['status']=='PASS' and main['ordered_trees']==144 and main['frontiers']==808
# Independent exact coefficient certificate; pairs represent coefficient of C0,constant.
K=(F(4),F(15))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def sc(x,a):return tuple(a*b for b in x)
root=sub(sc(K,F(7,8)),(F(2),F(15,8)))
padding=sub(sc(K,F(7,8)),(F(3,2),F(61,8)))
source=sub(sc(K,F(7,8)),(F(5,2),F(15,2)))
assert root==(F(3,2),F(45,4))
assert padding==(F(2),F(11,2)) and source==(F(1),F(45,8))
universal=(F(1),F(11,2));booking=(F(1),F(37,8))
assert all(all(a>=0 for a in sub(v,universal)) for v in [root,padding,source])
assert sub(universal,booking)==(0,F(7,8))
assert F(3**2+15*3+7,2**3)==F(61,8) and F(3+1,2**3)==F(1,2)
save('out/COEFFICIENT_CERTIFICATE.json',{'status':'EXACT_RATIONAL_IDENTITIES_PASS','root_margin_coefficients':[str(x) for x in root],'padding_margin_coefficients':[str(x) for x in padding],'source_margin_coefficients':[str(x) for x in source],'uniform_margin_coefficients':[str(x) for x in universal],'booking_coefficients':[str(x) for x in booking],'residual_coefficients':['0','7/8'],'q_equals_3_padding_overhead':'61/8','q_equals_3_source_overhead':'1/2','padding_monotonicity_difference_polynomial_in_q_minus_3':['39','19','1'],'source_monotonicity_difference':'q>=3','scope':'All nonnegative real C0 and G; analytic monotonicity proof in DERIVATION sections4,5; no finite extrapolation'})
ref=BASE/'agents/A086/runs/20261023T053719Z-account03-A086-joint-code-referee'
v2=BASE/'agents/A011/runs/20261023T000841Z-account03-A011-representation-existence'
v1=BASE/'agents/A011/runs/20261021T182829Z-account03-A011-representation-existence'
gen=BASE/'agents/A011/runs/20261014T074949Z-account05-A011-representation-existence'
src=next(c for c in read(ref/'CLAIMS.json') if c['claim_id']=='A086-NONVANISHING-ALL-FRONTIER-OLD-BOOKING-ALLOWANCE')
source=copy.deepcopy(src)
def conventions(c):
    candidates={'plain_exact_statement':c['exact_statement'],'compact_sorted_statement_hypotheses':json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,ensure_ascii=False,separators=(',',':'))}
    matches=[name for name,s in candidates.items() if hashlib.sha256(s.encode('utf-8')).hexdigest()==c['statement_sha256']]
    assert matches,(c['claim_id'],'unknown declared hash convention')
    return matches
hashes={'source':conventions(source)}
source['review_records'].append({'reviewer':'A094/account03/B19','at':NOW,'verdict':'HOLDS_AT_FULL_NAMED_SCOPE_WITHOUT_REPAIR','proof':str(RUN/'DERIVATION.md'),'locators':'sections1–5','validation':str(RUN/'out/MAIN_RESULTS.json'),'scope':'All supplied nonconstant Boolean cores, b>=2,r>=1, all original padding/source frontiers including final collapse; original subprobability mass, source C0, K, external U and full terminals retained','independence':'Own prescribed-model literal Boolean checker; independent complete signed ledger, original-source inheritance and exact coefficient calculation; no A011/A086 verifier imported','substantive_repair_supplied':False})
source['status']='INDEPENDENTLY_RECONSTRUCTED_AT_FULL_NAMED_SCOPE_LOCALLY'
statement='Let g be any nonconstant Boolean function on a>=1 uniform source bits, and R a subprobability of mass s in(0,1], positive on its true Fourier support, with finite c=CE(P_g,R)<=C0 I_g,C0>=0. For b>=2 padding bits and r>=1 fresh point controls, retain EXACTLY the original root/fresh floors, ORIGINAL-R mass-preserving source inheritance, padding-then-source policy and full signed history ledger L of A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK@2. Fix K=4C0+15 once. At the root, every nonempty padding frontier and every active source frontier including final source collapse, K I(F)-L>=(C0+11/2)I_g. Consequently any external already booked U in[0,(C0+37/8)I_g] is retained at ALL those frontiers with remaining quota at least7I_g/8>0. This enlarges A086 v1 allowance by29I_g/8 while keeping the same residual. Original source mass, original rate, all old signed charges, full complementary terminal CE/KL and untouched independent finite-cost terminal costs remain; the latter stay outside the core account. This does not identify a different canonical/narrow-first history with the prescribed history, pay arbitrary positive-part-only accumulation, supply an influence-priced initial reference, or prove arbitrary edit iteration/full FEI.'
new={'claim_id':'A094-LARGER-NONVANISHING-ALL-FRONTIER-ALLOWANCE','version':1,'exact_statement':statement,'hypotheses':['Finite uniform Boolean cube; information in ideal bits and influence physical; original source nonconstant','b>=2,r>=1; exactly A011 v2 old root and fresh floors and original-source inherited subprobability models; all original physical reaches retained','Original C0>=0 and K=4C0+15 fixed once, source cost finite and supplied; no descendant influence assumption','Complete signed history ledger including all complementary terminal costs and mass penalties; external old booking U remains fully charged','No arbitrary policy/reference identification; no positive-part-only replacement of signed ledger; independent untouched terminal finite and product compatible'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A094/account03'],'proof_source':{'path':str(RUN/'DERIVATION.md'),'locator':'sections4,5','exact_coefficients':str(RUN/'out/COEFFICIENT_CERTIFICATE.json'),'finite_validation':str(RUN/'out/MAIN_RESULTS.json')},'proof_dependencies':[{'claim_id':'A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK','version':2,'scope':'General-envelope, padding and quantitative source-prefix inputs independently reconstructed in sections1–4'}],'review_records':[],'status':'AUTHOR_ANALYTIC_PROOF_EXACT_RATIONAL_CERTIFICATE_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A086','A011','A095','A096','A097','B19','B20']}
claims=[source,new];hashes['new']=conventions(new);save('CLAIMS.json',claims);save('out/HASH_CONVENTIONS.json',hashes)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B19','packet_id':'A094','gap_id':'C024-SAME-REFERENCE-PRESCRIBED-RESET-ORIGINAL-BANK','attempt_id':'A094-stage19-nonvanishing-allowance-full-chain-audit','method':'Full source-prefix/root/padding proof reconstruction; q>=3 exact overhead sharpening; literal prescribed-model full signed histories with subprobability mass retained','mathematical_delta':f'A086 nonvanishing all-frontier allowance v1 HOLDS at full named scope. New complete margin(C0+11/2)Ig admits external U<=(C0+37/8)Ig with SAME7Ig/8 reserve; gain29Ig/8 over original allowance. {main["ordered_trees"]} trees/{main["frontiers"]} frontiers/{main["assertions"]} exact assertions PASS. Full FEI OPEN; reference/policy handoff and universal initial supplier unpaid.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SOURCE_FULL_SCOPE_RECONSTRUCTED; LARGER_ALLOWANCE_AUTHOR_PROOF_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':[{'claim_id':source['claim_id'],'version':1,'scope':'full named allowance independently reconstructed'},{'claim_id':'A011-PADDING-FRESH-RESET-SAME-SOURCE-BANK','version':2,'scope':'exact root/padding/source-prefix interface and full dependencies reconstructed'}],'claims_created_or_changed':[c['claim_id'] for c in claims],'source_artifacts':['DERIVATION.md','FROZEN_SPEC.json','SPEC_AMENDMENT.md','out/MAIN_RESULTS.json','out/COEFFICIENT_CERTIFICATE.json','out/SOURCE_RECEIPTS.json'],'next_consumers':['A086','A011','A095','A096','A097','B19','B20'],'next_action':'A086/A011 independently check q>=3 overhead61/8 and1/2 and all-frontier coefficients; pay ONE genuine compatible inherited-profile handoff against SAME larger original allowance with old U, actual conversion debit and both complete terminals retained.','stagnant_substantive_attempts':0,'blockers':['Initial influence-priced arbitrary-source reference remains supplied. No actual reference/policy handoff from A095 canonical narrow-first history is paid. Arbitrary fixed-rate iteration and positive-part-only accumulation remain open. New review and external mirror/adoption unverified.'],'packet_ids':['A094']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
paths=[ref/'CLAIMS.json',ref/'NONVANISHING_ALLOWANCE.md',ref/'RECONSTRUCTION.md',v2/'DERIVATION.md',v2/'CLAIMS.json',v1/'DERIVATION.md',gen/'GENERAL_ENVELOPE.md',BASE/'agents/A095/runs/20261023T044042Z-account03-A095-restricted-result-extraction/DERIVATION.md',BASE/'claude/B19/STREAM_NOTES.md',Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths])
old=OWN/'runs/20261023T035625Z-account03-A094-proof-chain-challenger/code/arithmetic.py'
save('out/HELPER_PROVENANCE.json',{'source':str(old),'source_sha256':sha(old),'copy_sha256':sha(RUN/'code/arithmetic.py'),'byte_identical':old.read_bytes()==(RUN/'code/arithmetic.py').read_bytes(),'new_checker_sha256':sha(RUN/'code/check.py'),'checker_version':'v2 strengthens upper-cost-bound verification to interval upper endpoint before main; margin checks already used upper endpoints','author_verifier_imported':False,'spec_amendment':'SPEC_AMENDMENT.md; pilot18 not handwritten19, domain unchanged'})
save('out/EXACT_RESULTS.json',{k:v for k,v in main.items() if k!='rows'})
status=f'STATE: Stage19 saved: A086 all-frontier allowance FULL chain HOLDS; NEW U<=(C0+37/8)Ig retains SAME7Ig/8 reserve;144 trees/808 frontiers/{main["assertions"]} exact checks PASS; FEI OPEN, new review pending.\nNEXT: A086/A011 review sharper q>=3 overheads; pay actual compatible inherited-profile handoff from SAME original account with old U, actual conversion debit and BOTH complete terminals.\n'
(OWN/'STATUS.md').write_text(status,encoding='utf-8')
marker='Stage19 [20261023T110024Z]'
for name,entry in [('WORKLOG.md',f'{NOW} — {marker}: read current board/B19/status, A086 allowance/full reconstruction and A011 v2/general/padding proof chain. Independently HOLDS at full named b>=2 scope. Sharpened q>=3 overheads to61/8 padding and1/2 source; NEW complete margin(C0+11/2)Ig admits U<=(C0+37/8)Ig with unchanged7Ig/8 reserve. Pilot handwritten frontier count19 corrected to18 without changing domain; ancillary interval upper-bound test strengthened before main. {main["assertions"]} exact assertions/144 ordered trees/808 frontiers PASS. Old source mass including final penalty retained. No v3 blanket acceptance or canonical-policy handoff. FEI OPEN.'),('LEARNED.md',f'{marker}: For A011 v2 b>=2,r>=1, q=b+r>=3. Padding overhead improves41/4 ->61/8 from max(q^2+15q+7)/2^q atq3; intermediate source entropy overhead improves3/4 ->1/2 from max(q+1)/2^q atq3. Root/final margin1.5C0+45/4, padding2C0+11/2, intermediate C0+45/8 all dominateC0+11/2. External old U<=(C0+37/8)Ig leaves7Ig/8 at ALL old frontiers with same original K4C0+15, R and signed ledger; improves original C0+1 allowance by29Ig/8. A larger numerical cap does not identify incompatible canonical/narrow-first and floor/padding-first references or policies. True source mass s persists to final single-atom -log2s; signed ledger is not positive-part-only payment.')]:
    p=OWN/name
    if marker not in p.read_text(encoding='utf-8'):
        with p.open('a',encoding='utf-8',newline='') as f:f.write('\n'+entry+'\n')
report=f'''# A094 stage19: larger nonvanishing allowance, same original reserve

## exact target, quantifiers, hypotheses and units

Challenge A086-NONVANISHING-ALL-FRONTIER-OLD-BOOKING-ALLOWANCE@1 through its full A011 v2/root/padding proof chain. The source g is ANY nonconstant Boolean function, supplied a finite subprobability reference R of mass s in(0,1] and cost c<=C0 Ig. There are b>=2 padding bits and r>=1 fresh point controls. Every model, original rate K=4C0+15, padding-then-source policy, original physical reach, signed charge and complete terminal is retained. Costs are ideal bits, influences physical and uniform. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read current BOARD, B19 STREAM_NOTES v2, own STATUS and the protocol schema2026-10-11-execution-v2. Read complete A086 run20261023T053719Z NONVANISHING_ALLOWANCE and RECONSTRUCTION; A011 run20261023T000841Z DERIVATION/v2 dependency interface; A011 run20261021T182829Z padding DERIVATION; A011 run20261014T074949Z GENERAL_ENVELOPE; and A095 run20261023T044042Z DERIVATION. A011 v3 interface was consulted for context but is not blanket accepted here. This stage consumes the productive new source dependency; prior rank-code/paper baselines are not repeated or credited as new literature work. Exact source paths and byte hashes are in out/SOURCE_RECEIPTS.json. No priority or external literature claim is made.

## complete derivation or exact first unsupported line

DERIVATION sections1–4 independently reconstruct the entire used dependency chain: actual full point-edit data marginal, true conditional-control entropy, prescribed floor mass and full CE, literal created/erased edge counts, source subprobability inheritance and actual normalizers, entropy/divergence contractions, every padding/source frontier, constant residual sources, a1, final zero-dimensional scalar penalty and additive untouched terminal. Section5 reconstructs A086's complete named allowance without repair, then derives a separately authored sharpening.

The original A086 allowance U<=(C0+1)Ig retains7Ig/8. With q=b+r>=3, padding overhead falls from41/4 to61/8 and the source overhead ratio from3/4 to1/2. Keeping the quantitative2(1+2^-b)c factor yields pre-booking margins at root/final of(3C0/2+45/4)Ig, padding of(2C0+11/2)Ig, and intermediate source of(C0+45/8)Ig, with further nonnegative created-edge terms retained. All exceed or equal(C0+11/2)Ig. Thus NEW U<=(C0+37/8)Ig leaves the SAME7Ig/8 reserve. The allowance increases by29Ig/8 because the q>=3 bounds are sharper; neither the original source bank nor K is renewed.

The proof prices the COMPLETE SIGNED history, retaining negative credits as well as positive charges. It does not price a replacement that discards all credits. The new theorem remains conditional on an influence-priced initial source reference. Larger U does not identify A095's different canonical/narrow-first model with the floor/padding-first model. The first unsupported universal line is a paid compatible handoff of an actual inherited profile conversion, with its reached debit, old bookings and both full terminals retained; arbitrary iteration and universal initial reference supply remain open. A100's differently calibrated/profile charge does not reverse A094's proved positive RAW canonical-reset charge: these are different quantities. No formal compiler was invoked.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC was saved before the pilot. A handwritten pilot frontier count19 was corrected to18 in SPEC_AMENDMENT; the four defined pilot trees were unchanged. An ancillary cost-bound assertion was strengthened from lower to upper interval endpoint before the main run, and the pilot was rerun. All allowance-margin tests already used upper endpoints. No dimension, domain or precision escalation occurred.

Commands from A094: `python -X utf8 runs/{RUN.name}/code/check.py pilot` and the same with `main`, then `code/finalize.py` for exact coefficients and artifact checks. Pilot:4 trees,18 frontiers,{pilot['assertions']} exact assertions PASS in{pilot['seconds']:.3f}s. Main:144 ordered trees,808 frontiers,{main['assertions']} exact assertions PASS in{main['seconds']:.3f}s. The pilot is a subset and is not added to the main total.

Main sources are all nonconstant truth tables on1 and2 bits, plus AND3,parity3,Maj3:19 literal Boolean functions. Padding b2,3; one control; references P_g of mass1 and(P_g+uniform)/4 of mass1/2. Source orders are forward/reverse (one order for a1). Every root, padding prefix, intermediate source prefix and final collapse is checked. Analytic unique-path/symmetry, entropy and integer-sequence arguments prove the remaining all-dimension/all-r/all-adaptive quantifiers; finite checks are not extrapolated.

Own integer Walsh spectra and independent literal edge counts verify functions and physical influence. Fraction arithmetic verifies complete floor masses, source child mass retention, actual model equality at physical restrictions, all stopped siblings, complete signed increment/endpoint/entropy-release ledger identities, boundary scalar penalties and the larger booked-U reserve. No A011/A086 verifier is imported. Logarithms use24-term range-reduced atanh with tail2z^49/[49(1-z^2)], z<=1/3 and outward dyadic rounding2^-70. No floating sign is used. out/COEFFICIENT_CERTIFICATE.json separately verifies rational coefficient identities and the q3 endpoint values; the full monotonicity proof is in DERIVATION. Estimated memory120MB; actual peak unmeasured. Each helper has a55s cutoff. No job above300MB, heavy build, GPU, detached work or process shedding was used.

## proof dependencies and changed downstream conclusions

CLAIMS preserves A086's original exact statement/version/hash and adds the full-scope independent review. The larger allowance is a separate claim pending independent review, not a repair to A086. It depends on the fully reconstructed quantitative A011 v2 interface. There is no blanket acceptance of A011 v3 or of a history/model identification. The global FEI constant improvement is zero. Source adoption, external mirror verification and downstream mathematical use are not presumed.

## one next mathematical action and independent reviewer

A086/A011 should independently reconstruct the q>=3 padding/source maxima and the three all-frontier margins. Then price ONE actual compatible inherited nonempty-profile handoff with the SAME original C0,K and larger allowed U, retaining the actual conversion debit and both complete terminals. This specifically addresses the model/policy gap that a numerical allowance alone cannot close. A095/A096/A097 may consume only the stated signed-ledger interface.

## actual persistence receipts or precise save blocker

The four protocol artifacts, complete derivation, frozen specification/amendment, code, exact outputs, coefficient certificate, source hashes and helper provenance are saved in this run. PROGRESS and PACKET_DELTA are identical with packet_ids=[A094]. STATUS has two lines and WORKLOG/LEARNED retain the result and NEXT. out/SCHEMA_VALIDATION.json checks exact field sets, source/new statement hash conventions, report headings, result counts, coefficient certificate and sizes; out/PERSISTENCE_RECEIPTS.json hashes local artifacts. No file exceeds20MB. Research writes remain inside A094 and shared mathematical sources remain unchanged. Brain wake is degraded: owner-model97.4h stale, state-of-mind82.0h stale, dream32.7h stale; these notes were not mathematical premises. External replication/review is unverified.

## Universal bridge

This stage advances C024 history transfer and C019 stopping-tree payment through C020 complete-reference accounting: A086's entire nonvanishing all-frontier allowance chain is independently reconstructed, and a new q>=3 estimate enlarges compatible external old bookings by29Ig/8 to(C0+37/8)Ig while preserving the SAME7Ig/8 original reserve and every full signed terminal liability. The universal FEI improvement is zero: arbitrary source supply, actual model/policy handoff and fixed-rate iteration remain unpaid. NEXT prices a genuine inherited-profile handoff against this enlarged original allowance because that tests the missing universal compatibility mechanism rather than collecting another isolated class result.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
proto=read(paths[-1])['required_per_run']
assert all(set(c)==set(proto['claim_fields']) for c in claims)
assert set(progress)=={k.split(' (')[0] for k in proto['progress_fields']}
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert all('## '+field in report for field in proto['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(p.stat().st_size<20*1024*1024 for p in RUN.rglob('*') if p.is_file())
save('out/SCHEMA_VALIDATION.json',{'status':'PASS','claim_fields_exact':True,'progress_fields_exact':True,'progress_delta_identical':True,'source_and_new_hashes_verified':True,'report_headings_and_final_bridge':True,'status_two_lines':True,'all_files_under_20MiB':True,'finite_ordered_trees':144,'finite_frontiers':808,'finite_assertions':main['assertions'],'new_independent_review':False,'formal_compilation':False})
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']+[OWN/p for p in ['STATUS.md','WORKLOG.md','LEARNED.md']]
save('out/PERSISTENCE_RECEIPTS.json',{'scope':'Local saved files only; no external mirror or adoption receipt','at':NOW,'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]})
print(json.dumps({'saved_and_validated':True,'ordered_trees':144,'frontiers':808,'assertions':main['assertions'],'allowance_gain':'29Ig/8','remaining_reserve':'7Ig/8','full_FEI':'OPEN','receipt_files':len(files)}))
