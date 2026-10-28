"""Complete the final structural/obstruction scope and persist the exact packet."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,runpy
RUN=Path(__file__).resolve().parents[1];HOME=RUN.parents[1]
def read(p):return p.read_text(encoding='utf-8')
def load(p):return json.loads(read(p))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):
 assert p.resolve().is_relative_to(HOME.resolve())
 p.write_text(s,encoding='utf-8')
def save(p,obj):write(p,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')

product=load(RUN/'out/product.json');conn=load(RUN/'out/connectivity.json')
for result,script in [(product,'product_check.py'),(conn,'connectivity_check.py')]:
 assert result['status']=='PASS' and not result['pilot']
 assert result['source_sha256']==sha(RUN/'code'/script)
assert product['assertions']==1510 and conn['assertions']==8922
assert conn['functions']==270 and conn['nonempty_Fourier_support_sets']==1334
assert conn['positive_disconnected_cases']==conn['outside_fiber_witnesses']==156
runpy.run_path(str(RUN/'code/finalize.py'),run_name='__main__')
now=datetime.now(timezone.utc).isoformat();total=118146+1510+8922;assert total==128578
claims=load(RUN/'CLAIMS.json')
root=next(c for c in claims if c['claim_id']=='A007-ACTUAL-QUEUE-ROOT-COMPONENT-BARRIER')
root['exact_statement']+=(' Additionally, for EVERY nonconstant sign Boolean f and nonempty A with '
 'fhat(A)!=0, construct coordinate-intersection graphs using the COMPLETE positive and negative '
 'signed prime tables. If the positive graph is disconnected, the negative graph contains every '
 'cross-pair of its different components and is connected. At least one table therefore supplies '
 'an actual ONE-root partition forest with at most |A| gates. The fixed output mixture '
 'Q_mix=(Q_+ + Q_-)/2, chosen before A, contains that forest; its binary polarity label costs '
 'Var(f)<=I(f) in total nonempty cross entropy. This is structural existence and label payment '
 'only, not complete name/rank/rarity payment.')
root['hypotheses']+=['For complementarity: actual Boolean Fourier support and BOTH complete signed prime tables',
 'The one-root construction uses allowed attachment multisets; all run probabilities remain part of full cost']
root['proof_source']+=['POLARITY_CONNECTIVITY.md','out/connectivity.json']
root['proof_dependencies']+=['Exact prime DNF on an outside fiber and physical pivotal certificates; complete proof in POLARITY_CONNECTIVITY.md']
counter=next(c for c in claims if c['claim_id']=='A007-ALL-POSITIVE-PRIME-PIJ-QUEUE-OBSTRUCTION')
counter['exact_statement']+=(' Furthermore let U be the zero/one base CNF indicator, '
 'V(Y)=1-U(-Y) on an independent identical-width-pattern copy and F=2U(X)V(Y)-1. '
 'Then I(F)=I(2U-1), H(F)<8I(F), Var(F)>39/64. EVERY positive-prime conditioned '
 'queue for F has C_+(F)/I(F)>r/63, and EVERY positive-prime conditioned queue for '
 '-F has C_-(-F)/I(F)>r/112, independently of their feasible weights and ordered covers. '
 'Thus choosing either ONE GLOBAL output polarity still fails. A fixed normalized mixture '
 'of both queue output laws is explicitly outside this refutation.')
counter['hypotheses']+=['Product family uses disjoint clone blocks; polarity is chosen once globally in the refuted extension',
 'Output-mass mixtures of polarity queues and nonprime representations are not refuted']
counter['proof_source']+=['BOTH_POLARITIES.md','out/product.json']
counter['proof_dependencies']+=['Disjoint AND-product prime classification, product Fourier sectors and physical influence calculation, independently checked on full8/10-bit tables']
counter['refutes']+=['Unregistered extension of PI-J: universal influence payment after choosing one global output polarity']
for claim in [root,counter]:
 claim['statement_sha256']=hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
 claim['review_records'][0]['evidence']+=['out/product.json','out/connectivity.json']
save(RUN/'CLAIMS.json',claims)
next_action=('Price the COMPLETE original fixed two-polarity mixture using the universal per-set '
 'one-root construction: retain each summand D, once-only polarity label, root names/rarities, '
 'child labels, attachment multiset/count and subset/rank costs. Start with the joint X/Y '
 'spectral sector of the both-global-polarity product family; prove payment or an exact rank '
 'obstruction without borrowing H. A008/A009/A015/A086/A094 review both universal structural '
 'proofs and all-reference obstructions first.')
p=load(RUN/'PROGRESS.json')
p['method']='Review-first; full-queue necessary-root bound; all-global-polarity obstruction; universal Boolean prime-complementarity and one-root construction in a fixed mixture; four exact representations'
p['mathematical_delta']=('Universal: every nonempty Boolean Fourier-supported set has a ONE-root '
 'partition forest in at least one complete prime polarity, usable inside one fixed mixture with '
 'polarity debit v<=I. Every original positive-prime queue fails on nonuniform dual tribes '
 '(cost/I>2^w/7,H/I<6); a disjoint product defeats BOTH single global polarity choices '
 '(cost/I>2^w/112,H/I<8). Exact D retained. Complete mixture label/rank/rarity payment remains open.')
p['mathematical_status']='LOCALLY_PROVED_UNIVERSAL_STRUCTURAL_BRIDGE_AND_GLOBAL_PRIME_ROUTE_OBSTRUCTIONS; FULL_FEI_OPEN'
p['source_artifacts']+=['BOTH_POLARITIES.md','POLARITY_CONNECTIVITY.md','FROZEN_SPEC_PRODUCT.json',
 'FROZEN_SPEC_CONNECTIVITY.json','out/product_pilot.json','out/product.json',
 'out/connectivity_pilot.json','out/connectivity.json']
p['next_action']=next_action
p['blockers']=['Full FEI and complete fixed-mixture label/rank/rarity payment remain OPEN',
 'New local proof bundles await independent review; supervisor mirror and downstream use are unobserved',
 'Brain self-care degraded/unverified: stale stored owner-model/state-of-mind freshness']
save(RUN/'PROGRESS.json',p);save(RUN/'PACKET_DELTA.json',p)
report=f'''# A007: universal one-root polarity bridge; global prime-route obstructions

## exact target, quantifiers, hypotheses and units

This is the2026-10-23 05:38 UTC A007/B02 root-normalization stage, under execution protocol2026-10-11-execution-v2 and the owner deadline2026-10-23 14:49 UTC. All costs/entropy are bits. Full FEI is OPEN. Two locally proved bundles in CLAIMS.json separate structural existence, paid reference label, all-reference coding obstructions and the unpaid complete cost.

UNIVERSAL STRUCTURE: for every nonconstant Boolean f and every nonempty A with fhat(A)!=0, at least one COMPLETE signed prime table (positive or negative) supplies a ONE-root actual partition forest. A SINGLE FIXED mixture Q_mix=(Q_++Q_-)/2 can use it, paying the polarity label at total debit Var(f)<=I(f). This does not pay all root names/widths, child names, rank/subset, count or multiset costs.

OBSTRUCTIONS: for any w>=4, r=2^w, arbitrary clause widths w or w+1, the base dual-CNF family has C_*/I>r/7 for EVERY original positive-prime reference and ordered cover, although H/I<6 and variance>3/4. Its disjoint AND product with the complementary-polarity clone defeats BOTH single GLOBAL polarity choices: each independently optimized queue has cost/I>r/112, although the new product has H/I<8 and variance>39/64. The differing constants refer to DIFFERENT families and the product's squared sector-mean factors; the base r/7,H<6 bounds are unchanged. Neither obstruction refutes the fixed output-MIXTURE or full FEI.

## sources actually read, revisions and theorem locators

Read fresh BOARD.md dated2026-10-23 05:35 UTC, B02 STREAM_NOTES.md v2 and own STATUS/LEARNED. A008 had already solved our central-band NEXT: read its20261023T024024Z CENTRAL_PAYMENT.md, REPORT.md, CLAIMS.json and REVIEW_A007.md completely. It independently accepted both previous A007 thinning/retuning statements. Read A01520261023T035924Z REPORT.md, including its independent central review and supplied-reference subprobability transport. Its history theorem is not assumed to create a root bound here.

Re-read forests.tex through the original queue, eq:forestconditioning, partition-forest definition, thm:posteriorforest and per-run cost proof. Baseline papers/protocol are inherited reads; schema validation rereads the protocol. A008's established threshold Theorem A dependency is explicitly retained ONLY in its independent review, not used for either new family entropy estimate. Source byte hashes are in out/SOURCE_RECEIPTS.json. Bounded local learning/obstruction searches found no corresponding entry in the inspected files. One read-only three-wording math-brain query returned weak unrelated cards and no implicant answer; it is not a proof premise or an exhaustive literature-priority check.

## complete derivation or exact first unsupported line

ROOT_COMPONENTS.md: for a target A, join its coordinates when a gate contains both. Successful finite queue visits select only within A; every child attachment lies in A and both gates. Consequently each initial-root descendant tree stays in one component. Every component needs a root and gates disjoint from A must be absent. Summing the EXACT conditioned root law gives Q_*(A)<=product_c D_c/D, D=product_e(1+lambda_e*pi_e)-1, D_c the corresponding component product minus one. This upper-bounds the FULL output law, including repeated visits, overlaps and all output ambiguity. Only original independent root activations are factored; no conditional success probabilities are multiplied without a joint argument.

For component activity S_c<=pi<=1/2, finite product expansion and D>=sum S_c give Q_*(A)<=pi^(k-1)/[k(1-pi)^k]. At pi=2^-r the bit cost is at least r(k-1)-3k pi. The NEGATIVE normalization is retained throughout: it refunds one rarity charge, not the other k-1 charges.

PRIME_QUEUE_OBSTRUCTION.md: positive primes of product OR_j select one variable per clause and have actual rarity2^-r. A one-clause target of size k has k separate components; the SAME original packing rows bound each activity by2^-r. Actual product Fourier coefficients on clause j have square4epsilon_j^2(P/p_j)^2, while physical influence is I_j=2w_j epsilon_j P/p_j. Summing the signed lower bound on these real spectral sectors yields C_*>=sum_j I_j(P/p_j)[r(1-2p_j/w_j)-3pi]. For arbitrary widths w or w+1, P/p_j>1/3 and w>=4, giving C_*/I>r/7. Direct product-spectrum entropy decomposition proves H<6I without borrowing FEI. The original per-run cost upper bound plus Gibbs identity implies every conditioned forest residual is at least C_*-K_ref I, so posterior entropy cannot repair the full positive-prime PI-J expression.

BOTH_POLARITIES.md: let U be that base indicator, a=Pr U, V(Y)=1-U(-Y) on an independent identical-pattern copy, b=1-a, and F=2UV-1. Its physical influence is EXACTLY I(F)=b I_0+a I_0=I_0. Positive primes combine an X-transversal with a complete Y-clause. On X one-clause targets they still need k roots, and their actual spectral mass is b^2 times the base mass; C_+/I>b^2 r/7>r/63. Negative primes are X-zero clauses or Y-zero transversals. On Y one-clause targets the cheap X gates are disjoint, cannot help, and the a^2 sector factor gives C_-/I>a^2 r/7>r/112. Product entropy sectors give H(F)<=2+H_0<8I(F). These prove failure of a SINGLE GLOBAL polarity choice, not failure of a fixed output mixture.

POLARITY_CONNECTIVITY.md supplies the universal repair of structural root multiplicity. If the complete positive A-graph has components C_c, then on every fixed outside fiber the positive DNF is a constant OR a collection h_c(x_Cc) on disjoint blocks. Nonzero fhat(A) supplies an actual outside fiber with nonzero full-A coefficient; there the complement factors as product(1-h_c), each factor's full coefficient is nonzero, and every coordinate is relevant. For ANY cross-pair a,b in different components, choose independent FALSE pivotal endpoints of h_c,h_d and false points in the other blocks. The full false point is pivotal in BOTH a,b. Every negative certificate there must contain both; minimizing it gives an actual negative prime containing a,b. Thus the negative graph contains every cross-pair and is connected.

For a connected table, greedily add a gate meeting both assigned and fresh A-coordinates; assign it ALL fresh coordinates and attach it to the owner of a shared coordinate. This gives a one-root tree with at most |A| gates and a partition of A. The original queue permits repeated attachment occurrences via multisets, so branching from one owner coordinate is legitimate; all probabilities still have to be paid. The full ownership graph is reachable from that root and hence has one source SCC. The two prime tables and mixture weights1/2 are fixed before A; the only new reference-label debit is exactly v<=I, charged once. Each summand keeps its OWN D; no pooled negative-normalizer credit is asserted.

FIRST UNSUPPORTED LINE toward full FEI: a dimension-independent COMPLETE label/rank/rarity payment for the resulting one-root forests inside this SAME FIXED mixture. Connectivity/existence alone is not that payment, and neither family entropy upper bound is used to assume it. Nonprime representations and normalized output mixtures remain viable. REVIEW_A008.md independently reconstructs the complete central251I/5 statement, including optional wrapper, at its unchanged hash and explicit established threshold premise: HOLDS without repair.

## executed validation with domain, arithmetic, commands and outputs

Every job has its own saved frozen spec and uses `python -X utf8`. Main `code/check.py --pilot`:561 assertions,0.142s; full:20464,1.312s. It constructs three complete Boolean tables, all signed positive/negative primes, integer Walsh coefficients, physical influences and product-spectrum identities; nine family references plus one fixed general-graph guard give454 component/output cases and2358 enumerated root sets. Its501 large-family parameter orbits use exact product moments, not impossible full truth tables. All-domain conclusions use the analytic proofs.

Independent `code/graph_audit.py`:97682 assertions,1.744s; all96966 root/target pairs in six separately weighted references. Direct BFS through ACTUAL allowed attachments tests which coordinates initial roots can reach, independently of the main union-find component derivation. Accepted root mass equals the factorized component-root expression exactly. It does not import the main helper.

`code/product_check.py --pilot`:332 assertions,0.046s; full:1510,0.550s. Complete8- and10-bit product tables supply1280 squared Walsh coefficients and physical influences. ALL65610 signed faces are classified for BOTH polarities by independent truth-point bitsets; complete prime tables match the analytic products/unions. Fifteen exact large-family moment cases verify both-global-polarity lower bounds and H<8I. No missing mixed certificate is assumed away.

`code/connectivity_check.py --pilot`:216 assertions; full:8922,0.075s. ALL270 labelled nonconstant functions through n=3, all complete signed prime tables and1334 nonempty Fourier-support sets are checked. There are156 positive-disconnected cases, each with an explicit nonzero outside fiber and every required negative cross-pair. All1334 sets receive a constructed actual one-root ownership forest; the FULL ownership graph, not just a recorded chosen tree, is independently traversed from its root.

TOTAL NONPILOT ASSERTIONS:{total}. Overlapping pilots561+332+216 are not added. All arithmetic is integer/Fraction/bitset; no tolerance or floating sign accepts a result. Guards show that dropping D changes mass, nonprime gates can merge components, and complementary prime tables can repair root connectivity. SPEC_NOTES.md retains the graph frozen-count typo134806 versus its unchanged expression/actual96966, and distinguishes the one fixed guard from the nine searched family references. New product/connectivity domains were explicitly frozen before their pilots; no automatic dimension increase occurred. Reported seconds are script timings, not claims about shell-startup latency or billing.

All jobs were estimated100MB and completed below55s. No >300MB job, heavy build, compiler, GPU, detached worker or remote machine was used; no other work was stopped/throttled. Lean certification is not claimed. The new all-function and all-parameter theorems rest on their complete displayed proofs, not finite extrapolation.

## proof dependencies and changed downstream conclusions

The root-component bound depends only on original queue semantics and finite products. Complementarity is proved directly from exact prime DNF, outside-fiber Fourier factorization, physical pivotal points and minimal certificates; the constructive one-root bridge adds the original attachment-multiset semantics and the elementary v<=I identity. The two obstruction families use those root bounds plus complete prime classification and direct Fourier/influence calculations. Their H<6I,H<8I guard bounds are independently derived, not assumed universal FEI. Gibbs identity/source per-run cost connect actual-output barriers to every posterior residual. The proof graph is acyclic.

Two new root/obstruction bundles remain pending independent-agent acceptance; self-checks are not independent review. A008 central@1 is independently reconstructed without repair. Previous A007 thinning/retuning statements are unchanged and now have A008's independent acceptance. No class-specific root payment, A008 central theorem, universal signed-normalizer upper bound or supplied-reference history transport is refuted. Only the exact universal fixed-positive-prime PI-J target and its one-global-polarity extension fail. A fixed normalized polarity mixture is explicitly outside both refutations and now has universal ONE-root structural witnesses; full payment remains open. Consumers relying on the false universal helpers must replace them or mark dependence conditional. Canonical propagation/mirror acceptance is not invented.

## one next mathematical action and independent reviewer

{next_action} The critical escape from the obstruction is now mathematically identified: select polarity PER SET within one previously fixed mixture, not a free reference reset. Test the product's joint sector, where root connectivity is available but repeated clause identification and subset/rank costs may still matter. A008/A009/A015/A086/A094 are named on-disk reviewers, not a claim that a message was sent or acceptance arrived. Review-first priority applies before opening another broad candidate.

## actual persistence receipts or precise save blocker

All four exact-schema protocol files, universal proofs, two obstruction proofs, source-bound A008 review, four frozen specs, accounting notes and exact output receipts are saved in this run. PACKET_DELTA.json is identical to PROGRESS.json with packet_ids=[A007]. STATUS.md, WORKLOG.md and LEARNED.md are current only in A007. out/PERSISTENCE_RECEIPT.json records landed hashes and is reread; files are below20MB. The full final package can be regenerated by `python -X utf8 code/finish.py` after executing the four named mathematical helpers (their pilots are optional reproduction checks).

Shared registries, other-agent files, brain data, source trees, trading paths, mail and git were not modified/performed. Supervisor mirror/registry adoption and independent acceptance remain unobserved. Task-checklist lifecycle is recorded separately as directed by the session hook. No job from these completed helpers remains running; no other work was stopped. Brain self-care remains degraded/unverified: owner-model91.3h and state-of-mind75.9h stale at wake; affected personal-context freshness is not used as a mathematical premise.

## Universal bridge

This stage moves C020 at the root-normalization interface in BOTH directions. The complete fixed-positive-prime route is locally refuted by actual-output cost/I>2^w/7, and even one global polarity choice fails on a product family with both costs/I>2^w/112; the exact D refunds one root rarity only. Positively, a universal Boolean prime-complementarity lemma constructs ONE-root partition forests for EVERY Fourier-supported set inside ONE fixed two-polarity mixture, with selector debit v<=I paid once. What remains is its complete original label/rank/rarity/count/multiset payment, not structural root existence or a free normalization reset. NEXT attacks that universal unpaid cost through the product's joint sector and the original mixture, so it tests a necessary representation interface rather than adding another already-known FEI class. Full FEI remains OPEN and all new local proofs await independent review.
'''
protocol=load(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading+'\n' in report
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
write(RUN/'REPORT.md',report)
write(RUN/'CHECKPOINT.md',f'COMPLETE_LOCAL {now}\nUniversal per-set polarity connectivity gives one-root forests in a fixed mixture, label v<=I. Both global-prime orientations locally refuted on product family. {total} nonpilot assertions PASS; new review pending; full FEI OPEN.\nNEXT: '+next_action+'\n')
write(HOME/'STATUS.md',f'STATE: A007 stage saved: UNIVERSAL per-set polarity one-root forest/label v<=I; BOTH global prime orientations cost/I>2^w/112 on product while H/I<8;{total} nonpilot checks PASS; A008 central HOLDS; new review pending; FEI OPEN.\nNEXT: '+next_action+'\n')
marker=RUN.name+' FINAL_POLARITY_MIXTURE'
entry=f'\n## {now} | {marker}\nFinal scope supersedes this stage\'s earlier NEXT of choosing one global polarity: a disjoint product defeats BOTH choices, with exact squared sector-mean factors giving cost/I>2^w/112 and actual H/I<8. Universal prime complementarity proves every nonempty Boolean Fourier-supported set has a one-root forest in at least one complete signed prime table. A fixed two-polarity mixture pays label debit v<=I; all remaining run costs stay unpaid. Full checks:20464+97682+1510+8922={total}, excluding overlapping pilots. All proofs and final protocol files saved; independent new review/mirror unobserved; FEI OPEN. NEXT: {next_action}\n'
old=read(HOME/'WORKLOG.md')
if marker not in old:write(HOME/'WORKLOG.md',old+entry)
lesson=f'''\n## {marker}

UNIVERSAL: for fhat(A)!=0, if the complete positive-prime A-intersection graph has multiple components, the negative graph contains EVERY cross-pair and is connected. Proof: an outside fiber has nonzero full-A coefficient; positive DNF decomposes as OR of disjoint component functions, each depends on all its coordinates; independent FALSE pivotal endpoints force any negative certificate to include any chosen cross-pair. A connected table greedily supplies an actual ONE-root partition forest, at most|A| gates. Repeated attachment occurrences are allowed by the original MULTISET law. Fix BOTH tables and Q_mix=(Q_++Q_-)/2 before seeing A; the reference-label debit is v<=I, once. Root D and all other costs remain with their own summand. Structural existence is not a full cost payment.

BOTH global orientations can fail: for U=AND of OR clauses with r=2^w, widths w or w+1, V=1-U(-Y), F=2UV-1, physical I(F)=I(2U-1). Positive primes combine an X-transversal with a Y-clause; negative primes are X-zero clauses or Y-zero transversals. Hard X-only and Y-only spectral sectors get squared factors b^2 and a^2. Thus every global-polarity queue cost/I>r/112, while H(F)/I(F)<8 and variance>39/64. This strengthens (not changes) the base family's r/7,H<6 result. A FIXED OUTPUT MIXTURE remains unrefuted and is the universal structural bridge above. Do not confuse choosing one orientation globally with selecting a run in a fixed mixture per set.

Final shortest NEXT: pay complete label/rank/rarity/attachment cost in this same fixed mixture, beginning with the product's joint X/Y sector where root connectivity no longer obstructs. Keep full original denominators and output ambiguity. Do not assume the actual H bound pays its queue cost. These new proofs require independent-agent acceptance; exhaustive n<=3 corroborates the universal graph lemma but does not replace the proof.\n'''
old=read(HOME/'LEARNED.md')
if marker not in old:write(HOME/'LEARNED.md',old+lesson)
assert load(RUN/'PROGRESS.json')==load(RUN/'PACKET_DELTA.json')
assert len(read(HOME/'STATUS.md').splitlines())==2
files=sorted(p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json')
assert all(p.stat().st_size<20_000_000 for p in files)
receipt={'saved_utc':now,'run_id':RUN.name,'schema_validation':'PASS','nonpilot_exact_assertions':total,
 'new_independent_review':'PENDING','mirror_verification':'UNOBSERVED','full_FEI':'OPEN',
 'files':[{'relative_path':str(q.relative_to(RUN)),'bytes':q.stat().st_size,'sha256':sha(q)} for q in files],
 'rolling_files':[{'path':str(HOME/n),'sha256':sha(HOME/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]}
save(RUN/'out/PERSISTENCE_RECEIPT.json',receipt)
assert load(RUN/'out/PERSISTENCE_RECEIPT.json')==receipt
print(json.dumps({'FINAL_SAVED':str(RUN),'nonpilot_exact_assertions':total,'schema':'PASS',
 'new_claim_bundles':2,'independent_review':'PENDING','files':len(files)+1,
 'largest_file_bytes':max(q.stat().st_size for q in files)}))
