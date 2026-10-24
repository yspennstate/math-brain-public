"""A configuration can lower the solver-response budgets but not lift them past the repository ceilings.

Scheduled audit account04/B17, B17-R79-EVALUATION-RESPONSE-LIMITS-UNBOUNDED-20260929: only depth had a
ceiling, so 10**18 bytes, nodes and string bytes and a 1,001-digit integer bound were accepted and the
parser enforced them faithfully. The parser cases run on the plan built from the shipped configuration.
"""

import json

import pytest

import math_brain.evaluation as ev
from test_evaluation import (  # noqa: F401  (config and plan are fixtures)
    assert_malformed,
    codex_artifact_for_batch,
    config,
    plan,
    response_payload,
)

SHIPPED = {
    "maximum_bytes": 524288,
    "maximum_depth": 12,
    "maximum_nodes": 12000,
    "maximum_string_bytes": 16384,
    "maximum_integer_abs": 10**12,
}


def _limits(**changes: int) -> ev.ResponseLimits:
    return ev.ResponseLimits(**{**SHIPPED, **changes})


def _parse(plan: ev.EvaluationPlan, raw: str) -> ev.BatchResult:
    return ev.parse_batch_response(plan, pair_id=0, condition=ev.Condition.BRAIN_ON, raw=raw)


def test_the_shipped_limits_are_within_the_ceilings(config: ev.EvaluationConfig) -> None:
    assert config.response_limits.to_dict() == _limits().to_dict()


@pytest.mark.parametrize(
    ("field", "ceiling"),
    [
        ("maximum_bytes", ev.RESPONSE_BYTES_CEILING),
        ("maximum_nodes", ev.RESPONSE_NODES_CEILING),
        ("maximum_integer_abs", ev.RESPONSE_INTEGER_CEILING),
        ("maximum_depth", 64),
    ],
)
def test_each_ceiling_is_accepted_and_one_more_is_refused(field: str, ceiling: int) -> None:
    roomy = {"maximum_bytes": ev.RESPONSE_BYTES_CEILING}
    assert getattr(_limits(**{**roomy, field: ceiling}), field) == ceiling
    with pytest.raises(ValueError, match="may not exceed"):
        _limits(**{**roomy, field: ceiling + 1})


def test_a_string_or_node_budget_above_the_byte_budget_is_refused() -> None:
    assert _limits(maximum_bytes=1000, maximum_string_bytes=1000, maximum_nodes=1000)
    with pytest.raises(ValueError, match="string bytes may not exceed"):
        _limits(maximum_bytes=1000, maximum_string_bytes=1001, maximum_nodes=100)
    with pytest.raises(ValueError, match="nodes may not exceed"):
        _limits(maximum_bytes=1000, maximum_string_bytes=100, maximum_nodes=1001)


def test_the_audit_witness_configuration_is_refused() -> None:
    with pytest.raises(ValueError, match="may not exceed"):
        ev.ResponseLimits(
            maximum_bytes=10**18,
            maximum_depth=64,
            maximum_nodes=10**18,
            maximum_string_bytes=10**18,
            maximum_integer_abs=10**1000,
        )


def test_a_response_at_the_byte_budget_parses_and_one_byte_more_does_not(plan: ev.EvaluationPlan) -> None:
    text = json.dumps(response_payload(plan, 0, ev.Condition.BRAIN_ON, correct=True))
    room = plan.config.response_limits.maximum_bytes - len(text.encode("utf-8"))
    at_budget = _parse(plan, text + " " * room)

    assert ev.AttemptStatus.MALFORMED not in {attempt.status for attempt in at_budget.attempts}
    assert_malformed(_parse(plan, text + " " * (room + 1)), "byte_budget")


@pytest.mark.parametrize(
    ("padding", "code"),
    [
        (lambda limits: [0] * (limits.maximum_nodes + 1), "node_budget"),
        (lambda limits: "x" * (limits.maximum_string_bytes + 1), "string_budget"),
        (lambda limits: limits.maximum_integer_abs + 1, "integer_budget"),
    ],
    ids=["nodes", "string", "integer"],
)
def test_a_compact_payload_over_a_tree_budget_is_refused(plan: ev.EvaluationPlan, padding, code: str) -> None:
    limits = plan.config.response_limits
    payload = response_payload(plan, 0, ev.Condition.BRAIN_ON, correct=True)
    payload["padding"] = padding(limits)
    raw = json.dumps(payload, separators=(",", ":"))

    assert len(raw.encode("utf-8")) <= limits.maximum_bytes
    assert_malformed(_parse(plan, raw), code)


def test_an_oversized_codex_artifact_fails_closed_on_the_same_budget(plan: ev.EvaluationPlan) -> None:
    raw = "x" * (plan.config.response_limits.maximum_bytes + 1)
    artifact = codex_artifact_for_batch(plan, 0, ev.Condition.BRAIN_ON, raw)
    result, _runtime, _isolation = ev.parse_codex_artifact_response(
        plan, pair_id=0, condition=ev.Condition.BRAIN_ON, artifact=artifact
    )

    assert_malformed(result, "byte_budget")
