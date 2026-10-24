"""A validated ambient status is judged the same before and after turn/completed.

Scheduled audit account03/B05, B05-R79-AMBIENT-EVENT-ORDER-SENSITIVE-ISOLATION-056: the three suppressed ambient
methods were inert before the turn completed and a policy violation one record later, by position alone. Their
payload checks still apply wherever they sit, and item, tool and active-status events after completion stay refused.
"""

import copy

import pytest

from test_codex_runner import audit, documented_clean_messages

AMBIENT = {
    "rate-limits": {
        "method": "account/rateLimits/updated",
        "params": {"rateLimits": {"limitId": "codex", "usedPercent": 1}},
    },
    "remote-control": {
        "method": "remoteControl/status/changed",
        "params": {
            "environmentId": None,
            "installationId": "installation-1",
            "serverName": "test-host",
            "status": "disabled",
        },
    },
    "mcp-startup": {
        "method": "mcpServer/startupStatus/updated",
        "params": {
            "error": None,
            "failureReason": None,
            "name": "developer-docs",
            "status": "ready",
            "threadId": "thread-1",
        },
    },
}


def _completion_index(messages: list[dict]) -> int:
    return next(i for i, m in enumerate(messages) if m.get("method") == "turn/completed")


def _placed(event: dict, *, after: bool) -> list[dict]:
    messages = documented_clean_messages()
    at = _completion_index(messages) + (1 if after else 0)
    messages.insert(at, copy.deepcopy(event))
    return messages


@pytest.mark.parametrize("name", sorted(AMBIENT))
def test_a_valid_ambient_status_is_judged_the_same_on_either_side_of_completion(name: str) -> None:
    before, after = audit(_placed(AMBIENT[name], after=False)), audit(_placed(AMBIENT[name], after=True))

    assert before.eligible and after.eligible
    assert before.reasons == after.reasons == ()


@pytest.mark.parametrize(
    ("name", "field", "value", "reason"),
    [
        ("remote-control", "status", "enabled", "unsafe_remote_control_status"),
        ("mcp-startup", "status", "failed", "unsafe_mcp_startup_status"),
        ("rate-limits", "unexpected", True, "malformed_rate_limit_status"),
    ],
)
def test_a_malformed_ambient_status_after_completion_is_still_refused(name, field, value, reason) -> None:
    event = copy.deepcopy(AMBIENT[name])
    event["params"][field] = value
    result = audit(_placed(event, after=True))

    assert not result.eligible
    assert reason in result.reasons


def test_item_and_active_status_events_after_completion_are_still_refused() -> None:
    item = {"method": "item/started", "params": {"threadId": "thread-1", "turnId": "turn-1", "item": {}}}
    active = {
        "method": "thread/status/changed",
        "params": {"threadId": "thread-1", "status": {"type": "active", "activeFlags": []}},
    }
    idle = {"method": "thread/status/changed", "params": {"threadId": "thread-1", "status": {"type": "idle"}}}

    assert "event_after_turn_completed:item/started" in audit(_placed(item, after=True)).reasons
    assert "non_idle_status_after_turn_completed" in audit(_placed(active, after=True)).reasons
    assert audit(_placed(idle, after=True)).eligible
