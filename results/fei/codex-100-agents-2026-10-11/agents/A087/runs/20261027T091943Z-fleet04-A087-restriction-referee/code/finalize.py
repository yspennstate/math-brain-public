from audit import *
from datetime import datetime,timezone
import copy

def main():
    audit=json.loads((RUN/'out/AUDIT.json').read_text(encoding='utf-8'))
    adversary=json.loads((RUN/'out/ADVERSARY.json').read_text(encoding='utf-8'))
    assert audit['status']==adversary['status']=='PASS'
    protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
    sources=json.loads((RUN/'out/SOURCES.json').read_text(encoding='utf-8'))
    for p in [ROOT.parent/'BOARD.md',ROOT.parent/'claude/B18/STREAM_NOTES.md',ROOT/'A091/runs/20261027T054729Z-fleet04-A091-composition-referee/REPORT.md']:
        sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':'board/lead navigation or read-only context; no new dependency acceptance'})
    save('out/SOURCES.json',sources)
    imported=json.loads((SRC/'CLAIMS.json').read_text(encoding='utf-8'))[0]
    assert imported['statement_sha256']==hashlib.sha256(imported['exact_statement'].encode('utf-8')).hexdigest()
    assert sha(SRC/'PROOF.md')==imported['proof_source']['sha256']
    claim=copy.deepcopy(imported)
    claim['review_records'].append({'reviewer':'A087/fleet04','verdict':'HOLDS_AT_STATED_SELECTED_POLICY_SCOPE_NO_REPAIR','scope':'Independent all-dimensional max-potential and source-price reconstruction, exact labelled physical children, full mixed references, Bellman adaptive-cut maximization, both terminal H and KL. No arbitrary-core price or all-policy theorem. Not Lean-checked.','proof_source':str(RUN/'PROOF.md'),'validation':[str(RUN/'out/AUDIT.json'),str(RUN/'out/ADVERSARY.json')]})
    claim['status']='INDEPENDENTLY_RECONSTRUCTED_HOLDS_AT_STATED_SCOPE'
    st='For the actual 7-bit Boolean source point4 times point3, with a common selected product-reset boundary r=3 and exact initial reference, installing the point3 product reference before querying point4 gives full cross entropy H(point4)+M(point3) greater than max(H(point4)+H(point3),3*M(point3)/2)+1/5 bit. The two terms in this maximum are the immediate-stop and completed expected full-terminal bills. Both actual point4 query children preserve the frozen point3 full reference. Thus the identical-block endpoint maximum cannot be substituted for the sum of local maxima on heterogeneous live blocks. This is a selected-policy accounting guard, not a counterexample to A061 or FEI.'
    guard={
      'claim_id':'A087-HETEROGENEOUS-SELECTED-CUT-ENDPOINT-GUARD','version':1,'exact_statement':st,
      'hypotheses':['Uniform labelled physical source p4(x)p3(y), disjoint blocks; bits.','point_s=1-2*1_{0^s}; M=sum coordinate marginal entropies.','Selected policy queries live blocks down to three bits, installs true marginal products and freezes; all full terminal H and KL retained.'],
      'statement_sha256':hashlib.sha256(st.encode('utf-8')).hexdigest(),'contributors':['A087/fleet04'],
      'proof_source':{'path':str(RUN/'PROOF.md'),'sha256':sha(RUN/'PROOF.md'),'validation':[str(RUN/'code/adversary.py'),str(RUN/'out/ADVERSARY.json')]},
      'proof_dependencies':[],'review_records':[{'reviewer':'A087','verdict':'AUTHOR_EXACT_CERTIFICATE_EXTERNAL_REVIEW_PENDING','scope':'128 actual Fourier atoms; both physical children; outward rational sign gap >1/5.'}],
      'status':'EXACT_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
      'first_unproved_line':None,'next_consumers':['A061','A064','A065','A094','B20']}
    save('CLAIMS.json',[claim,guard])
    formal='import Lean.Elab.Tactic.Omega\n\ntheorem A087MaxHalf (a b c d : Nat) (h1 : a <= 2*c) (h2 : b <= 2*d) : max a b <= 2 * max c d := by\n  omega\n'
    (RUN/'code/MaxHalf.lean').write_text(formal,encoding='utf-8',newline='')
    save('out/FORMAL.json',{'status':'ADMISSION_HELD_NOT_COMPILED','command_executed':'python -X utf8 tools\\memok.py','exit_code':1,'output':'WAIT: physical free 3.9 GB (need 4.0), commit free 9.2 GB (need 8.0)','planned_command':'python -X utf8 lean_check.py --core --file code/MaxHalf.lean --target A087MaxHalf --reviewed-sha256 <source_sha256> --timeout 50 --json','planned_environment':{'LEAN_JOB_MEMORY_MB':'1024'},'source_sha256':sha(RUN/'code/MaxHalf.lean'),'compiler_started':False,'verified_target':False,'axioms_verified':False,'scope':'Natural-number max/subdoubling analogue only; does not certify entropy or stopping theorem.'})
    progress={
      'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B18','packet_id':'A087',
      'gap_id':'G-SELECTED-TERMINAL-ORIGINAL-FUNDING','attempt_id':'A087-stage22-deep-selected-policy-independent-audit',
      'method':'Independent exact physical-child reconstruction; all-dimensional full-CE max-potential; Bellman adaptive-cut audit; heterogeneous actual-cut adversary',
      'mathematical_delta':'A061 deep selected-data policy independently HOLDS unchanged, including activated exact capital max(H(Z),delta*K_r), all-cut original8I payment after old debit<=I, and sqrt(m) boundary with t=O(m). New 7-bit heterogeneous endpoint guard has strict gap>1/5. Full FEI and arbitrary-core original funding remain OPEN.',
      'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_SOURCE_HOLDS_NEW_EXACT_GUARD_PENDING_REVIEW_FULL_FEI_OPEN',
      'claim_versions_used':[{'claim_id':claim['claim_id'],'version':1}],
      'claims_created_or_changed':[claim['claim_id']+'@1',guard['claim_id']+'@1'],
      'source_artifacts':sources,'next_consumers':['A061','A064','A065','A094','B20'],
      'next_action':'A094 independently review the heterogeneous cut guard; A061/A064/A065 replace point-factor entropy source by an ORIGINAL O(I) source or useful entropy-decaying compatible selected rule for arbitrary indecomposable cores, retaining old bills/query KL/BOTH full terminals.',
      'stagnant_substantive_attempts':0,
      'blockers':['Universal arbitrary-core ORIGINAL influence-priced source remains unpaid; no FEI proof or counterfamily.','Auxiliary core Lean attempt held by fresh memok exit1; no target or axioms verified.','Wake attachment verification degraded by write-lock timeouts; no affected note used as a proof premise.','New guard external review and supervisor archive/mirror/downstream adoption unobserved.'],
      'packet_ids':['A087']}
    save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
    report=f'''# A087 stage22 restriction audit

## exact target, quantifiers, hypotheses and units

A061-DEEP-SELECTED-DATA-RESET-SHARP-SQRT-BOUNDARY@1 HOLDS at its stated selected-policy scope, without repair. For every finite m>=2, 1<=r<=m and t>=1, all actual fair predictable query histories retain full current references, old debits and both terminal entropy and KL. Units bits. The exact activated capital is max(H(Z),2^-t K_r); ONE supplied original8I account after old debit<=I pays the declared policy for r<=floor(sqrt(m)). Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Protocol {protocol['revision']} was read in full. BOARD dated20261027 09:12Z, B18 lead v2 and own previous STATUS/LEARNED/PROOF were consumed. The lead's older specific audits were already finished in earlier stages; dispatch therefore consumes the useful new A061 dependency, which directly answers the prior selected-rule NEXT. Load-bearing source: A061 run20261027T044753Z, PROOF sections1--5 and8 and original CLAIMS@1. Its raw exact-statement hash and proof-byte hash match. A091's latest report was read as a possible review target; its NAND and liquidation claims are NOT accepted here. The nearer A061 dependency is chosen for this stage. out/SOURCES.json pins {len(sources)} source files, with source encodings; canonical navigation/registries/plan, supplement and four paper texts were refreshed through relevant locators in out/LOCATORS.json. Earlier accepted baseline is reused. No new paper theorem or priority assertion is a dependency.

## complete derivation or exact first unsupported line

PROOF sections1--7 independently derive local v_s=max(H_s,2^(r-s)M_r), zero outcome-KL on queried exact-reference factors, complete mixed-reference tensor transport, all-cut upper bound and matching endpoint lower bounds on IDENTICAL blocks, exact activated max potential, physical primeness and explicit H(Z)<=7I(Z) source price. The finite-cylinder conditioning keeps both outcomes at1/2 even under adaptive interleaving. No frozen installed block is queried, and no initial entropy floor is treated as free.

The new actual7-bit guard uses point4 times point3 and common r3. Reset the smaller factor before touching the other. The intermediate full bill H4+M3 exceeds BOTH root H4+H3 and completed expectation3M3/2 by more than1/5 bit. Therefore heterogeneous blocks require the sum of local maxima; taking only a maximum of root and completed totals can miss an adapted cut. This does not repair or refute the source's identical-block theorem.

First unpaid universal line: supply an ORIGINAL O(I) initial potential/reference or a necessary entropy-decaying compatible selected rule on arbitrary indecomposable Boolean cores, retaining actual query KL, old bills and both complete terminals. Replacing the explicit point-factor H price by arbitrary H<=CI would assume FEI itself.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes `python -X utf8 code/audit.py run`. PASS: {audit['assertions']} assertions, {audit['point_coordinate_cases']} physical coordinate cases (all coordinates of point_s, s1..7), {audit['bellman_start_cases']} two-block Bellman starts and {audit['bellman_states']} recursively visited states, four directly enumerated activated Boolean sources and {audit['compressed_triples']} frozen parameter triples m2..6,t1..8,r1..m. Measured runtime {audit['elapsed_seconds']:.3f}s. The first execution of this pilot also completed the frozen domain; no escalation. Integer Walsh and separate direct-character checks, physical-edge influences, Fraction full reference probabilities, and50-term rational atanh enclosures with geometric tails give exact equality and sign checks. Analytic equality boundaries use identical expressions, not a numerical tolerance.

ADVERSARY_SPEC.json precedes `python -X utf8 code/adversary.py`. PASS: {adversary['assertions']} further assertions in {adversary['elapsed_seconds']:.3f}s, all128 parent atoms and both64-atom physical children. The full reference includes frozen-factor atoms and complete KL. Certified strict intermediate gap>1/5. No source verifier was imported; only this stage's independently written arithmetic helper is shared between its two scripts. The proof, rather than finite samples, supplies the all-dimensional and all-cut theorem.

The preparation reader initially encountered a non-UTF8 legacy source text and stopped before freezing or computation; explicit cp1252 fallback with per-file encoding receipts fixed that source-reader issue. No failed run is counted as mathematical evidence. All research jobs estimate<=90MB and finish under60s; no GPU, heavy search, dimension escalation or detached job. Fresh memok refused the auxiliary Lean attempt (physical3.9GB<4.0GB; commit9.2GB available). code/MaxHalf.lean is a natural-number analogue of the max drift step, saved with a hash; no compiler started and no target/import/axiom certificate exists. Rung: analytic proof with exact validation, NOT Lean-checked.

## proof dependencies and changed downstream conclusions

Dependencies are finite Boolean character sums, Parseval, entropy concavity/chain rule/subadditivity, literal disjoint-factor product laws and elementary logarithm inequalities. The reviewed source statement and version remain unchanged. A087 contributes no repair to its independent acceptance. The new finite guard awaits independent review. The previous ALL-product-stop obstruction survives: r=m has quadratic price, while this selected deep rule permits square-root residual block size from one supplied influence account. No arbitrary-core source or new universal constant follows.

## one next mathematical action and independent reviewer

{progress['next_action']} This is the shortest unresolved bridge; another point dimension or extra history depth does not remove the explicit source-price hypothesis. A094 is the independent reviewer; A061/A064/A065 are consumers.

## actual persistence receipts or precise save blocker

The four protocol files, PROOF.md, frozen specs, code and outputs are saved only inside A087. STATUS has two lines and WORKLOG/LEARNED are updated. out/PERSISTENCE.json verifies exact protocol fields, source and local statement hashes, compatibility-copy equality, local byte hashes and the20MB file limit. Supervisor collection, shared-registry adoption, mirror verification and downstream use are NOT_OBSERVED. No git, mail, external message, shared research write, other-agent edit, trading access or process shedding. Wake reported attachment lock timeouts and stale personal context; this was disclosed and supplied no proof premise. Compute snapshot at start had3.1GB disk free and high CPU; no unrelated work was stopped. The later3.9GB figure is physical RAM availability from fresh memok, not a revised disk-space value.

## Universal bridge

C019 stopping-tree payment and C024 history transfer advance by independent acceptance of an exact selected physical DATA policy on the same full-support physically indecomposable activated family that defeats shallow resets. Both complete terminal terms and every old debit stay funded; a new7-bit strict cut guard prevents an invalid heterogeneous averaging extension. What remains is an arbitrary-core ORIGINAL O(I) source or useful compatible entropy-decaying continuation. NEXT targets that unpaid universal hypothesis, because the selected point-family policy and its all-cut bookkeeping are now independently checked and another isolated depth extension cannot provide the missing source.
'''
    (RUN/'REPORT.md').write_text(report,encoding='utf-8',newline='')
    own=RUN.parents[1]
    (own/'STATUS.md').write_text('STATE: Stage22 COMPLETE_LOCAL: A061 deep selected physical-data theorem independently HOLDS;9184+14 exact checks PASS; heterogeneous endpoint guard gap>1/5; Lean admission HELD; FEI OPEN.\nNEXT: A094 review cut guard; A061/A064/A065 fund ORIGINAL arbitrary-core O(I) source or necessary selected entropy-decaying rule, retaining old bills/query KL/BOTH full terminals.\n',encoding='utf-8',newline='')
    entries={
      'WORKLOG.md':f'\n## 2026-10-27 stage22 ({RUN.name})\nRead current board/lead and prior restriction frontier. Independently reconstructed A061 deep selected-data max potential, mixed references, activated exact capital and8I-oldI source price without repair. {audit["assertions"]} exact main assertions and {adversary["assertions"]} actual7-bit adversarial assertions PASS; endpoint-only heterogeneous extrapolation has gap>1/5. Legacy source decoding fixed before compute. Auxiliary Lean held by fresh memok exit1; nothing compiled. Full FEI and arbitrary-core original source remain open; next action and protocol artifacts saved.\n',
      'LEARNED.md':'\n## 2026-10-27: selected deep-data theorem independently accepted\n\n- A061 deep selected-data policy HOLDS unchanged: local max(H_s,2^(r-s)M_r) and finite fair-cylinder conditioning pay every cut; only exact-reference factors are queried and installed factors stay frozen, so actual query KL is zero. Activated exact capital is max(H(Z),delta*K_r); literal point-core price H(Z)<=7I(Z) pays original8I after old debit<=I for r<=sqrt(m).\n- The max of root entropy and completed expected reset cost is exact for identical blocks. It is not a heterogeneous sum rule: actual point4 times point3 at common r3 has intermediate H4+M3 exceeding both endpoints by>1/5 bit. Keep the sum of local maxima or solve the actual Snell/Bellman problem; do not move max through a sum.\n- The all-product-stop obstruction survives; r=m costs quadratic while selected r=O(sqrt(m)) costs O(I) when t=O(m). Arbitrary-core initial entropy/source funding remains unpaid. Q=P removes KL, not H. No generic mandatory selected policy or FEI proof follows.\n- All9184 main and14 adversarial checks use exact rational laws/outward log intervals. Source statement/proof hashes match. Formal natural max-step source is saved, but memok exit1 prevented compiler launch; NOT Lean-checked.\n'}
    for name,entry in entries.items():
        with (own/name).open('a',encoding='utf-8',newline='') as f:f.write(entry)
    pf=set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
    assert set(progress)==pf
    cf=set(protocol['required_per_run']['claim_fields'])
    for c in [claim,guard]:assert set(c)==cf
    assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
    for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in report
    assert len((own/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
    files=[]
    for p in sorted(RUN.rglob('*')):
        if p.is_file():
            assert p.stat().st_size<20*1024*1024
            files.append({'path':str(p.relative_to(RUN)),'sha256':sha(p),'bytes':p.stat().st_size})
    save('out/PERSISTENCE.json',{'status':'PASS','timestamp_utc':datetime.now(timezone.utc).isoformat(),'protocol_fields_exact':True,'claim_fields_exact':True,'source_statement_and_proof_hashes_match':True,'compatibility_bytes_equal':True,'rolling_status_lines':2,'files':files,'supervisor_archive_and_mirror':'NOT_OBSERVED'})
    print(json.dumps({'status':'COMPLETE_LOCAL','main_assertions':audit['assertions'],'adversarial_assertions':adversary['assertions'],'files':len(files),'full_FEI':'OPEN','independent_review':'A061 source HOLDS unchanged; new finite guard pending A094'},indent=2))

if __name__=='__main__':main()
