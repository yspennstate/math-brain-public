"""Deterministic, explainable lexical/formula plus signed-graph retrieval."""

from __future__ import annotations

import hashlib
import math
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from enum import StrEnum
from itertools import chain
from typing import Iterable

from .models import EdgeKind, EdgePolarity, GraphEdge, GraphNode


TOKEN_RE = re.compile(r"[^\W_]+(?:['’-][^\W_]+)?", re.UNICODE)
FORMULA_RE = re.compile(
    r"\$\$(.*?)\$\$|(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)|"
    r"\\\[(.*?)\\\]|\\\((.*?)\\\)",
    re.DOTALL,
)
MATH_HINT_RE = re.compile(
    r"\\[A-Za-z]+|[=<>≤≥≠≈≡∈∉∀∃∑∏∫√∂∇∞⊂⊆⊃⊇∪∩^_]|(?:->|=>|<->|:=)"
)
MATH_TOKEN_RE = re.compile(
    r"domain_[a-z]+|\\[a-z]+|[a-z][a-z0-9]*|\d+(?:\.\d+)?|"
    r"<->|->|<=|>=|!=|:=|[+\-*/^_=<>(){}\[\],:|]"
)

UNICODE_MATH_ALIASES = str.maketrans(
    {
        "∀": r" \forall ",
        "∃": r" \exists ",
        "∈": r" \in ",
        "∉": r" \notin ",
        "≤": r" \le ",
        "≥": r" \ge ",
        "≠": r" \ne ",
        "≈": r" \approx ",
        "≡": r" \equiv ",
        "→": r" \to ",
        "⇒": r" \implies ",
        "⇔": r" \iff ",
        "∑": r" \sum ",
        "∏": r" \prod ",
        "∫": r" \int ",
        "√": r" \sqrt ",
        "∂": r" \partial ",
        "∇": r" \nabla ",
        "∞": r" \infty ",
        "⊂": r" \subset ",
        "⊆": r" \subseteq ",
        "⊃": r" \supset ",
        "⊇": r" \supseteq ",
        "∪": r" \cup ",
        "∩": r" \cap ",
        "×": " * ",
        "·": " * ",
        "−": "-",
        "ℝ": " domain_real ",
        "ℤ": " domain_integer ",
        "ℚ": " domain_rational ",
        "ℕ": " domain_natural ",
        "ℂ": " domain_complex ",
        "α": r" \alpha ",
        "β": r" \beta ",
        "γ": r" \gamma ",
        "δ": r" \delta ",
        "ε": r" \epsilon ",
        "θ": r" \theta ",
        "λ": r" \lambda ",
        "μ": r" \mu ",
        "ν": r" \nu ",
        "ρ": r" \rho ",
        "σ": r" \sigma ",
        "τ": r" \tau ",
        "φ": r" \phi ",
        "ψ": r" \psi ",
        "ω": r" \omega ",
        "⁰": "^0",
        "¹": "^1",
        "²": "^2",
        "³": "^3",
        "⁴": "^4",
        "⁵": "^5",
        "⁶": "^6",
        "⁷": "^7",
        "⁸": "^8",
        "⁹": "^9",
    }
)

COMMAND_ALIASES = {
    r"\geq": r"\ge",
    r"\leq": r"\le",
    r"\neq": r"\ne",
    r"\longrightarrow": r"\to",
    r"\rightarrow": r"\to",
    r"\Rightarrow": r"\implies",
    r"\Leftrightarrow": r"\iff",
    r"\cdot": "*",
    r"\times": "*",
}

