"""Finalize only worker artifacts and the brief's expressly named DRAFT inbox."""
from pathlib import Path
import datetime as dt
import json

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w409')
now = dt.datetime.now(dt.timezone.utc).isoformat()

status = json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status.update({
 'checked_at_utc': now,
 'current_openness':'UNKNOWN',
 'exact_statement_status':'historical primary statement verified; working Jordan interface and crossing formulations explicit',
 'intake_exact_statement':'Prove that critical bond percolation on Z^2 at p = 1/2 is conformally invariant in the scaling limit (Cardy formula and convergence of interfaces to SLE(6)).',
 'intake_locator':{'path':'~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl','line':17,'verification':'unreviewed intake; primary source independently read'},
 'primary_source':{'source_id':'garban_steif_noise_2012','url':'https://arxiv.org/pdf/1102.5761v3','revision':'v3, 2012-05-29','locator':'Chapter II Section 4, Theorem II.2 and following paragraph; printed pp.23-24, PDF pp.25-26','source_quote':'proving the conformal invariance is still a challenging open problem','scope':'Historical source: triangular site theorem and square-bond open statement. Not a current-status certificate.'},
 'working_scope':{'crossings':'Jordan quads with consistent lattice/boundary arc approximations; crossing AB to CD tends to normalized Cardy C(u) for marks sent to (0,u,1,infinity).','interfaces':'Bounded Jordan D with marked a,b, consistent square-lattice approximations and primal/dual Dobrushin exploration boundary conditions. Medial exploration should converge in law to chordal SLE_6 in the uniform curve metric modulo increasing reparametrization.','full_configuration':'A full joint/CLE scaling limit needs an additional justified interface-to-configuration argument.'},
 'paired_proof_read':True,
 'paired_proof_read_after_independent_rows':['w409-C0017-001','w409-C0017-002','w409-C0017-003'],
 'recent_primary_records':[
   {'url':'https://arxiv.org/abs/2409.03235v6','author':'Wang Zhou','revision':'2024-12-17','checked':'metadata and abstract claim checked; proof NOT audited','scope':'Claims square-bond exploration convergence to SLE_6; does not itself certify proof correctness.'},
   {'url':'https://arxiv.org/pdf/2502.08394v2','author':'Ioan Manolescu','revision':'2025-03-02','locator':'Conjecture 5.1, printed p.51, PDF p.54; Chapter 5 rotational-invariance discussion','checked':'Primary full-plane CLE conjecture and scope distinction read','scope':'Nested full-plane CLE limit is stronger than a single-interface claim; its conjectural status is not a refutation of Zhou.'},
   {'url':'https://arxiv.org/abs/1112.2017v5','revision':'2013-01-10','checked':'Primary preliminary-version and critical-comments notice read; no proof audit'},
   {'url':'https://arxiv.org/pdf/0708.3908v1','locator':'equations (3.2)-(3.4), printed pp.18-19 and square-bond/mixed-model section','checked':'Model-specific cancellation route read; not asserted to transfer to square bonds.'}
 ],
 'prior_checks':[
   {'path':'probability_1000_intake_claude_20260907/attempts.jsonl:17','result':'C0017-A001 is unreviewed and reports no new observable. Its numerical spin convention has not been adopted here.'},
   {'path':'probability_1000_attempts_H_20260912 and probability_1000_attempts_I_20260914','result':'Targeted textual lookup found no C0017 record; no whole-corpus read.'},
   {'path':'prob1000_lean_20260908/RANKED_LIST_2026-09-07_annotated.md:588','result':'attempted_un ranking only; no target formal proof receipt found by exact-ID lookup.'},
   {'path':'~/Big Open problem in probability theory/README.md','result':'This project targets Benjamini-Schramm on nonamenable graphs, a different percolation problem.'},
   {'path':'~/math-brain-build/export/population/nodes.jsonl:272,5279','result':'Exact attempt/target cards exist as unverified concepts; no mathematical certification.'}
 ],
 'pending':['Independent mathematical review of w409 results by w410','Full proof audit of Zhou claim before current openness/resolution can be certified','Actual square-bond summed-defect estimate or stopped Cardy approximation'],
 'claims_are_not_target_proof':True
})
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(status,indent=2,ensure_ascii=False),encoding='utf-8')

source={'source_id':'owner-own-work:w409-c0017-adversary-20261010',
        'url':'urn:probability-research:20261010:w409:c0017-adversary',
        'revision':'w409-independent-draft-v1',
        'license':'owner-own-work; unreviewed campaign mathematics, not promoted to theorem',
        'excerpt':None}

