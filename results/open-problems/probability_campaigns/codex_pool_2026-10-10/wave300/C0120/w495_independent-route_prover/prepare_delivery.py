"""Prepare scoped local artifacts and an unreviewed draft inbox bundle; no live-store writes."""
from pathlib import Path
import json
import itertools

ROOT = Path(__file__).resolve().parent
LIVE_REL = "06_math_research/probability_1000_intake_claude_20260907/problems.jsonl"
LIVE = Path("~/<private-repo>") / LIVE_REL
INBOX = Path("~/math-brain-inbox/w495")


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


with LIVE.open(encoding="utf-8") as handle:
    old_line = next(itertools.islice(handle, 119, 120)).rstrip("\r\n")
before = json.loads(old_line)
assert before["problem_id"] == "C0120", "Source line moved: recover exact row before making a patch."
after = dict(before)
after["statement"] = (
    "For independent standard Gaussian vertex weights on Z^2, let M_n be the maximum weight "
    "of an n-vertex path beginning at the origin with east/north unit steps and free endpoint. "
    "Improve Var(M_n)<=C n/log n from Chatterjee's Theorem 8.1 to Var(M_n)<=C n^(1-epsilon) "
    "for some epsilon>0 and C<infinity, for every n>=2."
)
after["status_search"] = (
    "Source-scope correction by w495 on 2026-10-10: arXiv:0810.4221v2 section 8 treats the "
    "Gaussian ground-state maximum in 1+1 dimensions, not log Z_n in general dimension. "
    "Section 12 problem (3) asks to improve its fluctuation exponent; problem (2) separately "
    "asks about higher-dimensional chaos. Present openness UNKNOWN; finite temperature and "
    "arbitrary weights need their own statements and primary sources. Independent review pending."
)
after["locator"] = "Section 8, Theorem 8.1, pp.37-38; Section 12, problem (3), p.59"
new_line = json.dumps(after, ensure_ascii=False, sort_keys=True)
save(ROOT / "SOURCE_ROW_BEFORE.json", before)
save(ROOT / "SOURCE_ROW_AFTER.json", after)
(ROOT / "patches").mkdir(exist_ok=True)
patch = (
    f"--- a/{LIVE_REL}\n+++ b/{LIVE_REL}\n@@ -120 +120 @@\n"
    f"-{old_line}\n+{new_line}\n"
)
(ROOT / "patches/01_C0120_source_scope.diff").write_text(patch, encoding="utf-8")

proof_source = {
    "source_id": "owner-own-work:w495:C0120-independent-obstruction",
    "url": "~/brain_workers/w495/ATTEMPT.md",
    "revision": "2026-10-10-author-draft",
    "license": "owner-own-work (campaign argument; independent review pending)",
    "excerpt": None,
}


def entry(key, name, title, statement, assumptions, kind="concept", source=None):
    return {
        "key": key, "namespace": "probability.directed.polymers", "logical_name": name,
        "kind": kind, "title": title,
        "statement": "DRAFT; author proof or source audit only; independent review pending. " + statement,
        "proof_text": None, "assumptions": assumptions, "domain": "probability",
        "source": dict(source or proof_source),
    }


entries = [
    entry("scope", "c0120-gaussian-ground-state-source-scope-draft", "C0120 source scope (draft audit)",
          "Let g_v be independent N(0,1) weights on Z^2 and let M_n maximize their sum over "
          "n-vertex paths from (0,0) with east/north unit steps and free endpoint. The cited "
          "Chatterjee 2008 Theorem 8.1 gives Var(M_n)<=C n/log n. The source-faithful power "
          "target is Var(M_n)<=C n^(1-epsilon), epsilon>0. The cited theorem does not state "
          "the intake's general-dimension log-partition formulation. Present openness UNKNOWN.",
          ["Independent standard Gaussian vertex weights", "Fixed east/north lattice", "n>=2"],
          source={**proof_source, "source_id": "owner-own-work:w495:C0120-source-scope-audit",
                  "url": "~/brain_workers/w495/STATEMENT.md"}),
    entry("extrema", "independent-gaussian-maxima-explicit-log-variance-draft", "Gaussian maximum variance controls (draft)",
          "For W_m=max(Z_1,...,Z_m) with independent standard normal Z_i and m>=16, "
          "c/log(m)<=Var(W_m)<=2/log(m), where c=(1-exp(-(2/5)*exp(-3/2)))/8. "
          "The author proof uses Mills bounds, two separated quantile events, and finite-dimensional "
          "Gaussian OU hypercontractivity; see ATTEMPT.md L1.",
          ["m>=16", "Independent N(0,1) variables", "Natural logarithm"]),
    entry("model", "binary-tree-private-chains-gaussian-polymer-definition", "Binary-tree and private-chains polymer (draft)",
          "For r>=1 and m=n=2^r, put independent N(0,1) weights on a complete binary tree's "
          "internal levels 0,...,r-1 and on m private n-vertex chains at its leaf positions. "
          "Orient edges away from the root. Every root-to-terminal path has L=n+r vertices; "
          "indegree is at most 1 and outdegree at most 2. Let U_i be the internal prefix, S_i the "
          "private-chain sum, M=max_i(U_i+S_i), and A=max_i S_i. This graph family is not the "
          "fixed east/north lattice. The author bound is E[(M-A)^2]<=2r(log(2m)+1).",
          ["r>=1", "m=n=2^r", "Independent standard Gaussian vertex weights"]),
    entry("chaos", "binary-tree-private-chains-first-gaussian-chaos-draft", "Bounded first chaos on tree and chains (draft)",
          "For the binary-tree-plus-private-chains model with m=n=2^r and L=n+r, the "
          "first Gaussian-chaos projection Pi_1 M=sum_v E[M g_v]g_v has variance exactly "
          "3-2/m. Almost surely every coordinate derivative of M is 0 or 1 and the total "
          "squared gradient is L. Coefficients are 2^-k at each internal vertex on level k "
          "and 1/m on each chain vertex, by transitivity and Gaussian integration by parts.",
          ["Finite model defined in this bundle", "Unique maximizer almost surely"]),
    entry("obstruction", "bounded-degree-small-first-chaos-power-variance-obstruction-draft", "Power variance inference obstruction (draft)",
          "For the binary-tree-plus-private-chains Gaussian model, Var(M)=Theta(L/log L) "
          "as r grows although Var(Pi_1 M)<3, every derivative is bounded by 1, all paths "
          "have L vertices, the root is common, and outdegree is at most 2. Explicitly, "
          "c n/(4 log m)<=Var(M)<6n/log m whenever 2r(log(2m)+1)<=c n/(4 log m), with "
          "m=n=2^r, L=n+r and c=(1-exp(-(2/5)*exp(-3/2)))/8. These properties alone "
          "do not imply a positive power saving. This is not a counterexample on the source lattice.",
          ["Binary-tree-plus-private-chains model", "r sufficiently large"]),
    entry("finite-temp", "fixed-temperature-tree-private-chains-variance-obstruction-draft", "Fixed temperature obstruction (draft)",
          "In the same Gaussian graph family, for each fixed beta>0, F_beta=beta^-1 "
          "log[m^-1 sum_i exp(beta(U_i+S_i))] has Var(F_beta)=Theta(L/log L) as r grows "
          "and first Gaussian-chaos variance 3-2/m. The deterministic comparison is "
          "M-log(m)/beta<=F_beta<=M. This is a graph-family statement, not a theorem "
          "for the original lattice or for beta varying with r.",
          ["Binary-tree-plus-private-chains model", "beta fixed strictly positive", "r grows"]),
    entry("gap", "c0120-lattice-higher-gaussian-chaos-gap-draft", "Remaining C0120 lattice gap (draft)",
          "The independent attempt does not solve C0120. A power variance gain for the "
          "fixed east/north lattice requires a justified quantitative estimate controlling "
          "the higher Gaussian chaoses or noise overlap. The obstruction graph has 2^r "
          "vertices at layer r, versus r+1 for the source lattice, and lacks its reconvergence. "
          "Small first chaos and bounded outdegree alone leave this gap open.",
          ["Source-faithful Gaussian ground-state formulation", "No parent solved or novelty claim"]),
]