OPERATOR_COMMANDS = frozenset(
    {
        r"\forall",
        r"\exists",
        r"\in",
        r"\notin",
        r"\le",
        r"\ge",
        r"\ne",
        r"\approx",
        r"\equiv",
        r"\to",
        r"\implies",
        r"\iff",
        r"\sum",
        r"\prod",
        r"\int",
        r"\sqrt",
        r"\partial",
        r"\nabla",
        r"\subset",
        r"\subseteq",
        r"\supset",
        r"\supseteq",
        r"\cup",
        r"\cap",
    }
)
GREEK_VARIABLES = frozenset(
    {
        r"\alpha",
        r"\beta",
        r"\gamma",
        r"\delta",
        r"\epsilon",
        r"\varepsilon",
        r"\theta",
        r"\lambda",
        r"\mu",
        r"\nu",
        r"\rho",
        r"\sigma",
        r"\tau",
        r"\phi",
        r"\varphi",
        r"\psi",
        r"\omega",
    }
)
FUNCTION_NAMES = frozenset(
    {"sin", "cos", "tan", "log", "ln", "exp", "lim", "det", "ker", "im", "rank"}
)
FUNCTION_COMMANDS = {f"\\{name}": name for name in FUNCTION_NAMES}
CONSTANT_COMMANDS = {r"\pi": "pi", r"\infty": "infinity"}
OPERATOR_ALIASES = {
    "^": "pow",
    "=": "eq",
    "<": "lt",
    ">": "gt",
    "<=": "le",
    ">=": "ge",
    "!=": "ne",
    "+": "add",
    "-": "sub",
    "*": "mul",
    "/": "div",
    "_": "subscript",
    "->": "to",
    "<->": "iff",
    ":=": "define",
    "|": "such_that",
}
PUNCTUATION = frozenset("(){}[],: ")

EDGE_MULTIPLIER = {
    EdgeKind.DEPENDS_ON: 1.0,
    EdgeKind.DEFINES: 0.9,
    EdgeKind.PROVES: 1.0,
    EdgeKind.REFUTES: 1.25,
    EdgeKind.GENERALIZES: 0.8,
    EdgeKind.SPECIALIZES: 0.9,
    EdgeKind.ANALOGOUS_TO: 0.6,
    EdgeKind.CITES: 0.65,
    EdgeKind.VERIFIED_BY: 1.0,
    EdgeKind.FAILS_UNDER: 1.25,
    EdgeKind.TRIGGERS: 1.1,
}
MANDATORY_BLOCKED_ROLES = frozenset(
    {"answer_key", "solution", "fault_annotation", "evaluation_output"}
)


class ScoreChannel(StrEnum):
    LEXICAL = "lexical"
    SYMBOL = "symbol"
    FORMULA = "formula"
    GRAPH = "graph"
    WARNING = "warning"


class AbstentionReason(StrEnum):
    NO_INDEXABLE_SIGNALS = "no_indexable_signals"
    NO_CANDIDATE_MATCH = "no_candidate_match"
    BELOW_SUPPORT_THRESHOLD = "below_support_threshold"
    AMBIGUOUS_TOP_MATCH = "ambiguous_top_match"


@dataclass(frozen=True, slots=True)
class IndexSignals:
    lexical_tokens: tuple[str, ...]
    math_tokens: tuple[str, ...]
    formula_fingerprints: tuple[str, ...]

    @property
    def empty(self) -> bool:
        return not (self.lexical_tokens or self.math_tokens or self.formula_fingerprints)


@dataclass(frozen=True, slots=True)
class ScoreTrace:
    channel: ScoreChannel
    amount: float
    detail: str
    source_node_id: str | None = None
    edge_id: str | None = None
    edge_kind: EdgeKind | None = None
    edge_polarity: EdgePolarity | None = None
    path: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.amount < 0 or not math.isfinite(self.amount):
            raise ValueError("score trace amount must be finite and nonnegative")
        if not self.detail.strip():
            raise ValueError("score trace detail is required")

    @property
    def signed_amount(self) -> float:
        if self.edge_polarity is EdgePolarity.NEGATIVE:
            return -self.amount
        return self.amount


