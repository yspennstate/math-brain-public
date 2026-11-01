# Three-arm test: the timed-out questions asked again (24-29 October 2026)

The three arms are the same as in the thousand-question test: brain (the math brain's recall tool and its prompt
notes, no file tools), documents (no brain, but it can read and search every research repository) and bare (the model
alone). Every answer was graded by the test's own grader against the answer key; the key was not opened to write this
page. Only counts are given here; the questions and answers stay private.

Two sets of runs had never been written up.

1. Claude, one shard of 323 questions. Every question that timed out at 600 s was asked again with a 1,200 s limit, in
   each arm.
2. Codex, three reruns of the 17 questions the brain arm had lost in the full run.

## Claude: does more time close the gap?

| limit | brain | documents | bare | brain against documents (wins / losses) | p |
|---|---|---|---|---|---|
| 600 s | 297 (92.0%), 11 timeouts | 259 (80.2%), 52 timeouts | 50 (15.5%) | 47 / 9 | 2.6e-7 |
| 1,200 s for the timeouts | 307 (95.0%), 1 timeout | 278 (86.1%), 33 timeouts | 50 (15.5%) | 33 / 4 | 1.1e-6 |

Doubling the limit helped the documents arm more (19 of its 52 timeouts answered, all 19 right) than the brain arm (10
of 11 answered, all right), and the brain arm still wins 33 to 4. Where both arms answered they tie: 274 of 279 for the
brain arm and 278 of 279 for the documents arm. The brain's lead is speed, not knowledge; the documents arm still ran
out of time on 33 questions at twenty minutes. One documents answer came back after 7,600 s because the process was not
stopped at the limit; it is counted above, and under a strict 1,200 s limit the comparison is 34 to 4.

The bare arm's rerun is not usable. 87 of its 95 rows timed out at 1,200 s and 8 failed; a model with no tools has
nothing to wait on, so these were the machine stalling, not the model thinking. Its 600 s numbers stand.

Speed and cost on the 600 s run (Claude Sonnet at list price, tokens include cached input):

| arm | median time | mean time | USD a question | input tokens a question | output tokens a question |
|---|---|---|---|---|---|
| brain | 75 s | 123 s | 0.055 | 21,019 | 1,606 |
| documents | 104 s | 205 s | 0.096 | 88,105 | 3,965 |
| bare | 44 s | 210 s | 0.010 | 2,369 | 238 |

On the questions each arm answered, the brain arm took a median 73 s against 88 s and read a fifth of the documents
arm's input (22,481 tokens against 109,454). Over the whole shard, both runs together:

| arm | total USD | right | USD per right answer |
|---|---|---|---|
| brain | 22.59 | 307 | 0.074 |
| documents | 42.44 | 278 | 0.153 |
| bare | 3.27 | 50 | 0.065 |

The documents arm costs about twice as much per right answer and is slower. The bare arm is cheap, but it is right on
one question in six.

## Codex: the brain arm's 17 losses, asked again

These are the 17 questions where the Codex brain arm said it could not find the record in the full run (7 of 17 right
there, against 16 of 17 for the documents arm).

| rerun | brain arm | documents arm |
|---|---|---|
| first (28 Oct evening) | 11 of 17 right, 6 "unknown" | every answer "unknown" within 30-60 s and no search run, so this arm was broken in this run |
| second (28 Oct night) | 6 of 17 right, 11 timeouts | not run |
| third (29 Oct), the 11 not yet answered | 6 right, 5 timeouts | not run |

15 of the 17 were answered right by the brain arm in at least one rerun, and no rerun gave a wrong value: every miss is
an "unknown" or a timeout. The second rerun's timeouts came while the recall tool was rebuilding its prepared state;
the runner now waits for a recall probe before each brain question, and with it 6 of those 11 were answered, all
right. In the first rerun the brain arm answered in a median 40 s on 119,509 input tokens a question. Most of the Codex
brain arm's losses in the full test were recall being slow or unavailable, not the store lacking the record.
