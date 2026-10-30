from pathlib import Path
import json,hashlib,datetime
def main():
 R=Path(__file__).resolve().parents[1];A=R.parents[1]
 def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
 v=json.loads((R/'out/validation.json').read_text(encoding='utf-8'));c=json.loads((R/'out/core_validation.json').read_text(encoding='utf-8'))
 assert v['status']==c['status']=='PASS' and c['positive_additional_core_nodes']>0 and c['positive_posttag_core_nodes']>0
 assert c['nodes']==2298 and c['frontiers']==51
 total=v['assertions']+c['assertions']
 claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'));cl=claims[0]
 write(R/'out/CLAIM_V1.json',cl)
 cl['version']=2;cl['supersedes']=['A059-EXACT-EXCESS-ESCROW-AND-CORE-OWNER-OBSTRUCTION@1']
 extension=(' Moreover the SAME original owner also pays ANY adaptive interleaving of at most m/4 ADDITIONAL physical core queries per path, with ALL exterior/tag queries and arbitrary stopping: h2(c)<=11/32 gives initial unused L0>=3m/4-15/32; at each core query debit the ACTUAL inherited-core fee a=t D_iH(G)<=2t from CURRENT L and update BOTH actual core restrictions and their mean profiles. The full actual decrement is a plus the scalar-profile expected drop, so no debit is counted twice. Current L>=m/8 and B=L+E>=m/8 in EVERY terminal. Arbitrarily longer core histories are permitted by predictable admission L-2t>=m/8, paying actual fees without replenishment. The exterior-only obstruction excludes UNBOUNDED arbitrary core continuation, not these admitted additional queries.')
 cl['exact_statement']=cl['exact_statement'].replace('freeze the actual restricted core.','first consider the actual restricted core frozen, followed by the admitted extension below.')+extension
 cl['statement_sha256']=hashlib.sha256(cl['exact_statement'].encode()).hexdigest()
 cl['hypotheses']=[s.replace('then frozen core','then base frozen-core continuation, extended below to admitted core queries') for s in cl['hypotheses']]
 cl['hypotheses'].append('Extended policy permits at most m/4 ADDITIONAL core queries per actual path, or arbitrary further core depth while CURRENT L-2t>=m/8; no fresh cash.')
 cl['proof_source']['extended_core']='PROOF.md Section2a; CORE_SPEC.json; code/core.py; out/core_validation.json'
 cl['review_records'][0]['result']=f'{total} exact assertions PASS across main and additional-core audits; positive actual core queries AFTER last tag included; arbitrary m/history scope by written local-edge induction'
 cl['first_unproved_line']='Fund a necessary further core query AFTER the ACTUAL admitted core-cost budget is exhausted, from ORIGINAL core influence or Booleanity-based refunds, retaining old costs/current profiles/BOTH full terminals. Exterior-only unlimited continuation is refuted.'
 write(R/'CLAIMS.json',claims)
 p=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
 nxt='After an ACTUALLY exhausted admitted core-cost budget, fund a necessary further core query from ORIGINAL core influence or a Booleanity refund; keep CURRENT mean profiles, old debits and BOTH full terminals. A057/A060 construct; A091/A087 audit innovations and actual core fees. One extra query is already paid; no exterior-only unlimited retry.'
 p['attempt_id']='stage20-exact-excess-escrow-admitted-core-continuation'
 p['mathematical_delta']+=' Stronger v2: SAME original exterior account pays m/4 ADDITIONAL arbitrary core queries interleaved anywhere, retaining>=m/8; longer depths allowed by actual discounted-cost admission. This closes the ONE-further-core target without a new owner.'
 p['claims_created_or_changed'][0]=cl['claim_id']+'@2';p['next_action']=nxt
 p['source_artifacts']+=['CORE_SPEC.json','code/core.py','out/core_validation.json']
 p['blockers'][1]='Universal core supplier AFTER actual admitted budget exhaustion remains unpaid; unbounded exterior-only core payment is refuted.'
 write(R/'PROGRESS.json',p);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
 report=f'''# A059 stage20: original escrow pays further core queries

## exact target, quantifiers, hypotheses and units

Pay EVERY finite adaptive exterior/tag continuation and admitted FURTHER core queries after an actual positive old core debit, using SAME ORIGINAL exterior4I_X and BOTH complete terminal functions. Uniform finite Boolean cubes, bits entropy; m>=4 divisible4, paired bent background, all-one point C of densityc, arbitrary independent core G and nonempty fresh character. The new v2 allows m/4 ADDITIONAL core queries per path, or arbitrary longer core depth under CURRENT cost admission. It is an EXPECTED-resource allocation with explicit child innovations; full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD (including updated A057/A059/A060/A091 states), B12 STREAM_NOTESv2, own STATUS and stage19 proof; full execution protocol2026-10-11-execution-v2; A057 stage20 REPORT/PROOF Sections1-4/FULL_EXTERIOR Sections1-4/CLAIMS. Source hashes in out/SOURCES. Earlier campaign/paper intake is prior-stage context. A057 already completed m>=16 exterior/tag continuation; this stage independently reconstructs it, closes small m at explicitly different expected-resource scope, and ACTUALLY pays further core queries. Owner deadline23Oct14:49UTC governs; no schedules changed.

## complete derivation or exact first unsupported line

PROOF(1)-(3): the actual core-frequency marginal is(1-t)delta_empty+t p_G, since physical KC=0. Shannon mixture bounds and conditional exterior entropy give0<=E=H(F)-tH(G)<=m+h2(t). Expanding physical empty/nonempty core frequencies expresses E using ONLY the exterior spectrum and CURRENT core mean; the full coherent q-log profile is retained. This identity does not grant an initial H(G) cash bank.

After booking the ACTUAL old debit d_old=cD_iH(G)<=2c once, nonempty tags make E_start identical in BOTH core children. ORIGINAL owner B0=2m-4mc buys E_start and unused L0=B0-d_old-E_start. At exterior/tag queries inherited tH(G) is harmonic, so full actual entropy decrement equals the expected E drop. Assign each actual child L+its CURRENT E; innovations have conditional mean0. Every full terminal entropy and old debit remains.

Section2a is the final payment scope: h2(c)<=cm+c/ln2<=11/32 yields L0>=3m/4-15/32. At a FURTHER core query debit a=tD_iH(G)<=2t from this SAME CURRENT L and update BOTH actual G restrictions and mean profiles. The FULL physical decrement is EXACTLY a+E_parent-average E_child, so total B=L+E pays it once. Up to m/4 additional core queries cost<=m/2 and leave L>=m/4-15/32>=m/8. They may occur anywhere, even AFTER final-tag collapse, with all exterior queries and arbitrary stopping. Longer core histories are admitted while L-2t>=m/8; each uses its ACTUAL fee rather than the worst-case bound, and the reserve is never replenished. Thus the requested one-further-core transfer is closed without a new owner. Formula/core dimension has no fixed bound.

Section3 gives the necessary boundary: G_N is a product of N actual AND2 signs, H=2N,I=N. Exhausting its core with tags/exterior untouched costs EXACTLY2cN, beginning with positive old debit2c and retaining all full terminal functions. At N=m2^m-2m+1 this exceeds the WHOLE original exterior owner by2c. UNBOUNDED arbitrary core continuation from that owner alone is false; this does not prohibit the newly paid m/4 queries. First unpaid line: a necessary further core query AFTER its actual discounted-cost budget is exhausted, paid by an original core owner or a genuine Booleanity-based refund.

For an explicit growing-depth positive family, nested fresh m4 coherent wrappers satisfy H_d=cH_(d-1)+E_d, E_d<=5<=4I_ext=7, and I_d=cI_(d-1)+I_ext+c|J_d|. Induction gives H_d<=4I_d at every depth. This is an explicit factorization consequence, not a new general closure theorem.

## executed validation with domain, arithmetic, commands and outputs

SPEC and CORE_SPEC were saved BEFORE their respective runs. Commands: python -X utf8 code/check.py --pilot; code/check.py; code/core.py --pilot; code/core.py; code/finalize.py. First pilot1376 assertions PASS; core pilot2066 assertions PASS. Main exact-profile audit:1296 generic two-bit K/C/core roots;16 DIRECT character-sum reproductions;6 complete mixed trees,1146 nodes,45 full stopping frontiers,6 positive old debits,65 nonzero child innovations; root escrows m4/8/12/16;16 implicit product obstruction certificates m4..64. Main {v['assertions']} assertions PASS in{v['seconds']:.3f}s, including exact current last-tag packets and retained q-log bounds.

ADDITIONAL-core audit:{c['trees']} complete mixed trees,{c['nodes']} nodes,{c['frontiers']} full frontiers,{c['positive_additional_core_nodes']} POSITIVE actual additional-core nodes, of which{c['positive_posttag_core_nodes']} occur AFTER the final tag;{c['nonzero_child_innovations']} nonzero child budget innovations. It independently uses full physical spectra to verify exact total cash drop, original exterior owner, core fee<=2t, CURRENT L>=m/8 and SAME original full stopped equality in BOTH complete terminals. {c['assertions']} assertions PASS in{c['seconds']:.3f}s. Combined nonpilot total **{total} exact assertions PASS**. All-policy/all-dimensional conclusions are proved by the written local-edge induction and exact Fourier products, not finite extrapolation.

Fraction Walsh and exact prime-log arithmetic use rigorous32-term atanh log enclosures with geometric tails. Floating runtime never decides a mathematical sign. Estimated memory160MB main/100MB core, no measured peak claimed. No task expected above300MB, heavy search, GPU, compiler, window or detached worker. An initial helper copy failed before code/ existed, then the identical pinned helper was copied successfully. No mathematical assertion failure was hidden. The v1 draft only paid frozen-core histories; a mistaken NEXT inferred need for a new owner after ONE query from an UNBOUNDED-core obstruction. Tightening the original margin produced v2 and the separately frozen additional-core audit before final save.

## proof dependencies and changed downstream conclusions

New claim is A059-EXACT-EXCESS-ESCROW-AND-CORE-OWNER-OBSTRUCTION@2; v1 is preserved in out/CLAIM_V1. A057 unchanged coherent interface and FULL_EXTERIOR m>=16 pathwise cash/summability scope independently ACCEPTED without source repair. Its narrower29/32 and half-depth1/8 constants are not newly accepted here. New expected-resource v2 pays additional core queries; it does not silently assert A057's literal pathwise equal-debit cash at small m. Earlier designated-pair/length-admission obstructions remain valid, and the new arbitrary-core exterior-only obstruction concerns UNBOUNDED continuation. Universal initial core entropy/influence supplier remains unpaid; FEI OPEN.

## one next mathematical action and independent reviewer

{nxt} A universal source price must use Boolean structure; another exterior-class estimate cannot pay the exact unbounded core product bill.

## actual persistence receipts or precise save blocker

Four protocol files, full v2 proof, independent scoped review, both frozen specs, exact scripts/outputs and source pins saved in A059. code/finalize.py automatically applies code/extend.py after the core output exists, so regeneration preserves the final v2 scope. Exact schemas, statement hashes, identical progress copies, helper pin and all sizes<20MB checked; out/PERSISTENCE records final local readback hashes. STATUS exactly two lines; rolling WORKLOG/LEARNED appended. Supervisor mirror/registry use NOT_VERIFIED; no Git/messages or research write outside A059. Shared campaign/math-brain sources remain read-only.

Brain self-care degraded/unverified: personal model99.5h, state84.1h and dream34.8h stale at fresh wake; earlier runtime handoff integrity unverified. Owner notified; these notes supplied no mathematical premise. Low memory/stale compute metadata prompted small jobs; no governor intervention or resource shedding.

Did: paid m/4 further core queries from SAME original owner and saved exact certificates; reviewed A057 full exterior scope. Stopped: unlimited exterior-only core payment, disproved by actual product family. Left running: no research job; v2 independent review and post-budget universal core supplier remain open.

## Universal bridge

C019 stopping-tree payment and C024 history transfer advance to ALL m>=4 exterior/tag histories PLUS m/4 ADDITIONAL arbitrary core queries after positive old debit, paid from SAME ORIGINAL4I_X with CURRENT scalar profiles, explicit child innovations and remainder>=m/8 in BOTH full terminals. The exact-cost admission also permits longer core depth without renewing a ticket. This closes the three omitted outer dimensions and the concrete further-core transfer, retaining all coherent logarithms; A057's stronger pathwise m>=16 scope is independently reviewed separately. The actual product-AND2 family proves why unlimited core payment cannot come from this exterior owner alone. What remains is a necessary query after the ACTUAL admitted budget is exhausted, funded by original core influence or a noncircular Booleanity refund. That is the shortest NEXT toward full FEI: one extra query is already paid, while an unbounded exterior-only retry is rigorously impossible.
'''
 (R/'REPORT.md').write_text(report,encoding='utf-8')
 (A/'STATUS.md').write_text(f'STATE: Stage20 v2 SAME original4I_X pays all exterior/tag plus m/4 EXTRA CORE queries;expected escrow retains>=m/8;{total} exact assertions PASS;A057 pathwise scope ACCEPTED;unlimited exterior-only core REFUTED;FEI OPEN.\nNEXT: After ACTUAL admitted core-cost budget exhaustion,pay necessary next core query from ORIGINAL core influence/Booleanity refund;retain old debits/current profiles/BOTH terminals;A057/A060 construct,A091/A087 review.\n',encoding='utf-8')
 for name,entry in {'WORKLOG.md':f'2026-10-23 13:01 UTC stage20 v2 extension: caught that unbounded-core obstruction does NOT require a new owner for ONE further query. Tight h2(c)<=11/32 gives L0>=3m/4-15/32; SAME original cash pays m/4 extra core queries anywhere, even after tag collapse, with>=m/8 left. New frozen audit {c["assertions"]} exact assertions PASS; total{total}. Next is actual budget exhaustion, not a single already-funded query.', 'LEARNED.md':'Stage20 v2 durable correction: NEVER infer one-query insolvency from an unbounded continuation obstruction. Current scalar E handles coherent mean conversion; debit only a=tD_iH(G)<=2t from SAME unused L. Tight original margin3m/4-15/32 buys m/4 ADDITIONAL arbitrary core queries and leaves>=m/8; longer histories use current admission L-2t>=m/8 with actual fees, no replenishment. Missing supplier begins AFTER actual admitted occupation budget exhaustion.'}.items():
  f=A/name;old=f.read_text(encoding='utf-8')
  if entry not in old:f.write_text(old+'\n'+entry+'\n',encoding='utf-8')
 assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
 assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
 proto=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
 for cc in claims:
  assert set(cc)==set(proto['claim_fields']);assert cc['statement_sha256']==hashlib.sha256(cc['exact_statement'].encode()).hexdigest()
 assert set(p)==set(s.split(' (')[0] for s in proto['progress_fields'])
 assert all(h in report for h in proto['report_fields'])
 files=[f for f in R.rglob('*') if f.is_file() and '__pycache__' not in str(f) and f.name!='PERSISTENCE.json']
 assert all(f.stat().st_size<20_000_000 for f in files)
 write(R/'out/PERSISTENCE.json',dict(status='LOCAL_V2_READBACK_PASS',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),mirror='NOT_VERIFIED',files=[dict(path=str(f.relative_to(R)),sha256=sha(f),bytes=f.stat().st_size) for f in files]))
 print(json.dumps(dict(status='V2_PASS',main=v['assertions'],core=c['assertions'],total=total,files=len(files))))
if __name__=='__main__':main()
