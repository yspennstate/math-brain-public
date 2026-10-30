"""retrieve()'s support floor gives the same verdict at every limit.

Scheduled audit fleet04/B02 r72 (29 Sep 2026), B02-R72-SUPPORT-FLOOR-REMAINS-LIMIT-DEPENDENT-20260929: the pool is ordered
by total score, which adds warning mass to support, and the support floor judged only the first ``limit`` hits. A caution
card reached through a negative edge could fill a one-hit output and abstain for weak support, while the same query and
store asked for two hits served. The fixture below builds the warning mass through a real FAILS_UNDER edge from a stub
(a node with no statement, which scoring admits and the ordering demotes), not by constructing hits by hand.
"""

from __future__ import annotations

import pytest

from math_brain.models import EdgeKind, GraphEdge, GraphNode, NodeKind
from math_brain.retrieval import AbstentionReason, retrieve, search

QUERY = "martingale convergence theorem bounded"


def _fixture(sources: int = 1) -> tuple[list[GraphNode], list[GraphEdge]]:
    nodes = [
        GraphNode("warn_card", NodeKind.CLAIM, "A caution about interchanging limits",
                  "Interchanging a limit with an expectation requires a dominating function to exist."),
        GraphNode("supported", NodeKind.CLAIM, "A note on sequences",
                  "A bounded sequence of reals has a convergent subsequence."),
    ]
    edges = []
    for i in range(sources):
        nodes.append(GraphNode(f"source{i}", NodeKind.CLAIM, "martingale convergence theorem bounded", ""))
        edges.append(GraphEdge(f"source{i}", "warn_card", EdgeKind.FAILS_UNDER, "fails under the interchange"))
    return nodes, edges


def test_the_fixture_is_what_it_says() -> None:
    nodes, edges = _fixture()
    everything = retrieve(QUERY, nodes=nodes, edges=edges, limit=10, min_support_score=0.0, min_margin=0.0)
    first, second = everything.hits[0], everything.hits[1]
    assert first.node.id == "warn_card" and first.support_score < 0.15 < first.warning_score
    assert second.node.id == "supported" and second.support_score >= 0.15
    assert first.total_score > second.total_score
    assert any(t.edge_kind is EdgeKind.FAILS_UNDER for t in first.trace)


@pytest.mark.parametrize("sources", [1, 3])
def test_the_support_verdict_is_the_same_at_every_limit(sources: int) -> None:
    nodes, edges = _fixture(sources)
    verdicts = {limit: retrieve(QUERY, nodes=nodes, edges=edges, limit=limit) for limit in (1, 2, 10)}
    assert {(r.abstained, r.reason) for r in verdicts.values()} == {(False, None)}
    pool = len(retrieve(QUERY, nodes=nodes, edges=edges, limit=100).hits)
    for limit, result in verdicts.items():
        assert len(result.hits) == min(limit, pool)


def test_a_weak_whole_pool_abstains_at_every_limit() -> None:
    nodes, edges = _fixture()
    for limit in (1, 2, 10):
        result = retrieve(QUERY, nodes=nodes, edges=edges, limit=limit, min_support_score=1.0)
        assert result.abstained and result.reason is AbstentionReason.BELOW_SUPPORT_THRESHOLD


def test_a_demoted_stub_cannot_carry_the_floor() -> None:
    # the stubs match the query far better than anything else, but they have no statement: with a statement-bearing
    # candidate in the pool, only those are judged, at every limit
    nodes, edges = _fixture(3)
    for limit in (1, 2, 10):
        result = retrieve(QUERY, nodes=nodes, edges=edges, limit=limit, min_support_score=0.6)
        assert result.abstained and result.reason is AbstentionReason.BELOW_SUPPORT_THRESHOLD


def test_search_and_retrieve_agree_at_their_own_limits() -> None:
    nodes, edges = _fixture()
    small = search(QUERY, nodes=nodes, edges=edges, limit=1)
    large = retrieve(QUERY, nodes=nodes, edges=edges, limit=100000)
    small_abstained = getattr(small, "abstained", None)
    if small_abstained is not None:
        assert small_abstained == large.abstained
    assert not large.abstained
