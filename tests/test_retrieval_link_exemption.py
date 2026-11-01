"""A near tie between the two best-supported candidates is exempt from ambiguity abstention only through a link the
mode's walk follows, and the linked pair is then served together whatever the limit (interactive audit B100-01,
30 Sep 2026); the verdict stays the one an unlimited request gets (IA-20260929-MB-01)."""

import pytest

from math_brain.models import EdgeKind, GraphEdge, GraphNode, NodeKind
from math_brain.retrieval import PROOF_EDGE_KINDS, AbstentionReason, RetrievalMode, retrieve

NODES = (
    GraphNode("theorem", NodeKind.CLAIM, "finite group"),
    GraphNode("other", NodeKind.CLAIM, "finite group"),
)


def _edges(kind: EdgeKind | None) -> list[GraphEdge]:
    return [] if kind is None else [GraphEdge("theorem", "other", kind, "fixture link")]


@pytest.mark.parametrize("mode", [RetrievalMode.DISCOVERY, RetrievalMode.PROOF])
@pytest.mark.parametrize(
    "kind", [None, EdgeKind.SEMANTIC_ASSOCIATION, EdgeKind.CITES, EdgeKind.REFUTES]
)
@pytest.mark.parametrize("min_margin", [0.0, 0.01])
@pytest.mark.parametrize("limit", [1, 2])
def test_a_link_exempts_a_tie_only_when_the_walk_follows_it_and_serves_the_pair(
    mode: RetrievalMode, kind: EdgeKind | None, min_margin: float, limit: int
) -> None:
    tied = retrieve("group", nodes=NODES, edges=_edges(kind), min_margin=0.0, limit=2, mode=mode)
    assert len(tied.hits) == 2
    assert tied.hits[0].support_score == tied.hits[1].support_score, "fixture must be an exact tie"
    result = retrieve(
        "group", nodes=NODES, edges=_edges(kind), min_margin=min_margin, limit=limit, mode=mode
    )
    walked = kind is not None and (mode is RetrievalMode.DISCOVERY or kind in PROOF_EDGE_KINDS)
    assert result.abstained is (min_margin > 0 and not walked)
    if result.abstained:
        assert result.reason is AbstentionReason.AMBIGUOUS_TOP_MATCH
    elif min_margin > 0:
        # the exemption held: both linked candidates are served, even when one hit was asked for
        assert {hit.node.id for hit in result.hits} == {"theorem", "other"}


def test_a_proof_edge_that_settles_the_ranking_is_not_ambiguous() -> None:
    # the proof walk follows PROVES and raises the proved statement, so the margin itself answers the question
    result = retrieve(
        "group",
        nodes=NODES,
        edges=_edges(EdgeKind.PROVES),
        min_margin=0.01,
        limit=1,
        mode=RetrievalMode.PROOF,
    )
    assert not result.abstained
    assert result.hits[0].node.id == "other"
