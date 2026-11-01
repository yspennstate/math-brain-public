"""An overlay claim's card keeps its hypotheses (1000-page report, test D10-T01, 30 Sep 2026).

An overlay revision's node writes the statement and then each assumption on a line of its own,
with no marker, so render_parts read the assumptions as the tail of the statement and the budget
cut them first. Of the store's 4,163 claims with hypotheses, 3,125 delivered every one at the
live 480-character budget. claim_view gives such a node the "Assumes:" form from the claim's own
fields (3,763 then deliver them all), and render_parts keeps the hypotheses whatever the length
of the statement. A ledger record's provenance lines are not hypotheses and stay where they
were. The cases follow D10-T01: a necessary condition placed after a long result sentence,
rendered under a tight budget, must survive or the card must say it is incomplete; here it
survives.
"""

import json
from pathlib import Path

import pytest

from math_brain.delivery_audit import main as delivery_audit
from math_brain.models import Claim, ClaimKind, GraphNode, NodeKind, RecordStatus
from math_brain.overlay import (
    ContentAddressedTextStore,
    MathNodeRevision,
    SourceProvenance,
    TrustClass,
    append_revision,
)
from math_brain.rendering import claim_view, render_parts
from math_brain.store import ResearchStore

CONDITION = (
    "the averaging sets shrink nicely; for general families of sets the conclusion can fail"
)
LONG_RESULT = (
    "For every locally integrable f on R^n, the averages of f over balls centred at x converge "
    "to f(x) as the radius tends to zero, for almost every x; such x are the Lebesgue points "
    "of f. "
) + "The balls may be replaced by cubes centred at x, or by any family of sets in a ball. " * 6
TAIL = "|| Assumes: f locally integrable; " + CONDITION


def provenance() -> SourceProvenance:
    return SourceProvenance(
        source_id="source:claim-view-fixture",
        source_revision="git:0000000",
        locator="fixture-section-1",
        imported_by="test-suite",
        trust_class=TrustClass.PRIMARY_SOURCE,
    )


def revision(**changes: object) -> MathNodeRevision:
    values: dict[str, object] = {
        "namespace": "fixture.render",
        "logical_name": "lebesgue-differentiation",
        "kind": ClaimKind.THEOREM,
        "title": "Lebesgue differentiation theorem",
        "statement": LONG_RESULT,
        "assumptions": ("f locally integrable", CONDITION),
        "provenance": provenance(),
        "domain": "analysis",
    }
    values.update(changes)
    return MathNodeRevision(**values)  # type: ignore[arg-type]


def stored(tmp_path: Path, item: MathNodeRevision) -> tuple[GraphNode, Claim]:
    objects = ContentAddressedTextStore(tmp_path / "objects")
    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        node = append_revision(store, objects, item).node
        claim = store.get_claim(item.revision_id)
        assert claim is not None
        read_back = store.get_node(node.id)
    assert read_back is not None and read_back.body == node.body
    return read_back, claim


def rendered(node: GraphNode, claim: Claim, budget: int = 480, query: str = "") -> str:
    view = claim_view(node, claim.statement, claim.assumptions)
    return render_parts(view, max_text_chars=budget, query=query)[1]


def test_a_condition_after_a_long_result_survives_every_budget(tmp_path: Path) -> None:
    node, claim = stored(tmp_path, revision())
    # the overlay shape, unmarked
    assert node.body == "\n".join([claim.statement, *claim.assumptions])
    for budget in (200, 320, 480):
        for query in ("", "averages over balls", "Lebesgue points"):
            text = rendered(node, claim, budget, query)
            assert text.endswith(TAIL), (budget, query)
            assert len(text) <= budget + 8, (budget, query)
    # the statement is still the start of the card, and the view left the stored node alone
    assert rendered(node, claim).startswith("For every locally integrable f on R^n")
    assert node.body == "\n".join([claim.statement, *claim.assumptions])


def test_a_short_claim_is_served_whole_with_the_same_words(tmp_path: Path) -> None:
    short = "Averages over balls centred at x converge to f(x) for almost every x."
    node, claim = stored(tmp_path, revision(statement=short))
    _, plain = render_parts(node, max_text_chars=480)
    assert rendered(node, claim) == short + " " + TAIL
    # only the separator is new
    assert plain.split() == (short + " f locally integrable " + CONDITION).split()


def test_a_statement_on_several_lines_is_split_where_the_claim_ends(tmp_path: Path) -> None:
    statement = (
        "Part (a): the averages converge almost everywhere.\n"
        "Part (b): the maximal function is weak (1,1)."
    )
    node, claim = stored(tmp_path, revision(statement=statement))
    head, clause = rendered(node, claim).split(" || Assumes: ")
    assert "Part (b): the maximal function is weak (1,1)." in head
    assert clause == "f locally integrable; " + CONDITION


