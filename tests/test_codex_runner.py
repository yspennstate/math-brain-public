import copy
import hashlib
import io
import json
import os
from dataclasses import replace
from pathlib import Path

import pytest

from math_brain import codex_runner as codex_runner_module
from math_brain.codex_runner import (
    AppServerProtocolError,
    CodexAppServerRunner,
    CodexRunConfig,
    CodexRunResult,
    DEFAULT_BASE_INSTRUCTIONS,
    DEFAULT_DEVELOPER_INSTRUCTIONS,
    app_server_command_tail_policy_digest,
    audit_app_server_messages,
    build_app_server_command,
    resolve_codex_executable,
    validate_probability,
)


# a thread/tokenUsage/updated payload of the app-server schema the runner validates (codex-cli 0.157.1)
TOKEN_BREAKDOWN = {"cachedInputTokens": 0, "inputTokens": 12, "outputTokens": 3, "reasoningOutputTokens": 1,
                   "totalTokens": 15}
VALID_TOKEN_USAGE = {"last": dict(TOKEN_BREAKDOWN), "total": dict(TOKEN_BREAKDOWN), "modelContextWindow": 200000}


SYNTHETIC_NATIVE_BYTES = (
    b"MZ\x00\x00math-brain-test-native"
    if os.name == "nt"
    else b"\x7fELFmath-brain-test-native"
)


def synthetic_executable_path(label: str = "codex-test") -> str:
    path = (
        Path(f"C:/math-brain-tests/{label}.exe")
        if os.name == "nt"
        else Path(f"/math-brain-tests/{label}")
    )
    return str(path)


def native_executable(tmp_path: Path) -> Path:
    binary_dir = tmp_path / "bin"
    binary_dir.mkdir()
    path = binary_dir / ("codex-test.exe" if os.name == "nt" else "codex-test")
    path.write_bytes(SYNTHETIC_NATIVE_BYTES)
    if os.name != "nt":
        path.chmod(0o700)
    return path.resolve()


def runtime_directory(tmp_path: Path) -> Path:
    path = tmp_path / "runtime"
    path.mkdir()
    return path.resolve()


def auth_file(tmp_path: Path, token: str = "test-auth-sentinel-0123456789") -> Path:
    path = tmp_path / "auth.json"
    path.write_text(json.dumps({"token": token}), encoding="utf-8")
    return path.resolve()


def sha256(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def encode_transcript(messages: list[dict]) -> bytes:
    return b"".join(
        json.dumps(
            message,
            allow_nan=False,
            ensure_ascii=True,
            separators=(",", ":"),
        ).encode("utf-8")
        + b"\n"
        for message in messages
    )


def encode_request(value: object) -> bytes:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def thread_start_request(
    *,
    base_instructions: str = DEFAULT_BASE_INSTRUCTIONS,
    developer_instructions: str = DEFAULT_DEVELOPER_INSTRUCTIONS,
) -> dict:
    return {
        "id": 2,
        "method": "thread/start",
        "params": {
            "allowProviderModelFallback": False,
            "approvalPolicy": "never",
            "baseInstructions": base_instructions,
            "cwd": str(Path.cwd().resolve()),
            "developerInstructions": developer_instructions,
            "dynamicTools": [],
            "environments": [],
            "ephemeral": True,
            "experimentalRawEvents": True,
            "model": "gpt-5.6-sol",
            "modelProvider": "openai",
            "personality": "none",
            "runtimeWorkspaceRoots": [],
            "sandbox": "read-only",
            "selectedCapabilityRoots": [],
        },
    }


def turn_start_request(*, prompt: str = "Solve the sealed test batch.") -> dict:
    return {
        "id": 3,
        "method": "turn/start",
        "params": {
            "approvalPolicy": "never",
            "effort": "ultra",
            "environments": [],
            "input": [{"text": prompt, "type": "text"}],
            "model": "gpt-5.6-sol",
            "outputSchema": {},
            "personality": "none",
            "threadId": "thread-1",
        },
    }


def thread_result(
    *,
    model: str = "gpt-5.6-sol",
    effort: str = "ultra",
    provider: str = "openai",
) -> dict:
    return {
        "model": model,
        "reasoningEffort": effort,
        "modelProvider": provider,
        "thread": {"id": "thread-1"},
    }


def completed_messages(
    *, phase: str | None = "final_answer", text: object = "{}"
) -> list[dict]:
    return [
        {
            "method": "item/completed",
            "params": {
                "item": {
                    "id": "message-1",
                    "type": "agentMessage",
                    "phase": phase,
                    "text": text,
                },
                "threadId": "thread-1",
                "turnId": "turn-1",
            },
        },
        {
            "method": "turn/completed",
            "params": {
                "threadId": "thread-1",
                "turn": {"id": "turn-1", "status": "completed", "items": []},
            },
        },
    ]


def documented_clean_messages() -> list[dict]:
    bound = {"threadId": "thread-1", "turnId": "turn-1"}
    return [
        {
            "method": "thread/started",
            "params": {"thread": {"id": "thread-1"}},
        },
        {
            "method": "thread/status/changed",
            "params": {
                "threadId": "thread-1",
                "status": {"type": "active", "activeFlags": []},
            },
        },
        {
            "method": "turn/started",
            "params": {
                "threadId": "thread-1",
                "turn": {"id": "turn-1", "status": "inProgress", "items": []},
            },
        },
        {
            "method": "rawResponseItem/completed",
            "params": {
                **bound,
                "item": {
                    "type": "message",
                    "role": "developer",
                    "content": [
                        {"type": "input_text", "text": DEFAULT_BASE_INSTRUCTIONS},
                        {
                            "type": "input_text",
                            "text": DEFAULT_DEVELOPER_INSTRUCTIONS,
                        },
                    ],
                },
            },
        },
        {
            "method": "rawResponseItem/completed",
            "params": {
                **bound,
                "item": {
                    "type": "message",
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": "Solve the sealed test batch."}
                    ],
                },
            },
        },
        {
            "method": "item/started",
            "params": {
                **bound,
                "item": {"id": "user-1", "type": "userMessage"},
            },
        },
        {
            "method": "item/completed",
            "params": {
                **bound,
                "item": {"id": "user-1", "type": "userMessage"},
            },
        },
        {
            "method": "item/started",
            "params": {
                **bound,
                "item": {"id": "reasoning-1", "type": "reasoning"},
            },
        },
        {
            "method": "item/reasoning/summaryPartAdded",
            "params": {**bound, "itemId": "reasoning-1", "summaryIndex": 0},
        },
        {
            "method": "item/reasoning/summaryTextDelta",
            "params": {
                **bound,
                "itemId": "reasoning-1",
                "summaryIndex": 0,
                "delta": "checking",
            },
        },
        {
            "method": "item/reasoning/textDelta",
            "params": {
                **bound,
                "itemId": "reasoning-1",
                "contentIndex": 0,
                "delta": "internal",
            },
        },
        {
            "method": "rawResponseItem/completed",
            "params": {**bound, "item": {"type": "reasoning", "summary": []}},
        },
        {
            "method": "item/completed",
            "params": {
                **bound,
                "item": {"id": "reasoning-1", "type": "reasoning"},
            },
        },
        {
            "method": "item/started",
            "params": {
                **bound,
                "item": {"id": "message-1", "type": "agentMessage"},
            },
        },
        {
            "method": "item/agentMessage/delta",
            "params": {**bound, "itemId": "message-1", "delta": "{}"},
        },
        {
            "method": "rawResponseItem/completed",
            "params": {
                **bound,
                "item": {
                    "type": "message",
                    "role": "assistant",
                    "content": [],
                },
            },
        },
        *completed_messages(),
        {
            "method": "thread/tokenUsage/updated",
            "params": {**bound, "tokenUsage": copy.deepcopy(VALID_TOKEN_USAGE)},
        },
        {
            "method": "thread/status/changed",
            "params": {"threadId": "thread-1", "status": {"type": "idle"}},
        },
    ]


