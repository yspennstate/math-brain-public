"""The content-addressed store never writes through a link.

Scheduled audit fleet04/B19 (29 Sep 2026), B19-R69-OVERLAY-CONTAINMENT-PREMISE-20260929:
persist() created its directories with mkdir(parents=True), which follows a symbolic link or
junction already on the way, so a store whose objects/ pointed elsewhere wrote there under
correct-looking names. A Windows junction is used where symbolic links need privileges.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

from math_brain.models import ClaimKind
from math_brain.overlay import (
    ContentAddressedTextStore,
    MathNodeRevision,
    SourceProvenance,
    TrustClass,
)


def _revision() -> MathNodeRevision:
    return MathNodeRevision(
        namespace="combinatorics.mols",
        logical_name="containment-check",
        kind=ClaimKind.LEMMA,
        title="Containment check",
        statement="Repeated source pairs contradict quotient column-symbol AMO.",
        provenance=SourceProvenance(
            source_id="source:containment-test",
            source_revision="git:0000000",
            locator="test",
            imported_by="test-suite",
            trust_class=TrustClass.PRIMARY_SOURCE,
        ),
        assumptions=("Each source array is Latin.",),
        domain="finite combinatorics",
    )


def _link(link: Path, target: Path) -> None:
    if sys.platform == "win32":
        import _winapi

        _winapi.CreateJunction(str(target), str(link))
        return
    try:
        os.symlink(target, link, target_is_directory=True)
    except OSError as exc:  # pragma: no cover - platform without symlinks
        pytest.skip(f"cannot create a directory link here: {exc}")


def _files(root: Path) -> list[Path]:
    return [p for p in root.rglob("*") if p.is_file()]


def test_objects_dir_that_is_a_link_is_refused(tmp_path: Path) -> None:
    store_root = tmp_path / "store"
    outside = tmp_path / "outside"
    store_root.mkdir()
    outside.mkdir()
    _link(store_root / "objects", outside)
    store = ContentAddressedTextStore(store_root)
    with pytest.raises(OSError, match=r"link|outside"):
        store.persist(_revision())
    assert _files(outside) == [] and list(outside.iterdir()) == []


def test_a_shard_dir_that_is_a_link_is_refused(tmp_path: Path) -> None:
    store_root = tmp_path / "store"
    outside = tmp_path / "outside"
    outside.mkdir()
    store = ContentAddressedTextStore(store_root)
    receipt = store.persist(_revision())            # learn the shard directory, then replace it
    shard = (store_root / receipt.relative_path).parent
    for f in shard.iterdir():
        f.unlink()
    shard.rmdir()
    _link(shard, outside)
    with pytest.raises(OSError, match=r"link|outside"):
        store.persist(_revision())
    assert _files(outside) == []


def test_a_plain_store_still_persists_idempotently(tmp_path: Path) -> None:
    store = ContentAddressedTextStore(tmp_path / "store")
    first = store.persist(_revision())
    second = store.persist(_revision())
    assert first == second
    written = (store.root / first.relative_path).read_text(encoding="utf-8")
    assert written == _revision().render_markdown()