@dataclass(frozen=True, slots=True)
class SearchHit:
    node: GraphNode
    lexical_score: float
    symbol_score: float
    formula_score: float
    graph_score: float
    warning_score: float
    trace: tuple[ScoreTrace, ...] = ()

    @property
    def support_score(self) -> float:
        return self.lexical_score + self.symbol_score + self.formula_score + self.graph_score

    @property
    def total_score(self) -> float:
        return self.support_score + self.warning_score

    @property
    def warnings(self) -> tuple[ScoreTrace, ...]:
        return tuple(item for item in self.trace if item.channel is ScoreChannel.WARNING)


@dataclass(frozen=True, slots=True)
class GuardExclusion:
    node_id: str
    reason: str


@dataclass(frozen=True, slots=True)
class RetrievalGuard:
    """Fail-closed evaluation guard against answer and test-split contamination."""

    evaluation_split: str
    allowed_index_splits: tuple[str, ...] = ("train", "reference")
    active_item_id: str | None = None
    active_pair_id: str | None = None
    active_source_digest: str | None = None
    require_split_label: bool = True
    blocked_roles: tuple[str, ...] = (
        "answer_key",
        "solution",
        "fault_annotation",
        "evaluation_output",
    )

    def __post_init__(self) -> None:
        if not isinstance(self.evaluation_split, str) or not self.evaluation_split.strip():
            raise ValueError("evaluation_split is required")
        if self.require_split_label and not self.allowed_index_splits:
            raise ValueError("a split-requiring guard needs at least one allowed index split")
        if any(
            not isinstance(item, str) or not item.strip()
            for item in self.allowed_index_splits
        ):
            raise ValueError("allowed index splits must be nonempty")
        allowed = {item.strip().casefold() for item in self.allowed_index_splits}
        if self.evaluation_split.strip().casefold() in allowed:
            raise ValueError("the active evaluation split cannot be indexed")
        if any(not isinstance(item, str) or not item.strip() for item in self.blocked_roles):
            raise ValueError("blocked roles must be nonempty strings")
        blocked = {item.strip().casefold() for item in self.blocked_roles}
        missing_roles = MANDATORY_BLOCKED_ROLES.difference(blocked)
        if missing_roles:
            raise ValueError(
                "blocked roles must include " + ", ".join(sorted(missing_roles))
            )

    def exclusion_reason(self, node: GraphNode) -> str | None:
        metadata = node.metadata
        for marker, reason in (
            ("quarantined", "quarantined_record"),
            ("is_answer_key", "answer_key_marker"),
        ):
            if marker not in metadata:
                continue
            marker_value = _metadata_flag(metadata[marker])
            if marker_value is None:
                return f"malformed_boolean_marker:{marker}"
            if marker_value:
                return reason
        privacy_value = metadata.get("privacy_status", "")
        if not isinstance(privacy_value, str):
            return "malformed_privacy_status"
        privacy_status = privacy_value.strip().casefold()
        if privacy_status in {"denied", "quarantined"}:
            return "privacy_status_not_eligible"
        role_value = metadata.get("content_role", "")
        if not isinstance(role_value, str):
            return "malformed_content_role"
        role = role_value.strip().casefold()
        if role in {item.strip().casefold() for item in self.blocked_roles}:
            return f"blocked_content_role:{role}"
        split_value = metadata.get("split")
        if split_value is None and self.require_split_label:
            return "missing_split_label"
        if split_value is not None:
            if not isinstance(split_value, str) or not split_value.strip():
                return "malformed_split_label"
            split = split_value.strip().casefold()
            allowed = {item.strip().casefold() for item in self.allowed_index_splits}
            if split not in allowed:
                return f"split_not_allowed:{split}"
        if self.active_item_id is not None:
            if str(metadata.get("item_id", "")) == self.active_item_id:
                return "active_item_leakage"
        if self.active_pair_id is not None:
            if str(metadata.get("pair_id", "")) == self.active_pair_id:
                return "paired_item_leakage"
        if self.active_source_digest is not None:
            if str(metadata.get("source_digest", "")) == self.active_source_digest:
                return "source_digest_leakage"
        return None


