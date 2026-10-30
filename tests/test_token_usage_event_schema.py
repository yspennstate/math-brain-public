"""thread/tokenUsage/updated is eligible only when its payload matches the app-server schema (fleet04/B14,
B14-R79-TOKEN-USAGE-PAYLOAD-UNVALIDATED-20260929-01; the auditor's T-R79-TOKEN-USAGE-EVENT-SCHEMA).

Until 30 Sep the runner checked only this event's thread and turn ids: a missing, scalar or extended payload kept the
stream eligible, before or after turn/completed. The schema is codex-cli 0.157.1's
(`codex app-server generate-json-schema`, v2/ThreadTokenUsageUpdatedNotification).
"""

import copy
import math

import pytest

from test_codex_runner import TOKEN_BREAKDOWN, VALID_TOKEN_USAGE, audit, documented_clean_messages

BOUND = {"threadId": "thread-1", "turnId": "turn-1"}


def stream(params: dict, *, position: str) -> list[dict]:
    """The clean transcript with its token-usage events replaced by one carrying `params`, placed just before
    or just after turn/completed."""
    messages = [m for m in documented_clean_messages() if m.get("method") != "thread/tokenUsage/updated"]
    completion = next(i for i, m in enumerate(messages) if m.get("method") == "turn/completed")
    event = {"method": "thread/tokenUsage/updated", "params": params}
    messages.insert(completion if position == "before" else completion + 1, event)
    return messages


def usage(**changes) -> dict:
    value = copy.deepcopy(VALID_TOKEN_USAGE)
    value.update(changes)
    return value


def breakdown(**changes) -> dict:
    value = dict(TOKEN_BREAKDOWN)
    value.update(changes)
    return value


VALID = {
    "the documented payload": {**BOUND, "tokenUsage": usage()},
    "no model context window": {**BOUND, "tokenUsage": {"last": breakdown(), "total": breakdown()}},
    "a null model context window": {**BOUND, "tokenUsage": usage(modelContextWindow=None)},
    "the optional cache-write counter": {**BOUND, "tokenUsage": usage(last=breakdown(cacheWriteInputTokens=4))},
}

MALFORMED = {
    "tokenUsage missing": dict(BOUND),
    "tokenUsage a string": {**BOUND, "tokenUsage": "not-an-object"},
    "tokenUsage a list": {**BOUND, "tokenUsage": [1, 2]},
    "tokenUsage null": {**BOUND, "tokenUsage": None},
    "tokenUsage empty": {**BOUND, "tokenUsage": {}},
    "an unknown top-level field": {**BOUND, "tokenUsage": usage(), "mcpToolCall": {"server": "x"}},
    "an unknown field in tokenUsage": {**BOUND, "tokenUsage": usage(extra=1)},
    "an unknown counter": {**BOUND, "tokenUsage": usage(last=breakdown(toolTokens=3))},
    "a required counter missing": {**BOUND, "tokenUsage": usage(total={k: v for k, v in TOKEN_BREAKDOWN.items()
                                                                       if k != "inputTokens"})},
    "a boolean counter": {**BOUND, "tokenUsage": usage(last=breakdown(outputTokens=True))},
    "a negative counter": {**BOUND, "tokenUsage": usage(last=breakdown(inputTokens=-1))},
    "a float counter": {**BOUND, "tokenUsage": usage(last=breakdown(inputTokens=1.5))},
    "a NaN counter": {**BOUND, "tokenUsage": usage(last=breakdown(inputTokens=math.nan))},
    "an infinite counter": {**BOUND, "tokenUsage": usage(total=breakdown(totalTokens=math.inf))},
    "a counter past int64": {**BOUND, "tokenUsage": usage(total=breakdown(totalTokens=2**63))},
    "a breakdown that is not an object": {**BOUND, "tokenUsage": usage(last=[0, 0])},
    "a string model context window": {**BOUND, "tokenUsage": usage(modelContextWindow="200000")},
    "a nested object where a counter goes": {**BOUND, "tokenUsage": usage(last=breakdown(inputTokens={"n": 1}))},
}


@pytest.mark.parametrize("position", ["before", "after"])
@pytest.mark.parametrize("label", sorted(VALID))
def test_a_schema_payload_stays_eligible(label: str, position: str) -> None:
    result = audit(stream(VALID[label], position=position))
    assert result.eligible, (label, position, result.reasons)


@pytest.mark.parametrize("position", ["before", "after"])
@pytest.mark.parametrize("label", sorted(MALFORMED))
def test_a_malformed_payload_makes_the_stream_ineligible(label: str, position: str) -> None:
    result = audit(stream(MALFORMED[label], position=position))
    assert not result.eligible, (label, position)
    assert "malformed_token_usage_status" in result.reasons, (label, position, result.reasons)


def test_the_id_binding_keeps_its_own_reason() -> None:
    result = audit(stream({"threadId": "foreign", "turnId": "turn-1", "tokenUsage": usage()}, position="after"))
    assert not result.eligible
    assert any(reason.startswith("foreign_thread_id") for reason in result.reasons), result.reasons
    assert "malformed_token_usage_status" not in result.reasons
