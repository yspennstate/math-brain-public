from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
attempt = root/'ATTEMPT.md'
text = attempt.read_text(encoding='utf-8')
text = text.replace('The primary Anderson definition', 'For the primary variance-one uniform law use V=sqrt(3)U, U uniform[-1,1], hence the coupling in the formulas below is sqrt(3) times that primary coupling. Reversing unit hopping is a bipartite unitary conjugacy; a convention adding 6 times the identity requires the corresponding energy shift. The primary Anderson definition')
attempt.write_text(text, encoding='utf-8')

audit = root/'CORE_AUDIT.md'
text = audit.read_text(encoding='utf-8').replace('Verdict so far:', 'Verdict:')
text = text.replace('L5 (portion inspected):', 'L5:')
text = text.replace('Complete the remaining tail of this item before freezing the final audit.', 'The tail also checks: eta_k=N_k^(-1/2)>=3^(-k), and the off-diagonal lower bound diverges as N_k^((1-alpha)/2) while the diagonal tends to zero.')
text = text.replace('NEXT: Finish the short tail of L5, freeze this direct verdict with the audited file hash, and send w483 the cavity estimate as a disjoint sharper premise.', 'The directly audited snapshot is review/w483_ATTEMPT_snapshot.md, SHA256 4f99ebdf4c964aacc446b9399db3eab0b6edcecf85ad00534470ccd9c9867338 (12629 bytes). This scoped Codex audit does not supply different-model served-identity evidence.\n\nNEXT: Prove or refute the uniform resonant inverse-cavity estimate for the actual fixed-disorder lattice; it can complement w483\'s weighted-pair criterion. GOE requires a separate argument.')
audit.write_text(text, encoding='utf-8')

status = {
 'target_id':'C0056', 'worker':'w484', 'date':'2026-10-10',
 'title':'Extended states for the three-dimensional Anderson model at weak disorder',
 'current_openness':'UNKNOWN',
 'current_openness_reason':'2018 and 2026 survey statements describe the classical gap, but a September 23, 2026 public manuscript claims its resolution. That complete proof has not been independently audited here; no novelty claim is made.',
 'exact_intake_statement':'Prove existence of absolutely continuous spectrum (delocalised states) for the random Schrodinger operator -Delta + lambda V on Z^3 at small disorder lambda, and GOE local statistics for its finite-volume restriction.',
 'intake':{'path':'~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl','line':56,'result_status':'attempted_unsolved','verification':'unreviewed'},
 'primary_model':{'operator':'Discrete unit nearest-neighbor hopping plus lambda V on l^2(Z^3); sign is unitarily equivalent on the bipartite lattice','law':'iid real centered variance-one potentials in Bourgade Section 2.1','volume':'periodic boxes in the GOE paragraph','unfixed_details':['choice of single-site law beyond moments','exact bulk interval','density unfolding and GOE convergence mode']},
 'working_slice':{'operator':'A+g U, unit adjacency A, iid U uniform[-1,1]','coupling':'g fixed positive; g=sqrt(3)*lambda for the variance-one uniform law','spectral_interval':'fixed bounded open I','parent_goal_proved':False,'GOE_goal_proved':False},
 'primary_sources':[
  {'id':'bourgade_band_icm_2018','url':'https://arxiv.org/pdf/1807.03031','locator':'Section 2.1, printed p.7; PDF page index 6','indexed_pdf_sha256':'b8b15c02ac7b675471097e9c499a6d588cfd7b0c591c49b0135f2a42eaedddb0','hash_check':'hash reported in intake sources.jsonl:7; not recomputed locally','statement_check':'primary definition, periodic restrictions and distinct AC/GOE obligations inspected'},
  {'id':'stolz-2011','url':'https://arxiv.org/pdf/1104.2317','locator':'Sections 2 and 9.2','use':'operator and spectral-type definitions; historical gap only'},
  {'id':'yau-icm-2026','url':'https://epubs.siam.org/doi/10.1137/25M1806028','locator':'Introduction and Section 3.4, Theorem 3.6','use':'current-year survey distinguishes ordinary lattice gap from GUE block Anderson results with growing block width; not a proof for scalar iid Z^3'},
  {'id':'becker-oltman-2026','url':'https://arxiv.org/html/2609.20798v1','locator':'Introduction model definition','use':'hyperbolic product graph differs from Z^3; no transfer asserted'},
  {'id':'public-claimed-anderson-proof-20260923','url':'https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/02-state.tex','locator':'Finite-volume certificate proposition','use':'primary manuscript claims a weak-disorder result with true iid uniform potentials; proof not adopted as established'},
  {'id':'public-formalization-scope-261','url':'https://raw.githubusercontent.com/openai/math/main/lean/docs/261.md','locator':'Scope','use':'formalization scope identifies a two-dimensional spectral set, not the three-dimensional AC conclusion; no formal-check receipt issued'}
 ],
 'prior_attempt':{'path':'~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl','line':45,'method':'tree transfer and finite kinetic-time route','result':'no result; tree geometry and infinite-time gap'},
 'additional_prior_checks':{'attempts_H_I_and_lean':'targeted C0056/Anderson search found only the dated annotated ranking, no target proof','team_O':'board read; no C0056 row assigned there','owner_solved_registers':'no C0056/Anderson solution found in the two named registers; not a comprehensive retirement certificate'},
 'brain_recall':{'result':'timeout at 60 seconds','fallback':'targeted memory index had no match; read explicitly named perceptron and derived-joint-structure scars'},
 'paired_proof_read':True,
 'independent_derivation_saved_first':True,
 'paired_proof_snapshot':'~/brain_workers/w484/review/w483_ATTEMPT_snapshot.md',
 'paired_proof_sha256':'4f99ebdf4c964aacc446b9399db3eab0b6edcecf85ad00534470ccd9c9867338',
 'served_model_evidence':{'author':'unavailable; requested settings are not evidence','referee':'pending response-side evidence'},
 'formal_check':{'run':False,'parent_theorem_certified':False,'trusted_axioms':'no receipt issued'},
 'submission_state':'prepared locally; publish receipt pending','review_state':'w485 requested; mathematical review pending','ingestion_state':'not ingested','retrieval_state':'not verified'
}
(root/'SOURCE_STATUS.json').write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8')

