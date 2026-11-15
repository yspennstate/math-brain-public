VERDICT: PARTIAL located a later preprint ruling out polynomial worst-case trace complexity

The literature check found OpenAI, *Quantitative lower bounds for trace reconstruction* (September 24, 2026). Its main theorem gives a superpolynomial lower bound for complete deletion traces at every fixed deletion probability. The model is the one in the task, with unrestricted computation. See [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) for the precise theorem, primary links, identifier status, and the October algorithmic follow-up.

This follows the instructed stop branch. No new proof, finite computation, or counterexample search was undertaken. The precise asymptotic order remains unsettled by the cited bounds.

Checks: read the theorem and model definitions in the primary TeX; cross-checked title, author and date against the release citation and manuscript header; read the final transfer section for exact lengths and success quantifiers. Independently checked the fixed-channel consequence in two forms: log(q^3 log n)=log log n+3 log q diverges, and the logarithm of the displayed bound divided by log n diverges. Thus every fixed polynomial is eventually exceeded. The condition excludes q tending to zero too quickly; it includes every fixed q in (0,1).

Commands and tool calls: web searches and exact opened source paths are recorded in [LOG.md](LOG.md). Local commands were tiny reads/writes under `OMP_NUM_THREADS=1 nice -n 15 python3 -B`; there was no numerical run or dataset. `ps -o pid,ppid,ni,comm -p $$ -p $PPID` was blocked by the sandbox. The nice wrapper also emitted a priority warning, so effective priority was not verified.

Limitations: repository directory fetches and PDF extraction failed; the primary manuscript TeX was accessible. No arXiv identifier was located for either new preprint. Their full proofs and Lean artifacts were not independently verified here, and no journal acceptance was established.

Next worker: review the lower-bound construction or run its Lean comparator and check the formal statement against ordinary deletion traces before treating the reported resolution as independently certified. For new research, update the starting bounds and target the remaining superpolynomial-to-quasipolynomial gap.

Task: “push this problem forward by one checkable piece” — T116, November 14, 2026, 22:00 Asia/Tbilisi (session start).
