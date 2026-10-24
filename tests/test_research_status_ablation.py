"""Synthetic routing regression, NOT a held-out study or a live-store query.

Run with pytest, or directly to print the versioned diagnostic rows. Every
fixture below is original test text, not an excerpt from research records.
The lexical/formula arm preserves version edges and disables all graph mass.
"""

import json
import os
from dataclasses import asdict, replace
from datetime import datetime

import pytest

from math_brain import retrieval
from math_brain.models import EdgeKind, GraphEdge, GraphNode, NodeKind, content_hash
from math_brain.retrieval import RetrievalGuard, retrieve

EARLY = "2026-09-10T00:00:00+00:00"
LATE = "2026-09-16T00:00:00+00:00"
CUTOFF = "2026-09-20T00:00:00+00:00"
QUERY = "Which variance classification research statement currently applies?"
LIMIT = 2
BYTE_LIMIT = 2048


def aware(value):
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("availability and cutoff timestamps must have a timezone")
    return parsed


def fixture():
    title = "Variance classification research statement"
    old = GraphNode(
        "a-prior",
        NodeKind.CLAIM,
        title,
        "The variance classification research statement covers bounded input measures only.",
        {"split": "reference", "available_at": EARLY, "status": "provisional"},
        created_at=EARLY,
    )
    new = GraphNode(
        "z-current",
        NodeKind.CLAIM,
        title,
        "The variance classification research statement covers arbitrary input measures now.",
        {"split": "reference", "available_at": LATE, "status": "unverified"},
        created_at=LATE,
    )
    edge = GraphEdge(
        new.id,
        old.id,
        EdgeKind.SUPERSEDES,
        "The later statement corrects the scope.",
        metadata={"available_at": LATE},
        id="revision",
        created_at=LATE,
    )
    return (old, new), (edge,)


def freeze(nodes, edges, cutoff):
    """Use evidenced availability, not a filename or a backdated creation field.

    This test harness needs an explicit availability field. It cannot certify
    that a real source was available: the ingestion/export layer must attest it.
    """
    moment = aware(cutoff)
    # Validate all records before filtering, including future/dangling records.
    times = {("node", n.id): aware(n.metadata["available_at"]) for n in nodes}
    times.update({("edge", e.id): aware(e.metadata["available_at"]) for e in edges})
    if len({n.id for n in nodes}) != len(nodes):
        raise ValueError("duplicate node identifier")
    if len({e.id for e in edges}) != len(edges):
        raise ValueError("duplicate edge identifier")
    selected = tuple(n for n in nodes if times["node", n.id] <= moment)
    ids = {n.id for n in selected}
    links = tuple(
        e
        for e in edges
        if times["edge", e.id] <= moment and e.source_id in ids and e.target_id in ids
    )
    return selected, links


def replay(nodes, edges, cutoff=CUTOFF, *, depth=0, query=QUERY):
    if os.environ.get("MATH_BRAIN_SEMANTIC", "0") != "0":
        raise ValueError("this ablation requires the semantic lane disabled")
    if retrieval.EXPANSION or retrieval._SIGNAL_DB is not None:
        raise ValueError("this ablation requires no external expansion or signal store")
    nodes, edges = freeze(tuple(nodes), tuple(edges), cutoff)
    result = retrieve(
        query,
        nodes=nodes,
        edges=edges,
        graph_depth=depth,
        decay=0.0 if depth == 0 else 0.55,
        limit=LIMIT,
        seed_limit=8,
        guard=RetrievalGuard(evaluation_split="heldout"),
    )
    rendered = []
    used = 0
    for hit in () if result.abstained else result.hits:
        text = hit.node.title + "\n" + hit.node.body
        cost = len(text.encode("utf-8"))
        if used + cost > BYTE_LIMIT:
            break
        rendered.append(
            {
                "id": hit.node.id,
                "status": hit.node.metadata.get("status"),
                "text": text,
                "graph_score": hit.graph_score,
                "warning_score": hit.warning_score,
            }
        )
        used += cost
    return {
        "snapshot_digest": content_hash(
            {
                "nodes": sorted((asdict(n) for n in nodes), key=lambda n: n["id"]),
                "edges": sorted((asdict(e) for e in edges), key=lambda e: e["id"]),
                "cutoff": cutoff,
            }
        ),
        "graph_depth": depth,
        "decay": 0.0 if depth == 0 else 0.55,
        "hit_budget": LIMIT,
        "byte_budget": BYTE_LIMIT,
        "rendered_bytes": used,
        "hits": rendered,
        "abstained": result.abstained,
        "exclusions": sorted((e.node_id, e.reason) for e in result.exclusions),
    }