def audit(messages: list[dict], *, result: dict | None = None):
    return audit_app_server_messages(
        messages,
        requested_model="gpt-5.6-sol",
        requested_effort="ultra",
        requested_provider="openai",
        expected_thread_id="thread-1",
        expected_turn_id="turn-1",
        thread_start_result=result or thread_result(),
        process_exit_code=0,
        forced_termination=False,
        expected_model_inputs=(
            ("developer", DEFAULT_BASE_INSTRUCTIONS),
            ("developer", DEFAULT_DEVELOPER_INSTRUCTIONS),
            ("user", "Solve the sealed test batch."),
        ),
    )


def complete_transcript_messages(
    *, prompt: str = "Solve the sealed test batch."
) -> list[dict]:
    return [
        {"id": 1, "result": {"userAgent": "test"}},
        {
            "method": "thread/started",
            "params": {"thread": {"id": "thread-1"}},
        },
        {"id": 2, "result": thread_result()},
        {"id": 3, "result": {"turn": {"id": "turn-1"}}},
        {
            "method": "turn/started",
            "params": {
                "threadId": "thread-1",
                "turn": {"id": "turn-1", "items": [], "status": "inProgress"},
            },
        },
        {
            "method": "rawResponseItem/completed",
            "params": {
                "threadId": "thread-1",
                "turnId": "turn-1",
                "item": {
                    "type": "message",
                    "role": "developer",
                    "content": [
                        {"type": "input_text", "text": DEFAULT_BASE_INSTRUCTIONS},
                        {
                            "type": "input_text",
                            "text": DEFAULT_DEVELOPER_INSTRUCTIONS,
                        },
                    ],
                },
            },
        },
        {
            "method": "rawResponseItem/completed",
            "params": {
                "threadId": "thread-1",
                "turnId": "turn-1",
                "item": {
                    "type": "message",
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": prompt}
                    ],
                },
            },
        },
        {
            "method": "item/started",
            "params": {
                "item": {"id": "message-1", "type": "agentMessage"},
                "threadId": "thread-1",
                "turnId": "turn-1",
            },
        },
        *completed_messages(),
    ]


def result_kwargs(
    messages: list[dict] | None = None, *, stderr: bytes = b"diagnostic\n"
) -> dict:
    materialized = messages if messages is not None else complete_transcript_messages()
    transcript = encode_transcript(materialized)
    executable_path = synthetic_executable_path()
    return {
        "requested_model": "gpt-5.6-sol",
        "requested_effort": "ultra",
        "requested_provider": "openai",
        "prompt_text": "Solve the sealed test batch.",
        "output_schema_json": b"{}",
        "launch_command_json": encode_request(
            [
                executable_path,
                *codex_runner_module._app_server_command_tail(
                    "gpt-5.6-sol",
                    "ultra",
                ),
            ]
        ),
        "executable_path": executable_path,
        "executable_size_bytes": len(SYNTHETIC_NATIVE_BYTES),
        "executable_sha256_digest": sha256(SYNTHETIC_NATIVE_BYTES),
        "executable_lock_enforced": True,
        "standard_popen_used": True,
        "solver_process_isolation_policy_digest": (
            codex_runner_module.solver_process_isolation_policy_digest()
        ),
        "codex_home_directory_device": 2,
        "codex_home_directory_inode": 3,
        "codex_home_initial_auth_only": True,
        "codex_home_cleanup_verified": True,
        "credential_leak_scan_passed": True,
        "command_tail_policy_digest": app_server_command_tail_policy_digest(
            "gpt-5.6-sol",
            "ultra",
        ),
        "initialize_request_json": codex_runner_module.locked_initialize_request_json(),
        "initialized_notification_json": encode_request(
            {"method": "initialized", "params": {}}
        ),
        "thread_start_request_json": encode_request(thread_start_request()),
        "turn_start_request_json": encode_request(turn_start_request()),
        "execution_nonce": "0" * 64,
        "timeout_seconds": 180,
        "runtime_directory_device": 1,
        "runtime_directory_inode": 1,
        "thread_id": "thread-1",
        "turn_id": "turn-1",
        "output_text": "{}",
        "messages": tuple(materialized),
        "transcript_jsonl": transcript,
        "transcript_hash": sha256(transcript),
        "stderr_bytes": stderr,
        "stderr_hash": sha256(stderr),
        "stderr_excerpt": stderr.decode("utf-8", errors="replace")[-4_000:],
        "process_exit_code": 0,
        "forced_termination": False,
        "elapsed_seconds": 1.25,
        "audit": audit(materialized),
    }


