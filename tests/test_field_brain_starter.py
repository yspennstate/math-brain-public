"""The field brain starter: its dream agenda and one dream with a stand-in agent, run on a copy of the example."""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from math_brain.requests import RequestLedger

STARTER = Path(__file__).resolve().parents[1] / "examples" / "field_brain_starter"
pytestmark = pytest.mark.skipif(not STARTER.is_dir(), reason="the starter example is not in this checkout")


@pytest.fixture
def starter(tmp_path):
    copy = tmp_path / "starter"
    shutil.copytree(STARTER, copy, ignore=shutil.ignore_patterns("backups", "logs", ".dream.lock", "requests.jsonl"))
    return copy


def _agenda(starter: Path, *args: str, env: dict | None = None) -> str:
    out = starter / "dream" / "AGENDA_TEST.md"
    subprocess.run([sys.executable, str(starter / "dream" / "make_agenda.py"), "--out", str(out), *args],
                   check=True, capture_output=True, env=env)
    return out.read_text(encoding="utf-8")


def _env_without_ledger():
    import os

    return {k: v for k, v in os.environ.items() if k != "MATH_BRAIN_REQUESTS"}


def test_the_shipped_agenda_is_what_the_script_builds(starter):
    shipped = (starter / "dream" / "DREAM_AGENDA.md").read_text(encoding="utf-8")
    day = re.search(r"Built (\d{4}-\d{2}-\d{2})", shipped).group(1)
    fresh = _agenda(starter, "--today", day, env=_env_without_ledger())
    assert fresh.strip() == shipped.strip()
    for n in range(1, 7):
        assert f"## {n}." in fresh
    assert "## 7." not in fresh


def test_open_requests_reach_the_agenda(starter):
    led = RequestLedger(starter / "requests.jsonl")
    a = led.ask("Which records show a render reused after an audio change?", at="2026-04-01T09:00:00+00:00")
    led.ask("Which records show a render reused after an audio change?", at="2026-04-02T09:00:00+00:00")
    b = led.ask("What should the first test shot of a long render check?", at="2026-04-01T10:00:00+00:00")
    led.link(b.id, "method_one_test_shot_before_any_long_render_2026_03_19", "produced", at="2026-04-02T10:00:00+00:00")
    c = led.ask("Is a mistake without a How to apply line still a rule?", at="2026-04-01T11:00:00+00:00")
    led.link(c.id, "method_a_note_is_a_hint_not_an_order_2026_04_02", "answered_by", at="2026-04-02T11:00:00+00:00")
    d = led.ask("Should unlinked records be removed?", at="2026-04-01T12:00:00+00:00")
    led.set_status(d.id, "dropped")
    page = _agenda(starter, env=_env_without_ledger())
    part = page.split("## 7. Requests still waiting", 1)[1]
    items = [ln for ln in part.splitlines() if ln.startswith("- `")]
    assert [ln.split("`")[1] for ln in items] == [a.id, b.id]  # asked twice first; answered and dropped left out
    assert "asked 2x" in items[0] and "nothing produced" in items[0] and "1 produced" in items[1]
    assert {r.id for r in led.open_requests()} == {a.id, b.id}


def test_one_dream_with_a_stand_in_agent(starter, tmp_path):
    agent = tmp_path / "agent.py"
    agent.write_text(
        "import pathlib, sys\n"
        "sys.stdin.read()\n"
        "mem = pathlib.Path('memory')\n"
        "rec = mem / 'method_a_note_is_a_hint_not_an_order_2026_04_02.md'\n"
        "rec.write_text(rec.read_text(encoding='utf-8') + '\\n**How to apply:** check a note against the newest decision before acting on it.\\n',"
        " encoding='utf-8')\n"
        "(mem / 'method_one_test_shot_before_any_long_render_2026_03_19.md').unlink()\n"
        "print('added one rule')\n", encoding="utf-8")
    cmd = '"%s" "%s"' % (Path(sys.executable).as_posix(), agent.as_posix())
    res = subprocess.run([sys.executable, str(starter / "dream" / "run_dream.py"), "--agent-cmd", cmd],
                         capture_output=True, text=True, env=_env_without_ledger())
    assert res.returncode == 0, res.stdout + res.stderr
    assert (starter / "memory" / "method_one_test_shot_before_any_long_render_2026_03_19.md").exists()  # put back
    logs = list((starter / "dream" / "logs").glob("dream_*.md"))
    assert len(logs) == 1 and len(list((starter / "dream" / "backups").iterdir())) == 1
    log = logs[0].read_text(encoding="utf-8")
    assert "changed method_a_note_is_a_hint_not_an_order_2026_04_02.md" in log
    assert "method_one_test_shot_before_any_long_render_2026_03_19.md" in log.split("put back from the backup", 1)[1]
    before, after = map(int, re.search(r"no rule for next time: (\d+) before, (\d+) after", log).groups())
    assert after == before - 1
    assert not (starter / "dream" / ".dream.lock").exists()


