import pytest

from math_brain.models import EdgeKind, EdgePolarity, GraphEdge, GraphNode, NodeKind
from math_brain.retrieval import (
    AbstentionReason,
    RetrievalGuard,
    RetrievalMode,
    ScoreChannel,
    exact_dependency_closure,
    index_signals,
    retrieve,
    search,
    tokenize,
)


def test_unicode_tokenization() -> None:
    # Accents fold (2026-09-12): the accented and ASCII spellings of a name must be ONE token, or a query typed
    # the way a mathematician writes it ranks the wrong node. Measured before the fold on an identical candidate
    # set: "Vitali-Caratheodory" ranked its own node 1st in ASCII and 5th with the accent and en-dash.
    assert tokenize("Poincaré duality") == tokenize("Poincare duality")
    assert "poincare" in tokenize("Poincaré duality")
    assert tokenize("Vitali–Carathéodory theorem") == ("vitali-caratheodory", "theorem")
    # Greek and other non-Latin letters are not diacritics and survive the fold (a hyphenated word stays one token).
    assert "λ-calculus" in tokenize("the λ-calculus")
    assert "λ" in tokenize("the λ calculus")


def test_latex_and_unicode_formulae_have_the_same_alpha_normalized_signals() -> None:
    latex = index_signals(r"$\forall x \in \mathbb{R}, x^2 \geq 0$")
    unicode_notation = index_signals("$∀ y ∈ ℝ, y² ≥ 0$")
    assert latex.math_tokens == unicode_notation.math_tokens
    assert latex.formula_fingerprints == unicode_notation.formula_fingerprints


def test_formula_normalization_does_not_merge_changed_operators_or_exponents() -> None:
    square = index_signals(r"$x^2 \ge 0$").formula_fingerprints
    cube = index_signals(r"$y^3 \ge 0$").formula_fingerprints
    negative_square = index_signals(r"$z^2 \le 0$").formula_fingerprints
    assert square != cube
    assert square != negative_square


def test_latex_unicode_and_plain_variables_share_alpha_normalization() -> None:
    latex_greek = index_signals(r"$\alpha + \beta = \gamma$")
    unicode_greek = index_signals("$α + β = γ$")
    plain = index_signals("$x + y = z$")
    assert latex_greek.formula_fingerprints == unicode_greek.formula_fingerprints
    assert latex_greek.formula_fingerprints == plain.formula_fingerprints


def test_latex_and_plain_named_functions_share_formula_signals() -> None:
    latex = index_signals(r"$\sin(\theta) = 0$")
    plain = index_signals("$sin(x) = 0$")
    assert latex.formula_fingerprints == plain.formula_fingerprints


def test_formula_normalization_handles_a_very_long_numeral_without_integer_parsing() -> None:
    numeral = "0" * 5_000 + "17"
    signals = index_signals(f"$x = {numeral}$")
    assert "num:17" in signals.math_tokens


def test_formula_signal_and_trace_rank_alpha_equivalent_formula() -> None:
    formula = GraphNode(
        "formula",
        NodeKind.CLAIM,
        "Quadratic nonnegativity",
        r"For real a, $a^2 \ge 0$.",
    )
    noise = GraphNode("noise", NodeKind.CLAIM, "A qualitative lower bound")
    result = retrieve(r"$z² ≥ 0$", nodes=[noise, formula], edges=[])
    assert not result.abstained
    assert result.hits[0].node.id == "formula"
    assert result.hits[0].formula_score > 0
    assert any(item.channel is ScoreChannel.FORMULA for item in result.hits[0].trace)


def test_score_trace_exactly_explains_each_component() -> None:
    node = GraphNode("claim", NodeKind.CLAIM, "Polynomial", r"$x^2 \ge 0$")
    hit = retrieve(r"polynomial $y² ≥ 0$", nodes=[node], edges=[]).hits[0]
    channel_totals = {
        channel: sum(item.amount for item in hit.trace if item.channel is channel)
        for channel in ScoreChannel
    }
    assert channel_totals[ScoreChannel.LEXICAL] == pytest.approx(hit.lexical_score)
    assert channel_totals[ScoreChannel.SYMBOL] == pytest.approx(hit.symbol_score)
    assert channel_totals[ScoreChannel.FORMULA] == pytest.approx(hit.formula_score)
    assert channel_totals[ScoreChannel.GRAPH] == pytest.approx(hit.graph_score)
    assert channel_totals[ScoreChannel.WARNING] == pytest.approx(hit.warning_score)


