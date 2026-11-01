from pathlib import Path
p=Path('STATUS.md');t=p.read_text(encoding='utf8');t=t.replace('STATE: DONE','STATE: WORKING',1);t=t.replace(t.splitlines()[1],'NEXT: Test invariant-sigma-field shift coupling and a Kakutani product-law extension of the regenerative case.',1);p.write_text(t+'\n2026-10-12: Reopened at user request for a serious second attempt; reread full ATTEMPT.md and exact remaining gap.\n',encoding='utf8')
p=Path('ATTEMPT.md')
with p.open('a',encoding='utf8') as f:f.write('''

# Second attempt, 2026-10-12

The remaining gap is to produce an exact finite stationarizing shift, rather than finite-window limits with centers escaping to infinity. Two approaches not pursued in the first attempt:

1. **Orbit laws and shift coupling.** On two-sided continuous paths, integer recentering is an invertible ergodic transformation of Wiener measure. Thorisson's invariant-sigma-field criterion may convert full-path absolute continuity (or equality on invariant events) into an exact finite random shift. Test whether the independent cut plus FBM/BBM forces those invariant-event laws, and prove any valid full-law domination special case. The earlier proof used local total variation only, which does not give this full-path condition.
2. **Kakutani equivalence of independent stopped-piece laws.** Compare nonidentically distributed stopped pieces with a common finite-mean stopping law, whose concatenation is 2BM by source Theorem 5.1. Summable Hellinger discrepancies may make the entire product law absolutely continuous. Transport the reference stationarizing kernel, then use orbit-law shift coupling to remove the resulting Wiener tilt. This could extend Theorem 5.1 to genuinely path-dependent, nonidentically distributed stopping rules. Alternatively, divergence of the Hellinger sum may identify where a counterexample must lie, though singular marked laws alone are not a counterexample for unmarked paths.

Initial choice: pursue approach 2, supported by a fully proved orbit-law/filling lemma from approach 1. No claim yet that the source hypotheses imply any absolute continuity condition.
''')