def test_config_requires_an_empty_absolute_runtime_directory(tmp_path: Path) -> None:
    config = CodexRunConfig(tmp_path)
    config.validate_runtime()
    (tmp_path / "unexpected.txt").write_text("x", encoding="utf-8")
    with pytest.raises(ValueError, match="empty"):
        config.validate_runtime()


@pytest.mark.parametrize("field", ["model", "effort", "model_provider"])
def test_config_rejects_selector_injection(tmp_path: Path, field: str) -> None:
    values = {"cwd": tmp_path, field: 'x" -c shell_tool=true'}
    with pytest.raises(ValueError, match="unsafe"):
        CodexRunConfig(**values)


@pytest.mark.parametrize(
    "field",
    [
        "timeout_seconds",
        "max_event_line_bytes",
        "max_transcript_bytes",
        "max_stderr_bytes",
    ],
)
@pytest.mark.parametrize("value", [True, 1.0, float("nan"), float("inf"), "4096"])
def test_config_resource_fields_require_exact_integers(
    tmp_path: Path, field: str, value: object
) -> None:
    values = {"cwd": tmp_path, field: value}
    with pytest.raises(ValueError, match="exact integer"):
        CodexRunConfig(**values)


def test_command_fixes_model_effort_isolation_and_no_tool_features(
    tmp_path: Path,
) -> None:
    executable = native_executable(tmp_path)
    command = build_app_server_command(
        CodexRunConfig(tmp_path, executable=str(executable))
    )
    assert command[0] == str(executable)
    joined = " ".join(command)
    assert 'model="gpt-5.6-sol"' in command
    assert 'model_reasoning_effort="ultra"' in command
    assert 'approval_policy="never"' in command
    assert 'sandbox_mode="read-only"' in command
    assert 'web_search="disabled"' in command
    assert "project_doc_max_bytes=0" in command
    assert "project_doc_fallback_filenames=[]" in command
    assert 'history.persistence="none"' in command
    for feature in ("shell_tool", "multi_agent", "plugins", "hooks", "memories"):
        index = command.index(feature)
        assert command[index - 1] == "--disable"
    assert "danger-full-access" not in joined