def entry(key,name,title,statement,assumptions):
    return {'key':key,'namespace':'probability.percolation','logical_name':name,
            'kind':'concept','title':title,'statement':'UNREVIEWED DRAFT; independent referee pending. '+statement,
            'proof_text':None,'assumptions':assumptions,'domain':'probability theory and complex analysis','source':dict(source)}

entries=[
 entry('cell-obstruction','square-grid-cell-defects-need-summation-control',
       'Vanishing cell defects can leave a nonzero contour',
       'For f(z)=conjugate(z) on the mesh delta=1/n square grid in [0,1]^2, define I([u,v])=(f(u)+f(v))(v-u)/2. Every counterclockwise cell has contour defect 2i delta^2, tending uniformly to zero, but summing all n^2 cells gives the outer contour integral 2i. Thus boundedness, equicontinuity, convergence and per-cell O(delta^2) or o(1) errors do not imply a holomorphic limit. This is a deterministic counterexample to that inference, not a percolation counterexample.',
       ['Square grid and trapezoidal edge integrals','No percolation-specific observable identity assumed']),
 entry('summed-reduction','compact-nodal-convergence-and-summed-defects-imply-holomorphicity',
       'Conditional contour reduction for a grid observable',
       'Let Omega be open, delta_n tend to zero, and complex nodal functions f_n on Omega intersect delta_n Z^2 converge uniformly at grid nodes on every compact set to continuous f. Let D_n(c) be the counterclockwise trapezoidal edge-integral sum around cell c. If, for every axis-aligned rectangle R compactly contained in Omega and grid rectangle approximants R_n tending to R, the signed sum of D_n(c) over cells of R_n tends to zero, then f is holomorphic. Exact interior-edge cancellation and bounded-perimeter quadrature give zero limiting rectangle integrals; a local rectangular primitive proves holomorphicity. Deriving this summed estimate for an actual square-bond event observable remains unproved here.',
       ['Continuous limit and compact-uniform nodal convergence','Signed summed-defect limit for every fixed compact interior rectangle','No assertion that square-bond percolation satisfies these hypotheses']),
 entry('slit-obligation','square-bond-stopped-cardy-approximation-is-an-unproved-input',
       'Square-bond input required by two Cardy martingales',
       'The conditional two-Cardy-martingale identification route does not prove square-bond conformal invariance by itself. Its model-specific input is a construction of correctly oriented square-bond Doob crossing or exit martingales P_delta,i and, on each nondegenerate stopped exploration interval, an approximation E[sup |P_delta,i-C(X_delta/Y_delta,i)|] tending to zero, together with joint driver/marked-point convergence, compatible limiting filtration and stopping/boundary control. Here C(u) is the normalized integral of [v(1-v)]^(-2/3) from 0 to u. This input is UNPROVED in the reviewed route. Fixed-domain pointwise limits alone cannot justify evaluation at varying random slit domains.',
       ['Actual discrete event and primal/dual boundary convention must be specified','Both martingales use one exploration filtration','Curve-to-driver compatibility and joint convergence are additional obligations'])
]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w409','bundle_slug':'c0017-adversary-summed-defect-001',
        'entries':entries,'relations':[{'from_key':'cell-obstruction','to_key':'summed-reduction',
            'kind':'semantic_association',
            'rationale':'The first entry states "per-cell O(delta^2) or o(1) errors do not imply a holomorphic limit"; the second requires that "the signed sum of D_n(c) over cells of R_n tends to zero". The example isolates the missing summed premise without refuting the conditional reduction.'}]}
local=ROOT/'bundle_001.json'
local.write_text(json.dumps(bundle,indent=2,ensure_ascii=False),encoding='utf-8')
INBOX.mkdir(parents=True,exist_ok=True)
target=INBOX/'bundle_001.json'
if target.exists():
    raise RuntimeError('Named inbox draft already exists: refusing to overwrite')
part=INBOX/'bundle_001.json.part'
if part.exists():
    raise RuntimeError('Named inbox staging file already exists: refusing to overwrite')
part.write_bytes(local.read_bytes())
part.rename(target)
receipt={'submitted':{'status':'complete draft file written','time_utc':now,'path':str(target)},
         'reviewed':{'status':'pending','reviewer':'w410'},
         'ingested':{'status':'not observed; integrator not run by worker'},
         'retrievable':{'status':'not checked; no claim of live-store retrieval'},
         'entry_count':len(entries),'all_entries_are_concepts':True,'mathematical_review_required':True}
(ROOT/'DRAFT_SUBMISSION.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
