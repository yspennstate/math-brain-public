# How the agents work: a record from one ten-day loop

The mechanisms are described elsewhere: the mesh in `framework/mesh/PROTOCOL.md`, shared writes in
`framework/docs/MULTI_AGENT_OPERATIONS.md`, the owner's task list in `framework/docs/TASK_CHECKLIST.md`, and
brain/no-brain measurement in `framework/docs/MEASURING_A_NOTES_ARM.md`. This folder shows them in use. It is drawn
from the files one agent kept between 10 and 15 November 2026 while running three standing orders at once: find and
fix bugs in the brain framework, improve the brain and work on open problems with the idle GPUs, and publish the
framework's methods here. Agent identifiers, machine names, private paths and every test's answer key have been
removed; nothing else in the test files has been changed.

## One tick

Standing orders reach the agent as a prompt repeated every three minutes. A repeat is not a new task, so each tick
starts from a file rather than from the prompt:

1. Read the NEXT line. The agent keeps one file whose last line says what the next tick does. It is rewritten
   whenever a step finishes, so a crash or a context compaction costs at most one step. A real one, from 15 November:

   > NEXT: B5 how agents work (plans, NEXT lines, A/B designs and results without keys, scrubbed agent-to-agent
   > reports) -> framework/docs/how_agents_work/; then B7 credits index, B8 what's new. When the GPU job lands, add
   > its rows to the P0108 folder (both repos). AB4 scoring waits on all 16 ANSWERS.md.

2. Check what is running. Long jobs (a Codex test, a four-hour GPU sampler on another machine) are checked by
   their product, not by their return code: a run is done when its `ANSWERS.md` or its output rows exist. See the
   launch-queue report in `agent_reports.md` for why.
3. Claim before writing. Every write to shared state takes a mesh claim on the narrowest resource (an absolute
   path, or a `git:<repo>/<path>` or `topic:<name>` namespace). A claim that returns exit 3 belongs to someone else;
   the agent stops that write, messages the holder or picks a disjoint piece. The mutation is chained to the claim
   with `|| exit 3`, never with `;`, so a refused claim cannot be followed by the write.
4. Do one step and save it. Results go to disk the moment they exist, then to GitHub. A push is verified by
   comparing `git rev-parse origin/main:<path>` with `git hash-object <path>` for every file; a push that printed a
   commit hash but fails this check is not done.
5. Record it. A durable result becomes a memory with a status line (`verified` or `provisional`) and the
   measurement behind it; the task's checklist entry gets a dated note; the NEXT line is rewritten.
6. Release. Claims are released at the end of the step, not at the end of the session.

## Tests

Every comparison is written down before the first run, including the rule that decides it, the expected result and
how much room the test has to fail. Answer keys stay off GitHub because the same questions are reused on later
versions of the brain. Tokens are recorded for both arms, since a brain that helps at twice the cost is a different
result from one that helps for free.

| test | question | outcome | files |
|---|---|---|---|
| WBAB1 | Does the writing brain improve Codex pages? (1-10 scores) | 8.83 against 8.83: ceiling, no information | - |
| WBAB2 | Same, ranked by two blind judges | brain pages ranked worse (5.08 against 3.92 of 8), at 2.65 times the tokens; judges agreed weakly | - |
| WBAB3 | Same, three arms, four judges, prediction from WBAB2 stated in advance | no arm beats plain; the WBAB2 explanation did not replicate | `ab_tests/WBAB3_*` |
| BVNB139 | Do checklist and compaction rows crowd the answer out of recall? | no; the miss is a vocabulary gap upstream | `ab_tests/BVNB139_crowding.md` |
| AB4 | Does Codex answer questions about our own prior work better with the recall tools? | running | `ab_tests/CODEX_AB4_PLAN.md` |

The three writing tests are a sequence worth reading in order. WBAB1 failed as an instrument, so WBAB2 switched to
ranks; WBAB2's negative result came with a post-hoc explanation (repeated word stems), so WBAB3 made that explanation
a prediction that could fail, and it did. After three nulls with writer spread larger than any arm effect, AB4 moved
to questions with checkable answers.

## Files

- `ab_tests/WBAB3_PREREG.md`, `ab_tests/WBAB3_RESULT.md`, `ab_tests/wbab3_scores_summary.json`,
  `ab_tests/wbab3_tokens.json`: the third writing test, its rules as written before any page, its result, and tokens
  per writer and judge (B is the writing brain, M the reduced brain called B- in the text, C no brain, J the judges).
- `ab_tests/CODEX_AB4_PLAN.md`: plan and frozen preregistration of the prior-work test. The harness that runs it is
  `framework/experiments/codex_probe/`.
- `ab_tests/BVNB139_crowding.md`: an offline recall experiment on 139 of the owner's own prompts.
- `agent_reports.md`: three reports one agent sent to others, with what each receiver did.
