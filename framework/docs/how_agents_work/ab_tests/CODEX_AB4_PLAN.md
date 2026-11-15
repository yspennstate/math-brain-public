# Codex brain / no-brain test 4: prior work on open problems (plan, 14 Nov 2026)

Why a new design: the three writing tests (WBAB1-3) came out null, with the spread between writers larger than any
brain effect. Writing quality is a weak instrument. Questions about what we already know have checkable answers.

Task: 40 questions about our own prior work on open problems, each answerable from the brain and not from the
literature alone. Examples of the kind (not the items): what width exponent did a run show as flat, which
construction was refuted and by what counterexample, which threshold a referee corrected.

Arms, both Codex gpt-6.1-sol at normal speed, high effort, same prompt apart from one paragraph:
- A (brain): may run problem_recall.py, math_recall.py and brain.py recall.
- B (no brain): the same shell with those three tools absent from PATH and the memory folder unreadable.

Scoring: a hidden key of 1-3 checkable facts per question (kept in the scratchpad, never on GitHub); a fact counts
only if it is stated with its number or name. Record input, cached and output tokens for both arms.

Prereg before the run: primary measure is facts correct per question, paired by question; a sign test over
questions. A brain win also needs to be shown not to come only from answer-copying: count answers whose wording
matches a memory line verbatim.

Size: 40 questions x 2 arms, one Codex exec each, about 80 runs. Sized against the usage report before launch.

## Preregistration (frozen 14 Nov 2026 23:5x, before any run)

- Items: 40 questions, 103 key facts, written from 60 problem memories of 1-14 Nov drawn with seed 20261114. Kept: at
  most 4 P0434 items, 2 T104, 1 T228; dropped items whose answer is only a literature status. Questions name the
  problem, never the answer. Questions and key in the session scratchpad; the key never goes to GitHub.
- Runs: 8 groups of 5 questions (shuffle seed 20261115, ab4_groups.json, not published), one Codex exec per group and
  arm, 16 runs. gpt-6.1-sol, high effort, normal speed (service_tier default, fast and ultrafast off), HOOKS OFF in
  both arms, so the arms differ only in the paragraph naming the three recall tools (A) or forbidding the brain (B).
  Order alternates which arm goes first per group. Runner framework/experiments/codex_probe/ab4_run.py through run_probe.py.
- Score: a fact counts when the answer states it with its number or name; scored blind to arm (answers relabelled
  before scoring). Primary: facts correct per question, paired by question, two-sided sign test over the questions
  with a nonzero difference. Secondary: questions with at least one fact; answers that are wrong rather than
  "unknown" (confident errors).
- Contamination: an arm-B run whose log shows a read of the memory folder, the brain repo, a math-brain folder or a
  recall tool is reported and scored both ways. Copying check: count arm-A answer sentences that match a memory line
  verbatim (12+ word overlap).
- Expected result, stated now: A beats B on most questions (these facts are our own and mostly unpublished). A
  null here would mean the recall tools are not reaching their own records, and that is the bug to look for.
- Tokens: input, cached input and output for every run, from each codex.log.
