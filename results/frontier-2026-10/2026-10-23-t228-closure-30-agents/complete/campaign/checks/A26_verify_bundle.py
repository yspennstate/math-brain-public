#!/usr/bin/env python3
"""Local, standard-library integrity and reproducibility audit for the campaign.

Examples (run from a workspace/package root):
  python campaign/checks/A26_verify_bundle.py current
  python campaign/checks/A26_verify_bundle.py proof --output /tmp/A26-proof.json
  python campaign/checks/A26_verify_bundle.py --root bundle --manifest MANIFEST.json

`current` checks the available roster without pretending unfinished agents have
completed. `proof` checks mathematical evidence and provenance, omitting the
roster. Either mode may take --manifest; that makes final 30-agent completion
and complete manifest coverage mandatory. Exit 1 means failed integrity or an
unresolved final-package gap; current/proof exit 0 may still report pending work.

This is not a proof assistant or a remote-repository verification. A08 is rerun
on exact temporary copies with optimization disabled. A13's saved intervals
are checked with Fraction; its expensive quadrature is NOT rerun here. The
current A13 executable must reject -O, -OO, and PYTHONOPTIMIZE before reading
even a nonexistent proof. The old optimized false-pass fixture is rejected.

No verification gate uses a Python assert statement. Checker subprocesses and
their generated output stay in a temporary directory. Only --output writes a
user-selected audit result. Never list that live output or MANIFEST.json in
the manifest being checked: those would create self-reference/update cycles.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from fractions import Fraction


CORPUS_ROOTS = ("campaign", "a01", "a02", "a03", "a04", "a05", "a06")
PROOF_SHA256 = {
    "campaign/proofs/T228_EXPLICIT_CLOSURE.md": "a1dbdbb1e99a85749143f44dd8b7d7e264fb550d285c5667f69f1a35ff87c38f",
    "campaign/proofs/T228_NONZERO_TEACHER.md": "f95fa6fade82ba0dca4dab8e311fc61bb57b3267f3953b465c94228cb1315933",
    "campaign/proofs/T228_INDEX_DEPENDENCE.md": "4fc5a1c72f9ea24b1408c99aa1fc01c10492d1e816a59e2e3227addf8609e6ee",
    "campaign/proofs/T228_MOMENT_DYNAMICS.md": "e2ba8992e95ac4f43e2036fc9875761870a965038027942729347edae436c970",
    "campaign/proofs/T228_BATCH_TWO.md": "f302b97190ae773c1b6eee1a96c48ed7b46907c32091ea8bfc9e1afd8988bcbd",
    "campaign/checks/A08_reviewed_source.md": "a1dbdbb1e99a85749143f44dd8b7d7e264fb550d285c5667f69f1a35ff87c38f",
    "campaign/checks/A08_exact_checker.py": "276aba76fbc17e8b1efbaed5c86d19338d5dda0bd7f283edb593a0e89658dbed",
    "campaign/checks/A08_exact_checker.out": "0ce9659af85da24205f7156b1ebd84f08e1b3f00e2669f8c2a80ddee2e68079c",
    "campaign/checks/A13_tail_index_certificate.py": "ce9e6b42e901d7ffa06c11cbc6e35e6f2ad8b3216e957896374a9e4527a0bb58",
    "campaign/history/A13_tail_index_certificate_v1.py": "f3b81bb6b7b3520c842e21dfa7faa919c104e0ff21b68e44d85864b66d359ff4",
    "campaign/history/A02_CONTINUOUS_KERNEL_EXTENSION_v1.md": "0eb859b59c44b6396b65c98b90b5874eab1bfdf8262dc1710dfc024b4efe0543",
    "campaign/history/A05_ERM_BRIDGE_v1.md": "c7fcd6fdfa4b0a3d0c7af44e4760db75fd59fabd6c2114629c6bc0b64677144f",
    "a02/CONTINUOUS_KERNEL_EXTENSION.md": "5cd1bdd401d2efbd15433e9fa5fc1834e792424fa70fba552da85b776ef45566",
    "a05/ERM_BRIDGE.md": "97eeb783f610ea4ce4ead20c547a0ec65ebc4ca0320d7a07e4d38c05bf936d96",
}
REGISTRY_GIT_BLOB = "b8d4607e60eafcce5b3e8286cf882e8931737bd6"
REGISTRY_SHA256 = "c1a7636d5ef95888a26e92b36a017e2a2aae72d7140de9f6d39c695c67d2d3b0"
E_V1_SHA256 = "9d0ef065e10642dbc8967870bdc3f368300424659f9316456355775264133287"
HISTORICAL_ALIAS = {
    ("campaign/reviews/A26.md", "9362d2651a2c5923a3eb90897a10774a4721be7d1d57df9b4cf9171eabf60274"):
        "campaign/history/A26_report_v1.md",
    ("a02/CONTINUOUS_KERNEL_EXTENSION.md", "0eb859b59c44b6396b65c98b90b5874eab1bfdf8262dc1710dfc024b4efe0543"):
        "campaign/history/A02_CONTINUOUS_KERNEL_EXTENSION_v1.md",
    ("a06/T421_conditional_classification.md", "f7e1a52a4126001fa26180e1b2832d215eeb4e97d9d161a65ae6136202096400"):
        "campaign/history/A06_T421_conditional_classification_v1.md",
    ("a06/CLAIMS.jsonl", "bddd571a75d22177c064194ff1381c682f1ae85e1d19336d9f29e1f96ad35784"):
        "campaign/history/A06_CLAIMS_v1.jsonl",
}
SHA256_RE = re.compile(r"\b[0-9a-f]{64}\b")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError("duplicate JSON key: " + key)
        obj[key] = value
    return obj


def invalid_constant(value):
    raise ValueError("non-finite JSON number: " + value)


def parse_json(text):
    return json.loads(text, object_pairs_hook=unique_object, parse_constant=invalid_constant)


class Audit:
    def __init__(self, root, strict=False):
        self.root = root.resolve()
        self.strict = strict
        self.events = []
        self.details = {}
        self.observed = {}

    def event(self, status, label, **details):
        self.events.append({"status": status, "label": label, **details})

    def check(self, condition, label, **details):
        self.event("PASS" if condition else "FAIL", label, **details)
        return bool(condition)

    def gap(self, label, **details):
        self.event("PENDING", label, **details)

    def path(self, name):
        # Names inside evidence and manifests must be canonical relative paths.
        if not isinstance(name, str) or not name or "\\" in name:
            raise ValueError("invalid relative path: " + repr(name))
        pure = PurePosixPath(name)
        if pure.is_absolute() or ".." in pure.parts or str(pure) != name:
            raise ValueError("noncanonical relative path: " + repr(name))
        result = self.root.joinpath(*pure.parts)
        if not result.resolve().is_relative_to(self.root):
            raise ValueError("path escapes package root: " + name)
        return result

    def read(self, name):
        data = self.path(name).read_bytes()
        digest = sha256(data)
        previous = self.observed.setdefault(name, digest)
        if previous != digest:
            raise ValueError("file changed during audit: " + name)
        return data

    def json(self, name):
        return parse_json(self.read(name).decode("utf-8"))

    def hash_check(self, name, expected, label=None, historical=False):
        actual = sha256(self.read(name))
        if actual == expected:
            self.check(True, label or "SHA256 " + name, sha256=actual)
            return True
        alias = HISTORICAL_ALIAS.get((name, expected)) if historical else None
        if alias and self.path(alias).is_file() and sha256(self.read(alias)) == expected:
            self.event("PASS", label or "historical SHA256 " + name,
                       reviewed_path=name, preserved_path=alias, reviewed_sha256=expected,
                       current_sha256=actual, scope="preserved old version; not current bytes")
            return True
        self.check(False, label or "SHA256 " + name, expected=expected, actual=actual)
        return False

    def stage(self, name, function):
        try:
            function()
        except (OSError, ValueError, KeyError, TypeError, IndexError, subprocess.SubprocessError) as error:
            self.event("FAIL", name, exception=type(error).__name__, message=str(error))

    def corpus_files(self):
        result = []
        for dirname in CORPUS_ROOTS:
            base = self.root / dirname
            if not base.is_dir():
                continue
            for path in base.rglob("*"):
                if not path.is_file():
                    continue
                rel = path.relative_to(self.root)
                if any(p in {"__pycache__", ".git", ".pytest_cache"} for p in rel.parts):
                    continue
                if path.suffix in {".pyc", ".pyo", ".aux", ".log"} or path.name.endswith(".synctex.gz"):
                    continue
                result.append(rel.as_posix())
        return sorted(result)


def proof_and_record_pins(audit):
    for name, expected in PROOF_SHA256.items():
        audit.hash_check(name, expected)
    a16 = audit.json("campaign/manuscript/A16_build_verification.json")
    for name, expected in a16["source_and_output_sha256"].items():
        audit.hash_check(name, expected, "A16 build pin " + name)
    mapping = audit.json("campaign/T228_OBLIGATION_MAP.json")
    for item in mapping["provenance"]["reviewed_proofs"]:
        audit.hash_check(item["path"], item["sha256"], "A18 proof pin " + item["path"])
    a02 = audit.json("a02/MANIFEST.json")
    for item in a02:
        name = "a02/" + item["file"]
        audit.hash_check(name, item["sha256"], "A02 historical manifest " + name, historical=True)
        checked_name = HISTORICAL_ALIAS.get((name, item["sha256"]), name)
        audit.check(len(audit.read(checked_name)) == item["bytes"], "A02 manifest byte count " + checked_name)
    a03 = audit.json("a03/MANIFEST.json")
    for name, expected in a03["files"].items():
        audit.hash_check("a03/" + name, expected, "A03 SHA256 manifest " + name)


def source_pins(audit):
    exceptions_path = audit.path("campaign/SOURCE_PIN_EXCEPTIONS.json")
    exceptions = {}
    if exceptions_path.is_file():
        for item in audit.json("campaign/SOURCE_PIN_EXCEPTIONS.json")["exceptions"]:
            key = (item["path"], item["expected_git_blob_sha1"])
            if key in exceptions:
                raise ValueError("duplicate source-pin exception: " + str(key))
            exceptions[key] = item
    used = set()
    recoveries = {}
    recovery_path = audit.path("campaign/SOURCE_PIN_RECOVERY.json")
    if recovery_path.is_file():
        for item in audit.json("campaign/SOURCE_PIN_RECOVERY.json")["recoveries"]:
            key = (item["local_path"], item["expected_git_blob_sha1"])
            if key in recoveries:
                raise ValueError("duplicate source-pin recovery: " + str(key))
            recoveries[key] = item
    results = []

    def verify(name, expected, record, allow_one_lf=False):
        data = audit.read(name)
        raw = git_blob(data)
        normalized = git_blob(data[:-1]) if data.endswith(b"\n") else None
        row = {"path": name, "pin_record": record, "expected_git_blob_sha1": expected,
               "raw_git_blob_sha1": raw, "local_sha256": sha256(data), "bytes": len(data)}
        if raw == expected:
            row["pin_status"] = "RAW_MATCH"
            audit.check(True, "source Git blob " + name, **row)
        elif allow_one_lf and normalized == expected:
            row.update(pin_status="MATCH_AFTER_EXACTLY_ONE_TERMINAL_LF_REMOVAL",
                       normalized_git_blob_sha1=normalized)
            audit.event("PASS", "normalized source Git blob " + name,
                        normalization="comparison only: remove exactly one terminal LF byte", **row)
        else:
            row.update(pin_status="UNVERIFIED_REMOTE_PIN", minus_one_lf_git_blob_sha1=normalized)
            recovery = recoveries.get((name, expected))
            exception = exceptions.get((name, expected))
            if recovery is not None:
                recovered = audit.read(recovery["recovered_path"])
                valid = (recovery["local_sha256"] == sha256(data)
                         and recovery["recovered_sha256"] == sha256(recovered)
                         and recovery["recovered_bytes"] == len(recovered)
                         and git_blob(recovered) == expected
                         and recovered.replace(b"\r\n", b"\n") + b"\n" == data
                         and recovery.get("status") == "EXACT_REMOTE_BYTES_RECOVERED_SEPARATELY")
                audit.check(valid, "recovered exact Git bytes and declared transform " + name,
                            recovered_path=recovery["recovered_path"],
                            local_sha256=sha256(data), recovered_sha256=sha256(recovered),
                            source_bytes_modified=False)
                if valid:
                    row.update(pin_status="EXACT_GIT_BYTES_RECOVERED_AND_NORMALIZATION_VERIFIED",
                               recovered_path=recovery["recovered_path"],
                               recovered_git_blob_sha1=git_blob(recovered),
                               transform="replace CRLF with LF, then append exactly one terminal LF")
            elif exception is not None:
                used.add((name, expected))
                valid = (exception.get("local_sha256") == sha256(data)
                         and exception.get("status") == "UNVERIFIED_REMOTE_PIN"
                         and isinstance(exception.get("reason"), str)
                         and bool(exception["reason"].strip()))
                audit.check(valid, "source-pin exception binds exact local bytes " + name)
                if valid:
                    audit.event("WARN", "documented unverified remote source pin " + name,
                                reason=exception["reason"], **row)
            else:
                audit.gap("unreconciled source Git blob " + name, **row)
        results.append(row)

    a01 = audit.json("a01/SOURCE_MANIFEST.json")
    audit.check(len(a01) == 19, "A01 recovered source count is exactly 19")
    audit.check(len({x["local"] for x in a01}) == len(a01), "A01 source paths are unique")
    for item in a01:
        verify("a01/" + item["local"], item["blob_sha"], "a01/SOURCE_MANIFEST.json")
    payloads = audit.json("a01/SOURCE_PAYLOADS.json")
    audit.check(len(payloads) == len(a01), "A01 payload count matches manifest")
    by_path = {x["local"]: x for x in a01}
    audit.check({item["name"] for item in payloads} == set(by_path),
                "A01 payload names cover all 19 unique manifest paths")
    for item in payloads:
        name = item["name"]
        data = item["content"].encode("utf-8")
        audit.check(name in by_path and data == audit.read("a01/" + name)
                    and git_blob(data) == item["sha"] == by_path[name]["blob_sha"],
                    "A01 embedded payload agrees with exact recovered file " + name)
    for record in ("a02/SOURCE_PINS.json", "a02/COMPLETE_SOURCE_PINS.json"):
        content = audit.json(record)
        for item in content if isinstance(content, list) else content["files"]:
            name = "a02/" + (item.get("local") or item["name"])
            verify(name, item.get("blob_sha") or item["sha"], record, allow_one_lf=True)
    a06 = audit.json("a06/SOURCE_PINS.json")
    for key, filename in (("dossier_blob", "DOSSIER.md"), ("moves_blob", "moves.jsonl")):
        verify("a06/source/frontier/rows/T421/" + filename, a06[key],
               "a06/SOURCE_PINS.json", allow_one_lf=True)
    audit.check(a06["list_blob"] == REGISTRY_GIT_BLOB,
                "A06 registry metadata points to the full registry, not its single-row extract")
    for key in exceptions.keys() - used:
        audit.event("WARN", "unused source-pin exception", path=key[0], expected_git_blob_sha1=key[1])
    audit.details["source_pin_results"] = results


def registry_semantics(audit):
    raw = audit.read("a03/registry422.jsonl")
    audit.check(sha256(raw) == REGISTRY_SHA256, "full local registry exact SHA256")
    audit.check(git_blob(raw) != REGISTRY_GIT_BLOB and raw.endswith(b"\n")
                and git_blob(raw[:-1]) == REGISTRY_GIT_BLOB,
                "full registry pin requires exactly one terminal LF removal",
                raw_git_blob_sha1=git_blob(raw), source_bytes_modified=False)
    rows = [parse_json(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    ids = [row["problem_id"] for row in rows]
    audit.check(len(rows) == 422 and len(set(ids)) == 422, "422 unique registry problem IDs")
    lookup = dict(zip(ids, rows))
    for name, expected_id in (("campaign/sources/T228_REGISTRY.json", "T228"),
                              ("a02/T336_REGISTRY.json", "T336"),
                              ("a06/source/top200_probability_2026_10_14/list.jsonl", "T421")):
        row = audit.json(name)
        audit.check(row == lookup[expected_id], "exact extracted registry object " + expected_id,
                    path=name, comparison="all parsed keys and values; duplicate keys forbidden")
    for row in audit.json("a03/selected_registry_rows.json"):
        audit.check(row == lookup[row["problem_id"]], "selected registry row " + row["problem_id"])
    mapping = audit.json("campaign/T228_OBLIGATION_MAP.json")
    row = lookup["T228"]
    audit.check(mapping["registry_statement"] == row["statement"]
                and mapping["registry_title"] == row["title"]
                and mapping["registry_audit_route"] == row["audit"]["solver_shape"]
                and mapping["registry_audit_replacement"] == row["audit"]["replace_with"],
                "A18 obligation map preserves the literal operative registry fields")
    audit.details["registry"] = {"rows": len(rows), "raw_sha256": sha256(raw),
                                 "normalized_git_blob_sha1": git_blob(raw[:-1])}


def report_versions(audit):
    external = {}
    external_path = audit.path("campaign/EXTERNAL_REFERENCES.json")
    if external_path.is_file():
        for item in audit.json("campaign/EXTERNAL_REFERENCES.json")["references"]:
            digest = item["sha256"]
            valid = (isinstance(digest, str) and SHA256_RE.fullmatch(digest)
                     and isinstance(item.get("url"), str) and item["url"].startswith("https://")
                     and isinstance(item.get("reason"), str) and bool(item["reason"].strip())
                     and item.get("status") == "EXTERNAL_REFERENCE_NOT_BUNDLED")
            if not valid or digest in external:
                raise ValueError("invalid or duplicate external-reference declaration: " + str(digest))
            external[digest] = item
    historical_omissions = {}
    correction_path = audit.path("campaign/CORRECTIONS.json")
    if correction_path.is_file():
        corrections = audit.json("campaign/CORRECTIONS.json")
        corrections = corrections["corrections"] if isinstance(corrections, dict) else corrections
        for item in corrections:
            for prefix in ("current", "historical"):
                path, digest = item.get(prefix + "_path"), item.get(prefix + "_sha256")
                if path is not None and digest is not None:
                    audit.hash_check(path, digest, "correction ledger " + prefix + " version " + path)
            if item.get("status") == "HISTORICAL_DRAFT_BYTES_NOT_RETAINED":
                digest = item.get("historical_sha256")
                valid = (digest == E_V1_SHA256
                         and item.get("current_path") == "campaign/proofs/T228_EXPLICIT_CLOSURE.md"
                         and item.get("current_sha256") == PROOF_SHA256[item["current_path"]]
                         and isinstance(item.get("reason"), str) and bool(item["reason"].strip())
                         and not item.get("historical_path"))
                if not valid or digest in historical_omissions:
                    raise ValueError("invalid historical-draft omission declaration")
                historical_omissions[digest] = item
    digest_paths = {}
    for name in audit.corpus_files():
        # A sibling review can legitimately pin this completed report. Only
        # live A26 check outputs are excluded from the digest index; we still
        # skip scanning A26's own report below to avoid self-reference.
        if name.startswith("campaign/checks/A26_"):
            continue
        digest_paths.setdefault(sha256(audit.read(name)), []).append(name)
    table_count = 0
    unresolved = []
    for path in sorted(audit.path("campaign/reviews").glob("A*.md")):
        if path.name == "A26.md":
            continue
        name = path.relative_to(audit.root).as_posix()
        lines = audit.read(name).decode("utf-8").splitlines()
        for number, line in enumerate(lines, 1):
            hashes = SHA256_RE.findall(line)
            if not hashes:
                continue
            paths = re.findall(r"`((?:campaign|a0[1-6])/[^`]+)`", line)
            if line.startswith("|") and len(paths) == 1 and len(hashes) == 1:
                table_count += 1
                omitted = external.get(hashes[0])
                if (omitted is not None and omitted.get("original_path") == paths[0]
                        and not audit.path(paths[0]).is_file()):
                    audit.event("WARN", "declared external cache absent at its old local path",
                                path=paths[0], sha256=hashes[0], url=omitted["url"], report=name)
                else:
                    audit.hash_check(paths[0], hashes[0], f"review version pin {name}:{number}", historical=True)
            for digest in hashes:
                if digest not in digest_paths:
                    # A21 explicitly pins the raw JSON record without its terminator.
                    t421 = audit.read("a06/source/top200_probability_2026_10_14/list.jsonl")
                    record_hashes = {sha256(x) for x in t421.splitlines() if x.strip()}
                    if digest in record_hashes:
                        continue
                    unresolved.append({"report": name, "line": number, "sha256": digest})
    undocumented = []
    for item in unresolved:
        digest = item["sha256"]
        if digest in external:
            declaration = external[digest]
            audit.event("WARN", "external primary-source cache intentionally not bundled",
                        **item, url=declaration["url"], reason=declaration["reason"],
                        bytes_reverified_in_this_audit=False)
        elif digest in historical_omissions:
            declaration = historical_omissions[digest]
            audit.event("WARN", "historical explicit-proof draft bytes not retained",
                        **item, current_path=declaration["current_path"],
                        current_sha256=declaration["current_sha256"], reason=declaration["reason"],
                        historical_bytes_verified=False)
        else:
            undocumented.append(item)
    historical = [item for item in undocumented if item["sha256"] == E_V1_SHA256]
    other = [item for item in undocumented if item["sha256"] != E_V1_SHA256]
    if historical:
        audit.gap("original explicit-proof Version 1 bytes not recovered", references=historical,
                  scope="current Version 2 is independently pinned; do not equate the two versions")
    if other:
        audit.gap("review hashes without recovered whole-file or declared excerpt bytes", references=other)
    audit.check(table_count > 0, "review Markdown file/hash tables checked", entries=table_count)
    audit.details["review_sha256_reference_count_unresolved"] = len(undocumented)
    audit.details["review_sha256_reference_count_explicitly_not_bundled"] = len(unresolved) - len(undocumented)


def run_a08(audit):
    source = audit.read("campaign/checks/A08_exact_checker.py")
    proof = audit.read("campaign/checks/A08_reviewed_source.md")
    expected_output = audit.read("campaign/checks/A08_exact_checker.out")
    with tempfile.TemporaryDirectory(prefix="A26-exact-") as dirname:
        work = Path(dirname)
        script = work / "A08_exact_checker.py"
        script.write_bytes(source)
        (work / "A08_reviewed_source.md").write_bytes(proof)
        result = subprocess.run([sys.executable, "-I", "-B", str(script)], cwd=work,
                                capture_output=True, timeout=60)
        output = script.with_suffix(".out")
        reproduced = output.read_bytes() if output.exists() else b""
        passed = result.returncode == 0 and not result.stderr and reproduced == expected_output
        audit.check(passed, "A08 exact rational checker re-executed on isolated exact copies",
                    returncode=result.returncode, stdout_sha256=sha256(result.stdout),
                    output_sha256=sha256(reproduced), stderr=result.stderr.decode("utf-8", "replace"))
        lines = result.stdout.decode("utf-8").splitlines()
        audit.check(result.stdout == expected_output
                    and sum(line.startswith("PASS ") for line in lines) == 37
                    and lines[-1:] == ["All 37 exact checks passed."],
                    "A08 transcript and all 37 checks reproduce byte-for-byte")
    audit.check(audit.read("campaign/checks/A08_exact_checker.out") == expected_output,
                "A08 author output was not overwritten")


def interval_issues(certificate):
    """Independent rational validation of the saved certificate's sign evidence."""
    issues = []
    expected = {"0.99": ("1.10928", "1.10929"), "1": ("1.09082", "1.09083"),
                "1.01": ("1.07272", "1.07273")}
    cases = certificate["cases"]
    if len(cases) != 3 or {x["eta"] for x in cases} != set(expected):
        issues.append("three unique requested learning rates required")
    for case in cases:
        bracket = tuple(case["strict_root_bracket"])
        if bracket != expected.get(case["eta"]) or Fraction(bracket[1]) - Fraction(bracket[0]) != Fraction(1, 100000):
            issues.append("wrong strict bracket for " + case["eta"])
        endpoints = case["endpoint_certificates"]
        if len(endpoints) != 2:
            issues.append("two endpoints required")
            continue
        for i, endpoint in enumerate(endpoints):
            lo, hi = map(Fraction, endpoint["h_interval"])
            tlo, thi = map(Fraction, endpoint["normalized_trapezoid_interval"])
            error, tail = map(Fraction, (endpoint["quadrature_error_up"], endpoint["tail_error_up"]))
            if not (0 < lo <= hi and 0 < tlo <= thi and 0 < error and 0 < tail):
                issues.append("invalid interval ordering/allowance")
            if not (lo <= tlo - error and hi >= thi + error + tail):
                issues.append("h interval fails to include the stated error allowances")
            if endpoint["p"] != bracket[i]:
                issues.append("endpoint exponent does not match root bracket")
            if not (hi < 1 if i == 0 else lo > 1):
                issues.append("endpoint sign is not certified for eta=" + case["eta"])
    cal_lo, cal_hi = map(Fraction, certificate["calibration"]["h_interval"])
    if not cal_lo <= 2 <= cal_hi:
        issues.append("calibration fails to enclose h_1(2)=2")
    return issues