@dataclass(frozen=True, slots=True)
class RetrievalResult:
    query_signals: IndexSignals
    hits: tuple[SearchHit, ...]
    abstained: bool
    reason: AbstentionReason | None
    exclusions: tuple[GuardExclusion, ...] = ()


def _metadata_flag(value: object) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in {0, 1}:
        return bool(value)
    if isinstance(value, str):
        normalized = value.strip().casefold()
        if normalized in {"true", "yes", "1"}:
            return True
        if normalized in {"false", "no", "0"}:
            return False
    return None


def tokenize(text: str) -> tuple[str, ...]:
    normalized = unicodedata.normalize("NFKC", text).casefold()
    return tuple(match.group(0) for match in TOKEN_RE.finditer(normalized))


def _formula_segments(text: str) -> tuple[str, ...]:
    delimited = tuple(
        next(group for group in match.groups() if group is not None)
        for match in FORMULA_RE.finditer(text)
    )
    if delimited:
        return delimited
    if MATH_HINT_RE.search(text):
        return (text,)
    return ()


def _normalize_number(token: str) -> str:
    if "." not in token:
        return token.lstrip("0") or "0"
    integer, fractional = token.split(".", 1)
    integer = integer.lstrip("0") or "0"
    fractional = fractional.rstrip("0")
    return integer if not fractional else f"{integer}.{fractional}"


def normalize_formula(expression: str) -> str:
    """Canonicalize notation and alpha-rename variables without evaluating it."""

    value = expression.translate(UNICODE_MATH_ALIASES)
    value = unicodedata.normalize("NFKC", value).casefold()
    value = re.sub(r"\\mathbb\s*\{\s*r\s*\}", " domain_real ", value)
    value = re.sub(r"\\mathbb\s*\{\s*z\s*\}", " domain_integer ", value)
    value = re.sub(r"\\mathbb\s*\{\s*q\s*\}", " domain_rational ", value)
    value = re.sub(r"\\mathbb\s*\{\s*n\s*\}", " domain_natural ", value)
    value = re.sub(r"\\mathbb\s*\{\s*c\s*\}", " domain_complex ", value)
    value = re.sub(r"\\(?:mathrm|mathbf|mathit)\s*\{([^{}]*)\}", r"\1", value)
    value = re.sub(r"\\operatorname\s*\{([^{}]*)\}", r"\1", value)
    value = value.replace(r"\left", "").replace(r"\right", "")
    for source, target in COMMAND_ALIASES.items():
        value = value.replace(source.casefold(), target)
    for spacing in (r"\,", r"\;", r"\!", r"\quad", r"\qquad"):
        value = value.replace(spacing, " ")

    variable_names: dict[str, str] = {}
    normalized_tokens: list[str] = []
    for raw_token in MATH_TOKEN_RE.findall(value):
        if raw_token in OPERATOR_COMMANDS:
            normalized_tokens.append(f"op:{raw_token[1:]}")
        elif raw_token in FUNCTION_COMMANDS:
            normalized_tokens.append(f"fn:{FUNCTION_COMMANDS[raw_token]}")
        elif raw_token in CONSTANT_COMMANDS:
            normalized_tokens.append(f"const:{CONSTANT_COMMANDS[raw_token]}")
        elif raw_token in GREEK_VARIABLES:
            variable_names.setdefault(raw_token, f"v{len(variable_names)}")
            normalized_tokens.append(variable_names[raw_token])
        elif raw_token.startswith("domain_"):
            normalized_tokens.append(f"const:{raw_token.removeprefix('domain_')}")
        elif raw_token.startswith("\\"):
            normalized_tokens.append(f"cmd:{raw_token[1:]}")
        elif raw_token in FUNCTION_NAMES:
            normalized_tokens.append(f"fn:{raw_token}")
        elif raw_token[0].isalpha():
            variable_names.setdefault(raw_token, f"v{len(variable_names)}")
            normalized_tokens.append(variable_names[raw_token])
        elif raw_token[0].isdigit():
            normalized_tokens.append(f"num:{_normalize_number(raw_token)}")
        elif raw_token in OPERATOR_ALIASES:
            normalized_tokens.append(f"op:{OPERATOR_ALIASES[raw_token]}")
        elif raw_token in PUNCTUATION:
            normalized_tokens.append(f"punct:{raw_token}")
    return " ".join(normalized_tokens)


