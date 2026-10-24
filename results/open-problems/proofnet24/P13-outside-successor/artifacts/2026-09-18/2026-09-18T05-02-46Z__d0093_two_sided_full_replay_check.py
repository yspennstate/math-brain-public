#!/usr/bin/env python3
"""Exact finite self-check for P13 D0093 chronological full replay.

This is deliberately a bounded, source-shaped transcript model, not a proof of
Rolla Proposition 6.5. It implements only the structural features used by the
analytic replay lemma:

* an explorer starts at 0 between two barriers;
* at its current site it reveals the next previously-unrevealed instruction;
* S leaves the explorer in place, L/R moves one lattice step;
* exploration stops at the first current barrier hit;
* after a successful source-shaped trap test, the hit-side barrier is moved
  inward to that trap; if there is no such trap, that attempt prefix stops;
* after all virtual exploration records are fixed, we replay them
  chronologically as acceptable ARW topplings from m particles at 0.

The exact assertion checked is finite: for every enumerated completed transcript,
chronological full replay is acceptable and consumes at every site exactly the
number of instructions revealed there. This is a self-check only; the report
contains the general induction proof.
"""

from collections import defaultdict
from itertools import product

SYMS = ("L", "R", "S")
RADIUS = 2
PARTICLES = 2
MAX_STEPS_PER_EXPLORER = 6
CHOICE_LENGTH = 10


def run_explorer(revealed, left, right, choices, max_steps):
    pos = 0
    record = []
    local = defaultdict(list)

    for _ in range(max_steps):
        if pos == left or pos == right:
            break
        try:
            sym = next(choices)
        except StopIteration:
            return None, "insufficient"

        revealed[pos].append(sym)
        record.append((pos, sym))
        local[pos].append(sym)

        if sym == "L":
            pos -= 1
        elif sym == "R":
            pos += 1

        if pos == left or pos == right:
            break
    else:
        return None, "timeout"

    if pos not in (left, right):
        return None, "timeout"

    side = "L" if pos == left else "R"
    if side == "L":
        candidates = [
            x for x, seq in local.items()
            if left < x < 0 and len(seq) >= 2 and seq[-2:] == ["S", "L"]
        ]
        trap = min(candidates) if candidates else None
        new_left, new_right = (trap if trap is not None else left), right
    else:
        candidates = [
            x for x, seq in local.items()
            if 0 < x < right and len(seq) >= 2 and seq[-2:] == ["S", "R"]
        ]
        trap = max(candidates) if candidates else None
        new_left, new_right = left, (trap if trap is not None else right)

    return {
        "record": tuple(record),
        "hit": pos,
        "side": side,
        "trap": trap,
        "new_left": new_left,
        "new_right": new_right,
    }, "ok"


def generate_history(choice_tuple):
    choices = iter(choice_tuple)
    revealed = defaultdict(list)
    left, right = -RADIUS, RADIUS
    explorers = []

    for _ in range(PARTICLES):
        explorer, status = run_explorer(
            revealed, left, right, choices, MAX_STEPS_PER_EXPLORER
        )
        if status != "ok":
            return None, status
        explorers.append(explorer)

        if explorer["trap"] is None:
            break

        left, right = explorer["new_left"], explorer["new_right"]
        if not (left < 0 < right):
            break

    return {
        "explorers": tuple(explorers),
        "revealed": tuple(sorted((x, tuple(seq)) for x, seq in revealed.items())),
    }, "ok"


def apply_acceptable_instruction(state, site, sym):
    """Apply one ARW instruction, allowing toppling of one sleeper.

    state[x] is 0 (absent), 's' (one sleeper), or an integer >=1 (active).
    """
    value = state.get(site, 0)
    if value == 0:
        return False

    if sym == "S":
        if value == "s":
            state[site] = "s"
        elif value == 1:
            state[site] = "s"
        else:
            state[site] = value
        return True

    if value == "s" or value == 1:
        state.pop(site, None)
    else:
        state[site] = value - 1

    dest = site + (-1 if sym == "L" else 1)
    dest_value = state.get(dest, 0)
    if dest_value == 0:
        state[dest] = 1
    elif dest_value == "s":
        state[dest] = 2
    else:
        state[dest] = dest_value + 1
    return True


def particle_count_vector(state):
    out = {}
    for x, value in state.items():
        out[x] = 1 if value == "s" else value
    return {x: v for x, v in out.items() if v}


def replay_check(history):
    state = {0: PARTICLES}
    consumed = defaultdict(int)
    hits = []

    for explorer in history["explorers"]:
        for site, sym in explorer["record"]:
            if not apply_acceptable_instruction(state, site, sym):
                return False, "unacceptable_toppling"
            consumed[site] += 1
        hits.append(explorer["hit"])

    revealed_counts = {x: len(seq) for x, seq in history["revealed"]}
    consumed_counts = {x: c for x, c in consumed.items() if c}
    if consumed_counts != revealed_counts:
        return False, "consumed_revealed_mismatch"

    expected_mass = defaultdict(int)
    expected_mass[0] += PARTICLES - len(hits)
    for hit in hits:
        expected_mass[hit] += 1
    expected_mass = {x: v for x, v in expected_mass.items() if v}
    if particle_count_vector(state) != expected_mass:
        return False, "mass_transport_mismatch"

    return True, "ok"


def history_key(history):
    return (
        tuple(
            (
                exp["record"], exp["hit"], exp["side"], exp["trap"],
                exp["new_left"], exp["new_right"]
            )
            for exp in history["explorers"]
        ),
        history["revealed"],
    )


def main():
    status_counts = defaultdict(int)
    distinct = {}
    failures = []

    for choices in product(SYMS, repeat=CHOICE_LENGTH):
        history, status = generate_history(choices)
        status_counts[status] += 1
        if status != "ok":
            continue

        distinct.setdefault(history_key(history), history)
        ok, reason = replay_check(history)
        if not ok:
            failures.append((choices, reason, history))
            break

    total = len(SYMS) ** CHOICE_LENGTH
    print(f"radius={RADIUS}")
    print(f"particles={PARTICLES}")
    print(f"max_steps_per_explorer={MAX_STEPS_PER_EXPLORER}")
    print(f"global_choice_length={CHOICE_LENGTH}")
    print(f"choice_strings={total}")
    print(f"completed_choice_strings={status_counts['ok']}")
    print(f"timeout_choice_strings={status_counts['timeout']}")
    print(f"insufficient_choice_strings={status_counts['insufficient']}")
    print(f"distinct_completed_histories={len(distinct)}")
    print(f"replay_failures={len(failures)}")

    assert sum(status_counts.values()) == total
    assert not failures
    assert all(replay_check(history)[0] for history in distinct.values())
    print(
        "PASS: every completed source-shaped history has acceptable chronological "
        "full replay, consumed_count == revealed_count sitewise, and the exact "
        "source-to-hit-barrier mass-transport identity."
    )


if __name__ == "__main__":
    main()
