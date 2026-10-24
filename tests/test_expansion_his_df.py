"""The owner-prompt term counts behind the expansion vocabulary are bound to their source and do not depend on order.

Interactive audit MB 20260929T1824Z-brain-methods: BM-20260929-02 (the cache was keyed by file size and time alone, so
another file or a replaced file with an equal stamp read the old counts) and BM-20260929-03 (only the first prompt of a
300-character prefix cluster was read, so a later prompt's own terms were lost and the counts depended on order). The
tokenizer is replaced by a whitespace split so the tests isolate cache identity and counting.
"""

import json
import os
from pathlib import Path

import pytest

from math_brain import expansion


def _write(path: Path, texts: list[str], origin: str = "owner") -> None:
    path.write_text(
        "".join(json.dumps({"origin": origin, "text": t}) + "\n" for t in texts), encoding="utf-8"
    )


@pytest.fixture()
def rig(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    calls: list[str] = []

    def terms(text: str) -> list[str]:
        calls.append(text)
        return text.split()

    monkeypatch.setattr(expansion, "_terms", terms)
    monkeypatch.setattr(expansion, "_tokenizer_identity", lambda: "tokenizer-a", raising=False)
    cache = tmp_path / "his.pkl"
    return tmp_path, cache, calls, monkeypatch


def _use(monkeypatch: pytest.MonkeyPatch, path: Path) -> None:
    monkeypatch.setattr(expansion, "PROMPTS", path)


def test_an_unchanged_source_is_read_from_the_cache(rig) -> None:
    tmp, cache, calls, mp = rig
    source = tmp / "prompts.jsonl"
    _write(source, ["alpha beta gamma delta", "epsilon zeta eta theta"])
    _use(mp, source)
    cold = expansion._his_df(cache)
    n_calls = len(calls)
    warm = expansion._his_df(cache)

    assert warm == cold
    assert len(calls) == n_calls


def test_another_file_with_the_same_size_and_time_is_not_served_from_the_cache(rig) -> None:
    tmp, cache, calls, mp = rig
    first, second = tmp / "a.jsonl", tmp / "b.jsonl"
    _write(first, ["alpha alpha alpha words"])
    _write(second, ["gamma gamma gamma words"])
    stamp = os.stat(first).st_mtime_ns
    os.utime(second, ns=(stamp, stamp))
    assert os.path.getsize(first) == os.path.getsize(second)
    _use(mp, first)
    df_first, _ = expansion._his_df(cache)
    _use(mp, second)
    df_second, _ = expansion._his_df(cache)

    assert "alpha" in df_first and "gamma" in df_second and "alpha" not in df_second


def test_the_same_file_replaced_with_an_equal_stamp_is_recounted(rig) -> None:
    tmp, cache, calls, mp = rig
    source = tmp / "prompts.jsonl"
    _write(source, ["alpha alpha alpha words"])
    stamp = os.stat(source).st_mtime_ns
    _use(mp, source)
    expansion._his_df(cache)
    _write(source, ["gamma gamma gamma words"])
    os.utime(source, ns=(stamp, stamp))
    df, _ = expansion._his_df(cache)

    assert "gamma" in df and "alpha" not in df


def test_a_new_tokenizer_recounts(rig) -> None:
    tmp, cache, calls, mp = rig
    source = tmp / "prompts.jsonl"
    _write(source, ["alpha beta gamma delta"])
    _use(mp, source)
    expansion._his_df(cache)
    n_calls = len(calls)
    mp.setattr(expansion, "_tokenizer_identity", lambda: "tokenizer-b", raising=False)
    expansion._his_df(cache)

    assert len(calls) > n_calls


def test_a_later_prompt_in_a_cluster_keeps_its_own_terms(rig) -> None:
    tmp, cache, calls, mp = rig
    shared = "x" * 300
    source = tmp / "prompts.jsonl"
    _write(source, [shared + " first unique", shared + " second special"])
    _use(mp, source)
    df, n = expansion._his_df(cache)

    assert n == 1
    assert df["first"] == 1 and df["second"] == 1 and df["special"] == 1
    assert df["unique"] == 1


def test_exact_duplicates_count_once(rig) -> None:
    tmp, cache, calls, mp = rig
    source = tmp / "prompts.jsonl"
    _write(source, ["alpha beta gamma delta"] * 3)
    _use(mp, source)
    df, n = expansion._his_df(cache)

    assert n == 1 and df["alpha"] == 1


def test_the_counts_do_not_depend_on_the_order_of_the_prompts(rig) -> None:
    tmp, cache, calls, mp = rig
    shared = "y" * 300
    texts = [shared + " one", shared + " two", "a separate prompt here", shared + " three"]
    forward, backward = tmp / "f.jsonl", tmp / "b.jsonl"
    _write(forward, texts)
    _write(backward, list(reversed(texts)))
    _use(mp, forward)
    one = expansion._his_df(tmp / "f.pkl")
    _use(mp, backward)
    two = expansion._his_df(tmp / "b.pkl")

    assert one == two


def test_only_the_owners_prompts_of_twelve_characters_or_more_count(rig) -> None:
    tmp, cache, calls, mp = rig
    source = tmp / "prompts.jsonl"
    source.write_text(
        json.dumps({"origin": "agent", "text": "an agent message here"}) + "\n"
        + json.dumps({"origin": "owner", "text": "too short"}) + "\n"
        + "not json\n"
        + json.dumps({"origin": "owner", "text": "a real prompt of his"}) + "\n",
        encoding="utf-8",
    )
    _use(mp, source)
    df, n = expansion._his_df(cache)

    assert n == 1 and "agent" not in df and df["real"] == 1


def test_the_cache_is_published_without_leaving_temporary_files(rig) -> None:
    tmp, cache, calls, mp = rig
    source = tmp / "prompts.jsonl"
    _write(source, ["alpha beta gamma delta"])
    _use(mp, source)
    expansion._his_df(cache)

    assert cache.exists()
    assert not [p for p in tmp.iterdir() if p.name.endswith(".tmp")]
