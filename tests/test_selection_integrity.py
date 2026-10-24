"""consistent_hits and a selected card the integrity read refuses (audit account04/B04 r69)."""

from types import SimpleNamespace

import pytest

from math_brain.current_note import NoteReadError
from math_brain.selection_integrity import ON_REFUSAL, SelectionUnavailable, consistent_hits


class _Node:
    def __init__(self, nid, kind="claim"):
        self.id, self.kind, self.metadata = nid, kind, {}

    def digest(self):
        return "digest-" + self.id


def _hit(nid, kind="claim"):
    return SimpleNamespace(node=_Node(nid, kind))


def _reader(refused):
    def read(database, node_id, artifact_root=None):
        if node_id in refused:
            raise NoteReadError(refused[node_id])
        return {"current_id": node_id, "computed_node_digest": "digest-" + node_id,
                "body_complete": True, "artifact": {"verification": "none"}}
    return read


def _run(hits, refused, **kw):
    return consistent_hits(hits, "unused.sqlite3", deadline=float("inf"),
                           reader=_reader(refused), clock=lambda: 0.0, **kw)


def _ids(hits):
    return [h.node.id for h in hits]


@pytest.mark.parametrize("mode", ON_REFUSAL)
def test_consistent_cards_come_back_in_their_order(mode):
    hits = [_hit("a"), _hit("b"), _hit("c")]
    assert _run(hits, {}, on_refusal=mode) == hits


def test_drop_moves_the_runner_up_first_when_the_first_card_is_refused():
    hits = [_hit("a"), _hit("b")]
    assert _ids(_run(hits, {"a": "stored_node_digest_mismatch"})) == ["b"]


@pytest.mark.parametrize("mode", ["first", "all"])
def test_a_refused_first_card_refuses_the_selection(mode):
    hits = [_hit("a"), _hit("b")]
    with pytest.raises(SelectionUnavailable,
                       match="selected_card_refused:stored_node_digest_mismatch"):
        _run(hits, {"a": "stored_node_digest_mismatch"}, on_refusal=mode)


def test_first_drops_a_refused_later_card_and_keeps_the_first():
    hits = [_hit("a"), _hit("b"), _hit("c")]
    kept = _run(hits, {"b": "missing_artifact_binding"}, on_refusal="first")
    assert _ids(kept) == ["a", "c"]


def test_all_refuses_the_selection_when_a_later_card_is_refused():
    hits = [_hit("a"), _hit("b")]
    with pytest.raises(SelectionUnavailable,
                       match="selected_card_refused:missing_artifact_binding"):
        _run(hits, {"b": "missing_artifact_binding"}, on_refusal="all")


def test_a_refusal_is_recorded_before_it_raises():
    diagnostics = []
    with pytest.raises(SelectionUnavailable):
        _run([_hit("a")], {"a": "claim_node_statement_mismatch"}, on_refusal="first",
             diagnostics=diagnostics)
    assert diagnostics == [
        {"id": "a", "status": "REFUSED", "reason": "claim_node_statement_mismatch"}]


@pytest.mark.parametrize("mode", ON_REFUSAL)
def test_a_store_level_failure_keeps_its_own_reason(mode):
    with pytest.raises(SelectionUnavailable, match=r"^read_failed_or_inconsistent$"):
        _run([_hit("a")], {"a": "read_failed_or_inconsistent"}, on_refusal=mode)


def test_the_first_card_is_the_first_one_that_is_not_evidence():
    hits = [_hit("e", kind="evidence"), _hit("a"), _hit("b")]
    assert _ids(_run(hits, {}, on_refusal="first")) == ["a", "b"]
    with pytest.raises(SelectionUnavailable):
        _run(hits, {"a": "missing_artifact_binding"}, on_refusal="first")


def test_an_unknown_mode_is_refused():
    with pytest.raises(ValueError, match="on_refusal"):
        _run([_hit("a")], {}, on_refusal="strict")
