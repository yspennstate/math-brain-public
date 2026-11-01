"""A compact statement is not a stub (interactive audit B100-02, 30 Sep 2026): the word count alone demoted every body
under eight words below any wordy candidate, the two infinitude-of-primes theorems in the live store among them. A
short body now counts as a statement when its claim kind says so; an empty body, a proof-attempt fragment and a node
with no claim kind stay below every statement, so an empty hub still cannot take the first slot."""

from math_brain.models import GraphNode, NodeKind
from math_brain.retrieval import retrieve

COMPACT = GraphNode(
    "compact",
    NodeKind.CLAIM,
    "Infinitude of primes",
    "There are infinitely many prime numbers.",
    metadata={"claim_kind": "theorem"},
)
WORDY = GraphNode(
    "wordy",
    NodeKind.CLAIM,
    "Bounded partial sums",
    "Sequences of real numbers whose partial sums stay bounded need not converge, as the alternating series shows.",
    metadata={"claim_kind": "theorem"},
)


def _order(nodes, query="prime numbers"):
    return [hit.node.id for hit in retrieve(query, nodes=nodes, edges=[], limit=10).hits]


def test_a_compact_theorem_ranks_by_its_score() -> None:
    everything = retrieve("prime numbers", nodes=[COMPACT, WORDY], edges=[], limit=10)
    scores = {hit.node.id: hit.total_score for hit in everything.hits}
    assert scores["compact"] > scores["wordy"]  # the fixture's premise
    assert _order([COMPACT, WORDY]) == ["compact", "wordy"]


def test_an_empty_body_stays_below_every_statement_however_well_its_title_matches() -> None:
    hub = GraphNode("hub", NodeKind.CLAIM, "prime numbers prime numbers", "", metadata={"claim_kind": "theorem"})
    assert _order([hub, COMPACT, WORDY])[-1] == "hub"


def test_a_short_fragment_without_a_statement_kind_stays_below() -> None:
    fragment = GraphNode(
        "fragment",
        NodeKind.CLAIM,
        "prime numbers campaign fire",
        "prime numbers only",
        metadata={"claim_kind": "proof_attempt"},
    )
    note = GraphNode("note", NodeKind.EVIDENCE, "prime numbers check", "prime numbers, author-checked")
    order = _order([fragment, note, COMPACT, WORDY])
    assert order[:2] == ["compact", "wordy"]
    assert set(order[2:]) == {"fragment", "note"}


def test_a_full_prose_statement_is_unaffected() -> None:
    assert _order([WORDY]) == ["wordy"]


def test_the_auditors_compact_formula_competes_without_a_claim_kind() -> None:
    # the audit's own counterexample: seven words, no metadata, a complete statement
    formula = GraphNode("formula", NodeKind.CLAIM, "Squares are nonnegative", "x² ≥ 0 for every real x.")
    verbose = GraphNode(
        "verbose",
        NodeKind.CLAIM,
        "Real sequences",
        "A long remark about real sequences that says nothing about squares or signs of any kind at all.",
    )
    everything = retrieve("squares nonnegative real", nodes=[formula, verbose], edges=[], limit=10)
    scores = {hit.node.id: hit.total_score for hit in everything.hits}
    assert scores["formula"] > scores["verbose"]  # the fixture's premise
    assert [hit.node.id for hit in everything.hits] == ["formula", "verbose"]


def test_a_short_note_without_a_relation_or_a_kind_stays_below() -> None:
    note = GraphNode("note", NodeKind.CLAIM, "prime numbers note", "prime numbers, author-checked")
    assert _order([note, COMPACT, WORDY])[-1] == "note"


def test_a_compact_statement_counts_toward_the_support_floor() -> None:
    # the floor judges the servable candidates; a compact theorem left out of them made the query abstain for weak
    # support even though a strongly supported statement was in the pool
    weak = GraphNode(
        "weak",
        NodeKind.CLAIM,
        "Unrelated remark",
        "A remark about numbers of a different kind whose statement concerns bounded sequences instead.",
        metadata={"claim_kind": "theorem"},
    )
    pool = retrieve("prime numbers", nodes=[COMPACT, weak], edges=[], limit=10)
    supports = {hit.node.id: hit.support_score for hit in pool.hits}
    floor = (supports["compact"] + supports["weak"]) / 2
    assert supports["compact"] > floor > supports["weak"]  # the fixture's premise
    result = retrieve("prime numbers", nodes=[COMPACT, weak], edges=[], limit=10, min_support_score=floor)
    assert not result.abstained
    assert result.hits[0].node.id == "compact"
