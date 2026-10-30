"""A revision's declared status is recorded, never taken as the claim's authority (fleet02/B11,
B11-R79-OVERLAY-STATUS-CANNOT-APPEND-01, 29 Sep 2026).

Until 30 Sep MathNodeRevision.to_claim passed the revision's status into the stored claim, and the store admits only
an unverified claim, so a revision declaring any of the seven other statuses could not be appended at all. The claim
now always starts unverified (the store's anti-smuggling rule is kept), the node carries the revision's own status as
declared_status, and only verification events move the claim. T1, T7, T8 and T10 are the auditor's proposed checks.
"""

import json
from pathlib import Path

import pytest

from math_brain import verification
from math_brain.current_note import read_current_note
from math_brain.models import LEGACY_READ_ONLY_STATUSES, Claim, ClaimKind, EdgeKind, RecordStatus
from math_brain.overlay import (
    ContentAddressedTextStore,
    MathNodeRevision,
    SourceProvenance,
    TrustClass,
    append_revision,
)
from math_brain.retrieval import current_revision_nodes
from math_brain.store import ResearchStore


def provenance(*, fidelity: bool = False) -> SourceProvenance:
    return SourceProvenance(
        source_id="source:declared-status-fixture",
        source_revision="git:0000000",
        locator="fixture-section-1",
        imported_by="test-suite",
        trust_class=TrustClass.PRIMARY_SOURCE,
        statement_fidelity_reviewed=fidelity,
    )


def revision(**changes: object) -> MathNodeRevision:
    values: dict[str, object] = {
        "namespace": "fixture.overlay",
        "logical_name": "declared-status",
        "kind": ClaimKind.LEMMA,
        "title": "A fixture lemma",
        "statement": "Every finite nonempty set of integers has a least element.",
        "provenance": provenance(),
        "domain": "order",
    }
    values.update(changes)
    return MathNodeRevision(**values)  # type: ignore[arg-type]


# the fields each status's own invariant requires (overlay.MathNodeRevision.__post_init__)
REQUIRED = {
    RecordStatus.UNVERIFIED: {},
    RecordStatus.PROVISIONAL: {"evidence_ids": ("evidence_numeric",)},
    RecordStatus.CONDITIONAL: {"evidence_ids": ("evidence_numeric",), "conditions": ("the set is bounded below",)},
    RecordStatus.VERIFIED: {"evidence_ids": ("evidence_kernel",), "provenance": provenance(fidelity=True)},
    RecordStatus.GAP_FOUND: {"disposition_reason": "step 2 assumes what it proves"},
    RecordStatus.REFUTED: {"disposition_reason": "the empty set is a counterexample to the stated form"},
    RecordStatus.RETRACTED: {"disposition_reason": "withdrawn by its author"},
    RecordStatus.UNKNOWN: {},
}


def test_every_declared_status_can_be_appended_and_the_claim_starts_unverified(tmp_path: Path) -> None:
    """T7: every value of the enum, each with the fields its invariant needs."""
    assert set(REQUIRED) == set(RecordStatus) - LEGACY_READ_ONLY_STATUSES
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        for status, fields in REQUIRED.items():
            item = revision(logical_name="declared-" + status.value.replace("_", "-"), status=status, **fields)
            stored = append_revision(store, objects, item)
            claim = store.get_claim(item.revision_id)
            assert claim is not None and claim.status is RecordStatus.UNVERIFIED, status
            meta = stored.node.metadata
            assert meta["truth_status"] == "unverified", status
            if status is RecordStatus.UNVERIFIED:
                assert "declared_status" not in meta
            else:
                assert meta["declared_status"] == status.value, status


def test_a_verified_revision_appends_and_reads_back_as_declared_not_authenticated(tmp_path: Path) -> None:
    """T1 and T8: the revision the old code refused, round-tripped through the store and the full-note reader."""
    item = revision(status=RecordStatus.VERIFIED, **REQUIRED[RecordStatus.VERIFIED])
    objects = ContentAddressedTextStore(tmp_path / "objects")
    database = tmp_path / "brain.sqlite3"
    with ResearchStore(database) as store:
        stored = append_revision(store, objects, item)
    # the revision's identity still carries its declared status (content-addressed, unchanged by the fix)
    assert item.canonical_payload()["status"] == "verified"
    assert stored.node.id == item.revision_id
    artifact = (objects.root / stored.artifact.relative_path).read_text(encoding="utf-8")
    assert '"status":"verified"' in artifact.replace(" ", "")
    note = read_current_note(database, item.revision_id, artifact_root=objects.root)
    assert note["claim"]["status"] == "unverified"
    assert note["trust"]["truth_status"] == "unverified"
    assert note["trust"]["declared_status"] == "verified"


