"""Build isolated review artifacts and the explicitly requested DRAFT inbox file.

No integration command is run. All mathematical entries remain concepts until
the assigned referee approves them. Hashes here identify evidence files only,
not a store seal, signed manifest or proof certificate.
"""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import sqlite3

root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument("--publish-draft",action="store_true")
args=parser.parse_args()
def dump(name,value):
    (root/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
cards=json.loads((root/"target_cards.json").read_text(encoding="utf-8"))["rows"]
by_key={row["metadata"]["bundle_entry_key"]:row for row in cards}
parent=by_key["op-c0047"]
attempt=by_key["at-c0047"]
paired=Path("~/brain_workers/w561/ATTEMPT.md")
paired_body=paired.read_bytes()
(root/"W561_ATTEMPT_SNAPSHOT.md").write_bytes(paired_body)
dump("PAIRED_PROOF_RECEIPT.json",{"source":str(paired),"snapshot":"W561_ATTEMPT_SNAPSHOT.md","sha256":hashlib.sha256(paired_body).hexdigest(),"scope":"L01-L05 only; conditional KEEP, not parent-problem verification","independent_obstruction_precedes_read":True,"formal_check":False})
db=Path("~/math-brain-build/local/population/brain.sqlite3")
with sqlite3.connect(db.as_uri()+"?mode=ro",uri=True,timeout=1)as con:
    con.row_factory=sqlite3.Row
    row=con.execute("SELECT id,title,body,metadata_json FROM nodes WHERE id=?",("claim_a856b6832eb14a549e1823bdee33fbdf",)).fetchone()
    if row:
        returned=dict(row);returned["metadata"]=json.loads(returned.pop("metadata_json"));dump("RETURNED_SPECTRAL_CARD.json",returned)
        print("Returned generic card:",returned["title"],returned["body"])

norm_statement="DRAFT source-backed correction, pending referee check. In an infinite connected d-regular Cayley graph let rho be the normalized simple-random-walk spectral radius, so the adjacency norm is d*rho. The classical sufficient condition for bond nonuniqueness is p_c*d*rho<1: choose a supercritical p with p*d*rho<1, bound the connection kernel by the all-walk Neumann series, and exclude uniqueness by FKG. The degree-free p_c<1/rho condition in C0047-A001 is automatic when 0<rho<1 and p_c<=1, and is not that sufficient theorem. The correct condition is not necessary: on T4, p_c=1/3, rho=sqrt(3)/2 and p_u=1, while p_c*d*rho>1. This correction does not solve C0047."
overlap_statement="DRAFT refuted-route record, pending referee check. Under iid Bernoulli(p) bond percolation on Cay(F(a,b),{a,a^-1,b,b^-1}), let A and B indicate all-open routes (e,a,a^2) and (e,a,ab). For 0<p<1, P(A)=P(B)=p^2 and P(A and B)=p^3. Compared with iid Bernoulli(p^2) indicators the intersection probability is larger, while the union probability 2p^2-p^3 is smaller than 2p^2-p^4. Thus neither stochastic domination direction holds with that iid law. Replacing added-generator edges by overlapping paths cannot retain iid p^2 solely from its marginals."
coupling_statement="DRAFT candidate bridge, not a certified theorem. Let G,H be countable connected locally finite simple undirected graphs on the same vertex set. Fix for every H-edge h a simple G-path P_h joining its endpoints, with length <=L, and suppose each G-edge lies in <=M routes, for integers L,M>=1. For p in [0,1], set t=1-(1-p)^(1/M), q=t^L. Assign distinct independent Bernoulli(t) slots to routes at every base edge; OR M slots to realize iid G-percolation at p, and independently thin shorter route indicators to obtain iid H-percolation at q. This couples every H-open route inside a G-open path, hence p_c^bond(G)<=1-(1-(p_c^bond(H))^(1/L))^M. The written countable-product proof in bridge_derivation.md awaits w563. This transfers existence only; different H-clusters may merge in G."
gap_statement="DRAFT missing-premise record. For the prescribed Cayley graph, bounded critical connection operator T_{p_c} on counting-measure l2 would yield a strict operator interval above p_c via Russo/BK continuation; uniqueness is excluded there by FKG. The w561 packet proves this conditional implication but does not establish the critical bound. A September 24, 2026 public manuscript states the critical bound in Theorem 1.1 and every fixed finite symmetric generating set in Corollary 1.2; its 53-page proof is not certified by this packet. In the distinct bounded-congestion routing approach, the missing step is prevention of extra base-open edges merging the infinite routed clusters. Current openness is UNKNOWN here; no parent-solved or novelty claim."
def entry(key,logical,title,statement,assumptions,evidence):
    return {"key":key,"namespace":"probability.percolation","logical_name":logical,"kind":"concept","title":title,"statement":statement,"proof_text":None,"assumptions":assumptions,"domain":"Bernoulli bond percolation on graphs","source":{"source_id":"owner-campaign:C0047:w562:"+key,"url":"file:///~/brain_workers/w562/"+evidence,"revision":"candidate-2026-10-10; pending independent referee w563","license":"owner-own-work (campaign derivation or refuted route; unreviewed)","excerpt":None}}
entries=[
entry("spectral-normalization","benjamini-schramm-spectral-normalization-warning","DRAFT: degree factor in the C0047 spectral criterion",norm_statement,["Normalized random-walk rho","Infinite connected d-regular Cayley graph","Sufficient criterion, not equivalence"],"ATTEMPT.md"),
entry("overlap-obstruction","cayley-generator-path-indicators-overlap-obstruction","DRAFT: overlapping generator paths are not iid",overlap_statement,["iid Bernoulli base edges","0<p<1","Specified F(a,b) routes"],"independent_obstruction.md"),
entry("slot-coupling","bounded-congestion-path-slot-coupling-candidate","DRAFT: independent slots repair path routing with a probability penalty",coupling_statement,["Same countable vertex set","Connected locally finite simple undirected graphs","Fixed simple routes","Uniform length L>=1","Uniform congestion M>=1"],"bridge_derivation.md"),
entry("remaining-gap","c0047-critical-operator-and-routing-merger-gap","DRAFT: exact remaining C0047 bridge premises",gap_statement,["No novelty or global proof status certification","Fixed prescribed generating set","Bond model"],"AUDIT_W561.md")]
relations=[
{"from_key":"spectral-normalization","to_existing_logical":attempt["metadata"]["logical_id"],"kind":"refutes","rationale":"Refutes only the quoted degree-free sufficient-criterion route in the unreviewed attempt, not the entire record or parent conjecture. Primary Theorem 4 uses rho*k*p<1."},
{"from_key":"overlap-obstruction","to_existing_logical":parent["metadata"]["logical_id"],"kind":"semantic_association","rationale":"Records an obstruction to changing-generating-set transfer in the fixed-Cayley-graph target; it refutes no parent statement."},
{"from_key":"slot-coupling","to_key":"overlap-obstruction","kind":"semantic_association","rationale":"The candidate slot construction repairs the dependence exposed by the two specified overlapping paths, at a parameter penalty; it does not preserve their infinite-cluster separation."},
{"from_key":"remaining-gap","to_key":"slot-coupling","kind":"semantic_association","rationale":"States the precise lack of a merger bound after existence is coupled; no implication to a nonuniqueness theorem is asserted."},
{"from_key":"remaining-gap","to_existing_logical":parent["metadata"]["logical_id"],"kind":"semantic_association","rationale":"Separates the conditional operator route and recent unrefereed primary claim from a certified resolution of C0047."}]
bundle={"spec":"mathbrain-draft-v1","author_agent":"w562","bundle_slug":"c0047-w562-bridge-adversary-001","entries":entries,"relations":relations}
for e in entries:
    assert e["kind"]=="concept"and e["proof_text"]is None and e["source"]["license"].startswith("owner-own-work")
keys={e["key"]for e in entries}
assert len(entries)==len(keys)<=200
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
for relation in relations:
    assert relation["from_key"]in keys and relation["kind"]in allowed
    assert ("to_key"in relation) != ("to_existing_logical"in relation)
    if "to_key"in relation:assert relation["to_key"]in keys
draft=root/"draft_bundle_001.json"
draft.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
edge_rows=[]
entry_by_key={e["key"]:e for e in entries}
existing={attempt["metadata"]["logical_id"]:attempt,parent["metadata"]["logical_id"]:parent}
for number,relation in enumerate(relations,1):
    from_entry=entry_by_key[relation["from_key"]]
    target=entry_by_key[relation["to_key"]]if "to_key"in relation else existing[relation["to_existing_logical"]]
    edge_rows.append({"edge_id":f"S1.w562.E{number:03}","relation":relation,"from_quote":from_entry["statement"],"to_quote":target.get("statement",target.get("body")),"to_digest":target.get("digest"),"status":"DRAFT; independent review pending","reviewer":"w563"})
(root/"EDGE_AUDIT.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n"for row in edge_rows),encoding="utf-8")
hook={"id":"spectral-normalization-w562-01","area":"math","event":"stage-start","cue":"Percolation proof uses a spectral-radius criterion or transfers iid edges to overlapping replacement paths","fire_when":"C0047-A001 uses normalized rho in p_c<1/rho, or generator a^2/ab path indicators are multiplied as independent","silent_when":"The calculation explicitly uses adjacency norm d*rho and BK/disjoint supports or a verified slot coupling","text":"Check spectral normalization and the joint law before importing a percolation criterion: normalized rho requires the degree factor; overlapping replacement paths need a valid coupling or disjoint-occurrence bound. Marginals alone do not transfer nonuniqueness.","evidence":"CLAIMS.jsonl S1.w562.002-.003; target_cards.json; overlap_measurement.json; perceptron_proof_open_gaps_fleet_2026_07_12","proposer":"w562"}
assert len(hook["text"])<=300
(root/"HOOK_PROPOSALS.jsonl").write_text(json.dumps(hook,ensure_ascii=False)+"\n",encoding="utf-8")
patches=root/"patches";patches.mkdir(exist_ok=True)
source=root/"proposed/math_brain/target_fallback.py"
live="~/math-brain-build/src/math_brain/target_fallback.py"
diff="".join(difflib.unified_diff([],source.read_text(encoding="utf-8").splitlines(keepends=True),fromfile="a/"+live,tofile="b/"+live))
(patches/"01_candidate_target_fallback.diff").write_text(diff,encoding="utf-8")
status=json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
status["intake_primary"]={"url":"https://arxiv.org/pdf/1712.04651","title":"Sixty years of percolation","location":"Conjecture 2, page 4","model":"Bernoulli bond","local_extract":"~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/raw/duminil_copin_icm_2018_statements.txt","statement_verified":True}
status["recent_claim"].update({"statement_verified":True,"proof_verified":False,"exact_location":"Theorem 1.1 pp.3-4; Corollary 1.2 p.4; critical-bound argument Section 9 pp.45-47","pdf_sha256":sha(root/"recent_nonuniqueness.pdf"),"full_hypotheses":["Infinite connected locally finite undirected graph","Quasi-transitive","Positive vertex Cheeger constant","iid Bernoulli bond percolation","Counting measure l2"],"critical_claim":"sup_{0<=p<p_c}||T_p||=||T_{p_c}||<infinity and p_c<p_{2->2}<=p_u","validation_scope":"Statement, strategy, final conditional passage and endpoint lemma read; Sections 3-8 not fully referee-checked. A public claim does not alone prove or retire the problem."})
status["owner_solved_retired_check"]="Exact C0047 and percolation/nonamenability searches in named H/I prior-attempt folders returned no additional target record. September intake/Lean annotation remains attempted_un. Owner-folder filename search for percolation/Benjamini/Schramm/C0047 returned no matching path. Bounded search, not a complete retirement audit."
dump("SOURCE_STATUS.json",status)
dump("MODEL_PROVENANCE.json",{"agent_id":"w562","native_thread_id":"not exposed in this tool context; preserve this thread","requested_model":"gpt-6.1-sol","requested_reasoning":"max","requested_tier":"Fast","served_model":"UNKNOWN","response_side_identity_evidence":"Unavailable; requested settings, profiles and self-report do not establish served model.","subagents_started":0,"formal_proof_receipt":{"performed":False,"theorem":None,"assumptions":None,"trusted_axioms":None,"admitted_placeholder_counts_as_proof":False}})
receipt={"prepared":True,"prepared_path":str(draft),"submitted":False,"reviewed":False,"ingested":False,"retrievable":False,"draft_schema_structural_check":"PASS (local, not integrator attestation)","entries":len(entries),"relations":len(relations),"reviewer":"w563","live_store_changed":False}
if args.publish_draft:
    inbox=Path("~/math-brain-inbox/w562")
    inbox.mkdir(parents=True,exist_ok=True)
    final=inbox/"bundle_001.json"
    body=draft.read_bytes()
    if final.exists():
        if final.read_bytes()!=body:raise FileExistsError("Refusing to overwrite a different existing draft")
    else:
        part=inbox/"bundle_001.part"
        if part.exists():raise FileExistsError("Refusing to overwrite an existing .part")
        part.write_bytes(body)
        part.rename(final)
    receipt.update({"submitted":True,"submitted_path":str(final),"submission_kind":"DRAFT inbox placement only; no integration command"})
dump("BUNDLE_RECEIPT.json",receipt)
dump("ARTIFACT_HASHES.json",{str(p.relative_to(root)):sha(p)for p in [draft,root/"SOURCE_STATUS.json",root/"ATTEMPT.md",root/"bridge_derivation.md",root/"AUDIT_W561.md",root/"CLAIMS.jsonl",root/"EDGE_AUDIT.jsonl",root/"fallback_measurement.json",root/"overlap_measurement.json",root/"pivotal_measurement.json",patches/"01_candidate_target_fallback.diff"]})
print(json.dumps(receipt,indent=2));print("Draft bundle sha256",sha(draft))
