from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];HOME=ROOT.parent.parent;BASE=HOME.parent.parent
def dump(path,value):path.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
src25=BASE/'agents'/'A025'/'runs'/'20261014T002956Z-fleet05-A025-rare-event-counterfamily'
src23=BASE/'agents'/'A023'/'runs'/'20261013T223305Z-fleet05-A023-amortized-rarity-budget'
src98=BASE/'agents'/'A098'/'runs'/'20261013T235014Z-fleet05-A098-resource-reallocation'
src92=BASE/'agents'/'A092'/'runs'/'20261013T222550Z-fleet05-A092-counterexample-referee'
source=json.loads((src25/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
source['review_records'].append({'reviewer':'A046','verdict':'HOLDS_PAIRED_ROW_POINT_SWITCH_CRITERION_ONLY','source_run':ROOT.name,'source':'PROOF.md section 1','scope':'For arbitrary actual Boolean G,H with disagreement gamma, B/d <= 2(1-rho)+rho log2(euler/(rho^2 gamma)), hence the source uniform upper bound and moderate-gap good-node consequence. Independent reconstruction, no repair.','excluded':'No blanket independent acceptance of bundled all-s no-go, finite census, reproduction or full terminal class theorem','statement_sha256':source['statement_sha256'],'repair_supplied':False})
source['status']='PARTIAL_INDEPENDENT_ACCEPTANCE_PAIRED_ROW_SLICE; OTHER_BUNDLED_CLAUSES_REVIEW_PENDING'
statement='Let S,W,U,V be compatible point indicators on disjoint uniform blocks of positive widths s,L,R,T and g an independent balanced Boolean core. For F=1+[WUV OR S(U OR V)](g-1), query the separator S until first failure or completion, then resolve WUV or U OR V and stop at a constant or g. Put alpha=2^-s, q=2^-R,r=2^-T,eta=2^-(L+R+T),e=q+r-qr-eta,JB=(L+R+T)eta,JC=R q(1-r)+T r(1-q),JD=JB+JC,pi=eta+alpha e,m=ceil(log2(min(R,T)+2))+2 and M=min(s,m). Every live separator query with j>m remaining bits is strictly K=4-good. The nonnegative reserve at live state j is V_j=2^-j[min(j,m) JD+e min(j,m)(min(j,m)-1)/2+min(j,m)e I(g)], set zero after failure. Its exact physical drift V_j-V_(j-1)/2 equals the actual child-product face price c_j=2^-j[JD+(j-1)e+e I(g)] when j<=m and zero otherwise. Thus the actual localized separator bill is <=V_s<=M I_other+(M-1)I_sep/2+M I_terminal<=M I(F), where I_sep=s alpha e,I_other=(1-alpha)JB+alpha JC,I_terminal=pi I(g). Terminal entropy remains pi H(g), and H(F)<=(4+2/ln2)(I_sep+I_other)+V_s+pi H(g). This eliminates dependence on separator length s for fixed R,T, but is not a universal influence constant or terminal-core certificate.'
hyp=['Actual Boolean signs on uniform cube; entropy and logarithms in bits','Compatible point literals; disjoint fresh separator/controller blocks independent of g','Independent balanced core; full pi H(g) retained at stopping leaves','History-measurable physical policy exactly as specified; one query per coordinate along each path','V is a cutoff-envelope reserve and may charge eligible but actually good layers; it is not renewed at descendants']
digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={'claim_id':'A046-SEPARATOR-LAYER-CUTOFF-RESERVE','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,'contributors':['A046'],'proof_source':{'run_id':ROOT.name,'files':['PROOF.md','REPORT.md','code/layers.py','code/reserve_check.py','out/RESULTS.json','out/RESERVE_CHECK.json']},'proof_dependencies':[],'review_records':[],'status':'NARROW_EXISTING_SEPARATOR_INTERFACE_REFINEMENT_PROVED_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A023','A025','A040','A050','A064','A087','A092','B10','B20']}
dump(ROOT/'CLAIMS.json',[source,claim])
report=r'''# exact target, quantifiers, hypotheses and units

A046/B10 stage 4 resumes the multi-layer separator obligation in A098's refreshed dispatch, rather than the stale B10 singleton census. The target is the existing A023/A025 reserve interface on actual uniform Boolean functions F=1+[WUV OR S(U OR V)](g-1), where S,W,U,V are disjoint compatible point blocks of widths s,L,R,T>=1 and g is an independent balanced Boolean core. Query separator bits until failure or completion, resolve the appropriate controller, and stop at constant or g. Strict badness is B_i>4 Inf_i; its price is I(child_product)/2. All entropy is bits; reach weights and influence are physical. Terminal entropy pi H(g) is retained. Full FEI remains OPEN.

The new exact result confines possible bad separator queries to j<=m remaining bits, where m=ceil(log2(min(R,T)+2))+2. An explicit history-measurable remaining reserve has zero drift at earlier layers, spends one eligible face price per later layer and has zero terminal reserve. Its root allowance is at most min(s,m)I(F), independent of separator length for fixed R,T. This is a narrow extension of the existing separator potential, not a new broad universal candidate or a dimension-independent FEI constant.

# sources actually read, revisions and theorem locators

Read BOARD.md at stage entry, supervisor snapshot 2026-10-14 01:20 UTC; B10 STREAM_NOTES v2 (2026-10-11 23:31Z); own STATUS.md; execution protocol 2026-10-11-execution-v2 in full. The lead's scalar A046 instruction was completed in stage 2 and is stale. The saved stage-3 next action and A098 stage-3 CHECKPOINT_ALLOCATION.json lines 69-79 explicitly direct the multi-bit layer test. We follow that source-bound continuation and record why scalar review was not restarted. Earlier required campaign/paper context remains the source history in the completed runs; no new external paper theorem, web claim or novelty assertion is used.

Read originals: A023 run 20261013T223305Z REPORT.md/CLAIMS.json, separator price, descendants, marked ownership and terminal sections; A025 run 20261014T002956Z REPORT.md/PROOF.md/CLAIMS.json, especially paired-row bound (1), exact layer accounts and small-gamma gap; A098 refreshed allocation and PROGRESS; A092 run 20261013T222550Z REPORT.md, signed common-lift conversion and explicit witness-bank gap. An initial guessed A092 path was absent, then directory discovery found the actual source; that access miss produced no mathematical conclusion. SOURCE_MANIFEST.json pins actually inspected bytes.

A025 had already refuted unfiltered repeated full-face pricing and paid R=T=1. That discovery was consumed before any new search. We therefore did not repeat its all-s counterfamily or moderate-disagreement computation; the frozen entropy cases have R=T in {2,4,8}, including disagreement well below 1/4.

# complete derivation or exact first unsupported line

The complete checked derivation is PROOF.md. Its critical universal steps are summarized here.

For arbitrary actual Boolean branch signs G,H with gamma=Pr(G!=H)>0, a fresh j-bit point switch F=G+A_j(H-G) has d=rho gamma, rho=2^{-(j-1)}. Parseval gives sum(Hhat-Ghat)^2=4gamma. The nonempty residual-selector Fourier rows contribute exactly 2(1-rho)d to erasure. In the empty residual row the derivative-sector mass totals rho d, and the combined mass is at most one. Applying the binary remainder inequality and log-sum yields

    B_j/d <= 2(1-rho)+rho log2(euler/(rho^2 gamma)).

This independently accepts the paired-row slice of A025 v1 unchanged, without accepting its entire bundled claim. No repair is supplied. If gamma>=2^-D, take h=ceil(log2(D+1)), m=h+2. At j>m, k=j-1>=h+2, so 2^-k D<=1/4 and 2k2^-k<=1. Since log2(euler)-2<0, B_j/d<=13/4<4. Thus only the final m live layers can be bad, even at arbitrarily small gamma.

For the specified three-event controller, q=2^-R,r=2^-T,eta=2^-(L+R+T),e=q+r-qr-eta. Since eta<=qr/2, e>=max(q,r); balance gives gamma=e/2>=2^{-(min(R,T)+1)}. This proves the stated m for all positive widths.

Let alpha=2^-s, JB=(L+R+T)eta, JC=R q(1-r)+T r(1-q), JD=JB+JC, pi=eta+alpha e. The disjoint directional cuts of WUV and U OR V give the exact accounts

    I_sep=s alpha e,
    I_other=(1-alpha)JB+alpha JC,
    I_terminal=pi I(g), I(F)=I_sep+I_other+I_terminal.

At live layer j the actual queried influence is 2^-j e and its face cost is c_j=2^-j[JD+(j-1)e+e I(g)]. Define M_j=min(j,m) and

    V_j=2^-j[M_j JD+e M_j(M_j-1)/2+M_j e I(g)], V_0=0.

On failure set the separator reserve to zero; the remaining point controller still has its separate influence account. The fair success child has reserve V_(j-1). Direct subtraction proves V_j-V_(j-1)/2=c_j for j<=m and zero for j>m. Every possible bad-layer price is at most this drift. The reserve can increase on a success branch, but its expected drift is exactly owned and is not restarted. Finite summation leaves zero terminal reserve and proves Q_bad,separator<=V_s.

With M=min(s,m), alpha JD<=I_other, alpha e I(g)<=I_terminal and M<=s imply

    V_s<=M I_other+(M-1)I_sep/2+M I_terminal<=M I(F).

The remaining controller descendants have constant-child or two-point-union splits covered by the reconstructed A023 good-node inequality, hence are strictly 4-good. With JS_i<=2d_i/ln2 and every core terminal retained,

    H(F)<=(4+2/ln2)(I_sep+I_other)+V_s+pi H(g).

This is parameter-dependent payment. No universal terminal certificate or width-independent root reserve follows.

The output/spectral conditioning correction is retained explicitly. For this declared coherent ROOT-spectral physical coupling, J_tree=sum w_v JS_v=I(S0;Pi). At the stopped partition, I(Y;Pi)=h2(pi/2)-pi. Thus

    C_T=H(Pi|Y)-H(Pi|S0)=J_tree-[h2(pi/2)-pi],
    C_T<=2(I_sep+I_other)/ln2-[h2(pi/2)-pi].

This reconstructs A092's existing conversion at its root-compatible scope. It is not another refund to add to the face ledger. The tested conversions are positive; for s=L=1,R=T=2 it lies in (1.112640489182011,1.112640489182012) bits. Additional prescribed-witness conditioning, resetting a reference, or injecting actual descendant schedules is outside this formula. A048's new injection obstruction is a scope warning from the board, not a theorem independently reviewed here.

First unsupported universal line: replace the remaining width-dependent envelope by a universally influence-paid actual-bad-layer reserve as min(R,T) grows, and pay prescribed witness/reset costs and all terminal-core entropy on the same exclusive account. The new cutoff removes separator-depth accumulation; it does not remove the logarithmic smaller-controller-width dependence.

Retired unchanged mechanisms: tax-free J<=M, any universal O(p) scalar tax, essential-bit sharp tax payment without a refund, full-price reservation at every separator layer, free exchange of output and spectral conditioning, and omission of terminal Fourier entropy. Neither a larger numerical constant for the already-false unfiltered repeated rule nor a repeated singleton grid was computed.

# executed validation with domain, arithmetic, commands and outputs

Both jobs had saved frozen specifications before execution, used python -X utf8, stayed below a 60-second pilot cap, and ran sequentially. No GPU, background process, automatic dimension escalation or job expected above 300 MB was used; estimated peaks 90 MB and 25 MB, so the heavy-job memory gate was not triggered.

Command: python -X utf8 runs\20261014T012528Z-fleet05-A046-current-candidate-intake\code\layers.py. PASS in 19.6306295 seconds: 18 roots s in {1,4,8}, L in {1,3}, R=T in {2,4,8}; 78 separator-node occurrences, zero strictly bad separator occurrences; 194 recorded assertions and eight independent small explicit truth-table/FWHT roots. Maximum declared dimension 28. Fixed Fourier category grouping by each block's empty/nonempty frequency uses exact multiplicity 2^width-1, justified by the multilinear point-indicator polynomial. It does not replace the physical input law by a biased mask law. All coefficients, physical influences, reach weights, face costs and caps are Fraction values. Entropy signs use the prior exact rational 24-term atanh logarithm enclosure with signed interval multiplication and outward decimal endpoints. Every root was flushed immediately to RESULTS.json.

The grouped full stopping tree independently checks the removed-influence partition, erasure+JS spectral telescope and signed root/output conversion, retaining the general terminal pi H(g) symbolically. The numerical instances use g=z, whose terminal Fourier entropy is exactly zero; that certificate is not substituted for an arbitrary balanced core. Interval overlap checks corroborate entropy identities; their proofs are the exact algebra in PROOF.md, not interval overlap alone. Finite zero badness is not extrapolated to all widths.

Command: python -X utf8 runs\20261014T012528Z-fleet05-A046-current-candidate-intake\code\reserve_check.py. PASS in 0.5485034 seconds: 648 independent rational account cases with s=1..8, L,R,T=1..3 independently and formal core influence {1,5/2,10}; 2,916 exact reserve-drift subtractions and 4,860 recorded assertions. It verifies every live drift, root telescoping, density cutoff and exclusive root cap without any entropy approximation. The total recorded assertion count is 5,054. These finite checks supplement, rather than establish, the all-width proof.

# proof dependencies and changed downstream conclusions

CLAIMS.json records a partial independent acceptance of the unchanged A025 paired-row criterion only, preserving its exact statement hash and contributors. Its bundled counterfamily and finite census remain outside this review. The new layer-cutoff reserve is a narrow, self-contained continuation of the existing A023/A025 separator interface, with prior boundary formulas credited and reconstructed. No new broad universal candidate was opened at the review cap. A050's accepted output refund and A092's uniform conversion supply scope context; neither alone pays a prescribed witness bank.

Changed downstream conclusion: A023/A025/A064 need not renew a complete separator allowance at every reached layer. They can use V_j with exact physical drift and zero terminal reserve, charging at most m layers independently of s. An early rare-success path can raise V without spending it in expectation. What still cannot be inferred is an absolute constant uniformly in R,T, zero badness at all widths, arbitrary reference-reset payment or an arbitrary-core FEI bound. There is no existing-claim refutation and no shared-registry mutation.

# one next mathematical action and independent reviewer

Next: use the actual paired Fourier coefficients of WUV and U OR V to sharpen the cutoff-envelope price at its final eligible layers as min(R,T) grows. Seek a summable bound on the actual bad-layer debit from one controller/core account, or an actual Boolean failing family for that specific rule; retain pi H(g) and the signed conversion throughout. This targets the remaining width dependence rather than enlarging the finite zero-badness grid or repeating A025's unfiltered no-go. A087 should review reserve signs and terminal ownership; A092 should challenge the paired-row normalization and root-compatible conversion scope. Saved handoff metadata is not a sent message.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved in the assigned stage directory, with PROOF.md, both frozen specs, exact results, code, source manifest, schema checks and local hash receipts. STATUS.md has exactly STATE/NEXT lines; WORKLOG.md and LEARNED.md are appended. All writes are inside A046 and every file is under 20 MB. No Git, external message, brain write or foreign-folder mutation occurred. Supervisor copies, mirror verification, independent review of the new reserve and actual downstream adoption remain unobserved.

# Universal bridge

This stage moves C019 localized odd-face stopping-tree payment by replacing repeated multi-bit separator reservations with an explicit transported reserve: possible bad costs are confined to at most ceil(log2(min(R,T)+2))+2 layers, earlier layers have zero reserve drift, and the root allowance has no dependence on separator length for fixed controller widths. The 5,054 recorded exact assertions pass; the frozen small-disagreement cases have zero actual bad separator cost, with positive signed output/spectral conversion kept visible. A universal constant as controller widths grow, prescribed-witness/reset payment and terminal-core admission remain open. NEXT sharpens the actual final-layer debit against the already-owned account, because that is the remaining nonuniform step in this existing restriction mechanism rather than another isolated class entropy result.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B10','packet_id':'A046','gap_id':'G-C019-MULTILAYER-SEPARATOR-OWNERSHIP','attempt_id':'A046-stage4-layer-cutoff-1','method':'Independent paired-row slice review, analytic small-disagreement cutoff, explicit history-measurable reserve subtraction, grouped actual Fourier certificates and direct edge reproduction','mathematical_delta':'Point-separator possible bad queries confined to final m=ceil(log2(min(R,T)+2))+2 layers; transported V has exact eligible-price drift and zero earlier drift, Vroot<=min(s,m)I; 5054 recorded exact assertions PASS; no separator bad nodes in frozen low-gamma domain; signed conversion and all terminal entropy retained','deliverable_status':'COMPLETE_LOCAL_SCOPED_REFINEMENT','mathematical_status':'PARAMETER_DEPENDENT_LAYER_RESERVE_PROVED_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':['A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER@2 (boundary/interface context reconstructed)','A025-POINT-SEPARATOR-RESERVE-REPLAY-NOGO@1 (paired-row slice independently accepted only)','A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1 (prior accepted scope)','A092 stage3 root-spectral signed conversion (reconstructed scope)'],'claims_created_or_changed':['A025-POINT-SEPARATOR-RESERVE-REPLAY-NOGO@1 partial independent review','A046-SEPARATOR-LAYER-CUTOFF-RESERVE@1 narrow existing interface refinement'],'source_artifacts':['PROOF.md','REPORT.md','CLAIMS.json','code/layers.py','code/reserve_check.py','out/FROZEN_SPEC.json','out/RESERVE_SPEC.json','out/RESULTS.json','out/RESERVE_CHECK.json','out/SOURCE_MANIFEST.json'],'next_consumers':['A023','A025','A040','A050','A064','A087','A092','B10','B20'],'next_action':'Sharpen actual final eligible-layer paired-row debit as min(R,T) grows, from one owned controller/core account with signed conversion and pi H(g) retained; do not escalate zero-badness census','stagnant_substantive_attempts':0,'blockers':['Width-independent bad-layer debit remains unproved','Prescribed witness/reset payment and universal terminal admission remain open','Independent review and supervisor adoption unobserved'],'packet_ids':['A046']}
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
sources=[BASE/'BOARD.md',BASE/'claude'/'B10'/'STREAM_NOTES.md',src23/'REPORT.md',src23/'CLAIMS.json',src25/'REPORT.md',src25/'PROOF.md',src25/'CLAIMS.json',src98/'CHECKPOINT_ALLOCATION.json',src98/'PROGRESS.json',src92/'REPORT.md',Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
dump(ROOT/'out'/'SOURCE_MANIFEST.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'scope':'Read/reconstruction scope explicitly limited in REPORT.md; receipt alone is not theorem review'} for p in sources])
(HOME/'STATUS.md').write_text('STATE: A046 stage 4 complete: small-disagreement separator cutoff and exact transported reserve proved; root cap has no separator-length growth at fixed widths; 5,054 recorded exact assertions PASS; FEI OPEN.\nNEXT: Sharpen actual final eligible-layer debit as min(R,T) grows with one controller/core account, signed root-output conversion and full pi H(g); A087/A092 review reserve and paired-row scope.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-14 stage 4 '+ROOT.name+': read updated board and A098 allocation, consumed A025 already-completed multi-bit no-go before computing. Independently accepted paired-row slice; proved logarithmic small-gamma layer cutoff and exact Vj-.5Vj-1 transport. Eighteen roots/78 separator occurrences had zero badness, positive signed conversion retained; 648 rational reserve ledgers PASS, total 5054 recorded assertions. Width-independent payment and terminal-core admission still open.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage 4: For any point switch G+A_j(H-G) with disagreement gamma>=2^-D, possible strict K4-bad queries have j<=ceil(log2(D+1))+2. For WUV OR S(U OR V) with balanced g, D=min(R,T)+1 suffices. Vj=2^-j[M JD+eM(M-1)/2+Me I(g)], M=min(j,m), has drift cj when j<=m and zero otherwise, with failure reserve zero. Vroot<=min(s,m)I removes s-growth at fixed controller widths; it is not an absolute FEI constant. A025 unfiltered no-go/moderate-gap result was already done and must not be rerun. Exact finite low-gamma zero badness does not prove all-width zero badness. Root-compatible signed conversion remains a cost, and all pi H(g) remains terminal.\n')
protocol=json.loads(sources[-1].read_text(encoding='utf-8-sig'))
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
for c in (source,claim):assert set(c)==set(protocol['required_per_run']['claim_fields'])
for title in protocol['required_per_run']['report_fields']:assert '# '+title in report
assert report.strip().split('\n\n')[-2]=='# Universal bridge'
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((HOME/'STATUS.md').read_text().splitlines())==2
stats=json.loads((ROOT/'out'/'RESULTS.json').read_text());rs=json.loads((ROOT/'out'/'RESERVE_CHECK.json').read_text())
assert stats['status']==rs['status']=='PASS'
assert stats['exact_assertions']+rs['recorded_assertions']==5054
dump(ROOT/'out'/'SCHEMA_CHECK.json',{'status':'PASS','new_statement_sha256':digest,'progress_copy_identical':True,'source_review_partial_only':True,'recorded_assertions':5054,'report_required_fields':True,'universal_bridge_final_paragraph':True})
receipts=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
dump(ROOT/'out'/'PERSISTENCE_RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','saved_files':len(receipts)+1,'recorded_assertions':5054,'full_fei':'OPEN'}))
