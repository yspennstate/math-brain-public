from pathlib import Path
import json,importlib.util
R=Path(__file__).resolve().parents[1]
p=R/'code/finalize.py';s=p.read_text(encoding='utf-8')
s=s.replace('MAJORITY_CHECK','MIXED_CHECK')
s=s.replace('Maj3(y0,y1,y2)','(-1)^y2*(1-2*1[y0=y1=0])')
s=s.replace('Maj3 priority fixture','Character-times-point-defect priority fixture')
s=s.replace('python -X utf8 -B code/check.py --majority','python -X utf8 -B code/check.py --mixed')
s=s.replace('SUPPLEMENT_SPEC then freezes a separate fixed six-bit Maj3 fixture, with no automatic dimension escalation.', 'SUPPLEMENT_SPEC freezes Maj3, but its support requirement fails: every second-query erased fiber has source mass. MIXED_CORE_SPEC then freezes a character times a two-bit point defect at the SAME six-bit dimension; no automatic dimension escalation occurs. The failed support choice is retained in MAJORITY_SUPPORT_AUDIT and FAILURE_AND_SCOPE.md.')
s=s.replace('Separately froze fixed Maj3 six-bit non-flat continuation;', 'Maj3 support requirement failed; separately froze a mixed-core six-bit continuation;')
s=s.replace("'status':'EXACT_FINITE_CERTIFICATE_PENDING_INDEPENDENT_REVIEW'", "'status':'INDEPENDENT_FIXED_SUBSTATEMENT_REPRODUCED'" )
s=s.replace("'review_records':[]", "'review_records':[{'reviewer':'A038','verdict':'HOLDS_FIXED_SUBSTATEMENT_ONLY','source':'A039 runs/20261014T055326Z-account05-A039-projection-under-restrictions, fixed-reference final-frontier payment','scope':'Only the explicitly stated core and query tree; independent direct Fourier and interval implementation. No acceptance of the whole all-core/all-policy theorem.'}]")
s=s.replace('Close the saved next-data ownership test on one actual non-flat core,', 'Independently reproduce a fixed substatement of the already completed A039 next-data ownership test on one actual non-flat core,')
s=s.replace('Exact finite terminal laws independently certify S0 and Sfinal;', 'A039 already covers every essential non-flat three-bit core. This stage is an independent fixed-substatement reproduction and support audit, not a new class result. Exact finite terminal laws independently certify S0 and Sfinal;')
s=s.replace('The finite certificate gives W<min(S0,Sfinal),', 'At this explicitly limited scope, the finite certificate gives W<min(S0,Sfinal),')
s=s.replace('One explicit non-flat coherent data query is certified with the SAME inherited canonical reference', 'An already covered A039 fixed substatement is independently reconstructed with the SAME inherited canonical reference')
s=s.replace('COMPLETE_LOCAL_EXACT_FINITE_CERTIFICATE','COMPLETE_LOCAL_INDEPENDENT_FIXED_SUBSTATEMENT_REVIEW')
s=s.replace('FINITE_SOURCE_INTERFACE_CLOSED_UNIVERSAL_OWNERSHIP_OPEN','KNOWN_FINITE_SOURCE_INDEPENDENTLY_REPRODUCED_UNIVERSAL_OWNERSHIP_OPEN')
s=s.replace('This stage moves the C024 history-transfer/C019 terminal-ownership interface by certifying one complete non-flat two-query continuation', 'This stage adds independent fixed-substatement verification at the C024 history-transfer/C019 terminal-ownership interface for one complete non-flat two-query continuation already covered by A039')
s=s.replace('A038 stage6 local exact non-flat inherited-reference certificate saved;', 'A038 stage6 independent A039 fixed-substatement reproduction saved;')
s=s.replace('Lean is a separate limited row-algebra check if its tool receipt succeeds; no Lean certification of the full information statement is claimed without that receipt.', 'The fresh memok check returned WAIT (physical free 2.0GB<4.0GB, commit free 6.4GB<8.0GB), so the guarded Lean helper was not launched. Rung: exact finite rational certificate, not Lean-checked. No heavy job was started.')
s=s.replace("'out/SUPPLEMENT_SPEC.json','out/CHECK.json'", "'out/SUPPLEMENT_SPEC.json','out/MIXED_CORE_SPEC.json','REVIEW_A039.md','out/CHECK.json'")
p.write_text(s,encoding='utf-8')
# Independently certify the failure of the proposed Maj3 support test on the same frozen domain.
spec=importlib.util.spec_from_file_location('a038check',R/'code/check.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
t=[]
for z in range(64):
 x,a,b=[(z>>j)&1 for j in range(3)];v=-1 if (z>>3).bit_count()>=2 else 1
 t.append((-1 if a else 1) if x==0 else (v if b else 1))
audit=[]
for b in range(2):
 a=m.spectrum(m.restrict(t,1,b));p0=[w*w for w in a]
 zeros=sum(p0[i]+p0[i|4]==0 for i in range(32) if not i&4)
 coherent=sum(a[i]*a[i|4]!=0 for i in range(32) if not i&4)
 assert zeros==0 and coherent>0
 audit.append({'a':b,'zero_source_erased_rows':zeros,'coherent_erased_rows':coherent,'erased_rows':16})
(R/'out/MAJORITY_SUPPORT_AUDIT.json').write_text(json.dumps({'status':'SUPPORT_REQUIREMENT_REFUTED','domain':'frozen Maj3 six-bit fixture, both next y0 queries','arithmetic':'direct exact Fraction Fourier sums','rows':audit},indent=2)+'\n',encoding='utf-8')
(R/'out/LEAN_ADMISSION.txt').write_text('Fresh memok output: WAIT: physical free 2.0 GB (need 4.0), commit free 6.4 GB (need 8.0). Exit 1. Guarded lean_check.py invocation was not run. No Lean certificate.\n',encoding='utf-8')
(R/'FAILURE_AND_SCOPE.md').write_text('''# Failed support choice and review scope

The first five-bit point-defect fixture passed but has no second-query reference-only rows and zero positive bookings. It cannot test that support issue.

The next proposed Maj3 fixture also fails its source-zero-row requirement. Exact direct Fourier sums in out/MAJORITY_SUPPORT_AUDIT.json show zero source-zero erased rows at each of its two second-level nodes. This is a failure of A038\'s fixture choice, not a refutation of any upstream theorem or a completed payment certificate. The mixed character-times-point-defect fixture is separately frozen at the same six-bit dimension before execution.

The latest A039 source already covers every essential non-flat three-bit core. The final finite certificate is therefore an independent fixed-substatement reproduction. It is not new all-core mathematics. A050\'s newer arbitrary-data continuation and A047\'s full canonical-price obstruction remain distinct statements; this finite reproduction accepts neither bundle. The first unpaid target is a strictly positive additional inherited-reference conversion under earlier genuinely spent debits and an unchanged original owner.
''',encoding='utf-8')
(R/'REVIEW_A039.md').write_text('''# Independent review: limited fixed substatement

Source: A039/runs/20261014T055326Z-account05-A039-projection-under-restrictions/REPORT.md, fixed-reference final-frontier payment. Its stated finite scope contains all essential non-flat three-bit cores and all two-query policies. The core (-1)^y2*(1-2*1[y0=y1=0]) and a-then-y0 policy below are included.

Verdict: HOLDS for this fixed substatement only, conditional on the completed rational certificate in out/MIXED_CHECK.json. The checker independently constructs every physical Fourier coefficient by direct character summation, uses a separately implemented rational interval evaluator and the same original canonical reference, verifies source pushes atom by atom, retains positive inherited reference mass on source-zero rows, and keeps all four terminal H/I bills. No peer checker was imported or executed. No substantive repair of A039 is supplied and no broad all-core or all-policy acceptance is issued.

The intermediate TC values in PROOF are comparison potentials in one unchanged-reference history. They are not actual intermediate resets whose Bayes references are then resurrected. This distinction prevents a false double account. No fresh global FEI theorem follows.
''',encoding='utf-8')
print('Prepared final source, exact failed-support audit, scoped review and Lean-admission receipt.')
