from unittest.mock import patch

import pytest

from math_brain import retrieval as r
from math_brain.models import GraphNode, NodeKind


CONTENT = ("op:sum", "op:eq", "num:1", "num:2", "num:3")


@pytest.mark.parametrize("words,layout_count,expected", [
    (("alpha", "beta", "gamma"), 0, False),
    (("alpha", "beta", "gamma"), 1, True),
    (("alpha", "beta", "gamma", "delta"), 2, False),
    (("alpha", "beta", "gamma", "delta"), 3, True),
])
def test_notation_density_boundary(words, layout_count, expected):
    signals = r.IndexSignals(words, CONTENT + ("punct:(",) * layout_count, ())
    assert r._notation_idf_mode(signals) is expected


@pytest.mark.parametrize("symbols,expected", [
    (CONTENT[:4] * 3, False),
    (CONTENT + ("punct:(",), True),
    (("op:eq",) * 12, False),
])
def test_notation_requires_distinct_content_symbols(symbols, expected):
    signals = r.IndexSignals(("alpha", "beta", "gamma"), symbols, ())
    assert r._notation_idf_mode(signals) is expected


def test_variable_slots_do_not_inflate_notation_density():
    words = ("alpha", "beta", "gamma")
    plain = r.IndexSignals(words, CONTENT, ())
    padded = r.IndexSignals(words, CONTENT + tuple(f"v{i}" for i in range(30)), ())
    assert r._notation_idf_mode(plain) is False
    assert r._notation_idf_mode(padded) is False


def test_stopwords_do_not_suppress_notation():
    plain = r.IndexSignals((), CONTENT, ())
    padded = r.IndexSignals(("the", "is") * 20, CONTENT, ())
    assert r._notation_idf_mode(plain) is True
    assert r._notation_idf_mode(padded) is True


@pytest.mark.parametrize("prefix,expected", [
    ("", True),
    ("context explanation background narrative argument discussion detail summary ", False),
])
def test_retrieve_routes_actual_notation_and_prose(prefix, expected):
    # Exercise the real indexer and router; wrap only scoring to observe the mode.
    formula = r"$x_{1}+x_{2}=3$"
    query = prefix + formula
    assert r._notation_idf_mode(r.index_signals(query)) is expected
    node = GraphNode("formula", NodeKind.CLAIM, "Formula fixture", formula)
    with patch.object(r, "_channel_scores", wraps=r._channel_scores) as scoring:
        r.retrieve(query, nodes=[node], edges=[])
    calls = [call for call in scoring.call_args_list if call.kwargs["channel"] is r.ScoreChannel.SYMBOL]
    assert len(calls) == 1
    assert calls[0].kwargs["notation_mode"] is expected