def test_query_naming_a_node_title_outranks_related_material() -> None:
    named = GraphNode(
        "named",
        NodeKind.CLAIM,
        "First Isomorphism Theorem",
        "For a group homomorphism phi, the quotient G/ker(phi) is isomorphic to im(phi).",
    )
    related = GraphNode(
        "related",
        NodeKind.CLAIM,
        "Group Homomorphism and Kernel",
        "A group homomorphism maps products to products; the kernel of a group "
        "homomorphism is a normal subgroup of the group, and the kernel of the "
        "group homomorphism controls injectivity of the group homomorphism.",
    )
    result = retrieve(
        "quotient by a normal subgroup and the first isomorphism theorem",
        nodes=[named, related],
        edges=[],
    )
    assert not result.abstained
    assert result.hits[0].node.id == "named"
    assert any(
        item.channel is ScoreChannel.LEXICAL and "title phrase" in item.detail
        for item in result.hits[0].trace
    )


def test_possessive_titles_still_phrase_match_plain_queries() -> None:
    named = GraphNode(
        "lagrange",
        NodeKind.CLAIM,
        "Lagrange's Theorem",
        "The order of a subgroup of a finite group divides the order of the group.",
    )
    decoy = GraphNode(
        "decoy",
        NodeKind.CLAIM,
        "Finite Group Orders",
        "Orders of elements of a finite group and orders of its subgroups; the "
        "order of the group is the product over its composition factors.",
    )
    result = retrieve(
        "lagrange theorem on subgroup order",
        nodes=[decoy, named],
        edges=[],
    )
    assert not result.abstained
    assert result.hits[0].node.id == "lagrange"
    assert any("title phrase" in item.detail for item in result.hits[0].trace)


def test_negative_edges_surface_as_signed_warnings() -> None:
    claim = GraphNode("claim", NodeKind.CLAIM, "Interchange limit and integral")
    warning = GraphNode(
        "warning", NodeKind.ERROR_PATTERN, "Dominated convergence assumptions fail"
    )
    edge = GraphEdge(
        "claim",
        "warning",
        EdgeKind.FAILS_UNDER,
        "domination is absent",
        id="edge_warning",
    )
    hits = search("limit integral", nodes=[claim, warning], edges=[edge])
    warning_hit = next(hit for hit in hits if hit.node.id == "warning")
    assert warning_hit.warning_score > 0
    assert warning_hit.graph_score == 0
    assert warning_hit.warnings
    assert warning_hit.warnings[0].edge_polarity is EdgePolarity.NEGATIVE
    assert warning_hit.warnings[0].signed_amount < 0


@pytest.mark.parametrize(
    ("query", "nodes", "threshold", "reason"),
    [
        ("   ", [], 0.15, AbstentionReason.NO_INDEXABLE_SIGNALS),
        (
            "topology",
            [GraphNode("algebra", NodeKind.CLAIM, "finite group")],
            0.15,
            AbstentionReason.NO_CANDIDATE_MATCH,
        ),
        (
            "group",
            [GraphNode("group", NodeKind.CLAIM, "finite group")],
            100.0,
            AbstentionReason.BELOW_SUPPORT_THRESHOLD,
        ),
    ],
)
def test_retrieval_abstains_with_an_explicit_reason(
    query: str,
    nodes: list[GraphNode],
    threshold: float,
    reason: AbstentionReason,
) -> None:
    result = retrieve(query, nodes=nodes, edges=[], min_support_score=threshold)
    assert result.abstained
    assert result.reason is reason


def test_retrieval_abstains_when_the_top_match_is_ambiguous() -> None:
    nodes = [
        GraphNode("a", NodeKind.CLAIM, "finite group"),
        GraphNode("b", NodeKind.CLAIM, "finite group"),
    ]
    result = retrieve("group", nodes=nodes, edges=[], min_margin=0.01)
    assert result.abstained
    assert result.reason is AbstentionReason.AMBIGUOUS_TOP_MATCH


