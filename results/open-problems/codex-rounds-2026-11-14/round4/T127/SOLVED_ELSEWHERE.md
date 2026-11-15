# Reported outside solution

Reference: *The frog model is recurrent on the 3-ary tree and transient on
the 4-ary tree*. The paper's author field is
`311859884+mt0-svg@users.noreply.github.com`; the repository account is
`mt0-svg`. Do not replace this attribution with a guessed personal name.

- [Full paper, TeX source](https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/paper/main.tex)
- [Statement-to-Lean map](https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/STATEMENTS.md)
- [Repository](https://github.com/mt0-svg/frog-model-tree)
- [Releases](https://github.com/mt0-svg/frog-model-tree/releases), v2.0.0, displayed as 4 October 2026.

ArXiv id: none identified in the limited search. The full paper was actually
opened on 15 November 2026; the earlier rounds could not retrieve it.

Theorem 1.2 states almost-sure transience for d=4 and expected root visits
after time zero at most 5.756. Theorem 1.3 states almost-sure recurrence for
d=3. Section 1 specifies one active root frog, one sleeper at every other
vertex, independent simple random walks and the rooted d-ary tree. Thus the
statements address T127 itself.

Verification status: a full proof text and statement map are accessible.
The latter links the conclusions to `FrogModel.transient_four`,
`FrogModel.meanVisits_four_le` and `FrogModel.recurrent_three`, and identifies
generated certificate dependencies. This session has not independently
checked the complete argument, formal definitions or certificates. The file
records a reported solution, not a certification that the problem is settled.

The task's literature-stop instruction is applied here. Before treating the
result as verified, inspect the formal model and replay the certificates in
a separately authorized environment with sufficient compute and dependencies.
