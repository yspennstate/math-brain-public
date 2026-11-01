"""Portable synthetic audit of pinned AB30 sources and proposed source repairs.

No solver or hook process runs. All run records, grades, family-only metadata,
marker/state files and outputs exist in a TemporaryDirectory. The source modules
are imported without their command-line entry points; dispatch and subprocess
boundaries are mocked where exercised. Run with Python 3.9+ from any directory.
"""
import contextlib
import difflib
import hashlib
import importlib.util
import io
import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
FLAG = "BRAIN_HEADLESS_DIET"


def module(kind, name):
    path = HERE / kind / (name + ".py")
    spec = importlib.util.spec_from_file_location(kind + "_" + name, path)
    obj = importlib.util.module_from_spec(spec)
    with patch.object(sys, "argv", [str(path)]):
        spec.loader.exec_module(obj)
    return obj


def quiet(fn, *args):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*args)


def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj), encoding="utf-8")


def jsonl(path, rows):
    path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")


def source_identity():
    manifest = json.loads((HERE / "source_manifest.json").read_text())
    for rel, expected in manifest["files"].items():
        raw = (HERE / rel).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        assert blob == expected["git_blob"], rel
        assert hashlib.sha256(raw).hexdigest() == expected["sha256"], rel
    diffs = []
    for name in ("analyze.py", "ab30_run.py", "hook_dispatch.py"):
        path = manifest["files"]["source/" + name]["repository_path"]
        before = (HERE / "source" / name).read_text().splitlines(True)
        after = (HERE / "proposed" / name).read_text().splitlines(True)
        diffs.extend(difflib.unified_diff(before, after, fromfile="a/" + path, tofile="b/" + path))
    assert "".join(diffs) == (HERE / "ab30_source_repairs.patch").read_text()
    old = 'for fam in sorted({r["family"] for r in res["items"]}) | {"all"}:'
    new = 'for fam in sorted({r["family"] for r in res["items"]} | {"all"}):'
    assert (HERE / "proposed/analyze.py").read_text() == (HERE / "source/analyze.py").read_text().replace(old, new)
    print("PASS source identities: three pinned originals, three proposed copies, exact combined patch")


def score_controls(root, original, fixed):
    root.mkdir()
    original.RUNS = fixed.RUNS = root
    families = ("synthetic_alpha", "synthetic_alpha", "synthetic_beta")
    grades, amap, meta = [], {}, []
    pairs = (("full", "zero"), ("zero", "half"), ("half", "half"))
    for i, (fam, pair) in enumerate(zip(families, pairs)):
        q = "ab30_synthetic_%02d" % i
        meta.append({"id": q, "family": fam})  # No questions or answer keys.
        for arm, grade in zip(("on", "off"), pair):
            mid = "m%d" % len(grades)
            amap[mid] = {"id": q, "arm": arm}
            grades.append({"mid": mid, "grade": grade})
    gp, mp, kp = root / "grades.jsonl", root / "map.json", root / "family_metadata.jsonl"
    jsonl(gp, grades); dump(mp, amap); jsonl(kp, meta)
    try:
        original.score(gp, mp, kp)
    except TypeError as exc:
        assert "list" in str(exc) and "set" in str(exc)
        assert not (root / "RESULT.json").exists()
        print("REPRODUCED current score crash:", str(exc))
    else:
        raise AssertionError("Current grouping defect did not reproduce")
    quiet(fixed.score, gp, mp, kp)
    result = json.loads((root / "RESULT.json").read_text())
    assert set(result["by_family"]) == {"all", "synthetic_alpha", "synthetic_beta"}
    assert result["by_family"]["all"] == {"n": 3, "on_points": 1.5, "off_points": 1.0,
        "brain_better": 1, "brain_worse": 1, "sign_test_p": 1.0}
    print("PASS grouping repair: three synthetic pairs, two families, one win/loss/tie")
    amap["diet"] = {"id": meta[0]["id"], "arm": "ondiet"}
    amap["incomplete"] = {"id": "ab30_synthetic_incomplete", "arm": "on"}
    grades.extend([{"mid": "diet", "grade": "full"}, {"mid": "incomplete", "grade": "full"},
                   {"mid": "m0", "grade": "zero"}])
    meta.extend([{"id": "ab30_synthetic_incomplete", "family": "synthetic_alpha"},
                 {"id": "ab30_synthetic_absent", "family": "synthetic_alpha"}])
    dump(root / "AUDIT.json", [{"id": meta[0]["id"], "arm": "on", "hits": [["synthetic contamination"]]}])
    jsonl(gp, grades); dump(mp, amap); jsonl(kp, meta)
    quiet(fixed.score, gp, mp, kp)
    result = json.loads((root / "RESULT.json").read_text())
    assert len(result["items"]) == 3 and result["items"][0]["on"] == "zero"
    assert all("ondiet" not in row for row in result["items"])
    assert result["by_family"]["all"]["on_points"] == 0.5
    print("REPRODUCED remaining score limits: duplicate last-wins; missing/diet ignored; AUDIT not consumed")
    assert fixed.sign_p(19, 0) == 0.0 and 2 / 2**19 > 0
    print("REPRODUCED sign-test display rounding: 19 wins/0 losses gives 0.0 although exact p is positive")