def a13_evidence(audit):
    old_script = sha256(audit.read("campaign/history/A13_tail_index_certificate_v1.py"))
    current_script = audit.read("campaign/checks/A13_tail_index_certificate.py")
    proof_hash = PROOF_SHA256["campaign/proofs/T228_EXPLICIT_CLOSURE.md"]
    paths = ["campaign/checks/A13_tail_index_certificate.json",
             "campaign/checks/A24_replayed_certificate.json"]
    for name in paths:
        if not audit.path(name).is_file():
            audit.gap("saved interval certificate not yet present", path=name)
            continue
        certificate = audit.json(name)
        issues = interval_issues(certificate)
        audit.check(certificate["status"] == "PASS" and not issues,
                    "saved A13 endpoint sign evidence " + name, issues=issues,
                    quadrature_reexecuted=False)
        audit.check(certificate["source_proof_sha256"] == proof_hash
                    and certificate["script_sha256"] in {old_script, sha256(current_script)},
                    "A13 source/script provenance " + name,
                    script_version="historical v1" if certificate["script_sha256"] == old_script else "hardened current")
        audit.check(certificate["grid_denominator"] == 10000 and certificate["decimal_precision"] == 40,
                    "A13 declared precision/mesh " + name)
    bad_name = "campaign/checks/A24_optimized_falsepass.json"
    fixture = audit.json(bad_name)
    rejected = interval_issues(fixture)
    audit.check(fixture["status"] == "PASS" and len(rejected) >= 6,
                "historical A24 false-pass fixture is INVALID evidence and independently rejected",
                path=bad_name, rejected_issues=rejected,
                classification="INVALID_HISTORICAL_OPTIMIZED_FALSEPASS")
    with tempfile.TemporaryDirectory(prefix="A26-optimization-") as dirname:
        work = Path(dirname)
        script = work / "A13_tail_index_certificate.py"
        script.write_bytes(current_script)
        for flags, optimize in ((["-I", "-O", "-B"], None), (["-I", "-OO", "-B"], None), (["-B"], "1")):
            target = work / ("must_not_exist_" + str(optimize or flags[1]) + ".json")
            env = dict(os.environ)
            if optimize is not None:
                env["PYTHONOPTIMIZE"] = optimize
            args = [sys.executable, *flags, str(script), "--proof", str(work / "nonexistent.md"),
                    "--output", str(target), "--grid-denominator", "10"]
            result = subprocess.run(args, cwd=work, env=env, capture_output=True, timeout=15)
            rejected_early = (result.returncode != 0 and not target.exists()
                              and b"Certificate checks require assertions enabled" in result.stderr
                              and b"FileNotFoundError" not in result.stderr)
            audit.check(rejected_early, "current A13 unconditionally rejects optimized execution",
                        flags=flags, PYTHONOPTIMIZE=optimize, returncode=result.returncode,
                        output_created=target.exists())


