"""Bulk math-brain bundle C004: every admitted problem, its attempt, every literature exclusion, and the
reduction graph of the Claude intake ledger, as typed concept nodes with depends_on/analogous_to/cites edges.

Same integrator path as brain_cycle_C001.py. Problems already carried by a dedicated lemma/concept node from
bundles C001-C003 get a 'cites' edge to that node instead of a second attempt node.
"""
import json, os, re, subprocess, sys
import brain_cycle_C001 as cyc
from intake_tools import HERE, now, records

AGENT = cyc.AGENT; INBOX = cyc.INBOX; ROOT = cyc.ROOT; POP = cyc.POP

DEDICATED = {  # problem id -> existing logical id from bundles C001-C003
    "C0036": "math:probability.determinantal:harmonic-mean-product-domination-equivariant-determinantal-finite-group",
    "C0035": "math:probability.determinantal:determinantal-symbol-in-k-theta-splits-into-independent-sublattice-copies",
    "C0127": "math:probability.gaussian:two-summit-gaussian-field-has-multiple-peaks-without-chaos",
    "C0018": "math:probability.percolation:four-arm-exponent-existence-on-square-lattice-needs-scale-invariance",
    "C0062": "math:combinatorics.partitions:maximal-dimension-partition-unique-up-to-conjugation-for-n-at-most-40",
    "C0034": "math:probability.determinantal:union-marginal-coupling-of-projection-determinantal-laws-lp-feasible-evidence",
    "C0023": "math:probability.percolation:critical-percolation-full-space-from-half-space-needs-infinite-susceptibility-and-gluing",
    "C0052": "math:probability.statmech:ising-3d-nontriviality-reduces-to-current-intersection-lower-bound",
    "C0113": "math:probability.percolation:poisson-minimal-spanning-forest-high-dimension-single-tree-conditional",
    "C0073": "math:probability.percolation:effective-conductivity-theta-times-sigma-squared-is-nondecreasing-in-p",
    "C0021": "math:probability.boolean:iterated-three-majority-revealment-exponent-between-0166-and-0369",
    "C0005": "math:probability.gaussian:deep-extremal-level-set-conjecture-equivalent-to-cluster-size-limit-given-uniform-integrability",
    "C0057": "math:probability.planarmaps:filled-in-peeling-exhausts-the-map-iff-swallowing-series-diverges",
    "C0075": "math:probability.branching:moment-determinate-limit-turns-r-point-convergence-into-measure-convergence",
    "C0089": "math:probability.percolation:vacant-set-quenched-invariance-principle-all-u-from-prs-plus-sharpness",
    "C0071": "math:probability.percolation:critical-clusters-wrap-the-torus-iff-d-above-6-mean-field-depletion-mechanism",
    "C0087": "math:probability.percolation:torus-mst-diameter-and-limit-reduce-to-supercritical-uniqueness-and-window-geometry",
    "C0070": "math:probability.percolation:hypercube-duality-principle-reduces-to-sharp-subcritical-cluster-tail",
    "C0041": "math:probability.randomenvironment:rwre-transience-implies-ballistic-reduces-to-regeneration-time-integrability-and-moment-self-improvement",
    "C0053": "math:probability.random-matrices:one-dimensional-band-matrix-transition-established-2025-status-note",
    "C0090": "math:probability.percolation:scale-free-percolation-effective-long-range-exponent-mean-field-prediction",
}
NS = {"biskup": "probability.gaussian", "garban": "probability.percolation", "bordenave": "probability.random-matrices", "lyons": "probability.determinantal",
      "drewitz": "probability.randomenvironment", "duminil": "probability.statmech", "bourgade": "probability.random-matrices", "curien": "probability.planarmaps",
      "drs": "probability.percolation", "romik": "combinatorics.partitions", "heydenreich": "probability.percolation", "bdgs": "probability.percolation",
      "levine": "probability.core", "arguin": "probability.gaussian", "berestycki": "probability.branching", "werner": "probability.percolation",
      "tao": "probability.random-matrices", "aldous": "probability.core", "panchenko": "probability.statmech", "ding": "probability.core",
      "chatterjee": "probability.gaussian", "kumagai": "probability.percolation", "kosygina": "probability.randomenvironment"}


def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:70].rstrip("-")


def ns_of(source_id):
    for k, v in NS.items():
        if source_id.startswith(k):
            return v
    return "probability.core"


def entry(key, namespace, logical, kind, title, statement, proof, assumptions):
    e = cyc.entry(key, namespace, logical, kind, title, statement, proof, assumptions)
    e["source"]["source_id"] = "owner-probability-intake-claude-20260907:" + key
    e["source"]["url"] = "urn:probability-research:20260907:claude-intake:" + key
    return e