def ids(result):
    return [h["id"] for h in result["hits"]]


@pytest.mark.parametrize("depth", [0, 2])
def test_explicit_revision_is_current_in_both_arms(depth):
    nodes, edges = fixture()
    row = replay(nodes, edges, depth=depth)
    assert ids(row) == ["z-current"]
    assert [h["status"] for h in row["hits"]] == ["unverified"]
    assert ("a-prior", "superseded_revision") in row["exclusions"]


def test_dropping_edges_is_a_confounded_lexical_baseline():
    nodes, edges = fixture()
    fair = replay(nodes, edges, depth=0)
    confounded = replay(nodes, (), depth=0)
    assert ids(fair) == ["z-current"]
    assert "a-prior" in ids(confounded)
    assert fair["snapshot_digest"] != confounded["snapshot_digest"]


def test_surface_arm_has_no_graph_or_warning_mass():
    nodes, edges = fixture()
    for links in (edges, (), (replace(edges[0], kind=EdgeKind.DEPENDS_ON),)):
        result = replay(nodes, links, depth=0)
        assert all(h["graph_score"] == 0 and h["warning_score"] == 0 for h in result["hits"])


def test_surface_arm_avoids_depth_only_seed_retention_rank_reversal():
    # Fixed-seed search witness: deterministic original words, not owner data.
    rows = [
        (
            "lemma revision delta branch measure",
            "classification lemma corrected lemma revision convolution integration convolution "
            "corrected branch measure measure branch measure classification analytic",
        ),
        (
            "analytic",
            "lemma measure classification inverse integration delta revision "
            "corrected variance delta",
        ),
        (
            "corrected lemma classification analytic",
            "variance branch convolution analytic inverse branch lemma delta revision lemma "
            "inverse lemma corrected analytic revision variance convolution classification "
            "corrected measure delta branch lemma corrected convolution measure integration "
            "integration delta lemma variance measure measure inverse branch",
        ),
    ]
    nodes = [
        GraphNode(
            str(i),
            NodeKind.CLAIM,
            title,
            body,
            {"split": "reference", "available_at": EARLY},
            created_at=EARLY,
        )
        for i, (title, body) in enumerate(rows)
    ]
    query = "revision delta delta measure variance"
    zero_depth = retrieve(query, nodes=nodes, edges=[], graph_depth=0)
    zero_weight = retrieve(query, nodes=nodes, edges=[], graph_depth=0, decay=0)
    # Existing production semantics are preserved: depth controls traversal,
    # not zero-hop retention. A benchmark must not call this graph-off.
    assert zero_depth.hits[0].node.id == "1"
    assert zero_weight.hits[0].node.id == "0"
    assert ids(replay(nodes, (), query=query)) == [h.node.id for h in zero_weight.hits[:LIMIT]]


@pytest.mark.parametrize("depth", [0, 2])
def test_creation_dates_do_not_supply_missing_revision_links(depth):
    nodes, _ = fixture()
    # Equal surface text isolates date preference from relevance differences.
    new = replace(nodes[1], body=nodes[0].body)
    assert ids(replay((nodes[0], new), (), depth=depth)) == ["a-prior", "z-current"]


@pytest.mark.parametrize("depth", [0, 2])
def test_future_revision_cannot_erase_the_asof_source(depth):
    nodes, edges = fixture()
    row = replay(nodes, edges, cutoff=EARLY, depth=depth)
    assert ids(row) == ["a-prior"]
    assert not row["exclusions"]


def test_backdated_creation_does_not_make_a_future_node_available():
    nodes, edges = fixture()
    backdated = replace(nodes[1], created_at=EARLY)
    assert ids(replay((nodes[0], backdated), edges, cutoff=EARLY)) == ["a-prior"]


