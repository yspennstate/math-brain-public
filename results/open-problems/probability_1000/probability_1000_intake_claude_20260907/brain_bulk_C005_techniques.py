"""Bundle C005: forty technique cards (drafted by a Sonnet helper from a spec, every card read and seven rewritten
by the Fable agent before ingestion) as concept nodes, each linked to the attempt/problem nodes whose text uses it.
Same integrator path as brain_bulk_C004.py."""
import json, os, re, subprocess, sys
import brain_cycle_C001 as cyc
from intake_tools import HERE, now

AGENT = cyc.AGENT; INBOX = cyc.INBOX; ROOT = cyc.ROOT; POP = cyc.POP
CARDS = r"~/AppData/Local/Temp/claude/<project>/406c48e3-c31c-4f06-b23b-3ffa39f2f2a6/scratchpad/technique_cards.json"
KEYWORDS = {  # technique key -> phrases whose presence in an attempt/problem statement links it
    "lace-expansion": ["lace expansion", "lace-expansion"], "infrared-bound": ["infrared bound", "reflection positivity"],
    "osss-inequality": ["OSSS"], "holley-inequality": ["Holley"], "fkg-harris-inequality": ["FKG", "Harris"], "russo-formula-pivotals": ["Russo", "pivotal"],
    "russo-seymour-welsh": ["RSW"], "quasi-multiplicativity-arm-events": ["quasi-multiplicativity", "arm probabilit", "arm exponent"],
    "sharpness-phase-transition": ["sharpness", "Duminil-Copin-Tassion", "Duminil-Copin, Raoufi"], "burton-keane-uniqueness": ["Burton-Keane"],
    "second-moment-method": ["second moment", "second-moment"], "efron-stein-bks-influence": ["Efron-Stein", "Benjamini-Kalai-Schramm", "BKS"],
    "hypercontractivity-bonami-beckner": ["hypercontractiv"], "talagrand-convex-distance": ["Talagrand"], "borell-tis-slepian-sudakov-fernique": ["Borell", "Slepian", "Sudakov"],
    "kahane-interpolation": ["Kahane", "interpolation"], "concentric-decomposition-gff": ["concentric decomposition"], "gibbs-markov-gff": ["Gibbs-Markov"],
    "second-ray-knight-isomorphism": ["Ray-Knight", "isomorphism"], "random-current-switching-lemma": ["random current", "random-current", "switching lemma"],
    "simon-lieb-inequality": ["Simon-Lieb"], "aizenman-barsky-differential-inequalities": ["Aizenman-Barsky", "Barsky-Aizenman", "differential inequalit"],
    "sznitman-zerner-regeneration": ["regeneration"], "kesten-kozlov-spitzer": ["Kesten-Kozlov-Spitzer", "branching process with migration", "branching-process-with-migration"],
    "kalikow-zero-one-law": ["Kalikow"], "rayleigh-monotonicity-effective-resistance": ["Rayleigh", "effective resistance", "effective-resistance"],
    "commute-time-identity": ["commute-time", "commute time"], "nash-inequality-heat-kernel": ["heat kernel", "Nash inequality"],
    "kesten-subdiffusivity": ["subdiffusiv"], "local-weak-convergence-objective-method": ["local weak", "objective method", "PWIT"],
    "aldous-exploration-multiplicative-coalescent": ["exploration process", "multiplicative coalescent"], "doob-h-transform-kesten-tree": ["h-transform", "Kesten tree", "Doob"],
    "moment-determinacy-carleman": ["Carleman", "moment-determina", "moment determina"], "steins-method": ["Stein's method"],
    "fekete-lemma-subadditive": ["Fekete", "subadditiv"], "kingman-subadditive-ergodic": ["Kingman"], "lindeberg-exchange-four-moment": ["Lindeberg", "four-moment", "four moment"],
    "hermitization-girko": ["Hermitis", "Hermitiz", "Girko", "log-potential"], "poisson-dirichlet-smoothing-transform": ["smoothing transform", "Durrett-Liggett"],
    "schur-complement-determinantal-conditionals": ["Schur complement"],
}


