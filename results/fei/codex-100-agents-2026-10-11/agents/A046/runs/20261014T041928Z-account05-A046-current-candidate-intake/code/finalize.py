from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];HOME=ROOT.parent.parent;BASE=HOME.parent.parent
def dump(path,value):path.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
src40=BASE/'agents'/'A040'/'runs'/'20261014T033148Z-account05-A040-credit-insufficiency-tests'
src21=BASE/'agents'/'A021'/'runs'/'20261014T011316Z-account05-A021-rare-core-asymptotics'
src23=BASE/'agents'/'A023'/'runs'/'20261014T022245Z-account05-A023-amortized-rarity-budget'
old=json.loads((src40/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
assert old['claim_id']=='A046-SEPARATOR-LAYER-CUTOFF-RESERVE' and old['status']=='INDEPENDENT_REVIEW_HOLDS'
statement='Let S,W,U,V be independent compatible point indicators on disjoint uniform blocks of positive widths s,L,R,T, and let g be an independent balanced Boolean sign. Set F=1+[WUV OR S(U OR V)](g-1), q=2^-R,r=2^-T,eta=2^-(L+R+T),e=q+r-qr-eta,alpha=2^-s,JB=(L+R+T)eta,JC=R q(1-r)+T r(1-q),JD=JB+JC,pi=eta+alpha e. Query S until failure or completion, then resolve WUV or U OR V and stop at a constant or the actual g. For e<=1/8 every live separator query has B_i/Inf_i<1781/480<4. In particular min(R,T)>=4 gives zero localized strict-K4 bad-control-prefix bill for every s,L. Otherwise define m_*=ceil(log2(min(R,T)+2))+2<=5; in the rare regime define m_*=0. The reserve at live layer j is W_j=2^-j[M_j JD+e M_j(M_j-1)/2+M_j e I(g)], M_j=min(j,m_*), and is zero after separator failure. Its physical drift equals the actual child-product face price c_j=2^-j[JD+(j-1)e+e I(g)] at j<=m_* and zero otherwise. Every possible bad-layer debit is bounded by this drift. With I_sep=s alpha e,I_other=(1-alpha)JB+alpha JC,I_terminal=pi I(g), the entire controller-prefix bad bill obeys Q_bad<=W_s<=5 I_other+2 I_sep+5 I_terminal<=5 I(F), uniformly in all widths and core dimension. Terminal entropy remains pi H(g). Moreover H(F)<=(4+2/ln2)(I_sep+I_other)+W_s+pi H(g); with a separately proved terminal rate C0, H(F)<=max(9+2/ln2,C0+5)I(F). No prescribed-witness funding, arbitrary unbalanced-core K4 bound or general nested-selector reserve is asserted.'
hyp=['Actual uniform Boolean signs; entropy and logarithms in bits; physical pivotal influences and history reaches','Independent balanced core g and disjoint compatible positive point blocks of the specified widths','Exactly the declared control-first stopping prefix; each physical coordinate queried at most once along a path','Q_bad is strict-K4 bad-node face price, not the unfiltered old V envelope or bad nodes inside the stopped core','All terminal pi H(g) is retained; any C0 is a separately certified inherited core rate; no spectral reference bank is assumed free']
digest=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={'claim_id':'A046-SEPARATOR-LAYER-CUTOFF-RESERVE','version':2,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,'contributors':['A046'],'proof_source':{'run_id':ROOT.name,'files':['PROOF.md','REPORT.md','code/check.py','code/accounts.py','code/direct.py','out/SPECTRAL_CHECK.json','out/ACCOUNT_CHECK.json','out/DIRECT_CHECK.json']},'proof_dependencies':[{'claim_id':old['claim_id'],'version':1,'statement_sha256':old['statement_sha256'],'status':'INDEPENDENTLY_ACCEPTED_BY_A040_WITHOUT_REPAIR','scope':'Original cutoff and physical reserve/account theorem, including descendant-good and retained terminal scope'}],'review_records':[],'status':'EXISTING_INTERFACE_WIDTH_PAYMENT_CLOSED_AUTHOR_PROVED_REVIEW_PENDING','supersedes':[{'claim_id':old['claim_id'],'version':1,'scope':'Improved actual-bad-node payment interface; original V envelope remains valid and its obstruction is preserved'}],'refutes':[],'first_unproved_line':None,'next_consumers':['A040','A021','A023','A025','A050','A064','A087','A092','B10','B20']}
dump(ROOT/'CLAIMS.json',[old,claim])
report=r'''# exact target, quantifiers, hypotheses and units

A046/B10 stage 5 closes the saved width-dependent actual-bad-layer payment target for the existing compatible three-event controller. For arbitrary positive point widths s,L,R,T and any independent BALANCED Boolean core g, set F=1+[WUV OR S(U OR V)](g-1). Query S until failure or completion, resolve the corresponding WUV or U OR V controller, and stop at a constant or g. All laws are uniform physical cube laws; entropy is bits. A strictly K=4-bad node has B_i>4 Inf_i and costs I(child_product)/2. The entire terminal pi H(g) remains present. Full FEI remains OPEN.

The new exact result is Q_bad,controller-prefix<=5 I(F) uniformly in all block widths and core dimension. If min(R,T)>=4 the actual controller-prefix bill is exactly zero, for every s,L. An improved constant-row proof gives B_i/Inf_i<1781/480 whenever event-difference density e<=1/8. This removes the previous logarithmic controller-width dependence in this interface; it does not supply an arbitrary-core entropy certificate or prescribed spectral-reference bank.

# sources actually read, revisions and theorem locators

Read BOARD.md, supervisor snapshot 2026-10-14 04:19 UTC; B10 lead notes v2, 2026-10-11 23:31Z; own rolling status; complete execution protocol 2026-10-11-execution-v2. The lead's old A046 scalar task was completed earlier; this stage resumes the saved actual late-layer target after consuming the new independent review. Earlier campaign and supplied-paper context remains the source history of the completed stages; no external theorem, literature claim, web research or brain mutation is used.

Read A040 run 20261014T033148Z REPORT.md/CLAIMS.json: it independently accepts A046 v1 without repair and proves that the old cutoff envelope still has V/I~log(width). Read A021 run 20261014T011316Z REPORT.md: bounded-contrast all-width K7 closure and its explicit still-open K4 interface. The board lists a newer A021 run; its REPORT.md was not yet available at the checked path, so no result from it was imported. Read A023 run 20261014T022245Z REPORT.md: once-owned whole-block shared-data payment, terminal fractions and the unresolved nested reuse. Own stage-4 PROOF, grouped helper and independent review record supply the accepted cutoff/account interface. SOURCE_MANIFEST.json records inspected bytes; source receipts are not new theorem acceptances.

This consumes A040's objection rather than attempting a larger constant for the false old envelope. A025's earlier unfiltered-reserve no-go and A021's existing K7 entropy bound are not repeated as new results.

# complete derivation or exact first unsupported line

PROOF.md contains the full all-dimensional derivation. Let q=2^-R,r=2^-T,eta=2^-(L+R+T), beta=q+r-qr,e=beta-eta. The underlying switch branches are G=1+WUV(g-1), H=1+(U OR V)(g-1). Balance gives EG=1-eta, EH=1-beta, Pr(G!=H)=e/2. At a live point query let rho=2^{-(j-1)} and d=rho e/2. Nonempty residual-selector frequencies contribute exactly 2(1-rho)d to erasure. For empty residual-selector frequencies the paired coefficients are u_T=Ghat(T)+rho Delta_T/2, v_T=-rho Delta_T/2, Delta=Hhat-Ghat.

Separating the FULL constant data row gives u_0=1-eta-d and v_0=d. On every nonconstant data row, including controller and arbitrary core frequencies, exact Boolean/Parseval identities yield

    sum Ghat^2=2eta-eta^2,
    sum Ghat Delta=-eta e,
    sum Delta^2=2e-e^2.

Hence the exceptional nonconstant total and derivative masses are exactly q_*=2eta-eta^2-rho eta e+rho^2(e-e^2/2) and b_*=rho^2 e(2-e)/4. In particular q_*<=2eta+rho^2 e. Binary entropy remainder and log-sum, with theta=eta/e, give

    B_j/d <=2+rho log2(euler/(2-e))
               +rho log2(1+2theta/rho^2)
               +d log2(euler/d^2).

Compatible nested events imply eta<=8e^2/25: writing t=sqrt(qr)<=1/2, e>=2t-(3/2)t^2>=(5/4)t and eta<=t^2/2. For e<=1/8, c=1/ln2<3/2 and euler<11/4 imply the three variable terms above are strictly below 2/3, 9/20 and 19/32 respectively. The middle bound follows from ln(1+x^2)<=x, giving rho log2(1+2theta/rho^2)<=c sqrt(2theta)<(6/5)sqrt(e)<9/20. The last bound uses d<=1/16 and monotonicity of d log2(euler/d^2). Thus B_j/d<1781/480<4 at EVERY layer, even as disagreement tends to zero. Since min(R,T)>=4 implies e<=q+r<=1/8, those cases need no separator reserve at all.

For the remaining widths min(R,T)<=3, the independently accepted v1 cutoff gives at most m=ceil(log2(min(R,T)+2))+2<=5 eligible layers. Put m_*=0 in the wide-block rare regime and m_*=m otherwise. With alpha=2^-s, JB=(L+R+T)eta, JC=R q(1-r)+T r(1-q), JD=JB+JC and pi=eta+alpha e, retain the exact accounts I_sep=s alpha e, I_other=(1-alpha)JB+alpha JC and I_terminal=pi I(g). The modified reserve

    W_j=2^-j[M_j JD+e M_j(M_j-1)/2+M_j e I(g)],
    M_j=min(j,m_*), W_0=0,

is set to zero on separator failure. Its physical drift W_j-W_(j-1)/2 is the actual face cost c_j=2^-j[JD+(j-1)e+e I(g)] when j<=m_* and zero otherwise. All potentially bad queries are covered by that drift. No budget is recreated; early successes may raise the reserve but have zero expected release. Finite summation and alpha JD<=I_other give

    Q_bad<=W_s<=5 I_other+2 I_sep+5 I_terminal<=5 I(F).

The point-conjunction/union descendants remain good by the accepted v1 scope, so this is the complete controller-prefix price. The full terminal-inclusive entropy ledger is H(F)<=(4+2/ln2)(I_sep+I_other)+W_s+pi H(g). If a core rate C0 is separately certified, the conclusion is H(F)<=max(9+2/ln2,C0+5)I(F). The new advance is K4 localized payment, not an improved class entropy constant over A021's already-paid K7 route.

For A040's explicit width-obstruction family w=2^h-2, all h>=3 have min(R,T)>=4 and hence actual prefix bill zero. Its ORIGINAL V envelope still has V/I~log2(w); the reviewed obstruction remains intact. W filters those already-good faces out instead of increasing their allowance. This is not an FEI counterexample or a reversal of Q_bad<=V.

The root-compatible signed output/spectral correction remains C_T=J_tree-[h2(pi/2)-pi] as in the prior stage. It is neither canceled nor paid by this new row bound, and prescribed witness conditioning and reference resets are additional obligations. First unsupported universal line: transport an actual-bad debit through a general shared-data or interleaved data/selector history using genuinely unused child surplus, including balance loss, all inherited terminals and the prescribed-reference correction. The key eta<=8e^2/25 relies on this nested compatible geometry; a large-contrast bent/point-flip branch pair need not satisfy it.

Known falsifiers rejected before computation: a uniform bound for the same old V cutoff envelope is now source-refuted by A040; all-layer full-face reservation is retired by A025; tax-free J<=M and universal O(p) taxes remain false; essential contraction does not pay sharp tax; free output/spectral-bank exchange and dropped terminal entropy remain invalid. No unchanged numerical repair was searched.

# executed validation with domain, arithmetic, commands and outputs

All three specifications were frozen before their jobs, each job was sequential and under 60 seconds, and no job was expected above 300 MB. Memory estimates were 90 MB, 25 MB and 100 MB; no heavy-job memok gate was triggered. No GPU, background job, random sampling or automatic dimension escalation.

Commands, relative to the A046 folder:

    python -X utf8 runs\20261014T041928Z-account05-A046-current-candidate-intake\code\check.py
    python -X utf8 runs\20261014T041928Z-account05-A046-current-candidate-intake\code\accounts.py
    python -X utf8 runs\20261014T041928Z-account05-A046-current-candidate-intake\code\direct.py

All PASS. Spectral job: 18 actual grouped nodes, j in {1,2,4}, L in {1,3}, (R,T) in {(4,4),(4,8),(8,16)}, 126 recorded assertions, 0.2227853 seconds. Maximum declared physical dimension 32. It checks both nonconstant masses exactly, reconstructs the constant/nonconstant split, compares actual queried influence and certifies B/d<1781/480. Exact Fourier category multiplicity is 2^width-1, justified by point-indicator coefficients; this does not collapse the fair physical coordinates to biased gates. Fraction masses and rational 24-term atanh enclosures certify entropy signs. Per-node results are flushed immediately.

Account job: 3,072 formal rational ledgers s=1..8,L=1..3,R,T=1..8 independently, core influence {1,5/2}; 13,824 exact drift identities and 16,896 recorded assertions, 0.2801446 seconds. It checks the piecewise reserve, its drift and absolute root cap. These are algebraic account checks, not Boolean spectrum searches.

Independent representation job: 16 explicit actual Boolean truth tables using core z or non-flat balanced Maj3, j in {1,2}, L=1 and (R,T) in {(1,1),(1,2),(2,2),(4,4)}; maximum dimension 14. Integer FWHT, direct physical flips and exact rational prime-log vectors verify equality with the grouped erasure law, without importing the grouped transform. PASS: 36 recorded assertions in 0.1979704 seconds. Log-vector equality is sufficient exact evidence; no independence of prime logarithms is assumed. This is a separate implementation by the same author, not independent-agent acceptance of v2. Total: 17,058 recorded exact assertions. The all-width theorem rests on the analytic proof, not the finite domain.

# proof dependencies and changed downstream conclusions

CLAIMS.json consumes the full A040 independent HOLDS record for A046 v1, preserving its statement, hash, contributors and review. A046-SEPARATOR-LAYER-CUTOFF-RESERVE v2 extends that existing interface with actual-row filtering and uniform width payment; its dependency on v1 is explicit and acyclic. New v2 is author-proved, pending independent challenge. A040's old-envelope obstruction is consumed as a source-bound objection and remains valid; it is not independently accepted in its entirety here. No broad new universal potential is opened.

Changed downstream conclusion: the previously unpaid controller-width dependence of the actual K4 bill is closed for all compatible three-event blocks with balanced independent core. A040/A023/A025 can delete every wide-private-block separator charge and use at most five owned layers for the remaining widths. Arbitrary stopped-core entropy, common-reference resets and nested shared-data bank ownership remain unpaid. A021's broader biased-core K7 theorem is unchanged and is not promoted to a K4 claim. No shared index or another agent's folder was edited.

# one next mathematical action and independent reviewer

NEXT: after the first actual core-coordinate reveal while this selector is unresolved, derive the conditional constant/nonconstant moments for both biased child cores and test the remaining W account without replenishing its terminal-coordinate capacity. Retain the original child reach weights, complete terminal Fourier laws, consumed core influence and signed root/witness correction. This is the first interleaved-history step not covered by balance, and builds toward general shared-data ownership instead of enlarging a now-closed width census. A040/A087 should independently review the rare-row proof and piecewise reserve; A092 should challenge the reference-side conditioning scope. Saved metadata is a handoff, not a sent message.

# actual persistence receipts or precise save blocker

All four protocol files, PROOF.md, code, three frozen specs, exact outputs, source hashes, schema checks and local artifact receipts are saved in the assigned stage directory. PROGRESS.json and PACKET_DELTA.json are byte-identical with packet_ids=[A046]. STATUS.md has exactly STATE/NEXT lines; WORKLOG.md and LEARNED.md are appended. All files are below 20 MB and all writes remain inside A046. No Git, external message, brain mutation or foreign-folder write occurred. Independent review of v2, canonical adoption, supervisor copying and remote mirrors remain unverified.

# Universal bridge

This stage moves C019 localized stopping-tree payment by closing the controller-width gap in the existing three-event separator mechanism: actual K4 bad-prefix cost is at most 5I for all widths, and it is zero when both private widths are at least four. The constant-row bound B/d<1781/480, once-owned piecewise drift and complete pi H(g) terminal ledger are proved analytically and checked by 17,058 recorded exact assertions. The old envelope obstruction remains true, and no universal FEI constant or prescribed-reference payment is established. NEXT addresses balance loss at the first interleaved core reveal with the same unused capacities, the shortest unresolved ownership step toward a general restriction theorem rather than another isolated family census.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B10','packet_id':'A046','gap_id':'G-C019-MULTILAYER-SEPARATOR-OWNERSHIP','attempt_id':'A046-stage5-actual-row-filter-1','method':'Consume independent v1 review and envelope obstruction; split full constant Fourier row; analytic rare-event geometry; exact piecewise reserve transport; direct non-flat-core reproduction','mathematical_delta':'A046 v2 closes actual K4 controller-prefix price uniformly in all widths: Qbad<=5I; zero when min(R,T)>=4; B/d<1781/480 for e<=1/8; 17058 recorded exact assertions PASS; terminal and reference costs retained','deliverable_status':'COMPLETE_LOCAL_EXISTING_INTERFACE_CLOSURE_REVIEW_PENDING','mathematical_status':'WIDTH_UNIFORM_ACTUAL_BAD_PREFIX_PAYMENT_PROVED; UNIVERSAL_FEI_OPEN','claim_versions_used':[{'claim_id':old['claim_id'],'version':1,'statement_sha256':old['statement_sha256'],'scope':'Full A040 independent acceptance consumed'},'A040-CUTOFF-ENVELOPE-WIDTH-OBSTRUCTION@1 (source-bound obstruction, unchanged)','A021 stage4 bounded-contrast K7 result (scope context only)','A023 stage4 whole-block marked terminal payment (next-gap context only)'],'claims_created_or_changed':['A046-SEPARATOR-LAYER-CUTOFF-RESERVE@1 independent review adopted locally','A046-SEPARATOR-LAYER-CUTOFF-RESERVE@2 actual width-payment closure'],'source_artifacts':['PROOF.md','REPORT.md','CLAIMS.json','code/check.py','code/accounts.py','code/direct.py','out/FROZEN_SPEC.json','out/ACCOUNT_SPEC.json','out/DIRECT_SPEC.json','out/SPECTRAL_CHECK.json','out/ACCOUNT_CHECK.json','out/DIRECT_CHECK.json','out/SOURCE_MANIFEST.json'],'next_consumers':['A040','A021','A023','A025','A050','A064','A087','A092','B10','B20'],'next_action':'Derive biased child-core constant/nonconstant moments after first real core query inside unresolved separator, with actual remaining W account, original physical weights and full terminal/reference costs','stagnant_substantive_attempts':0,'blockers':['Independent v2 review pending','Interleaved balance-loss and general shared-data terminal surplus remain unpaid','Prescribed witness/reset funding and full FEI remain open','Canonical adoption and mirror receipts unobserved'],'packet_ids':['A046']}
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
sources=[BASE/'BOARD.md',BASE/'claude'/'B10'/'STREAM_NOTES.md',src40/'REPORT.md',src40/'CLAIMS.json',src21/'REPORT.md',src23/'REPORT.md',ROOT.parent/'20261014T012528Z-account05-A046-current-candidate-intake'/'PROOF.md',ROOT.parent/'20261014T012528Z-account05-A046-current-candidate-intake'/'code'/'layers.py',Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
dump(ROOT/'out'/'SOURCE_MANIFEST.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Inspection/reconstruction scope explicitly limited in REPORT; receipt is not theorem acceptance'} for p in sources])
(HOME/'STATUS.md').write_text('STATE: A046 stage 5 complete: all-width actual K4 controller-prefix Qbad<=5I proved; zero at min(R,T)>=4 via B/d<1781/480; 17,058 recorded exact assertions PASS; v2 review pending, FEI OPEN.\nNEXT: Derive first interleaved core-query biased child moments with remaining W capacity, original reaches, terminal spectra and signed reference costs; A040/A087/A092 review rare-row proof.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-14 stage 5 '+ROOT.name+': consumed A040 full independent v1 acceptance and its valid old-envelope obstruction. Full constant-row split proves every rare compatible-switch layer K4-good; min private width>=4 gives zero prefix charge, otherwise at most five old-cutoff layers. Existing claim extended to v2 Qbad<=5I with all pi H(g) retained. Spectral/account/direct non-flat-core checks PASS, 17058 recorded assertions. No full FEI or free witness bank claimed.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage 5 durable: A040 independently accepted A046 v1 without repair; original V envelope still has log-width obstruction. For balanced compatible overlap, eta<=8e^2/25; separating full constant row gives Qnon=2eta-eta^2-rho eta e+rho^2(e-e^2/2), bnon=rho^2 e(2-e)/4. Thus e<=1/8 forces B/d<1781/480 at every layer. Set eligible count zero at min(R,T)>=4, previous cutoff otherwise (<=5); actual prefix Qbad<=5I all widths. This does not extend unconditionally to biased/core-revealed or large-contrast rows. Terminal pi H(g) and signed/reference resets remain visible; next interleaved data reveal consumes inherited capacity once.\n')
protocol=json.loads(sources[-1].read_text(encoding='utf-8-sig'))
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
for cl in (old,claim):assert set(cl)==set(protocol['required_per_run']['claim_fields'])
for title in protocol['required_per_run']['report_fields']:assert '# '+title in report
assert report.strip().split('\n\n')[-2]=='# Universal bridge'
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((HOME/'STATUS.md').read_text().splitlines())==2
stats=[json.loads((ROOT/'out'/f).read_text()) for f in ('SPECTRAL_CHECK.json','ACCOUNT_CHECK.json','DIRECT_CHECK.json')]
assert all(x['status']=='PASS' for x in stats)
assert sum(x['recorded_assertions'] for x in stats)==17058
dump(ROOT/'out'/'SCHEMA_CHECK.json',{'status':'PASS','new_statement_sha256':digest,'recorded_assertions':17058,'fields_exact':True,'progress_copy_identical':True,'source_review_consumed_without_repair':True,'universal_bridge_final':True})
receipts=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
dump(ROOT/'out'/'PERSISTENCE_RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','files_saved':len(receipts)+1,'recorded_assertions':17058,'full_fei':'OPEN'}))