def make_payload():
    problems = {r["problem_id"]: r for r in records(HERE / "problems.jsonl")}
    sources = {r["source_id"]: r for r in records(HERE / "sources.jsonl")}
    attempts = {}
    for a in records(HERE / "attempts.jsonl"):
        if a.get("substantive") and not a.get("superseded_by"):
            attempts[a["problem_id"]] = a  # later rows (corrections) win
    entries, relations, keys = [], [], {}
    for pid, p in sorted(problems.items()):
        src = sources.get(p["source_id"], {})
        stitle = src.get("title", p["source_id"])
        ns = ns_of(p["source_id"])
        if p.get("current_status") == "resolved_in_literature":
            key = "res-" + pid.lower(); logical = "resolved-" + pid.lower() + "-" + slug(p["title"])
            stmt = ("RESOLVED IN THE LITERATURE (status recorded by a bounded search or recall on 2026-09-07, verify before citing). "
                    + p["statement"] + " Resolution: " + str(p.get("resolved_by", "")) + ". Notes: " + str(p.get("status_search", ""))
                    + " Source posing it: " + stitle + ", " + p["locator"] + ".")
            entries.append(entry(key, ns, logical, "concept", "Resolved: " + p["title"], stmt, None,
                                 ["Posed as open in " + stitle, "Resolution citation from bounded recall, not re-fetched"]))
            keys[pid] = key
            continue
        key = "op-" + pid.lower(); logical = "open-problem-" + pid.lower() + "-" + slug(p["title"])
        stmt = ("OPEN PROBLEM (" + p["historical_status"] + "; current status " + p["current_status"] + "; result status " + p["result_status"] + "). "
                + p["statement"] + " Source: " + stitle + ", " + p["locator"] + "." + (" Status notes: " + p["status_search"] if p.get("status_search") else ""))
        entries.append(entry(key, ns, logical, "concept", "Open problem: " + p["title"], stmt, None,
                             ["Posed in " + stitle, "Current status " + p["current_status"] + " as of 2026-09-07"]))
        keys[pid] = key
        if pid in DEDICATED:
            relations.append(dict(from_key=key, to_existing_logical=DEDICATED[pid], kind="cites", rationale="Dedicated author-checked node for this problem from bundles C001-C003"))
            continue
        a = attempts.get(pid)
        if not a or pid == "C0094":
            continue
        akey = "at-" + pid.lower(); alogical = "attempt-" + pid.lower() + "-" + slug(p["title"])
        astmt = ("ATTEMPT RECORD, author-checked only, from the 2026-09-07 intake. Method: " + a["method"] + " Result: " + a["result"]
                 + ((" Key identity: " + a["key_identity"]) if a.get("key_identity") else "")
                 + ((" Check: " + a["independent_check"]) if a.get("independent_check") else "")
                 + " Obstruction: " + a.get("obstruction", ""))
        entries.append(entry(akey, ns, alogical, "concept", "Attempt on " + p["title"], astmt, None,
                             ["Refers to the open problem node " + logical, "No independent review; result status " + p["result_status"]]))
        relations.append(dict(from_key=akey, to_key=key, kind="depends_on", rationale="The attempt is about this problem and inherits its hypotheses"))
    # reduction graph
    g = json.load(open(HERE / "raw/reduction_graph.json", encoding="utf-8"))
    kindmap = {"reduces_to": "depends_on", "equivalent_given": "depends_on", "reformulates": "depends_on", "analogous": "analogous_to",
               "shares_block": "analogous_to", "independent_of": "analogous_to", "duplicate": None}
    for e in g["edges"]:
        k = kindmap.get(e["kind"])
        if k and e["target"] in keys and e["needs"] in keys:
            relations.append(dict(from_key=keys[e["target"]], to_key=keys[e["needs"]], kind=k, rationale=e["note"]))
    return dict(spec="mathbrain-draft-v1", author_agent=AGENT, bundle_slug="probability-intake-claude-bulk-problems-attempts-exclusions-c004", entries=entries, relations=relations)


