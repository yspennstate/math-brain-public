#!/usr/bin/env python3
"""Validate FEI coordination records without claiming to verify mathematics.

Uses only the standard library. Reads local JSON; never authenticates, uploads,
changes Git, or writes research state. Exit 1 means a metadata/consistency error.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath

STATUSES = {
    "OPEN", "PROVED_IN_SOURCE", "REFUTED", "CANDIDATE_UNPROVED",
    "EQUIVALENT_REFORMULATION", "CONDITIONAL_IN_SOURCE",
    "FINITE_CHECK_IN_SOURCE", "NEEDS_REVALIDATION",
}
POSITIVE_STATUSES = {"PROVED_IN_SOURCE", "EQUIVALENT_REFORMULATION"}
ROLES = {"positive_result", "definition_only", "negative_result",
         "historical_context", "assumption", "current_candidate"}
SCOPES = {"FULL_FEI", "CANDIDATE_GATE_INEQUALITY", "FINITE_WITNESS",
          "AUXILIARY_LEMMA", "EQUIVALENT_REFORMULATION", "FINITE_CHECK",
          "READ_ONCE", "BIAS_DEPENDENT", "LITERATURE"}
COMMIT = re.compile(r"^[0-9a-f]{40}$")
REPOSITORY = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def pin_key(source):
    return (source.get("repository"), source.get("commit"), source.get("path"))


def validate_pin(source, location, errors):
    if not isinstance(source, dict):
        errors.append(f"{location}: source must be an object")
        return
    repo, commit, path = pin_key(source)
    if not isinstance(repo, str) or not REPOSITORY.fullmatch(repo):
        errors.append(f"{location}: missing or invalid repository")
    if not isinstance(commit, str) or not COMMIT.fullmatch(commit):
        errors.append(f"{location}: commit must be a full immutable SHA")
    if (not isinstance(path, str) or not path or path.startswith("/")
            or ".." in PurePosixPath(path).parts):
        errors.append(f"{location}: missing or invalid repository-relative path")
    url = source.get("url")
    if url is not None and url != f"https://github.com/{repo}/blob/{commit}/{path}":
        errors.append(f"{location}: URL does not match the pinned source")


def validate_claims(state, previous=None):
    errors = []
    if not isinstance(state, dict):
        return ["claims: expected a JSON object"]
    if state.get("schema_version") != 1:
        errors.append("claims: schema_version must be 1")
    for field in ("programme_id", "control_revision", "state_revision"):
        if not isinstance(state.get(field), str) or not state[field]:
            errors.append(f"claims: missing {field}")
    catalog = state.get("sources", {})
    if not isinstance(catalog, dict):
        return errors + ["claims.sources: expected an object"]
    for name, source in catalog.items():
        validate_pin(source, f"sources.{name}", errors)
    cards = state.get("claims")
    if not isinstance(cards, list):
        return errors + ["claims.claims: expected an array"]
    indexed = {}
    for card in cards:
        if not isinstance(card, dict):
            errors.append("claims: card must be an object")
            continue
        identifier = card.get("id")
        if not isinstance(identifier, str) or not identifier:
            errors.append("claims: missing immutable claim ID")
            continue
        if identifier in indexed:
            errors.append(f"{identifier}: duplicate claim ID")
        indexed[identifier] = card
        if card.get("status") not in STATUSES:
            errors.append(f"{identifier}: invalid mathematical status")
        if not isinstance(card.get("statement"), str) or not card["statement"]:
            errors.append(f"{identifier}: missing exact statement")
        if not isinstance(card.get("scope"), str) or not card["scope"]:
            errors.append(f"{identifier}: missing exact scope")
        if card.get("scope_kind") is not None and card["scope_kind"] not in SCOPES:
            errors.append(f"{identifier}: unknown scope_kind")
        if card.get("scope_kind") == "CANDIDATE_GATE_INEQUALITY" and not card.get("candidate_id"):
            errors.append(f"{identifier}: candidate scope requires candidate_id")
        if card.get("scope_kind") == "FULL_FEI" and card.get("candidate_id"):
            errors.append(f"{identifier}: candidate-specific claim cannot be FULL_FEI")
        refs = card.get("source_refs")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{identifier}: missing source provenance")
            refs = []
        for ref in refs:
            if ref not in catalog:
                errors.append(f"{identifier}: unknown source reference {ref}")
        pins = card.get("sources")
        if not isinstance(pins, list) or not pins:
            errors.append(f"{identifier}: missing pinned claim sources")
            pins = []
        allowed_pins = {pin_key(catalog[r]) for r in refs
                        if r in catalog and isinstance(catalog[r], dict)}
        for index, source in enumerate(pins):
            validate_pin(source, f"{identifier}.sources[{index}]", errors)
            if isinstance(source, dict) and pin_key(source) not in allowed_pins:
                errors.append(f"{identifier}: pinned source not covered by source_refs")
        if not isinstance(card.get("verification"), dict):
            errors.append(f"{identifier}: missing verification provenance")
        if not isinstance(card.get("dependencies"), list):
            errors.append(f"{identifier}: dependencies must be an explicit array")
        if card.get("status") == "CONDITIONAL_IN_SOURCE" and not card.get("remaining_obligations"):
            errors.append(f"{identifier}: conditional claim must expose remaining obligations")

    # This graph means actual proof/application dependence, never mere citation.
    graph = {identifier: [] for identifier in indexed}
    blocked = set()
    for identifier, card in indexed.items():
        dependencies = card.get("dependencies", [])
        if not isinstance(dependencies, list):
            continue
        for dependency in dependencies:
            if not isinstance(dependency, dict):
                errors.append(f"{identifier}: dependency must be an object")
                continue
            parent_id, role = dependency.get("claim_id"), dependency.get("role")
            if role not in ROLES:
                errors.append(f"{identifier}: invalid dependency role {role}")
            if parent_id not in indexed:
                errors.append(f"{identifier}: missing dependency {parent_id}")
                continue
            parent = indexed[parent_id]
            if role in {"positive_result", "current_candidate", "assumption"}:
                graph[identifier].append(parent_id)
            if role == "positive_result" and parent.get("status") not in POSITIVE_STATUSES:
                blocked.add(identifier)
                errors.append(f"{identifier}: positive dependency {parent_id} is {parent.get('status')}")
            if role == "current_candidate" and (
                parent.get("status") in {"REFUTED", "NEEDS_REVALIDATION"}
                or parent.get("lifecycle", "CURRENT") == "SUPERSEDED"
            ):
                blocked.add(identifier)
                errors.append(f"{identifier}: current-candidate dependency {parent_id} is retired or invalid")
            if role == "assumption" and card.get("status") not in {
                "CONDITIONAL_IN_SOURCE", "CANDIDATE_UNPROVED", "OPEN", "NEEDS_REVALIDATION"
            }:
                errors.append(f"{identifier}: unresolved assumption cannot support an unconditional status")
            if (card.get("scope_kind") == "FULL_FEI" and role == "positive_result"
                    and parent.get("scope_kind") in {"FINITE_WITNESS", "FINITE_CHECK", "READ_ONCE"}
                    and not card.get("verification", {}).get("scope_extension_proof_refs")):
                errors.append(f"{identifier}: finite/subclass premise needs an explicit full-scope extension proof")

    # A broken premise must also block grandchildren, even if an intermediate
    # worker left a stale PROVED_IN_SOURCE label on its projection.
    changed = True
    while changed:
        changed = False
        for identifier, parents in graph.items():
            if identifier not in blocked and any(parent in blocked for parent in parents):
                blocked.add(identifier)
                errors.append(f"{identifier}: downstream dependency needs revalidation")
                changed = True
    visiting, visited = set(), set()

    def visit(identifier):
        if identifier in visiting:
            errors.append(f"{identifier}: circular mathematical dependency")
            return
        if identifier in visited:
            return
        visiting.add(identifier)
        for parent_id in graph[identifier]:
            visit(parent_id)
        visiting.remove(identifier)
        visited.add(identifier)

    for identifier in indexed:
        visit(identifier)
    full_status = state.get("full_fei_status")
    if full_status not in {"OPEN", "PROOF_CANDIDATE", "VERIFIED_PROVED", "VERIFIED_REFUTED"}:
        errors.append("claims: invalid full_fei_status")
    if full_status in {"VERIFIED_PROVED", "VERIFIED_REFUTED"}:
        if state.get("global_independent_full_review") is not True:
            errors.append("FULL_FEI: verified status requires actual independent full review")
        expected = "PROVED_IN_SOURCE" if full_status == "VERIFIED_PROVED" else "REFUTED"
        conclusions = [c for c in cards if isinstance(c, dict)
                       and c.get("scope_kind") == "FULL_FEI" and c.get("status") == expected
                       and not c.get("candidate_id")]
        if not conclusions:
            errors.append("FULL_FEI: no target-scope conclusion supports the promoted status")
        for conclusion in conclusions:
            reviewers = conclusion.get("verification", {}).get("independent_reviews", [])
            identities = {r.get("reviewer_id") for r in reviewers if isinstance(r, dict)
                          and r.get("end_to_end") is True and r.get("source_ref") in catalog}
            if None in identities or len(identities) < 2:
                errors.append("FULL_FEI: need two distinct source-bound end-to-end reviews")
    elif state.get("global_independent_full_review") is True:
        errors.append("FULL_FEI: global full-review flag conflicts with open/candidate status")
    if previous:
        for old in previous.get("claims", []):
            if old.get("id") not in indexed:
                errors.append(f"{old.get('id')}: prior truth-history claim was removed")
                continue
            new = indexed[old["id"]]
            for field in ("statement", "scope", "scope_kind", "candidate_id"):
                if old.get(field) != new.get(field):
                    errors.append(f"{old['id']}: immutable {field} changed; mint a new claim ID")
    return errors


def validate_snapshot(snapshot, state, manifest=None, observed_head=None, inbox=None):
    errors = []
    if not isinstance(snapshot, dict):
        return ["snapshot: expected an object"]
    if snapshot.get("schema_version") != 1:
        errors.append("snapshot: schema_version must be 1")
    if snapshot.get("account") not in {f"account{i:02d}" for i in range(1, 5)}:
        errors.append("snapshot: invalid logical account")
    if snapshot.get("slot") not in {f"B{i:02d}" for i in range(1, 21)}:
        errors.append("snapshot: invalid slot")
    for field in ("run_id", "next_mathematical_step"):
        if not isinstance(snapshot.get(field), str) or not snapshot[field]:
            errors.append(f"snapshot: missing {field}")
    for field in ("control_commit", "manifest_commit", "write_parent_commit"):
        value = snapshot.get(field)
        if not isinstance(value, str) or not COMMIT.fullmatch(value):
            errors.append(f"snapshot: {field} must be a full observed commit SHA")
    if observed_head and snapshot.get("write_parent_commit") != observed_head:
        errors.append("snapshot: stale write parent; re-fetch and merge before publication")
    if snapshot.get("state_revision") != state.get("state_revision"):
        errors.append("snapshot: stale state_revision")
    if snapshot.get("control_revision") != state.get("control_revision"):
        errors.append("snapshot: stale control_revision")
    if manifest:
        if snapshot.get("manifest_revision") != manifest.get("state_revision"):
            errors.append("snapshot: stale manifest_revision")
        required = set(manifest.get("mandatory_correction_ids", manifest.get("required_correction_ids", [])))
        consumed = set(snapshot.get("consumed_correction_ids", []))
        if not required.issubset(consumed):
            errors.append("snapshot: missing mandatory corrections: " + ", ".join(sorted(required - consumed)))
    indexed = {c["id"]: c for c in state.get("claims", []) if isinstance(c, dict) and "id" in c}
    pending_targets = {p.get("claim_id") for p in snapshot.get("pending_challenges", [])}
    if inbox:
        available = {event.get("id") for event in inbox.get("pending_events", [])}
        consumed = set(snapshot.get("consumed_inbox_event_ids", []))
        if not available.issubset(consumed):
            errors.append("snapshot: unconsumed live correction inbox events")
        pending_targets.update(event.get("target_claim_id") for event in inbox.get("pending_events", [])
                               if event.get("blocks_positive_use") is True)
    for remembered in snapshot.get("remembered_claims", []):
        identifier = remembered.get("claim_id")
        if identifier not in indexed:
            errors.append(f"snapshot: unknown remembered claim {identifier}")
            continue
        current = indexed[identifier]
        if remembered.get("status") != current.get("status"):
            errors.append(f"snapshot: stale mathematical status for {identifier}")
        if remembered.get("candidate_id") != current.get("candidate_id"):
            errors.append(f"snapshot: candidate identity mismatch for {identifier}")
        if remembered.get("use") == "positive_premise" and current.get("status") not in POSITIVE_STATUSES:
            errors.append(f"snapshot: {identifier} cannot be a positive premise")
        if remembered.get("use") == "positive_premise" and identifier in pending_targets:
            errors.append(f"snapshot: {identifier} has a pending source-bound challenge")
    native = snapshot.get("native_memory", {})
    if native.get("status") == "loaded":
        for field in ("api", "receipt", "receiver_run_id", "source_commit", "observed_use"):
            if not native.get(field):
                errors.append(f"snapshot: native memory loaded requires actual {field}")
    if snapshot.get("full_brain_connected") is True and not snapshot.get("full_readiness_evidence"):
        errors.append("snapshot: full brain readiness cannot follow from repository memory")
    return errors


def validate_deltas(deltas, state, previous=None):
    errors = []
    for field in ("programme_id", "control_revision", "state_revision"):
        if deltas.get(field) != state.get(field):
            errors.append(f"deltas: {field} disagrees with CLAIMS.json")
    indexed = {c["id"]: c for c in state.get("claims", []) if isinstance(c, dict) and "id" in c}
    catalog, identifiers = state.get("sources", {}), set()
    for event in deltas.get("events", []):
        identifier = event.get("id")
        if not identifier or identifier in identifiers:
            errors.append(f"deltas: missing or duplicate event ID {identifier}")
        identifiers.add(identifier)
        if event.get("action") not in {"REFUTE", "CLARIFY_SCOPE", "REFINE_CANDIDATE", "SUPERSEDE"}:
            errors.append(f"{identifier}: invalid correction action")
        target = indexed.get(event.get("target_claim_id"))
        if not target:
            errors.append(f"{identifier}: missing target claim")
            continue
        for field in ("candidate_id", "scope_kind"):
            if event.get(field) != target.get(field):
                errors.append(f"{identifier}: correction {field} exceeds its exact target scope")
        if event.get("after_status") != target.get("status"):
            errors.append(f"{identifier}: correction after_status disagrees with target projection")
        if event.get("action") == "REFUTE" and target.get("status") != "REFUTED":
            errors.append(f"{identifier}: refutation must target a refuted scoped claim")
        if event.get("action") == "SUPERSEDE":
            if target.get("lifecycle") != "SUPERSEDED":
                errors.append(f"{identifier}: superseded lifecycle is missing from target")
            if event.get("superseded_by") not in indexed:
                errors.append(f"{identifier}: replacement claim is missing")
        if event.get("action") == "REFINE_CANDIDATE" and target.get("status") != "CANDIDATE_UNPROVED":
            errors.append(f"{identifier}: witness refinement cannot promote a universal proof")
        refs, pins = event.get("source_refs", []), event.get("sources", [])
        if not refs or not pins:
            errors.append(f"{identifier}: missing correction provenance")
        for ref in refs:
            if ref not in catalog:
                errors.append(f"{identifier}: unknown correction source {ref}")
        allowed = {pin_key(catalog[r]) for r in refs if r in catalog}
        for source in pins:
            validate_pin(source, identifier, errors)
            if isinstance(source, dict) and pin_key(source) not in allowed:
                errors.append(f"{identifier}: correction pin is absent from its source_refs")
    if previous:
        new_events = {event["id"]: event for event in deltas.get("events", [])}
        for old in previous.get("events", []):
            if new_events.get(old.get("id")) != old:
                errors.append(f"{old.get('id')}: immutable correction event was edited or removed")
    return errors


def validate_inbox(inbox, state):
    errors, identifiers = [], set()
    for field in ("programme_id", "control_revision"):
        if inbox.get(field) != state.get(field):
            errors.append(f"inbox: {field} disagrees with current controls")
    for entry in inbox.get("pending_events", []):
        identifier = entry.get("id")
        if not identifier or identifier in identifiers:
            errors.append("inbox: missing or duplicate pending event ID")
        identifiers.add(identifier)
        validate_pin(entry.get("event_source"), f"inbox.{identifier}", errors)
        if not isinstance(entry.get("target_claim_id"), str) or not entry["target_claim_id"]:
            errors.append(f"inbox.{identifier}: missing target claim")
        if not isinstance(entry.get("blocks_positive_use"), bool):
            errors.append(f"inbox.{identifier}: specify whether this is a blocking challenge")
    return errors


def validate_manifest(manifest, state, directory=None):
    errors = []
    for field in ("programme_id", "control_revision", "state_revision"):
        if manifest.get(field) != state.get(field):
            errors.append(f"manifest: {field} disagrees with CLAIMS.json")
    # Optional artifact digest verification. The producer passes the directory
    # matching each stored relative path; self-referential hashes are forbidden.
    files = manifest.get("files", {})
    records = files.values() if isinstance(files, dict) else files
    if directory and isinstance(records, (list, type({}.values()))):
        root = Path(directory).resolve()
        for record in records:
            if not isinstance(record, dict) or not record.get("sha256"):
                continue
            path = record.get("local_path", record.get("filepath", record.get("path", "")))
            resolved = (root / path).resolve()
            if not path or not resolved.is_relative_to(root):
                errors.append("manifest: artifact path escapes supplied directory")
            elif not resolved.is_file():
                errors.append(f"manifest: missing artifact {path}")
            elif hashlib.sha256(resolved.read_bytes()).hexdigest() != record["sha256"]:
                errors.append(f"manifest: content hash mismatch for {path}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claims", required=True, type=Path)
    parser.add_argument("--previous-claims", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--deltas", type=Path)
    parser.add_argument("--previous-deltas", type=Path)
    parser.add_argument("--inbox", type=Path)
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--observed-head", help="fresh observed branch SHA for prewrite comparison")
    parser.add_argument("--directory", type=Path, help="local root for manifest artifact hashes")
    args = parser.parse_args()
    try:
        read = lambda path: json.loads(path.read_text(encoding="utf-8")) if path else None
        state, previous = read(args.claims), read(args.previous_claims)
        manifest, snapshot = read(args.manifest), read(args.snapshot)
        deltas, previous_deltas = read(args.deltas), read(args.previous_deltas)
        inbox = read(args.inbox)
        errors = validate_claims(state, previous)
        if manifest:
            errors.extend(validate_manifest(manifest, state, args.directory))
        if snapshot:
            errors.extend(validate_snapshot(snapshot, state, manifest, args.observed_head, inbox))
        if inbox:
            errors.extend(validate_inbox(inbox, state))
        if deltas:
            errors.extend(validate_deltas(deltas, state, previous_deltas))
            if manifest:
                required = set(manifest.get("mandatory_correction_ids", manifest.get("required_correction_ids", [])))
                available = {event.get("id") for event in deltas.get("events", [])}
                if not required.issubset(available):
                    errors.append("manifest: mandatory correction IDs absent from DELTAS.json")
        print(json.dumps({"ok": not errors, "errors": errors,
                          "scope": "coordination consistency only; no mathematical proof certification",
                          "claim_count": len(state.get("claims", []))}, indent=2))
        return 1 if errors else 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)]}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
