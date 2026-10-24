"""Prepare review artifacts; writes only w426 and its explicitly authorized draft inbox."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re
import difflib

ROOT = Path(__file__).resolve().parent
INBOX = Path(r"~\math-brain-inbox\w426")
claims = [json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
receipt = json.loads((ROOT/"VERIFICATION.json").read_text(encoding="utf-8"))
assert receipt["status"] == "PASS"
by_id = {row["id"]: row for row in claims}
source = {"source_id": "owner-own-work:w426-c0023-boundary-20261010",
          "url": "file:///~/brain_workers/w426/ATTEMPT.md",
          "revision": "author-packet-v2-2026-10-10; independent review pending",
          "license": "owner-own-work", "excerpt": None}

names = {
    "L1": ("separator-witness-percolation-gluing", "Separator witness for percolation gluing"),
    "L2": ("finite-forest-arbitrary-relay-percolation-gluing", "Gluing with arbitrary many relays in a finite forest"),
    "L3": ("sharp-finite-forest-near-one-gluing-modulus", "Sharp near-one gluing modulus in finite forests"),
    "B1": ("arbitrary-order-relay-selection-conditioning-counterexample", "Relay selection can destroy terminal connectivity"),
    "B2": ("square-obstruction-to-fixed-relay-witness", "A square prevents a fixed pointwise relay witness")}
standalone = {
    "L1": "Let G be a finite undirected graph with vertices o,b, a nonempty relay set A, a vertex v, and a_star in A. If every o-to-A path and every a_star-to-b path contains v, then in every edge configuration {o connects to A,a_star connects to b} is contained in {o connects to b,o connects to A}. For independent Bernoulli edge states with arbitrary edge probabilities in [0,1], P(o connects to b)>=P(o connects to A)min_{a in A}P(a connects to b). Connection means an open path in G.",
    "L2": "Let G be any finite undirected forest, o,b any vertices, and A any nonempty vertex set. For independent Bernoulli edge states with arbitrary edge probabilities in [0,1], P(o connects to b)>=P(o connects to A)min_{a in A}P(a connects to b). There is also a deterministic a_star in A such that {o connects to A,a_star connects to b} is contained in {o connects to b,o connects to A} in every configuration. Consequently P(o connects to b,o connects to A)>=min_{a in A}P(o connects to A,a connects to b) holds for any edge-state law. The product inequality's coefficient 1 is sharp. Connection means an open path; overlap of terminals and relays, disconnected forests, and o=b are allowed.",
    "L3": "For each epsilon in (0,1), delta_star=1-sqrt(1-epsilon) is the largest delta in (0,1] such that the following implication holds for every finite forest G, independent Bernoulli edge probabilities in [0,1], vertices o,b and nonempty relay set A: if P(o connects to A)>1-delta and P(a connects to b)>1-delta for all a in A, then P(o connects to b)>1-epsilon. A two-edge path rules out every larger delta, so delta_star is also a necessary upper bound on any proposed all-finite-graph modulus. Its sufficiency for arbitrary cyclic graphs is not asserted.",
    "B1": "In independent bond percolation on the path o--a2--a1--b, give successive edges probabilities r,s,t in (0,1) and order A=(a1,a2). Let I be the first member of A connected to o, undefined when o misses A. Then P(I=a2)=r(1-s)>0 but P(a2 connects to b | I=a2)=0<P(a2 connects to b)=st. Moreover P(o connects to b)=rst while sum_{a in A}P(I=a)P(a connects to b)=rst(2-s)>rst. For r=s=t=1/2 these are 1/8 and 3/16. This refutes unconditional substitution or the averaged bridge for arbitrary relay order, without refuting product gluing or claims requiring a nondecreasing terminal-marginal order.",
    "B2": "Let G have vertices o,a1,a2,v,b, exactly the edges o-a1,a1-v,o-a2,a2-v,v-b, and A={a1,a2}. No fixed a_star in A satisfies {o connects to A,a_star connects to b} subset {o connects to b} for every edge configuration. With each independent edge probability 1/2, P(o connects to b)=7/32, P(o connects to A)=3/4, and min_{a in A}P(a connects to b)=9/32, so product gluing still holds with margin 1/128. Thus only a universal deterministic-witness bridge is refuted, not stochastic gluing."}
entries = []
for label, (logical_name, title) in names.items():
    row = by_id["w426-C0023-"+label]
    entries.append({"key": label.lower(), "namespace": "probability.percolation",
                    "logical_name": logical_name, "kind": "lemma", "title": title,
                    "statement": "AUTHOR PROOF; independent audit pending. "+standalone[label],
                    "proof_text": row["proof_or_counterexample"],
                    "assumptions": row["assumptions"], "domain": "probability theory",
                    "source": dict(source)})
entries.extend([
    {"key":"bad-selected-marginal", "namespace":"probability.percolation",
     "logical_name":"refuted-arbitrary-order-unconditional-selected-relay-bridge",
     "kind":"concept", "title":"Refuted arbitrary-order selected-relay bridge",
     "statement":"REFUTED AUXILIARY PROPOSITION, not a theorem: after selecting the first member I of an arbitrarily ordered relay set A reached from o in independent bond percolation, replace P(a connects to b | I=a) by a lower bound P(a connects to b), or assert P(o connects to b)>=sum_a P(I=a)P(a connects to b). This proposition is false on o--a2--a1--b with relay order (a1,a2). A specified nondecreasing marginal order is a separate proposition. The original product and near-one gluing assertions are not refuted.",
     "proof_text":None, "assumptions":["Finite undirected graph", "Independent edge states", "Arbitrary fixed relay order"],
     "domain":"probability theory", "source":dict(source)},
    {"key":"bad-fixed-witness", "namespace":"probability.percolation",
     "logical_name":"refuted-universal-fixed-relay-pointwise-witness",
     "kind":"concept", "title":"Refuted universal fixed-relay witness bridge",
     "statement":"REFUTED AUXILIARY PROPOSITION, not a theorem: for every finite graph and nonempty relay set A there is a deterministic a_star in A such that {o connects to A,a_star connects to b} is contained in {o connects to b}. A square o--a1--v--a2--o with a pendant edge v--b and A={a1,a2} is a counterexample. The inclusion does hold for forests; failure of this deterministic bridge does not refute probabilistic gluing.",
     "proof_text":None, "assumptions":["Finite undirected graph", "Nonempty relay set"],
     "domain":"probability theory", "source":dict(source)}])
relations = [
    {"from_key":"l2","to_key":"l1","kind":"depends_on",
     "rationale":"L2: 'Let G be any finite undirected forest' admits the separator demanded by L1: 'If every o-to-A path and every a_star-to-b path contains v'. Tree projection supplies both hypotheses; no arbitrary cyclic extension is asserted."},
    {"from_key":"l3","to_key":"l2","kind":"depends_on",
     "rationale":"L3's 'delta_star=1-sqrt(1-epsilon)' follows from L2's 'P(o connects to b)>=P(o connects to A)min_{a in A}P(a connects to b)' and the two strict near-one premises; two-edge paths establish necessity."},
    {"from_key":"b1","to_key":"bad-selected-marginal","kind":"refutes",
     "rationale":"B1: 'P(a2 connects to b | I=a2)=0<P(a2 connects to b)=st' refutes the concept's 'replace P(a connects to b | I=a) by a lower bound P(a connects to b)'; the exact rst(2-s) sum separately refutes its arbitrary-order averaged inequality."},
    {"from_key":"b2","to_key":"bad-fixed-witness","kind":"refutes",
     "rationale":"B2: 'No fixed a_star in A satisfies' the pointwise inclusion refutes the concept's 'there is a deterministic a_star in A such that' assertion. The two explicit square configurations exclude both possible candidates."},
    {"from_key":"b2","to_key":"l2","kind":"semantic_association",
     "rationale":"B2: 'No fixed a_star in A satisfies' on its square describes the boundary of L2's forest claim: 'There is also a deterministic a_star in A'. B2 explicitly leaves the probability product bound intact (margin 1/128 at half weights)."}]
support_quotes = [
    ("l2","Let G be any finite undirected forest","l1","If every o-to-A path and every a_star-to-b path contains v"),
    ("l3","delta_star=1-sqrt(1-epsilon)","l2","P(o connects to b)>=P(o connects to A)min_{a in A}P(a connects to b)"),
    ("b1","P(a2 connects to b | I=a2)=0<P(a2 connects to b)=st","bad-selected-marginal","replace P(a connects to b | I=a) by a lower bound P(a connects to b)"),
    ("b2","No fixed a_star in A satisfies","bad-fixed-witness","there is a deterministic a_star in A such that"),
    ("b2","No fixed a_star in A satisfies","l2","There is also a deterministic a_star in A")]
bundle = {"spec":"mathbrain-draft-v1", "author_agent":"w426",
          "bundle_slug":"draft-c0023-forest-relay-boundary-w426-20261010",
          "entries":entries, "relations":relations}

# Validate the documented draft shape without touching a live store or integrator.
assert len(entries)<=10 and len(relations)<=15
keys = {e["key"] for e in entries}
assert len(keys)==len(entries)
allowed = {"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
for e in entries:
    assert set(("key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source")) <= e.keys()
    assert re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*",e["logical_name"])
    assert e["source"]["license"].startswith("owner-own-work")
    assert e["source"]["source_id"] and e["statement"] and e["assumptions"]
    assert (e["kind"]=="lemma" and e["proof_text"]) or (e["kind"]=="concept" and e["proof_text"] is None)
for r in relations:
    assert r["from_key"] in keys and r["to_key"] in keys and r["kind"] in allowed
entry_map={e["key"]:e for e in entries}
for r,(fk,fq,tk,tq) in zip(relations,support_quotes):
    assert (r["from_key"],r["to_key"])==(fk,tk)
    assert fq in entry_map[fk]["statement"] and tq in entry_map[tk]["statement"]
    assert fq in r["rationale"] and tq in r["rationale"]
def visit(k, active):
    assert k not in active, "cyclic depends_on"
    for r in relations:
        if r["kind"]=="depends_on" and r["from_key"]==k:
            visit(r["to_key"],active|{k})
for k in keys:
    visit(k,set())
raw = json.dumps(bundle,indent=2,ensure_ascii=False)+"\n"
(ROOT/"bundle_001.json").write_text(raw,encoding="utf-8")
INBOX.mkdir(parents=True,exist_ok=True)
index=1
while (INBOX/f"bundle_{index:03}.json").exists():
    old_raw=(INBOX/f"bundle_{index:03}.json").read_text(encoding="utf-8")
    old=json.loads(old_raw)
    if old_raw==raw or (old.get("author_agent")=="w426" and old.get("bundle_slug")==bundle["bundle_slug"]):
        break
    index += 1
destination = INBOX/f"bundle_{index:03}.json"
if not destination.exists() or destination.read_text(encoding="utf-8")!=raw:
    if destination.exists():
        (ROOT/"bundle_001.before_statement_expansion.json").write_text(destination.read_text(encoding="utf-8"),encoding="utf-8")
    part = INBOX/f"bundle_{index:03}.json.part"
    with part.open("x",encoding="utf-8") as f:
        f.write(raw)
    assert part.read_text(encoding="utf-8")==raw
    part.replace(destination)
assert destination.read_text(encoding="utf-8")==raw

cue = r"(?is)(?:first[ -](?:hit|reached|reachable) relay|selected relay|chosen relay).{0,100}(?:retains? (?:its |the )?unconditional|replace conditional with unconditional|unconditional terminal marginal)"
hook = {"id":"percolation-relay-w426-01","area":"math","event":"stage-start",
        "cue":cue,
        "fire_when":"An arbitrary first reached relay is asserted to retain its unconditional terminal marginal, without checking the selection-conditioned law.",
        "silent_when":"The selection-conditioned law is computed explicitly, or a fixed separator/disjoint-edge witness has been proved.",
        "text":"Relay selection can reveal closed edges. On o-a2-a1-b, order (a1,a2), selecting a2 forces the middle edge closed: conditional terminal probability 0, unconditional st. Audit the selected law before substituting marginals or averaging.",
        "evidence":"~/brain_workers/w426/VERIFICATION.json: half_weight_counterexample, actual 1/8 vs incorrect sum 3/16; ATTEMPT.md B1",
        "proposer":"w426"}
assert len(hook["text"])<=300
controls = [("First reached relay retains its unconditional terminal probability.",True),
            ("Selected relay: replace conditional with unconditional terminal marginal.",True),
            ("First reached relay: compute the conditional terminal law exactly.",False),
            ("Fixed relay and terminal use disjoint edge sets, proved independent.",False)]
for text, expected in controls:
    assert bool(re.search(cue,text)) is expected
hook_raw=json.dumps(hook,ensure_ascii=False)+"\n"
(ROOT/"HOOK_PROPOSAL.jsonl").write_text(hook_raw,encoding="utf-8")
patches=ROOT/"patches"
patches.mkdir(exist_ok=True)
live="~/primary_directive/hooks1000/proposals/percolation-relay-w426.jsonl"
diff="".join(difflib.unified_diff([],hook_raw.splitlines(keepends=True),fromfile="a/"+live,tofile="b/"+live))
(patches/"01_selected_relay_hook.diff").write_text(diff,encoding="utf-8")

status=json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
status["brain_pipeline"]={"prepared":True,"submitted":True,"reviewed":False,"ingested":False,"retrievable":False,
                          "draft_path":destination.as_posix(),"schema_check":"local PASS, live integrator not run"}
status["canonical_store_lookup"]="STORE_LOOKUP.json; read-only bounded title query"
(ROOT/"SOURCE_STATUS.json").write_text(json.dumps(status,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
validation={"status":"PASS","command":"python -X utf8 prepare_review.py",
            "bundle_entries":len(entries),"proved_author_claims":5,"refuted_bridge_concepts":2,
            "relations":len(relations),"dependency_cycle_check":"PASS",
            "relation_support_quote_checks":2*len(support_quotes),
            "source_license_check":"owner-own-work PASS","hook_fire_controls":2,"hook_silent_controls":2,
            "hook_control_failures":0,"draft_path":destination.as_posix(),
            "reviewed":False,"ingested":False,"retrievable":False,
            "scope":"Local schema/control checks only. Coordinator integration and independent mathematical review pending."}
(ROOT/"BUNDLE_VALIDATION.json").write_text(json.dumps(validation,indent=2)+"\n",encoding="utf-8")
progress={"event":"C0023 w426: five sharp-boundary author results saved; 29,339 exact probability checks pass; seven-entry draft submitted, independent review pending.",
          "agent":"w426","row":"S1.C0023.boundary","evidence":str(ROOT/"REVIEW_PACKET.md"),
          "state":"staged_local_for_reviewer","reason":"Worker forbids writes outside its folder except its named peer handoffs and dedicated draft inbox; no global progress/hook file was changed."}
(ROOT/"PROGRESS_EVENT.jsonl").write_text(json.dumps(progress)+"\n",encoding="utf-8")
report=f"""# w426 C0023 report

