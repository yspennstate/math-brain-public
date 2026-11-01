"""ab30 analysis: contamination audit, token accounting, blind grading sheet, scoring.

    python analyze.py audit                 every run's tool inputs AND tool results against the forbidden list
    python analyze.py tokens                per-run and per-arm token/cost table -> runs/TOKENS.json
    python analyze.py sheet OUT.jsonl MAP   blind grading sheet (answers shuffled under masked ids); the arm map is
                                            written to MAP, which the grader does not open until every grade is in
    python analyze.py score GRADES MAP KEYS unmask and score -> runs/RESULT.json

Grades file: one JSON per line {"mid": ..., "grade": "full|half|zero|abstain", "note": ...}.
"""
import json
import random
import re
import statistics
import sys
from pathlib import Path

RUNS = Path(r"C:\Users\Public\ab30\runs")
if "--runs-dir" in sys.argv:                      # round 2 writes its own tree (ab30_run.py --runs-dir)
    _i = sys.argv.index("--runs-dir")
    RUNS = Path(sys.argv[_i + 1])
    del sys.argv[_i:_i + 2]
ARMS = ("on", "off", "ondiet")
CAMP = Path(__file__).resolve().parent.parent
FORBIDDEN = [r"bank_multidomain_keys_quarantine", r"mdlit_keys", r"proofs\.jsonl", r"corpus_statements",
             r"benchmark_validity_a", r"arxiv_multidomain_sources", r"campaign_2026-09-06_multidomain_bank",
             r"ab30_keys", r"scratchpad[/\\]+ab30", r"_quarantine", r"\bcurl\b", r"\bwget\b", r"https?://",
             r"pip3? install", r"Invoke-WebRequest", r"urllib\.request", r"requests\.get", r"clean_step_text",
             r'"truth"\s*:', r"served\.jsonl", r"campaign_2026-09-23_ab30_tokens"]
FRX = re.compile("|".join(FORBIDDEN), re.I)


def runs():
    for q in sorted(RUNS.iterdir()):
        if not q.is_dir() or not q.name.startswith("ab30_"):
            continue
        for arm in ARMS:
            r = q / arm / "result.json"
            if r.exists():
                yield q.name, arm, json.load(open(r, encoding="utf-8"))