def test_near_tied_top_hits_that_are_directly_linked_do_not_abstain() -> None:
    nodes = [
        GraphNode("theorem", NodeKind.CLAIM, "finite group"),
        GraphNode("conjecture", NodeKind.CLAIM, "finite group"),
    ]
    linked = GraphEdge(
        "theorem", "conjecture", EdgeKind.CITES, "the theorem cites the conjecture"
    )
    result = retrieve("group", nodes=nodes, edges=[linked], min_margin=0.01)
    assert not result.abstained
    assert {hit.node.id for hit in result.hits[:2]} == {"theorem", "conjecture"}


def test_evaluation_guard_fails_closed_against_test_and_answer_leakage() -> None:
    safe = GraphNode(
        "safe",
        NodeKind.CLAIM,
        "Cauchy completeness reference",
        metadata={"split": "reference", "item_id": "reference-1"},
    )
    answer = GraphNode(
        "answer",
        NodeKind.EVIDENCE,
        "Cauchy completeness exact answer",
        metadata={"split": "test", "content_role": "answer_key", "item_id": "test-7"},
    )
    active_copy = GraphNode(
        "active-copy",
        NodeKind.CLAIM,
        "Cauchy completeness exact item",
        metadata={"split": "train", "item_id": "test-7"},
    )
    unlabeled = GraphNode("unlabeled", NodeKind.CLAIM, "Cauchy completeness solution")
    quarantined = GraphNode(
        "quarantined",
        NodeKind.CLAIM,
        "Cauchy completeness draft",
        metadata={"split": "train", "quarantined": "TRUE"},
    )
    malformed = GraphNode(
        "malformed",
        NodeKind.CLAIM,
        "Cauchy completeness candidate",
        metadata={"split": "train", "content_role": ["reference"]},
    )
    guard = RetrievalGuard(evaluation_split="test", active_item_id="test-7")
    result = retrieve(
        "Cauchy completeness",
        nodes=[answer, active_copy, unlabeled, quarantined, malformed, safe],
        edges=[GraphEdge("safe", "answer", EdgeKind.ANALOGOUS_TO, "possible analogy")],
        guard=guard,
    )
    assert [hit.node.id for hit in result.hits] == ["safe"]
    reasons = {item.node_id: item.reason for item in result.exclusions}
    assert reasons["answer"].startswith("blocked_content_role")
    assert reasons["active-copy"] == "active_item_leakage"
    assert reasons["unlabeled"] == "missing_split_label"
    assert reasons["quarantined"] == "quarantined_record"
    assert reasons["malformed"] == "malformed_content_role"


def test_guard_configuration_cannot_allow_the_active_split_or_answer_roles() -> None:
    with pytest.raises(ValueError, match="active evaluation split"):
        RetrievalGuard(
            evaluation_split="test",
            allowed_index_splits=("train", "test"),
        )
    with pytest.raises(ValueError, match="blocked roles must include"):
        RetrievalGuard(
            evaluation_split="test",
            blocked_roles=("answer_key",),
        )
    with pytest.raises(ValueError, match="allowed index splits"):
        RetrievalGuard(
            evaluation_split="test",
            allowed_index_splits=("train", 7),  # type: ignore[arg-type]
        )


def test_retrieval_rejects_nonfinite_abstention_thresholds() -> None:
    node = GraphNode("claim", NodeKind.CLAIM, "group")
    with pytest.raises(ValueError, match="thresholds"):
        retrieve("group", nodes=[node], edges=[], min_support_score=float("nan"))


def test_search_is_deterministic_including_scores_and_traces() -> None:
    nodes = [
        GraphNode("a", NodeKind.CLAIM, "finite group action"),
        GraphNode("b", NodeKind.CLAIM, "group representation"),
    ]
    edge = GraphEdge("a", "b", EdgeKind.ANALOGOUS_TO, "shared representation", id="e")
    first = search("group", nodes=nodes, edges=[edge])
    second = search("group", nodes=reversed(nodes), edges=reversed([edge]))
    observed_first = [
        (hit.node.id, hit.total_score, hit.trace)
        for hit in first
    ]
    observed_second = [
        (hit.node.id, hit.total_score, hit.trace)
        for hit in second
    ]
    assert observed_first == observed_second


