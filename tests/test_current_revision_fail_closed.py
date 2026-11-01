"""Revision resolution fails closed at retrieve() (1000-page report, D06-T02 and D06-T05, 30 Sep 2026).

T05: a statement that a correction supersedes is history even when the correction's row is missing. Until 30 Sep
only an edge whose source was also a given node counted, so the old text came back as current content from
retrieve() over a whole store (the path of `math_sense.py --query`); the note reader and the math hook's loader
already failed closed on a missing endpoint. A correction that exists but that the evaluation guard refuses is a
different case and keeps its zero influence (test_research_status_ablation), so the report's guard variant of T05
is answered by that rule, not by withholding.

T02: a family with two heads (two successors of one claim, no reviewed merge) serves neither head. Ranking would
otherwise choose one by relevance and present it as the current statement; read_current_note already refuses the
family as ambiguous.

Controls: a single successor, a chain, and a retraction resolve exactly as before.
"""

import dataclasses

from math_brain.models import EdgeKind, GraphEdge, GraphNode, NodeKind
from math_brain.retrieval import RetrievalGuard, current_revision_nodes, retrieve


def node(node_id: str, title: str, body: str, **metadata: object) -> GraphNode:
    return GraphNode(id=node_id, kind=NodeKind.CLAIM, title=title, body=body, metadata=dict(metadata))


def supersedes(newer: str, older: str) -> GraphEdge:
    return GraphEdge(source_id=newer, target_id=older, kind=EdgeKind.SUPERSEDES, rationale="correction")


OLD = node("old", "Deviation bound for the sample mean",
           "The sample mean deviates by more than t with probability at most exp(-n t^2 / 2) for every t.")
FIX = node("fix", "Deviation bound for the sample mean (Chebyshev)",
           "The sample mean deviates by more than t with probability at most s^2 / (n t^2) for every t > 0.")
QUERY = "deviation bound for the sample mean"


def reasons(exclusions) -> dict[str, str]:
    return {item.node_id: item.reason for item in exclusions}


def test_a_single_successor_is_served_and_its_predecessor_withheld_as_before() -> None:
    current, excluded = current_revision_nodes([OLD, FIX], [supersedes("fix", "old")])
    assert [n.id for n in current] == ["fix"]
    assert reasons(excluded) == {"old": "superseded_revision"}


def test_a_missing_correction_withholds_the_statement_it_replaced() -> None:
    current, excluded = current_revision_nodes([OLD], [supersedes("fix", "old")])
    assert current == ()
    assert reasons(excluded) == {"old": "superseded_by_unavailable_revision"}
    result = retrieve(QUERY, nodes=[OLD], edges=[supersedes("fix", "old")], limit=5,
                      min_support_score=0.0, min_margin=0.0)
    assert [hit.node.id for hit in result.hits] == []


def test_retrieve_withholds_history_whose_correction_is_missing_from_the_store() -> None:
    # the valid counterpart first: the pair together serves the correction
    valid = retrieve(QUERY, nodes=[OLD, FIX], edges=[supersedes("fix", "old")], limit=5,
                     min_support_score=0.0, min_margin=0.0)
    assert [hit.node.id for hit in valid.hits] == ["fix"]
    # the correction's row is gone, its edge is not: the old statement is not served as current
    missing = retrieve(QUERY, nodes=[OLD], edges=[supersedes("fix", "old")], limit=5,
                       min_support_score=0.0, min_margin=0.0)
    assert [hit.node.id for hit in missing.hits] == []
    assert reasons(missing.exclusions)["old"] == "superseded_by_unavailable_revision"
    # and the valid counterpart again, unchanged by the adverse call
    again = retrieve(QUERY, nodes=[OLD, FIX], edges=[supersedes("fix", "old")], limit=5,
                     min_support_score=0.0, min_margin=0.0)
    assert [hit.node.id for hit in again.hits] == ["fix"]


def test_a_correction_the_guard_excludes_has_no_effect_on_the_statement_it_replaced() -> None:
    """An ineligible node has no influence at all (test_ineligible_correction_cannot_hide_eligible_history): the
    evaluation guard holds the correction out, so the caller sees the store as it was before it."""
    guard = RetrievalGuard(evaluation_split="test", require_split_label=False)
    held_out = dataclasses.replace(FIX, metadata={"split": "test"})
    result = retrieve(QUERY, nodes=[OLD, held_out], edges=[supersedes("fix", "old")], limit=5,
                      min_support_score=0.0, min_margin=0.0, guard=guard)
    assert [hit.node.id for hit in result.hits] == ["old"]
    assert reasons(result.exclusions) == {"fix": "split_not_allowed:test"}


def test_two_successors_without_a_merge_serve_neither_head() -> None:
    base = node("base", "Mixing time bounded by relaxation time", "t_mix <= C t_rel log(1/pi_min).")
    left = node("left", "Mixing time bounded by relaxation time (positive mass)",
                "With pi_min > 0, t_mix <= C t_rel log(1/pi_min).")
    right = node("right", "Mixing time bounded by relaxation time (explicit constant)",
                 "t_mix <= t_rel (1 + log(1/pi_min) / 2).")
    edges = [supersedes("left", "base"), supersedes("right", "base")]
    current, excluded = current_revision_nodes([base, left, right], edges)
    assert current == ()
    assert reasons(excluded) == {"base": "superseded_revision", "left": "competing_revision_heads",
                                 "right": "competing_revision_heads"}
    # a head missing from the store still makes the family forked
    current, excluded = current_revision_nodes([base, left], edges)
    assert current == ()
    assert reasons(excluded)["left"] == "competing_revision_heads"
    # an ineligible head does not: the caller holds it and the guard refused it, so it has no effect
    current, excluded = current_revision_nodes([base, left], edges, known_ids=["base", "left", "right"])
    assert [n.id for n in current] == ["left"]
    assert reasons(excluded) == {"base": "superseded_revision"}


def test_a_merge_that_supersedes_both_heads_is_served() -> None:
    base = node("base", "Claim", "the first statement")
    left = node("left", "Claim, left", "the left statement")
    right = node("right", "Claim, right", "the right statement")
    merged = node("merged", "Claim, merged", "the reviewed statement")
    edges = [supersedes("left", "base"), supersedes("right", "base"),
             supersedes("merged", "left"), supersedes("merged", "right")]
    current, excluded = current_revision_nodes([base, left, right, merged], edges)
    assert [n.id for n in current] == ["merged"]
    assert set(reasons(excluded).values()) == {"superseded_revision"}


def test_a_chain_serves_only_its_head_and_leaves_other_nodes_alone() -> None:
    first = node("v1", "Claim", "one")
    second = node("v2", "Claim", "two")
    third = node("v3", "Claim", "three")
    other = node("other", "Another claim", "a different statement")
    current, excluded = current_revision_nodes(
        [first, second, third, other], [supersedes("v2", "v1"), supersedes("v3", "v2")])
    assert sorted(n.id for n in current) == ["other", "v3"]
    assert reasons(excluded) == {"v1": "superseded_revision", "v2": "superseded_revision"}
