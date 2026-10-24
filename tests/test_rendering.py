from math_brain.models import GraphNode, NodeKind
from math_brain.rendering import render_parts


def _legacy_claim() -> GraphNode:
    statement = (
        "FPP campaign row: constant-A variance doubling at one scale ratio would "
        "propagate along a quantile interpolation segment and improve the linear "
        "certificate at every larger dyadic scale, provided the engine implication "
        "holds at each interpolated law with constants independent of the scale."
    )
    return GraphNode(
        "legacy",
        NodeKind.CLAIM,
        statement,
        "bounded non-degenerate weights on [a,b]\nthe implication holds uniformly (NOT available)",
        metadata={"claim_kind": "proof_attempt", "domain": "probability.fpp"},
    )


def test_legacy_claim_reunites_statement_with_assumptions() -> None:
    label, text = render_parts(_legacy_claim())
    assert label.endswith("...")
    assert len(label) <= 123
    assert "constant-A variance doubling" in text
    assert "Assumes: bounded non-degenerate weights on [a,b]; " in text
    assert "(NOT available)" in text


def test_assumes_tail_survives_any_statement_length() -> None:
    node = _legacy_claim()
    long_node = GraphNode(
        node.id,
        node.kind,
        node.title + " " + "very long tail of extra prose " * 40,
        node.body,
        metadata=node.metadata,
    )
    _, text = render_parts(long_node)
    assert "(NOT available)" in text
    assert len(text) <= 320 + 8


def test_new_shape_claim_keeps_inline_assumes_through_truncation() -> None:
    statement = "The mixing time is at most quadratic in the relaxation time. " * 12
    body = statement.strip() + "\n\nAssumes: lazy reversible chain; finite state space"
    node = GraphNode(
        "new",
        NodeKind.CLAIM,
        "Mixing versus relaxation",
        body,
        metadata={"claim_kind": "theorem", "domain": "probability"},
    )
    label, text = render_parts(node)
    assert label == "Mixing versus relaxation"
    assert text.endswith("|| Assumes: lazy reversible chain; finite state space")
    assert len(text) <= 320 + 8


def test_non_claim_nodes_pass_through_with_plain_truncation() -> None:
    node = GraphNode("plain", NodeKind.CLAIM, "Stopping time", "A stopping time is " + "x" * 400)
    label, text = render_parts(node)
    assert label == "Stopping time"
    assert text.startswith("A stopping time is")
    assert len(text) == 320