Saved five author results: separator gluing, arbitrary-relay forest gluing, its sharp near-one modulus, a selected-relay conditioning counterexample, and a square obstructing a fixed pointwise witness. The sharp modulus is 1-sqrt(1-epsilon). These are special cases and refuted auxiliary routes; C0023 remains unresolved in this packet and current openness is UNKNOWN.

The tempting arbitrary-order relay sum gives 3/16 instead of the actual 1/8: a 50% overstatement. Correct conditioning gives terminal probability 0 for the selected bad relay instead of its unconditional 1/4. `python -X utf8 verify_boundary.py` passed 29,339 exact probability cases and 7,916 pointwise cases across 25 forest topologies, plus 29 counterexample weight vectors, in {receipt['elapsed_seconds']:.2f} seconds. Fractions are exact. These checks are not an independent or formal proof audit.

Submitted {len(entries)} DRAFT entries and {len(relations)} supported relations at `{destination.as_posix()}`. `python -X utf8 prepare_review.py` passed local shape, license, relation and hook controls (2 fire, 2 silent, zero failures). Source license is owner-own-work. No live store or recall controls changed. Reviewed, ingested and retrievable remain false.

Apply: the validating coordinator reviews and ingests the dedicated draft using BUNDLE_SPEC; after hook pair approval, apply patches/01_selected_relay_hook.diff by adding its sole JSON line at the named live proposal path. PROGRESS_EVENT.jsonl is staged for the reviewer to publish under the worker write boundary.

Main risk: neither the separator proof nor arbitrary-order counterexample settles uniform gluing on cyclic graphs. A marginal-sorted selection claim is outside B1's refutation. w428 should check ATTEMPT.md and reproduce VERIFICATION.json; only audited results should land. The live integrator was not invoked because this worker may not write a live store.

NEXT: w428 audits L1-L3 and B1-B2; the coordinator integrates approved entries, keeping arbitrary-graph gluing as the single remaining gap.
"""
(ROOT/"REPORT.md").write_text(report,encoding="utf-8")
print(json.dumps(validation,indent=2))
