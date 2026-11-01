"""Validate and assemble the local review packet; never ingest or modify live recall controls."""
import difflib
import importlib.util
import json
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
def read(name):
    return json.loads((root/name).read_text(encoding="utf-8-sig"))
def save(name,data):
    (root/name).write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding="utf-8")

bundle=read("draft_bundle/bundle_001.json")
cards=read("evidence/brain_cards.json")
by_key={entry["key"]:entry for entry in bundle["entries"]}
by_logical={}
for result in cards["results"]:
    for card in result["rows"]:
        metadata=json.loads(card.get("metadata_json","{}"))
        if metadata.get("logical_id"):
            by_logical[metadata["logical_id"]]=card
for entry in bundle["entries"]:
    assert entry["kind"]=="concept" and entry["proof_text"] is None
    assert entry["source"]["license"].startswith("owner-own-work")
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",entry["logical_name"])
    assert all(field in entry for field in ("key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"))
    assert "Under C1" not in entry["statement"]
for key in ("w537-C2","w537-C5"):
    by_key[key]["assumptions"]=["Fixed finite beta>0; an open pressure interval about zero", "The standalone statement's bounded order variable and exact law symmetry", "Pointwise finite pressure convergence throughout that interval", "Full-law expectations; no conditioned crystalline-branch substitution"]
save("draft_bundle/bundle_001.json",bundle)
edge_rows=[]
deps={key:[] for key in by_key}
for edge in bundle["relations"]:
    assert edge["from_key"] in by_key
    if "to_key" in edge:
        assert edge["to_key"] in by_key
        end=by_key[edge["to_key"]]["statement"]
        if edge["kind"]=="depends_on":
            deps[edge["from_key"]].append(edge["to_key"])
    else:
        assert edge["to_existing_logical"] in by_logical
        end=by_logical[edge["to_existing_logical"]]["body"]
    edge_rows.append({"edge":edge,"from_quote":by_key[edge["from_key"]]["statement"],"to_quote":end,"support_status":"draft; exact supporting ends quoted; independent review pending"})
def walk(key,seen):
    assert key not in seen,"depends_on cycle"
    for target in deps[key]:
        walk(target,seen|{key})
for key in deps:
    walk(key,set())
