from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import pytest

from math_brain.benchmark import BenchmarkItem, BenchmarkManifest, verify_manifest
from math_brain import benchmark_artifacts
from math_brain.benchmark_artifacts import (
    ARTIFACT_SCHEMA,
    ARTIFACT_SCHEMA_VERSION,
    BenchmarkDurabilityError,
    materialize_benchmark,
    verify_materialized_benchmark,
)


def test_materializer_writes_one_certified_atomic_artifact(tmp_path: Path) -> None:
    destination = tmp_path / "bank"
    artifact = materialize_benchmark(
        destination,
        seed="artifact-regression",
        count=12,
    )
    assert artifact.directory == destination.resolve()
    lines = artifact.items_path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 12
    items = tuple(BenchmarkItem.from_json(line) for line in lines)
    assert len({item.item_id for item in items}) == 12
    raw_items = artifact.items_path.read_bytes()
    assert artifact.items_digest == "sha256:" + hashlib.sha256(raw_items).hexdigest()

    manifest = BenchmarkManifest.from_json(
        artifact.manifest_path.read_text(encoding="utf-8")
    )
    assert manifest == artifact.manifest
    assert verify_manifest(manifest)
    provenance = json.loads(artifact.provenance_path.read_text(encoding="utf-8"))
    assert provenance["schema"] == ARTIFACT_SCHEMA
    assert provenance["schema_version"] == ARTIFACT_SCHEMA_VERSION
    assert provenance["items_digest"] == artifact.items_digest
    assert provenance["manifest_digest"] == manifest.digest()


def test_materializer_refuses_overwrite_and_invalid_windows(tmp_path: Path) -> None:
    destination = tmp_path / "bank"
    materialize_benchmark(destination, seed="no-overwrite", count=1)
    with pytest.raises(FileExistsError):
        materialize_benchmark(destination, seed="no-overwrite", count=1)
    with pytest.raises(ValueError, match="count"):
        materialize_benchmark(tmp_path / "zero", seed="invalid", count=0)
    with pytest.raises(ValueError, match="capacity"):
        materialize_benchmark(
            tmp_path / "overflow",
            seed="invalid",
            count=2,
            start=9_999,
        )


# B17-R79-BENCHMARK-DIRECTORY-RENAME-NOT-DURABLE-20260929: the rename is atomic, the directory
# entry is made durable where the platform allows, and a directory is verified jointly.


def test_publication_order_is_file_syncs_then_rename_then_directory_sync(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    events: list[str] = []
    real_fsync, real_replace = os.fsync, os.replace

    def spy_fsync(descriptor: int) -> None:
        events.append("file-fsync")
        real_fsync(descriptor)

    def spy_replace(source: object, target: object) -> None:
        events.append("rename")
        real_replace(source, target)

    monkeypatch.setattr(benchmark_artifacts.os, "fsync", spy_fsync)
    monkeypatch.setattr(benchmark_artifacts.os, "replace", spy_replace)
    monkeypatch.setattr(benchmark_artifacts, "_directory_sync_supported", lambda: True)
    monkeypatch.setattr(
        benchmark_artifacts, "_fsync_directory", lambda directory: events.append("directory-sync")
    )
    artifact = materialize_benchmark(tmp_path / "bank", seed="order", count=3)

    assert events == ["file-fsync"] * 3 + ["rename", "directory-sync"]
    assert artifact.durability == "parent-fsync"


def test_a_platform_without_directory_sync_says_so(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(benchmark_artifacts, "_directory_sync_supported", lambda: False)
    artifact = materialize_benchmark(tmp_path / "bank", seed="no-directory-sync", count=2)

    assert artifact.durability == "unavailable"


@pytest.mark.skipif(os.name == "nt", reason="Windows has no directory fsync")
def test_the_real_directory_sync_runs_where_supported(tmp_path: Path) -> None:
    artifact = materialize_benchmark(tmp_path / "bank", seed="posix-sync", count=1)

    assert artifact.durability == "parent-fsync"


def test_a_failed_rename_leaves_no_destination_and_no_staging(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def refuse(source: object, target: object) -> None:
        raise OSError("rename refused")

    monkeypatch.setattr(benchmark_artifacts.os, "replace", refuse)
    with pytest.raises(OSError, match="rename refused"):
        materialize_benchmark(tmp_path / "bank", seed="rename", count=2)

    assert list(tmp_path.iterdir()) == []


def test_a_failed_directory_sync_raises_and_leaves_a_verifiable_bank(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def refuse(directory: Path) -> None:
        raise OSError("sync refused")

    monkeypatch.setattr(benchmark_artifacts, "_directory_sync_supported", lambda: True)
    monkeypatch.setattr(benchmark_artifacts, "_fsync_directory", refuse)
    with pytest.raises(BenchmarkDurabilityError) as error:
        materialize_benchmark(tmp_path / "bank", seed="directory-sync", count=2)

    assert error.value.destination == (tmp_path / "bank").resolve()
    assert verify_materialized_benchmark(tmp_path / "bank").item_count == 2


def test_the_verifier_returns_the_manifest_of_a_fresh_bank(tmp_path: Path) -> None:
    artifact = materialize_benchmark(tmp_path / "bank", seed="verify", count=5)

    assert verify_materialized_benchmark(artifact.directory) == artifact.manifest


@pytest.mark.parametrize("name", ["items.jsonl", "manifest.json", "provenance.json"])
def test_the_verifier_rejects_one_changed_byte_in_each_file(tmp_path: Path, name: str) -> None:
    artifact = materialize_benchmark(tmp_path / "bank", seed="one-byte", count=4)
    path = artifact.directory / name
    raw = bytearray(path.read_bytes())
    middle = len(raw) // 2
    raw[middle] = ord("0") if raw[middle] != ord("0") else ord("1")
    path.write_bytes(bytes(raw))

    with pytest.raises(ValueError):
        verify_materialized_benchmark(artifact.directory)


@pytest.mark.parametrize(
    "damage", ["truncated-line", "extra-file", "missing-provenance", "extra-item"]
)
def test_the_verifier_rejects_structural_damage(tmp_path: Path, damage: str) -> None:
    artifact = materialize_benchmark(tmp_path / "bank", seed="damage", count=3)
    raw = artifact.items_path.read_bytes()
    if damage == "truncated-line":
        artifact.items_path.write_bytes(raw[:-10])
    elif damage == "extra-file":
        (artifact.directory / "notes.txt").write_text("unexpected", encoding="utf-8")
    elif damage == "missing-provenance":
        artifact.provenance_path.unlink()
    else:
        artifact.items_path.write_bytes(raw + raw.split(b"\n")[0] + b"\n")

    with pytest.raises(ValueError):
        verify_materialized_benchmark(artifact.directory)