def test_resolver_fails_when_no_cli_is_present(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("math_brain.codex_runner.shutil.which", lambda _: None)
    with pytest.raises(RuntimeError, match="native Codex executable was not found"):
        resolve_codex_executable()


def test_config_and_resolver_reject_relative_or_shim_executables(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="absolute path"):
        CodexRunConfig(tmp_path, executable="codex.cmd")

    shim = tmp_path / "codex.cmd"
    shim.write_text("@echo off\r\nnode codex.js %*\r\n", encoding="ascii")
    if os.name != "nt":
        shim.chmod(0o700)
    with pytest.raises(AppServerProtocolError, match="native"):
        resolve_codex_executable(str(shim.resolve()))


def test_clean_event_stream_is_eligible_but_model_identity_is_unverified() -> None:
    result = audit(documented_clean_messages())
    assert result.eligible
    assert not result.model_identity_verified
    assert result.accepted_model == "gpt-5.6-sol"
    assert result.final_message_count == 1


def test_documented_lifecycle_token_raw_and_delta_events_are_eligible() -> None:
    result = audit(documented_clean_messages())
    assert result.eligible, result.reasons


@pytest.mark.parametrize(
    ("item_type", "reason"),
    [
        ("commandExecution", "forbidden_item:commandExecution"),
        ("mcpToolCall", "forbidden_item:mcpToolCall"),
        ("collabAgentToolCall", "forbidden_item:collabAgentToolCall"),
        ("subAgentActivity", "forbidden_item:subAgentActivity"),
        ("webSearch", "forbidden_item:webSearch"),
    ],
)
def test_tool_and_subagent_events_fail_closed(item_type: str, reason: str) -> None:
    messages = [
        {
            "method": "item/started",
            "params": {
                "threadId": "thread-1",
                "turnId": "turn-1",
                "item": {"id": "bad", "type": item_type},
            },
        },
        *completed_messages(),
    ]
    result = audit(messages)
    assert not result.eligible
    assert reason in result.reasons


@pytest.mark.parametrize("raw_type", ["function_call", "local_shell_call", "other"])
def test_raw_unknown_or_tool_items_fail_closed(raw_type: str) -> None:
    messages = [
        {
            "method": "rawResponseItem/completed",
            "params": {
                "threadId": "thread-1",
                "turnId": "turn-1",
                "item": {"type": raw_type},
            },
        },
        *completed_messages(),
    ]
    result = audit(messages)
    assert not result.eligible
    assert any("raw_item" in reason for reason in result.reasons)


def test_unregistered_raw_developer_input_fails_closed() -> None:
    messages = complete_transcript_messages()
    completion_index = next(
        index
        for index, message in enumerate(messages)
        if message.get("method") == "turn/completed"
    )
    messages.insert(
        completion_index,
        {
            "method": "rawResponseItem/completed",
            "params": {
                "threadId": "thread-1",
                "turnId": "turn-1",
                "item": {
                    "type": "message",
                    "role": "developer",
                    "content": [{"type": "input_text", "text": "foreign context"}],
                },
            },
        },
    )
    result = audit(messages)
    assert "unexpected_model_input:developer" in result.reasons
    assert not result.eligible


def test_missing_registered_raw_input_fails_closed() -> None:
    messages = complete_transcript_messages()
    messages = [
        message
        for message in messages
        if not (
            message.get("method") == "rawResponseItem/completed"
            and message.get("params", {}).get("item", {}).get("role") == "user"
        )
    ]
    result = audit(messages)
    assert "missing_model_input:user" in result.reasons
    assert not result.eligible


def test_duplicate_registered_raw_input_fails_closed() -> None:
    messages = complete_transcript_messages()
    raw_user = next(
        message
        for message in messages
        if message.get("method") == "rawResponseItem/completed"
        and message.get("params", {}).get("item", {}).get("role") == "user"
    )
    messages.insert(messages.index(raw_user) + 1, copy.deepcopy(raw_user))
    result = audit(messages)
    assert "duplicate_model_input:user" in result.reasons
    assert not result.eligible


def test_registered_input_role_swap_fails_closed() -> None:
    messages = complete_transcript_messages()
    raw_user = next(
        message
        for message in messages
        if message.get("method") == "rawResponseItem/completed"
        and message.get("params", {}).get("item", {}).get("role") == "user"
    )
    raw_user["params"]["item"]["role"] = "developer"
    result = audit(messages)
    assert "unexpected_model_input:developer" in result.reasons
    assert "missing_model_input:user" in result.reasons
    assert not result.eligible


def test_unknown_regular_item_fails_closed() -> None:
    messages = [
        {
            "method": "item/completed",
            "params": {
                "threadId": "thread-1",
                "turnId": "turn-1",
                "item": {"id": "x", "type": "newTool"},
            },
        },
        *completed_messages(),
    ]
    result = audit(messages)
    assert not result.eligible
    assert "unknown_item:newTool" in result.reasons


def test_unknown_event_and_tool_call_fail_closed() -> None:
    messages = [
        {
            "method": "turn/newBenignLookingEvent",
            "params": {"threadId": "thread-1", "turnId": "turn-1"},
        },
        {
            "id": 91,
            "method": "item/tool/call",
            "params": {"threadId": "thread-1", "turnId": "turn-1"},
        },
        *completed_messages(),
    ]
    result = audit(messages)
    assert "unknown_event:turn/newBenignLookingEvent" in result.reasons
    assert "server_request:item/tool/call" in result.reasons
    assert "unknown_event:item/tool/call" in result.reasons


def test_current_ambient_status_events_are_inert_and_tightly_validated() -> None:
    remote = {
        "method": "remoteControl/status/changed",
        "params": {
            "environmentId": None,
            "installationId": "installation-1",
            "serverName": "test-host",
            "status": "disabled",
        },
    }
    mcp = {
        "method": "mcpServer/startupStatus/updated",
        "params": {
            "error": None,
            "failureReason": None,
            "name": "developer-docs",
            "status": "ready",
            "threadId": "thread-1",
        },
    }
    rate_limits = {
        "method": "account/rateLimits/updated",
        "params": {"rateLimits": {"limitId": "codex", "usedPercent": 1}},
    }
    messages = documented_clean_messages()
    messages.insert(0, remote)
    messages.insert(2, mcp)
    completion_index = next(
        index
        for index, message in enumerate(messages)
        if message.get("method") == "turn/completed"
    )
    messages.insert(completion_index, rate_limits)
    assert audit(messages).eligible

    remote_enabled = copy.deepcopy(messages)
    remote_enabled[0]["params"]["status"] = "enabled"
    assert "unsafe_remote_control_status" in audit(remote_enabled).reasons

    mcp_failed = copy.deepcopy(messages)
    mcp_failed[2]["params"]["status"] = "failed"
    assert "unsafe_mcp_startup_status" in audit(mcp_failed).reasons

    foreign_mcp = copy.deepcopy(messages)
    foreign_mcp[2]["params"]["threadId"] = "foreign"
    assert (
        "foreign_thread_id:mcpServer/startupStatus/updated"
        in audit(foreign_mcp).reasons
    )

    malformed_rate_limits = copy.deepcopy(messages)
    next(
        message
        for message in malformed_rate_limits
        if message.get("method") == "account/rateLimits/updated"
    )["params"]["unexpected"] = True
    assert "malformed_rate_limit_status" in audit(malformed_rate_limits).reasons

    unknown_mcp = [
        {"method": "mcpServer/tool/called", "params": {}},
        *completed_messages(),
    ]
    assert "forbidden_event:mcpServer/tool/called" in audit(unknown_mcp).reasons


def test_model_reroute_fails_even_if_accepted_configuration_matched() -> None:
    messages = [
        {
            "method": "model/rerouted",
            "params": {
                "fromModel": "gpt-5.6-sol",
                "toModel": "fallback",
                "reason": {"type": "unavailable"},
                "threadId": "thread-1",
                "turnId": "turn-1",
            },
        },
        *completed_messages(),
    ]
    result = audit(messages)
    assert not result.eligible
    assert "model_rerouted" in result.reasons
    assert result.reroutes[0][:2] == ("gpt-5.6-sol", "fallback")


@pytest.mark.parametrize(
    ("result", "reason"),
    [
        (thread_result(model="fallback"), "accepted_model_mismatch"),
        (thread_result(effort="high"), "accepted_effort_mismatch"),
        (thread_result(provider="other"), "accepted_provider_mismatch"),
        (
            {**thread_result(), "thread": {"id": "foreign"}},
            "accepted_thread_id_mismatch",
        ),
    ],
)
def test_accepted_configuration_or_thread_mismatch_fails(
    result: dict, reason: str
) -> None:
    checked = audit(completed_messages(), result=result)
    assert not checked.eligible
    assert reason in checked.reasons


def test_server_request_and_hook_event_fail_closed() -> None:
    messages = [
        {"id": 91, "method": "tool/requestUserInput", "params": {}},
        {"method": "hook/started", "params": {}},
        *completed_messages(),
    ]
    result = audit(messages)
    assert not result.eligible
    assert "server_request:tool/requestUserInput" in result.reasons
    assert "forbidden_event:hook/started" in result.reasons


def test_missing_duplicate_or_failed_completion_is_ineligible() -> None:
    missing = audit(completed_messages()[:-1])
    duplicate_messages = completed_messages()
    duplicate_messages.append(copy.deepcopy(duplicate_messages[-1]))
    duplicate = audit(duplicate_messages)
    failed = completed_messages()
    failed[1]["params"]["turn"]["status"] = "failed"
    assert "missing_turn_completed" in missing.reasons
    assert "turn_completed_cardinality" in duplicate.reasons
    assert "turn_not_completed" in audit(failed).reasons


def test_extra_unphased_agent_message_is_not_hidden_by_a_phased_message() -> None:
    messages = completed_messages()
    messages.insert(0, completed_messages(phase=None)[0])
    result = audit(messages)
    assert "final_message_cardinality" in result.reasons
    assert result.final_message_count == 2


def test_final_message_must_precede_turn_completion() -> None:
    messages = completed_messages()
    messages.reverse()
    result = audit(messages)
    assert "final_message_not_before_turn_completed" in result.reasons
    assert "event_after_turn_completed:item/completed" in result.reasons
    assert not result.eligible


def test_orphan_delta_and_pre_turn_item_are_ineligible() -> None:
    orphan = documented_clean_messages()
    orphan.insert(
        -2,
        {
            "method": "item/agentMessage/delta",
            "params": {
                "delta": "forged",
                "itemId": "never-started",
                "threadId": "thread-1",
                "turnId": "turn-1",
            },
        },
    )
    assert "delta_without_active_item" in audit(orphan).reasons

    pre_turn = documented_clean_messages()
    turn_start_index = next(
        index for index, message in enumerate(pre_turn)
        if message.get("method") == "turn/started"
    )
    reasoning_start = next(
        index for index, message in enumerate(pre_turn)
        if message.get("method") == "item/started"
        and message["params"]["item"]["type"] == "reasoning"
    )
    pre_turn.insert(turn_start_index, pre_turn.pop(reasoning_start))
    assert "turn_bound_event_outside_lifecycle" in audit(pre_turn).reasons


def test_only_idle_status_may_follow_turn_completion() -> None:
    messages = documented_clean_messages()
    messages[-1]["params"]["status"] = {"activeFlags": [], "type": "active"}
    result = audit(messages)
    assert "non_idle_status_after_turn_completed" in result.reasons
    assert not result.eligible


def test_non_string_final_message_text_is_ineligible() -> None:
    result = audit(completed_messages(text={"not": "text"}))
    assert "final_message_text_not_string" in result.reasons


@pytest.mark.parametrize(
    "foreign_event",
    [
        {
            "method": "thread/started",
            "params": {"thread": {"id": "foreign"}},
        },
        {
            "method": "thread/status/changed",
            "params": {"threadId": "foreign", "status": {"type": "idle"}},
        },
        {
            "method": "turn/started",
            "params": {
                "threadId": "thread-1",
                "turn": {"id": "foreign", "status": "inProgress"},
            },
        },
        {
            "method": "thread/tokenUsage/updated",
            "params": {
                "threadId": "thread-1",
                "turnId": "foreign",
                "tokenUsage": copy.deepcopy(VALID_TOKEN_USAGE),
            },
        },
        {
            "method": "item/agentMessage/delta",
            "params": {
                "threadId": "foreign",
                "turnId": "turn-1",
                "itemId": "message-1",
                "delta": "x",
            },
        },
        {
            "method": "rawResponseItem/completed",
            "params": {
                "threadId": "thread-1",
                "turnId": "foreign",
                "item": {"type": "reasoning"},
            },
        },
    ],
)
def test_foreign_or_unbound_events_fail_closed(foreign_event: dict) -> None:
    result = audit([foreign_event, *completed_messages()])
    assert not result.eligible
    assert any(reason.startswith("foreign_") for reason in result.reasons)


def test_wrong_completion_ids_do_not_match_the_expected_turn() -> None:
    completion = completed_messages()[-1]
    wrong_thread = copy.deepcopy(completion)
    wrong_thread["params"]["threadId"] = "foreign"
    wrong_turn = copy.deepcopy(completion)
    wrong_turn["params"]["turn"]["id"] = "foreign"
    assert not codex_runner_module._is_expected_turn_completion(
        wrong_thread, expected_thread_id="thread-1", expected_turn_id="turn-1"
    )
    assert not codex_runner_module._is_expected_turn_completion(
        wrong_turn, expected_thread_id="thread-1", expected_turn_id="turn-1"
    )
    assert codex_runner_module._is_expected_turn_completion(
        completion, expected_thread_id="thread-1", expected_turn_id="turn-1"
    )


def test_run_result_deep_freezes_transcript_derived_messages() -> None:
    messages = complete_transcript_messages()
    result = CodexRunResult(**result_kwargs(messages))
    messages[-2]["params"]["item"]["text"] = "mutated later"
    assert result.output_text == "{}"
    assert result.messages[-2]["params"]["item"]["text"] == "{}"
    with pytest.raises(TypeError):
        result.messages[-2]["params"]["item"]["text"] = "mutation"


def test_run_result_rejects_messages_that_do_not_match_transcript() -> None:
    kwargs = result_kwargs()
    supplied = [copy.deepcopy(message) for message in kwargs["messages"]]
    supplied[-2]["params"]["item"]["text"] = "different"
    kwargs["messages"] = tuple(supplied)
    with pytest.raises(AppServerProtocolError, match="messages do not match"):
        CodexRunResult(**kwargs)


@pytest.mark.parametrize("hash_field", ["transcript_hash", "stderr_hash"])
def test_run_result_rejects_artifact_hash_mismatch(hash_field: str) -> None:
    kwargs = result_kwargs()
    kwargs[hash_field] = "sha256:" + "0" * 64
    with pytest.raises(AppServerProtocolError, match="hash does not match"):
        CodexRunResult(**kwargs)


def test_run_result_binds_canonical_request_artifacts() -> None:
    wrong_schema = result_kwargs()
    wrong_schema["output_schema_json"] = b'{"z":1, "a":2}'
    with pytest.raises(AppServerProtocolError, match="not canonical"):
        CodexRunResult(**wrong_schema)
    missing_prompt = result_kwargs()
    missing_prompt["prompt_text"] = "  "
    with pytest.raises(AppServerProtocolError, match="prompt artifact"):
        CodexRunResult(**missing_prompt)

    duplicate_schema = result_kwargs()
    duplicate_schema["output_schema_json"] = b'{"answer":1,"answer":2}'
    with pytest.raises(AppServerProtocolError, match="output-schema artifact is invalid"):
        CodexRunResult(**duplicate_schema)

    altered_launch = result_kwargs()
    launch = json.loads(altered_launch["launch_command_json"])
    launch.pop()
    altered_launch["launch_command_json"] = encode_request(launch)
    with pytest.raises(AppServerProtocolError, match="locked no-tool policy"):
        CodexRunResult(**altered_launch)

    altered_initialize = result_kwargs()
    initialize = json.loads(altered_initialize["initialize_request_json"])
    initialize["params"]["capabilities"] = {}
    altered_initialize["initialize_request_json"] = encode_request(initialize)
    with pytest.raises(AppServerProtocolError, match="locked protocol"):
        CodexRunResult(**altered_initialize)


def test_run_result_rejects_duplicate_keys_in_transcript() -> None:
    kwargs = result_kwargs()
    transcript = kwargs["transcript_jsonl"].replace(
        b'{"id":1,',
        b'{"id":1,"id":1,',
        1,
    )
    kwargs["transcript_jsonl"] = transcript
    kwargs["transcript_hash"] = sha256(transcript)
    with pytest.raises(AppServerProtocolError, match="invalid app-server JSONL transcript"):
        CodexRunResult(**kwargs)


@pytest.mark.parametrize(
    ("field", "value", "match"),
    [
        ("thread_id", "foreign", "turn/start request differs"),
        ("turn_id", "foreign", "turn_id does not match"),
        ("output_text", "asserted", "output_text does not match"),
        ("stderr_excerpt", "asserted", "stderr excerpt does not match"),
    ],
)
def test_run_result_validates_derived_ids_and_text(
    field: str, value: object, match: str
) -> None:
    kwargs = result_kwargs()
    kwargs[field] = value
    with pytest.raises(AppServerProtocolError, match=match):
        CodexRunResult(**kwargs)


def test_run_result_rejects_asserted_audit_mismatch() -> None:
    kwargs = result_kwargs()
    kwargs["audit"] = replace(kwargs["audit"], final_message_count=99)
    with pytest.raises(AppServerProtocolError, match="audit does not match"):
        CodexRunResult(**kwargs)


def test_run_result_rejects_foreign_or_duplicate_protocol_response_ids() -> None:
    foreign = complete_transcript_messages()
    foreign.insert(1, {"id": 4, "result": {}})
    with pytest.raises(AppServerProtocolError, match="foreign response id"):
        CodexRunResult(**result_kwargs(foreign))

    duplicate = complete_transcript_messages()
    duplicate.insert(1, {"id": 1, "result": {}})
    with pytest.raises(AppServerProtocolError, match="duplicate response id"):
        CodexRunResult(**result_kwargs(duplicate))

    reordered = complete_transcript_messages()
    response_indices = [
        index for index, message in enumerate(reordered)
        if message.get("id") in {1, 2, 3} and "method" not in message
    ]
    responses = [reordered[index] for index in response_indices]
    for index, response in zip(response_indices, reversed(responses), strict=True):
        reordered[index] = response
    with pytest.raises(AppServerProtocolError, match="request causality"):
        CodexRunResult(**result_kwargs(reordered))


@pytest.mark.parametrize("nonce", [None, 7, b"0" * 64, "A" * 64, "0" * 63])
def test_run_result_rejects_noncanonical_execution_nonce(nonce: object) -> None:
    kwargs = result_kwargs()
    kwargs["execution_nonce"] = nonce
    with pytest.raises(AppServerProtocolError, match="execution nonce"):
        CodexRunResult(**kwargs)


def test_locally_asserted_nonce_cannot_mint_a_new_protocol_identity() -> None:
    first = CodexRunResult(**result_kwargs())
    second_kwargs = result_kwargs()
    second_kwargs["execution_nonce"] = "f" * 64
    second = CodexRunResult(**second_kwargs)
    assert first.protocol_execution_id == second.protocol_execution_id


def test_local_attempt_metadata_cannot_mint_a_new_protocol_identity() -> None:
    first = CodexRunResult(**result_kwargs())
    changed = result_kwargs(stderr=b"different local diagnostic\n")
    changed.update(
        {
            "elapsed_seconds": 0.0,
            "execution_nonce": "f" * 64,
            "runtime_directory_device": 987,
            "runtime_directory_inode": 654,
            "timeout_seconds": 999,
        }
    )
    second = CodexRunResult(**changed)
    assert first.protocol_execution_id == second.protocol_execution_id


def test_launcher_and_cwd_alias_cannot_mint_a_new_protocol_identity() -> None:
    first = CodexRunResult(**result_kwargs())
    changed = result_kwargs()
    launch = json.loads(changed["launch_command_json"])
    launch[0] = synthetic_executable_path("another-codex")
    changed["launch_command_json"] = encode_request(launch)
    changed["executable_path"] = launch[0]
    request = json.loads(changed["thread_start_request_json"])
    request["params"]["cwd"] = str(
        Path(request["params"]["cwd"]).parent / "another-empty-runtime"
    )
    changed["thread_start_request_json"] = encode_request(request)
    second = CodexRunResult(**changed)
    assert first.protocol_execution_id == second.protocol_execution_id


def test_run_result_rejects_command_zero_not_bound_to_executable_provenance() -> None:
    changed = result_kwargs()
    launch = json.loads(changed["launch_command_json"])
    launch[0] = synthetic_executable_path("fake-command-zero")
    changed["launch_command_json"] = encode_request(launch)
    with pytest.raises(AppServerProtocolError, match="locked no-tool policy"):
        CodexRunResult(**changed)


def test_run_result_rejects_forged_command_tail_policy_digest() -> None:
    changed = result_kwargs()
    changed["command_tail_policy_digest"] = "sha256:" + "0" * 64
    with pytest.raises(AppServerProtocolError, match="command-tail policy digest"):
        CodexRunResult(**changed)


class MissingPipeProcess:
    def __init__(self) -> None:
        self.stdin = None
        self.stdout = None
        self.stderr = None
        self.returncode: int | None = None
        self.kill_calls = 0
        self.wait_calls = 0

    def kill(self) -> None:
        self.kill_calls += 1

    def wait(self, timeout: float | None = None) -> int:
        self.wait_calls += 1
        self.returncode = -9
        return self.returncode


class ScriptedProcess:
    def __init__(self, messages: list[dict], *, stderr: bytes = b"") -> None:
        self.stdin = io.BytesIO()
        self.stdout = io.BytesIO(encode_transcript(messages))
        self.stderr = io.BytesIO(stderr)
        self.returncode: int | None = 0
        self.kill_calls = 0
        self.terminate_calls = 0
        self.wait_calls = 0

    def kill(self) -> None:
        self.kill_calls += 1
        self.returncode = -9

    def terminate(self) -> None:
        self.terminate_calls += 1
        self.returncode = -15

    def wait(self, timeout: float | None = None) -> int:
        self.wait_calls += 1
        assert self.returncode is not None
        return self.returncode


class KeepBytesIO(io.BytesIO):
    def close(self) -> None:
        pass


def test_standard_runner_uses_sterile_home_and_scrubbed_environment(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    process = ScriptedProcess(complete_transcript_messages(prompt="prove it"))
    executable = native_executable(tmp_path)
    runtime = runtime_directory(tmp_path)
    auth = auth_file(tmp_path)
    observed_home: Path | None = None
    parent_environment = dict(os.environ)

    def factory(*args: object, **kwargs: object) -> ScriptedProcess:
        nonlocal observed_home
        environment = kwargs["env"]
        assert isinstance(environment, dict)
        assert tuple(sorted(environment)) == tuple(
            sorted(codex_runner_module.SOLVER_CHILD_ENVIRONMENT_NAMES)
        )
        assert "CODEX_THREAD_ID" not in environment
        observed_home = Path(environment["CODEX_HOME"])
        assert {entry.name for entry in observed_home.iterdir()} == {
            "auth.json",
            "tmp",
        }
        return process

    monkeypatch.setattr(codex_runner_module, "_STANDARD_POPEN", factory)
    result = CodexAppServerRunner(
        CodexRunConfig(runtime, executable=str(executable), auth_file=auth),
        process_factory=factory,
    ).run(prompt="prove it", output_schema={"type": "object"})
    assert result.standard_popen_used
    assert result.codex_home_initial_auth_only
    assert result.codex_home_cleanup_verified
    assert result.credential_leak_scan_passed
    assert observed_home is not None and not observed_home.exists()
    assert dict(os.environ) == parent_environment


def test_standard_runner_purges_home_after_credential_leak(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    token = "test-auth-sentinel-abcdefghijklmnopqrstuvwxyz"
    process = ScriptedProcess(
        complete_transcript_messages(prompt="prove it"), stderr=token.encode()
    )
    executable = native_executable(tmp_path)
    runtime = runtime_directory(tmp_path)
    auth = auth_file(tmp_path, token)
    observed_home: Path | None = None

    def factory(*args: object, **kwargs: object) -> ScriptedProcess:
        nonlocal observed_home
        observed_home = Path(kwargs["env"]["CODEX_HOME"])
        return process

    monkeypatch.setattr(codex_runner_module, "_STANDARD_POPEN", factory)
    with pytest.raises(
        AppServerProtocolError,
        match="contained authentication material",
    ) as captured:
        CodexAppServerRunner(
            CodexRunConfig(runtime, executable=str(executable), auth_file=auth),
            process_factory=factory,
        ).run(prompt="prove it", output_schema={"type": "object"})
    assert token not in str(captured.value)
    assert observed_home is not None and not observed_home.exists()


def test_standard_runner_purges_home_after_launch_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    executable = native_executable(tmp_path)
    runtime = runtime_directory(tmp_path)
    auth = auth_file(tmp_path)
    observed_home: Path | None = None

    def factory(*args: object, **kwargs: object) -> ScriptedProcess:
        nonlocal observed_home
        observed_home = Path(kwargs["env"]["CODEX_HOME"])
        raise OSError("synthetic launch failure")

    monkeypatch.setattr(codex_runner_module, "_STANDARD_POPEN", factory)
    with pytest.raises(OSError, match="synthetic launch failure"):
        CodexAppServerRunner(
            CodexRunConfig(runtime, executable=str(executable), auth_file=auth),
            process_factory=factory,
        ).run(prompt="prove it", output_schema={"type": "object"})
    assert observed_home is not None and not observed_home.exists()


def test_scripted_clean_process_exercises_full_runner_path(
    tmp_path: Path,
) -> None:
    process = ScriptedProcess(
        complete_transcript_messages(prompt="prove it"), stderr=b"diagnostic\n"
    )
    executable = native_executable(tmp_path)
    runtime = runtime_directory(tmp_path)

    def process_factory(command: tuple[str, ...], **kwargs: object) -> ScriptedProcess:
        assert command[0] == str(executable)
        return process

    runner = CodexAppServerRunner(
        CodexRunConfig(runtime, executable=str(executable)),
        process_factory=process_factory,
    )
    result = runner.run(prompt="prove it", output_schema={"type": "object"})
    assert result.audit.eligible, result.audit.reasons
    assert result.output_text == "{}"
    assert result.stderr_bytes == b"diagnostic\n"
    assert result.executable_path == str(executable)
    assert result.executable_size_bytes == len(SYNTHETIC_NATIVE_BYTES)
    assert result.executable_sha256_digest == sha256(SYNTHETIC_NATIVE_BYTES)
    assert result.executable_lock_enforced is (os.name == "nt")
    assert result.standard_popen_used is False
    assert process.wait_calls == 1
    assert process.kill_calls == 0
    assert process.terminate_calls == 0


def test_process_factory_identity_is_snapshotted_before_callback_mutation(
    tmp_path: Path,
) -> None:
    process = ScriptedProcess(complete_transcript_messages(prompt="prove it"))
    executable = native_executable(tmp_path)
    runtime = runtime_directory(tmp_path)
    runner: CodexAppServerRunner

    def self_mutating_factory(*args: object, **kwargs: object) -> ScriptedProcess:
        runner._process_factory = codex_runner_module.subprocess.Popen
        return process

    runner = CodexAppServerRunner(
        CodexRunConfig(runtime, executable=str(executable)),
        process_factory=self_mutating_factory,
    )
    result = runner.run(prompt="prove it", output_schema={"type": "object"})
    assert runner._process_factory is codex_runner_module.subprocess.Popen
    assert result.standard_popen_used is False


def test_runner_sends_the_same_schema_snapshot_it_retains(
    tmp_path: Path,
) -> None:
    process = ScriptedProcess(complete_transcript_messages(prompt="prove it"))
    process.stdin = KeepBytesIO()
    schema = {"type": "object"}
    executable = native_executable(tmp_path)
    runtime = runtime_directory(tmp_path)

    def process_factory(*args: object, **kwargs: object) -> ScriptedProcess:
        schema["type"] = "array"
        return process

    runner = CodexAppServerRunner(
        CodexRunConfig(runtime, executable=str(executable)),
        process_factory=process_factory,
    )
    result = runner.run(prompt="prove it", output_schema=schema)
    outbound = [json.loads(line) for line in process.stdin.getvalue().splitlines()]
    turn_start = next(message for message in outbound if message.get("id") == 3)

    assert result.output_schema_json == b'{"type":"object"}'
    assert turn_start["params"]["outputSchema"] == {"type": "object"}
    assert schema == {"type": "array"}


def test_missing_pipe_process_is_killed_and_reaped(
    tmp_path: Path,
) -> None:
    process = MissingPipeProcess()
    executable = native_executable(tmp_path)
    runtime = runtime_directory(tmp_path)
    runner = CodexAppServerRunner(
        CodexRunConfig(runtime, executable=str(executable)),
        process_factory=lambda *args, **kwargs: process,
    )
    with pytest.raises(AppServerProtocolError, match="pipes were not created"):
        runner.run(prompt="prove it", output_schema={"type": "object"})
    assert process.kill_calls == 1
    assert process.wait_calls == 1


def test_runner_rejects_executable_toctou_after_process_launch(tmp_path: Path) -> None:
    process = ScriptedProcess(complete_transcript_messages(prompt="prove it"))
    executable = native_executable(tmp_path)
    runtime = runtime_directory(tmp_path)
    mutation_blocked = False

    def process_factory(*args: object, **kwargs: object) -> ScriptedProcess:
        nonlocal mutation_blocked
        try:
            executable.write_bytes(SYNTHETIC_NATIVE_BYTES + b"tampered")
        except OSError:
            mutation_blocked = True
        return process

    runner = CodexAppServerRunner(
        CodexRunConfig(runtime, executable=str(executable)),
        process_factory=process_factory,
    )
    if os.name == "nt":
        result = runner.run(prompt="prove it", output_schema={"type": "object"})
        assert mutation_blocked
        assert result.executable_lock_enforced
    else:
        with pytest.raises(AppServerProtocolError, match="preflight and postflight"):
            runner.run(prompt="prove it", output_schema={"type": "object"})


@pytest.mark.skipif(os.name != "nt", reason="Windows deny-delete lease")
def test_windows_lease_blocks_swap_and_restore_between_hashes(tmp_path: Path) -> None:
    process = ScriptedProcess(complete_transcript_messages(prompt="prove it"))
    executable = native_executable(tmp_path)
    runtime = runtime_directory(tmp_path)
    backup = executable.with_name("codex-original.exe")
    malicious = executable.with_name("codex-malicious.exe")
    malicious.write_bytes(b"MZ\x00\x00malicious-test-native")
    swap_blocked = False

    def process_factory(*args: object, **kwargs: object) -> ScriptedProcess:
        nonlocal swap_blocked
        try:
            executable.rename(backup)
        except OSError:
            swap_blocked = True
            return process
        try:
            malicious.rename(executable)
            executable.rename(malicious)
            backup.rename(executable)
        finally:
            if backup.exists() and not executable.exists():
                backup.rename(executable)
        return process

    result = CodexAppServerRunner(
        CodexRunConfig(runtime, executable=str(executable)),
        process_factory=process_factory,
    ).run(prompt="prove it", output_schema={"type": "object"})
    assert swap_blocked
    assert result.executable_lock_enforced


@pytest.mark.parametrize(
    "value", [True, False, "0.5", None, float("nan"), float("inf"), -0.1, 1.1]
)
def test_probability_validation_rejects_non_json_or_out_of_range_values(
    value: object,
) -> None:
    with pytest.raises(ValueError):
        validate_probability(value)


@pytest.mark.parametrize("value", [0, 0.0, 0.5, 1, 1.0])
def test_probability_validation_accepts_finite_interval(value: object) -> None:
    assert validate_probability(value) == float(value)


def test_clean_stream_is_json_serializable_for_ignored_evidence_storage() -> None:
    encoded = json.dumps(completed_messages(), allow_nan=False, sort_keys=True)
    assert json.loads(encoded)[-1]["method"] == "turn/completed"
