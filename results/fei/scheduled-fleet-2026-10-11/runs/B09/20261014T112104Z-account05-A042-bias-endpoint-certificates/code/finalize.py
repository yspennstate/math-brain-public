from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[1];agent=root.parents[1];team=agent.parents[1]
a45=team/'agents/A045/runs/20261014T063646Z-account05-A045-biased-realizability-referee'
a44=team/'agents/A044/runs/20261014T055346Z-account05-A044-non-symmetric-gate-classes'
a43=team/'agents/A043/runs/20261014T052009Z-account05-A043-prime-gate-decomposition'
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def save(name,obj): (root/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(s,h):return hashlib.sha256(json.dumps({'statement':s,'hypotheses':h},sort_keys=True,separators=(',',':')).encode()).hexdigest()
src=next(c for c in json.loads((a45/'CLAIMS.json').read_text(encoding='utf-8')) if c['claim_id']=='A045-SHARP-MEAN-REFUND-PAIR-CONGESTION-NOGO')
assert src['statement_sha256']=='b6f5938ce1562003dfdfc4ecc4e1dbe8f30f6c9875ff965bf34bd7c1a986af9f'
assert hashlib.sha256(src['exact_statement'].encode()).hexdigest()==src['statement_sha256']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
review={'reviewer':'A042/account05','at_utc':now,'verdict':'HOLDS_FULL_STATED_NARROW_OBSTRUCTION_CLAIM','claim_id':src['claim_id'],'version':1,'statement_sha256':src['statement_sha256'],'accepted_scope':['sharp mean-only multiplier and actual AND3 admission','actual fair parity/band selector, pair means and shared top packets','all-r binomial bounds and diverging refunded bill/deficit','ordinary entropy control and exact scope exclusions'],'excluded_scope':['the source separate review record for A044','any selected conditional reference or universal FEI bound'],'repair_supplied':False,'contributor_to_source_version':False,'independence':'new count-profile finite-difference and physical boundary checker, independent analytic binomial/Chebyshev proof; epsilon=1/2 specialization reproduces original constants','evidence':['PROOF.md sections1-3','code/check.py','out/FAMILY.json','out/CHECK.json']}
review['source_hash_convention']='SHA256 of exact_statement UTF8 only, verified against source code/finalize.py; hypotheses pinned by full CLAIMS.json file hash'
save('out/REVIEW_A045.json',review)
reviewed=dict(src);reviewed['review_records']=src['review_records']+[review];reviewed['status']='FULL_NARROW_OBSTRUCTION_INDEPENDENTLY_RECONSTRUCTED_LOCALLY; ORIGINAL_UNCHANGED'
statement=('For the actual parity/band selector on n=16r^2 fair data bits, r>=1, with band sign g positive at counts <=n/2-r or >=n/2+r, '
 'and independent selector probability epsilon in (0,1/2], let F be parity when C=0 and g when C=1. '
 'Let a=2(2r-1)Pr[Bin(n-1,1/2)=n/2-r]/(n-1), m=2epsilon a, '
 'V=4(1-epsilon)+epsilon E Z_g^2-4epsilon^2a^2 for the actual integer data-pair profile. '
 'The complete mean-refunded pair bill is L_kappa=binom(n,2)kappa(m)V/4, and exact signed pair residual is Q_pair=binom(n,2)h(m)/4, '
 'where kappa(m)=2m ln(1/m)/(1-m), h(m)=m^2 ln(1/m^2). '
 'With D=I-Var, L_kappa/D>=epsilon(1-epsilon)ln((n-1)/(4epsilon))/6, '
 'while 0<=Q_pair/D<=10epsilon^2 ln((n-1)/(4epsilon))/n. '
 'On epsilon=1/k,r=2^(k^2),k>=2, the former is >=k ln2/6 and diverges while the latter tends to zero. '
 'Ordinary H/I<=2+2/n, so this is a ledger obstruction, not a FEI disproof. '
 'For any fixed n>=1 and Boolean branch g on fair data, at the same parity-selector endpoint write mu=Eg,t=E[g parity], '
 'b_T=ghat(T)-1_{T=full}, J=sum_all_data_T b_T^2 ln(4/b_T^2), Z=1-t^2-mu^2, '
 'B=sum_nonempty_T_not_full h(ghat(T))-J-3(1-t)^2. '
 'Then corrected natural E=epsilon[2(1-t)+J]+2Z epsilon^2 ln(1/epsilon)+B epsilon^2+O_g,n(epsilon^3), '
 'and exact D=n-1+epsilon[I(g)-n+2-2t]-epsilon^2[2-2t-mu^2]. '
 'At n>=2 the limiting unit atom has positive deficit n-1. At n=1 the four branches yield respectively E=D=0 for g=parity, '
 'E/D->1 for g=-parity and E/D->2+4ln2 for constant branches, with ratios here in natural units. '
 'There is no claim of a bounded selected whole-set reference or universal FEI theorem.')
hyp=['actual Boolean signs and independent physical product inputs; fair data and one biased selector','natural E=(ln2)Hplus, ordinary H in bits, spectral D=I-Var','kappa sum applies to all data pairs with actual strict-superset masses; selector pairs have zero mean','integer r>=1 and 0<epsilon<=1/2 for uniform family bounds; no growing-diagonal brute force','unit-atom expansion fixes g and n; no uniformity in growing dimension is inferred from its remainder','zero entropy terms continuous; deterministic selector contracted before endpoint deficit or ratio interpretation']
claim={'claim_id':'A042-RARE-SELECTOR-CONGESTION-UNIT-ATOM-ENDPOINT','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest(statement,hyp),'contributors':['A042/account05'],'proof_source':{'run_id':root.name,'paths':['PROOF.md','code/check.py','out/CHECK.json','out/FAMILY.json']},'proof_dependencies':['actual parity/band Boolean family and integer pair profiles','physical count compression and exact product Fourier algebra','elementary binomial/Chebyshev argument independently reconstructed in PROOF.md','Taylor expansion at a unit coefficient; empty nonselector atom excluded'],'review_records':[],'status':'SOURCE_COMPLETE_ENDPOINT_MECHANISM_OBSTRUCTION_AND_SYMBOLIC_CERTIFICATES; INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':['Unregistered proposal that vanishing selector probability restores a uniform all-pairs mean-refunded variance price'],'first_unproved_line':None,'next_consumers':['A043','A044','A045','A041','A090','A091','B09','B20']}
save('CLAIMS.json',[claim,reviewed])
checks=json.loads((root/'out/CHECK.json').read_text())
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B09','packet_id':'A042','gap_id':'C020-B09-COHERENT-PAIR-OWNERSHIP-RARE-ENDPOINT','attempt_id':'A042-stage6-rare-selector-unit-atom','method':'independent review plus exact biased selector profile moments, uniform binomial bounds and symbolic parity-unit-atom expansion','mathematical_delta':'Full narrow A045 obstruction independently HOLDS. Extend failure to selector probability tending to zero, with bill/deficit divergent and exact residual/deficit vanishing on the SAME actual Boolean diagonal; corrected entropy expansion explicitly excludes empty nonselector mass.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'ENDPOINT_OBSTRUCTION_AND_EXPANSION_PROVED; WHOLE_SET_PAYMENT_AND_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':src['claim_id'],'version':1,'statement_sha256':src['statement_sha256'],'status':'FULL_NARROW_CLAIM_INDEPENDENTLY_RECONSTRUCTED; actual family and rejected scalar ledger consumed'}],'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'statement_sha256':claim['statement_sha256']},{'claim_id':src['claim_id'],'version':1,'change':'local independent review added; source unchanged'}],'source_artifacts':['PROOF.md','out/FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/FAMILY.json','out/REVIEW_A045.json'],'next_consumers':['A043','A044','A045','A041','A090','A091','B09','B20'],'next_action':'Select or merge the two common top-packet owners in one complete conditional pair reference on the rare parity/band family; pay exact signed residual rather than nonnegative mean-only variance bills and retain all terminal sectors.','stagnant_substantive_attempts':0,'blockers':['No complete selected or merged conditional reference with bounded whole-set/terminal cost.'],'packet_ids':['A042']}
save('PROGRESS.json',progress);(root/'PACKET_DELTA.json').write_bytes((root/'PROGRESS.json').read_bytes())
report=f'''# A042 stage6: rare-selector congestion and unit-atom endpoint certificates

## exact target, quantifiers, hypotheses and units

Analyze whether a selected bias tending to zero repairs the latest B09 mean-refunded pair-variance ledger. The actual Boolean family is A045's band/parity selector, now with arbitrary selector probability0<epsilon<=1/2. Natural E=(ln2)Hplus, D=I-Var is spectral deficit, ordinary H is in bits. Also derive the exact corrected-entropy and deficit endpoint expansions when an arbitrary fixed Boolean branch is attached to a fair parity unit atom. Full FEI remains OPEN.

Result: an actual vanishing-selector family has L_kappa/D>=k ln2/6 tending to infinity, although its exact pair residual/D tends to zero and H/I<=2+2/n. Rarity does not rescue the failed scalar ledger. Unit-atom expansions include the necessary empty-data-atom subtraction and classify the n=1 zero-deficit case. No new universal scalar payment is proposed.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot2026-10-14 11:15UTC, targeted B09 after full-board display truncation; B09 STREAM_NOTES.md v2 (2026-10-11 23:33); own STATUS/LEARNED; and complete EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2. Read A043 stage5 REPORT.md and PROOF.md, run20261014T052009Z, which now closes prime56067 at a nonsharp global constant and independently accepts own prior endpoint theorem. That steers this stage away from repeating its closed all-bias bound.

Read A044 stage5 PROOF.md and CLAIMS opening, run20261014T055346Z, for the integer physical mixed-profile interface and congestion frontier. Read A045 stage5 REPORT.md and CLAIMS.json, run20261014T063646Z-account05-A045-biased-realizability-referee; exact source {src['claim_id']}@1 hash {src['statement_sha256']}. The source proof is in REPORT.md; no separate PROOF.md exists there, as a read attempt confirmed. Independently reconstruct its sharp admission, binomial lower bound, ownership and entropy control in PROOF.md sections1-3. A persistence pilot initially assumed compound statement/hypothesis hashing; reading source code/finalize.py confirmed that this source instead hashes exact_statement alone. That original recorded hash is reproduced unchanged; the complete source CLAIMS file pins hypotheses. The new A042 claim uses compound hashing. No source checker was copied/executed. No external paper/web/brain premise or lead-tax recomputation is used. Source hashes saved locally.

## complete derivation or exact first unsupported line

PROOF.md contains the complete argument. For n=16r^2, every data-pair profile mean is m=2epsilon a and its variance is V=4(1-epsilon)+epsilon E Z_g^2-m^2. Thus the exact total pair residual is binom(n,2)h(m)/4, while the refunded bill is binom(n,2)kappa(m)V/4. The two common high-degree packets have mass(1-epsilon)+epsilon t^2>=1-epsilon. Uniform actual-family binomial bounds imply

    L_kappa/D>=epsilon(1-epsilon)ln((n-1)/(4epsilon))/6,
    0<=Q_pair/D<=10epsilon^2 ln((n-1)/(4epsilon))/n.

Take epsilon=1/k,r=2^(k^2),k>=2. The bill ratio diverges at least linearly, while the exact residual ratio vanishes. These dimension-uniform bounds prove the joint limit directly; no fixed-dimension Taylor remainder is substituted into it. The ordinary H/I control excludes any FEI-disproof interpretation.

For arbitrary fixed Boolean g on n fair bits, put mu=Eg,t=E[g parity]. Corrected entropy is epsilon[2(1-t)+J]+2(1-t^2-mu^2)epsilon^2 ln(1/epsilon)+B epsilon^2+O_g,n(epsilon^3), with J,B explicit in PROOF.md. Deficit is the exact quadratic (13). The empty NONSELECTOR data atom must be excluded; the selector-containing empty DATA atom is included. At n>=2 the unit atom has D=n-1; at n=1 all four branches are explicitly classified. There is no first-order epsilon ln term.

First unsupported universal line: a selected or merged conditional reference must retain exact signed costs and full terminal spectra while charging the common high-degree owners only once. Neither the valid local profile lemma nor rare activation supplies that reference. Full A045 narrow source claim independently HOLDS, with no repair and no acceptance of its separate A044 meta-review.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json preceded execution. `python -X utf8 code/check.py`: {checks['assertions_passed']} exact assertions PASS, {checks['runtime_seconds']:.3f} seconds, one pilot and no failed check. 24 exact physical count-compressed laws cover r=1..8,n=16..1024, epsilon=1/2,1/8,1/64. Each certificate is saved immediately to out/FAMILY.json. Independent second finite differences, physical boundary influence and selector disagreements verify exact means, variances, top-packet mass, entire L_kappa and Q_pair formulas and rigorous inequalities. Fair-selector specializations recover A045's precise original lower constants.

44 direct moment fixtures include all one-bit and all two-bit Boolean branches at two fixed selector biases, plus four fixed three-bit branches at one bias. Independent actual truth-table product moments agree with every selected and unselected spectrum atom, exact deficit quadratic and entropy normalization (11); Parseval checks the excluded empty-atom term. These finite cases validate identities; the all-r rare diagonal and endpoint expansions are proved analytically. No exponentially large diagonal truth table is computed.

Arithmetic is Fraction with exact integer binomials. Log intervals use24-term range-reduced atanh sums, tail <=2z^49/[49(1-z^2)], z<=1/3. All strict bounds use rational outward intervals. Estimated memory90MB, peak unmeasured; no >300MB job, memok trigger, heavy job, automatic domain growth, GPU or background process.

## proof dependencies and changed downstream conclusions

Dependencies are actual Boolean cofactor/count identities, physical product Fourier algebra and elementary Chebyshev/binomial/logarithm/Taylor bounds, reconstructed here. A045's source is independently accepted at its complete stated narrow obstruction scope. Its review record is copied locally without modifying the original or claiming acceptance of its other reviewed theorem. New rare-selector extension and unit-atom expansion need independent review.

B09/A043/A044/A041/A045 must not use vanishing selector bias to restore all-pairs mean-only variance funding. The exact residual and its variance majorant have opposite ratio behavior on the same actual family; merging owners must preserve this distinction. The source A044 local packet inequality and A043's newly closed prime upper theorem remain intact. No FEI constant or all-arity payment is gained.

## one next mathematical action and independent reviewer

NEXT: construct a single selected/merged conditional reference for the rare parity/band fixture, owning the two shared top packets once and retaining exact signed residual plus all terminal sectors. A043/A044/A045 should consume the rare endpoint obstruction; A090/A091 should reconstruct the uniform diagonal bounds, the unit-atom empty-atom exclusion and n=1 classification. Do not tune another scalar variance multiplier: A045's optimality and this endpoint extension already rule out that unchanged mechanism.

## actual persistence receipts or precise save blocker

Four protocol files, complete PROOF.md, frozen specification, new checker, immediately saved family certificates, exact output and source-bound review are saved in this run only. Rolling STATUS.md has two lines; WORKLOG.md and LEARNED.md are appended. out/VALIDATION.json checks schemas, hashes, headings, sizes and progress-copy equality; out/PERSISTENCE.json records actual local artifact sizes/hashes. No save blocker. Supervisor copy, registry adoption, independent review of the new extension, brain ingestion and mirror verification remain pending; no remote save is asserted.

**Universal bridge:** This stage advances the B09 C025/G-BIASED-LTF localization frontier through its C020 whole-set ownership gap: it independently accepts the latest scalar-refund obstruction and proves that it persists even at a vanishing selector bias, with refunded bill/deficit diverging while the exact pair residual/deficit vanishes. The parity unit-atom expansion supplies the corrected endpoint normalization and zero-deficit special cases needed by a conditional reference. No universal entropy constant is gained; selected/merged owner cost with complete terminals remains open. NEXT attacks the same repeated high-degree ownership with exact signed charges, the shortest surviving route after both raw and optimally mean-refunded all-pairs variance ledgers have failed, rather than another isolated gate or scalar calibration.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8')
state='STATE: A042 stage6 saved: A045 narrow no-go independently HOLDS; vanishing-selector bill/D diverges while exact pair residual/D vanishes; unit-atom/zero-deficit expansions;819 exact checks PASS; FEI OPEN.\nNEXT: A043/A044/A045 merge shared top-packet ownership in one complete conditional reference; A090/A091 review rare diagonal and empty-atom normalization.\n'
(agent/'STATUS.md').write_text(state,encoding='utf-8')
if 'stage6 rare-selector' not in (agent/'WORKLOG.md').read_text(encoding='utf-8'):
 with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} stage6 rare-selector: read new prime closure and scalar-refund no-go. Independently accepted A045 full narrow obstruction; derived rare-selector extension with divergent majorant/D and vanishing exact residual/D on explicit diagonal. Derived corrected parity unit-atom expansion with log coefficient excluding empty data mass. 819 exact checks in {checks["runtime_seconds"]:.3f}s, no heavy job. Whole-set ownership/FEI open.\n')
if 'Stage6 rare-selector:' not in (agent/'LEARNED.md').read_text(encoding='utf-8'):
 with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage6 rare-selector: for band/parity family n=16r^2, selector eps<=1/2, m=2eps*a, V=4(1-eps)+eps*E Zg^2-m^2, exact pair residual=choose(n,2)h(m)/4 versus kappa bill=choose(n,2)kappa(m)V/4. Bill/D>=eps(1-eps)ln((n-1)/(4eps))/6; exact residual/D<=10eps^2 ln((n-1)/(4eps))/n. At eps=1/k,r=2^(k^2), bill/D>=k ln2/6 while exact residual/D->0. H/I<=2+2/n. For fixed parity branch and arbitrary g, corrected E=eps[2(1-t)+J]+2(1-t^2-mu^2)eps^2ln(1/eps)+B eps^2+O(eps^3); exclude empty NONSELECTOR atom, include selector+empty data atom. Exact D=n-1+eps[Ig-n+2-2t]-eps^2[2-2t-mu^2]. n1 zero-deficit branch ratios: unchanged parity E=D=0, negated parity natural ratio1, constants natural ratio2+4ln2. A045 full narrow no-go independently HOLDS; rare bias does not repair scalar all-pairs ownership.\n')
paths=[protocol,team/'BOARD.md',team/'claude/B09/STREAM_NOTES.md',a43/'REPORT.md',a43/'PROOF.md',a44/'PROOF.md',a44/'CLAIMS.json',a45/'REPORT.md',a45/'CLAIMS.json',a45/'code/finalize.py']
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p)} for p in paths])
pr=json.loads(protocol.read_text())['required_per_run']
for c in (claim,reviewed):
 assert set(c)==set(pr['claim_fields'])
 assert (digest(c['exact_statement'],c['hypotheses']) if c['claim_id']==claim['claim_id'] else hashlib.sha256(c['exact_statement'].encode()).hexdigest())==c['statement_sha256']
assert set(progress)=={s.split(' (')[0] for s in pr['progress_fields']}
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
assert all('## '+h in report for h in pr['report_fields'])
assert len(state.splitlines())==2
assert checks['assertions_passed']==819 and checks['family_cases']==24 and checks['unit_atom_direct_cases']==44
assert all(p.stat().st_size<20*1024*1024 for p in root.rglob('*') if p.is_file())
save('out/VALIDATION.json',{'schemas':'PASS','statement_hashes':'PASS','progress_copy':'PASS','report_headings':'PASS','status_two_lines':'PASS','file_sizes':'PASS','exact_checks':819,'full_fei':'OPEN'})
save('out/PERSISTENCE.json',[{'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(root.rglob('*')) if p.is_file() and p.name!='PERSISTENCE.json'])
print(json.dumps({'local_save':'COMPLETE','schema_validation':'PASS','assertions':819,'claim_sha256':claim['statement_sha256']}))