def record(cost, status="ok"):
    return {"family": "synthetic", "status": status, "cost_usd_list": cost, "num_turns": 1,
        "duration_ms": 2000, "duration_api_ms": 1000, "wall_s": 2, "tool_counts": {},
        "max_context_tokens": 100, "hook_bytes": {}, "answer": "SYNTHETIC",
        "modelUsage": {"a": {"inputTokens": 2, "cacheReadInputTokens": 10,
             "cacheCreationInputTokens": 3, "outputTokens": 4, "thinkingTokens": 1},
                       "b": {"inputTokens": 5, "cacheReadInputTokens": 20,
             "cacheCreationInputTokens": 7, "outputTokens": 8, "thinkingTokens": 2}},
        "usage": {"output_tokens": 9999}}


def token_round_controls(root, analyzer):
    first, second = root / "round1", root / "round2"
    for arm, cost in (("on", 4), ("off", 2), ("ondiet", 1)):
        dump(first / "ab30_synthetic_01" / arm / "result.json", record(cost))
    dump(first / "ab30_synthetic_02/on/result.json", record(4))
    dump(first / "ab30_synthetic_03/on/result.json", record(3, "failed"))
    jsonl(first / "results.jsonl", [record(100, "failed")])  # Historical attempt log is not read.
    dump(first / "AUDIT.json", [{"id": "ab30_synthetic_01", "arm": "on", "hits": [["synthetic"]]}])
    analyzer.RUNS = first
    assert analyzer.tok(record(1)) == {"input": 7, "cache_read": 30, "cache_write": 10, "output": 12, "thinking": 3}
    assert analyzer.tok({"usage": {"output_tokens": 9}})["output"] == 9
    quiet(analyzer.tokens)
    result = json.loads((first / "TOKENS.json").read_text())
    assert len(result["runs"]) == 5 and result["by_arm"]["on"]["n"] == 2
    assert result["by_arm"]["on"]["cost_usd_list_sum"] == 8
    assert result["paired_summary"]["n"] == result["paired_diet_summary"]["n"] == 1
    assert result["paired_diet"][0]["cost_ratio_diet_over_on"] == 0.25
    assert result["runs"][0]["total_in"] == 47
    print("PASS cumulative usage and diet token pairing: both model entries; total input 47; diet/on ratio 0.25")
    print("REPRODUCED cost scope: unmatched success included; failed/history excluded from summaries; AUDIT ignored")
    quiet(analyzer.sheet, first / "sheet.jsonl", first / "arm_map.json")
    amap = json.loads((first / "arm_map.json").read_text())
    assert {r["arm"] for r in amap.values()} == {"on", "off", "ondiet"}
    assert len(amap) == 5
    dump(second / "ab30_synthetic_01/ondiet/result.json", record(1))
    spec = importlib.util.spec_from_file_location("cli_round_selection", HERE / "source/analyze.py")
    selected = importlib.util.module_from_spec(spec)
    with patch.object(sys, "argv", ["analyze.py", "tokens", "--runs-dir", str(second)]):
        spec.loader.exec_module(selected)
        assert selected.RUNS == second and sys.argv == ["analyze.py", "tokens"]
    quiet(selected.tokens)
    result = json.loads((second / "TOKENS.json").read_text())
    assert len(result["runs"]) == 1 and result["paired_diet"] == []
    print("PASS round selection: separate --runs-dir does not import round1 on/off; diet-only root has no diet pair")
    dump(second / "ab30_synthetic_01/on/result.json", {**record(4), "round": "other", "started": "different"})
    quiet(selected.tokens)
    result = json.loads((second / "TOKENS.json").read_text())
    assert len(result["paired_diet"]) == 1 and "round" not in result["runs"][0]
    print("REPRODUCED round-provenance limit: colocated item IDs pair without round/start checks")
    stream = second / "ab30_synthetic_01/on/stream.jsonl"
    stream.write_text("not valid json\n", encoding="utf-8")
    (second / "ab30_synthetic_01/ondiet/stream.jsonl").write_text("", encoding="utf-8")
    quiet(selected.audit)
    assert all(not row["hits"] for row in json.loads((second / "AUDIT.json").read_text()))
    print("REPRODUCED audit coverage limit: empty/malformed-only synthetic streams get empty hit lists")


