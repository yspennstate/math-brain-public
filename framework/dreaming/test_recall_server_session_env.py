"""test_recall_server_session_env.py - a served call sees exactly the session names its caller sent: a name the
caller lacks is unset for the call (so a script's search is not filed under the server spawner's session), a name it
sent is used, and the server's own environment is back as it was after the call."""
import os

import brain_recall_server as BRS


def make_brain(seen):
    b = object.__new__(BRS.Brain)
    b.refresh_state = lambda: []
    b.miss = {}
    b.calls = 0

    def main():
        seen.update({k: os.environ.get(k) for k in ("CLAUDE_CODE_SESSION_ID", "CLAUDE_CODE_ENTRYPOINT", "CODEX_THREAD_ID")})
    b.g = {"main": main}
    return b


def run(env, monkeypatch, pop=None):
    monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "spawner-session")
    monkeypatch.setenv("CLAUDE_CODE_ENTRYPOINT", "cli")
    monkeypatch.delenv("CODEX_THREAD_ID", raising=False)
    if pop is not None:
        monkeypatch.setenv("BRS_POP_SESSION_ENV", pop)
    else:
        monkeypatch.delenv("BRS_POP_SESSION_ENV", raising=False)
    seen = {}
    out = make_brain(seen).call(["recall", "x"], env, os.getcwd())
    assert out["rc"] == 0, out
    return seen


def test_caller_without_session_gets_none(monkeypatch):
    seen = run({}, monkeypatch)
    assert seen["CLAUDE_CODE_SESSION_ID"] is None
    assert seen["CLAUDE_CODE_ENTRYPOINT"] is None
    assert os.environ["CLAUDE_CODE_SESSION_ID"] == "spawner-session"   # restored after the call
    assert os.environ["CLAUDE_CODE_ENTRYPOINT"] == "cli"


def test_caller_session_is_used(monkeypatch):
    seen = run({"CODEX_THREAD_ID": "t-1"}, monkeypatch)
    assert seen["CODEX_THREAD_ID"] == "t-1"
    assert seen["CLAUDE_CODE_SESSION_ID"] is None
    assert "CODEX_THREAD_ID" not in os.environ


def test_switch_off_keeps_the_spawner(monkeypatch):
    seen = run({}, monkeypatch, pop="0")
    assert seen["CLAUDE_CODE_SESSION_ID"] == "spawner-session"
