"""Population integrator: draft JSON bundles -> validated, sealed, signed, ingested.

Codex agents author simple draft bundles (see math-brain-inbox/BUNDLE_SPEC.md).
This tool performs every piece of ceremony the overlay ingestion contract needs:
statement/proof excerpt digests, per-source artifact bindings, the transitive
source manifest, core pins, the store build seal, and the population-gate MAC.
Drafts that fail validation are quarantined beside the original with reasons;
one bad draft never blocks the line. Ingestion is sequential because every
release manifest seals against the store state it lands on.

Revising a node that already exists: resubmit the same logical_name with the new statement and set
``supersedes_existing`` to true on that entry. Without the flag a changed statement is a conflict and
the whole draft is skipped.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

# the repository this tool sits in (or MATH_BRAIN_BUILD) and the inbox beside it (or MATH_BRAIN_INBOX)
BUILD_ROOT = Path(os.environ.get("MATH_BRAIN_BUILD") or Path(os.path.abspath(__file__)).parents[1])
SRC = BUILD_ROOT / "src"
sys.path.insert(0, str(SRC))

from math_brain.ingestion import (  # noqa: E402
    BundleEndpoint,
    BundleReleaseManifest,
    ClaimSourceBinding,
    IngestionCoreBinding,
    MathBundleEntry,
    MathKnowledgeBundle,
    MathRelationSpec,
    ReleaseDisposition,
    ReleaseVerifier,
    SourceArtifactBinding,
    SourceExcerptBinding,
    StoreBuildSeal,
    TransitiveSourceManifest,
    ingest_bundle,
    release_authorization_mac,
    text_digest,
)
from math_brain.models import ClaimKind, EdgeKind  # noqa: E402
from math_brain.overlay import (  # noqa: E402
    IDENTIFIER_RE,
    ContentAddressedTextStore,
    MathNodeRevision,
    SourceProvenance,
    TrustClass,
)
from math_brain.store import ResearchStore  # noqa: E402

INBOX = Path(os.environ.get("MATH_BRAIN_INBOX") or BUILD_ROOT.parent / "math-brain-inbox")
LOCAL = BUILD_ROOT / "local"
POP = LOCAL / "population"
STORE_PATH = POP / "brain.sqlite3"
OBJECTS_PATH = POP / "objects"
KEY_PATH = LOCAL / "population_gate.key"
LEDGER_PATH = POP / "integration_ledger.jsonl"
GATE_KEY_ID = "population-gate-20260802"
SPEC_PATH = INBOX / "BUNDLE_SPEC.md"

DRAFT_KINDS = {
    "definition": ClaimKind.DEFINITION,
    "lemma": ClaimKind.LEMMA,
    "theorem": ClaimKind.THEOREM,
    "concept": ClaimKind.CONCEPT,
}
PROOF_REQUIRED = {ClaimKind.LEMMA, ClaimKind.THEOREM}
DRAFT_RELATIONS = {
    "depends_on": EdgeKind.DEPENDS_ON,
    "defines": EdgeKind.DEFINES,
    "proves": EdgeKind.PROVES,
    "refutes": EdgeKind.REFUTES,
    "generalizes": EdgeKind.GENERALIZES,
    "specializes": EdgeKind.SPECIALIZES,
    "analogous_to": EdgeKind.ANALOGOUS_TO,
    "cites": EdgeKind.CITES,
    "semantic_association": EdgeKind.SEMANTIC_ASSOCIATION,
}
ALLOWED_LICENSE_PREFIXES = (
    "cc-by-sa",
    "cc-by",
    "cc0",
    "apache-2.0",
    "gfdl",
    "public-domain",
    "mit",
    "arxiv-nonexclusive",
    "owner-own-work",
)


class DraftError(Exception):
    pass


def load_gate_key() -> bytes:
    LOCAL.mkdir(parents=True, exist_ok=True)
    if not KEY_PATH.exists():
        KEY_PATH.write_bytes(os.urandom(64))
    key = KEY_PATH.read_bytes()
    if len(key) < 32:
        raise SystemExit("population gate key is too short; delete it to regenerate")
    return key


def package_pin() -> str:
    try:
        tree = subprocess.run(
            ["git", "rev-parse", "HEAD:src/math_brain"],
            cwd=BUILD_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except Exception:
        tree = "unpinned"
    return text_digest(f"math-brain-package-tree:{tree}")


def core_binding(allowlist_digest: str) -> IngestionCoreBinding:
    return IngestionCoreBinding(
        allowlist_manifest_digest=allowlist_digest,
        builder_digest=text_digest(Path(__file__).read_text(encoding="utf-8")),
        proofswarm_parser_digest=text_digest("population-run-no-proofswarm-parser"),
        math_brain_package_digest=package_pin(),
        toolchain_digest=text_digest(f"python:{sys.version}"),
        normalization_digest=text_digest("mathbrain-draft-v1"),
    )


def require(cond: bool, msg: str, errors: list[str]) -> bool:
    if not cond:
        errors.append(msg)
        return False
    return True


def parse_draft(path: Path) -> tuple[dict, list[str]]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:  # noqa: BLE001
        return {}, [f"unreadable JSON: {exc}"]
    if not isinstance(payload, dict):
        return {}, ["top level must be an object"]
    require(payload.get("spec") == "mathbrain-draft-v1", "spec must be mathbrain-draft-v1", errors)
    entries = payload.get("entries")
    if not require(isinstance(entries, list) and entries, "entries must be a nonempty list", errors):
        return payload, errors
    if len(entries) > 200:
        errors.append("more than 200 entries in one draft")
    seen_keys: set[str] = set()
    seen_logical: set[str] = set()
    for i, entry in enumerate(entries):
        where = f"entries[{i}]"
        if not isinstance(entry, dict):
            errors.append(f"{where}: not an object")
            continue
        key = entry.get("key", "")
        if not require(isinstance(key, str) and key.strip(), f"{where}: key required", errors):
            continue
        if key in seen_keys:
            errors.append(f"{where}: duplicate key {key}")
        seen_keys.add(key)
        kind = entry.get("kind", "")
        if not require(kind in DRAFT_KINDS, f"{where}: kind must be one of {sorted(DRAFT_KINDS)}", errors):
            continue
        claim_kind = DRAFT_KINDS[kind]
        ns, ln = entry.get("namespace", ""), entry.get("logical_name", "")
        require(isinstance(ns, str) and IDENTIFIER_RE.fullmatch(ns) is not None, f"{where}: bad namespace {ns!r}", errors)
        require(isinstance(ln, str) and IDENTIFIER_RE.fullmatch(ln) is not None, f"{where}: bad logical_name {ln!r}", errors)
        logical = f"{ns}:{ln}"
        if logical in seen_logical:
            errors.append(f"{where}: duplicate logical name {logical} within draft")
        seen_logical.add(logical)
        stmt = entry.get("statement", "")
        require(isinstance(stmt, str) and len(stmt.strip()) >= 20, f"{where}: statement missing or too short", errors)
        require(isinstance(entry.get("title", ""), str) and entry.get("title", "").strip() != "", f"{where}: title required", errors)
        proof = entry.get("proof_text")
        if claim_kind in PROOF_REQUIRED:
            require(isinstance(proof, str) and len(proof.strip()) >= 20, f"{where}: {kind} requires proof_text", errors)
        else:
            require(proof in (None, ""), f"{where}: {kind} must not carry proof_text", errors)
        assumptions = entry.get("assumptions", [])
        require(isinstance(assumptions, list) and all(isinstance(a, str) and a.strip() for a in assumptions), f"{where}: assumptions must be nonempty strings", errors)
        src = entry.get("source")
        if not require(isinstance(src, dict), f"{where}: source object required", errors):
            continue
        for field_name in ("source_id", "url", "revision", "license"):
            require(isinstance(src.get(field_name), str) and src.get(field_name, "").strip() != "", f"{where}: source.{field_name} required", errors)
        lic = str(src.get("license", "")).lower()
        require(any(lic.startswith(p) for p in ALLOWED_LICENSE_PREFIXES), f"{where}: license {lic!r} not in allowlist", errors)
    relations = payload.get("relations", [])
    if not isinstance(relations, list):
        errors.append("relations must be a list")
        relations = []
    adjacency: dict[str, set[str]] = {}
    for i, rel in enumerate(relations):
        where = f"relations[{i}]"
        if not isinstance(rel, dict):
            errors.append(f"{where}: not an object")
            continue
        fk, tk, kind = rel.get("from_key"), rel.get("to_key"), rel.get("kind")
        require(fk in seen_keys, f"{where}: from_key {fk!r} not an entry key", errors)
        if rel.get("to_existing_logical"):
            require(
                isinstance(rel["to_existing_logical"], str)
                and rel["to_existing_logical"].startswith("math:"),
                f"{where}: to_existing_logical must be a math:namespace:name id",
                errors,
            )
        else:
            require(tk in seen_keys, f"{where}: to_key {tk!r} not an entry key", errors)
        require(kind in DRAFT_RELATIONS, f"{where}: bad relation kind {kind!r}", errors)
        require(isinstance(rel.get("rationale"), str) and rel.get("rationale", "").strip() != "", f"{where}: rationale required", errors)
        if kind == "depends_on" and fk in seen_keys and tk in seen_keys:
            adjacency.setdefault(fk, set()).add(tk)
    state: dict[str, int] = {}

    def acyclic(node: str) -> bool:
        state[node] = 1
        for nxt in adjacency.get(node, ()):
            mark = state.get(nxt, 0)
            if mark == 1:
                return False
            if mark == 0 and not acyclic(nxt):
                return False
        state[node] = 2
        return True

    for node in list(adjacency):
        if state.get(node, 0) == 0 and not acyclic(node):
            errors.append("depends_on relations contain a cycle")
            break
    return payload, errors


def build_bundle(payload: dict, draft_name: str, existing: dict[str, str]) -> tuple[MathKnowledgeBundle, list[str], int]:
    """Convert a validated draft. Returns (bundle, skipped_reasons, kept_count, retire_releases)."""
    skipped: list[str] = []
    entries: list[MathBundleEntry] = []
    kept_keys: set[str] = set()
    retire_releases: set[str] = set()
    # 2026-09-13: the dedup below keys on the AUTHOR-CHOSEN logical name, so one statement submitted under two
    # names is never compared with itself. Measured on the live store: 48 groups of nodes share a title AND a full
    # body, and 46 of them carry different logical ids - the same harvested lead filed under the article's alias
    # (wiki-arzel-ascoli-theorem beside wiki-ascoli-arzel-theorem, wiki-uniform-boundedness-principle beside
    # wiki-banach-steinhaus-theorem, wiki-vapnik-chervonenkis-dimension beside wiki-vc-dimension). Every
    # re-harvest of a source lands another copy, and two cards saying one thing can then occupy two of a block's
    # three slots. This indexes what is already stored by statement digest so the same text under a new name is
    # caught the way an identical resubmission already is. REPORTS ONLY by default: set
    # MATHBRAIN_DEDUP_BY_CONTENT=1 to make it skip, once someone has read the report and agreed with it.
    by_digest: dict[str, str] = {}
    for _lid, _prior in existing.items():
        if _prior and _prior[0]:
            by_digest.setdefault(_prior[0], _lid)
    dedup_by_content = os.environ.get("MATHBRAIN_DEDUP_BY_CONTENT", "0") == "1"
    for entry in payload["entries"]:
        ns, ln = entry["namespace"], entry["logical_name"]
        logical_id = f"math:{ns}:{ln}"
        stmt_digest = text_digest(entry["statement"])
        supersede_target: tuple[str, ...] = ()
        if entry.get("supersedes_existing"):
            prior = existing.get(logical_id)
            if not prior or not prior[2] or not prior[3]:
                skipped.append(f"supersede-target-missing {logical_id}")
                continue
            supersede_target = (prior[1],)
            retire_releases.add(prior[3])
        elif logical_id in existing:
            if existing[logical_id][0] == stmt_digest:
                skipped.append(f"dup-identical {logical_id}")
            else:
                skipped.append(f"CONFLICT {logical_id} (statement differs from stored; left for QA)")
            continue
        twin = by_digest.get(stmt_digest)
        if twin and twin != logical_id:
            if dedup_by_content:
                skipped.append(f"dup-content {logical_id} (same statement as {twin})")
                continue
            print(
                f"[dup-content] {logical_id} has the same statement as {twin} - both will land;"
                " set MATHBRAIN_DEDUP_BY_CONTENT=1 to skip it",
                file=sys.stderr,
            )
        src = entry["source"]
        provenance = SourceProvenance(
            source_id=str(src["source_id"]),
            source_revision=str(src["revision"]),
            locator=str(src["url"]),
            imported_by=str(payload.get("author_agent", "unknown")),
            trust_class=TrustClass.CURATED_SECONDARY,
            source_content_digest=text_digest(
                str(src.get("excerpt") or entry["statement"])
            ),
        )
        revision = MathNodeRevision(
            namespace=ns,
            logical_name=ln,
            kind=DRAFT_KINDS[entry["kind"]],
            title=entry["title"].strip(),
            statement=entry["statement"].strip(),
            provenance=provenance,
            assumptions=tuple(entry.get("assumptions", [])),
            domain=str(entry.get("domain", "")),
            supersedes=supersede_target,
            metadata={"draft": draft_name, "proof_text": (entry.get("proof_text") or "").strip()},
        )
        entries.append(MathBundleEntry(entry["key"], revision))
        kept_keys.add(entry["key"])
        existing[logical_id] = (stmt_digest, "", "", "")
        by_digest.setdefault(stmt_digest, logical_id)
    relations: list[MathRelationSpec] = []
    for rel in payload.get("relations", []):
        to_logical = rel.get("to_existing_logical")
        if to_logical:
            target = existing.get(str(to_logical))
            if rel.get("from_key") in kept_keys and target and target[1]:
                relations.append(
                    MathRelationSpec(
                        BundleEndpoint.entry(rel["from_key"]),
                        BundleEndpoint.existing(target[1]),
                        DRAFT_RELATIONS.get(rel.get("kind"), EdgeKind.SEMANTIC_ASSOCIATION),
                        str(rel.get("rationale", "cross-bundle link")).strip(),
                    )
                )
            else:
                # 2026-08-12: distinguish the two causes - a relation whose SOURCE entry
                # was skipped (conflict/duplicate) is not a resolution failure of the
                # TARGET; the old single message blamed the target and misled a debug.
                if rel.get("from_key") not in kept_keys:
                    skipped.append(f"xrel-source-skipped {rel.get('from_key')} -> {to_logical}")
                else:
                    skipped.append(f"xrel-unresolved {to_logical}")
            continue
        if rel["from_key"] in kept_keys and rel["to_key"] in kept_keys:
            relations.append(
                MathRelationSpec(
                    BundleEndpoint.entry(rel["from_key"]),
                    BundleEndpoint.entry(rel["to_key"]),
                    DRAFT_RELATIONS[rel["kind"]],
                    rel["rationale"].strip(),
                )
            )
    # NOTE: existing->existing relations are FORBIDDEN by the ingestion contract
    # ("bundle relations must originate at a bundle entry") - a bundle asserts
    # knowledge about what it ships. Orphaned edges around superseded revisions
    # self-heal as future bundles cite the corrected nodes; do not re-add a
    # relations-only knit path here.
    if not entries:
        return None, skipped, 0, ()
    bundle = MathKnowledgeBundle(
        bundle_id=f"population.{payload.get('bundle_slug', draft_name)}",
        entries=tuple(entries),
        relations=tuple(relations),
        metadata={
            "verification_disposition": "population-phase content, trust CURATED_SECONDARY, pending QA",
            "author_agent": str(payload.get("author_agent", "unknown")),
            "draft_file": draft_name,
        },
    )
    return bundle, skipped, len(entries), tuple(sorted(retire_releases))


def approve(
    store: ResearchStore,
    bundle: MathKnowledgeBundle,
    key: bytes,
    allowlist_digest: str,
    retires: tuple[str, ...] = (),
) -> MathKnowledgeBundle:
    from dataclasses import replace

    bindings: list[ClaimSourceBinding] = []
    artifacts: list[SourceArtifactBinding] = []
    for entry in bundle.entries:
        prov = entry.revision.provenance
        artifact_id = text_digest(f"{entry.key}:{prov.source_id}")[7:39]
        stmt_digest = text_digest(entry.revision.statement)
        excerpts = [SourceExcerptBinding(stmt_digest, prov.locator)]
        proof_digest = None
        proof_locator = None
        proof_text = entry.revision.metadata.get("proof_text", "")
        if entry.revision.kind in PROOF_REQUIRED:
            proof_digest = text_digest(proof_text)
            proof_locator = prov.locator
            if (proof_digest, proof_locator) != (stmt_digest, prov.locator):
                excerpts.append(SourceExcerptBinding(proof_digest, proof_locator))
        bindings.append(
            ClaimSourceBinding(
                entry_key=entry.key,
                source_artifact_ids=(artifact_id,),
                statement_digest=stmt_digest,
                statement_locator=prov.locator,
                proof_digest=proof_digest,
                proof_locator=proof_locator,
            )
        )
        artifacts.append(
            SourceArtifactBinding(
                artifact_id=artifact_id,
                source_id=prov.source_id,
                source_revision=prov.source_revision,
                locator=prov.locator,
                content_digest=prov.source_content_digest,
                excerpts=tuple(excerpts),
            )
        )
    sources = TransitiveSourceManifest(allowlist_digest, tuple(artifacts))
    manifest = BundleReleaseManifest(
        release_id=f"{bundle.bundle_id}.release",
        disposition=ReleaseDisposition.APPROVED,
        disposition_reason=(
            "population-phase local gate; content enters CURATED_SECONDARY/UNVERIFIED "
            "pending cross-agent QA; MAC binds integrity, not mathematical review"
        ),
        sources=sources,
        core=core_binding(allowlist_digest),
        claim_bindings=tuple(bindings),
        store_seal=StoreBuildSeal(store.schema_digest(), store.state_digest()),
        approved_by="population-gate claude-mathbrain-build-0802",
        review_receipt_digest=text_digest(f"validation:{bundle.bundle_id}"),
        retires_release_digests=retires,
        authorization_key_id=GATE_KEY_ID,
        authorization_mac="hmac-sha256:" + "0" * 64,
    )
    manifest = replace(manifest, authorization_mac=release_authorization_mac(manifest, key))
    return replace(bundle, release_manifest=manifest)


def existing_logical_ids(store: ResearchStore) -> dict[str, tuple[str, str, str, str]]:
    """logical_id -> (stored statement digest, node id, revision digest, release digest).

    Superseded revisions are excluded so dedupe, supersession, and cross-bundle
    relations always bind the CURRENT revision, never a retired one.
    """
    from math_brain.models import EdgeKind as _EK

    superseded: dict[str, str] = {}  # retired node -> the node that superseded it
    aliases: list[tuple[str, str]] = []
    for edge in store.iter_edges():
        if getattr(edge, "kind", None) is not _EK.SUPERSEDES:
            continue
        superseded[edge.target_id] = edge.source_id
        emeta = edge.metadata if isinstance(edge.metadata, dict) else {}
        if emeta.get("derived_from") == "dedup_merge" and emeta.get("alias_logical_id"):
            aliases.append((edge.target_id, str(emeta["alias_logical_id"])))
    out: dict[str, tuple[str, str, str, str]] = {}
    for node in store.iter_nodes():
        if node.id in superseded:
            continue
        meta = node.metadata if isinstance(node.metadata, dict) else {}
        logical = str(meta.get("logical_id") or node.id)
        out[logical] = (
            text_digest(node.body or ""),
            node.id,
            str(meta.get("revision_digest") or ""),
            str(meta.get("release_manifest_digest") or ""),
        )
    # A duplicate retired by a dedup merge (land_merge_plans.py, 6 Oct 2026) keeps binding its logical id, now to the
    # current head of the card that absorbed it, so a later draft that names the retired id still finds the result.
    by_node = {entry[1]: entry for entry in out.values()}
    for retired, alias in aliases:
        head, seen = retired, set()
        while head in superseded and head not in seen:
            seen.add(head)
            head = superseded[head]
        if alias not in out and head in by_node:
            out[alias] = by_node[head]
    return out


def _index_pending_path() -> Path:
    return POP / "derived_indexes.pending.json"


def _mark_indexes_pending() -> None:
    """Write ahead of ingestion so an interrupted derived-index refresh is retried."""
    POP.mkdir(parents=True, exist_ok=True)
    pending = _index_pending_path()
    temporary = pending.with_name(pending.name + ".tmp")
    payload = {"schema": "derived-index-refresh.v1", "generation": os.urandom(16).hex(),
               "marked_at": time.time(), "reason": "population ingestion may change current revisions"}
    temporary.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")
    os.replace(temporary, pending)


def _refresh_pending_indexes(*, force: bool = False) -> bool:
    """Refresh both caches; never clear a failed or replaced pending generation.

    A failed refresh does not roll back already committed mathematical records.
    A subsequent pass retries interrupted refreshes without new drafts. Timeouts
    get at most three automatic attempts. Structural or unclassified failures
    require a diagnosed repair and explicit force=True, or a new generation.
    """
    pending = _index_pending_path()
    if not pending.exists():
        return True
    generation_bytes = pending.read_bytes()
    generation = json.loads(generation_bytes)
    target = POP / "derived_indexes.refresh.json"
    prior = json.loads(target.read_text(encoding="utf-8")) if target.exists() else {}
    attempts = int(prior.get("attempts", 0)) if prior.get("generation") == generation["generation"] else 0
    if attempts and not force:
        if prior.get("failure") != "TimeoutExpired" or attempts >= 3:
            return False
    commands = [
        ([sys.executable, "-B", "-c",
          "import sys; from pathlib import Path; from math_brain import build_signal_cache as b; "
          "b.STORE=Path(sys.argv[1]); b.CACHE=b.STORE.with_name('brain_signal_cache.pkl'); raise SystemExit(b.main())",
          str(STORE_PATH)], SRC),
        ([sys.executable, "-B", str(Path.home() / ".claude/dreaming/math_prefilter.py"),
          "build", str(STORE_PATH)], BUILD_ROOT),
    ]
    runs = []
    status = "pending"
    failure = None
    for command, cwd in commands:
        try:
            result = subprocess.run(command, cwd=cwd, capture_output=True, timeout=120,
                                    creationflags=(0x08000000 | 0x4000) if os.name == "nt" else 0)
            runs.append({"component": "signal_cache" if not runs else "lexical_prefilter",
                         "returncode": result.returncode})
            if result.returncode:
                failure = "index_builder_nonzero_exit"
                break
        except (OSError, subprocess.TimeoutExpired) as error:
            failure = type(error).__name__
            break
    else:
        if pending.exists() and pending.read_bytes() == generation_bytes:
            pending.unlink()
            status = "refreshed"
        else:
            failure = "pending_generation_changed"
    receipt = {"schema": "derived-index-refresh.v1", "generation": generation["generation"],
               "at": time.time(), "status": status, "runs": runs, "failure": failure,
               "attempts": attempts + 1, "explicit_retry": force}
    temporary = target.with_name(target.name + ".tmp")
    temporary.write_text(json.dumps(receipt, sort_keys=True), encoding="utf-8")
    os.replace(temporary, target)
    return status == "refreshed"


def process_once(verbose: bool = True, only: str | None = None) -> dict:
    """Sweep the inbox once. `only` restricts the sweep to one author directory, so an
    agent can integrate its own drafts without deciding the fate of drafts other agents
    left pending (2026-08-29: four never-ledgered drafts from another lane sat in the
    inbox while a different agent needed to integrate its own bundle)."""
    key = load_gate_key()
    POP.mkdir(parents=True, exist_ok=True)
    allowlist_digest = text_digest(SPEC_PATH.read_text(encoding="utf-8"))
    done: set[str] = set()
    if LEDGER_PATH.exists():
        for line in LEDGER_PATH.read_text(encoding="utf-8").splitlines():
            try:
                done.add(json.loads(line)["draft"])
            except Exception:  # noqa: BLE001
                continue
    stats = {"processed": 0, "entries": 0, "skipped": 0, "rejected": 0}
    with ResearchStore(STORE_PATH) as store:
        objects = ContentAddressedTextStore(OBJECTS_PATH)
        verifier = ReleaseVerifier({GATE_KEY_ID: key})
        existing = existing_logical_ids(store)
        drafts = sorted(
            p for p in INBOX.glob("*/bundle_*.json")
            if p.suffix == ".json" and (only is None or p.parent.name == only)
        )
        for draft in drafts:
            rel_name = f"{draft.parent.name}/{draft.name}"
            if rel_name in done:
                continue
            payload, errors = parse_draft(draft)
            if errors:
                draft.with_suffix(".rejected-note").write_text(
                    json.dumps({"draft": rel_name, "errors": errors}, indent=2),
                    encoding="utf-8",
                )
                stats["rejected"] += 1
                _ledger(rel_name, "rejected", {"errors": errors[:20]})
                if verbose:
                    print(f"REJECTED {rel_name}: {len(errors)} error(s); first: {errors[0]}")
                continue
            try:
                bundle, skipped, kept, retires = build_bundle(payload, rel_name, existing)
                if kept == 0:
                    stats["skipped"] += len(skipped)
                    _ledger(rel_name, "all-duplicate", {"skipped": len(skipped)})
                    if verbose:
                        print(f"SKIP {rel_name}: all {len(skipped)} entries duplicate/conflict")
                    continue
                sealed = approve(store, bundle, key, allowlist_digest, retires=retires)
                _mark_indexes_pending()
                stored = ingest_bundle(store, objects, sealed, release_verifier=verifier)
            except Exception as exc:  # noqa: BLE001 - one bad draft never kills the line
                draft.with_suffix(".rejected-note").write_text(
                    json.dumps({"draft": rel_name, "errors": [f"conversion/ingest: {exc}"]}, indent=2),
                    encoding="utf-8",
                )
                stats["rejected"] += 1
                _ledger(rel_name, "rejected", {"errors": [str(exc)[:400]]})
                if verbose:
                    print(f"REJECTED {rel_name}: {exc}")
                continue
            stats["processed"] += 1
            stats["entries"] += kept
            stats["skipped"] += len(skipped)
            _ledger(
                rel_name,
                "ingested",
                {
                    "bundle_digest": getattr(stored, "bundle_digest", None)
                    or getattr(sealed, "bundle_digest", "unknown"),
                    "entries": kept,
                    "skipped": skipped[:50],
                },
            )
            if verbose:
                print(f"INGESTED {rel_name}: {kept} entries ({len(skipped)} skipped)")
    if not _refresh_pending_indexes() and verbose:
        print("INDEX_REFRESH_PENDING: committed records retained; inspect derived_indexes.refresh.json for bounded retry or repair")
    return stats


def _ledger(draft: str, status: str, extra: dict) -> None:
    POP.mkdir(parents=True, exist_ok=True)
    record = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "draft": draft, "status": status}
    record.update(extra)
    with LEDGER_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", action="store_true", help="poll the inbox every 120s")
    parser.add_argument("--only", default=None,
                        help="integrate drafts from this author directory only")
    args = parser.parse_args()
    while True:
        stats = process_once(only=args.only)
        print(json.dumps(stats))
        if not args.watch:
            return 0
        time.sleep(120)


if __name__ == "__main__":
    raise SystemExit(main())