def build_probes(payload):
    # probes use the OBSTRUCTION text of attempts (wording distinct from titles) as queries; targets are the attempt nodes
    probes = []
    for e in payload["entries"]:
        if e["key"].startswith("at-") and "Obstruction: " in e["statement"]:
            obs = e["statement"].split("Obstruction: ", 1)[1].strip()
            if 40 <= len(obs) <= 300:
                probes.append(("positive", obs, e["logical_name"]))
    probes = probes[::max(1, len(probes) // 12)][:12]
    probes += [("negative", "Prove the Cauchy-Schwarz inequality in an inner product space", None),
               ("negative", "Find all integer solutions of x^2 - 2y^2 = 1", None),
               ("negative", "Show that a compact Hausdorff space is normal", None)]
    return probes


def split_payload(payload):
    """Part A: problem + resolved nodes with their mutual (reduction) relations. Part B: attempt nodes whose
    edges point at the part-A nodes by logical id (the integrator caps a draft at 200 entries)."""
    A = [e for e in payload["entries"] if not e["key"].startswith("at-")]
    B = [e for e in payload["entries"] if e["key"].startswith("at-")]
    akeys = {e["key"] for e in A}; logical = {e["key"]: "math:" + e["namespace"] + ":" + e["logical_name"] for e in payload["entries"]}
    relA = [r for r in payload["relations"] if r["from_key"] in akeys and (r.get("to_key") in akeys or "to_existing_logical" in r)]
    relB = []
    for r in payload["relations"]:
        if r["from_key"] not in akeys:
            if "to_key" in r and r["to_key"] in akeys:
                relB.append(dict(from_key=r["from_key"], to_existing_logical=logical[r["to_key"]], kind=r["kind"], rationale=r["rationale"]))
            else:
                relB.append(r)
    pA = dict(spec="mathbrain-draft-v1", author_agent=AGENT, bundle_slug="probability-intake-claude-bulk-problems-and-exclusions-c004a", entries=A, relations=relA)
    pB = dict(spec="mathbrain-draft-v1", author_agent=AGENT, bundle_slug="probability-intake-claude-bulk-attempts-c004b", entries=B, relations=relB)
    return pA, pB


def run_part(payload, tag, inbox_num):
    saved = HERE / f"brain_bundle_{tag}.json"; part = INBOX / f"bundle_{inbox_num:03d}.part"; final = INBOX / f"bundle_{inbox_num:03d}.json"
    if final.exists():
        raise RuntimeError("Inbox already exists: " + str(final))
    INBOX.mkdir(parents=True, exist_ok=True)
    saved.write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    part.write_bytes(saved.read_bytes()); os.replace(part, final)
    targets = [POP / x for x in ("brain.sqlite3", "brain.sqlite3-wal", "brain.sqlite3-shm", "brain_signal_cache.pkl", "brain_signal_cache.pkl.tmp", "integration_ledger.jsonl", "objects")] + [final.with_suffix(".rejected-note")]
    cyc.guard(*targets)
    r = subprocess.run([sys.executable, "-B", str(ROOT / "tools/integrate_drafts.py"), "--only", AGENT], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=900, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    (HERE / f"brain_ingestion_{tag}.json").write_text(json.dumps(dict(recorded_at=now(), scope=AGENT, exit_code=r.returncode, stdout=r.stdout, stderr=r.stderr, public_promotion=False, proof_review="none"), indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(part=tag, exit_code=r.returncode, stdout_tail=r.stdout[-400:], stderr_tail=r.stderr[-200:])))
    if r.returncode or "REJECTED" in r.stdout:
        raise RuntimeError("Ingestion failed for " + tag)


def main():
    payload = make_payload()
    cyc.PROBES = build_probes(payload)
    n = len(payload["entries"]); print("entries", n, "relations", len(payload["relations"]), "probes", len(cyc.PROBES))
    sys.path.insert(0, str(ROOT / "src")); cyc.HERE = HERE
    before = cyc.retrieve(payload, "before"); os.replace(HERE / "brain_retrieval_C001_before.json", HERE / "brain_retrieval_C004_before.json")
    if before["own_nodes"]:
        raise RuntimeError("Bundle already exists")
    pA, pB = split_payload(payload); print("partA", len(pA["entries"]), len(pA["relations"]), "partB", len(pB["entries"]), len(pB["relations"]))
    run_part(pA, "C004a", 6); run_part(pB, "C004b", 7)
    after = cyc.retrieve(payload, "after"); os.replace(HERE / "brain_retrieval_C001_after.json", HERE / "brain_retrieval_C004_after.json")
    pos = [p for p in after["probes"] if p["control"] == "positive"]; neg = [p for p in after["probes"] if p["control"] == "negative"]
    print(json.dumps({"own_nodes": after["own_nodes"], "expected": n, "touching_edges": len(after["touching_edges"]),
                      "positive_top5": sum(bool(p["target_ranks"]) for p in pos), "positive_total": len(pos),
                      "negative_clean": sum(not p["own_ranks"] for p in neg), "negative_total": len(neg)}))


if __name__ == "__main__":
    main()
