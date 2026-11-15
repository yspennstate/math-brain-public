blind: yes
disk: small

Referee brief. Read ~/fei_solve_agent/NOTES.md (this one outside path is allowed) and nothing
else outside your folder.

Task: act as a hostile referee of Theorem 1, Proposition 4, Lemma 2, Lemma 3 and the composition law in NOTES.md.
1. For each statement, either write a complete proof in your own words (every step justified, edge cases S = empty,
   mu(S) = 0, up(S) = 0, constant f, |S| = n) or give an explicit counterexample.
2. Write your own verification code from scratch (do not reuse the code folder): exact rational or integer arithmetic
   where possible, all 65,536 functions on 4 variables for every statement, at least 10^6 random functions on 5 to 8
   variables at biases 0.5, 0.2, 0.05, and the structured families AND, OR, majority, tribes, address, parity times
   AND, bent functions on 4 and 6 variables.
3. Equality cases and sharpness: for which f is A = B + 2I - 2Var? Is the constant 2 in front of I best possible
   (is there a family with (A - B)/I -> 2)? Is Proposition 4 sharp? Find the best constants a, b, c such that
   A <= a B + b I and B <= a' A + b' I + c' Gamma can hold, from the 4-variable census (linear programs over the
   census are fine) and say which are proved and which are only observed.
4. State precisely the equivalence "FEI <=> B <= C' I" and "FEI <=> (A <= C I and Gamma <= C I)" with the constants
   that the proofs give in each direction.
Deliverables: PROOFS.md (the proofs), your scripts and their outputs, REPORT.md with a verdict line per statement:
PROVED / REFUTED (with the function) / GAP (with the exact step).
