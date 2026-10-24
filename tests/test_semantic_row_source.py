"""The semantic loader reads how each claim vector was made (row_source) and refuses a file whose sources are not the
closed set (scheduled audits account04/B06 r76 and account04/B14 r8,
B06-R76-LEGACY-DIGEST-MIGRATION-OPENS-UNVERIFIED-ROWS-20260929).

A legacy row carries its claim's current store digest, but no text of the claim reproduces it; a caller can tell it from
a row made from its text only if the loader hands the sources on.

    python -m pytest tests/test_semantic_row_source.py
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import os
import sys

import numpy as np
import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

IDS = np.array(["claim_A", "claim_B", "claim_C"])
VECS = np.array([[1.0, 0.0], [0.0, 1.0], [0.6, 0.8]], dtype=np.float32)
DIGESTS = np.array(["sha256:a", "sha256:b", "sha256:c"])


def load_module(name):
    path = os.environ.get("SEMANTIC_UNDER_TEST") or os.path.join(SRC, "math_brain", "semantic.py")
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


def artifact(tmp_path, **fields):
    path = str(tmp_path / "claim_embeddings.npz")
    np.savez(path, vecs=VECS, slugs=IDS, model=np.array("BAAI/bge-small-en-v1.5"), **fields)
    return path


def test_row_sources_are_read(tmp_path) -> None:
    m = load_module("semantic_rs_read")
    m.ARTIFACT = artifact(tmp_path, node_digests=DIGESTS, row_source=np.array(["body", "legacy", "title body"]))
    m._load_artifact()
    assert [str(s) for s in m._sources] == ["body", "legacy", "title body"]
    assert m._status[0] == "READY"


def test_a_file_without_sources_loads_with_none(tmp_path) -> None:
    m = load_module("semantic_rs_none")
    m.ARTIFACT = artifact(tmp_path, node_digests=DIGESTS)
    m._load_artifact()
    assert m._sources is None


@pytest.mark.parametrize(
    "sources",
    [np.array(["body", "verified", "body"]), np.array(["body", "legacy"]), np.array([1, 2, 3])],
    ids=["value outside the set", "count that is not the file's", "not strings"],
)
def test_sources_outside_the_closed_set_are_refused(tmp_path, sources) -> None:
    m = load_module("semantic_rs_bad")
    m.ARTIFACT = artifact(tmp_path, node_digests=DIGESTS, row_source=sources)
    with pytest.raises(RuntimeError, match="row sources"):
        m._load_artifact()
    assert m._sources is None and m._vecs is None
    assert m._status[0] == "INVALID_ARTIFACT"
