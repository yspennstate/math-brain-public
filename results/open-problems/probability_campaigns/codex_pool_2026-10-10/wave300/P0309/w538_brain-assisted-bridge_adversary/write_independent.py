# Independent checkpoint, written before opening any paired prover artifact.
from pathlib import Path
import json
w=Path('~/brain_workers/w538')
text = r'''P0309 independent obstruction and conditional bridge (w538, 2026-10-10)

Independence: This checkpoint was saved before reading any w537 proof or ATTEMPT file. Sources inspected: dated P0309 ranking; Lewin arXiv:2202.09240v2, Definition 15, Section VI opening, and the distinction from Conjectures 35/38. Current openness: UNKNOWN. The ranking and 2022 survey establish only dated provenance. The survey describes a finite-temperature periodic Gibbs phase but does not attach a unique exponent range and full quantifier package to this intake title. Work below is on an explicitly bounded surrogate, not a proof of P0309.

Independent obstruction O1 (exact computation)
For s>0 and x!=0 in R^3, V_s(x)=|x|^{-s} has
D^2 V_s(x)=s|x|^{-s-2}[(s+2)ee^T-I], e=x/|x|.
Its radial eigenvalue is s(s+1)|x|^{-s-2}, but both transverse eigenvalues are -s|x|^{-s-2}. Thus convexity of r -> r^{-s} does not imply convexity in vector displacements. A concrete two-particle path x(t)=(1,t,0) has V_s(x(t))=(1+t^2)^{-s/2} and second derivative at t=0 equal to -s. Any attempt to apply a convex Gibbs variance inequality to the full Riesz energy requires a separately proved lower bound for the assembled Hessian; positivity cannot be obtained term by term. This counterexample does not show that a full lattice Hessian is unstable: other bonds and the background can compensate.

Candidate bridge B1 (conditional special case; pending w539)
Fix any finite nonempty D subset Z^3. On R^{3|D|}, let u=(u_x) and let L_D be the Dirichlet lattice Laplacian: diagonal 6, off-diagonal -1 for nearest neighbors in D, boundary coordinates fixed to zero. Suppose H_D is C^2 on all of R^{3|D|}, even (H_D(-u)=H_D(u)), and
D^2 H_D(u) >= kappa (L_D tensor I_3) for every u,
with the same kappa>0 for all D. Let beta>0 and dP_D=Z_D^{-1} exp(-beta H_D(u)) du. For every nonzero G in 2pi Z^3, set
B_{D,G}=|D|^{-1} sum_{x in D} exp(i G dot (x+u_x)).
Define
C_3=(2pi)^{-3} integral_{[-pi,pi]^3} [2 sum_j(1-cos q_j)]^{-1} dq.
Then C_3 is finite and
Re E B_{D,G} >= 1 - |G|^2 C_3/(2 beta kappa).
Consequently, if a=1-|G|^2 C_3/(2 beta kappa)>0, E|B_{D,G}|^2>=a^2 uniformly in D.

Proof: Strong convexity in each finite D gives integrability and all linear moments; evenness gives E u_x=0. The Brascamp-Lieb variance inequality for the potential beta H_D and f(u)=G dot u_x gives
Var(G dot u_x) <= |G|^2 (L_D^{-1})_{xx}/(beta kappa).
The inverse inequality follows from the assumed matrix lower bound and order reversal of positive definite matrices. The killed simple-random-walk expansion of L_D^{-1} is bounded by the unrestricted Green series; equivalently its diagonal is at most C_3. Finiteness follows from the integrable |q|^{-2} singularity in dimension three. Since cos t >= 1-t^2/2 and e^{iG dot x}=1, averaging over x proves the real-part bound. Jensen gives E|B|^2 >= |EB|^2 >= a^2. No independence among displacements is used. Using 1-cos t >= 2t^2/pi^2 for |t|<=pi and enclosing the Fourier cube in the radius sqrt(3)pi ball also gives the loose explicit bound C_3<=sqrt(3)pi/8.

Hardest missing piece
No argument here establishes the Hessian comparison, centered phase, lattice labeling, or control of vacancies/dislocations under an actual continuum Riesz Gibbs specification. The full interacting Riesz energy is not an even globally convex displacement potential. Conditioning on a defect-free neighborhood changes the measure and is not the unconditioned DLR specification. O1 refutes the automatic transfer of scalar convexity. Even a bound for these labeled finite-volume Fourier observables would still need a justified thermodynamic/DLR limit and an extremal periodic phase. Those are separate missing premises, not conclusions of B1.

Retrieval failure checkpoint
Command: python -X utf8 recall_probe.py. brain.py recall completed in 15.881437 seconds. Its first three hits are Bernoulli-convolution Riesz-product memories, not Riesz-gas theorems (0/3 directly relevant; see brain_recall_receipt.json). The response reports P0309 absent. Proposed bounded repair: recognize the query's explicit Riesz-gas/Gibbs scope, flag product-only matches as a homonym collision, and expose an unresolved target rather than supply these as proof support. Do not silently rerank all uses of the word Riesz. A local replay guard and controls will measure this proposal; no live recall change is authorized.

NEXT: Retrieve the complete Brascamp-Lieb card and compare its hypotheses to B1, then read w537's saved proof and audit its central bridge.
'''
(w/'ATTEMPT.md').write_text(text,encoding='utf-8')
rows=[
 {'id':'w538-S1.2','kind':'refuted_route','statement':'For every s>0 the vector potential V_s(x)=|x|^{-s}, x in R^3 minus {0}, has negative transverse Hessian eigenvalues -s|x|^{-s-2}; scalar radial convexity does not imply the vector convexity needed for a direct Brascamp-Lieb application.','assumptions':['s>0','x!=0','The claim is about individual pair terms, not the total lattice Hessian.'],'source':'owner-own-work; ATTEMPT.md O1','proof_or_counterexample':'D^2 V_s=s|x|^{-s-2}[(s+2)ee^T-I]; x(t)=(1,t,0) has second derivative -s at zero.','independent_reviewer':'w539 (pending)','remaining_gap':'Independent referee check; full collective Hessian not determined.','status':'proved special case'},
 {'id':'w538-S1.3','kind':'conditional_bridge','statement':'For C^2 even H_D on R^{3|D|} with Hessian >= kappa L_D tensor I_3 for every displacement and a uniform kappa>0, the Gibbs measure at beta has Re E B_{D,G}>=1-|G|^2 C_3/(2 beta kappa), for G in 2pi Z^3, where C_3 is the massless lattice Green integral. When the right side a is positive, E|B_{D,G}|^2>=a^2 uniformly in finite D subset Z^3.','assumptions':['D finite nonempty subset Z^3; Dirichlet boundary','beta>0','H_D globally C^2 and even','Uniform all-displacement Hessian comparison','Reference positions x in Z^3 and G in its reciprocal lattice'],'source':'owner-own-work; ATTEMPT.md B1; Brascamp-Lieb theorem pending complete card comparison','proof_or_counterexample':'Brascamp-Lieb linear variance bound, killed-walk Green comparison, cos(t)>=1-t^2/2, Jensen. Full derivation in ATTEMPT.md.','independent_reviewer':'w539 (pending)','remaining_gap':'Referee check; none of the actual Riesz Gibbs Hessian, labeling, defect, centering, or DLR-limit premises has been established.','status':'sketch'},
 {'id':'w538-S1.4','kind':'retrieval_failure','statement':'The saved P0309 Riesz-gas proof-mistakes recall returned three Riesz-product/Bernoulli-convolution hits and zero directly relevant Riesz-gas hits at rank <=3.','assumptions':['Single saved recall on 2026-10-10','Manual topic relevance, not a blind benchmark'],'source':'brain_recall_receipt.json','proof_or_counterexample':'Actual brain.py stdout; elapsed 15.881437 seconds; three returned slugs listed in receipt.','independent_reviewer':'w539 (pending)','remaining_gap':'Evaluate a local scope guard with silent controls; no general recall-quality claim.','status':'numerical evidence'}]
