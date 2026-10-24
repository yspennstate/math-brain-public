"""Bundle series C006: the Codex campaign ledger (read-only from its worktree) as typed nodes, in drafts of at most
200 entries: problem and exclusion nodes first (with reduction-free depends_on edges only inside a chunk), then attempt
nodes whose edges point to the problem nodes by logical id. Same integrator path as brain_bulk_C004.py."""
import json, os, re, subprocess, sys
from pathlib import Path
import brain_cycle_C001 as cyc
from intake_tools import HERE, now, records

AGENT = cyc.AGENT; INBOX = cyc.INBOX; ROOT = cyc.ROOT; POP = cyc.POP
CODEX = Path("~/.codex/worktrees/probability-1000-20h-20260906/06_math_research/probability_1000_20h_20260906")
CHUNK = 190


def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:70].rstrip("-")


def entry(key, namespace, logical, kind, title, statement, assumptions):
    e = cyc.entry(key, namespace, logical, kind, title, statement, None, assumptions)
    e["source"]["source_id"] = "owner-probability-campaign-codex-20260906:" + key
    e["source"]["url"] = "urn:probability-research:20260906:codex-campaign:" + key
    e["source"]["license"] = "owner-own-work; private campaign ledger row (Codex worker, 2026-09-06/07), no public promotion"
    return e


def build():
    problems = {r["problem_id"]: r for r in records(CODEX / "problems.jsonl")}
    sources = {r["source_id"]: r for r in records(CODEX / "sources.jsonl")}
    attempts = {}
    for a in records(CODEX / "attempts.jsonl"):
        if a.get("substantive"):
            attempts[a["problem_id"]] = a
    P, A, seen = [], [], set()
    for pid, p in sorted(problems.items()):
        if not re.fullmatch(r"[A-Z]\d{4}", pid):
            continue
        low = pid.lower(); s = slug(p.get("title", pid)) or "untitled"
        stitle = sources.get(p.get("source_id", ""), {}).get("title", p.get("source_id", "unknown source"))
        stmt_core = str(p.get("statement", "")).strip()
        if len(stmt_core) < 20:
            continue
        if p.get("current_status") == "resolved_in_literature" or not p.get("admitted", True):
            logical = "resolved-" + low + "-" + s
            if logical in seen: continue
            seen.add(logical)
            stmt = ("RESOLVED OR EXCLUDED in the Codex campaign ledger (status " + str(p.get("current_status")) + ", recorded by that worker's bounded search; verify before citing). "
                    + stmt_core + " Source posing it: " + stitle + ", " + str(p.get("locator", "")) + ". Notes: " + str(p.get("status_search", ""))[:600])
            P.append(entry("res-" + low, "probability.core", logical, "concept", "Resolved: " + p.get("title", pid), stmt, ["Posed in " + stitle, "Exclusion status from the campaign ledger"]))
            continue
        logical = "open-problem-" + low + "-" + s
        if logical in seen: continue
        seen.add(logical)
        stmt = ("OPEN PROBLEM from the Codex campaign ledger (" + str(p.get("historical_status")) + "; current status " + str(p.get("current_status")) + "; result status " + str(p.get("result_status")) + "). "
                + stmt_core + " Source: " + stitle + ", " + str(p.get("locator", "")) + "." + ((" Status notes: " + str(p.get("status_search"))[:500]) if p.get("status_search") else ""))
        P.append(entry("op-" + low, "probability.core", logical, "concept", "Open problem: " + p.get("title", pid), stmt, ["Posed in " + stitle, "Status as recorded in the campaign ledger on 2026-09-07"]))
        a = attempts.get(pid)
        if not a:
            continue
        alogical = "attempt-" + low + "-" + s
        astmt = ("ATTEMPT RECORD from the Codex campaign (author-checked by that worker only). Method: " + str(a.get("method", "")) + " Result: " + str(a.get("result", ""))
                 + ((" Key identity: " + str(a["key_identity"])) if a.get("key_identity") else "") + ((" Check: " + str(a["independent_check"])) if a.get("independent_check") else "")
                 + " Obstruction: " + str(a.get("obstruction", "")))
        if len(astmt) < 60:
            continue
        A.append((entry("at-" + low, "probability.core", alogical, "concept", "Attempt on " + p.get("title", pid), astmt, ["Refers to the open problem node " + logical, "No independent review"]),
                  "math:probability.core:" + logical))
    return P, A


