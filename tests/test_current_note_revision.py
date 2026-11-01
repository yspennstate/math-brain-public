"""A superseded revision's id reads the current note, labelled (1000-page report, test D10-T04).

The report's case: a caller holds an older revision (its title may even match the question better)
and asks for it. The reader must return the current object and say so, never the old text as if it
were current. read_current_note resolves the family's current revision, reports the requested and
current ids with revision_changed, and withholds every predecessor's text.
"""

import json
from pathlib import Path

from math_brain.current_note import read_current_note
from math_brain.models import ClaimKind
from math_brain.overlay import (
    ContentAddressedTextStore,
    MathNodeRevision,
    SourceProvenance,
    TrustClass,
    append_revision,
)
from math_brain.store import ResearchStore

OLD = "Every bounded sequence of reals converges."
NEW = "Every bounded monotone sequence of reals converges."


def revision(**changes: object) -> MathNodeRevision:
    values: dict[str, object] = {
        "namespace": "fixture.note",
        "logical_name": "monotone-convergence",
        "kind": ClaimKind.THEOREM,
        "title": "Bounded sequences converge (stronger-sounding old title)",
        "statement": OLD,
        "provenance": SourceProvenance(
            source_id="source:note-fixture",
            source_revision="git:0000000",
            locator="fixture-1",
            imported_by="test-suite",
            trust_class=TrustClass.PRIMARY_SOURCE,
        ),
        "domain": "analysis",
    }
    values.update(changes)
    return MathNodeRevision(**values)  # type: ignore[arg-type]


def test_the_old_id_reads_the_current_revision_and_says_so(tmp_path: Path) -> None:
    objects = ContentAddressedTextStore(tmp_path / "objects")
    database = tmp_path / "brain.sqlite3"
    first = revision()
    correction = revision(
        title="Monotone convergence theorem", statement=NEW, supersedes=(first.revision_id,)
    )
    with ResearchStore(database) as store:
        append_revision(store, objects, first)
        append_revision(store, objects, correction)

    note = read_current_note(database, first.revision_id)
    assert note["requested_id"] == first.revision_id
    assert note["current_id"] == correction.revision_id
    assert note["revision_changed"] is True
    assert note["revision_family_size"] == 2
    assert note["node"]["id"] == correction.revision_id
    assert note["claim"]["statement"] == NEW
    # the predecessor's text is not returned anywhere in the note
    assert OLD not in json.dumps(note)

    # the current id reads itself, unflagged
    current = read_current_note(database, correction.revision_id)
    assert current["current_id"] == correction.revision_id
    assert current["revision_changed"] is False