def _prompt(starter: Path, stage: str) -> str:
    out = starter / "dream" / "prompt_test.md"
    subprocess.run([sys.executable, str(starter / "dream" / "run_dream.py"), "--write-prompt", str(out), "--stage", stage],
                   check=True, capture_output=True, env=_env_without_ledger())
    return out.read_text(encoding="utf-8")


def test_each_stage_gets_its_own_sections(starter):
    heads = {s: re.findall(r"^## (\d+)\.", _prompt(starter, s), re.M) for s in ("all", "file", "connect")}
    assert heads["all"] == ["1", "2", "3", "4", "5", "6"]
    assert heads["file"] == ["1", "2", "3", "4"]
    assert heads["connect"] == ["5", "6"]
    assert "This is the connecting pass" in _prompt(starter, "connect")
    assert "This is the filing pass" in _prompt(starter, "file")
    assert "This is the" not in _prompt(starter, "all")


def test_a_night_takes_the_stages_in_turn(starter, tmp_path):
    seen = tmp_path / "seen.txt"
    agent = tmp_path / "agent.py"
    agent.write_text(
        "import sys\n"
        "p = sys.stdin.read()\n"
        "stage = 'connect' if 'This is the connecting pass' in p else 'file' if 'This is the filing pass' in p else 'all'\n"
        "open(%r, 'a', encoding='utf-8').write(stage + '\\n')\n" % str(seen), encoding="utf-8")
    cmd = '"%s" "%s"' % (Path(sys.executable).as_posix(), agent.as_posix())
    res = subprocess.run([sys.executable, str(starter / "dream" / "dream_night.py"), "--agent-cmd", cmd,
                          "--stages", "file,connect", "--max-cycles", "3", "--rest", "0", "--min-cycle", "0",
                          "--idle-stop", "0", "--hours", "1"], capture_output=True, text=True, env=_env_without_ledger())
    assert res.returncode == 0, res.stdout + res.stderr
    assert seen.read_text(encoding="utf-8").split() == ["file", "connect", "file"]
    night = next((starter / "dream" / "logs").glob("night_*.md")).read_text(encoding="utf-8")
    assert [r.split("|")[2].strip() for r in night.splitlines() if re.match(r"\| \d+ \|", r)] == ["file", "connect", "file"]
    logs = sorted((starter / "dream" / "logs").glob("dream_*.md"))
    assert len(logs) == 3 and "Stage: connect." in logs[1].read_text(encoding="utf-8")


def test_a_night_refuses_an_unknown_stage(starter):
    res = subprocess.run([sys.executable, str(starter / "dream" / "dream_night.py"), "--agent-cmd", "x",
                          "--stages", "file,deep"], capture_output=True, text=True)
    assert res.returncode == 2 and "--stages" in res.stderr


def _recall(starter: Path, *args: str) -> str:
    res = subprocess.run([sys.executable, str(starter / "recall.py"), *args], check=True, capture_output=True,
                         text=True, encoding="utf-8", env=_env_without_ledger())
    return res.stdout


def test_recall_lists_the_requests_asked_before(starter):
    q = "how long should the harbour film be"
    assert "Asked before" not in _recall(starter, q)  # no ledger, no block
    led = RequestLedger(starter / "requests.jsonl")
    r = led.ask("How long should the harbour film be for the festival?", at="2026-03-09T09:00:00+00:00")
    led.link(r.id, "project_harbour_film_cut_to_twelve_minutes_2026_03_10", "answered_by", at="2026-03-10T09:00:00+00:00")
    led.ask("How long should the harbour film be for the festival?", at="2026-04-02T09:00:00+00:00")
    led.ask("Which music library terms cover online release?", at="2026-03-15T09:00:00+00:00")
    out = _recall(starter, q, "--or", "festival slot length")
    block = out.split("Asked before (the request ledger):", 1)[1]
    assert r.id in block and "asked 2x since 2026-03-09, open" in block
    assert "the answer may not have landed" in block
    assert "answered by: project_harbour_film_cut_to_twelve_minutes_2026_03_10" in block
    assert "music library" not in block  # an unrelated request stays out