def diet_controls(root, original_runner, fixed_runner, original_hook, fixed_hook):
    root.mkdir()
    marker = root / "HEADLESS_DIET_ON"
    state = root / "state"
    state.mkdir()
    for hook in (original_hook, fixed_hook):
        hook.HEADLESS_DIET_SWITCH = str(marker)
        hook._HEADLESS_STATE = str(state)
    payload = json.dumps({"prompt": "[headless-worker] SYNTHETIC"})
    outcomes = []
    for enabled in (False, True):
        if enabled:
            marker.touch()
        elif marker.exists():
            marker.unlink()
        row = []
        for arm in ("on", "ondiet"):
            with patch.dict(os.environ, {FLAG: "1"}, clear=True):
                env = original_runner.child_env(arm)
            with patch.dict(os.environ, env, clear=True):
                row.append(original_hook._headless_session("UserPromptSubmit", payload, ""))
        outcomes.append(row)
    assert outcomes == [[False, False], [True, True]]
    print("REPRODUCED current diet collapse: marker absent => on=False/ondiet=False; present => on=True/ondiet=True")
    checks = 0
    for enabled in (False, True):
        if enabled:
            marker.touch()
        elif marker.exists():
            marker.unlink()
        for inherited in (None, "0", "1"):
            inherited_env = {} if inherited is None else {FLAG: inherited}
            for arm, expected in (("on", False), ("ondiet", True)):
                with patch.dict(os.environ, inherited_env, clear=True):
                    env = fixed_runner.child_env(arm)
                assert env[FLAG] == str(int(expected))
                with patch.dict(os.environ, env, clear=True):
                    assert fixed_hook._headless_session("UserPromptSubmit", payload, "") == expected
                    assert not fixed_hook._headless_session("UserPromptSubmit", '{"prompt":"ordinary synthetic"}', "")
                    assert not fixed_hook._headless_session("SessionStart", "{}", "")
                    dump(state / "synthetic-session.json", {"headless": True})
                    assert fixed_hook._headless_session("PreToolUse", "{}", "synthetic-session") == expected
                checks += 1
        for legacy in ({}, {FLAG: "unrecognized"}):
            with patch.dict(os.environ, legacy, clear=True):
                assert fixed_hook._headless_session("UserPromptSubmit", payload, "") == enabled
    with patch.dict(os.environ, {FLAG: "1"}, clear=True):
        assert FLAG not in fixed_runner.child_env("off")
        assert FLAG not in fixed_runner.child_env(None)
    print("PASS proposed diet modes: 12 arm/marker/inheritance combinations; ordinary prompts and SessionStart unchanged")
    print("PASS proposed legacy fallback and marked-session tool events; no inherited flag reaches off/unspecified child")
    for value, expected_names in (("0", ["slow_sense.py", "math_sense.py"]), ("1", ["math_sense.py"])):
        with patch.dict(os.environ, {FLAG: value}, clear=True), \
             patch.object(fixed_hook, "hook_entries", return_value=[("python", ["slow_sense.py"]), ("python", ["math_sense.py"])]), \
             patch.object(fixed_hook, "as_python_argv", side_effect=lambda cmd, args, allow_all=False: (args[0], [])), \
             patch.object(fixed_hook, "run_in_process", return_value=(0, "", "")), \
             patch.object(fixed_hook, "merge", return_value=(0, "", "")), \
             patch.object(fixed_hook, "log"):
            rows = fixed_hook.dispatch("UserPromptSubmit", payload, "")[3]
        assert [r[0] for r in rows] == expected_names
    print("PASS proposed dispatch seam: full mode runs both mock hooks; diet skips slow_sense and retains math_sense")


def runner_error_control(root, runner):
    runner.RUNS = root
    root.mkdir()
    fake_parsed = {"result": {"is_error": True, "subtype": "error_during_execution", "total_cost_usd": 1.0},
        "max_context_tokens": 0, "assistant_msgs": 0, "hook_events": 0, "hook_bytes": {},
        "tool_uses": [], "init": None}
    class FakeProcess:
        def wait(self, timeout=None):
            return 1
    with patch.object(runner.subprocess, "Popen", return_value=FakeProcess()) as launch, \
         patch.object(runner, "parse_stream", return_value=fake_parsed):
        rec = quiet(runner.run_one, {"id": "ab30_synthetic_error", "family": "synthetic", "question": "SYNTHETIC"}, "off", 1)
        assert rec["status"] == "ok" and rec["is_error"] and rec["rc"] == 1
        quiet(runner.run_one, {"id": "ab30_synthetic_error", "question": "SYNTHETIC"}, "off", 1)
        assert launch.call_count == 1
    print("REPRODUCED runner status limit: mocked error result/rc1 labeled ok and skipped on repeat; no process launched")


def main():
    source_identity()
    original, fixed = module("source", "analyze"), module("proposed", "analyze")
    original_runner, fixed_runner = module("source", "ab30_run"), module("proposed", "ab30_run")
    original_hook, fixed_hook = module("source", "hook_dispatch"), module("proposed", "hook_dispatch")
    with tempfile.TemporaryDirectory(prefix="ab30-update-synthetic-") as tmp:
        root = Path(tmp)
        score_controls(root / "scores", original, fixed)
        token_round_controls(root, original)
        diet_controls(root / "diet", original_runner, fixed_runner, original_hook, fixed_hook)
        runner_error_control(root / "runner", original_runner)
    print("PASS: synthetic source audit only; zero solver/hook processes; no live edits; no held-out answers")


if __name__ == "__main__":
    main()