def run(payload, tag, inbox_num):
    saved = HERE / f"brain_bundle_{tag}.json"; part = INBOX / f"bundle_{inbox_num:03d}.part"; final = INBOX / f"bundle_{inbox_num:03d}.json"
    if final.exists():
        raise RuntimeError("Inbox already exists: " + str(final))
    INBOX.mkdir(parents=True, exist_ok=True)
    saved.write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    part.write_bytes(saved.read_bytes()); os.replace(part, final)
    targets = [POP / x for x in ("brain.sqlite3", "brain.sqlite3-wal", "brain.sqlite3-shm", "brain_signal_cache.pkl", "brain_signal_cache.pkl.tmp", "integration_ledger.jsonl", "objects")] + [final.with_suffix(".rejected-note")]
    cyc.guard(*targets)
    r = subprocess.run([sys.executable, "-B", str(ROOT / "tools/integrate_drafts.py"), "--only", AGENT], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=1200, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    (HERE / f"brain_ingestion_{tag}.json").write_text(json.dumps(dict(recorded_at=now(), scope=AGENT, exit_code=r.returncode, stdout=r.stdout, stderr=r.stderr, public_promotion=False, proof_review="none"), indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(part=tag, exit_code=r.returncode, stdout_tail=r.stdout[-300:], stderr_tail=r.stderr[-200:])), flush=True)
    if r.returncode or "REJECTED" in r.stdout:
        raise RuntimeError("Ingestion failed for " + tag)


def main(start_inbox, skip=0):
    sys.path.insert(0, str(ROOT / "src")); cyc.HERE = HERE
    P, A = build(); print("problem/exclusion nodes", len(P), "attempt nodes", len(A), flush=True)
    n = start_inbox; k = 0
    for i in range(0, len(P), CHUNK):
        chunk = P[i:i + CHUNK]; k += 1
        if k <= skip:
            continue
        run(dict(spec="mathbrain-draft-v1", author_agent=AGENT, bundle_slug=f"probability-codex-ledger-problems-c006-{k:02d}", entries=chunk, relations=[]), f"C006p{k:02d}", n); n += 1
    for i in range(0, len(A), CHUNK):
        chunk = A[i:i + CHUNK]; k += 1
        rels = [dict(from_key=e["key"], to_existing_logical=lid, kind="depends_on", rationale="The attempt is about this problem and inherits its hypotheses") for e, lid in chunk]
        run(dict(spec="mathbrain-draft-v1", author_agent=AGENT, bundle_slug=f"probability-codex-ledger-attempts-c006-{k:02d}", entries=[e for e, _ in chunk], relations=rels), f"C006a{k:02d}", n); n += 1
    # retrieval receipt: obstruction-text probes on 12 attempt nodes + 3 negatives
    probes = []
    for e, _ in A:
        obs = e["statement"].split("Obstruction: ", 1)[-1].strip()
        if 40 <= len(obs) <= 300:
            probes.append(("positive", obs, e["logical_name"]))
    cyc.PROBES = probes[::max(1, len(probes) // 12)][:12] + [("negative", "Prove the intermediate value theorem", None), ("negative", "Compute the determinant of a 3 by 3 Vandermonde matrix", None), ("negative", "Define a topological group", None)]
    fake = dict(entries=[e for e, _ in A] + P)
    after = cyc.retrieve(fake, "after"); os.replace(HERE / "brain_retrieval_C001_after.json", HERE / "brain_retrieval_C006_after.json")
    pos = [p for p in after["probes"] if p["control"] == "positive"]; neg = [p for p in after["probes"] if p["control"] == "negative"]
    print(json.dumps({"own_nodes": after["own_nodes"], "expected": len(P) + len(A), "positive_top5": sum(bool(p["target_ranks"]) for p in pos), "positive_total": len(pos), "negative_clean": sum(not p["own_ranks"] for p in neg), "negative_total": len(neg)}), flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]) if len(sys.argv) > 2 else 0)
