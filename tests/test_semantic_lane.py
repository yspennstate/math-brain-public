"""The semantic channel refuses a damaged vector file and says why a call returned nothing.

Interactive audits IA-20260929-MB-03 and MB-02 / 052554-03 (29 Sep 2026): one NaN coordinate in the
claim vectors loaded without complaint, available() said the channel was healthy, and every question
then got an empty result that looked like "no claim is close". And the standout score is relative:
some claim stands out for any question, so the raw cosine now travels beside it.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path

import numpy as np
import pytest

from math_brain import semantic
from math_brain.models import GraphNode, NodeKind
from math_brain.retrieval import ScoreChannel, retrieve

IDS = np.array(["claim_a", "claim_b", "claim_c"])
GOOD = np.array([[1.0, 0.1, 0.0], [0.2, 1.0, 0.0], [0.0, 0.3, 1.0]], dtype=np.float32)
QUESTION = np.array([1.0, 0.0, 0.0], dtype=np.float32)


class _Encoder:
    def __init__(self, vector=QUESTION, fail=False):
        self.vector, self.fail = vector, fail

    def embed(self, text):
        if self.fail:
            raise RuntimeError("encoder not available")
        return self.vector


@pytest.fixture
def lane(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    art = tmp_path / "claim_embeddings.npz"
    monkeypatch.setenv("MATH_BRAIN_SEMANTIC", "1")
    monkeypatch.setattr(semantic, "ARTIFACT", str(art))
    monkeypatch.setattr(semantic, "_vecs", None)
    monkeypatch.setattr(semantic, "_ids", None)
    monkeypatch.setattr(semantic, "_gen", None)
    monkeypatch.setattr(semantic, "_digests", None, raising=False)
    monkeypatch.setattr(semantic, "_status", ("NOT_LOADED", ""))
    monkeypatch.setattr(semantic, "_query_encoder", lambda: _Encoder())

    def write(vecs, ids=IDS, model="bge-small-en-v1.5"):
        np.savez(str(art), vecs=vecs, slugs=ids, model=np.array(model))
        return art

    return write


def _with(vecs: np.ndarray, row: int, col: int, value: float) -> np.ndarray:
    out = vecs.copy()
    out[row, col] = value
    return out


@pytest.mark.parametrize(
    "name, vecs, ids, needle",
    [
        ("a NaN coordinate", _with(GOOD, 1, 2, np.nan), IDS, "NaN or infinite"),
        ("an infinite coordinate", _with(GOOD, 0, 0, np.inf), IDS, "NaN or infinite"),
        ("a repeated identifier", GOOD, np.array(["claim_a", "claim_a", "claim_c"]), "not unique"),
        # account04/B06 r75: one row per id, and the ids a flat list
        ("a two-dimensional identifier array", GOOD, IDS.reshape(-1, 1), "1-D"),
        ("a one-dimensional array", GOOD[:, 0].copy(), IDS, "2-D"),
    ],
)
def test_a_damaged_file_is_not_reported_healthy(lane, name, vecs, ids, needle) -> None:
    lane(vecs, ids)
    assert semantic.available() is False, name
    state, detail = semantic.lane_status()
    assert state == "INVALID_ARTIFACT" and needle in detail, (name, detail)


class _Marker:
    """Unpickling this creates an empty file: a harmless stand-in for code run at load time."""

    def __init__(self, path: str) -> None:
        self.path = path

    def __reduce__(self):
        return (open, (self.path, "w"))


def test_a_pickled_identifier_array_is_refused_without_running(lane, tmp_path: Path) -> None:
    # account04/B17 r14, B17-R24-SEMANTIC-NPZ-ALLOW-PICKLE-CODE-EXEC-20260929
    marker = tmp_path / "unpickled.marker"
    ids = np.empty(3, dtype=object)
    for i in range(3):
        ids[i] = _Marker(str(marker))
    lane(GOOD, ids)
    assert semantic.available() is False
    assert not marker.exists()
    assert semantic.lane_status()[0] == "INVALID_ARTIFACT"


def test_numeric_identifiers_are_refused(lane) -> None:
    lane(GOOD, np.array([1, 2, 3]))
    assert semantic.available() is False
    assert "string array" in semantic.lane_status()[1]


def test_a_repaired_file_is_ready_again(lane) -> None:
    lane(_with(GOOD, 1, 2, np.nan))
    assert semantic.available() is False
    lane(GOOD)  # a failed load keeps nothing, so the next call reads the file again
    assert semantic.available() is True
    assert semantic.lane_status()[0] == "READY"


def _top() -> str:
    return str(semantic._ids[int(np.argmax(semantic._vecs @ QUESTION))])


def test_the_generation_names_the_bytes_that_were_read(lane, monkeypatch: pytest.MonkeyPatch,
                                                      tmp_path: Path) -> None:
    # account04/B11 r4, B11-R31-SEMANTIC-LOAD-TOCTOU-20260929-01: the file is replaced between the
    # generation check and the read. The loader now reads the file once, hashes those bytes and parses the
    # same bytes, so the vectors it keeps are always the ones its generation names; the next call reads the
    # replacement.
    art = Path(lane(GOOD))                                     # A: claim_a wins
    a_bytes = art.read_bytes()
    other = tmp_path / "other.npz"
    np.savez(str(other), vecs=np.array([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]],
                                       dtype=np.float32),
             slugs=IDS, model=np.array("bge-small-en-v1.5"))    # B: claim_c wins
    real = semantic.np.load
    fired: list[int] = []

    def replace_before_the_parse(*args, **kwargs):
        if not fired:
            fired.append(1)
            os.replace(other, art)
        return real(*args, **kwargs)

    monkeypatch.setattr(semantic.np, "load", replace_before_the_parse)
    semantic._load_artifact()
    monkeypatch.setattr(semantic.np, "load", real)
    assert fired and _top() == "claim_a"                       # A's bytes were parsed
    assert semantic.artifact_identity()["sha256"] == hashlib.sha256(a_bytes).hexdigest()
    semantic._load_artifact()                                  # B is on disk now
    assert _top() == "claim_c"
    assert semantic.artifact_identity()["sha256"] == hashlib.sha256(art.read_bytes()).hexdigest()


def test_the_identity_names_the_file_and_its_manifest(lane) -> None:
    assert semantic.artifact_identity() == {}
    art = Path(lane(GOOD))
    semantic._load_artifact()
    digest = hashlib.sha256(art.read_bytes()).hexdigest()
    assert semantic.artifact_identity() == {"sha256": digest, "manifest": "absent"}
    assert digest[:12] in semantic.lane_status()[1]
    Path(str(art) + ".sha256").write_text(digest + "  claim_embeddings.npz\n")
    semantic._load_artifact()
    assert semantic.artifact_identity() == {"sha256": digest, "manifest": "match"}


def test_no_file_and_off_are_their_own_states(lane, monkeypatch: pytest.MonkeyPatch) -> None:
    assert semantic.available() is False
    assert semantic.lane_status()[0] == "NO_ARTIFACT"
    monkeypatch.setenv("MATH_BRAIN_SEMANTIC", "0")
    assert semantic.lane_status()[0] == "DISABLED"


def test_scores_carry_their_raw_cosine(lane) -> None:
    lane(GOOD)
    details = semantic.standout_details("q", None)
    unit = GOOD / np.linalg.norm(GOOD, axis=1, keepdims=True)
    cosines = unit @ QUESTION
    assert set(details) == {"claim_a"}  # only one claim is above the mean for this question
    score, cosine = details["claim_a"]
    assert cosine == pytest.approx(float(cosines[0]), abs=1e-6)
    assert score == pytest.approx(float((cosines[0] - cosines.mean()) / cosines.std()), abs=1e-5)
    assert semantic.standout_scores("q", None) == {"claim_a": score}
    assert semantic.lane_status()[0] == "READY"


def test_a_weak_best_claim_still_stands_out_which_is_why_the_cosine_is_shown(lane) -> None:
    # Cosines 0.01, 0.00, -0.01: nothing is close, and the best claim still gets a positive score.
    near_orthogonal = np.array([[0.01, 1.0, 0.0], [0.0, 1.0, 0.0], [-0.01, 1.0, 0.0]],
                               dtype=np.float32)
    lane(near_orthogonal)
    details = semantic.standout_details("q", None)
    score, cosine = details["claim_a"]
    assert score > 1.0 and abs(cosine) < 0.02


def test_why_a_call_returned_nothing(lane, monkeypatch: pytest.MonkeyPatch) -> None:
    lane(GOOD)
    monkeypatch.setattr(semantic, "_query_encoder", lambda: _Encoder(fail=True))
    assert semantic.standout_scores("q", None) == {}
    assert semantic.lane_status()[0] == "ENCODER_FAILURE"
    monkeypatch.setattr(semantic, "_query_encoder",
                        lambda: _Encoder(vector=np.array([1.0, 0.0], dtype=np.float32)))
    assert semantic.standout_scores("q", None) == {}
    assert semantic.lane_status()[0] == "ENCODER_FAILURE"
    monkeypatch.setattr(semantic, "_query_encoder", lambda: _Encoder())
    assert semantic.standout_scores("q", ["claim_b"]) == {}
    assert semantic.lane_status()[0] == "NO_MATCH"


def test_identical_claims_have_no_spread(lane) -> None:
    lane(np.array([[1.0, 0.0, 0.0]] * 3, dtype=np.float32))
    assert semantic.standout_scores("q", None) == {}
    assert semantic.lane_status()[0] == "NO_SPREAD"


def _nodes() -> list[GraphNode]:
    body = "A finite group of prime order is cyclic, generated by any element but the identity."
    return [GraphNode(i, NodeKind.CLAIM, "finite group " + i, body) for i in IDS.tolist()]


def test_retrieval_keeps_its_lexical_answer_when_the_file_is_damaged(lane) -> None:
    lane(_with(GOOD, 1, 2, np.nan))
    result = retrieve("finite group", nodes=_nodes(), edges=[], limit=3)
    assert len(result.hits) == 3
    assert all(h.semantic_score == 0.0 for h in result.hits)
    assert semantic.lane_status()[0] == "INVALID_ARTIFACT"


def test_retrieval_trace_shows_the_cosine(lane) -> None:
    lane(GOOD)
    result = retrieve("finite group", nodes=_nodes(), edges=[], limit=3)
    traces = [t for h in result.hits for t in h.trace if t.channel is ScoreChannel.SEMANTIC]
    assert traces and all("cosine" in t.detail for t in traces)


# One store digest per row, when the file records them (account03/B12 r56,
# B12-R56-ID-ONLY-COVERAGE-CERTIFIES-UNBOUND-VECTOR-TEXT-20260929): read with the vectors, from the
# same bytes, so a caller can check each vector against the text its claim holds now.
def test_recorded_digests_are_read_with_the_vectors(lane, tmp_path: Path) -> None:
    art = tmp_path / "claim_embeddings.npz"
    digests = np.array(["d-a", "d-b", "d-c"])
    np.savez(str(art), vecs=GOOD, slugs=IDS, model=np.array("bge-small-en-v1.5"),
             node_digests=digests)
    semantic._load_artifact()
    assert semantic.lane_status()[0] == "READY"
    assert list(semantic._digests) == ["d-a", "d-b", "d-c"]


def test_a_file_without_digests_loads_with_none(lane) -> None:
    lane(GOOD)
    semantic._load_artifact()
    assert semantic.lane_status()[0] == "READY" and semantic._digests is None


@pytest.mark.parametrize("digests", [np.array(["d-a", "d-b"]), np.array([1, 2, 3])])
def test_digests_of_the_wrong_count_or_kind_are_refused(lane, tmp_path: Path, digests) -> None:
    art = tmp_path / "claim_embeddings.npz"
    np.savez(str(art), vecs=GOOD, slugs=IDS, model=np.array("bge-small-en-v1.5"),
             node_digests=digests)
    with pytest.raises(RuntimeError):
        semantic._load_artifact()
    assert semantic.lane_status()[0] == "INVALID_ARTIFACT" and semantic._digests is None