def index_signals(text: str) -> IndexSignals:
    formulas = tuple(
        normalized
        for normalized in (normalize_formula(segment) for segment in _formula_segments(text))
        if normalized
    )
    math_tokens = tuple(chain.from_iterable(formula.split() for formula in formulas))
    fingerprints = tuple(
        "sha256:" + hashlib.sha256(formula.encode("utf-8")).hexdigest()
        for formula in formulas
    )
    return IndexSignals(tokenize(text), math_tokens, fingerprints)


def _channel_scores(
    query_terms: Iterable[str],
    document_terms: dict[str, tuple[str, ...]],
    *,
    channel: ScoreChannel,
    weight: float,
) -> tuple[dict[str, float], dict[str, list[ScoreTrace]]]:
    query_counts = Counter(query_terms)
    if not query_counts:
        return {}, {}
    document_counts = {node_id: Counter(terms) for node_id, terms in document_terms.items()}
    document_frequency: Counter[str] = Counter()
    for counts in document_counts.values():
        document_frequency.update(counts.keys())
    total_documents = max(1, len(document_counts))
    scores: dict[str, float] = {}
    traces: dict[str, list[ScoreTrace]] = defaultdict(list)
    for node_id, counts in document_counts.items():
        length = max(1, sum(counts.values()))
        for term, query_weight in sorted(query_counts.items()):
            if term not in counts:
                continue
            inverse_frequency = math.log1p(total_documents / (1 + document_frequency[term]))
            amount = (
                weight
                * query_weight
                * inverse_frequency
                * (1 + math.log1p(counts[term]))
                / math.sqrt(length)
            )
            scores[node_id] = scores.get(node_id, 0.0) + amount
            traces[node_id].append(
                ScoreTrace(channel, amount, f"matched normalized term {term!r}")
            )
    return scores, traces


def lexical_scores(query: str, nodes: Iterable[GraphNode]) -> dict[str, float]:
    materialized = list(nodes)
    scores, _ = _channel_scores(
        tokenize(query),
        {node.id: tokenize(node.title + " " + node.body) for node in materialized},
        channel=ScoreChannel.LEXICAL,
        weight=1.0,
    )
    return scores


def guard_nodes(
    nodes: Iterable[GraphNode], guard: RetrievalGuard | None
) -> tuple[tuple[GraphNode, ...], tuple[GuardExclusion, ...]]:
    accepted: list[GraphNode] = []
    excluded: list[GuardExclusion] = []
    for node in sorted(nodes, key=lambda item: item.id):
        reason = guard.exclusion_reason(node) if guard is not None else None
        if reason is None:
            accepted.append(node)
        else:
            excluded.append(GuardExclusion(node.id, reason))
    return tuple(accepted), tuple(excluded)


