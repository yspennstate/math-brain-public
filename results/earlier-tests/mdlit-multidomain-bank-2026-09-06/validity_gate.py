"""Keep documented invalid items out of prospective MDLIT samples and scores.

This is an exclusion gate, not certification of unreviewed proofs. It reads
review metadata only; it never emits answers or changes the sealed bank.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


class ValidityError(ValueError):
    pass


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValidityError("duplicate JSON field: " + str(key))
        result[key] = value
    return result


def read_review(path):
    try:
        raw = Path(path).read_bytes()
        review = json.loads(raw.decode("utf-8-sig"), object_pairs_hook=_unique_object)
    except (OSError, UnicodeError, ValueError) as exc:
        raise ValidityError("validity review missing or malformed") from exc
    if not isinstance(review, dict) or not review:
        raise ValidityError("validity review must be a nonempty object")
    excluded = set()
    for iid, row in review.items():
        if not isinstance(iid, str) or not iid or not isinstance(row, dict):
            raise ValidityError("malformed validity record")
        if not isinstance(row.get("valid"), str) or row["valid"] not in {"yes", "no", "unsure"}:
            raise ValidityError("unknown validity judgment")
        if row["valid"] != "yes":
            excluded.add(iid)
    receipt = {
        "schema": "mdlit-validity-gate-v1",
        "review_sha256": hashlib.sha256(raw).hexdigest(),
        "reviewed_count": len(review),
        "excluded_count": len(excluded),
        "excluded_ids_sha256": hashlib.sha256("\n".join(sorted(excluded)).encode()).hexdigest(),
        "scope": "exclude known no/unsure; unreviewed items are not certified",
    }
    return excluded, receipt


def text_hash(items, ids):
    """Match the inherited runner's existing sampled-text receipt exactly."""
    digest = hashlib.sha256()
    for iid in sorted(ids):
        item = items[iid]
        digest.update(item["claim"].encode("utf-8"))
        for step in item["argument_steps"]:
            digest.update(b"|")
            digest.update(step["text"].encode("utf-8"))
    return digest.hexdigest()[:16]


def validate_sample(sample, review_path, items=None):
    excluded, receipt = read_review(review_path)
    ids = sample.get("item_ids") if isinstance(sample, dict) else None
    if not isinstance(ids, list) or not ids or any(not isinstance(i, str) for i in ids):
        raise ValidityError("sample needs a nonempty list of item IDs")
    if len(set(ids)) != len(ids):
        raise ValidityError("duplicate sample item IDs")
    bad = set(ids) & excluded
    if bad:
        raise ValidityError("sample contains %d validity-rejected items; preserve it and freeze a new run" % len(bad))
    if sample.get("validity_gate") != receipt:
        raise ValidityError("sample lacks the current validity receipt; preserve it and freeze a new run")
    if items is not None:
        if any(i not in items for i in ids):
            raise ValidityError("sample item missing from bank")
        if sample.get("sampled_text_hash") != text_hash(items, ids):
            raise ValidityError("sample text changed or lacks a text receipt")
    return receipt


def validate_run(run, here):
    """Shared grading entry guard, before reading or writing any scores."""
    try:
        sample = json.loads((Path(run) / "SAMPLE.json").read_text(encoding="utf-8-sig"),
                            object_pairs_hook=_unique_object)
        items = {}
        with (Path(here) / "items" / "mdlit.jsonl").open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    item = json.loads(line)
                    iid = item["item_id"]
                    if iid in items:
                        raise ValidityError("duplicate bank item ID")
                    items[iid] = item
        return validate_sample(sample, Path(here) / "VALIDITY_REVIEW.json", items)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit("MDLIT VALIDITY GATE: " + str(exc)) from exc
