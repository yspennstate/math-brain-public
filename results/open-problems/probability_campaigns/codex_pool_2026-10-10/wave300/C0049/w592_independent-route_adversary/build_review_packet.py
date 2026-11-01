"""Prepare local evidence and explicitly authorized concept-only inbox material."""
from pathlib import Path
import hashlib
import json
import sqlite3
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parent
stamp=datetime.now(timezone.utc).isoformat()
def write(name, obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

op_id='claim_347e594687b6554f3064529196a1a3a40b60b0076bb44dfa5593974e31ea4f4c'
at_id='claim_3908da7919a7318bc7b220dc189ceb958a0b62e279555dd907896a7f04d7bf77'
canonical=[]
for candidate in [Path('~/math-research-brain/local/population/brain.sqlite3'),
                  Path('~/math-research-brain/local/brain.sqlite3'),
                  Path('~/math-brain-build/local/population/brain.sqlite3')]:
    if not candidate.is_file():
        canonical.append({'path':str(candidate),'state':'not found at exact named candidate path'})
        continue
    try:
        with sqlite3.connect(candidate.as_uri()+'?mode=ro',uri=True,timeout=5) as db:
            tables={r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            matches=[]
            for table in ['nodes','claims']:
                if table not in tables:
                    continue
                columns={r[1] for r in db.execute('PRAGMA table_info('+table+')')}
                if 'id' not in columns:
                    continue
                wanted=[c for c in ['id','kind','title','body','payload_json','digest'] if c in columns]
                rows=db.execute('SELECT '+','.join(wanted)+' FROM '+table+' WHERE id IN (?,?)',(op_id,at_id)).fetchall()
                for row in rows:
                    matches.append({'table':table,**dict(zip(wanted,row))})
            canonical.append({'path':str(candidate),'state':'read-only exact-ID query complete','matches':matches})
    except sqlite3.Error as e:
        canonical.append({'path':str(candidate),'state':'read-only query unavailable','reason':str(e)})
write('STORE_EVIDENCE.json',canonical)

peer_path=Path('~/brain_workers/w591/ATTEMPT.md')
peer_bytes=peer_path.read_bytes()
(ROOT/'PEER_PROOF_SNAPSHOT.md').write_bytes(peer_bytes)

source_status={
 'target':'C0049','exact_statement_recovered':True,
 'statement':'Fix 0<q<=4 and p=p_c(q). For square-lattice Dobrushin domains (Omega_delta,a_delta,b_delta) approximating a simply connected domain with two marked boundary points, the FK exploration path is conjectured to converge weakly to chordal SLE with kappa=4*pi/(pi-arccos(sqrt(q)/2)). The assigned target excludes q=2.',
 'topology_note':'Conjecture 3 does not itself spell out the full curve topology/prime-end approximation convention; any proof must state these. ATTEMPT.md supplies a proposed Jordan-domain formulation, not a stronger source attribution.',
 'q_less_than_one_note':'The finite identities hold for q>0. Do not infer p_c=p_sd or RSW for q<1 from q>=1 theorems.',
 'current_openness':'UNKNOWN','novelty_claim':False,
 'sources':[
  {'source_id':'duminil_copin_ising_potts_2017','url':'https://www.ihes.fr/~/duminil/publi/2017PIMS.pdf','locator':'Conjecture 3, printed p.93, zero-based PDF page 92','checked':'exact primary statement and adjacent sufficient observable route','excerpt':'the previous conjecture would follow from the convergence of vertex parafermionic observables'},
  {'source_id':'smirnov_icm_2006','url':'https://www.unige.ch/~smirnov/papers/icm-publ.pdf','locator':'Conjecture 4, printed p.1429, zero-based PDF page 8','checked':'square-lattice loop/Dobrushin formulation and equivalent kappa formula'},
  {'source_id':'averous_et_al_fk4_20261006','url':'https://unige.ch/~duminil/publi/2026%20conformal%20invariance%20FK%20q=4.pdf','date_on_pdf':'2026-10-06','locator':'Theorem 1.2, printed p.4, zero-based PDF page 3','checked':'q=4,p=2/3,free boundary loop convergence to CLE(4), Caratheodory approximation, Camia-Newman topology','chordal_transfer':'not certified by this audit; no full C0049 retirement','arxiv_id':'not verified; author page used a placeholder'},
  {'source_id':'dst_2015','url':'https://arxiv.org/abs/1505.04159','checked':'abstract scope q in [1,4] and RSW; no extrapolation below 1'}],
 'prior_work':{
  'intake_record':'~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl:49',
  'attempt_record':'~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl:39',
  'earlier_method':'parafermionic observable and missing full discrete relations',
  'H_I_search':'No C0049 or FK/SLE/P0124 exact text match returned from scoped H/I searches; not a corpus-wide novelty check.',
  'lean_search':'C0049 only in annotated ranked list; no exact C0049 Lean theorem found in the scoped scan.',
  'owner_solved_retired_search':'No exact C0049/P0124/random-cluster-SLE hit returned in the permitted notes/research directories; current solved/retired status remains UNKNOWN.',
  'team_O':'C0049 absent from Team O board; P0124 assigned to w341.',
  'export_ids':[op_id,at_id],
  'canonical_exact_id_receipt':'STORE_EVIDENCE.json',
  'duplication_note':'Finite next-edge connectivity dependence already appears in the P0124 attempt; no novelty claimed for that diagnostic.'},
 'independence':{'independent_file':'ATTEMPT.md','written_before_paired_statement_read':True,
                 'paired_statement':'~/brain_workers/w591/STATEMENT_FOR_ADVERSARY.md',
                 'paired_proof_at_first_read':'ATTEMPT.md was a placeholder; returned a separately derived proof of the frozen statement',
                 'paired_proof_read_after_independent_derivation':True,
                 'paired_proof_snapshot':'PEER_PROOF_SNAPSHOT.md',
                 'paired_proof_sha256':hashlib.sha256(peer_bytes).hexdigest()},
 'served_identity':{'requested_model':'gpt-6.1-sol','requested_reasoning':'max','requested_tier':'Fast','response_side_evidence':'unavailable','author_served_model':'UNKNOWN','referee_served_model':'UNKNOWN'},
 'mathematical_review':{'referee':'w593','state':'requested, pending','independent_referee_for_new_referee_results':'w596'},
 'last_updated':stamp}
write('SOURCE_STATUS.json',source_status)

def entry(key,logical,title,statement,assumptions):
    return {'key':key,'namespace':'probability.statmech','logical_name':logical,'kind':'concept',
     'title':'DRAFT: '+title,'statement':'DRAFT, independent mathematical review pending. '+statement,
     'proof_text':None,'assumptions':assumptions,'domain':'probability theory',
     'source':{'source_id':'owner-own-work:w592:c0049-audit:'+key,'url':None,
               'revision':'2026-10-10-review-pending','license':'owner-own-work (original campaign derivation or source-scope audit; not a claim of mathematical novelty)',
               'excerpt':None}}
entries=[
 entry('wiring','fk-boundary-wiring-density-draft','Boundary wiring density and its q=1 degeneracy',
  'On a finite FK graph with fixed edge probabilities, q>0 and boundary partition xi, merging u,v gives R=Z_eta/Z_xi=1/q+(1-1/q)*P_xi(u connected to v). For a common predictable edge-revelation filtration, the density is D_n=[1/q+(1-1/q)*P_xi(u connected to v|F_n)]/R. At q=1 it is identically one, so this density alone supplies no Loewner variance constraint.',
  ['Finite graph; 0<p_e<1; q>0','Count every connected component, including identified boundary components','Same edge factors and same predictable revelation rule']),
 entry('two-profile','loewner-two-profile-identification-draft','Two profiles identify a localized Loewner driver',
  'Let continuous adapted W_0=0 drive dg_t(z)=2/(g_t(z)-W_t)dt. For 0<x1<x2<y, set X_i=g_t(x_i)-W_t,Y=g_t(y)-W_t,U_i=X_i/Y. Stop before swallowing and localize with positive X_i,Y and U_i in compact subsets of (0,1). For kappa>0 let H prime be u^(-4/kappa)(1-u)^(8/kappa-2). If both H(U_i) are continuous local martingales in the same filtration, the independent calculation recovers W as a semimartingale and gives zero drift and bracket kappa dt on that stopped interval. This supplies no FK profile convergence theorem.',
  ['Capacity normalization 2','Two distinct ordered marked points','Common filtration and compact unswallowed localization','Conclusion only on the stopped interval']),
 entry('one-profile','loewner-one-profile-constant-ratio-counterexample-draft','One profile does not identify the driver',
  'For 0<x<y and t<xy/4, the smooth deterministic driver W_t=(x+y)(1-sqrt(1-4t/(xy))) has Loewner images with X_t=x*sqrt(1-4t/(xy)) and Y_t=y*sqrt(1-4t/(xy)). Therefore U_t=x/y is constant and every finite H(U_t) is a local martingale, while W has nonzero finite variation and bracket zero. The second independent observable in the two-profile criterion cannot simply be dropped.',
  ['Stop strictly before xy/4','H is finite at x/y','Counterexample targets a one-profile inference, not the actual two-profile criterion']),
 entry('profile-gap','fk-random-slit-profile-convergence-obligation-draft','The unresolved input in a boundary-event SLE route',
  'The proposed boundary-event route requires two actual FK observables converging jointly with the exploration to the specified conformal profiles, uniformly in localized random slit domains, with a justified limiting-filtration martingale argument and coverage beyond fixed marked-point swallowing. Finite domain Markov and partition identities give martingales without identifying their profiles. The parent C0049 statement remains unproved in this packet.',
  ['Conjectural FK-to-profile input','No theorem promotion from finite enumeration']),
 entry('source-scope','fk-q-four-loop-versus-chordal-source-audit-draft','q=4 loop convergence source scope',
  'A source-scope audit of Averous et al. (October 6, 2026), Theorem 1.2, finds a free-boundary q=4,p=2/3 FK loop convergence theorem to CLE(4) in simply connected square-lattice domains with Caratheodory approximation and Camia-Newman topology. A marked Dobrushin chordal-path limit requires a separate justified transfer. Preserve that distinction when updating the dated C0049 card; this packet makes no blanket retirement claim.',
  ['Original audit of the cited primary theorem','Separate chordal transfer not established here']),
 entry('route-scope','fk-parafermionic-route-sufficient-not-necessary-draft','A sufficient route is not an equivalence',
  'The 2017 lecture after Conjecture 3 provides a sufficient implication from parafermionic observable convergence to interface convergence. The old C0049 attempt says the problem is reduced exactly to finding an additional discrete relation; the cited source does not establish necessity of that method. Retain alternative approaches while recording their own precise gaps.',
  ['Source-scope audit of C0049-A001','No completed alternate FK proof claimed'])]
relations=[
 {'from_key':'one-profile','to_key':'two-profile','kind':'semantic_association','rationale':'The one-profile card says "the second independent observable ... cannot simply be dropped"; the two-profile card explicitly requires "two distinct ordered marked points". The counterexample does not refute the stated two-profile criterion.'},
 {'from_key':'profile-gap','to_key':'two-profile','kind':'depends_on','rationale':'The gap card requires "two actual FK observables" converging to the "specified conformal profiles"; the conditional driver criterion begins "If both H(U_i) are continuous local martingales".'},
 {'from_key':'profile-gap','to_key':'wiring','kind':'semantic_association','rationale':'The gap card distinguishes finite martingales from identified profiles; the wiring card states that q=1 density is "identically one".'},
 {'from_key':'source-scope','to_existing_logical':'math:probability.statmech:open-problem-c0049-convergence-of-random-cluster-interfaces-to-sle-kappa-for-q-in-0-4-q-n','kind':'semantic_association','rationale':'Existing C0049 node names Dobrushin exploration convergence; this audit records that the October 6 theorem is a free-boundary loop theorem. No relation asserts a full solution.'},
 {'from_key':'route-scope','to_existing_logical':'math:probability.statmech:attempt-c0049-convergence-of-random-cluster-interfaces-to-sle-kappa-for-q-in-0-4-q-n','kind':'semantic_association','rationale':'The exact existing attempt says "reduced ... exactly to finding an additional discrete relation"; the primary source says only that the conjecture would follow from observable convergence.'}]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w592','bundle_slug':'c0049-driver-and-scope-audit-001','entries':entries,'relations':relations}
write('bundle_001.json',bundle)

# Explicit task output exception. Never ingest, seal, deploy, or write the live store.
inbox=Path('~/math-brain-inbox/w592')
inbox.mkdir(parents=True,exist_ok=True)
final=inbox/'bundle_001.json'
content=(ROOT/'bundle_001.json').read_bytes()
if final.exists():
    assert final.read_bytes()==content,'Existing inbox draft differs; do not overwrite it.'
else:
    part=inbox/'bundle_001.json.part'
    with part.open('xb') as handle:
        handle.write(content)
    part.rename(final)

write('BRAIN_HANDOFF.json',{
 'draft_path':str(final),'entry_count':len(entries),'relation_count':len(relations),
 'state':{'prepared':True,'submitted':True,'reviewed':False,'ingested':False,'retrievable':False},
 'review_gate':'All entries are concept/draft material; mathematical claims require w593 review and valid served-model evidence before any theorem promotion.',
 'license':'owner-own-work','integration_owner':'validating coordinator','time':stamp})
hook={'id':'fk-wiring-w592-01','area':'math','event':'stage-start',
 'cue':'A proof uses an FK boundary-wiring density alone to identify a q=1 Loewner driver.',
 'fire_when':'A q=1 SLE argument infers its Brownian variance solely from a boundary-wiring Radon-Nikodym martingale.',
 'silent_when':'A separate nonconstant observable and its required conformal profile theorem are supplied, or the missing profile is explicitly left open.',
 'text':'An FK boundary-wiring density is constant at q=1. Name a nonconstant geometric observable and prove its conformal profile before using this route to identify the Loewner variance.',
 'evidence':'~/brain_workers/w592/MEASUREMENTS.json: 5576 q=1 history checks; CLAIMS.jsonl w592-C0049-O1; memory gist_proven_means_every_step_2026_07_21',
 'proposer':'w592'}
(ROOT/'HOOK_PROPOSAL.jsonl').write_text(json.dumps(hook)+'\n',encoding='utf-8')

claims=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
required={'statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status'}
allowed_status={'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
assert len({c['claim_id'] for c in claims})==len(claims)
for c in claims:
    assert required<=c.keys() and c['status'] in allowed_status
keys={e['key'] for e in entries}
for e in entries:
    assert e['kind']=='concept' and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
for relation in relations:
    assert relation['from_key'] in keys
    assert relation.get('to_key') in keys or 'to_existing_logical' in relation
assert len(hook['text'])<=300
assert len(entries)<=200
write('VALIDATION.json',{'claims':len(claims),'draft_entries':len(entries),'relations':len(relations),
      'concept_only':True,'schema_shape_checks':'passed','mathematical_review':'pending',
      'hook_text_characters':len(hook['text']),'inbox_matches_local_copy':final.read_bytes()==content,
      'command':'python -X utf8 ~/brain_workers/w592/build_review_packet.py',
      'scope':'shape/transport checks only; not a mathematical proof or cryptographic bundle manifest'})
files=['ATTEMPT.md','ADVERSARIAL_AUDIT.md','CLAIMS.jsonl','SOURCE_STATUS.json','STORE_EVIDENCE.json',
       'MEASUREMENTS.json','check_fk_wiring.py','bundle_001.json','BRAIN_HANDOFF.json','HOOK_PROPOSAL.jsonl','VALIDATION.json',
       'PEER_PROOF_SNAPSHOT.md','REPORT.md','build_review_packet.py']
write('REVIEW_PACKET.json',{'target':'C0049','author':'w592','referee':'w593',
 'verdict':'KEEP localized conditional criterion; reject one-profile identification; HOLD parent FK convergence',
 'hardest_gap':'Two FK conformal profiles uniformly in random slit domains and their limiting-filtration identification.',
 'files':[{'path':str(ROOT/name),'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in files],
 'hash_scope':'Review artifact hashes only. The coordinator owns bundle manifests, seals and all ingestion ceremony.',
 'served_model_evidence':'UNKNOWN for author and referee; requested settings are not receipts.',
 'formal_check_receipt':None,'independent_mathematical_review':'requested, pending',
 'inbox_states':'BRAIN_HANDOFF.json','next':'w593 check the signed-measure proof and deterministic counterexample; coordinator keep concepts draft until review gates pass.',
 'created':stamp})
print(json.dumps({'packet':str(ROOT/'REVIEW_PACKET.json'),'claims':len(claims),'inbox':str(final),
                  'concepts':len(entries),'relations':len(relations),'validation':'passed','canonical_receipt':'STORE_EVIDENCE.json'}))