def _graph_spread(
    seeds: list[str],
    base_scores: dict[str, float],
    edges: Iterable[GraphEdge],
    node_ids: set[str],
    *,
    graph_depth: int,
    decay: float,
) -> tuple[dict[str, float], dict[str, float], dict[str, list[ScoreTrace]]]:
    adjacency: dict[str, list[tuple[str, GraphEdge]]] = defaultdict(list)
    for edge in edges:
        if edge.source_id not in node_ids or edge.target_id not in node_ids:
            continue
        adjacency[edge.source_id].append((edge.target_id, edge))
        adjacency[edge.target_id].append((edge.source_id, edge))
    for neighbors in adjacency.values():
        neighbors.sort(key=lambda item: (item[0], item[1].kind.value, item[1].id))

    graph_scores: dict[str, float] = defaultdict(float)
    warning_scores: dict[str, float] = defaultdict(float)
    traces: dict[str, list[ScoreTrace]] = defaultdict(list)
    for seed in seeds:
        frontier: list[
            tuple[str, float, int, tuple[str, ...], tuple[GraphEdge, ...], GraphEdge | None]
        ] = [(seed, base_scores[seed], 0, (seed,), (), None)]
        best: dict[
            tuple[str, bool], tuple[float, tuple[str, ...], tuple[GraphEdge, ...], GraphEdge | None]
        ] = {}
        while frontier:
            current, score, depth, path, path_edges, warning_edge = frontier.pop(0)
            if depth >= graph_depth:
                continue
            for neighbor, edge in adjacency.get(current, []):
                if neighbor in path:
                    continue
                propagated = score * decay * abs(edge.signed_weight) * EDGE_MULTIPLIER[edge.kind]
                next_warning = warning_edge or (edge if edge.is_warning else None)
                key = (neighbor, next_warning is not None)
                previous = best.get(key)
                if previous is not None and previous[0] >= propagated:
                    continue
                next_path = (*path, neighbor)
                next_edges = (*path_edges, edge)
                best[key] = (propagated, next_path, next_edges, next_warning)
                frontier.append(
                    (neighbor, propagated, depth + 1, next_path, next_edges, next_warning)
                )

        for (node_id, warning_path), (score, path, path_edges, warning_edge) in sorted(
            best.items(), key=lambda item: (item[0][0], item[0][1])
        ):
            if warning_path:
                warning_scores[node_id] += score
                assert warning_edge is not None
                traces[node_id].append(
                    ScoreTrace(
                        ScoreChannel.WARNING,
                        score,
                        f"surfaced by negative {warning_edge.kind.value} edge",
                        source_node_id=seed,
                        edge_id=warning_edge.id,
                        edge_kind=warning_edge.kind,
                        edge_polarity=warning_edge.polarity,
                        path=path,
                    )
                )
            else:
                graph_scores[node_id] += score
                last_edge = path_edges[-1]
                traces[node_id].append(
                    ScoreTrace(
                        ScoreChannel.GRAPH,
                        score,
                        f"propagated through typed {last_edge.kind.value} edge",
                        source_node_id=seed,
                        edge_id=last_edge.id,
                        edge_kind=last_edge.kind,
                        edge_polarity=last_edge.polarity,
                        path=path,
                    )
                )
    return dict(graph_scores), dict(warning_scores), traces


