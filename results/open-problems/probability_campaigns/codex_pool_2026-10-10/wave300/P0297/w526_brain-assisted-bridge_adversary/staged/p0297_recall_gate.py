"""Proposed LQG relevance gate; does not certify truth or alter live recall.

Use only for a target query already identified as LQG/LFPP. Full mathematical
assumptions and source fidelity still require inspection after this filter.
"""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from typing import Any

_ANCHOR = re.compile(
    r"\b(?:lqg|lfpp)\b|liouville\s+(?:quantum\s+gravity|first[- ]passage\s+percolation)",
    re.IGNORECASE,
)


def filter_lqg_hits(hits: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Keep order, reject absent target anchors, and abstain on an empty result."""
    accepted = []
    for hit in hits:
        text = " ".join(str(hit.get(k) or "") for k in ("slug", "title", "text"))
        if _ANCHOR.search(text.replace("_", " ")):
            accepted.append(dict(hit))
    return {
        "accepted": accepted,
        "rejected_count": len(hits) - len(accepted),
        "abstained": not accepted,
        "reason": "no_lqg_anchor" if not accepted else "relevance_only_source_check_required",
    }