def roster(audit):
    final = "campaign/AGENT_ROSTER.json"
    name = final if audit.path(final).is_file() else "campaign/admin/AGENT_ROSTER_IN_PROGRESS.json"
    record = audit.json(name)
    agents = record["agents"]
    numbers = [x["number"] for x in agents]
    names = [x["task_name"] for x in agents]
    audit.check(record["requested_agents"] == 30, "roster records the request for 30 agents")
    audit.check(all(type(n) is int and 1 <= n <= 30 for n in numbers)
                and len(set(numbers)) == len(numbers), "roster agent numbers are unique and in 1..30")
    audit.check(all(isinstance(n, str) and n.strip() for n in names)
                and len(set(names)) == len(names), "roster task names are nonempty and distinct")
    completed = []
    reports = []
    for agent in agents:
        if agent.get("status") != "completed":
            continue
        completed.append(agent["number"])
        report = agent.get("report_path")
        digest = agent.get("report_sha256")
        if not isinstance(report, str) or not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
            audit.check(False, "completed agent lacks exact report path/hash", number=agent["number"])
            continue
        reports.append(report)
        audit.hash_check(report, digest, "completed agent report " + str(agent["number"]))
    audit.check(len(reports) == len(set(reports)), "completed agents have distinct report files")
    if set(numbers) != set(range(1, 31)) or set(completed) != set(range(1, 31)):
        audit.gap("30-agent final completion is not yet evidenced", roster=name,
                  roster_count=len(agents), completed_count=len(completed),
                  missing_numbers=sorted(set(range(1, 31)) - set(numbers)),
                  not_completed_numbers=sorted(set(range(1, 31)) - set(completed)))
    else:
        audit.check(True, "30 distinct agents each have completed status and an exact report hash")
    audit.details["roster"] = {"path": name, "agent_count": len(agents), "completed_count": len(completed),
                               "backend_runtime_model_independently_verified": False}