def entry(key, logical, title, statement, assumptions):
 return {'key':key,'namespace':'probability.random-operators','logical_name':logical,'kind':'concept','title':title,
         'statement':statement,'proof_text':None,'assumptions':assumptions,'domain':'probability theory; spectral theory',
         'source':{'source_id':'owner-own-work:w484:C0056:'+key,'url':attempt.as_uri(),'revision':'2026-10-10-independent-unreviewed','license':'owner-own-work (campaign derivation; pending independent review)','excerpt':None}}

bundle = {'spec':'mathbrain-draft-v1','author_agent':'w484','bundle_slug':'c0056-poisson-cavity-obstructions-w484-001','entries':[
 entry('atomic','annealed-poisson-bound-does-not-imply-sample-absolute-continuity','Draft obstruction: smooth average, atomic samples',
  'DRAFT, independent review pending. For D on l^2(Z^3) with D delta_x=U_x delta_x and iid U_x uniform[-1,1], every sample has a complete eigenbasis. For u_eta(E)=pi^(-1) Im <delta_0,(D-E-i eta)^(-1)delta_0>, sup_{eta>0,E} E u_eta(E)<=1/2, but each local spectral measure is delta_{U_x}. Ward identity also holds. For every sample integral_R u_eta(E)^2 dE=1/(2 pi eta). This refutes an inference from annealed first moments to sample absolute continuity. Zero hopping excludes this example from the unit-hopping Anderson target.',
  ['eta>0','zero hopping','iid uniform[-1,1] potentials','resolvent (H-z)^(-1)']),
 entry('compactness','poisson-lp-compactness-criterion-draft','Draft criterion: Poisson Lp control at fixed disorder',
  'DRAFT sufficient criterion, independent review pending. For a measurable random probability measure mu, a fixed bounded open interval I, 1<p<infinity, and eta_n->0, the bound sup_n E integral_I (P_eta_n*mu)^p dE<infinity implies an Lp(I) density almost surely. Fatou and pathwise weak compactness identify that density against compactly supported tests. Stationarity and a countable site intersection extend this conclusion to all lattice basis spectral measures. The premise is unproved for weak-disorder Z^3, and nonzero mass in I must be established separately. The p=1 variant is false. No GOE assertion follows.',
  ['mu is a positive probability measure','fixed bounded open I','1<p<infinity','eta_n tends to zero','stationarity for all-site transfer','fixed positive disorder']),
 entry('cavity','anderson-single-site-cavity-second-moment-gap-draft','Draft reduction: resonant inverse cavity response',
  'DRAFT conditional reduction, independent review pending. For H=A+lambda V on Z^3, unit adjacency A, lambda>0 and bounded iid potentials with density rho bounded by M, remove site 0 and write Sigma=<h,(H^(0)-E-i eta)^(-1)h>, a=E+Re Sigma and b=eta+Im Sigma>0. The exact Schur complement gives G_00=(lambda V_0-a-i b)^(-1). Conditioning only on sites other than 0 yields E[(Im G_00/pi)^2|cavity]<=M/(2 pi lambda b). A uniform expected integral of b^(-1) along eta_n->0 is sufficient for the Poisson L2 criterion. If V_0 is uniform[-1,1], the same second moment is >=1/(4 lambda pi^2 b) on {|a|+b<=lambda}. Control of these resonant small-b environments is unproved. The six cavity neighbors need not be independent.',
  ['eta>0','fixed lambda>0','bounded iid potentials','bounded density rho','single-site independence from the cavity','uniform[-1,1] only for lower bound']),
 entry('scope','c0056-spectral-and-goe-obligations-separated-draft','Draft scope: C0056 has two proof obligations',
  'DRAFT scope note. The C0056 intake requests both weak-disorder absolutely continuous spectrum on Z^3 and GOE local statistics of finite-volume bulk eigenvalues. The independent Poisson/cavity route supplies conditional spectral reductions only. Its uniform inverse-cavity estimate is unproved and its GOE branch is untouched. The dated attempted_unsolved label does not certify current openness; a September 2026 public proof claim remains unaudited here. Current openness UNKNOWN; no novelty or solved claim.',
  ['intake C0056 at problems.jsonl:56','historical sources are dated','no complete current-status certification'])
 ],'relations':[
  {'from_key':'cavity','to_key':'compactness','kind':'depends_on','rationale':'The second-moment upper bound plus uniform expected inverse-b energy control gives exactly the p=2 premise of the conditional compactness criterion; that uniform control remains open.'},
  {'from_key':'atomic','to_key':'compactness','kind':'semantic_association','rationale':'The atomic example satisfies first-moment control but has Poisson L2 norm 1/(2 pi eta), so it tests the failed p=1 weakening of the criterion.'},
  {'from_key':'scope','to_key':'cavity','kind':'semantic_association','rationale':'The cavity route covers only the spectral obligation and explicitly leaves both its hard estimate and GOE unresolved.'}
 ]}