def test_an_unverified_revision_is_written_exactly_as_before(tmp_path: Path) -> None:
    """The 5,690 overlay nodes of the live store were all unverified: their writers see no change."""
    item = revision()
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        stored = append_revision(store, objects, item)
    assert "declared_status" not in stored.node.metadata
    assert stored.node.metadata["truth_status"] == "unverified"


def test_a_retraction_supersedes_and_keeps_the_history(tmp_path: Path) -> None:
    """T10 (and T3's retrieval half): the retraction is a new revision; the old one stays in the store, leaves the
    current set, and nothing is deleted."""
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        first = revision()
        append_revision(store, objects, first)
        retraction = revision(status=RecordStatus.RETRACTED, supersedes=(first.revision_id,),
                              disposition_reason="withdrawn by its author")
        append_revision(store, objects, retraction)
        nodes = list(store.iter_nodes())
        edges = list(store.iter_edges())
    ids = {node.id for node in nodes}
    assert {first.revision_id, retraction.revision_id} <= ids
    current, excluded = current_revision_nodes(nodes, edges)
    assert retraction.revision_id in {node.id for node in current}
    assert first.revision_id in {item.node_id for item in excluded}
    assert (retraction.revision_id, first.revision_id, EdgeKind.SUPERSEDES) in {
        (edge.source_id, edge.target_id, edge.kind) for edge in edges
    }
    served = next(node for node in current if node.id == retraction.revision_id)
    assert served.metadata["declared_status"] == "retracted"


def test_which_statuses_an_event_can_reach_is_pinned() -> None:
    """T7's second half: each status is reachable by an authenticated event or is a declared disposition only. A new
    transition in verification.py fails this until the contract here is updated with it."""
    reachable, frontier = {RecordStatus.UNVERIFIED}, [RecordStatus.UNVERIFIED]
    while frontier:
        for target in verification._ALLOWED_TRANSITIONS.get(frontier.pop(), frozenset()):
            if target not in reachable:
                reachable.add(target)
                frontier.append(target)
    assert reachable == {RecordStatus.UNVERIFIED, RecordStatus.PROVISIONAL, RecordStatus.VERIFIED, RecordStatus.REFUTED}
    declared_only = set(RecordStatus) - reachable - LEGACY_READ_ONLY_STATUSES
    assert declared_only == {RecordStatus.CONDITIONAL, RecordStatus.GAP_FOUND, RecordStatus.RETRACTED,
                             RecordStatus.UNKNOWN}


def test_a_bundle_still_refuses_a_declared_status() -> None:
    """The bundle path keeps its own rule: every entry unverified. A declared disposition comes through
    append_revision, one revision at a time."""
    import inspect

    from math_brain import ingestion

    assert "entry.revision.status is not RecordStatus.UNVERIFIED" in inspect.getsource(ingestion)


@pytest.mark.parametrize("status", [RecordStatus.GAP_FOUND, RecordStatus.REFUTED, RecordStatus.RETRACTED])
def test_a_negative_disposition_still_needs_its_reason(status: RecordStatus) -> None:
    with pytest.raises(ValueError, match="disposition reason"):
        revision(status=status)


def test_a_legacy_stored_status_is_read_but_never_declared(tmp_path: Path) -> None:
    """7 Oct 2026: 34 live cards carry a status a campaign landing wrote straight into the claims table. get_claim reads
    each with its digest intact, so the current-note path can serve it; a new revision cannot declare one."""
    assert LEGACY_READ_ONLY_STATUSES == {RecordStatus.VERIFIED_REPLACEMENT, RecordStatus.DERIVED_IN_CAMPAIGN,
                                         RecordStatus.DERIVED_IN_CAMPAIGN_REFEREED}
    for status in LEGACY_READ_ONLY_STATUSES:
        try:
            revision(logical_name="legacy-" + status.value.replace("_", "-"), status=status)
        except ValueError as exc:
            assert "legacy stored status" in str(exc)
        else:
            raise AssertionError(status)
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        item = revision(logical_name="legacy-read")
        append_revision(store, objects, item)
        row = store.connection.execute("SELECT payload_json FROM claims WHERE id = ?", (item.revision_id,)).fetchone()
        payload = json.loads(row["payload_json"])
        payload["status"] = RecordStatus.VERIFIED_REPLACEMENT.value
        legacy = Claim(**{**payload, "kind": ClaimKind(payload["kind"]), "status": RecordStatus.VERIFIED_REPLACEMENT,
                          "assumptions": tuple(payload["assumptions"])})
        store.connection.execute("UPDATE claims SET payload_json = ?, digest = ? WHERE id = ?",
                                 (json.dumps(payload), legacy.digest(), item.revision_id))
        claim = store.get_claim(item.revision_id)
        assert claim is not None and claim.status is RecordStatus.VERIFIED_REPLACEMENT
