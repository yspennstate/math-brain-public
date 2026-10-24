# B12 lead - learned

## 2026-10-11 (run 20261011T225832Z-claude-B12-erasure-ledger-depth)
- The A057 packet function L_j(x)=sum_T phi(a_T^2, x b_T^2) is nondecreasing and concave with L_j(1)=B_j(g). Use the cap B_j(g) next to A057's concavity bound; on odd gates it gives the exact value 0.
- For balanced Boolean h, sum_i hhat(i)^2 ln(1/hhat(i)^2)<=(4+6/e)(I(h)-1) nats (largest-coefficient term <=2u<=4(I-1), the rest <=(2/e)*3(I-1)). Best ratio seen: 3 ln2 at Maj3.
- Odd functions have zero erasure entropy at every coordinate (Fourier sets all odd), so odd threshold chains are a clean test bed: any bound with a positive bank is loose there, and the recharged whole-subformula bank grows like 2^k against I<k.
- A058's private anchors make every outer label visible in the physical support, so overlapping shared gates cost nothing extra; the collision problem starts only when an anchor is shared.
- Exact checks of entropy identities: Walsh coefficients are integers over 2^n, so every entropy is a rational combination of logs of primes; compare the vectors. 6,468 identities ran in seconds.
- Practicalities: heredoc scripts with many quotes broke the Bash tool's parser here; write scripts with the Write tool. Python launched from Git Bash gets /c/ paths converted only when they are arguments, not inside -c strings. The subagent Write tool refuses REPORT.md; return report content in the structured output.