(root/'DRAFT_BUNDLE.json').write_text(json.dumps(bundle,indent=2)+'\n',encoding='utf-8')

hook = {'id':'poisson-w484-01','area':'math','event':'stage-start',
 'cue':'An argument infers sample absolute continuity from a bounded disorder-averaged Poisson/resolvent density',
 'fire_when':'A proof uses a Wegner or annealed first-moment bound to conclude almost-sure AC spectrum without a uniform-integrability argument',
 'silent_when':'Uniform expected integrated Lp control with p>1, fixed disorder and eta->0 is proved and used via valid compactness',
 'text':'A smooth disorder average can hide atomic sample spectra. Test a random point mass. To infer almost-sure AC from Poisson densities, derive the needed uniform integrability as eta tends to zero at fixed disorder; a first-moment bound alone is insufficient.',
 'evidence':'~/brain_workers/w484/ATTEMPT.md:L01; MEASUREMENTS.json: L2 norm grows by 10000 while mean density remains <=1/2',
 'proposer':'w484'}
assert len(hook['text']) <= 300
(root/'HOOK_PROPOSAL.jsonl').write_text(json.dumps(hook)+'\n',encoding='utf-8')
patch_dir=root/'patches'; patch_dir.mkdir(exist_ok=True)
live='~/primary_directive/hooks1000/proposals/math-w484.jsonl'
patch='--- a/'+live+'\n+++ b/'+live+'\n@@ -0,0 +1 @@\n+'+json.dumps(hook)+'\n'
(patch_dir/'01_poisson_first_moment_hook.diff').write_text(patch,encoding='utf-8')

claim_file=root/'CLAIMS.jsonl'
claims=[json.loads(line) for line in claim_file.read_text(encoding='utf-8').splitlines() if line.strip()]
if not any(row['id']=='w484-C0056-A01' for row in claims):
 with claim_file.open('a',encoding='utf-8') as handle:
  handle.write(json.dumps({'id':'w484-C0056-A01','kind':'direct-audit','statement':'KEEP w483 L1-L5 as scoped conditional spectral reductions and an abstract obstruction. The volume- and scale-uniform marked pair-concentration bound for the true fixed-disorder Z^3 operator is unproved; nonzero AC mass and GOE remain separate obligations.','assumptions':['bounded iid uniform-law slice','fixed eta before volume limit','uniform pair bound explicitly assumed, not proved'],'source':{'path':'~/brain_workers/w484/review/w483_ATTEMPT_snapshot.md','sha256':'4f99ebdf4c964aacc446b9399db3eab0b6edcecf85ad00534470ccd9c9867338','author':'w483'},'proof_or_counterexample':'Direct constants, conditioning, volume-limit and Cantor-bound checks in CORE_AUDIT.md; independent L01-L03 were saved first.','independent_reviewer':{'agent':'w484','state':'scoped Codex direct audit; different-model served-evidence gate not satisfied'},'remaining_gap':'Uniform weighted-pair concentration and uniform resonant inverse-cavity control on the target. No parent promotion.','status':'sketch'})+'\n')

print('PREPARED',len(bundle['entries']),'draft concepts;',len(bundle['relations']),'supported relations; hook kept local with application diff')
