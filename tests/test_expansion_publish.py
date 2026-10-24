"""The expansion sidecar and the prompt counts behind it (interactive audit, 30 Sep 2026).

B100-05: an owner record whose text was not a string reached str.strip and the whole count raised, which dropped the
expansion from the index build. A record that cannot be read is now refused and counted, and the valid records around
it are counted as before.

B100-04: every build staged the sidecar through the one name path + ".tmp", so two builds could publish each other's
bytes and the second then failed on a missing file. Builds now run one at a time under a lock file, stage under a
private name, and a build from an older store state does not replace a sidecar built from a newer one.
"""

import json
import os
import pickle
import sqlite3
import time
from pathlib import Path

import pytest

from math_brain import expansion
from math_brain.models import GraphNode, NodeKind


@pytest.fixture()
def split_terms(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(expansion, "_terms", lambda text: (text or "").split())
    monkeypatch.setattr(expansion, "_tokenizer_identity", lambda: "tokenizer-a", raising=False)


def _lines(path: Path, lines: list[str]) -> None:
    path.write_text("".join(line + "\n" for line in lines), encoding="utf-8")


def test_unreadable_prompt_records_are_refused_by_reason_and_the_rest_counted(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    good = json.dumps({"origin": "owner", "text": "alpha beta gamma delta"})
    source = tmp_path / "prompts.jsonl"
    _lines(
        source,
        [
            good,
            "{not json",
            json.dumps(["an", "array"]),
            json.dumps({"origin": "owner"}),
            json.dumps({"origin": "owner", "text": None}),
            json.dumps({"origin": "owner", "text": ["a", "list"]}),
            json.dumps({"origin": "owner", "text": 42}),
            json.dumps({"origin": "owner", "text": True}),
            json.dumps({"origin": "owner", "text": {"a": "dict"}}),
            json.dumps({"origin": "owner", "text": "short"}),
            json.dumps({"origin": "assistant", "text": ["not", "his"]}),
            json.dumps({"origin": "owner", "text": "epsilon zeta eta theta"}),
        ],
    )
    monkeypatch.setattr(expansion, "PROMPTS", source)
    df, n, rejected = expansion._his_counts(tmp_path / "his.pkl")
    assert n == 2
    assert df["alpha"] == 1 and df["epsilon"] == 1
    assert rejected == {"not_json": 1, "not_an_object": 1, "no_text": 2, "text_not_a_string": 4}
    # the cache returns the same refusals, and the two-value reader still works
    assert expansion._his_counts(tmp_path / "his.pkl")[2] == rejected
    assert expansion._his_df(tmp_path / "his.pkl") == (df, n)


def test_a_strict_build_refuses_an_unreadable_record_even_from_the_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    source = tmp_path / "prompts.jsonl"
    _lines(source, [json.dumps({"origin": "owner", "text": "alpha beta gamma delta"}),
                    json.dumps({"origin": "owner", "text": ["a", "list"]})])
    monkeypatch.setattr(expansion, "PROMPTS", source)
    cache = tmp_path / "his.pkl"
    assert expansion._his_counts(cache)[2] == {"text_not_a_string": 1}  # ordinary build: counted around
    with pytest.raises(ValueError, match="strict build"):
        expansion._his_counts(cache, strict=True)  # the cached result is refused too


def test_an_unknown_tokenizer_identity_neither_reads_nor_writes_the_cache(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    source = tmp_path / "prompts.jsonl"
    _lines(source, [json.dumps({"origin": "owner", "text": "alpha beta gamma delta"})])
    monkeypatch.setattr(expansion, "PROMPTS", source)
    monkeypatch.setattr(expansion, "_tokenizer_identity", lambda: "unknown")
    cache = tmp_path / "his.pkl"
    assert expansion._his_counts(cache)[1] == 1
    assert not cache.exists()
    # a cache written under a known identity is not served to an environment whose tokenizer is unknown
    monkeypatch.setattr(expansion, "_tokenizer_identity", lambda: "tokenizer-a")
    expansion._his_counts(cache)
    assert cache.exists()
    monkeypatch.setattr(expansion, "_terms", lambda text: ["from-a-different-tokenizer"])
    monkeypatch.setattr(expansion, "_tokenizer_identity", lambda: "unknown")
    df, _n, _rej = expansion._his_counts(cache)
    assert set(df) == {"from-a-different-tokenizer"}


def test_publishing_twice_leaves_the_second_and_no_staging_file(tmp_path: Path) -> None:
    path = str(tmp_path / "store.sqlite3.expansion.pkl")
    assert expansion._publish(path, {"generation": "2026-09-30T00:00:00Z", "expansion": {"a": "first"}})
    assert expansion._publish(path, {"generation": "2026-09-30T00:00:00Z", "expansion": {"a": "second"}})
    with open(path, "rb") as fh:
        assert pickle.load(fh)["expansion"] == {"a": "second"}
    assert not [p for p in tmp_path.iterdir() if p.name.endswith(".tmp")]


def test_a_build_from_an_older_store_state_does_not_replace_a_newer_sidecar(tmp_path: Path) -> None:
    path = str(tmp_path / "store.sqlite3.expansion.pkl")
    assert expansion._publish(path, {"generation": "2026-09-30T02:00:00Z", "expansion": {"a": "newer"}})
    assert not expansion._publish(path, {"generation": "2026-09-30T01:00:00Z", "expansion": {"a": "older"}})
    with open(path, "rb") as fh:
        assert pickle.load(fh)["expansion"] == {"a": "newer"}


def test_an_interrupted_write_leaves_the_published_sidecar_and_no_staging_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    path = str(tmp_path / "store.sqlite3.expansion.pkl")
    expansion._publish(path, {"generation": "g1", "expansion": {"a": "kept"}})

    def broken_dump(*args, **kwargs):
        raise OSError("disk full")

    monkeypatch.setattr(expansion.pickle, "dump", broken_dump)
    with pytest.raises(OSError, match="disk full"):
        expansion._publish(path, {"generation": "g2", "expansion": {"a": "lost"}})
    monkeypatch.undo()
    with open(path, "rb") as fh:
        assert pickle.load(fh)["expansion"] == {"a": "kept"}
    assert not [p for p in tmp_path.iterdir() if p.name.endswith(".tmp")]


def _fixture_store(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    memory = tmp_path / "memory"
    memory.mkdir()
    (memory / "house_result.md").write_text(
        "---\nname: house_result\n---\nThe halfspace coefficient bound holds for every halfspace.\n", encoding="utf-8"
    )
    store = tmp_path / "brain.sqlite3"
    db = sqlite3.connect(store)
    db.execute("CREATE TABLE claim_provenance (claim_id TEXT, source_ref TEXT)")
    db.execute("INSERT INTO claim_provenance VALUES ('house', 'memory:house_result')")
    db.commit()
    db.close()
    nodes = [GraphNode("house", NodeKind.CLAIM, "FEI result", "The program's result.", created_at="2026-09-30T01:00:00Z")]
    nodes += [
        GraphNode("c%d" % k, NodeKind.CLAIM, "halfspace coefficient", "A card about a halfspace coefficient %d." % k,
                  created_at="2026-09-29T00:00:00Z")
        for k in range(3)
    ]
    monkeypatch.setattr(expansion, "MEMORY_DIR", memory)
    monkeypatch.setattr(expansion, "PROMPTS", tmp_path / "no_prompts.jsonl")
    monkeypatch.setattr(expansion, "MAX_DF_SHARE", 1.0)
    return store, nodes


def test_a_build_waits_for_a_live_lock_and_fails_visibly_after_the_wait(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    store, nodes = _fixture_store(tmp_path, monkeypatch)
    lock = Path(expansion.sidecar_path(store) + ".lock")
    lock.write_text("another builder", encoding="ascii")
    monkeypatch.setattr(expansion, "LOCK_WAIT_S", 0.5)
    started = time.monotonic()
    with pytest.raises(TimeoutError, match="another expansion build"):
        expansion.build(store, nodes)
    assert time.monotonic() - started >= 0.5
    assert lock.exists()  # a live holder's lock is not removed


def test_a_stale_lock_is_taken_over_and_the_build_publishes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    store, nodes = _fixture_store(tmp_path, monkeypatch)
    lock = Path(expansion.sidecar_path(store) + ".lock")
    lock.write_text("a builder that died", encoding="ascii")
    old = time.time() - 2 * expansion.LOCK_STALE_S
    os.utime(lock, (old, old))
    out = expansion.build(store, nodes)
    assert "house" in out and "halfspace" in out["house"].split()
    with open(expansion.sidecar_path(store), "rb") as fh:
        published = pickle.load(fh)
    assert published["expansion"] == out
    assert published["generation"] == "2026-09-30T01:00:00Z"
    assert not lock.exists()
    assert not [p for p in tmp_path.iterdir() if p.name.endswith(".tmp")]
