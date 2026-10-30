"""A StudyExecution is reported verified only when execute_prepared_study built it or a recheck against the ledger has
just passed.

Scheduled audit fleet03/B09, B09-R79-STUDYEXECUTION-VERIFIED-SUMMARY-UNBOUND-20260929: a hand-built object with
repeated slot ids and non-digest strings passed construction, and its summary said the attempt ledger was verified.
The ledger cases drive a real AttemptLedger to terminal states with the ledger tests' own helpers.
"""

from pathlib import Path

import pytest

from math_brain.attempt_ledger import ArtifactPayload, SlotState
from math_brain.challenge_study import StudyExecution
from test_attempt_ledger import _ledger, _start_first
from test_evaluation import complete_run, config, plan  # noqa: F401  (fixtures)


def _digest(number: int) -> str:
    return "sha256:" + format(number, "064x")


def _slots(run) -> int:
    return 2 * len(run.plan.spec.required_pair_ids)


def _driven_ledger(tmp_path: Path, count: int, *, leave_open: int | None = None):
    base = tmp_path / "base"
    base.mkdir(parents=True, exist_ok=True)
    ledger = _ledger(base, count=count)
    terminals = []
    for index in range(count):
        started = _start_first(ledger, tmp_path / ("slot%d" % index), index=index)
        if index == leave_open:
            continue
        terminals.append(ledger.record_returned(started, ArtifactPayload(b'{"answer":%d}' % index)))
    return ledger, terminals


def _evidence(run, ledger, terminals, **changes):
    fields = {
        "run": run,
        "ledger_digest": ledger.ledger_digest,
        "terminal_record_digests": tuple((t.slot_id, t.record_digest) for t in terminals),
        "outcome_object_digests": tuple((t.slot_id, t.object_digest) for t in terminals),
    }
    fields.update(changes)
    return StudyExecution(**fields)


def test_repeated_slot_ids_are_refused(complete_run) -> None:
    rows = tuple(("dup", _digest(index + 1)) for index in range(_slots(complete_run)))
    with pytest.raises(ValueError, match="unique"):
        StudyExecution(
            run=complete_run,
            ledger_digest=_digest(99),
            terminal_record_digests=rows,
            outcome_object_digests=rows,
        )


@pytest.mark.parametrize("where", ["terminal", "outcome"])
def test_non_digest_strings_are_refused(complete_run, where: str) -> None:
    good = tuple(("slot_%d" % index, _digest(index + 1)) for index in range(_slots(complete_run)))
    bad = (("slot_0", "not-a-digest"),) + good[1:]
    with pytest.raises(ValueError, match="sha256"):
        StudyExecution(
            run=complete_run,
            ledger_digest=_digest(99),
            terminal_record_digests=bad if where == "terminal" else good,
            outcome_object_digests=bad if where == "outcome" else good,
        )


def test_a_hand_built_object_is_not_reported_verified(complete_run) -> None:
    rows = tuple(("slot_%d" % index, _digest(index + 1)) for index in range(_slots(complete_run)))
    evidence = StudyExecution(
        run=complete_run,
        ledger_digest=_digest(99),
        terminal_record_digests=rows,
        outcome_object_digests=rows,
    )
    summary = evidence.privacy_safe_summary()

    assert summary["attempt_ledger_verified"] is False
    assert summary["attempt_ledger_verification"] == "not verified"


def test_evidence_that_matches_its_ledger_is_rechecked_as_verified(complete_run, tmp_path: Path) -> None:
    ledger, terminals = _driven_ledger(tmp_path, _slots(complete_run))
    evidence = _evidence(complete_run, ledger, terminals)

    assert evidence.verify_against_ledger(ledger)
    summary = evidence.privacy_safe_summary(ledger)
    assert summary["attempt_ledger_verified"] is True
    assert summary["attempt_ledger_verification"] == "rechecked against the ledger"


def test_a_changed_outcome_or_terminal_digest_fails_the_recheck(complete_run, tmp_path: Path) -> None:
    ledger, terminals = _driven_ledger(tmp_path, _slots(complete_run))
    good = _evidence(complete_run, ledger, terminals)
    wrong_outcome = _evidence(
        complete_run, ledger, terminals,
        outcome_object_digests=((terminals[0].slot_id, _digest(12345)),) + good.outcome_object_digests[1:],
    )
    wrong_terminal = _evidence(
        complete_run, ledger, terminals,
        terminal_record_digests=((terminals[0].slot_id, _digest(54321)),) + good.terminal_record_digests[1:],
    )

    assert not wrong_outcome.verify_against_ledger(ledger)
    assert not wrong_terminal.verify_against_ledger(ledger)
    assert wrong_outcome.privacy_safe_summary(ledger)["attempt_ledger_verified"] is False


def test_another_ledger_or_another_slot_order_fails_the_recheck(complete_run, tmp_path: Path) -> None:
    ledger, terminals = _driven_ledger(tmp_path / "a", _slots(complete_run))
    other, _ = _driven_ledger(tmp_path / "b", _slots(complete_run))
    good = _evidence(complete_run, ledger, terminals)
    reordered = _evidence(complete_run, ledger, [terminals[1], terminals[0]] + list(terminals[2:]))

    assert not good.verify_against_ledger(other)
    assert not reordered.verify_against_ledger(ledger)


def test_a_recheck_on_an_unfinished_slot_fails_and_writes_nothing(complete_run, tmp_path: Path) -> None:
    count = _slots(complete_run)
    ledger, terminals = _driven_ledger(tmp_path, count, leave_open=count - 1)
    open_slot = ledger.slots[count - 1].slot_id
    rows_t = tuple((t.slot_id, t.record_digest) for t in terminals) + ((open_slot, _digest(7)),)
    rows_o = tuple((t.slot_id, t.object_digest) for t in terminals) + ((open_slot, _digest(8)),)
    evidence = StudyExecution(
        run=complete_run,
        ledger_digest=ledger.ledger_digest,
        terminal_record_digests=rows_t,
        outcome_object_digests=rows_o,
    )
    before = sorted(p.name for p in ledger.root.rglob("*"))

    assert not evidence.verify_against_ledger(ledger)
    assert ledger.state(open_slot) is SlotState.STARTED
    assert sorted(p.name for p in ledger.root.rglob("*")) == before
