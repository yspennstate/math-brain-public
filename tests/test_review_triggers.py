"""Schema-2 review triggers (front G02, 12 Oct 2026): controls in both directions for the probability catalogue."""

from pathlib import Path

import pytest

from math_brain.triggers import (
    ReviewTrigger,
    load_triggers,
    match_triggers,
    normalize_text,
    review_cautions,
)

ROOT = Path(__file__).parents[1]
CATALOGUE = ROOT / "config" / "review_triggers_probability.toml"


@pytest.fixture(scope="module")
def catalogue():
    return load_triggers(CATALOGUE)


def fired(text, triggers):
    return {match.trigger.id for match in match_triggers(text, triggers)}


def test_catalogue_loads_with_unique_ids_and_patterns(catalogue) -> None:
    assert len(catalogue) >= 30
    assert len({trigger.id for trigger in catalogue}) == len(catalogue)
    assert all(trigger.whole_words and trigger.reflex for trigger in catalogue)


def test_schema_one_file_keeps_substring_semantics() -> None:
    triggers = load_triggers(ROOT / "config" / "triggers.toml")
    assert all(not trigger.whole_words for trigger in triggers)
    trigger = ReviewTrigger("limit", ("limit", "integral"), "check theorem")
    assert match_triggers("Interchange LIMIT and Integral", [trigger])[0].matched_keywords == ("limit", "integral")


def test_normalization_spells_out_symbols() -> None:
    assert normalize_text("Lévy’s σ ≥ 0, k²") == "levy's sigma >= 0, k^2"
    assert normalize_text(r"$\sigma \le \infty$") == "sigma <= infinity"
    assert normalize_text("non-negative sub-Gaussian") == "non negative sub gaussian"


@pytest.mark.parametrize(
    "flawed, repaired, trigger_id",
    [
        (
            "By Hoeffding's inequality, P(S_n - E S_n >= t) <= exp(-2t^2/n).",
            "Let X_1,...,X_n be independent with a_i <= X_i <= b_i; Hoeffding's inequality gives P(S_n - E S_n >= t) <= exp(-2t^2/n).",
            "conc-independence",
        ),
        (
            "By Chebyshev's inequality the variance tends to zero, so X_n -> 0 almost surely.",
            "By Chebyshev's inequality the variance tends to zero, so X_n -> 0 in probability.",
            "as-from-in-probability-tools",
        ),
        (
            "Chebyshev: P(|X - mu| >= k sigma) <= 1/k^2 for every k > 0.",
            "Chebyshev: if sigma > 0 then P(|X - mu| >= k sigma) <= 1/k^2 for every k > 0.",
            "standardized-positive-variance",
        ),
        (
            "By Markov's inequality, P(X >= a) >= E[X]/a.",
            "By Markov's inequality, P(X >= a) <= E[X]/a, so P(X < a) >= 1 - E[X]/a.",
            "tail-bound-direction",
        ),
        (
            "Uncorrelated variables are independent.",
            "Uncorrelated jointly Gaussian variables are independent.",
            "uncorrelated-not-independent",
        ),
        (
            "By the optional stopping theorem E[M_T] = E[M_0].",
            "T is a bounded stopping time, so by the optional stopping theorem E[M_T] = E[M_0].",
            "optional-stopping-condition",
        ),
        (
            "Rescaled random walks converge to Brownian motion by Donsker's invariance principle.",
            "Rescaled random walks with iid steps of mean zero and finite variance converge to Brownian motion by Donsker's invariance principle.",
            "clt-variance",
        ),
        (
            "The cumulants are the coefficients of log E[e^{tX}] (the cumulant generating function).",
            "When E e^{tX} is finite near 0, the cumulants are the coefficients of the cumulant generating function.",
            "mgf-finiteness",
        ),
    ],
)
def test_trigger_fires_on_flawed_text_and_is_silent_on_repaired(catalogue, flawed, repaired, trigger_id) -> None:
    assert trigger_id in fired(flawed, catalogue)
    assert trigger_id not in fired(repaired, catalogue)


def test_plain_prose_and_unrelated_mathematics_stay_silent(catalogue) -> None:
    assert not fired("Please rebalance the portfolio before the close and report the fills.", catalogue)
    assert not fired("The Riemann mapping theorem needs a simply connected proper subdomain of the plane.", catalogue)


def test_missing_match_names_the_absent_hypothesis(catalogue) -> None:
    matches = [m for m in match_triggers("By Azuma's inequality the martingale concentrates.", catalogue)
               if m.trigger.id == "conc-boundedness"]
    assert matches and matches[0].missing


def test_review_cautions_are_capped_and_one_per_pattern(catalogue) -> None:
    text = "By Hoeffding's inequality and Chebyshev, X_n -> 0 almost surely; uncorrelated variables are independent."
    lines = review_cautions(text, catalogue, limit=2)
    assert len(lines) == 2
    assert all(line.startswith("review trigger ") for line in lines)
    assert review_cautions("A simply connected domain.", catalogue) == []
