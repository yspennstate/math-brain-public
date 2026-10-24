from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[3]
run=Path(__file__).resolve().parents[1]
def save(name,data):
    (run/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
cert=json.loads((run/'out/CERTIFICATES.json').read_text(encoding='utf-8'))
finite_path=run/'out/FINITE_HOD_CERTIFICATE.json'
finite=json.loads(finite_path.read_text(encoding='utf-8')) if finite_path.exists() else None
report_fields=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
statement=('Exact tensor and balanced-core activation identities preserve the optimal universal FEI constant; the complete restriction-tree minority retained-KL charge Q satisfies Q<=H<=Q+(3/ln2)I. Certified balanced seed amplification gives C_FEI>6.278944 and Hod rational limit recurrence gives C_FEI>6.4547837, all as constant lower bounds only.' + (' The explicitly defined finite monotone formula F_(48,80) on 81^48 bits has H/I>6.4547837 by rational interval propagation.' if finite else ' Finite Hod interval propagation remains incomplete; no finite high-ratio formula certificate claimed.'))
claim={
 'claim_id':'A080-UNIVERSAL-DISPROOF-STANDARD-AND-LOWER-BOUND-AUDIT',
 'version':1,'exact_statement':statement,
 'hypotheses':['Actual finite sign-valued Boolean functions on uniform cubes','Entropy in bits, empty spectral atom included','Total physical influence','Independent operand blocks in tensor and composition identities','Q uses minority parent spectral mass, not an unoriented child-difference mass'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A080 (independent baseline/literature reconstruction; finite certificate implementation)'],
 'proof_source':{'path':str(run/'FEI_DISPROOF_STANDARD.md'),'validation':[str(run/'out/CERTIFICATES.json')]+([str(finite_path)] if finite else [])},
 'proof_dependencies':[{'id':'C005','version':'supplement CLAIMS.md, 2026-10-11; reconstructed scalar proof in standard'},{'id':'C013','version':'threshold 38pp Proposition 8.9 and Corollary 8.10; reconstructed'},{'id':'Hod-2017','version':'arXiv:1711.00762 PDF, Sections 1.2 and 4.1; scalar identities reconstructed'}],
 'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A092','A088','B16 lead','B20','A046','A076','A077','A078']}
save('CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2',
 'run_id':run.name,'stream':'B16','packet_id':'A080','gap_id':'G-UNIVERSAL-COUNTEREXAMPLE-STANDARD','attempt_id':'A080-stage1-standard-and-primary-source-reproduction',
 'method':'Analytic quantifier/normalization audit; exact integer Walsh and rational log certificates; finite disjoint-gate interval propagation',
 'mathematical_delta':statement,
 'deliverable_status':'COMPLETE_WITH_EXPLICIT_HISTORICAL_SOURCE_GAP',
 'mathematical_status':'SCOPED_BASELINE_AND_CONSTANT_CERTIFICATES_PROVED; FULL_FEI_OPEN; REVIEW_PENDING',
 'claim_versions_used':claim['proof_dependencies'],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['FEI_DISPROOF_STANDARD.md','FROZEN_SPEC.json','FROZEN_FINITE_HOD.json','FROZEN_GATE_CHECK.json','out/CERTIFICATES.json','out/GATE_RECONSTRUCTION.json','out/SOURCE_READ_MANIFEST.json']+(['out/FINITE_HOD_CERTIFICATE.json'] if finite else []),
 'next_consumers':claim['next_consumers'],
 'next_action':'A092/A088 independently reconstruct the finite Hod gate entropy and rational enclosure; then apply this standard to the next source-complete B16 candidate, requiring actual unbounded H/I and terminal costs.',
 'stagnant_substantive_attempts':0,
 'blockers':['OWZ 2011 consulted paper states 60/13 without defining its asserted explicit family; historical-family reconstruction not claimed.','Independent review and supervisor mirrors not performed.']+([] if finite else ['Finite Hod certificate not completed.']),
 'packet_ids':['A080']}
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
for c in [claim]: assert set(c)==set(report_fields['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in report_fields['progress_fields']}
finite_text=(f"The explicit F_(48,80) formula on 81^48={finite['dimension']} bits passed {finite['recurrences']} exact scalar interval recurrences in {finite['runtime_seconds']:.3f} seconds. Its certified ratio endpoints are in out/FINITE_HOD_CERTIFICATE.json; decimal display {finite['final_ratio_decimal_display']}." if finite else 'The finite-formula certificate did not complete; its first unsupported line is the final interval comparison H/I>6.4547837. No success is claimed for it.')
sections={
report_fields['report_fields'][0]: 'For every candidate uniform-cube FEI disproof require actual finite Boolean f_m, I(f_m)>0, and a proved H(f_m)/I(f_m)->infinity. The delivered standard fixes all quantifiers, physical influence, the empty atom, log units, conditional nonempty normalization, additive constants and rare-control overhead. FEI remains OPEN. Literature values are constant lower bounds.',
report_fields['report_fields'][1]: 'Execution protocol v2; campaign README/status/registries/plan and three earlier B05/B09/B19 reports; supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and sources; BOARD at stage start and B16 lead v1 (22:45Z). Texts of both threshold and percolation revisions were inspected for theorem scope; the used threshold sections 7 and 8.4 (Prop. 8.9, Cor. 8.10) were read with proofs. Primary OWZ Section 1, O\'Donnell-Tan Section 5, Hod Sections 1.2, 2.4, 4.1 and Appendix A.4 were consulted. Exact local byte hashes are in out/SOURCE_READ_MANIFEST.json. Some large batched tool output was truncated; no source-complete audit of every manuscript theorem is claimed. No percolation theorem is used as a proof dependency.',
report_fields['report_fields'][2]: 'FEI_DISPROOF_STANDARD.md supplies all derivations: Boolean XOR admission; tensor/spectator and additive-error limits; balanced activation formula and seed-dependent diagonal; physical Q/B/JS telescope including stopping leaves; collision-free balanced gate recursion; finite Hod gate sector entropy and its limit bridge. '+finite_text+' The particular historical OWZ family is not reconstructed: the first missing line is its Boolean definition, absent from the consulted primary text. Instead, a separately defined later gate already certifies a stronger lower bound. Hod\'s printed six-decimal >6.454784 is not justified by beta(1/2); the certified strict bound is >6.4547837.',
report_fields['report_fields'][3]: f"Frozen finite domain: gm m=2..6, corrected variants n=6,8, all 16 two-bit transformation seeds; integer Walsh/Fraction calculations, direct edge influence, independent direct Walsh summation for g3; {cert['assertions']} exact assertions PASS in {cert['runtime_seconds']:.3f}s. Commands: python -X utf8 {run/'code/check.py'}; python -X utf8 {run/'code/finite_hod.py'}; python -X utf8 {run/'code/gate_check.py'}. The first check hit Python's 4300-digit serialization limit; outward dyadic log rounding fixed certificate growth. Initial finite-Hod attempts self-stopped at frozen 60s and 180s caps. The L=80,16-term/64-bit version completed but returned [6.4547836092,6.4547838235], too wide for the target. The final spec explicitly increases precision to 28-term/80-bit with intermediate atanh rounding at 112 bits, leaving the frozen formula dimension unchanged. The direct gate checker found and repaired an OR-for-AND sign error in its truth-table reconstruction and in the explanatory polynomial; after correction, all 256 disjoint two-bit pairs passed, including 196 interior conjunction-entropy cases, with direct Walsh sums and physical pivotal-edge influence. The scalar formula itself was unchanged. All memory estimates <100MB; no dimension enumeration escalation or GPU. Rational atanh remainders, positive-denominator division, binary entropy extrema and dyadic outward rounding certify signs; floating output is display only. "+finite_text,
report_fields['report_fields'][4]: 'The C005/C013 identities and Hod conjunction formulas are independently re-derived in the delivered standard; original sources are retained as provenance. No new universal paid estimate is proved. Downstream proper-block constants must confront arbitrary spectator seeds and literature lower bounds. Q/I tests on already bounded-H/I families cannot move C019. A divergence of Lambda_T alone remains a surrogate obstruction. Status labels, certificates and mirror receipts are distinguished.',
report_fields['report_fields'][5]: progress['next_action']+' Independent reviewers: A092 (primary), A088 (alternate); neither has reviewed this stage. Recover the historical OWZ formula only if a source-bound review requires it; do not let that baseline gap replace the universal frontier.',
report_fields['report_fields'][6]: 'Saved locally in the assigned A080 run only: standard, REPORT, CLAIMS, PROGRESS, compatibility PACKET_DELTA, frozen specs, code, exact outputs, source manifest and hashed file receipts. Rolling STATUS/WORKLOG/LEARNED updated locally. No shared indices, other agents, git, brain writes, mail, publication or mirror mutations. out/PERSISTENCE_RECEIPTS.json records file SHA256/bytes and actual local save time. Supervisor copying and independent review are pending.'}
text='# A080 / B16 — universal-counterexample standard\n\n'
for heading,body in sections.items(): text+='## '+heading+'\n\n'+body+'\n\n'
text+='## Universal bridge\n\nThis stage moves the lead-named universal-counterexample standard and clarifies C019: complete-tree retained-KL Q and actual entropy differ by at most (3/ln2)I, while stopping trees must retain terminal entropy. It closes the normalization/finite-ratio acceptance interface and reproduces certified constant lower bounds; it pays no previously unpaid universal remainder and finds no unbounded-ratio Boolean family. C018/C019/C020/C024 remain open at their universal endpoints. NEXT is independent reconstruction followed by applying this standard to a new source-complete candidate: this is the shortest route because it rejects surrogate-only growth, retains genuine Booleanity and physical influence, and directs work to an actual all-dimensional endpoint rather than another bounded-ratio class.\n'
(run/'REPORT.md').write_text(text,encoding='utf-8')
(root/'STATUS.md').write_text('STATE: A080 standard and constant certificates saved; '+('finite Hod F_(48,80) certified >6.4547837; ' if finite else 'finite Hod gap explicit; ')+'FEI OPEN, review pending.\nNEXT: A092/A088 reconstruct certificates; apply standard to the next B16 candidate with actual unbounded H/I and full terminal costs.\n',encoding='utf-8')
with (root/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+datetime.now(timezone.utc).isoformat()+': Completed standard; 663 exact baseline checks. Recorded bounded aborted finite-Hod pilots and revised exact precision. '+finite_text+' OWZ historical formula remains a precise source gap. Local artifacts saved; review/mirrors pending.\n')
(root/'LEARNED.md').write_text('''# A080 durable facts

- A finite or bounded limiting H/I only lowers the universal constant. A disproof needs actual finite Boolean functions with unbounded ratio.
- Tensor powers preserve H/I and remove fixed additive errors; balanced recursive composition has a distinct finite ceiling H(g)/(I(g)-1).
- Rare activation preserves the optimal FEI constant after seed tensoring; r/(tI(seed)) must vanish. Empty and control-only atoms cannot be dropped.
- For parent minority packets Q, every complete physical restriction tree satisfies Q<=H<=Q+(3/ln2)I. A Q/I counterfamily is FEI-strength; Lambda surrogate growth is not.
- Exact g3 correction (Hod) yields C>6.278944; Hod beta(1/2) is between 6.4547837159 and 6.4547837169, so >6.454784 is an upward-rounded overstatement for this construction.
- Finite monotone F_(48,80) on 81^48 bits has certified H/I in [6.454783715947497,6.45478371595095]; 3840 exact scalar interval steps avoid enumerating its truth table. Final rational endpoints, rather than these floating displays, are the certificate.
- OWZ's consulted 2011 paper asserts 60/13 without a formula; record the historical-source gap rather than inventing the family.
- Outward dyadic rounding of exact log enclosures prevents Fraction denominators from exploding. Lower precision with a proved remainder can give the required sign much faster.
''',encoding='utf-8')
receipts=[]
for p in run.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
save('out/PERSISTENCE_RECEIPTS.json',{'saved_at_utc':datetime.now(timezone.utc).isoformat(),'local_only':True,'files':receipts})
print(json.dumps({'status':'SAVED','claims':1,'finite_Hod_certified':bool(finite),'run':str(run),'files':len(receipts),'schema_checks':'PASS'},indent=2))
