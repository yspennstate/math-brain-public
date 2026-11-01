from dataclasses import replace
from pathlib import Path

import pytest

import math_brain.ingestion as ingestion_module
from math_brain.ingestion import (
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
from math_brain.models import (
    ClaimKind,
    EdgeKind,
    GraphNode,
    NodeKind,
    RecordStatus,
    canonical_json,
)
from math_brain.overlay import (
    ContentAddressedTextStore,
    MathNodeRevision,
    SourceProvenance,
    TrustClass,
    append_revision,
    external_reference_node,
)
from math_brain.store import ResearchStore


def digest(label: str) -> str:
    return text_digest(f"fixture:{label}")


SOURCE_CONTENT_DIGEST = digest("full-source")
ALLOWLIST_DIGEST = digest("allowlist")
AUTHORIZATION_KEY_ID = "independent-gate-v1"
AUTHORIZATION_KEY = b"independent-test-gate-key-material-2026-v1"


def release_verifier() -> ReleaseVerifier:
    return ReleaseVerifier({AUTHORIZATION_KEY_ID: AUTHORIZATION_KEY})


def provenance() -> SourceProvenance:
    return SourceProvenance(
        source_id="source:mols10-residual-coloring",
        source_revision="mesh:msg-93589aa006",
        locator="independent-audit-required",
        imported_by="test-suite",
        trust_class=TrustClass.GENERATED_UNVERIFIED,
        source_content_digest=SOURCE_CONTENT_DIGEST,
    )


def revision(
    logical_name: str,
    kind: ClaimKind,
    statement: str,
    *,
    supersedes: tuple[str, ...] = (),
    created_at: str = "2026-08-02T00:00:00+00:00",
) -> MathNodeRevision:
    return MathNodeRevision(
        namespace="combinatorics.mols",
        logical_name=logical_name,
        kind=kind,
        title=logical_name.replace("-", " ").title(),
        statement=statement,
        provenance=provenance(),
        assumptions=("The residual rows come from a fixed orthogonal-array encoding.",),
        domain="finite combinatorics",
        supersedes=supersedes,
        created_at=created_at,
    )


def mols_entries() -> tuple[MathBundleEntry, ...]:
    concept = revision(
        "common-transversal",
        ClaimKind.CONCEPT,
        "A common transversal selects one cell of every symbol in every OA coordinate.",
    )
    definition = revision(
        "residual-conflict-graph",
        ClaimKind.DEFINITION,
        "Residual rows are adjacent exactly when they share an OA coordinate value.",
    )
    lemma = revision(
        "color-class-transversal-lemma",
        ClaimKind.LEMMA,
        "Every color class of a proper q-coloring is a common transversal.",
    )
    theorem = revision(
        "extension-coloring-equivalence",
        ClaimKind.THEOREM,
        "The fixed partial net extends exactly when the residual graph is q-colorable.",
    )
    return (
        MathBundleEntry("concept", concept),
        MathBundleEntry("definition", definition),
        MathBundleEntry("lemma", lemma),
        MathBundleEntry("theorem", theorem),
    )


def mols_relations() -> tuple[MathRelationSpec, ...]:
    return (
        MathRelationSpec(
            BundleEndpoint.entry("definition"),
            BundleEndpoint.entry("concept"),
            EdgeKind.DEFINES,
            "the residual graph definition uses the common-transversal concept",
        ),
        MathRelationSpec(
            BundleEndpoint.entry("lemma"),
            BundleEndpoint.entry("definition"),
            EdgeKind.DEPENDS_ON,
            "the color-class lemma uses the residual conflict graph",
        ),
        MathRelationSpec(
            BundleEndpoint.entry("theorem"),
            BundleEndpoint.entry("lemma"),
            EdgeKind.DEPENDS_ON,
            "the equivalence proof uses the color-class transversal lemma",
        ),
    )


def mols_bundle(
    *,
    entries: tuple[MathBundleEntry, ...] | None = None,
    relations: tuple[MathRelationSpec, ...] | None = None,
    created_at: str = "2026-08-02T01:00:00+00:00",
) -> MathKnowledgeBundle:
    return MathKnowledgeBundle(
        bundle_id="combinatorics.mols.residual-coloring-v1",
        entries=entries if entries is not None else mols_entries(),
        relations=relations if relations is not None else mols_relations(),
        metadata={"verification_disposition": "unverified infrastructure fixture"},
        created_at=created_at,
    )


def approved_release(
    store: ResearchStore,
    entries: tuple[MathBundleEntry, ...],
    *,
    retires: tuple[str, ...] = (),
    disposition: ReleaseDisposition = ReleaseDisposition.APPROVED,
) -> BundleReleaseManifest:
    excerpts: list[SourceExcerptBinding] = []
    bindings: list[ClaimSourceBinding] = []
    for entry in entries:
        statement_locator = entry.revision.provenance.locator
        statement_binding = SourceExcerptBinding(
            text_digest(entry.revision.statement), statement_locator
        )
        excerpts.append(statement_binding)
        proof_digest = None
        proof_locator = None
        if entry.revision.kind in {
            ClaimKind.LEMMA,
            ClaimKind.THEOREM,
            ClaimKind.PROOF_ATTEMPT,
        }:
            proof_digest = digest(f"proof:{entry.key}")
            proof_locator = f"{statement_locator}#proof-{entry.key}"
            excerpts.append(SourceExcerptBinding(proof_digest, proof_locator))
        bindings.append(
            ClaimSourceBinding(
                entry_key=entry.key,
                source_artifact_ids=("root-source",),
                statement_digest=statement_binding.digest,
                statement_locator=statement_binding.locator,
                proof_digest=proof_digest,
                proof_locator=proof_locator,
            )
        )

    source = SourceArtifactBinding(
        artifact_id="root-source",
        source_id="source:mols10-residual-coloring",
        source_revision="mesh:msg-93589aa006",
        locator="independent-audit-required",
        content_digest=SOURCE_CONTENT_DIGEST,
        excerpts=tuple(excerpts),
    )
    sources = TransitiveSourceManifest(ALLOWLIST_DIGEST, (source,))
    core = IngestionCoreBinding(
        allowlist_manifest_digest=ALLOWLIST_DIGEST,
        builder_digest=digest("builder"),
        proofswarm_parser_digest=digest("proofswarm-parser"),
        math_brain_package_digest=digest("math-brain-package"),
        toolchain_digest=digest("toolchain"),
        normalization_digest=digest("normalization"),
    )
    approved = disposition is ReleaseDisposition.APPROVED
    manifest = BundleReleaseManifest(
        release_id="combinatorics.mols.release-v1",
        disposition=disposition,
        disposition_reason="synthetic fixture exercises the cryptographic release boundary",
        sources=sources,
        core=core,
        claim_bindings=tuple(bindings),
        store_seal=StoreBuildSeal(store.schema_digest(), store.state_digest()),
        approved_by="independent-test-reviewer" if approved else "",
        review_receipt_digest=digest("review-receipt") if approved else None,
        retires_release_digests=retires,
        authorization_key_id=AUTHORIZATION_KEY_ID if approved else "",
        authorization_mac="hmac-sha256:" + "0" * 64 if approved else None,
    )
    if not approved:
        return manifest
    return replace(
        manifest,
        authorization_mac=release_authorization_mac(manifest, AUTHORIZATION_KEY),
    )


def approve_bundle(
    store: ResearchStore,
    bundle: MathKnowledgeBundle,
    *,
    retires: tuple[str, ...] = (),
) -> MathKnowledgeBundle:
    return replace(
        bundle,
        release_manifest=approved_release(store, bundle.entries, retires=retires),
    )


def test_bundle_digest_is_order_and_ingestion_time_independent(tmp_path: Path) -> None:
    first_draft = mols_bundle()
    reordered_draft = mols_bundle(
        entries=tuple(reversed(mols_entries())),
        relations=tuple(reversed(mols_relations())),
        created_at="2026-08-03T01:00:00+00:00",
    )
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        first = approve_bundle(store, first_draft)
        reordered = approve_bundle(store, reordered_draft)

    assert first.bundle_digest == reordered.bundle_digest


def test_mols_bundle_ingests_all_nodes_and_typed_edges_atomically(tmp_path: Path) -> None:
    draft = mols_bundle()
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        bundle = approve_bundle(store, draft)
        stored = ingest_bundle(
            store, objects, bundle, release_verifier=release_verifier()
        )
        nodes = {node.id: node for node in store.iter_nodes()}
        edges = list(store.iter_edges())
        manifest = store.get_bundle_manifest(bundle.bundle_id)

    assert stored.receipt.bundle_digest == bundle.bundle_digest
    assert stored.receipt.release_manifest_digest == bundle.release_manifest.release_digest
    assert stored.receipt.node_count == 4
    assert stored.receipt.edge_count == 3
    assert stored.receipt.receipt_digest.startswith("sha256:")
    assert len(nodes) == 4
    assert len(edges) == 3
    assert {edge.kind for edge in edges} == {EdgeKind.DEFINES, EdgeKind.DEPENDS_ON}
    assert all(edge.metadata["bundle_digest"] == bundle.bundle_digest for edge in edges)
    assert all(node.metadata["bundle_id"] == bundle.bundle_id for node in nodes.values())
    assert canonical_json(manifest) == canonical_json(bundle.canonical_payload())
    for receipt in stored.receipt.artifacts:
        artifact_path = objects.root / receipt.artifact.relative_path
        assert artifact_path.is_file()
        assert receipt.artifact.digest == "sha256:" + artifact_path.stem


def test_missing_existing_endpoint_fails_before_artifact_or_database_write(
    tmp_path: Path,
) -> None:
    entry = mols_entries()[-1]
    draft = mols_bundle(
        entries=(entry,),
        relations=(
            MathRelationSpec(
                BundleEndpoint.entry(entry.key),
                BundleEndpoint.existing("claim_missing_dependency"),
                EdgeKind.DEPENDS_ON,
                "a required prior lemma",
            ),
        ),
    )
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        bundle = approve_bundle(store, draft)
        with pytest.raises(ValueError, match="missing existing nodes"):
            ingest_bundle(store, objects, bundle, release_verifier=release_verifier())
        assert list(store.iter_nodes()) == []
    assert list(objects.root.rglob("*.md")) == []


def test_dependency_cycle_is_rejected_before_artifact_write(tmp_path: Path) -> None:
    entries = mols_entries()[2:]
    draft = mols_bundle(
        entries=entries,
        relations=(
            MathRelationSpec(
                BundleEndpoint.entry("lemma"),
                BundleEndpoint.entry("theorem"),
                EdgeKind.DEPENDS_ON,
                "first half of a bad cycle",
            ),
            MathRelationSpec(
                BundleEndpoint.entry("theorem"),
                BundleEndpoint.entry("lemma"),
                EdgeKind.DEPENDS_ON,
                "second half of a bad cycle",
            ),
        ),
    )
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        bundle = approve_bundle(store, draft)
        with pytest.raises(ValueError, match="directed cycle"):
            ingest_bundle(store, objects, bundle, release_verifier=release_verifier())
        assert list(store.iter_nodes()) == []
    assert list(objects.root.rglob("*.md")) == []


def test_external_proxy_cannot_become_a_proof_dependency(tmp_path: Path) -> None:
    entry = mols_entries()[-1]
    proxy = external_reference_node(
        "main-brain",
        "memory:mols10-residual-coloring",
        "Main-brain MOLS memory",
    )
    draft = mols_bundle(
        entries=(entry,),
        relations=(
            MathRelationSpec(
                BundleEndpoint.entry(entry.key),
                BundleEndpoint.existing(proxy.id),
                EdgeKind.DEPENDS_ON,
                "unsafe attempt to use discovery memory as a proof premise",
            ),
        ),
    )
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        store.add_node(proxy)
        store.transaction().commit()
        bundle = approve_bundle(store, draft)
        with pytest.raises(ValueError, match="only be targets of bridges_to"):
            ingest_bundle(store, objects, bundle, release_verifier=release_verifier())
        assert [node.id for node in store.iter_nodes()] == [proxy.id]
    assert list(objects.root.rglob("*.md")) == []


def test_exact_bundle_replay_fails_clearly_without_duplicate_rows(tmp_path: Path) -> None:
    draft = mols_bundle()
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        bundle = approve_bundle(store, draft)
        ingest_bundle(store, objects, bundle, release_verifier=release_verifier())
        with pytest.raises(ValueError, match="cannot be replayed"):
            ingest_bundle(store, objects, bundle, release_verifier=release_verifier())
        assert len(list(store.iter_nodes())) == 4
        assert len(list(store.iter_edges())) == 3


def test_dark_release_gate_cannot_create_a_graph_or_artifact(tmp_path: Path) -> None:
    draft = mols_bundle(entries=mols_entries()[:1], relations=())
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        dark = replace(
            draft,
            release_manifest=approved_release(
                store,
                draft.entries,
                disposition=ReleaseDisposition.DARK,
            ),
        )
        with pytest.raises(ValueError, match="release gate is dark"):
            ingest_bundle(store, objects, dark, release_verifier=release_verifier())
        assert list(store.iter_nodes()) == []
        assert store.get_bundle_manifest(dark.bundle_id) is None
    assert list(objects.root.rglob("*.md")) == []


def test_forged_release_authorization_fails_before_artifact_write(tmp_path: Path) -> None:
    draft = mols_bundle(entries=mols_entries()[:1], relations=())
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        bundle = approve_bundle(store, draft)
        release = bundle.release_manifest
        assert release is not None and release.authorization_mac is not None
        replacement = "0" if release.authorization_mac[-1] != "0" else "1"
        forged_release = replace(
            release,
            authorization_mac=release.authorization_mac[:-1] + replacement,
        )
        forged_bundle = replace(bundle, release_manifest=forged_release)
        with pytest.raises(ValueError, match="authorization receipt is invalid"):
            ingest_bundle(
                store,
                objects,
                forged_bundle,
                release_verifier=release_verifier(),
            )
        assert list(store.iter_nodes()) == []
        assert store.get_bundle_manifest(forged_bundle.bundle_id) is None
    assert list(objects.root.rglob("*.md")) == []


def test_stale_database_build_seal_fails_before_artifact_write(tmp_path: Path) -> None:
    draft = mols_bundle(entries=mols_entries()[:1], relations=())
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        bundle = approve_bundle(store, draft)
        store.add_node(GraphNode("concurrent_node", NodeKind.SOURCE, "Concurrent append"))
        store.transaction().commit()
        with pytest.raises(ValueError, match="pre-state seal is stale"):
            ingest_bundle(store, objects, bundle, release_verifier=release_verifier())
        assert store.get_bundle_manifest(bundle.bundle_id) is None
    assert list(objects.root.rglob("*.md")) == []


def test_lemma_release_requires_an_exact_proof_slice(tmp_path: Path) -> None:
    draft = mols_bundle(entries=(mols_entries()[2],), relations=())
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        release = approved_release(store, draft.entries)
        binding = release.claim_bindings[0]
        missing_proof = replace(binding, proof_digest=None, proof_locator=None)
        malformed_release = replace(release, claim_bindings=(missing_proof,))
        with pytest.raises(ValueError, match="requires proof digest"):
            replace(draft, release_manifest=malformed_release)


def test_bundle_cannot_smuggle_caller_authored_promotion_status() -> None:
    entry = mols_entries()[0]
    promoted = replace(
        entry.revision,
        status=RecordStatus.PROVISIONAL,
        evidence_ids=("fabricated_evidence_id",),
    )
    with pytest.raises(ValueError, match="unverified revisions only"):
        mols_bundle(entries=(MathBundleEntry(entry.key, promoted),), relations=())


def test_approved_bridge_can_target_external_proxy_without_becoming_proof(
    tmp_path: Path,
) -> None:
    entry = mols_entries()[0]
    proxy = external_reference_node(
        "main-brain",
        "memory:mols10-residual-coloring",
        "Main-brain MOLS memory",
    )
    draft = mols_bundle(
        entries=(entry,),
        relations=(
            MathRelationSpec(
                BundleEndpoint.entry(entry.key),
                BundleEndpoint.existing(proxy.id),
                EdgeKind.BRIDGES_TO,
                "discovery-only cross-brain bridge",
            ),
        ),
    )
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        store.add_node(proxy)
        store.transaction().commit()
        bundle = approve_bundle(store, draft)
        ingest_bundle(store, objects, bundle, release_verifier=release_verifier())
        edge = next(store.iter_edges())
    assert edge.kind is EdgeKind.BRIDGES_TO
    assert edge.target_id == proxy.id


def test_supersession_must_preserve_logical_identity(tmp_path: Path) -> None:
    objects = ContentAddressedTextStore(tmp_path / "objects")
    prior = revision("different-logical-object", ClaimKind.LEMMA, "An unrelated lemma.")
    candidate = revision(
        "extension-coloring-equivalence",
        ClaimKind.THEOREM,
        "A changed theorem statement.",
        supersedes=(prior.revision_id,),
    )
    draft = mols_bundle(
        entries=(MathBundleEntry("candidate", candidate),),
        relations=(),
    )
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        append_revision(store, objects, prior)
        bundle = approve_bundle(store, draft, retires=(digest("legacy-release"),))
        with pytest.raises(ValueError, match="same logical_id"):
            ingest_bundle(store, objects, bundle, release_verifier=release_verifier())
        assert store.get_claim(candidate.revision_id) is None


def test_duplicate_logical_objects_and_cardinality_overflow_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    first = revision("same-object", ClaimKind.LEMMA, "First statement.")
    second = revision("same-object", ClaimKind.LEMMA, "Second statement.")
    with pytest.raises(ValueError, match="duplicate logical ids"):
        mols_bundle(
            entries=(MathBundleEntry("first", first), MathBundleEntry("second", second)),
            relations=(),
        )

    monkeypatch.setattr(ingestion_module, "MAX_BUNDLE_ENTRIES", 1)
    with pytest.raises(ValueError, match="entry limit"):
        mols_bundle(entries=mols_entries()[:2], relations=())
