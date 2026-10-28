"""Build traceable matched proof forms; never manufacture semantic acceptance.

Source proofs and proposed changes are private authoring inputs. Output keys,
source records, and proposals must remain outside solver-facing note stores.
One proposal per distinct source proof is permitted in one packet. More textual
variants are not counted as independent questions.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode("utf-8")).hexdigest()


def records(path):
    rows = []
    for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            row = json.loads(line)
            if not isinstance(row, dict):
                raise ValueError(f"{path}:{n}: expected an object")
            rows.append(row)
    return rows


def family(identifier):
    return re.sub(r"v\d+$", "", identifier.strip().removeprefix("arXiv:"))


def nonempty(row, field):
    value = row.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"missing {field}")
    return value


def checked_file(path, expected):
    if not re.fullmatch(r"[0-9a-f]{64}", str(expected)):
        raise ValueError("invalid file digest")
    path = Path(path)
    if not path.is_file():
        raise ValueError(f"missing source evidence: {path}")
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise ValueError(f"source evidence drift: {path}")
    return actual


def validate_source(source):
    for field in ("proof_group", "paper_id", "source_locator", "claim",
                  "license_uri", "source_url", "source_version",
                  "source_statement_locator", "source_proof_locator"):
        nonempty(source, field)
    if source.get("schema") != "source-proof-construction/v1":
        raise ValueError("wrong source schema")
    # URI and evidence establish a traceable claim, not a legal determination.
    if not source["license_uri"].startswith(("https://", "http://")):
        raise ValueError("license needs a URI")
    checked_file(source.get("source_file_path", ""), source.get("source_file_sha256"))
    checked_file(source.get("license_evidence_path", ""), source.get("license_evidence_sha256"))
    steps = source.get("original_steps")
    if not isinstance(steps, list) or not steps or not all(
            isinstance(x, str) and x.strip() for x in steps):
        raise ValueError("invalid original steps")
    if not isinstance(source.get("assumptions"), list) or not all(
            isinstance(x, str) and x.strip() for x in source["assumptions"]):
        raise ValueError("explicit assumptions list required")
    if not isinstance(source.get("dependencies"), list):
        raise ValueError("explicit dependencies list required")
    return source


PROMPT = ("Determine whether the argument proves the stated claim. If it does not, "
          "identify the first invalid numbered step, explain the mathematical "
          "defect, and state a minimal repair. If it is sound, say so. Do not "
          "assume that an error has been planted.")


def construct(sources, proposals, split, exposed_families=(), bank_version="source_pairs_v1"):
    if split not in {"development", "calibration", "heldout"}:
        raise ValueError("invalid split")
    by_proof = {}
    for source in sources:
        validate_source(source)
        proof = source["proof_group"]
        if proof in by_proof:
            raise ValueError("duplicate source proof")
        by_proof[proof] = source
    exposed = {family(x) for x in exposed_families}
    used = set()
    proof_texts = set()
    out = {name: [] for name in ("items", "keys", "sources", "splits", "pairs")}
    for proposal in proposals:
        proof = nonempty(proposal, "proof_group")
        if proof in used:
            raise ValueError("multiple proposals for one source proof")
        used.add(proof)
        source = by_proof.get(proof)
        if source is None:
            raise ValueError("proposal has no source proof")
        original = source["original_steps"]
        identity = digest([source["claim"], original])
        if identity in proof_texts:
            raise ValueError("duplicate original proof text under different labels")
        proof_texts.add(identity)
        if split == "heldout" and family(source["paper_id"]) in exposed:
            raise ValueError("exposed source family cannot enter heldout")
        fault = proposal.get("fault_step")
        if type(fault) is not int or not 1 <= fault <= len(original):
            raise ValueError("invalid fault step")
        replacement = nonempty(proposal, "replacement")
        if replacement == original[fault - 1]:
            raise ValueError("no-op replacement")
        # Multi-line mathematical displays can be one step, so no line-count
        # fiction is imposed here. The changed numbered step is recorded exactly.
        for field in ("defect_explanation", "minimal_repair", "falsifier"):
            nonempty(proposal, field)
        pair_ids = []
        for truth in ("clean", "flawed"):
            steps = list(original)
            if truth == "flawed":
                steps[fault - 1] = replacement
            item_id = "sp_" + digest([bank_version, proof, truth, source["claim"], steps])[:24]
            item = {"schema": "proof-bank-item/v1", "item_id": item_id,
                "bank_version": bank_version, "claim": source["claim"],
                "argument_steps": [{"n": n, "text": text}
                                   for n, text in enumerate(steps, 1)], "prompt": PROMPT}
            key = {"item_id": item_id, "truth": truth,
                "fault_step": fault if truth == "flawed" else None,
                "proof_group": proof, "paper_id": source["paper_id"],
                "original_proof_sha256": identity,
                "defect_explanation": proposal["defect_explanation"] if truth == "flawed" else None,
                "minimal_repair": proposal["minimal_repair"] if truth == "flawed" else None,
                "falsifier": proposal["falsifier"] if truth == "flawed" else None}
            receipt = dict(source, item_id=item_id, item_sha256=digest(item),
                           key_sha256=digest(key), construction_source_sha256=digest(source))
            out["items"].append(item)
            out["keys"].append(key)
            out["sources"].append(receipt)
            out["splits"].append({"item_id": item_id, "split": split})
            pair_ids.append(item_id)
        out["pairs"].append({"proof_group": proof, "paper_family": family(source["paper_id"]),
            "split": split, "item_ids": pair_ids, "original_proof_sha256": identity,
            "same_accumulating_solver_session_allowed": False})
    if not out["items"]:
        raise ValueError("empty construction packet")
    out["summary"] = {"candidate_forms": len(out["items"]),
        "distinct_source_proofs": len(used),
        "distinct_paper_families": len({p["paper_family"] for p in out["pairs"]}),
        "forms_by_truth": dict(Counter(k["truth"] for k in out["keys"])),
        "semantic_acceptance_status": "PENDING_AUTHOR_AND_INDEPENDENT_REVIEW",
        "semantically_accepted_by_this_builder": 0, "evaluated_by_this_builder": 0,
        "split": split, "bank_version": bank_version}
    return out


def write_packet(packet, directory):
    directory = Path(directory)
    if directory.exists():
        raise ValueError("output must be a fresh private packet directory")
    directory.mkdir(parents=True)
    (directory / "NO_INGEST.md").write_text(
        "Private author/reviewer packet. Keys, source proofs and review reasoning "
        "must not enter solver notes, memory indexes or public exports.\n", encoding="utf-8")
    hashes = {}
    for name in ("items", "keys", "sources", "splits", "pairs"):
        data = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True, allow_nan=False)
                       + "\n" for row in packet[name]).encode("utf-8")
        filename = name + ".jsonl"
        (directory / filename).write_bytes(data)
        hashes[filename] = hashlib.sha256(data).hexdigest()
    manifest = {"schema": "source-pair-packet/v1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "summary": packet["summary"], "sha256": hashes}
    (directory / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, required=True)
    parser.add_argument("--proposals", type=Path, required=True)
    parser.add_argument("--split", required=True, choices=["development", "calibration", "heldout"])
    parser.add_argument("--exposed-family", action="append", default=[])
    parser.add_argument("--private-dir", type=Path, required=True)
    args = parser.parse_args()
    packet = construct(records(args.sources), records(args.proposals), args.split, args.exposed_family)
    manifest = write_packet(packet, args.private_dir)
    print(json.dumps(manifest["summary"], indent=2))


if __name__ == "__main__":
    main()
