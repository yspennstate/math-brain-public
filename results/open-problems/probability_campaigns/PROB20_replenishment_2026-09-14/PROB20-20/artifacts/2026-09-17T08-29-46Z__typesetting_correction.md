# PROB20-20 run 2026-09-17T08-29-46Z — immutable typesetting correction

This note corrects one notation typo in the immutable report

`runs/2026-09-17/2026-09-17T08-29-46Z__report.md`

created at commit `3a996f1ac862824439dec5c1f758c1b2191c3af0`.

In the proof of Lemma 7.1, equations (7.3) and (7.4) display `\nu^p` because the TeX control sequence `\nu` was typed where the previously defined large coordinate `u` was intended. Both occurrences should read `u^p`:

\[
\sum_r y_r^p\ge u^p+(C-u)^p,
\]

and

\[
u^p+(C-u)^p\ge (K+1)^p+(C-K-1)^p.
\]

The surrounding prose already defines `u>K` and explicitly says no source parameter `nu` is involved. This is a typesetting-only correction; the statement of Lemma 7.1, the endpoint-concavity argument, every subsequent bound, and Theorem 11.1 are unchanged.