def make_payload(existing_logical):
    cards = json.load(open(CARDS, encoding="utf-8"))
    entries, relations = [], []
    for x in cards:
        stmt = ("TECHNIQUE CARD (drafted from a spec by a helper model, every card read and seven corrected by the Fable agent on 2026-09-07; "
                "canonical statements only, no original claim). " + x["statement"] + " Typical failure: " + x["typical_failure"]
                + " Canonical reference: " + x["canonical_reference"] + ".")
        entries.append(cyc.entry(x["key"], x["namespace"], x["logical_name"], "concept", "Technique: " + x["title"], stmt, None, list(x["assumptions"])))
        for k in ("source",):
            entries[-1][k]["source_id"] = "owner-probability-intake-claude-20260907:technique:" + x["key"]
            entries[-1][k]["url"] = "urn:probability-research:20260907:claude-intake:technique:" + x["key"]
    # link techniques to the attempt/problem nodes whose statements mention them (from the store, read-only)
    n_links = 0
    for x in cards:
        phrases = KEYWORDS.get(x["key"], [])
        for lid, body in existing_logical.items():
            if not (":attempt-c0" in lid or ":open-problem-c0" in lid or ":resolved-c0" in lid or "claude" in lid):
                continue
            if any(p.lower() in body.lower() for p in phrases):
                relations.append(dict(from_key=x["key"], to_existing_logical=lid, kind="cites", rationale="The recorded attempt or problem text invokes this technique"))
                n_links += 1
                if n_links > 400:
                    break
    return dict(spec="mathbrain-draft-v1", author_agent=AGENT, bundle_slug="probability-intake-claude-technique-cards-c005", entries=entries, relations=relations)


def existing_bodies():
    nodes, edges = cyc.read_store()
    out = {}
    for n in nodes:
        lid = n.metadata.get("logical_id", "")
        if lid.startswith("math:probability") or lid.startswith("math:combinatorics.partitions"):
            out[lid] = (n.title or "") + " " + (n.body or "")
    return out


def build_probes():
    return [("positive", "Two lattice spin-model correlation functions compared by counting how often two integer edge flows connect the same sources", "random-current-switching-lemma-technique"),
            ("positive", "A weighted-hamming distance to a set gives sub-gaussian tails for functionals certifiable by few coordinates", "talagrand-convex-distance-technique"),
            ("positive", "Increasing a conductance can only lower the resistance between two terminals", "rayleigh-monotonicity-effective-resistance-technique"),
            ("positive", "Replace the entries one at a time by Gaussians and Taylor-expand a smooth test function to prove universality", "lindeberg-exchange-four-moment-technique"),
            ("positive", "Conditioning a critical branching process to survive forever produces a spine with independent trees hanging off it", "doob-h-transform-kesten-tree-technique"),
            ("positive", "A ghost vertex magnetisation satisfies inequalities that force finite susceptibility below the threshold but say nothing about continuity at it", "aizenman-barsky-differential-inequalities-technique"),
            ("positive", "The event that a walk in random environment escapes along a direction or its opposite has probability zero or one, but the one-sided version is unresolved in three dimensions", "kalikow-zero-one-law-technique"),
            ("positive", "Local time at an inverse local time plus half a squared free field equals half a shifted squared free field in law", "second-ray-knight-isomorphism-technique"),
            ("negative", "Derive the quadratic formula", None), ("negative", "State Fermat's little theorem", None), ("negative", "What is the chromatic number of the Petersen graph", None)]


def run(payload, tag, inbox_num):
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
    sys.path.insert(0, str(ROOT / "src")); cyc.HERE = HERE
    ex = existing_bodies()
    payload = make_payload(ex); print("entries", len(payload["entries"]), "relations", len(payload["relations"]))
    cyc.PROBES = build_probes()
    before = cyc.retrieve(payload, "before"); os.replace(HERE / "brain_retrieval_C001_before.json", HERE / "brain_retrieval_C005_before.json")
    if before["own_nodes"]:
        raise RuntimeError("Bundle already exists")
    run(payload, "C005", 8)
    after = cyc.retrieve(payload, "after"); os.replace(HERE / "brain_retrieval_C001_after.json", HERE / "brain_retrieval_C005_after.json")
    pos = [p for p in after["probes"] if p["control"] == "positive"]; neg = [p for p in after["probes"] if p["control"] == "negative"]
    print(json.dumps({"own_nodes": after["own_nodes"], "expected": len(payload["entries"]), "touching_edges": len(after["touching_edges"]),
                      "positive_top5": sum(bool(p["target_ranks"]) for p in pos), "positive_total": len(pos),
                      "negative_clean": sum(not p["own_ranks"] for p in neg), "negative_total": len(neg)}))


if __name__ == "__main__":
    main()
