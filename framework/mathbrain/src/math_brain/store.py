"""Append-only SQLite store for mathematical claims, evidence, and graph edges."""

from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict
from pathlib import Path
from typing import Iterable, Iterator

from .mistakes import MistakeKind, MistakeRecord, ReflexRecord
from .models import (
    Claim,
    ClaimKind,
    EdgeKind,
    Evidence,
    EvidenceKind,
    GraphEdge,
    GraphNode,
    NodeKind,
    RecordStatus,
    VerificationEvent,
    canonical_json,
)


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS schema_meta (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS nodes (
    id TEXT PRIMARY KEY,
    kind TEXT NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    metadata_json TEXT NOT NULL,
    digest TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS claims (
    id TEXT PRIMARY KEY REFERENCES nodes(id),
    payload_json TEXT NOT NULL,
    digest TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS evidence (
    id TEXT PRIMARY KEY REFERENCES nodes(id),
    claim_id TEXT NOT NULL REFERENCES claims(id),
    payload_json TEXT NOT NULL,
    digest TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS mistakes (
    id TEXT PRIMARY KEY REFERENCES nodes(id),
    claim_id TEXT NOT NULL REFERENCES claims(id),
    payload_json TEXT NOT NULL,
    digest TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reflexes (
    id TEXT PRIMARY KEY REFERENCES nodes(id),
    payload_json TEXT NOT NULL,
    digest TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS reflex_sources (
    reflex_id TEXT NOT NULL REFERENCES reflexes(id),
    mistake_id TEXT NOT NULL REFERENCES mistakes(id),
    PRIMARY KEY(reflex_id, mistake_id)
);
CREATE TABLE IF NOT EXISTS verification_events (
    id TEXT PRIMARY KEY,
    claim_id TEXT NOT NULL REFERENCES claims(id),
    payload_json TEXT NOT NULL,
    digest TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS edges (
    id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL REFERENCES nodes(id),
    target_id TEXT NOT NULL REFERENCES nodes(id),
    kind TEXT NOT NULL,
    rationale TEXT NOT NULL,
    weight REAL NOT NULL CHECK(weight > 0 AND weight <= 1),
    metadata_json TEXT NOT NULL,
    digest TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL,
    UNIQUE(source_id, target_id, kind)
);
CREATE INDEX IF NOT EXISTS idx_nodes_kind ON nodes(kind);
CREATE INDEX IF NOT EXISTS idx_evidence_claim ON evidence(claim_id);
CREATE INDEX IF NOT EXISTS idx_mistakes_claim ON mistakes(claim_id);
CREATE INDEX IF NOT EXISTS idx_reflex_sources_mistake ON reflex_sources(mistake_id);
CREATE INDEX IF NOT EXISTS idx_events_claim_time ON verification_events(claim_id, created_at);
CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source_id);
CREATE INDEX IF NOT EXISTS idx_edges_target ON edges(target_id);
"""


class ResearchStore:
    """Small trusted persistence layer with no update/delete API."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.connection.execute("PRAGMA journal_mode = WAL")
        self.connection.executescript(SCHEMA_SQL)
        self.connection.execute("INSERT OR IGNORE INTO schema_meta(version) VALUES (1)")
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> ResearchStore:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def transaction(self) -> sqlite3.Connection:
        return self.connection

    def add_node(self, node: GraphNode) -> None:
        self.connection.execute(
            """INSERT INTO nodes(id, kind, title, body, metadata_json, digest, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                node.id,
                node.kind.value,
                node.title,
                node.body,
                canonical_json(node.metadata),
                node.digest(),
                node.created_at,
            ),
        )

    def add_claim(self, claim: Claim) -> None:
        payload = asdict(claim)
        try:
            with self.connection:
                self.add_node(
                    GraphNode(
                        id=claim.id,
                        kind=NodeKind.CLAIM,
                        title=claim.statement,
                        body="\n".join(claim.assumptions),
                        metadata={"claim_kind": claim.kind.value, "domain": claim.domain},
                        created_at=claim.created_at,
                    )
                )
                self.connection.execute(
                    "INSERT INTO claims(id, payload_json, digest, created_at) VALUES (?, ?, ?, ?)",
                    (claim.id, canonical_json(payload), claim.digest(), claim.created_at),
                )
        except sqlite3.IntegrityError as exc:
            raise ValueError(f"claim is not appendable: {exc}") from exc

    def add_evidence(self, evidence: Evidence, *, link: bool = True) -> None:
        payload = asdict(evidence)
        try:
            with self.connection:
                self.add_node(
                    GraphNode(
                        id=evidence.id,
                        kind=NodeKind.EVIDENCE,
                        title=evidence.summary,
                        body="\n".join(evidence.limitations),
                        metadata={
                            "evidence_kind": evidence.kind.value,
                            "scope": evidence.scope,
                            "passed": evidence.passed,
                        },
                        created_at=evidence.created_at,
                    )
                )
                self.connection.execute(
                    """INSERT INTO evidence(id, claim_id, payload_json, digest, created_at)
                       VALUES (?, ?, ?, ?, ?)""",
                    (
                        evidence.id,
                        evidence.claim_id,
                        canonical_json(payload),
                        evidence.digest(),
                        evidence.created_at,
                    ),
                )
                if link:
                    edge_kind = (
                        EdgeKind.REFUTES
                        if evidence.kind is EvidenceKind.COUNTEREXAMPLE and evidence.passed
                        else EdgeKind.VERIFIED_BY
                    )
                    self.add_edge(
                        GraphEdge(
                            source_id=evidence.claim_id,
                            target_id=evidence.id,
                            kind=edge_kind,
                            rationale=f"Evidence record {evidence.id}",
                            metadata={"passed": evidence.passed},
                        ),
                        commit=False,
                    )
        except sqlite3.IntegrityError as exc:
            raise ValueError(f"evidence is not appendable: {exc}") from exc

    def add_mistake(self, mistake: MistakeRecord, *, link: bool = True) -> None:
        try:
            with self.connection:
                self.add_node(mistake.to_node())
                self.connection.execute(
                    """INSERT INTO mistakes(
                           id, claim_id, payload_json, digest, created_at
                       ) VALUES (?, ?, ?, ?, ?)""",
                    (
                        mistake.id,
                        mistake.claim_id,
                        canonical_json(asdict(mistake)),
                        mistake.digest(),
                        mistake.created_at,
                    ),
                )
                if link:
                    self.add_edge(
                        GraphEdge(
                            source_id=mistake.claim_id,
                            target_id=mistake.id,
                            kind=EdgeKind.FAILS_UNDER,
                            rationale=(
                                "A structured mistake records a condition under which the claim "
                                "or its attempted proof failed"
                            ),
                            metadata={"mistake_kind": mistake.kind.value},
                        ),
                        commit=False,
                    )
        except sqlite3.IntegrityError as exc:
            raise ValueError(f"mistake is not appendable: {exc}") from exc

    def add_reflex(self, reflex: ReflexRecord, *, link: bool = True) -> None:
        try:
            with self.connection:
                self.add_node(reflex.to_node())
                self.connection.execute(
                    """INSERT INTO reflexes(id, payload_json, digest, created_at)
                       VALUES (?, ?, ?, ?)""",
                    (
                        reflex.id,
                        canonical_json(asdict(reflex)),
                        reflex.digest(),
                        reflex.created_at,
                    ),
                )
                for mistake_id in reflex.source_mistake_ids:
                    self.connection.execute(
                        "INSERT INTO reflex_sources(reflex_id, mistake_id) VALUES (?, ?)",
                        (reflex.id, mistake_id),
                    )
                    if link:
                        self.add_edge(
                            GraphEdge(
                                source_id=mistake_id,
                                target_id=reflex.id,
                                kind=EdgeKind.TRIGGERS,
                                rationale=(
                                    "Replaying the cited mistake activates a concrete review reflex"
                                ),
                                metadata={"required_evidence": reflex.required_evidence},
                            ),
                            commit=False,
                        )
        except sqlite3.IntegrityError as exc:
            raise ValueError(f"reflex is not appendable: {exc}") from exc

    def add_verification_event(self, event: VerificationEvent) -> None:
        try:
            with self.connection:
                self.connection.execute(
                    """INSERT INTO verification_events(id, claim_id, payload_json, digest, created_at)
                       VALUES (?, ?, ?, ?, ?)""",
                    (
                        event.id,
                        event.claim_id,
                        canonical_json(asdict(event)),
                        event.digest(),
                        event.created_at,
                    ),
                )
        except sqlite3.IntegrityError as exc:
            raise ValueError(f"verification event is not appendable: {exc}") from exc

    def add_edge(self, edge: GraphEdge, *, commit: bool = True) -> None:
        self.connection.execute(
            """INSERT INTO edges(
                   id, source_id, target_id, kind, rationale, weight,
                   metadata_json, digest, created_at
               ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                edge.id,
                edge.source_id,
                edge.target_id,
                edge.kind.value,
                edge.rationale,
                edge.weight,
                canonical_json(edge.metadata),
                edge.digest(),
                edge.created_at,
            ),
        )
        if commit:
            self.connection.commit()

    def get_claim(self, claim_id: str) -> Claim | None:
        row = self.connection.execute(
            "SELECT payload_json FROM claims WHERE id = ?", (claim_id,)
        ).fetchone()
        if row is None:
            return None
        payload = json.loads(row["payload_json"])
        payload["kind"] = ClaimKind(payload["kind"])
        payload["status"] = RecordStatus(payload["status"])
        payload["assumptions"] = tuple(payload["assumptions"])
        return Claim(**payload)

    def evidence_for(self, claim_id: str) -> list[Evidence]:
        rows = self.connection.execute(
            "SELECT payload_json FROM evidence WHERE claim_id = ? ORDER BY created_at, id",
            (claim_id,),
        ).fetchall()
        result = []
        for row in rows:
            payload = json.loads(row["payload_json"])
            payload["kind"] = EvidenceKind(payload["kind"])
            payload["limitations"] = tuple(payload["limitations"])
            result.append(Evidence(**payload))
        return result

    def get_mistake(self, mistake_id: str) -> MistakeRecord | None:
        row = self.connection.execute(
            "SELECT payload_json FROM mistakes WHERE id = ?", (mistake_id,)
        ).fetchone()
        if row is None:
            return None
        payload = json.loads(row["payload_json"])
        payload["kind"] = MistakeKind(payload["kind"])
        payload["repair_steps"] = tuple(payload["repair_steps"])
        payload["affected_assumptions"] = tuple(payload["affected_assumptions"])
        return MistakeRecord(**payload)

    def get_reflex(self, reflex_id: str) -> ReflexRecord | None:
        row = self.connection.execute(
            "SELECT payload_json FROM reflexes WHERE id = ?", (reflex_id,)
        ).fetchone()
        if row is None:
            return None
        payload = json.loads(row["payload_json"])
        for field_name in (
            "activation_cues",
            "action_steps",
            "required_evidence",
            "source_mistake_ids",
        ):
            payload[field_name] = tuple(payload[field_name])
        return ReflexRecord(**payload)

    def current_status(self, claim_id: str) -> RecordStatus:
        row = self.connection.execute(
            """SELECT payload_json FROM verification_events
               WHERE claim_id = ? ORDER BY created_at DESC, rowid DESC LIMIT 1""",
            (claim_id,),
        ).fetchone()
        if row is not None:
            return RecordStatus(json.loads(row["payload_json"])["to_status"])
        claim = self.get_claim(claim_id)
        if claim is None:
            raise KeyError(claim_id)
        return claim.status

    def iter_nodes(self) -> Iterator[GraphNode]:
        for row in self.connection.execute("SELECT * FROM nodes ORDER BY created_at, id"):
            yield GraphNode(
                id=row["id"],
                kind=NodeKind(row["kind"]),
                title=row["title"],
                body=row["body"],
                metadata=json.loads(row["metadata_json"]),
                created_at=row["created_at"],
            )

    def iter_edges(self) -> Iterator[GraphEdge]:
        for row in self.connection.execute("SELECT * FROM edges ORDER BY created_at, id"):
            yield GraphEdge(
                id=row["id"],
                source_id=row["source_id"],
                target_id=row["target_id"],
                kind=EdgeKind(row["kind"]),
                rationale=row["rationale"],
                weight=row["weight"],
                metadata=json.loads(row["metadata_json"]),
                created_at=row["created_at"],
            )

    def neighbors(self, node_ids: Iterable[str]) -> list[GraphEdge]:
        ids = tuple(dict.fromkeys(node_ids))
        if not ids:
            return []
        placeholders = ",".join("?" for _ in ids)
        query = f"SELECT * FROM edges WHERE source_id IN ({placeholders}) OR target_id IN ({placeholders})"
        rows = self.connection.execute(query, ids + ids).fetchall()
        result = []
        for row in rows:
            result.append(
                GraphEdge(
                    id=row["id"],
                    source_id=row["source_id"],
                    target_id=row["target_id"],
                    kind=EdgeKind(row["kind"]),
                    rationale=row["rationale"],
                    weight=row["weight"],
                    metadata=json.loads(row["metadata_json"]),
                    created_at=row["created_at"],
                )
            )
        return result