def retrieve(
    query: str,
    *,
    nodes: Iterable[GraphNode],
    edges: Iterable[GraphEdge],
    limit: int = 10,
    seed_limit: int = 8,
    graph_depth: int = 2,
    decay: float = 0.55,
    min_support_score: float = 0.15,
    min_margin: float = 0.0,
    guard: RetrievalGuard | None = None,
) -> RetrievalResult:
    if limit <= 0 or seed_limit <= 0:
        raise ValueError("limit and seed_limit must be positive")
    if graph_depth < 0:
        raise ValueError("graph_depth must be nonnegative")
    if not 0 <= decay <= 1:
        raise ValueError("decay must be in [0, 1]")
    if (
        not math.isfinite(min_support_score)
        or not math.isfinite(min_margin)
        or min_support_score < 0
        or min_margin < 0
    ):
        raise ValueError("abstention thresholds must be nonnegative")

    signals = index_signals(query)
    accepted, exclusions = guard_nodes(nodes, guard)
    if len({node.id for node in accepted}) != len(accepted):
        raise ValueError("node identifiers must be unique")
    if signals.empty:
        return RetrievalResult(
            signals, (), True, AbstentionReason.NO_INDEXABLE_SIGNALS, exclusions
        )

    node_map = {node.id: node for node in accepted}
    node_signals = {
        node.id: index_signals(node.title + " " + node.body) for node in accepted
    }
    lexical, lexical_traces = _channel_scores(
        signals.lexical_tokens,
        {node_id: item.lexical_tokens for node_id, item in node_signals.items()},
        channel=ScoreChannel.LEXICAL,
        weight=1.0,
    )
    symbols, symbol_traces = _channel_scores(
        signals.math_tokens,
        {node_id: item.math_tokens for node_id, item in node_signals.items()},
        channel=ScoreChannel.SYMBOL,
        weight=1.35,
    )
    formulas, formula_traces = _channel_scores(
        signals.formula_fingerprints,
        {node_id: item.formula_fingerprints for node_id, item in node_signals.items()},
        channel=ScoreChannel.FORMULA,
        weight=2.0,
    )
    base_scores = {
        node_id: lexical.get(node_id, 0.0)
        + symbols.get(node_id, 0.0)
        + formulas.get(node_id, 0.0)
        for node_id in node_map
    }
    base_scores = {node_id: score for node_id, score in base_scores.items() if score > 0}
    seeds = sorted(base_scores, key=lambda item: (-base_scores[item], item))[:seed_limit]
    graph, warnings, graph_traces = _graph_spread(
        seeds,
        base_scores,
        edges,
        set(node_map),
        graph_depth=graph_depth,
        decay=decay,
    )

    hits: list[SearchHit] = []
    for node_id, node in node_map.items():
        components = (
            lexical.get(node_id, 0.0),
            symbols.get(node_id, 0.0),
            formulas.get(node_id, 0.0),
            graph.get(node_id, 0.0),
            warnings.get(node_id, 0.0),
        )
        if not any(components):
            continue
        trace = tuple(
            sorted(
                chain(
                    lexical_traces.get(node_id, []),
                    symbol_traces.get(node_id, []),
                    formula_traces.get(node_id, []),
                    graph_traces.get(node_id, []),
                ),
                key=lambda item: (
                    item.channel.value,
                    item.detail,
                    item.source_node_id or "",
                    item.edge_id or "",
                    item.path,
                ),
            )
        )
        hits.append(SearchHit(node, *components, trace))
    ranked = tuple(sorted(hits, key=lambda hit: (-hit.total_score, hit.node.id))[:limit])
    if not ranked:
        return RetrievalResult(
            signals, (), True, AbstentionReason.NO_CANDIDATE_MATCH, exclusions
        )

    by_support = sorted(ranked, key=lambda hit: (-hit.support_score, hit.node.id))
    if by_support[0].support_score < min_support_score:
        return RetrievalResult(
            signals,
            ranked,
            True,
            AbstentionReason.BELOW_SUPPORT_THRESHOLD,
            exclusions,
        )
    if len(by_support) > 1:
        margin = by_support[0].support_score - by_support[1].support_score
        if margin < min_margin:
            return RetrievalResult(
                signals,
                ranked,
                True,
                AbstentionReason.AMBIGUOUS_TOP_MATCH,
                exclusions,
            )
    return RetrievalResult(signals, ranked, False, None, exclusions)


def search(
    query: str,
    *,
    nodes: Iterable[GraphNode],
    edges: Iterable[GraphEdge],
    limit: int = 10,
    seed_limit: int = 8,
    graph_depth: int = 2,
    decay: float = 0.55,
) -> list[SearchHit]:
    """Backward-compatible hit list; use :func:`retrieve` for abstention details."""

    result = retrieve(
        query,
        nodes=nodes,
        edges=edges,
        limit=limit,
        seed_limit=seed_limit,
        graph_depth=graph_depth,
        decay=decay,
        min_support_score=0.0,
    )
    return list(result.hits)