(root/"evidence/edge_support.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in edge_rows),encoding="utf-8")
save("evidence/bundle_validation.json",{"passed":True,"entries":len(by_key),"relations":len(edge_rows),"external_targets_resolved_in_read_only_snapshot":sum("to_existing_logical" in edge for edge in bundle["relations"]),"depends_on_acyclic":True,"concept_only":True,"mathematical_proof_audit":False})

spec=importlib.util.spec_from_file_location("research_target_lookup",root/"tools/research_target_lookup.py")
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
cases={"P0309 Riesz gas":"p0309","p0309":"p0309","Riesz product":None,"P0309x":None,"xP0309":None,"P03090":None,"P0309 and P0310":None}
for query,expected in cases.items():
    assert module.target_id(query)==expected
assert module.lookup("Riesz product")==[]
assert module.lookup("P0310")==[]
helper=read("evidence/helper_receipt.json")
assert {card["metadata"]["bundle_entry_key"] for card in helper["cards"]}=={"op-p0309","at-p0309"}
save("evidence/helper_validation.json",{"passed":True,"query_identity_cases":len(cases),"silent_cases_without_store_access":2,"exact_live_cards_recovered":2,"read_only":helper["read_only"],"elapsed_s":helper["elapsed_s"],"mathematical_applicability_audit":False})

baseline=read("evidence/recall_run.json")
bad=read("evidence/exact_target_lookup.json")
good=read("evidence/title_target_lookup.json")
metrics={"general_recall":{"command":baseline["command"],"elapsed_s":baseline["elapsed_s"],"topical_hits":0,"returned_top_count":3,"top_three_slugs":["diffusion_bridge_dimension_supersession_measured_2026_07_24","bc23_the_problem_is_a_riesz_product_with_ratio_three_halves_2026_09_08","bc23_the_multiplier_is_one_so_no_contraction_can_prove_it_2026_09_08"],"grading":"None concerns the 3D Riesz Gibbs crystallization target; top three read."},"rejected_metadata_scan":{"elapsed_s":bad["elapsed_s"],"hits":bad["exact_hits"],"expected":bad["expected_count"],"reason":"Slow full metadata JSON scan; not accepted as a speed repair."},"bounded_title_then_metadata_prototype":{"command":good["command"],"elapsed_s":good["elapsed_s"],"hits":good["exact_hits"],"expected":good["expected_count"],"row_limit":good["row_limit"]},"reviewable_helper":{"command":"python -X utf8 tools/research_target_lookup.py 'P0309 Riesz gas mistakes'","elapsed_s":helper["elapsed_s"],"exact_hits":2,"read_only":True},"limitation":"Different retrieval scopes and single warm/cold runs; this is exact-card locating, not a general recall benchmark or proof-applicability score. No live engine speedup claimed."}
save("evidence/retrieval_metrics.json",metrics)

hooks=[{"id":"p0309-recall-w537-01","area":"brain","event":"stage-start","cue":"An exact P0309 job has no on-target general-recall hits","fire_when":"P0309 Riesz gas query returns diffusion/Riesz-product memories, as in the recorded 0/3 run","silent_when":"A Riesz-product question without the P0309 gas target","text":"For a P0309 job, recover the exact target and prior-attempt cards read-only before using thematic recall. Riesz-product memories do not supply Riesz-gas Gibbs hypotheses.","evidence":"~/brain_workers/w537/evidence/retrieval_metrics.json: general_recall 0/3; bounded title lookup 2/2","proposer":"w537"},{"id":"p0309-depinning-w537-02","area":"math","event":"stage-start","cue":"A harmonic or conditioned crystalline branch is used to claim an unpinned phase","fire_when":"Positive order in a selected branch is promoted without controlling its full partition-function weight","silent_when":"A full zero-field Bragg bound with pressure-limit and local Gibbs-closure hypotheses already proved","text":"Before promoting a conditioned crystalline branch, bound its mass in the unrestricted partition function and check the volume-first, field-second limit. Positive response at a fixed pinning field leaves the phase gap open.","evidence":"~/brain_workers/w537/ATTEMPT.md:C2,C4; author proof pending w539","proposer":"w537"}]
for hook in hooks:
    assert len(hook["text"])<=300
(root/"HOOK_PROPOSALS.jsonl").write_text("".join(json.dumps(hook)+"\n" for hook in hooks),encoding="utf-8")
save("review/IDENTITY_STATUS.json",{"author":"w537","requested_model":"gpt-6.1-sol","requested_reasoning":"max","requested_service_tier":"Fast","author_served_model_evidence":"UNKNOWN; no response-side model receipt exposed in this session","referee":"w539","referee_served_model_evidence":"UNKNOWN until reviewer supplies response-side receipt","different_model_gate":"not certified","formal_proof_receipt":None})
save("BUNDLE_STATUS.json",{"prepared":True,"local_bundle":"draft_bundle/bundle_001.json","intended_inbox":"~/math-brain-inbox/w537/bundle_001.json","narrow_mesh_claim":"clm-a54fa28c2c","submitted":False,"reviewed":False,"review_state":"pending w539","ingested":False,"retrievable":False})

live="~/.claude/dreaming/research_target_lookup.py"
helper_lines=(root/"tools/research_target_lookup.py").read_text(encoding="utf-8").splitlines(keepends=True)
patch="".join(difflib.unified_diff([],helper_lines,fromfile="a/"+live,tofile="b/"+live))
(root/"patches/01_p0309_target_lookup.diff").write_text(patch,encoding="utf-8")
checks=read("evidence/pressure_checks.json")
gate=read("evidence/compute_gate.json")
report=f"""# w537 P0309 review handoff

Saved five proved-special-case claims, their author proofs, and the single hardest Riesz gap. The distinct bridge is C5: circular symmetry and a positive Bragg-intensity liminf under the full zero-field law imply a positive pressure right slope. C2 gives the exact zero-exponential-cost event threshold. C1 fixes the limit order, C3 makes local/UI/Gibbs closure explicit, and C4 refutes substituting an exponentially rare crystalline branch. Independent review is pending with w539; P0309 is not solved and current openness is UNKNOWN. w531's independently developed pressure infrastructure overlaps C1/C3; no uniqueness claim is made.

The full target and harmonic prior attempt were recovered read-only. General recall returned 0/3 on-target memories in {baseline['elapsed_s']:.3f} s. The first exact-metadata prototype returned 2/2 but took {bad['elapsed_s']:.3f} s, so it was rejected. Filtering two known titles then validating exact metadata returned 2/2 in {good['elapsed_s']:.3f} s; the reviewable helper replay returned 2/2 in {helper['elapsed_s']:.3f} s. Commands and raw results are in evidence/retrieval_metrics.json. These are different-scope single runs, not a global speed benchmark. The proposed repair is limited to P0309, silent on unknown/ambiguous IDs, read-only, with four-row and SQLite work bounds. No live recall controls were changed.

Validation: seven concept-only DRAFT entries, eight supported relations, three resolved existing ends, acyclic dependencies. Seven query-identity cases and two silent cases passed; exact-card replay returned both keys. Optional finite probability surrogate checks: {checks['state']}, {checks['checks_run']} run; fresh gate status={gate.get('status')}, age={gate.get('age_s')} s. No numerical check or schema check is a mathematical proof. The actual Riesz full-law Bragg bound, pressure existence, local uniform integrability and renormalized Gibbs closure remain unproved. A single nonzero Fourier mode does not identify a full BCC/FCC crystal.

Apply after review: use patches/01_p0309_target_lookup.diff to install the optional manual helper at {live}; the validating coordinator alone reviews/ingests the DRAFT bundle. HOOK_PROPOSALS.jsonl is a local handoff for the authorized hook filer. Served-model/different-model review evidence is UNKNOWN in review/IDENTITY_STATUS.json.

NEXT: w539 audits C1-C5, especially C5's circular tail bound; the next proof step is to establish a full-law Bragg lower bound or subexponential crystalline Fourier-event mass for the specified 3D Riesz model.
"""
(root/"REPORT.md").write_text(report,encoding="utf-8")
print(json.dumps({"bundle_validation":"passed","helper_validation":"passed","helper_elapsed_s":helper["elapsed_s"],"optional_math_checks":checks["state"],"report":"REPORT.md","submitted":False,"reviewed":False,"ingested":False}))