def test_proof_mode_uses_exact_directed_edges_and_excludes_diffuse_relations() -> None:
    nodes = [
        GraphNode("root", NodeKind.CLAIM, "target theorem"),
        GraphNode("dependency", NodeKind.CLAIM, "support lemma"),
        GraphNode("analogy", NodeKind.CLAIM, "distant analogy"),
        GraphNode("external", NodeKind.EXTERNAL_REFERENCE, "main brain proxy"),
    ]
    edges = [
        GraphEdge("root", "dependency", EdgeKind.DEPENDS_ON, "exact proof dependency"),
        GraphEdge("root", "analogy", EdgeKind.ANALOGOUS_TO, "discovery-only similarity"),
        GraphEdge("root", "external", EdgeKind.BRIDGES_TO, "cross-brain discovery bridge"),
    ]

    proof = retrieve(
        "target theorem",
        nodes=nodes,
        edges=edges,
        graph_depth=1,
        min_support_score=0,
        mode=RetrievalMode.PROOF,
    )
    discovery = retrieve(
        "target theorem",
        nodes=nodes,
        edges=edges,
        graph_depth=1,
        min_support_score=0,
        mode=RetrievalMode.DISCOVERY,
    )

    assert {hit.node.id for hit in proof.hits} == {"root", "dependency"}
    assert {hit.node.id for hit in discovery.hits} == {
        "root",
        "dependency",
        "analogy",
        "external",
    }

    reverse = retrieve(
        "support lemma",
        nodes=nodes,
        edges=edges,
        graph_depth=1,
        min_support_score=0,
        mode=RetrievalMode.PROOF,
    )
    assert "root" not in {hit.node.id for hit in reverse.hits}


def test_exact_dependency_closure_is_dependency_first_and_ignores_semantics() -> None:
    nodes = [
        GraphNode("root", NodeKind.CLAIM, "root"),
        GraphNode("a", NodeKind.CLAIM, "a"),
        GraphNode("b", NodeKind.CLAIM, "b"),
        GraphNode("semantic", NodeKind.CLAIM, "semantic"),
    ]
    edges = [
        GraphEdge("root", "b", EdgeKind.DEPENDS_ON, "root needs b", id="e2"),
        GraphEdge("root", "a", EdgeKind.DEPENDS_ON, "root needs a", id="e1"),
        GraphEdge("b", "a", EdgeKind.DEPENDS_ON, "b needs a", id="e3"),
        GraphEdge(
            "root",
            "semantic",
            EdgeKind.SEMANTIC_ASSOCIATION,
            "discovery signal only",
            id="e4",
        ),
    ]

    closure = exact_dependency_closure("root", nodes=nodes, edges=edges)

    assert closure.ordered_node_ids == ("a", "b", "root")
    assert closure.edge_ids == ("e1", "e3", "e2")


def test_exact_dependency_closure_fails_closed_on_cycles_and_missing_nodes() -> None:
    root = GraphNode("root", NodeKind.CLAIM, "root")
    dependency = GraphNode("dependency", NodeKind.CLAIM, "dependency")
    cycle = [
        GraphEdge("root", "dependency", EdgeKind.DEPENDS_ON, "forward"),
        GraphEdge("dependency", "root", EdgeKind.DEPENDS_ON, "backward"),
    ]
    with pytest.raises(ValueError, match="dependency cycle"):
        exact_dependency_closure("root", nodes=[root, dependency], edges=cycle)

    missing = GraphEdge("root", "missing", EdgeKind.DEPENDS_ON, "missing target")
    with pytest.raises(ValueError, match="missing dependency node"):
        exact_dependency_closure("root", nodes=[root], edges=[missing])


def test_retrieval_defaults_to_current_immutable_revisions() -> None:
    prior = GraphNode("prior", NodeKind.CLAIM, "finite group classification")
    current = GraphNode("current", NodeKind.CLAIM, "finite group classification corrected")
    supersedes = GraphEdge(
        "current",
        "prior",
        EdgeKind.SUPERSEDES,
        "corrected scope supersedes the prior immutable revision",
    )

    default = retrieve(
        "finite group classification",
        nodes=[prior, current],
        edges=[supersedes],
        min_support_score=0,
    )
    historical = retrieve(
        "finite group classification",
        nodes=[prior, current],
        edges=[supersedes],
        min_support_score=0,
        current_only=False,
    )

    assert [hit.node.id for hit in default.hits] == ["current"]
    assert ("prior", "superseded_revision") in {
        (item.node_id, item.reason) for item in default.exclusions
    }
    assert {hit.node.id for hit in historical.hits} == {"prior", "current"}