def audit():
    rows = []
    for qid, arm, rec in runs():
        hits = []
        p = RUNS / qid / arm / "stream.jsonl"
        for line in open(p, encoding="utf-8", errors="replace"):
            try:
                e = json.loads(line)
            except Exception:
                continue
            if e.get("type") == "assistant":
                for b in (e.get("message") or {}).get("content") or []:
                    if b.get("type") == "tool_use":
                        s = json.dumps(b.get("input"), ensure_ascii=False)
                        # the run's own scratch directory legitimately contains 'ab30'; only its cwd prefix is exempt
                        s2 = s.replace(str(RUNS).replace("\\", "\\\\"), "").replace(str(RUNS), "")
                        s2 = s2.replace("/c/Users/Public/ab30/runs", "").replace("C:/Users/Public/ab30/runs", "")
                        for m in FRX.finditer(s2):
                            hits.append(("input", b.get("name"), m.group(0), s[:240]))
            elif e.get("type") == "user":
                content = (e.get("message") or {}).get("content")
                if isinstance(content, list):
                    for c in content:
                        if isinstance(c, dict) and c.get("type") == "tool_result":
                            t = c.get("content")
                            t = t if isinstance(t, str) else json.dumps(t, ensure_ascii=False)
                            for m in re.finditer(r"clean_step_text|\"truth\"\s*:|mdlit_keys|ab30_keys", t):
                                hits.append(("result", "", m.group(0), t[max(0, m.start() - 120):m.end() + 120]))
        rows.append({"id": qid, "arm": arm, "hits": hits})
        mark = "CLEAN" if not hits else "HITS %d" % len(hits)
        print(qid, arm, mark)
        for h in hits[:6]:
            print("    ", h[0], h[1], repr(h[2]), "|", h[3][:200].replace("\n", " "))
    json.dump(rows, open(RUNS / "AUDIT.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)


def tok(rec):
    """Session totals from modelUsage (summed over models). The result's own `usage` block is NOT cumulative: on
    ab30_03/off, a run with a background task, it read 912 output tokens against modelUsage's 25,528, and only the
    modelUsage figures add up to the reported cost. Fall back to `usage` only when modelUsage is missing."""
    mu = rec.get("modelUsage") or {}
    if mu:
        s = {"input": 0, "cache_read": 0, "cache_write": 0, "output": 0, "thinking": 0}
        for v in mu.values():
            s["input"] += v.get("inputTokens") or 0
            s["cache_read"] += v.get("cacheReadInputTokens") or 0
            s["cache_write"] += v.get("cacheCreationInputTokens") or 0
            s["output"] += v.get("outputTokens") or 0
            s["thinking"] += v.get("thinkingTokens") or 0
        return s
    u = rec.get("usage") or {}
    return {"input": u.get("input_tokens") or 0, "cache_read": u.get("cache_read_input_tokens") or 0,
            "cache_write": u.get("cache_creation_input_tokens") or 0, "output": u.get("output_tokens") or 0,
            "thinking": ((u.get("output_tokens_details") or {}).get("thinking_tokens") or 0)}


def tokens():
    table = []
    for qid, arm, rec in runs():
        t = tok(rec)
        t["total_in"] = t["input"] + t["cache_read"] + t["cache_write"]
        dur, api = rec.get("duration_ms") or 0, rec.get("duration_api_ms") or 0
        table.append({"id": qid, "family": rec.get("family"), "arm": arm, "status": rec.get("status"),
                      "cost_usd_list": rec.get("cost_usd_list"), "turns": rec.get("num_turns"),
                      "wall_s": rec.get("wall_s"), "api_s": round(api / 1000.0, 1),
                      "local_s": round(max(0, dur - api) / 1000.0, 1),
                      "tool_calls": sum((rec.get("tool_counts") or {}).values()),
                      "max_context": rec.get("max_context_tokens"), "hook_bytes": sum((rec.get("hook_bytes") or {}).values()),
                      **t})
    out = {"runs": table, "by_arm": {}, "by_family_arm": {}, "paired": [], "paired_diet": []}
    for arm in ARMS:
        rs = [r for r in table if r["arm"] == arm and r["status"] == "ok"]
        if rs:
            out["by_arm"][arm] = summarize(rs)
        for fam in sorted({r["family"] for r in table}):
            fs = [r for r in rs if r["family"] == fam]
            if fs:
                out["by_family_arm"]["%s/%s" % (fam, arm)] = summarize(fs)
    ids = sorted({r["id"] for r in table})
    for q in ids:
        on = [r for r in table if r["id"] == q and r["arm"] == "on" and r["status"] == "ok"]
        off = [r for r in table if r["id"] == q and r["arm"] == "off" and r["status"] == "ok"]
        if on and off and off[0]["cost_usd_list"]:
            out["paired"].append({"id": q, "family": on[0]["family"],
                                  "cost_ratio": round(on[0]["cost_usd_list"] / off[0]["cost_usd_list"], 2),
                                  "output_ratio": round(on[0]["output"] / max(1, off[0]["output"]), 2),
                                  "total_in_ratio": round(on[0]["total_in"] / max(1, off[0]["total_in"]), 2)})
        diet = [r for r in table if r["id"] == q and r["arm"] == "ondiet" and r["status"] == "ok"]
        if on and diet and on[0]["cost_usd_list"]:
            out["paired_diet"].append({"id": q, "family": on[0]["family"],
                                       "cost_ratio_diet_over_on": round(diet[0]["cost_usd_list"] / on[0]["cost_usd_list"], 3),
                                       "hook_bytes_on": on[0]["hook_bytes"], "hook_bytes_diet": diet[0]["hook_bytes"],
                                       "wall_on": on[0]["wall_s"], "wall_diet": diet[0]["wall_s"],
                                       "local_on": on[0]["local_s"], "local_diet": diet[0]["local_s"],
                                       "total_in_on": on[0]["total_in"], "total_in_diet": diet[0]["total_in"]})
    if out["paired"]:
        cr = [p["cost_ratio"] for p in out["paired"]]
        out["paired_summary"] = {"n": len(cr), "median_cost_ratio": statistics.median(cr),
                                 "min": min(cr), "max": max(cr)}
    if out["paired_diet"]:
        d = out["paired_diet"]
        out["paired_diet_summary"] = {
            "n": len(d), "median_cost_ratio_diet_over_on": statistics.median(p["cost_ratio_diet_over_on"] for p in d),
            "median_hook_bytes_on": statistics.median(p["hook_bytes_on"] for p in d),
            "median_hook_bytes_diet": statistics.median(p["hook_bytes_diet"] for p in d),
            "median_local_s_on": statistics.median(p["local_on"] for p in d),
            "median_local_s_diet": statistics.median(p["local_diet"] for p in d)}
    json.dump(out, open(RUNS / "TOKENS.json", "w", encoding="utf-8"), indent=1)
    for k, v in out["by_arm"].items():
        print(k, v)
    for k, v in out["by_family_arm"].items():
        print(k, v)
    if out.get("paired_summary"):
        print("paired", out["paired_summary"])
    if out.get("paired_diet_summary"):
        print("paired diet", out["paired_diet_summary"])


def summarize(rs):
    s = {"n": len(rs)}
    for k in ("cost_usd_list", "output", "thinking", "cache_read", "cache_write", "input", "total_in", "turns",
              "wall_s", "api_s", "local_s", "tool_calls", "max_context", "hook_bytes"):
        vals = [r[k] or 0 for r in rs]
        s[k + "_sum"] = round(sum(vals), 4) if isinstance(vals[0], float) else sum(vals)
        s[k + "_median"] = statistics.median(vals)
    return s


def sheet(out_path, map_path):
    rows = []
    for qid, arm, rec in runs():
        rows.append({"id": qid, "arm": arm, "family": rec.get("family"), "answer": rec.get("answer"),
                     "confidence": rec.get("confidence"), "basis": rec.get("basis"),
                     "final_text": (rec.get("final_text") or "")[-6000:], "status": rec.get("status")})
    rng = random.Random()
    rng.shuffle(rows)
    amap = {}
    with open(out_path, "w", encoding="utf-8") as f:
        for i, r in enumerate(rows):
            mid = "m%03d" % i
            amap[mid] = {"id": r["id"], "arm": r["arm"]}
            f.write(json.dumps({"mid": mid, "item": r["id"], "family": r["family"], "status": r["status"],
                                "answer": r["answer"], "confidence": r["confidence"], "basis": r["basis"],
                                "final_text": r["final_text"]}, ensure_ascii=False) + "\n")
    json.dump(amap, open(map_path, "w", encoding="utf-8"), indent=1)
    print("sheet", len(rows), "rows ->", out_path)


def score(grades_path, map_path, keys_path):
    amap = json.load(open(map_path, encoding="utf-8"))
    keys = {json.loads(l)["id"]: json.loads(l) for l in open(keys_path, encoding="utf-8")}
    pts = {"full": 1.0, "half": 0.5, "zero": 0.0, "abstain": 0.0}
    g = {}
    for line in open(grades_path, encoding="utf-8"):
        d = json.loads(line)
        m = amap[d["mid"]]
        g[(m["id"], m["arm"])] = d
    items = sorted({k[0] for k in g})
    res = {"items": [], "by_family": {}}
    for q in items:
        on, off = g.get((q, "on")), g.get((q, "off"))
        if not on or not off:
            continue
        res["items"].append({"id": q, "family": keys[q]["family"], "on": on["grade"], "off": off["grade"],
                             "on_pts": pts[on["grade"]], "off_pts": pts[off["grade"]]})
    for fam in sorted({r["family"] for r in res["items"]}) | {"all"}:
        rs = [r for r in res["items"] if fam == "all" or r["family"] == fam]
        better = sum(1 for r in rs if r["on_pts"] > r["off_pts"])
        worse = sum(1 for r in rs if r["on_pts"] < r["off_pts"])
        res["by_family"][fam] = {"n": len(rs), "on_points": sum(r["on_pts"] for r in rs),
                                 "off_points": sum(r["off_pts"] for r in rs), "brain_better": better,
                                 "brain_worse": worse, "sign_test_p": sign_p(better, worse)}
    json.dump(res, open(RUNS / "RESULT.json", "w", encoding="utf-8"), indent=1)
    print(json.dumps(res["by_family"], indent=1))


def sign_p(a, b):
    """Two-sided exact sign test on a wins against b losses."""
    from math import comb
    n = a + b
    if n == 0:
        return 1.0
    k = min(a, b)
    p = sum(comb(n, i) for i in range(0, k + 1)) / 2 ** n
    return round(min(1.0, 2 * p), 5)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "audit":
        audit()
    elif cmd == "tokens":
        tokens()
    elif cmd == "sheet":
        sheet(sys.argv[2], sys.argv[3])
    elif cmd == "score":
        score(sys.argv[2], sys.argv[3], sys.argv[4])
