"""Crash-safe materialization for the deterministic synthetic benchmark bank."""

from __future__ import annotations

import hashlib
import os
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path

from .benchmark import (
    BENCHMARK_CAPACITY,
    GENERATOR_BUNDLE_HASH,
    GENERATOR_SOURCE_HASH,
    GENERATOR_VERSION,
    BenchmarkManifest,
    build_manifest,
    generate_bank,
)
from .models import canonical_json


ARTIFACT_SCHEMA = "org.math-research-brain/benchmark-artifact"
ARTIFACT_SCHEMA_VERSION = 1


@dataclass(frozen=True, slots=True)
class MaterializedBenchmark:
    directory: Path
    items_path: Path
    manifest_path: Path
    provenance_path: Path
    manifest: BenchmarkManifest
    items_digest: str
    items_bytes: int


def _write_canonical(path: Path, payload: object) -> None:
    raw = (canonical_json(payload) + "\n").encode("utf-8")
    with path.open("xb") as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())


def materialize_benchmark(
    output_directory: str | Path,
    *,
    seed: str,
    count: int,
    start: int = 0,
) -> MaterializedBenchmark:
    """Write one certified JSONL bank and its manifest as an atomic directory.

    The destination must not exist. Items are generated once, streamed into a
    private staging directory, and simultaneously consumed by ``build_manifest``.
    A failed certificate or write leaves no apparently complete destination.
    """

    if (
        isinstance(count, bool)
        or not isinstance(count, int)
        or not 1 <= count <= BENCHMARK_CAPACITY
    ):
        raise ValueError(f"count must be in [1, {BENCHMARK_CAPACITY}]")
    if isinstance(start, bool) or not isinstance(start, int) or start < 0:
        raise ValueError("start must be a nonnegative exact integer")
    if start + count > BENCHMARK_CAPACITY:
        raise ValueError("requested window exceeds benchmark capacity")
    if not isinstance(seed, str) or not seed:
        raise ValueError("seed must be nonempty text")

    destination = Path(output_directory).resolve(strict=False)
    if destination.exists():
        raise FileExistsError(f"benchmark destination already exists: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(
        tempfile.mkdtemp(
            prefix=f".{destination.name}.staging-",
            dir=destination.parent,
        )
    )
    items_path = staging / "items.jsonl"
    manifest_path = staging / "manifest.json"
    provenance_path = staging / "provenance.json"
    digest = hashlib.sha256()
    item_bytes = 0

    try:
        with items_path.open("xb") as handle:

            def emitted_items():
                nonlocal item_bytes
                for item in generate_bank(seed, count, start=start):
                    raw = (item.canonical_json() + "\n").encode("utf-8")
                    handle.write(raw)
                    digest.update(raw)
                    item_bytes += len(raw)
                    yield item

            manifest = build_manifest(emitted_items(), seed=seed, start=start)
            handle.flush()
            os.fsync(handle.fileno())

        items_digest = "sha256:" + digest.hexdigest()
        _write_canonical(manifest_path, manifest.to_dict())
        _write_canonical(
            provenance_path,
            {
                "generator_bundle_hash": GENERATOR_BUNDLE_HASH,
                "generator_source_hash": GENERATOR_SOURCE_HASH,
                "generator_version": GENERATOR_VERSION,
                "item_count": count,
                "items_bytes": item_bytes,
                "items_digest": items_digest,
                "manifest_digest": manifest.digest(),
                "schema": ARTIFACT_SCHEMA,
                "schema_version": ARTIFACT_SCHEMA_VERSION,
                "seed": seed,
                "start_index": start,
            },
        )
        os.replace(staging, destination)
    except BaseException:
        if staging.exists() and staging.parent == destination.parent:
            shutil.rmtree(staging)
        raise

    return MaterializedBenchmark(
        directory=destination,
        items_path=destination / items_path.name,
        manifest_path=destination / manifest_path.name,
        provenance_path=destination / provenance_path.name,
        manifest=manifest,
        items_digest=items_digest,
        items_bytes=item_bytes,
    )


__all__ = [
    "ARTIFACT_SCHEMA",
    "ARTIFACT_SCHEMA_VERSION",
    "MaterializedBenchmark",
    "materialize_benchmark",
]
