"""Distinguish generated proof items from source-bound, semantically reviewed ones.

This does not prove mathematics. It validates the identity and completeness of
review evidence and keeps structural checks separate from semantic judgments.
Items are solver-facing; keys, sources, reviews and the detailed result are not.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
from typing import Any


def digest(value: Any) -> str:
    """Hash the complete JSON value, independent of record formatting."""
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode("utf-8")).hexdigest()


def records(path: Path) -> list[dict]:
    result = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"line {line_no} is not an object")
        result.append(value)
    return result


def unique(rows: list[dict], label: str) -> dict[str, dict]:
    result = {}
    for row in rows:
        item_id = row.get("item_id")
        if not isinstance(item_id, str) or not item_id:
            raise ValueError(f"{label}: missing item_id")
        if item_id in result:
            raise ValueError(f"{label}: duplicate item_id {item_id}")
        result[item_id] = row
    return result


def step_texts(item: dict) -> list[str]:
    steps = item.get("argument_steps")
    if not isinstance(steps, list) or not steps:
        raise ValueError("missing argument steps")
    texts = []
    for n, step in enumerate(steps, 1):
        if (not isinstance(step, dict) or set(step) != {"n", "text"}
                or type(step["n"]) is not int or step["n"] != n
                or not isinstance(step["text"], str) or not step["text"].strip()):
            raise ValueError("malformed argument step")
        texts.append(step["text"])
    return texts


def structural_errors(item: dict, key: dict, source: dict | None) -> list[str]:
    errors = []
    allowed = {"item_id", "schema", "bank_version", "claim", "argument_steps", "prompt"}
    if set(item) != allowed:
        errors.append("solver_field_set_mismatch")
    if not isinstance(item.get("claim"), str) or not item["claim"].strip():
        errors.append("missing_claim")
    try:
        shown = step_texts(item)
    except ValueError:
        return errors + ["malformed_steps"]
    truth = key.get("truth")
    if truth not in {"clean", "flawed"}:
        errors.append("invalid_truth")
    fault = key.get("fault_step")
    if truth == "flawed" and (type(fault) is not int or not 1 <= fault <= len(shown)):
        errors.append("invalid_fault_step")
    if truth == "clean" and fault is not None:
        errors.append("clean_has_fault_step")
    if source is None:
        return errors + ["missing_source_record"]
    if source.get("item_sha256") != digest(item):
        errors.append("source_item_binding_mismatch")
    if source.get("key_sha256") != digest(key):
        errors.append("source_key_binding_mismatch")
    for field in ("paper_id", "proof_group", "source_locator", "license_uri"):
        if not isinstance(source.get(field), str) or not source[field].strip():
            errors.append("missing_" + field)
    if not re.fullmatch(r"[0-9a-f]{64}", str(source.get("source_file_sha256", ""))):
        errors.append("invalid_source_file_sha256")
    if source.get("claim") != item.get("claim"):
        errors.append("claim_differs_from_source")
    original = source.get("original_steps")
    if (not isinstance(original, list) or len(original) != len(shown)
            or not all(isinstance(x, str) and x.strip() for x in original)):
        return errors + ["malformed_original_steps"]
    changed = [n for n, (a, b) in enumerate(zip(original, shown), 1) if a != b]
    if truth == "clean" and changed:
        errors.append("clean_differs_from_source")
    if truth == "flawed" and changed != [fault]:
        errors.append("mutation_not_exactly_keyed_step")
    # One textual edit is a structural fact, never a semantic validity finding.
    return errors


def review_errors(review: dict, item: dict, key: dict, source: dict) -> list[str]:
    errors = []
    if review.get("schema") != "semantic-proof-review/v1":
        errors.append("unversioned_review")
    for field, value in (("item_sha256", digest(item)), ("key_sha256", digest(key)),
                         ("source_sha256", digest(source))):
        if review.get(field) != value:
            errors.append("review_" + field + "_mismatch")
    if review.get("role") not in {"author", "independent"}:
        errors.append("invalid_reviewer_role")
    for field in ("reviewer_id", "reason", "source_fidelity_reason", "soundness_reason"):
        if not isinstance(review.get(field), str) or not review[field].strip():
            errors.append("missing_" + field)
    for field in ("complete_source_read", "source_fidelity", "self_contained",
                  "original_sound", "research_substance"):
        if review.get(field) is not True:
            errors.append("unconfirmed_" + field)
    if review.get("valid") != "yes":
        errors.append("not_accepted_by_reviewer")
    if key.get("truth") == "flawed":
        if review.get("exactly_one_semantic_defect") is not True:
            errors.append("unconfirmed_one_semantic_defect")
        if (type(review.get("first_invalid_step")) is not int
                or review["first_invalid_step"] != key.get("fault_step")):
            errors.append("first_invalid_step_mismatch")
        for field in ("defect_explanation", "minimal_repair", "falsifier"):
            if not isinstance(review.get(field), str) or not review[field].strip():
                errors.append("missing_" + field)
    elif review.get("first_invalid_step") is not None:
        errors.append("clean_review_has_invalid_step")
    return errors


def paper_family(identifier: str) -> str:
    """Keep arXiv versions in the same family; caller must resolve aliases/DOIs."""
    return re.sub(r"v\d+$", "", identifier.strip().removeprefix("arXiv:"))


def evaluate(items: list[dict], keys: list[dict], sources: list[dict],
             reviews: list[dict], splits: list[dict]) -> dict:
    if not items:
        raise ValueError("empty bank cannot pass acceptance")
    by_item = unique(items, "items")
    by_key = unique(keys, "keys")
    by_source = unique(sources, "sources")
    by_split = unique(splits, "splits")
    review_map = defaultdict(list)
    for review in reviews:
        if review.get("item_id") not in by_item:
            raise ValueError("review refers to unknown item")
        review_map[review["item_id"]].append(review)
    if set(by_key) != set(by_item):
        raise ValueError("item/key identities differ")
    if set(by_source) - set(by_item) or set(by_split) - set(by_item):
        raise ValueError("source/split refers to unknown item")

    # No paper version, proof family, or exact original proof may cross a
    # development/evaluation boundary. Analogy equivalence needs review too.
    groups = defaultdict(set)
    for item_id, source in by_source.items():
        split = by_split.get(item_id, {}).get("split")
        if split not in {"development", "calibration", "heldout"}:
            continue
        for group in ("paper:" + paper_family(str(source.get("paper_id", ""))),
                      "proof:" + str(source.get("proof_group", "")),
                      "text:" + digest([source.get("claim"), source.get("original_steps")])):
            groups[group].add(split)
    contaminated = {group for group, assigned in groups.items() if len(assigned) > 1}
    results = []
    for item_id, item in by_item.items():
        key, source = by_key[item_id], by_source.get(item_id)
        errors = structural_errors(item, key, source)
        split = by_split.get(item_id, {}).get("split")
        if split not in {"development", "calibration", "heldout"}:
            errors.append("missing_or_invalid_split")
        if source is not None:
            identifiers = {"paper:" + paper_family(str(source.get("paper_id", ""))),
                           "proof:" + str(source.get("proof_group", "")),
                           "text:" + digest([source.get("claim"), source.get("original_steps")])}
            if identifiers & contaminated:
                errors.append("source_family_crosses_splits")
        accepted = []
        review_results = []
        for review in review_map[item_id]:
            reasons = review_errors(review, item, key, source) if source else ["missing_source_record"]
            review_results.append({"reviewer_id": review.get("reviewer_id"), "errors": reasons})
            if not reasons:
                accepted.append(review)
        authors = {r["reviewer_id"] for r in accepted if r["role"] == "author"}
        independent = {r["reviewer_id"] for r in accepted if r["role"] == "independent"}
        reviewed = bool(authors and independent - authors)
        # A conflicting negative or uncertain judgment is not silently outvoted.
        conflict = any(r.get("valid") != "yes" for r in review_map[item_id])
        if conflict:
            errors.append("unresolved_review_disagreement")
        results.append({"item_id": item_id, "item_sha256": digest(item),
            "truth": key.get("truth"), "split": split, "structural_errors": errors,
            "review_results": review_results, "independently_reviewed": reviewed,
            "accepted": not errors and reviewed})
    summary = {"candidate_items": len(items),
        "structurally_eligible": sum(not r["structural_errors"] for r in results),
        "semantically_accepted": sum(r["accepted"] for r in results),
        "accepted_by_truth": dict(Counter(r["truth"] for r in results if r["accepted"])),
        "cross_split_groups": len(contaminated),
        "candidate_count_is_not_validated_count": True,
        "limit": "Checks review evidence, not the mathematical truth of the reviews."}
    return {"schema": "proof-bank-acceptance/v1", "summary": summary, "items": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("items", "keys", "sources", "reviews", "splits"):
        parser.add_argument("--" + name, type=Path, required=name in {"items", "keys"})
    parser.add_argument("--private-report", type=Path, required=True)
    args = parser.parse_args()
    result = evaluate(*(records(getattr(args, name)) if getattr(args, name) else []
                        for name in ("items", "keys", "sources", "reviews", "splits")))
    args.private_report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    return 0 if result["summary"]["semantically_accepted"] == result["summary"]["candidate_items"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