def test_future_edge_cannot_suppress_an_earlier_source():
    nodes, edges = fixture()
    delayed = replace(edges[0], metadata={"available_at": "2026-10-01T00:00:00+00:00"})
    assert "a-prior" in ids(replay(nodes, (delayed,)))


@pytest.mark.parametrize(
    "marker",
    [
        {"is_answer_key": True},
        {"split": "heldout"},
        {"quarantined": True},
        {"content_role": "solution"},
    ],
)
def test_ineligible_correction_cannot_hide_eligible_history(marker):
    nodes, edges = fixture()
    blocked = replace(nodes[1], metadata={**nodes[1].metadata, **marker})
    for depth in (0, 2):
        assert ids(replay((nodes[0], blocked), edges, depth=depth)) == ["a-prior"]


def test_both_arms_share_snapshot_and_output_budget():
    nodes, edges = fixture()
    a, b = (replay(nodes, edges, depth=d) for d in (0, 2))
    for field in ("snapshot_digest", "hit_budget", "byte_budget", "exclusions"):
        assert a[field] == b[field]
    assert a["rendered_bytes"] <= BYTE_LIMIT and b["rendered_bytes"] <= BYTE_LIMIT


def test_input_order_does_not_change_digest_or_output():
    nodes, edges = fixture()
    assert replay(nodes, edges) == replay(nodes[::-1], edges[::-1])


def test_no_match_abstains_in_both_arms():
    nodes, edges = fixture()
    for depth in (0, 2):
        row = replay(nodes, edges, depth=depth, query="cyclotomic tessellation")
        assert row["abstained"] and not row["hits"]


def test_graph_positive_control_reaches_a_nonlexical_neighbor():
    nodes, _ = fixture()
    neighbor = replace(
        nodes[1],
        title="Analytic continuation lemma",
        body="The analytic continuation lemma identifies a unique local inverse branch.",
    )
    link = GraphEdge(
        nodes[0].id,
        neighbor.id,
        EdgeKind.DEPENDS_ON,
        "The research statement uses this analytic lemma.",
        id="dependency",
        metadata={"available_at": LATE},
        created_at=LATE,
    )
    corpus = (nodes[0], neighbor)
    assert ids(replay(corpus, (link,), depth=0)) == ["a-prior"]
    graph = replay(corpus, (link,), depth=2)
    assert "z-current" in ids(graph)
    assert next(h for h in graph["hits"] if h["id"] == "z-current")["graph_score"] > 0


@pytest.mark.parametrize("bad", ["2026-09-16", "not-a-date"])
def test_ambiguous_availability_fails_closed(bad):
    nodes, edges = fixture()
    invalid = replace(nodes[1], metadata={**nodes[1].metadata, "available_at": bad})
    with pytest.raises(ValueError):
        replay((nodes[0], invalid), edges)


def test_missing_availability_fails_closed():
    nodes, edges = fixture()
    invalid = replace(nodes[1], metadata={"split": "reference"})
    with pytest.raises(KeyError):
        replay((nodes[0], invalid), edges)


def test_changed_reference_text_changes_snapshot_digest():
    nodes, edges = fixture()
    changed = replace(nodes[1], body=nodes[1].body + " Additional qualification.")
    assert (
        replay(nodes, edges)["snapshot_digest"]
        != replay((nodes[0], changed), edges)["snapshot_digest"]
    )


if __name__ == "__main__":
    records, relations = fixture()
    payload = {
        "schema_version": 1,
        "evidence_class": "synthetic_runtime_regression_not_heldout",
        "rows": {
            "lexical_current": replay(records, relations, depth=0),
            "graph_current": replay(records, relations, depth=2),
            "confounded_edges_removed": replay(records, (), depth=0),
            "lexical_historical_cutoff": replay(records, relations, EARLY, depth=0),
            "graph_historical_cutoff": replay(records, relations, EARLY, depth=2),
        },
    }
    print(json.dumps({**payload, "digest": content_hash(payload)}, indent=2, sort_keys=True))
