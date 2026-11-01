"""typed_paths (w15 mechanism 6) as math_brain CLI commands: the module's selftest, and history/source/links/path through
cli.main on the selftest's toy store written to disk. The toy store lacks the tables the store's reader needs, so the
reader refuses its cards and the CLI adds WARNING lines; apart from those lines the CLI prints exactly what the module
prints with no reader."""
from __future__ import annotations

import sqlite3
from pathlib import Path

from math_brain import cli, typed_paths


def _toy_db(tmp_path: Path) -> Path:
    db = tmp_path / "toy.sqlite3"
    src = typed_paths._toy()
    src.commit()                  # the toy's inserts are an open transaction; backup() would retry on it forever
    out = sqlite3.connect(str(db))
    src.backup(out)
    out.close()
    src.close()
    return db


def test_selftest_passes() -> None:
    assert typed_paths.selftest() == 0


def test_cli_prints_the_module_output_plus_reader_warnings_only(tmp_path: Path, capsys) -> None:
    db = _toy_db(tmp_path)
    plain = typed_paths.Store(sqlite3.connect("file:%s?mode=ro" % db.as_posix(), uri=True))
    cases = [(["history", str(db), "c_old"], typed_paths.history(plain, "c_old")),
             (["source", str(db), "c_old"], typed_paths.source(plain, "c_old")),
             (["links", str(db), "c_new"], typed_paths.links(plain, "c_new")),
             (["path", str(db), "c_new", "c_far"], typed_paths.path(plain, "c_new", "c_far")),
             (["path", str(db), "c_far", "c_new", "--undirected"],
              typed_paths.path(plain, "c_far", "c_new", undirected=True)),
             (["path", str(db), "c_new", "c_far", "--kinds", "cites"],
              typed_paths.path(plain, "c_new", "c_far", kinds=("cites",)))]
    for i, (argv, expected) in enumerate(cases):
        assert cli.main(argv) == 0
        got = capsys.readouterr().out.splitlines()
        assert [x for x in got if "WARNING: the store's own reader refuses" not in x] == expected.splitlines(), argv
        if i == 0:      # the toy has no schema_meta, so the reader refuses the current version and the CLI says so
            assert any("WARNING: the store's own reader refuses c_new (" in x for x in got)
    assert "v2 CURRENT c_new" in typed_paths.history(plain, "c_old")
    assert typed_paths.path(plain, "c_new", "c_far", kinds=("cites",)).startswith("no path")


def test_cli_opens_the_store_read_only(tmp_path: Path, capsys) -> None:
    db = _toy_db(tmp_path)
    before = db.read_bytes()
    for argv in (["history", str(db), "c_old"], ["links", str(db), "c_old"], ["path", str(db), "c_old", "c_far"]):
        assert cli.main(argv) == 0
    capsys.readouterr()
    assert db.read_bytes() == before
    assert not list(tmp_path.glob("toy.sqlite3-*"))      # no journal or WAL file left by a writer