def test_a_conditional_revision_keeps_its_conditions(tmp_path: Path) -> None:
    lemma = "the covering lemma holds with constant 3^n"
    item = revision(
        status=RecordStatus.CONDITIONAL,
        evidence_ids=("evidence_numeric",),
        conditions=(lemma,),
    )
    node, claim = stored(tmp_path, item)
    assert list(node.metadata["conditions"]) == [lemma]  # a list once stored
    assert rendered(node, claim).endswith(TAIL + "; " + lemma)


def test_nodes_that_are_not_the_unmarked_overlay_shape_come_back_unchanged(
    tmp_path: Path,
) -> None:
    # an overlay claim without assumptions
    node, claim = stored(tmp_path / "a", revision(assumptions=()))
    assert claim_view(node, claim.statement, claim.assumptions) is node
    # a claim in the store's own projection, which already carries its Assumes clause
    plain = Claim(
        statement=LONG_RESULT, kind=ClaimKind.THEOREM, assumptions=("f locally integrable",)
    )
    (tmp_path / "b").mkdir()
    with ResearchStore(tmp_path / "b" / "brain.sqlite3") as store:
        store.add_claim(plain)
        store_node = store.get_node(plain.id)
    assert store_node is not None
    assert claim_view(store_node, plain.statement, plain.assumptions) is store_node
    # a legacy node: the whole statement in the title, only the assumptions in the body
    legacy = GraphNode(
        "legacy", NodeKind.CLAIM, LONG_RESULT, "f locally integrable",
        metadata={"claim_kind": "theorem"},
    )
    assert claim_view(legacy, LONG_RESULT, ("f locally integrable",)) is legacy
    # a claim whose fields do not match the node, and a node that is not a claim
    node, claim = stored(tmp_path / "c", revision())
    assert claim_view(node, claim.statement + " changed", claim.assumptions) is node
    assert claim_view(node, claim.statement, claim.assumptions[:1]) is node
    other = GraphNode("n", NodeKind.CLAIM, "T", "s\na", metadata={})
    assert claim_view(other, "s", ("a",)) is other
    # an empty assumption line is left alone rather than rendered as "; ;"
    blank = GraphNode("b", NodeKind.CLAIM, "T", "s\n\na", metadata={"claim_kind": "theorem"})
    assert claim_view(blank, "s", ("", "a")) is blank


RECORD_LINES = (
    "Posed in D Achille and Khezeli: Convergence towards Ideal Poisson Voronoi tessellations",
    "Status as recorded in the campaign ledger on 2026-09-07",
)
LEDGER_STATEMENT = (
    "OPEN PROBLEM from the campaign ledger (source_says_open; current status unverified). "
    "Identify the limiting boundary measure for products with the L2 metric, including "
    "comparison with a weighted L1 model. "
) + "Status notes: a primary literature check found no later resolution. " * 3 + "Source: PDF49."


def test_a_ledger_record_is_left_as_it_was(tmp_path: Path) -> None:
    """Its lines are record fields, not hypotheses; protecting them cut the page number off."""
    item = revision(kind=ClaimKind.CONCEPT, statement=LEDGER_STATEMENT, assumptions=RECORD_LINES)
    node, claim = stored(tmp_path, item)
    assert claim_view(node, claim.statement, claim.assumptions) is node
    assert "Source: PDF49." in rendered(node, claim)


def test_a_record_line_stays_behind_the_statement_and_a_hypothesis_is_protected(
    tmp_path: Path,
) -> None:
    mixed = ("f locally integrable", RECORD_LINES[1])
    node, claim = stored(tmp_path, revision(assumptions=mixed))
    view = claim_view(node, claim.statement, claim.assumptions)
    assert view.body.endswith(" " + RECORD_LINES[1] + " Assumes: f locally integrable")
    assert rendered(node, claim, budget=320).endswith("|| Assumes: f locally integrable")


def test_the_delivery_audit_counts_hypotheses_as_the_hook_renders_them(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    stored(tmp_path, revision())
    # the fixture states no numeric value, so the audit's main rate is out of scope (exit 4);
    # the hypothesis line is measured all the same
    args = ["--store", str(tmp_path / "brain.sqlite3"), "--budget", "480", "--json"]
    assert delivery_audit(args) == 4
    report = json.loads(capsys.readouterr().out)
    assert report["status"] == "NONE_IN_SCOPE"
    assert report["assumptions"]["carrying"] == 1
    assert report["assumptions"]["intact"] == 1
