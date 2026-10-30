from pathlib import Path
from datetime import datetime,timezone
import copy,json,hashlib
ROOT=Path(__file__).resolve().parents[1];AGENT_DIR=ROOT.parents[1];AGENTS=AGENT_DIR.parent
CANON=Path(r'~\mop_fei100\reports\fei-2026-10-11')
RUNID=ROOT.name
protocol=json.loads((CANON/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
required=protocol['required_per_run']
cert=json.loads((ROOT/'LOG_SIGN_CERTIFICATE.json').read_text());alt=json.loads((ROOT/'out/alternate_check.json').read_text())
assert cert['failures']==alt['failures']==0
now=datetime.now(timezone.utc).isoformat()
a071=AGENTS/'A071/runs/20261011T214639Z-fleet05-A071-search-space-design'
a072=AGENTS/'A072/runs/20261011T220909Z-fleet05-A072-exact-walsh-engine'
a096=AGENTS/'A096/runs/20261011T215017Z-fleet05-A096-live-gap-ledger'

def write(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(raw):return hashlib.sha256(raw).hexdigest()

claims=json.loads((a071/'CLAIMS.json').read_text())
assert len(claims)==1
claim=claims[0]
# Preserve existing version and statement hash; add only a limited review record.
claim['proof_source']=[str(a071/x) for x in claim['proof_source']]
claim['review_records'].append({'reviewer':'fleet05/A073','at':now,
  'verdict':'SELECTED_RECORDS_CONFIRMED_ONLY_FULL_GRID_REVIEW_PENDING',
  'scope':'Code4 p=(1/8,1/8,1/2) A={2} strict positive; code15 at same p,A exact zero; does not accept all 20736 cases, symmetries, or minimum assertion',
  'source':str(ROOT/'REPORT.md'),
  'method':'Integer-product sign comparison, one eight-term rational interval, direct centered moment and unfactored-product reconstruction'})
registry=json.loads((CANON/'CLAIM_REGISTRY.json').read_text())
old=next(c for c in registry['claims'] if c['claim_id']=='B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED')
old=copy.deepcopy(old)
old={k:old[k] for k in required['claim_fields']}
old['review_records'].append({'reviewer':'fleet05/A073','at':now,
  'verdict':'FIXED_COUNTEREXAMPLE_RECONFIRMED_BY_ALTERNATE_PRODUCT_REPRESENTATION',
  'scope':'Specified two-bit witness and J-M>1195/10000 only',
  'source':str(ROOT/'REPORT.md')})
claims.append(old)
for c in claims:
    assert set(c)==set(required['claim_fields']),(c['claim_id'],set(c)^set(required['claim_fields']))
    data=json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()
    assert sha(data)==c['statement_sha256']
write(ROOT/'CLAIMS.json',claims)

progress={
 'protocol_revision':protocol['revision'],'run_id':RUNID,'stream':'B15','packet_id':'A073',
 'gap_id':'G-BIASED-TAX','attempt_id':'A073-CERTIFIED-LOGS-1',
 'method':'Exact integer-product comparison from rational entropy laws; separate N=8 outward interval; selected-record verification',
 'mathematical_delta':'Three selected Boolean comparison signs certified: D>5/2048 and 0.00256646<D<0.00256649; D=0; AND J-M>1195/10000. Generic exact-product equivalence documented. No new broad candidate or full-grid acceptance.',
 'deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'SELECTED_SIGNS_RESOLVED_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A071-B09-THREEBIT-GRID-CERTIFICATE','version':1,'acceptance':'Selected records only; full grid pending'},
 {'claim_id':'A072-EXACT-GRID-ALGEBRA','version':1,'acceptance':'Selected algebra independently rechecked; full engine review pending'},
 {'claim_id':'B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED','version':1,'acceptance':'Existing certified witness reproduced'}],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'Added scope-limited local review record; original theorem status unchanged'} for c in claims],
 'source_artifacts':['REPORT.md','CLAIMS.json','LOG_SIGN_CERTIFICATE.json','CERTIFIED_COMPARISON.md','FROZEN_SPEC.json','code/certified_logs.py','code/certify.py','code/check_products.py','out/alternate_check.json','out/source_receipts.json'],
 'next_consumers':['A074','A085','A092','A050','A057','A082','B09','B20'],
 'next_action':'Consume a source-versioned nonreusing singleton-tax transport inequality from A050/A057; certify its residual on exact Boolean records while retaining M and terminal entropy, rather than rerun the grid.',
 'stagnant_substantive_attempts':0,'blockers':['Full-grid independent review and supervisor mirror adoption pending; B15 lead notes absent but not blocking selected certification'],
 'packet_ids':['A073']}
