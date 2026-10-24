#!/usr/bin/env python3
"""Adversarial isolated fixtures for A26_verify_bundle.py; standard library only.

This test creates no fictitious completed campaign. Temporary roster objects
are explicitly synthetic and only exercise duplicate/pending detection.
Run normally or with -O; all test gates use unconditional exceptions.
"""
import ast
import hashlib
import json
from pathlib import Path
import runpy
import tempfile


HERE = Path(__file__).resolve().parent
API = runpy.run_path(str(HERE / "A26_verify_bundle.py"), run_name="A26_selftest_import")
Audit = API["Audit"]
TESTS = []


def require(condition, name):
    if not condition:
        raise RuntimeError(name)
    TESTS.append({"check": name, "status": "PASS"})


def rejects(function, name):
    try:
        function()
    except (ValueError, KeyError, TypeError):
        TESTS.append({"check": name, "status": "PASS"})
        return
    raise RuntimeError(name + " was accepted")


def main():
    tree = ast.parse((HERE / "A26_verify_bundle.py").read_text())
    require(not any(isinstance(node, ast.Assert) for node in ast.walk(tree)),
            "Verifier contains no assertion gates")
    rejects(lambda: API["parse_json"]('{"x":1,"x":2}'), "Reject duplicate JSON keys")
    rejects(lambda: API["parse_json"]('{"x":NaN}'), "Reject non-finite JSON constants")
    with tempfile.TemporaryDirectory(prefix="A26-selftest-") as dirname:
        root = Path(dirname)
        (root / "campaign").mkdir()
        (root / "campaign/checks").mkdir()
        (root / "a05").mkdir()
        (root / "campaign/proof.md").write_text("synthetic proof fixture\n")
        (root / "a05/partial.md").write_text("synthetic partial-result fixture\n")
        preservation = "campaign/checks/A26_required_files.json"
        (root / preservation).write_text(json.dumps({"required_paths": ["campaign/proof.md", "a05/partial.md"]}))
        items = []
        for name in ("campaign/proof.md", "a05/partial.md", preservation):
            data = (root / name).read_bytes()
            items.append({"path": name, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})

        def test_manifest(content, output=None):
            (root / "MANIFEST.json").write_text(json.dumps({"files": content}))
            audit = Audit(root, True)
            API["manifest"](audit, "MANIFEST.json", output)
            return audit

        audit = test_manifest(items)
        require(all(event["status"] == "PASS" for event in audit.events),
                "Valid synthetic manifest verifies hashes, lengths and partial-result coverage")
        audit = test_manifest(items[:1])
        require(any(event["status"] == "FAIL" and "covers" in event["label"] for event in audit.events),
                "Manifest omission of partial result fails coverage")
        corrupt = [dict(item) for item in items]
        corrupt[0]["sha256"] = "0" * 64
        audit = test_manifest(corrupt)
        require(any(event["status"] == "FAIL" and "SHA256" in event["label"] for event in audit.events),
                "Tampered manifest hash fails")
        corrupt = [dict(item) for item in items]
        corrupt[0]["bytes"] += 1
        audit = test_manifest(corrupt)
        require(any(event["status"] == "FAIL" and "byte count" in event["label"] for event in audit.events),
                "Wrong byte count fails")
        rejects(lambda: test_manifest(items + [items[0]]), "Duplicate manifest entries rejected")
        rejects(lambda: test_manifest([{"path": "../outside", "sha256": "0" * 64}]),
                "Manifest traversal path rejected")
        rejects(lambda: test_manifest([{"path": "MANIFEST.json", "sha256": "0" * 64}]),
                "Manifest self-reference rejected")
        rejects(lambda: test_manifest(items, root / "campaign/proof.md"),
                "Manifest cannot hash this run's live output")
        for name in ("/absolute", "../parent", "a//b", "./a", "a\\b"):
            rejects(lambda name=name: Audit(root).path(name), "Noncanonical path rejected: " + name)
        (root / "escape").symlink_to(root.parent)
        rejects(lambda: Audit(root).path("escape/file"), "Symlink escape rejected")
        audit = Audit(root)
        audit.read("campaign/proof.md")
        (root / "campaign/proof.md").write_text("mutated\n")
        rejects(lambda: audit.read("campaign/proof.md"), "Concurrent input mutation rejected")
        fixture_roster = {"requested_agents": 30, "agents": [
            {"number": 1, "task_name": "/synthetic/agent", "status": "pending"},
            {"number": 1, "task_name": "/synthetic/agent", "status": "pending"}]}
        (root / "campaign/AGENT_ROSTER.json").write_text(json.dumps(fixture_roster))
        audit = Audit(root, True)
        API["roster"](audit)
        require(sum(event["status"] == "FAIL" for event in audit.events) == 2,
                "Duplicate agent numbers and task names both fail")
        require(any(event["status"] == "PENDING" for event in audit.events),
                "Incomplete synthetic roster cannot claim 30-agent completion")
        # Regression: A30 may pin A26's completed report. The report belongs
        # in the digest lookup even though A26 does not scan its own text.
        (root / "campaign/reviews").mkdir()
        report_bytes = b"Synthetic completed A26 report.\n"
        report_hash = hashlib.sha256(report_bytes).hexdigest()
        (root / "campaign/reviews/A26.md").write_bytes(report_bytes)
        (root / "campaign/reviews/A30.md").write_text(
            "| `campaign/reviews/A26.md` | `" + report_hash + "` |\n")
        audit = Audit(root)
        API["report_versions"](audit)
        require(all(event["status"] == "PASS" for event in audit.events),
                "Sibling review can pin current A26 report without a false unresolved-hash gap")
        # A30's actual original acceptance must also survive an A26 repair.
        historical = HERE.parent / "history/A26_report_v1.md"
        (root / "campaign/history").mkdir()
        (root / "campaign/history/A26_report_v1.md").write_bytes(historical.read_bytes())
        original_hash = "9362d2651a2c5923a3eb90897a10774a4721be7d1d57df9b4cf9171eabf60274"
        (root / "campaign/reviews/A30.md").write_text(
            "| `campaign/reviews/A26.md` | `" + original_hash + "` |\n")
        audit = Audit(root)
        API["report_versions"](audit)
        require(all(event["status"] == "PASS" for event in audit.events)
                and any(event.get("preserved_path") == "campaign/history/A26_report_v1.md"
                        for event in audit.events),
                "Sibling review of original A26 snapshot resolves to preserved historical bytes")
    accepted = json.loads((HERE / "A13_tail_index_certificate.json").read_text())
    invalid = json.loads((HERE / "A24_optimized_falsepass.json").read_text())
    require(not API["interval_issues"](accepted), "Saved accepted A13 endpoint signs verify")
    require(len(API["interval_issues"](invalid)) == 6, "All six historical false-pass signs are rejected")
    result = {"status": "PASS", "scope": "Isolated synthetic fixtures; not a completed-agent or final-package claim",
              "verifier_sha256": hashlib.sha256((HERE / "A26_verify_bundle.py").read_bytes()).hexdigest(),
              "tests": TESTS}
    (HERE / "A26_selftest.json").write_text(json.dumps(result, indent=2) + "\n")
    print(str(len(TESTS)) + " self-tests passed")


if __name__ == "__main__":
    main()