def manifest(audit, name, output):
    document = audit.json(name)
    items = document["files"] if isinstance(document, dict) else document
    if isinstance(items, dict):
        items = [{"path": path, "sha256": digest} for path, digest in items.items()]
    if not isinstance(items, list) or not items:
        raise ValueError("manifest must contain a nonempty files list or map")
    seen = set()
    for item in items:
        path, expected = item["path"], item["sha256"]
        audit.path(path)
        if path in seen:
            raise ValueError("duplicate manifest path: " + path)
        seen.add(path)
        if path == name or output is not None and audit.path(path).resolve() == output.resolve():
            raise ValueError("manifest includes itself or this run's output: " + path)
        if not isinstance(expected, str) or not SHA256_RE.fullmatch(expected):
            raise ValueError("invalid manifest SHA256: " + path)
        audit.hash_check(path, expected, "final manifest SHA256 " + path)
        if "bytes" in item:
            audit.check(type(item["bytes"]) is int and item["bytes"] >= 0
                        and len(audit.read(path)) == item["bytes"], "final manifest byte count " + path)
    required = set(audit.corpus_files()) - {name}
    preservation = audit.json("campaign/checks/A26_required_files.json")
    for path in preservation["required_paths"]:
        audit.path(path)
        required.add(path)
    external_path = audit.path("campaign/EXTERNAL_REFERENCES.json")
    if external_path.is_file():
        for item in audit.json("campaign/EXTERNAL_REFERENCES.json")["references"]:
            original = item.get("original_path", "")
            if original and not PurePosixPath(original).is_absolute():
                audit.path(original)
                required.discard(original)
    if output is not None and output.resolve().is_relative_to(audit.root):
        required.discard(output.resolve().relative_to(audit.root).as_posix())
    missing = sorted(required - seen)
    audit.check(not missing, "manifest covers all substantive campaign/a01-a06 files",
                missing_paths=missing, excluded="Python caches and TeX build auxiliaries; manifest/live audit output")
    audit.details["manifest"] = {"path": name, "entry_count": len(items), "required_corpus_files": len(required),
                                 "sha256": sha256(audit.read(name))}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("mode", nargs="?", choices=("current", "proof"), default="current")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--manifest", metavar="RELATIVE_PATH", help="enable strict final-package checks")
    parser.add_argument("--output", type=Path, help="write full audit JSON; do not include this live file in the manifest")
    args = parser.parse_args()
    audit = Audit(args.root, strict=args.manifest is not None)
    # Avoid overwriting source evidence by accidental output-path reuse.
    if args.output is not None:
        resolved_output = args.output.resolve()
        if resolved_output.is_relative_to(audit.root):
            relative = resolved_output.relative_to(audit.root).as_posix()
            if not (relative.startswith("campaign/checks/A26_") and relative.endswith(".json")):
                parser.error("an output inside the corpus must be campaign/checks/A26_*.json")
        if resolved_output == Path(__file__).resolve():
            parser.error("output cannot overwrite this verifier")
    audit.stage("key proof and record pins", lambda: proof_and_record_pins(audit))
    audit.stage("source pins", lambda: source_pins(audit))
    audit.stage("exact registry semantics", lambda: registry_semantics(audit))
    audit.stage("report-version provenance", lambda: report_versions(audit))
    audit.stage("A08 replay", lambda: run_a08(audit))
    audit.stage("A13 historical/current certificate boundary", lambda: a13_evidence(audit))
    if args.mode == "current" or audit.strict:
        audit.stage("agent roster", lambda: roster(audit))
    if args.manifest:
        audit.stage("final manifest", lambda: manifest(audit, args.manifest, args.output))
    else:
        audit.gap("final file manifest was not requested; final package is not certified")
    # Detect an author editing any previously read evidence during the audit.
    for name, digest in list(audit.observed.items()):
        try:
            if sha256(audit.path(name).read_bytes()) != digest:
                audit.check(False, "file changed during audit", path=name)
        except OSError as error:
            audit.check(False, "file disappeared during audit", path=name, message=str(error))
    counts = {status: sum(x["status"] == status for x in audit.events)
              for status in ("PASS", "WARN", "PENDING", "FAIL")}
    failed = counts["FAIL"] > 0 or audit.strict and counts["PENDING"] > 0
    status = "FAIL" if failed else "PASS_WITH_GAPS" if counts["PENDING"] else "PASS_WITH_WARNINGS" if counts["WARN"] else "PASS"
    result = {"audit": "A26", "status": status, "mode": args.mode, "strict_final_manifest": audit.strict,
              "utc": datetime.now(timezone.utc).isoformat(), "python": platform.python_version(),
              "verifier_sha256": sha256(Path(__file__).read_bytes()), "root": str(audit.root),
              "counts": counts, "details": audit.details, "events": audit.events,
              "scope": "Local byte integrity, saved evidence consistency, A08 replay, optimized-A13 rejection; not formal proof or remote-state verification."}
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("audit", "status", "mode", "strict_final_manifest", "counts")}, sort_keys=True))
    for event in audit.events:
        if event["status"] != "PASS":
            print(event["status"] + ": " + event["label"])
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
