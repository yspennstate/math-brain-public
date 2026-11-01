from pathlib import Path

import pytest

from math_brain.models import ClaimKind, EdgeKind, NodeKind, RecordStatus
from math_brain.overlay import (
    ContentAddressedTextStore,
    MathNodeRevision,
    SourceProvenance,
    TrustClass,
    append_revision,
    bridge_edge,
    external_reference_node,
)
from math_brain.store import ResearchStore


def provenance(*, fidelity: bool = False) -> SourceProvenance:
    return SourceProvenance(
        source_id="source:mols10-forward-phi",
        source_revision="git:69bb746",
        locator="public-paper-section-4",
        imported_by="test-suite",
        trust_class=TrustClass.PRIMARY_SOURCE,
        statement_fidelity_reviewed=fidelity,
    )


def revision(**changes: object) -> MathNodeRevision:
    values: dict[str, object] = {
        "namespace": "combinatorics.mols",
        "logical_name": "forward-phi-injectivity",
        "kind": ClaimKind.LEMMA,
        "title": "Forward Phi injectivity",
        "statement": "Repeated source pairs contradict quotient column-symbol AMO.",
        "provenance": provenance(),
        "assumptions": ("Each source array is Latin.",),
        "domain": "finite combinatorics",
    }
    values.update(changes)
    return MathNodeRevision(**values)  # type: ignore[arg-type]


def test_revision_identity_is_content_stable_and_changes_with_scope() -> None:
    first = revision(created_at="2026-08-02T00:00:00+00:00")
    later_ingestion = revision(created_at="2026-08-03T00:00:00+00:00")
    narrowed = revision(assumptions=("Each source array is normalized and Latin.",))

    assert first.logical_id == "math:combinatorics.mols:forward-phi-injectivity"
    assert first.revision_id == later_ingestion.revision_id
    assert first.render_markdown() == later_ingestion.render_markdown()
    assert narrowed.revision_id != first.revision_id


def test_statuses_fail_closed_without_scope_and_evidence() -> None:
    with pytest.raises(ValueError, match="conditions"):
        revision(status=RecordStatus.CONDITIONAL, evidence_ids=("evidence_1",))
    with pytest.raises(ValueError, match="evidence"):
        revision(status=RecordStatus.PROVISIONAL)
    with pytest.raises(ValueError, match="fidelity"):
        revision(status=RecordStatus.VERIFIED, evidence_ids=("evidence_1",))

    verified = revision(
        status=RecordStatus.VERIFIED,
        evidence_ids=("evidence_kernel", "evidence_fidelity"),
        provenance=provenance(fidelity=True),
    )
    assert verified.status is RecordStatus.VERIFIED


def test_content_addressed_text_is_idempotent_and_tamper_evident(tmp_path: Path) -> None:
    objects = ContentAddressedTextStore(tmp_path / "overlay")
    item = revision()
    first = objects.persist(item)
    second = objects.persist(item)

    assert first == second
    artifact = objects.root / first.relative_path
    assert artifact.read_text(encoding="utf-8") == item.render_markdown()

    artifact.write_text("tampered", encoding="utf-8")
    with pytest.raises(OSError, match="does not match"):
        objects.persist(item)


def test_append_revision_persists_artifact_metadata_and_supersession(
    tmp_path: Path,
) -> None:
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        first = revision()
        stored_first = append_revision(store, objects, first)
        corrected = revision(
            statement="The retained AMO family still requires an independent attestation.",
            supersedes=(first.revision_id,),
        )
        stored_corrected = append_revision(store, objects, corrected)

        nodes = {node.id: node for node in store.iter_nodes()}
        edges = list(store.iter_edges())

    assert stored_first.node.metadata["artifact_digest"] == stored_first.artifact.digest
    assert nodes[stored_corrected.node.id].metadata["truth_status"] == "unverified"
    assert [(edge.source_id, edge.target_id, edge.kind) for edge in edges] == [
        (corrected.revision_id, first.revision_id, EdgeKind.SUPERSEDES)
    ]


def test_bridge_uses_a_deterministic_external_proxy_without_merging_stores() -> None:
    proxy = external_reference_node(
        "main-brain",
        "memory:mols10-forward-phi",
        "MOLS10 forward-Phi memory",
    )
    repeated = external_reference_node(
        "main-brain",
        "memory:mols10-forward-phi",
        "MOLS10 forward-Phi memory",
    )
    edge = bridge_edge(revision().revision_id, proxy.id, "cross-brain retrieval bridge")

    assert proxy.id == repeated.id
    assert proxy.metadata == repeated.metadata
    assert proxy.kind is NodeKind.EXTERNAL_REFERENCE
    assert edge.kind is EdgeKind.BRIDGES_TO
    assert edge.source_id != edge.target_id
