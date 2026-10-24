"""Command-line entry point for local, deny-by-default operation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .calibration_v2 import (
    CalibrationBundle,
    generate_calibration_report,
    load_calibration_bundle,
    load_calibration_freeze,
    load_calibration_input,
    publish_calibration_bundle,
)
from .models import Claim, ClaimKind
from .privacy import (
    PrivacyViolation,
    check_manifest_source_path,
    load_allowlist_manifest,
)
from .privacy_scan import load_scan_policy, scan_repository_files
from .publication import check_public_export
from .retrieval import search
from .store import ResearchStore
from .triggers import load_triggers, match_triggers


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="math-brain")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="initialize an empty local brain database")
    init.add_argument("database", type=Path)

    policy = sub.add_parser("policy", help="evaluate a source path without reading it")
    policy_sub = policy.add_subparsers(dest="policy_command", required=True)
    check = policy_sub.add_parser("check", help="check a file against a run-local manifest")
    check.add_argument("path", type=Path)
    check.add_argument("--manifest", type=Path, required=True)
    check.add_argument("--source-id", required=True)
    check.add_argument("--repository-root", type=Path, default=Path.cwd())

    scan = policy_sub.add_parser("scan", help="scan explicitly named repository files")
    scan.add_argument("paths", type=Path, nargs="+")
    scan.add_argument("--repository-root", type=Path, default=Path.cwd())
    scan.add_argument("--config", type=Path, default=Path("config/privacy.toml"))

    export = policy_sub.add_parser("export", help="validate one public artifact and sidecar")
    export.add_argument("artifact", type=Path)
    export.add_argument("--manifest", type=Path, required=True)
    export.add_argument("--repository-root", type=Path, default=Path.cwd())

    add = sub.add_parser("add-claim")
    add.add_argument("database", type=Path)
    add.add_argument("statement")
    add.add_argument("--kind", choices=[kind.value for kind in ClaimKind], required=True)
    add.add_argument("--domain", default="")

    recall = sub.add_parser("recall")
    recall.add_argument("database", type=Path)
    recall.add_argument("query")
    recall.add_argument("--limit", type=int, default=10)

    trigger = sub.add_parser("triggers")
    trigger.add_argument("text")
    trigger.add_argument("--config", type=Path, default=Path("config/triggers.toml"))

    calibration = sub.add_parser(
        "calibrate-v2",
        help="run public difficulty and shortcut calibration from a precommitted design",
    )
    calibration.add_argument("input", type=Path)
    calibration.add_argument("--state", type=Path, required=True)
    calibration.add_argument("--seed-file", type=Path, required=True)
    calibration.add_argument("--bundle", type=Path, required=True)

    verify_calibration = sub.add_parser(
        "verify-calibration-v2",
        help="recompute and verify persisted public calibration evidence",
    )
    verify_calibration.add_argument("input", type=Path)
    verify_calibration.add_argument("--state", type=Path, required=True)
    verify_calibration.add_argument("--seed-file", type=Path, required=True)
    verify_calibration.add_argument("--bundle", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "init":
        with ResearchStore(args.database):
            pass
        print(json.dumps({"database": str(args.database), "initialized": True}))
        return 0
    if args.command == "policy":
        if args.policy_command == "check":
            try:
                manifest = load_allowlist_manifest(
                    args.manifest,
                    repository_root=args.repository_root,
                )
                decision = check_manifest_source_path(
                    args.path,
                    manifest=manifest,
                    source_id=args.source_id,
                )
            except PrivacyViolation as exc:
                decision = {"allowed": False, "code": exc.code, "reason": str(exc)}
            else:
                decision = {
                    "allowed": decision.allowed,
                    "code": decision.code,
                    "reason": decision.reason,
                }
            print(json.dumps(decision, ensure_ascii=False))
            return 0 if decision["allowed"] else 2
        if args.policy_command == "scan":
            try:
                scan_policy = load_scan_policy(
                    args.config,
                    repository_root=args.repository_root,
                )
                findings = scan_repository_files(
                    repository_root=args.repository_root,
                    relative_paths=args.paths,
                    policy=scan_policy,
                )
            except PrivacyViolation as exc:
                payload = {"allowed": False, "code": exc.code, "reason": str(exc)}
                print(json.dumps(payload, ensure_ascii=False))
                return 2
            payload = {
                "allowed": not findings,
                "findings": [
                    {
                        "code": finding.code,
                        "path": finding.path,
                        "line": finding.line,
                        "column": finding.column,
                        "message": finding.message,
                    }
                    for finding in findings
                ],
            }
            print(json.dumps(payload, ensure_ascii=False))
            return 0 if not findings else 2
        if args.policy_command == "export":
            decision = check_public_export(
                args.artifact,
                manifest_path=args.manifest,
                repository_root=args.repository_root,
            )
            print(
                json.dumps(
                    {
                        "allowed": decision.allowed,
                        "code": decision.code,
                        "reason": decision.reason,
                    },
                    ensure_ascii=False,
                )
            )
            return 0 if decision.allowed else 2
        raise AssertionError("unreachable policy command")
    if args.command == "add-claim":
        claim = Claim(args.statement, ClaimKind(args.kind), domain=args.domain)
        with ResearchStore(args.database) as store:
            store.add_claim(claim)
        print(json.dumps({"claim_id": claim.id, "digest": claim.digest()}))
        return 0
    if args.command == "recall":
        with ResearchStore(args.database) as store:
            hits = search(
                args.query,
                nodes=store.iter_nodes(),
                edges=store.iter_edges(),
                limit=args.limit,
            )
        print(
            json.dumps(
                [
                    {
                        "id": hit.node.id,
                        "kind": hit.node.kind.value,
                        "title": hit.node.title,
                        "score": hit.total_score,
                        "warning_score": hit.warning_score,
                    }
                    for hit in hits
                ],
                ensure_ascii=False,
            )
        )
        return 0
    if args.command == "triggers":
        matches = match_triggers(args.text, load_triggers(args.config))
        print(
            json.dumps(
                [
                    {
                        "id": match.trigger.id,
                        "keywords": match.matched_keywords,
                        "action": match.trigger.action,
                    }
                    for match in matches
                ],
                ensure_ascii=False,
            )
        )
        return 0
    if args.command == "calibrate-v2":
        config, cases = load_calibration_input(args.input.read_text(encoding="utf-8"))
        state = load_calibration_freeze(args.state.read_text(encoding="utf-8"))
        seed = args.seed_file.read_text(encoding="utf-8").rstrip("\r\n")
        report = generate_calibration_report(
            cases,
            state=state,
            seed=seed,
            config=config,
        )
        frozen = (
            state.freeze(
                report,
                cases=cases,
                seed=seed,
                config=config,
            )
            if report.accepted
            else None
        )
        bundle = CalibrationBundle(report=report, frozen_state=frozen)
        published = publish_calibration_bundle(args.bundle, bundle)
        print(
            json.dumps(
                {
                    "accepted": report.accepted,
                    "bundle": str(args.bundle),
                    "bundle_digest": bundle.content_digest,
                    "published": published,
                    "report_digest": report.content_digest,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 0 if report.accepted else 2
    if args.command == "verify-calibration-v2":
        config, cases = load_calibration_input(args.input.read_text(encoding="utf-8"))
        state = load_calibration_freeze(args.state.read_text(encoding="utf-8"))
        seed = args.seed_file.read_text(encoding="utf-8").rstrip("\r\n")
        persisted = load_calibration_bundle(args.bundle.read_text(encoding="utf-8"))
        regenerated = generate_calibration_report(
            cases,
            state=state,
            seed=seed,
            config=config,
        )
        if persisted.report.content_digest != regenerated.content_digest:
            raise ValueError("persisted report does not match deterministic recomputation")
        expected_frozen = (
            state.freeze(
                regenerated,
                cases=cases,
                seed=seed,
                config=config,
            )
            if regenerated.accepted
            else None
        )
        expected_bundle = CalibrationBundle(
            report=regenerated,
            frozen_state=expected_frozen,
        )
        if persisted.canonical_json() != expected_bundle.canonical_json():
            raise ValueError("persisted bundle does not match deterministic recomputation")
        print(
            json.dumps(
                {
                    "accepted": persisted.report.accepted,
                    "bundle_digest": persisted.content_digest,
                    "report_digest": persisted.report.content_digest,
                    "verified": True,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 0
    raise AssertionError("unreachable")


if __name__ == "__main__":
    raise SystemExit(main())
