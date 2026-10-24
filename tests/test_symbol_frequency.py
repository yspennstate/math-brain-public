import math
from unittest.mock import patch

import pytest

from math_brain import retrieval as r
from math_brain.models import GraphNode, NodeKind
from math_brain.retrieval import (
    ScoreChannel,
    _channel_scores,
    _symbol_terms,
    index_signals,
)


def test_symbol_variable_slots_are_not_evidence_but_layout_is_retained():
    # Layout is retained for prose compatibility and notation routing. The
    # notation scoring mode removes it on both sides of the symbol channel.
    assert _symbol_terms(("v0", "v12", "punct:(", "punct:}", "op:subscript",
                          "op:eq", "op:sum", "num:2", "func:det")) == (
        "punct:(", "punct:}", "op:subscript", "op:eq", "op:sum", "num:2", "func:det",
    )


def test_frequent_notation_is_small_but_distinctive_notation_scores():
    documents = {str(i): ("op:eq", "op:in", "op:le", "op:sum") for i in range(10)}
    documents["0"] += ("func:det", "num:17")
    scores, traces = _channel_scores(
        ("op:eq", "op:in", "op:le", "op:sum", "func:det", "num:17"),
        documents, channel=ScoreChannel.SYMBOL, weight=1.35, notation_mode=True,
    )
    assert scores["0"] > 0
    assert all(0 < scores[str(i)] < scores["0"] / 10 for i in range(1, 10))
    assert sum(t.amount for t in traces["0"]) == pytest.approx(scores["0"])
    assert all(math.isfinite(t.amount) and t.amount >= 0 for ts in traces.values() for t in ts)


def test_prose_symbol_channel_keeps_existing_idf():
    documents = {str(i): ("op:eq",) for i in range(10)}
    scores, _ = _channel_scores(("op:eq",), documents, channel=ScoreChannel.SYMBOL, weight=1.0)
    expected = math.log1p(10 / 11) * (1 + math.log1p(1))
    assert all(score == pytest.approx(expected) for score in scores.values())


@pytest.mark.parametrize("notation_mode", [False, True])
def test_layout_scoring_depends_on_notation_mode(notation_mode):
    layout = ("punct:(", "punct:}", "op:subscript")
    documents = {"clean": ("num:2",), "layout": ("num:2",) + layout}
    scores, traces = _channel_scores(
        _symbol_terms(layout), documents, channel=ScoreChannel.SYMBOL,
        weight=1.0, notation_mode=notation_mode,
    )
    if notation_mode:
        assert (scores, traces) == ({}, {})
        # Adding layout must change neither content evidence nor its divisor.
        content, _ = _channel_scores(("num:2",), documents, channel=ScoreChannel.SYMBOL,
                                     weight=1.0, notation_mode=True)
        assert content["clean"] == pytest.approx(content["layout"])
    else:
        assert scores["layout"] > 0
        assert "clean" not in scores


@pytest.mark.parametrize("notation_mode", [False, True])
def test_symbol_idf_is_monotone_in_document_frequency(notation_mode):
    docs = {str(i): tuple(["num:2"] + (["op:le"] if i < 5 else [])
                         + (["func:det"] if i == 0 else [])) for i in range(10)}
    _, traces = _channel_scores(("num:2", "op:le", "func:det"), docs,
                               channel=ScoreChannel.SYMBOL, weight=1.0,
                               notation_mode=notation_mode)
    amounts = {t.detail: t.amount for t in traces["0"]}
    assert amounts["matched normalized term 'func:det'"] > amounts["matched normalized term 'op:le'"] > amounts["matched normalized term 'num:2'"]


@pytest.mark.parametrize("notation_mode", [False, True])
def test_single_document_and_empty_symbol_channels_are_finite(notation_mode):
    scores, traces = _channel_scores(("num:2",), {"one": ("num:2",)},
                                    channel=ScoreChannel.SYMBOL, weight=1.0,
                                    notation_mode=notation_mode)
    assert 0 < scores["one"] < 1
    assert traces["one"][0].amount == scores["one"]
    assert _channel_scores((), {}, channel=ScoreChannel.SYMBOL, weight=1.0,
                           notation_mode=notation_mode) == ({}, {})


@pytest.mark.parametrize("notation_mode", [False, True])
@pytest.mark.parametrize("channel", [ScoreChannel.LEXICAL, ScoreChannel.FORMULA])
def test_other_channels_keep_existing_idf(channel, notation_mode):
    scores, _ = _channel_scores(("test",), {"one": ("test",)}, channel=channel,
                               weight=1.0, notation_mode=notation_mode)
    assert scores["one"] == pytest.approx(math.log1p(1 / 2) * (1 + math.log1p(1)))


def test_layout_still_distinguishes_exact_formula_fingerprints():
    a = index_signals(r"$x_{1}+x_{2}=3$")
    b = index_signals(r"$x^{1}+x^{2}=3$")
    assert a.formula_fingerprints != b.formula_fingerprints
    assert "op:subscript" in a.math_tokens
    assert "op:subscript" in _symbol_terms(a.math_tokens)


@pytest.mark.parametrize("notation_mode", [False, True])
def test_retrieve_passes_notation_route_to_symbol_channel(notation_mode):
    node = GraphNode("formula", NodeKind.CLAIM, "Formula fixture", r"$x_{1}+x_{2}=3$")
    with patch.object(r, "_notation_idf_mode", return_value=notation_mode), \
         patch.object(r, "_channel_scores", wraps=r._channel_scores) as scoring:
        r.retrieve(node.body, nodes=[node], edges=[])
    calls = [call for call in scoring.call_args_list if call.kwargs["channel"] is ScoreChannel.SYMBOL]
    assert len(calls) == 1
    assert calls[0].kwargs["notation_mode"] is notation_mode
