"""What an expansion build says it found (fleet04/B03, 29 Sep 2026).

Until 30 Sep the memory directory defaulted to one machine's absolute user path, and a build with that directory unset
or missing returned an empty expansion exactly like a store with nothing to expand, so a misconfigured index build
looked like a successful one. build() now names no directory of its own and records in LAST_BUILD whether it was
unconfigured, found no directory, built nothing, or built cards, and which sidecar it wrote.
"""

import collections
import pickle
import sqlite3
from pathlib import Path

import pytest

from math_brain import expansion, privacy_scan
from math_brain.models import GraphNode, NodeKind


@pytest.fixture()
def split_terms(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(expansion, "_terms", lambda text: (text or "").split())
    monkeypatch.setattr(expansion, "_tokenizer_identity", lambda: "tokenizer-a", raising=False)
    monkeypatch.setattr(expansion, "MAX_DF_SHARE", 1.0)


def _store(tmp_path: Path, refs=(("house", "memory:house_result"),)):
    store = tmp_path / "brain.sqlite3"
    db = sqlite3.connect(store)
    db.execute("CREATE TABLE claim_provenance (claim_id TEXT, source_ref TEXT)")
    db.executemany("INSERT INTO claim_provenance VALUES (?, ?)", list(refs))
    db.commit()
    db.close()
    nodes = [GraphNode("house", NodeKind.CLAIM, "FEI result", "The program's result.", created_at="2026-09-30T01:00:00Z")]
    nodes += [
        GraphNode("c%d" % k, NodeKind.CLAIM, "halfspace coefficient", "A card about a halfspace coefficient %d." % k,
                  created_at="2026-09-29T00:00:00Z")
        for k in range(3)
    ]
    return store, nodes


def _memory(tmp_path: Path) -> Path:
    memory = tmp_path / "memory"
    memory.mkdir()
    (memory / "house_result.md").write_text(
        "---\nname: house_result\n---\nThe halfspace coefficient bound holds for every halfspace.\n", encoding="utf-8"
    )
    return memory


# codex_runner.py falls back to the Windows system directory when SystemRoot is unset: a system path, not a user's
KNOWN_SYSTEM_PATHS = {"src/math_brain/codex_runner.py": 1}


def test_no_package_module_carries_an_absolute_local_path() -> None:
    # the expansion defaults and build_signal_cache's store were both one machine's absolute user path until 30 Sep;
    # the repository's own privacy scanner is the judge, so this test carries no path of its own
    root = Path(expansion.__file__).resolve().parents[2]
    policy = privacy_scan.load_scan_policy(root / "config" / "privacy.toml", repository_root=root)
    modules = sorted(p.relative_to(root).as_posix() for p in (root / "src" / "math_brain").glob("*.py"))
    found = collections.Counter(
        f.path for f in privacy_scan.scan_repository_files(repository_root=root, relative_paths=modules, policy=policy)
        if f.code == "absolute-path"
    )
    assert dict(found) == KNOWN_SYSTEM_PATHS


def test_an_unconfigured_build_says_so_and_writes_nothing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    monkeypatch.setattr(expansion, "MEMORY_DIR", None)
    monkeypatch.setattr(expansion, "PROMPTS", None)
    store, nodes = _store(tmp_path)
    assert expansion.build(store, nodes) == {}
    assert expansion.LAST_BUILD["status"] == "unconfigured"
    assert "memory_dir" in expansion.LAST_BUILD["reason"]
    assert expansion.LAST_BUILD["sidecar"] is None
    assert not Path(expansion.sidecar_path(store)).exists()


def test_a_named_directory_that_does_not_exist_is_source_missing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    monkeypatch.setattr(expansion, "MEMORY_DIR", None)
    monkeypatch.setattr(expansion, "PROMPTS", None)
    store, nodes = _store(tmp_path)
    assert expansion.build(store, nodes, memory_dir=tmp_path / "no_such_memory") == {}
    assert expansion.LAST_BUILD["status"] == "source_missing"
    assert expansion.LAST_BUILD["source"] == str(tmp_path / "no_such_memory")
    assert not Path(expansion.sidecar_path(store)).exists()


def test_a_valid_directory_with_nothing_to_expand_is_success_empty(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    monkeypatch.setattr(expansion, "MEMORY_DIR", None)
    monkeypatch.setattr(expansion, "PROMPTS", None)
    store, nodes = _store(tmp_path, refs=())   # no card was born from a memory
    assert expansion.build(store, nodes, memory_dir=_memory(tmp_path)) == {}
    assert expansion.LAST_BUILD["status"] == "success_empty"
    assert expansion.LAST_BUILD["reason"]
    assert expansion.LAST_BUILD["sidecar"] is None


def test_a_valid_build_names_its_cards_and_the_sidecar_it_wrote(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    monkeypatch.setattr(expansion, "MEMORY_DIR", None)
    monkeypatch.setattr(expansion, "PROMPTS", None)
    store, nodes = _store(tmp_path)
    out = expansion.build(store, nodes, memory_dir=_memory(tmp_path))
    assert "halfspace" in out["house"].split()
    assert expansion.LAST_BUILD["status"] == "success"
    assert expansion.LAST_BUILD["cards"] == 1
    assert expansion.LAST_BUILD["sidecar"] == expansion.sidecar_path(store)
    with open(expansion.sidecar_path(store), "rb") as fh:
        assert pickle.load(fh)["expansion"] == out


def test_the_environment_names_the_directory_when_the_caller_does_not(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    monkeypatch.setattr(expansion, "MEMORY_DIR", _memory(tmp_path))
    monkeypatch.setattr(expansion, "PROMPTS", None)
    store, nodes = _store(tmp_path)
    assert "house" in expansion.build(store, nodes)
    assert expansion.LAST_BUILD["status"] == "success"


def test_a_build_that_leaves_a_newer_sidecar_in_place_names_no_sidecar(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    monkeypatch.setattr(expansion, "MEMORY_DIR", None)
    monkeypatch.setattr(expansion, "PROMPTS", None)
    store, nodes = _store(tmp_path)
    newer = {"generation": "2026-09-30T09:00:00Z", "expansion": {"house": "from a newer store state"}}
    expansion._publish(expansion.sidecar_path(store), newer)
    out = expansion.build(store, nodes, memory_dir=_memory(tmp_path))
    assert out and expansion.LAST_BUILD["status"] == "success"
    assert expansion.LAST_BUILD["sidecar"] is None
    with open(expansion.sidecar_path(store), "rb") as fh:
        assert pickle.load(fh)["expansion"] == newer["expansion"]


def test_the_prompt_ledger_defaults_under_the_named_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, split_terms
) -> None:
    monkeypatch.setattr(expansion, "MEMORY_DIR", None)
    monkeypatch.setattr(expansion, "PROMPTS", None)
    memory = _memory(tmp_path)
    (memory / "prompts").mkdir()
    # his prompts carry "halfspace" in every cluster, so the owner filter drops it from the vocabulary
    lines = ['{"origin": "owner", "text": "halfspace question number %d please"}' % k for k in range(5)]
    (memory / "prompts" / "PROMPTS.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    monkeypatch.setattr(expansion, "HIS_SHARE", 0.0)
    store, nodes = _store(tmp_path)
    out = expansion.build(store, nodes, memory_dir=memory)
    assert "halfspace" not in out.get("house", "").split()