with (w/'CLAIMS.jsonl').open('a',encoding='utf-8') as f:
 for row in rows: f.write(json.dumps(row,ensure_ascii=False)+'\n')
(w/'SOURCE_STATUS.json').write_text(json.dumps({'target':'P0309','title':'Positive-temperature crystalline Gibbs phases for three-dimensional Riesz gases','current_openness':'UNKNOWN','dated_ranking_status':'unsolved on 2026-09-07','primary_source':{'author':'Mathieu Lewin','title':'Coulomb and Riesz gases: The known and the unknown','url':'https://arxiv.org/abs/2202.09240','version':'v2 (30 Apr 2022; PDF dated 3 May 2022)','locations':['Definition 15, p17, short-range DLR','Section VI opening pp59-60, finite-temperature symmetry-breaking formulation','Conjectures 35/38 concern zero-temperature energy/configurations'],'scope_warning':'Intake title does not by itself fix exponent range or canonical/grand-canonical quantifiers. B1 is a labeled finite-volume surrogate only.'},'exact_intake_record':'pending; P0309 title verified in dated ranking and dedup_index, original primary locator not recovered','owner_solved_retired_check':'No P0309 match in targeted H/I/lean search; no certificate of exhaustiveness.','recent_literature_check':'Scoped arXiv query inconclusive; no current novelty claim.','independent_checkpoint':'ATTEMPT.md saved before reading w537','states':{'submitted':False,'reviewed':False,'ingested':False,'retrievable':False}},ensure_ascii=False,indent=2),encoding='utf-8')
(w/'STATUS.md').write_text('STATE: WORKING\nNEXT: Retrieve the full Brascamp-Lieb card, compare hypotheses, and audit w537 after the saved independent checkpoint.\n\n2026-10-10: Saved source row S1.1, transverse Hessian obstruction S1.2, conditional massless variance bridge S1.3, and measured 0/3 relevance failure S1.4. No P0309 solution or live-store change claimed.\n',encoding='utf-8')
print('Saved ATTEMPT.md, SOURCE_STATUS.json, CLAIMS S1.2-S1.4 and STATUS.md before peer-proof access.')
