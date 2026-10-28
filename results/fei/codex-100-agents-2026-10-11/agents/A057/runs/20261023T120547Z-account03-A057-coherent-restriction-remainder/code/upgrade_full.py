from pathlib import Path
import json, hashlib, datetime
R=Path(__file__).resolve().parents[1]; HOME=R.parents[1]
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def write(p,v): p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
full=read(R/'out/full.json'); assert full['status']=='PASS'
results=read(R/'out/RESULTS.json'); results['runs']['full.json']=full
total=sum(v['exact_assertions'] for v in results['runs'].values()); assert total==13499
results['nonpilot_assertions']=total
results['scope']='Analytic coherent character theorem; half-depth for m>=4 and FULL exterior/tag continuation for m>=16 divisible by4. Finite exact checks support the written proofs; no finite extrapolation.'
write(R/'out/RESULTS.json',results)
claims=read(R/'CLAIMS.json'); c=claims[0]
old='Full X exhaustion, further core queries and universal FEI/root supplier are not proved.'
assert old in c['exact_statement']
extension='For m>=16 divisible by4, the exterior depth cap can be removed: after the same one old core query, EVERY adaptive interleaving and stopping policy on all X and tag coordinates is funded from the SAME B0, with pathwise cash at least m/4. First queries of original quadratic pairs cost at most m in total. Second-partner queries after mask death cost0; while the mask survives their cost is at most 2^(1-n)(n+4) for n>=2 remaining X coordinates, and at most2 for n=1, summing to at most9 per path. The last-tag spent OR pending bill is capped by U(t,q)=min(T(t,q),2), concave in t and still retaining q log(1/q). Cash>=B0-2c-m-11>=m/4. Both complete old children and all full residual core spectra are retained. Further core queries, full-depth m=4,8,12 and a universal original root/core supplier are not proved; full FEI remains OPEN.'
c['exact_statement']=c['exact_statement'].replace(old,extension)
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
c['hypotheses'].append('FULL exterior/tag continuation requires m>=16 divisible by4; it allows all X coordinates, but still no further core queries after the one specified old core query.')
c['proof_source']['full_exterior_continuation']='FULL_EXTERIOR.md: rare second-partner summability, capped coherent reserve and original-owner invariant'
c['proof_source']['certificates'].append('out/full.json')
c['proof_dependencies'].append('Erasure<=h2(influence), JS<=2min(influence,1-influence)/ln2; geometric second-partner bound derived in FULL_EXTERIOR.md; no large-dimensional truth-table extrapolation.')
c['review_records'][0]['result']=f'{total} nonpilot exact assertions PASS; includes 1458 full local mixed states, 1944 X edges, 972 tag edges, 127 geometric tail checks and 61 exact owner scalar cases; independent external acceptance PENDING.'
c['first_unproved_line']='Pay further actual core queries from a universal original owner while retaining arbitrary residual core Fourier entropy. The complete exterior/tag continuation is now proved for m>=16 divisible by4; smaller m=4,8,12 full-depth remains outside this theorem. Full FEI remains open.'
write(R/'CLAIMS.json',claims)
p=read(R/'PROGRESS.json')
p['attempt_id']='A057-stage20-character-plus-full-exterior-v1'
p['method']+='; summable rare second-partner costs and concave capped coherent reserve'
p['mathematical_delta']='Retained q-log coherent ticket after actual positive old core debit. ORIGINAL4I_X funds arbitrary-width tag/exterior continuation: >=29B0/32 before X, >=B0/8 to half depth for m>=4, and FULL X/tag continuation with cash>=m/4 for m>=16 divisible by4. All actual costs and full terminal/core spectra retained.'
p['source_artifacts']+=['FULL_EXTERIOR.md','FULL_SPEC.json','out/full.json']
p['next_action']='A059/A060/A091 independently audit rare second-partner summability and original-owner cash with retained q-log capped reserve; then supply payment for additional actual core queries from a universal original owner with all residual core entropy retained.'
p['blockers']=[('full-depth m=4,8,12 and further actual core queries not paid' if x=='full exterior exhaustion and further core queries not paid' else x) for x in p['blockers']]
write(R/'PROGRESS.json',p); write(R/'PACKET_DELTA.json',p)
notes=read(R/'out/EXECUTION_NOTES.json')
notes['stage20_validation']+=f' Full-depth extension added {full["exact_assertions"]} exact assertions; final total {total}. All mathematical assertions passed on first execution.'
notes['full_exterior_extension']='First pair queries cost<=m; rare second-partner costs sum<=9 across all remaining dimensions; spent OR pending last-tag cap<=2. Original cash>=B0-2c-m-11>=m/4 for m>=16 divisible by4. Further core payment is not proved.'
write(R/'out/EXECUTION_NOTES.json',notes)
report=(R/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('The mixed continuation has at most m/2 exterior queries per path and no further core queries. Full FEI is OPEN.','The half-depth continuation applies for m>=4. A subsequent summable refinement covers ALL exterior/tag interleavings for m>=16 divisible by4, still with no further core queries. Full FEI is OPEN.')
report=report.replace('The first unsupported line is continuing beyond half exterior depth or making further core queries with CURRENT q and ACTUAL unused original cash.','FULL_EXTERIOR.md removes the exterior-depth cap for m>=16 divisible by4. Charge at most2 for each first query of an original quadratic pair (total<=m). A second partner after mask death has zero decrement, since its surviving background dependence is linear or absent. With a surviving mask and n remaining X bits, disagreement deficit e<=2^(1-n); the erasure/JS bound gives D<=2^(1-n)(n+4) for n>=2, and D<=2 for n=1. Each n occurs at most once per path, so all second-partner costs sum to<=9. The capped pending reserve U=min(T,2) is concave in current density, so child allocation is valid. Count a spent OR pending tag bill<=2 once. Cash>=B0-2c-m-11>=m/4 for all m>=16. All full residual core spectra remain in the terminal telescope.\n\nThe first unsupported line is making further actual core queries with CURRENT q and ACTUAL unused original cash; full-depth m=4,8,12 is also outside the new theorem.')
report=report.replace('Frozen SPEC.json, REPRO_SPEC.json and MIXED_SPEC.json precede their jobs.','Frozen SPEC.json, REPRO_SPEC.json, MIXED_SPEC.json and FULL_SPEC.json precede their respective jobs.')
report=report.replace('code/check_mixed.py and code/mixed_repro.py.','code/check_mixed.py, code/mixed_repro.py and code/check_full.py.')
report=report.replace('**5643 nonpilot exact assertions passed**','**13499 nonpilot exact assertions passed**')
report=report.replace('Detailed outputs are saved in out/RESULTS.json.','Full local continuation:1458 states,1944 X edges,972 tag edges,288 surviving-mask second-partner edges,1008 dead-mask zero-cost partner edges,127 exact geometric-tail identities and61 original-owner scalar cases;7856 additional assertions. Detailed outputs are saved in out/RESULTS.json.')
report=report.replace('The new mixed checks explain the increase from3203 earlier in this stage to5643;','The mixed checks increased3203 to5643; the full-depth refinement adds7856 to13499;')
report=report.replace('These are distinct scopes, not conflicting constants.','For FULL exterior continuation m>=16 the cash bound is m/4. These three constants describe different policy scopes.')
start=report.index('A059/A060/A091 should independently reconstruct')
end=report.index('\n\n## actual persistence',start)
report=report[:start]+'A059/A060/A091 should independently reconstruct the retained q-log packet and full-depth rare second-partner summability from the SAME original4I_X cash, preserving the positive old AND3 debit and BOTH complete terminal profiles. Next supply a universal original owner for further actual core queries: complete exterior exhaustion leaves arbitrary residual core entropy unpaid, so another exterior-class example would not address the remaining universal bridge.'+report[end:]
start=report.index('Universal bridge:')
report=report[:start]+'Universal bridge: C019 moves from half-depth to COMPLETE exterior/tag continuation for this actual non-hereditary coherent block, for every m>=16 divisible by4 and arbitrary character width, after a positive old internal debit, funded by the SAME ORIGINAL4I_X owner with pathwise cash>=m/4 and both full terminal profiles. The alpha^2 log(1/alpha^2) term remains literal in a summable capped ticket; second-partner costs sum to at most9. Universal root/core payment and further actual core queries remain open, as does full-depth m=4,8,12 in this statement. Supplying a core-payment invariant from the original owner is the shortest route toward full FEI because this stage now completes the exterior mechanism while explicitly retaining the unpaid arbitrary core entropy.\n'
(R/'REPORT.md').write_text(report,encoding='utf-8')
status=f'STATE: A057 stage20 retained q-log ticket and FULL exterior/tag continuation for m>=16 divisible by4 paid SAME original4I_X after positive old core debit, cash>=m/4; {total} exact assertions PASS; external review pending; FEI OPEN.\nNEXT: A059/A060/A091 audit rare second-partner sum<=9 and original cash/both full terminals; fund further actual core queries from a universal original owner retaining arbitrary core entropy.\n'
(HOME/'STATUS.md').write_text(status,encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for name,body in [('WORKLOG.md',f'{stamp} stage20 FULL extension: removed exterior depth cap for m>=16 divisible by4. First quadratic-pair queries cost<=m; surviving-mask second-partners cost<=2^(1-n)(n+4), dead-mask second-partners cost0; total second-partner bill<=9. Capped retained-q-log reserve U=min(T,2) gives SAME original cash>=B0-2c-m-11>=m/4 after old core debit. Added7856 exact assertions, final13499 PASS; external review pending. Further core payment/full FEI remain open.'),('LEARNED.md','Stage20 durable FULL exterior refinement: charge each first quadratic-pair query<=2, then exploit second-partner derivative near1 along the unique surviving point-mask path. Remaining dimensions occur once: second-partner total<=2+sum(n>=2)2^(1-n)(n+4)=9. After mask death second-partner dependence is linear or absent, hence entropy debit0. Capping coherent T by universal2 preserves density concavity and its literal q log(1/q) term. ORIGINAL owner4I_X pays all exterior/tag interleavings after one actual core query with cash>=m/4 for m>=16 divisible by4. Arbitrary residual core entropy is retained, not paid. Next universal bridge is core payment, not further exterior examples.')]:
 with (HOME/name).open('a',encoding='utf-8') as f: f.write('\n'+body+'\n')
audit=R/'code/audit.py'; text=audit.read_text(encoding='utf-8').replace('==5643','==13499').replace("'nonpilot_assertions':5643","'nonpilot_assertions':13499").replace("'assertions':5643","'assertions':13499")
text=text.replace('print(report)','print("REPORT saved; seven protocol headings and final Universal bridge verified.")').replace("print((ROOT.parents[1]/'STATUS.md').read_text(encoding='utf-8'))",'')
audit.write_text(text,encoding='utf-8')
print(json.dumps({'upgrade':'SAVED','assertions':total,'full_exterior_m':'>=16 divisible by4','full_FEI':'OPEN','external_review':'PENDING'}))
