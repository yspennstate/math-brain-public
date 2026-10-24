"""The strict benefit decision says whether a run could answer, not only whether the brain helped.

Scheduled audit account04/B08, B08-R79-STRICT-BENEFIT-VERDICT-UNREACHABLE-20260929: helped=False meant both "the
brain did not help" and "this run cannot say". The strongest run the test helpers can build - a sealed plan,
every slot a parsed Codex artifact, a perfect effect - fails exactly two evidence gates, the two the current
transport cannot pass, and must read as ineligible, never as a verdict about the brain.
"""

import inspect
import json
import re
from dataclasses import replace

import pytest

import math_brain.evaluation as ev
from math_brain.challenge_study import summarize_run
from test_evaluation import (  # noqa: F401  (config is a fixture)
    SYNTHETIC_EXECUTABLE_PROVENANCE,
    build_test_plan,
    codex_artifact_for_batch,
    config,
    response_payload,
    retrieval_evidence,
)

TRANSPORT_BLOCKERS = ("output_token_budget_unenforced", "served_identity")


def _artifact_run(config: ev.EvaluationConfig, *, brain_off_correct: bool) -> ev.EvaluationRun:
    sealed = replace(
        config,
        runtime=replace(config.runtime, executable_provenance=SYNTHETIC_EXECUTABLE_PROVENANCE),
    )
    plan = build_test_plan(sealed, manifest_label="benefit-status")
    results, runtimes, isolations = [], [], []
    for pair_id in plan.spec.required_pair_ids:
        for condition in ev.Condition:
            correct = condition is ev.Condition.BRAIN_ON or brain_off_correct
            raw = json.dumps(response_payload(plan, pair_id, condition, correct=correct))
            artifact = codex_artifact_for_batch(plan, pair_id, condition, raw)
            result, runtime, isolation = ev.parse_codex_artifact_response(
                plan, pair_id=pair_id, condition=condition, artifact=artifact
            )
            results.append(result)
            runtimes.append(runtime)
            isolations.append(isolation)
    return ev.finalize_run(
        plan,
        batch_results=results,
        runtime_evidence=runtimes,
        isolation_evidence=isolations,
        retrieval_evidence=retrieval_evidence(plan),
    )


@pytest.mark.parametrize(
    ("failed", "status"),
    [
        ((), "helped"),
        (("primary_delta", "exact_randomization_p"), "not_shown"),
        (("primary_delta", "served_identity"), "ineligible"),
        (("a_gate_added_later",), "ineligible"),
    ],
    ids=["nothing-failed", "effect-only", "effect-and-evidence", "unknown-gate"],
)
def test_the_status_separates_no_benefit_from_no_answer(failed, status) -> None:
    assert ev.benefit_status(failed) == status
    assert status in ev.BENEFIT_STATUSES


def test_every_outcome_gate_is_one_decide_benefit_can_fail() -> None:
    names = set(re.findall(r'failed\.append\("([a-z_]+)"\)', inspect.getsource(ev.decide_benefit)))

    assert ev.OUTCOME_GATES <= names
    assert set(TRANSPORT_BLOCKERS) <= names - ev.OUTCOME_GATES


def test_a_perfect_effect_on_the_current_transport_is_ineligible(config: ev.EvaluationConfig) -> None:
    decision = ev.decide_benefit(_artifact_run(config, brain_off_correct=False))

    assert decision.primary_delta == pytest.approx(1.0)
    assert decision.inference.randomization_p < 0.01
    assert decision.failed_gates == TRANSPORT_BLOCKERS
    assert decision.ineligible_gates == TRANSPORT_BLOCKERS
    assert not decision.helped
    assert decision.status == "ineligible"


def test_a_null_effect_the_run_cannot_judge_is_not_reported_as_no_benefit(config: ev.EvaluationConfig) -> None:
    decision = ev.decide_benefit(_artifact_run(config, brain_off_correct=True))

    assert "primary_delta" in decision.failed_gates
    assert set(TRANSPORT_BLOCKERS) <= set(decision.ineligible_gates)
    assert decision.status == "ineligible"


def test_the_study_summary_carries_the_status(config: ev.EvaluationConfig) -> None:
    run = _artifact_run(config, brain_off_correct=False)
    summary = summarize_run(run)

    assert summary["benefit_status"] == "ineligible"
    assert summary["ineligible_gates"] == list(TRANSPORT_BLOCKERS)
    assert summary["helped_strict"] is False