fields=set(required['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(progress)==fields
write(ROOT/'PROGRESS.json',progress);write(ROOT/'PACKET_DELTA.json',progress)

extra=[a071/x for x in ['REPORT.md','CLAIMS.json','SEARCH_DOMAIN.json','code/search.py','out/zero_certificates.json']]
extra += [a072/x for x in ['REPORT.md','CLAIMS.json','EXACT_WALSH_INTERFACE.py','out/witnesses.json']]
extra += [a096/x for x in ['REPORT.md','CLAIMS.json']]
extra += [CANON/'verification/B09_interval_repair_20261011/REPORT.md',AGENTS.parent/'BOARD.md']
receipts=json.loads((ROOT/'out/source_receipts.json').read_text())
for p in extra:
    raw=p.read_bytes();receipts.append({'path':str(p),'bytes':len(raw),'sha256':sha(raw),'scope':'Read selected report/source/data relevant to exact selected comparisons; A096 tax noted but not used as proof dependency'})
write(ROOT/'out/source_receipts.json',receipts)

report=f'''# A073: certified logarithms on exact physical-block records

## exact target, quantifiers, hypotheses and units

Complete A073's LOG_SIGN_CERTIFICATE.json and CERTIFIED_COMPARISON.md obligations. Verify precisely three existing Boolean records, without repeating the 20736-case baseline or opening a third broad B15 candidate. For each, the sign is defined from the actual physical-child/spectral experiment in normalized product basis; units are bits. Record1: f=(1,1,1,-1,1,1,1,1), p=(1/8,1/8,1/2), A={{2}}, D=M-J. Record2: f=(1,-1,-1,-1,-1,1,1,1), same p,A, D=M-J. Record3: AND f=(1,1,1,-1), p=(1/8,1/4), A={{0}}, R=J-M. Truth tables use little-endian physical assignments. For records1-2, selected p=1/2 means Delta_A=0. No minimum-over-grid or continuum quantifier is claimed here.

## sources actually read, revisions and theorem locators

Protocol read in full: {protocol['revision']}. Campaign README, CURRENT_STATUS, claims/obstructions, PACKET_STATUS A073, STREAM_NEXT_ACTIONS, and LaTeX B15 A073 acceptance contract consulted. BOARD.md at stage start was the supervisor's 2026-10-11 22:26 UTC snapshot; Claude B15 STREAM_NOTES.md absent. Existing B05/B09/B19 report bytes ingested; B09 sections2-4 and the independent interval repair's Defect/Counterexample sections read for the exact identity and signed-division hazard. Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING read; sources BLOCK_RESTRICTION_IDENTITY and LOG_ALLOCATION consulted for physical versus spectral bookkeeping. All source-byte receipts are in out/source_receipts.json; a receipt is not a full scholarly proof audit.

A071 REPORT's minimum-positive record and equality code15, CLAIMS@1, SEARCH_DOMAIN and zero certificates supply selected inputs. A072 EXACT_WALSH_INTERFACE@1 and REPORT/witness records supply the algebraic API and phases; source hash {cert['engine_sha256']}. A096 REPORT equations5-9 and its uniform-singleton-tax claim were consulted as the next live dependency; no sqrt tax is assumed in the present proof. Context papers consulted through their introductions, product-bias normalization, threshold Proposition7.1/8.1, and percolation Theorem1.1; both earlier versions distinguished by hashes. These class results are context, not premises. Complete byte ingestion with scoped locator reading is recorded, not independent reconstruction of all manuscript theorems.

## complete derivation or exact first unsupported line

CERTIFIED_COMPARISON.md gives the full elementary proof of R=(1/L)log2(U/V), the prime-cancellation equality test, signed interval rules, and atanh remainder. The physical mixture q=sum_z w_z mu_z is verified exactly, so D=H(mu)-2H(q)+E H(mu_z). Direct weighted centered moments independently reproduce selected masses, while unfactored rational entropy products reproduce the factored ratios exactly.

Record1 has mu=(3969,7,7,49,1,7,7,49)/4096, q=(1985,7,7,49)/2048, and equally weighted children (961,7,7,49)/1024 and (1,0,0,0). With U=1985^3970, V=2^10240*3^7938*7^3969*31^1922, we verify 2^5 V<U<2^6 V. Hence 5/2048<D<3/1024. The separate initial eight-term interval gives the rigorously outward decimal bounds 0.00256646<D<0.00256649.

Record2 has every aggregated prime coefficient zero, so D=0 exactly and no logarithm approximation is used. Record3 has 128 R=log2[(2^224*3^225*5^225*7^14)/(29^232)]. Its integer bracket is 15/128<R<1/8; its N=8 rational enclosure gives 0.11954501<R<0.11954502, so R>1195/10000. Existing tax-free biased uncertainty is refuted at its original scope; FEI is not refuted.

There is no unsupported line in these three exact sign comparisons. The first unsupported extrapolation would be to accept A071's full symmetry-covered grid, its asserted global minimum, any all-real-bias statement, or a universal influence payment from these records. None is made. Initial sanity assertion failure was a hand-expanded expected coefficient error: two of four mass-7 parent entries were omitted. The exact algorithm's coefficients and masses were unchanged; the expected list was corrected and the successful checks rerun. No source claim was repaired or silently altered.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json saved before computation: three cases, no symmetry, <=40 MB estimated memory, max55 seconds, fixed dimensions n=2,3. All mathematics uses integer/Fraction arithmetic, including exact outward rounding. Product bytes and hashes are saved per record, with numerator/denominator bit lengths only43492/43486 for record1. Runtime measurements and displayed approximate floats do not participate in a sign test.

Executed from A073:

    python -X utf8 runs/{RUNID}/code/certify.py
    python -X utf8 runs/{RUNID}/code/check_products.py

Final certificate run: three signs (+,0,+), no unresolved cases, runtime {cert['runtime_seconds']:.6f}s. It also checks powers2^k for -12<=k<=12 and a negative non-power-of-two logarithm. Separate direct moment/unfactored-product check: three exact matches, zero failures, runtime {alt['runtime_seconds']:.6f}s. Both were bounded pilots; no heavy job, GPU or dimension escalation. Product sign was established first; a single fixed N=8 interval check corroborated positive records. Precision refinements: zero. A subsequent output-only correction collapsed the exact-zero dyadic bounds to [0,0] and added rational outward decimal fields; it did not increase precision.

## proof dependencies and changed downstream conclusions

Only finite Boolean inputs and elementary Parseval/orthogonality, log monotonicity, unique factorization and the proved series tail are used. A072 is reused for the main algebra; its selected outputs are rechecked directly without its code in the second checker. Thus no unreviewed universal B09 theorem, FEI lemma or A096 upper bound is assumed. CLAIMS.json preserves A071@1's statement and pending full-grid status while adding a scope-limited selected-record review; it preserves the canonical repaired AND@1 statement and adds corroboration. No new broad candidate is added, respecting B15's two pending candidates. A074 can consume exact product bytes and rational margins; A085/A092 must still audit full grid coverage and their required scope.

## one next mathematical action and independent reviewer

Consume one source-versioned nonreusing singleton-tax transport inequality from A050/A057 and certify its actual Boolean residual with this interface, keeping conditional M and terminal entropy. A085/A092 independently review the three sign certificates and equivalence proof; A074 may reconstruct the selected inputs from a different representation. The second checker here is a second implementation by A073, not an independent agent acceptance. A071 is a distinct original author, so our selected-record review is independent of A071's original log calculation, but does not accept its full claim.

## actual persistence receipts or precise save blocker

Saved locally under the assigned A073 run: protocol REPORT, CLAIMS, PROGRESS, identical PACKET_DELTA, frozen spec, LOG_SIGN_CERTIFICATE, CERTIFIED_COMPARISON, code and exact outputs. out/manifest.json records hashes and sizes; finalization checks exact field sets, unchanged statement hashes, delta equality and every file below20 MB. STATUS is two lines, WORKLOG appended and LEARNED updated. No shared trees, other agent folders or brain were written. GitHub copy, mirror verification and supervisor adoption are pending; no external durability or full independent acceptance is claimed.

**Universal bridge:** This stage supports C019 stopping-tree payment by replacing floating sign uncertainty on three actual physical restriction ledgers with exact products and a reusable rational entropy interface. Its quantified movement is D>5/2048 for the selected surviving helper record, D=0 for a selected equality, and the retained necessary biased correction J-M>1195/10000. It moves no universal FEI constant. The remaining obligation is to pay conditional M plus a valid singleton tax and terminal entropy using nonreused physical influence. Certifying a source-versioned transport candidate on already verified Boolean records is the shortest next step toward that universal bridge; another baseline census or extra precision would not address the unpaid implication.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
for field in required['report_fields']:assert f'## {field}' in report
(AGENT_DIR/'STATUS.md').write_text('STATE: A073 packet complete locally: three exact log signs (+,0,+), minimum record D>5/2048, AND J-M>1195/10000; selected reviews only; full FEI OPEN.\nNEXT: A085/A092 review product certificates; consume A050/A057 nonreusing singleton-tax transport candidate with conditional M and terminal entropy retained.\n',encoding='utf-8')
with (AGENT_DIR/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} — Read protocol/board/dependencies; B15 notes absent. Certified three selected signs by integer products and N=8 rational intervals, no refinement. Fixed a hand-expanded expected-coefficient sanity assertion (algorithm unchanged); final check {cert["runtime_seconds"]:.6f}s, alternate check {alt["runtime_seconds"]:.6f}s. Saved protocol files and limited review records; no full-grid acceptance or new broad candidate.\n')
with (AGENT_DIR/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nRational entropy linear forms have exact sign via prime-factor aggregation, clearing denominators and U versus V; zeros require no precision. For A071 code4 p=(1/8,1/8,1/2), A={2}: 2048D=log2[1985^3970/(2^10240 3^7938 7^3969 31^1922)], D>5/2048, 0.00256646<D<0.00256649. Count all four 7/4096 masses before expansion. Code15 at same biases/block is exact zero. AND p=(1/8,1/4), A={0}: 128(J-M)=log2[(2^224 3^225 5^225 7^14)/29^232], 0.11954501<J-M<0.11954502. Range reduction log2(x)=k+ln(t)/ln2 divides only a nonnegative numerator and avoids historical signed-division failure. Full grid coverage, continuum tax, and nonreusing C019 payment are separate obligations.\n')
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
manifest=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='manifest.json':
        raw=p.read_bytes();assert len(raw)<20_000_000
        manifest.append({'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':sha(raw)})
write(ROOT/'out/manifest.json',{'saved_at':now,'files':manifest,'schema_checks':'PASS','external_mirror':'PENDING'})
print(json.dumps({'protocol_fields':'PASS','unchanged_statement_hashes':'PASS','claims':'Two existing versions with limited local review records; zero new broad candidates','saved_files':len(manifest),'max_bytes':max(x['bytes'] for x in manifest),'run':str(ROOT)},indent=2))