def relation(start, end, kind, why):
    return {"from_key": start, "to_key": end, "kind": kind, "rationale": why}


relations = [
    relation("chaos", "model", "depends_on", "The exact coefficient sum uses the model's r internal levels and m private n-vertex chains."),
    relation("obstruction", "model", "depends_on", "The variance comparison uses E[(M-A)^2]<=2r(log(2m)+1) in this specific graph family."),
    relation("obstruction", "extrema", "depends_on", "The private-chain maximum has law sqrt(n) W_m; the explicit logarithmic variance bounds transfer through the prefix error."),
    relation("obstruction", "chaos", "depends_on", "The simultaneous first-chaos variance 3-2/m and total variance Theta(L/log L) invalidate the abstract implication."),
    relation("finite-temp", "model", "depends_on", "The Gibbs sum is over the same m equal-length root-to-terminal paths."),
    relation("finite-temp", "obstruction", "analogous_to", "The log-sum-exp comparison produces the same logarithmic variance obstruction for each fixed beta>0."),
    relation("gap", "obstruction", "depends_on", "The graph obstruction shows why bounded degree and first-chaos smallness do not discharge the parent lattice estimate."),
    relation("gap", "scope", "semantic_association", "Both refer explicitly to C0120's fixed Gaussian east/north ground-state model, with present openness UNKNOWN."),
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w495",
          "bundle_slug": "c0120-independent-first-chaos-obstruction-w495", "entries": entries, "relations": relations}
save(ROOT / "bundle_001.json", bundle)
INBOX.mkdir(parents=True, exist_ok=True)
target = INBOX / "bundle_001.json"
if target.exists():
    assert json.loads(target.read_text(encoding="utf-8")) == bundle, "Refuse to overwrite a different existing draft."
else:
    part = INBOX / "bundle_001.json.part"
    assert not part.exists(), "Existing part requires inspection; preserve it."
    save(part, bundle)
    part.rename(target)

state_path = ROOT / "SOURCE_STATUS.json"
state = json.loads(state_path.read_text(encoding="utf-8"))
state["brain_pipeline"] = {"prepared": True, "submitted": True, "reviewed": False, "ingested": False, "retrievable": False}
state["draft_path"] = str(target).replace("\\", "/")
state["local_raw_extraction"] = {"path": "~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/raw/chatterjee_chaos_2008_loose.txt",
                                 "sha256": "4957f4a7993bd62ad0793195622c7cc7ecaceeeb8c19f7b8ca90d19f0b96aa39",
                                 "scope": "intake loose excerpts only; not the complete primary PDF"}
state["owner_solved_retired_check"] = "Bounded recall and target-ID reads completed; canonical live-store result not certified. Current openness remains UNKNOWN."
state["prior_attempt_other_roots"] = "Targeted C0120 scans of named H, I and Lean Markdown/JSONL/Lean artifacts found no additional C0120 proof. Exact intake A001 is the recovered attempt. This is not a whole-corpus exclusion."
save(state_path, state)
print(json.dumps({"prepared_entries": len(entries), "prepared_relations": len(relations), "draft_submitted": str(target), "patch": str(ROOT / "patches/01_C0120_source_scope.diff")}))
