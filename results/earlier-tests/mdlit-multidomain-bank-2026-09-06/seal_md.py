# -*- coding: utf-8 -*-
"""seal_md.py - commit the multi-domain bank: SHA-256 over every artifact plus an RFC 6962 ordered Merkle root over the
canonical key records (the B1 lane's convention, seal_and_audit.py, 2026-08-23), and the quarantine notice beside
the keys. A seal is a commitment, not encryption: anyone can recompute it and prove the keys were not edited after
the timestamp; it hides nothing from anyone with read access.

    python seal_md.py            # writes SEAL.json here and NO_INGEST.md in the keys directory
    python seal_md.py --verify   # recomputes and compares against SEAL.json (exit 1 on any difference)
"""
import argparse
import hashlib
import io
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
KEYS_DIR = "<HOME>/bank_multidomain_keys_quarantine"
KEYS = os.path.join(KEYS_DIR, "mdlit_keys.jsonl")
ARTIFACTS = ["items/mdlit.jsonl", "BUILD_REPORT.json", "PROTOCOL_MDLIT.md", "mutate_md.py", "build_bank_md.py",
             "extract_proofs_md.py", "arxiv_harvest_md.py", "seal_md.py", "review_sample_md.py", "VALIDITY_REVIEW.json"]
NO_INGEST = """# Quarantine

Everything in this directory is answer-bearing and must never be ingested. `mdlit_keys.jsonl` holds the key records
of the multi-domain literature proof bank (mdlit_v1): the truth of every item, the changed step, the operator, the
original text of the line, the arXiv id and the theorem it came from. Nothing here may be written into the math-brain
store at <HOME>/math-brain-build, into the brain memory directory at
<BRAIN_MEMORY>, into <BRAIN_HOOKS>, into any retrieval corpus, index,
embedding, solver payload, or prompt, and no `remember`, `ingest` or indexing path may be pointed at this directory or
at any file inside it. The quarantine is a directory convention and not encryption: the seal in the campaign
directory's SEAL.json commits the exact bytes so that later tampering is detectable, but it hides nothing from anyone
with read access, so the discipline has to be kept by whoever moves files rather than enforced by the files themselves.
If the bank is used to evaluate a brain-backed solver, the solver gets items/ and this directory stays out of its reach;
a run in which a key record was reachable measures retrieval and not judgment, and its numbers should be discarded
rather than reported.
"""


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical(rec):
    return json.dumps(rec, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def merkle_root(leaves):
    """RFC 6962: leaf hash = SHA256(0x00 || data); node = SHA256(0x01 || left || right); the tree is split at the
    largest power of two smaller than n."""
    if not leaves:
        return hashlib.sha256(b"").hexdigest()

    def node(hs):
        if len(hs) == 1:
            return hs[0]
        k = 1
        while k * 2 < len(hs):
            k *= 2
        return hashlib.sha256(b"\x01" + node(hs[:k]) + node(hs[k:])).digest()
    hs = [hashlib.sha256(b"\x00" + canonical(l)).digest() for l in leaves]
    return node(hs).hex()


def compute():
    keys = [json.loads(l) for l in io.open(KEYS, encoding="utf-8") if l.strip()]
    art = {}
    for rel in ARTIFACTS:
        p = os.path.join(HERE, rel)
        if os.path.exists(p):
            art[rel] = sha_file(p)
    art["keys/mdlit_keys.jsonl"] = sha_file(KEYS)
    no_ingest = os.path.join(KEYS_DIR, "NO_INGEST.md")
    if os.path.exists(no_ingest):
        art["keys/NO_INGEST.md"] = sha_file(no_ingest)
    return {
        "schema": "mdlit-key-seal/v1", "bank_version": "mdlit_v1", "key_records": len(keys),
        "solver_items": sum(1 for _ in io.open(os.path.join(HERE, "items", "mdlit.jsonl"), encoding="utf-8")),
        "merkle_root_rfc6962_over_canonical_key_records": merkle_root(keys),
        "artifact_sha256": dict(sorted(art.items())),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()
    if not a.verify:
        with io.open(os.path.join(KEYS_DIR, "NO_INGEST.md"), "w", encoding="utf-8") as f:
            f.write(NO_INGEST)
    seal = compute()
    out = os.path.join(HERE, "SEAL.json")
    if a.verify:
        old = json.load(io.open(out, encoding="utf-8"))
        diffs = []
        for k in ("key_records", "solver_items", "merkle_root_rfc6962_over_canonical_key_records"):
            if old.get(k) != seal.get(k):
                diffs.append((k, old.get(k), seal.get(k)))
        for k, v in old.get("artifact_sha256", {}).items():
            if seal["artifact_sha256"].get(k) != v:
                diffs.append((k, v, seal["artifact_sha256"].get(k)))
        print("VERIFY", "OK" if not diffs else "DIFFERENCES", json.dumps(diffs, indent=1))
        sys.exit(1 if diffs else 0)
    seal.update({"sealed_at": time.strftime("%Y-%m-%dT%H:%M:%S+03:00"), "sealed_by": "campaign-2026-09-06-multidomain-bank-f4",
                 "recompute": "python seal_md.py --verify",
                 "what_this_seal_does": "commits the exact bytes of every key record and of every artifact in this lane, so later tampering is detectable by recomputation",
                 "what_this_seal_does_not_do": "it does not encrypt or access-control the keys; the quarantine directory is a convention"})
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(seal, f, indent=1)
    print(json.dumps({k: v for k, v in seal.items() if k != "artifact_sha256"}, indent=1))


if __name__ == "__main__":
    main()