def test_positional_variable_slots_are_not_symbol_vocabulary() -> None:
    # $m + n$ and $p - q$ share only alpha-renamed slots v0, v1 - word order,
    # not vocabulary. The symbol channel must not score that overlap.
    node = GraphNode("sums", NodeKind.CLAIM, "A sum identity", "$m + n$ appears here.")
    hits = search("$p - q$", nodes=[node], edges=[])
    assert all(hit.symbol_score == 0 for hit in hits)


def test_named_functions_still_carry_symbol_signal_after_slot_filtering() -> None:
    node = GraphNode("sine", NodeKind.CLAIM, "A sine root", r"$\sin(y) = 0$ on the axis.")
    hits = search(r"$\sin(x)$", nodes=[node], edges=[])
    assert hits and hits[0].node.id == "sine"
    assert hits[0].symbol_score > 0


def test_stopword_overlap_earns_no_lexical_credit() -> None:
    filler = GraphNode(
        "filler",
        NodeKind.CLAIM,
        "Connective filler",
        "the of a an and or to in on for is are was were it this that",
    )
    content = GraphNode(
        "content",
        NodeKind.CLAIM,
        "Martingale convergence",
        "Almost sure convergence of martingales under an L1 bound.",
    )
    hits = search(
        "the convergence of the martingales in the limit",
        nodes=[filler, content],
        edges=[],
    )
    assert hits and hits[0].node.id == "content"
    filler_hits = [hit for hit in hits if hit.node.id == "filler"]
    assert all(hit.lexical_score == 0 for hit in filler_hits)


def test_directly_matched_claims_outrank_their_shared_neighbour() -> None:
    # Two seeds each match half the query; their common neighbour matches none of
    # it. Under spread-without-retention the neighbour collected decay from both
    # seeds and overtook each of them. The seeds must stay on top.
    seed_a = GraphNode("seed-a", NodeKind.CLAIM, "Rademacher tail bound")
    seed_b = GraphNode("seed-b", NodeKind.CLAIM, "Skorokhod embedding step")
    hub = GraphNode("hub", NodeKind.CLAIM, "An unrelated bookkeeping row")
    edges = [
        GraphEdge("seed-a", "hub", EdgeKind.DEPENDS_ON, "a cites the row", id="ea"),
        GraphEdge("seed-b", "hub", EdgeKind.DEPENDS_ON, "b cites the row", id="eb"),
    ]
    hits = search(
        "rademacher tail bound skorokhod embedding step",
        nodes=[seed_a, seed_b, hub],
        edges=edges,
    )
    assert hits[0].node.id in {"seed-a", "seed-b"}
    hub_hit = next(hit for hit in hits if hit.node.id == "hub")
    assert hub_hit.total_score < hits[0].total_score


def test_graph_channel_scale_does_not_grow_with_seed_count() -> None:
    # Three seeds saying the same thing must not hand their neighbour three times
    # the graph mass one seed would: the channel is an average over seeds, not a
    # sum, so it measures connectedness rather than prompt length.
    def build(k: int) -> float:
        seeds = [
            GraphNode(f"seed-{i}", NodeKind.CLAIM, "Spectral gap estimate")
            for i in range(k)
        ]
        target = GraphNode("target", NodeKind.CLAIM, "Mixing time corollary")
        edges = [
            GraphEdge(seed.id, "target", EdgeKind.DEPENDS_ON, "uses", id=f"e{seed.id}")
            for seed in seeds
        ]
        hits = search("spectral gap estimate", nodes=[*seeds, target], edges=edges)
        return next(hit.graph_score for hit in hits if hit.node.id == "target")

    assert build(3) == pytest.approx(build(1))


def test_a_claim_with_no_statement_cannot_take_a_slot_from_one_that_says_something() -> None:
    hollow = GraphNode("hollow", NodeKind.CLAIM, "Borel Cantelli lemma survey note", "")
    stated = GraphNode(
        "stated",
        NodeKind.CLAIM,
        "Borel Cantelli lemma",
        "If the measures sum finitely then the limsup event has measure zero.",
    )
    hits = search("borel cantelli lemma", nodes=[hollow, stated], edges=[])
    assert hits[0].node.id == "stated"
    assert [hit.node.id for hit in hits][:2] == ["stated", "hollow"]
