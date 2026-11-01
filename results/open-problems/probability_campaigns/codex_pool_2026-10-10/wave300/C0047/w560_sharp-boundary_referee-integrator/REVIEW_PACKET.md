# w560 review packet for C0047, 2026-10-10

## Reviewed snapshots

- w558 `ATTEMPT.md` SHA256 `5B109745182BD6F210EFC0931E7BDCAFD8A024AD486F1BC629B665537B8941DC`; `CLAIMS.jsonl` SHA256 `427F6F57D518542286B6E0CEB7F09A84BD9DB67437C3E3B5934552E8CA8BAE5B`.
- w559 `CLAIMS.jsonl` SHA256 `C399B32841EE9ECCAE7195355349331B853EBEE8497F155DA474F1DA2B4865E0` (one provenance row at review time).
- w559 later snapshot: `ATTEMPT.md` SHA256 `DF0DD85C512A52C307C704D1909E879E4551EE34F05DD5EA292BCB6B5137EB58`; `CLAIMS.jsonl` SHA256 `B36B44B7911658B20BEB9D28CA5FF8A4C1B8D95464AFEDB251A01FF89978BADC`; `MEASUREMENTS.json` SHA256 `D1306D1E0E07F9CC667D62043C29444D4C8A32C6290D7FAAC1B98FF694191610`.
- Original source: https://emis.de/ft/41630, pages 2 and 6.
- Spectral criterion: https://arxiv.org/html/1206.2183v3, Section 1, equation (3).
- Free-product threshold comparator: https://arxiv.org/html/math/0611668, Theorem 1.
- Recent bond manuscript: public OpenAI math result 214, PDF in this folder; proof not fully audited.

## Verdicts with reproduction

**w559-source-001 — KEEP as dated provenance only.** Ranking line 431 really says tier 4 / `attempted_un` and every-Cayley wording. Its row correctly withholds proof and current openness. The source-status work must additionally state the 1996 graph and site/bond scope and the 2026 bond manuscript claim; the ranking cannot certify current openness. No mathematical proof is inferred.

**w558-L0 — KEEP, classical bond tree special case.** I rederive $p_c=1/(d-1)$ from independent $\mathrm{Binomial}(d-1,p)$ descendant offspring and critical extinction. For any $p\in(p_c,1)$, side subtrees off a fixed ray are disjoint; each has positive survival probability, while its attaching edge is independently closed with probability $1-p$. Infinitely many isolated surviving subtrees occur almost surely, precluding uniqueness. The at/below-$p_c$ and $p=1$ endpoints are handled. It is a special case only.

**w558-L1 — KEEP within the stated family.** Independently collapse the $a$-lines of the ordinary $F_2$ Cayley tree. A $b$-edge joins distinct lines and no quotient cycle can occur, so each is a bridge. For an arrived line, its fresh horizontal cluster has size $K_N$ and its distinct fresh $b$-edges number exactly $2K_N-1$. All these edges and subsequent factor lines are disjoint; hence offspring is a mixture $\mathrm{Binomial}(2K_N-1,p)$ with mean $p(2\chi_N-1)$. Closed cuts crossing at most $N$ steps give a geometric confinement tail for $K_N$ at $p<1$, so the branching process has finite mean and the critical equality is valid. At $N=1$, $\chi_1=(1+p)/(1-p)$ gives $p(2\chi_1-1)=1$ exactly at $p=1/3$. Kozakova's published free-product equation $(\chi_a-1)(\chi_b-1)=1$ reproduces the same condition after $\chi_b=(1+p)/(1-p)$. No extension to arbitrary Cayley graphs follows.

**w558-L1 uniqueness part — KEEP.** The chosen $b$-side components along the deterministic $b$-ray are disjoint and have one attaching bridge each. In each, survival above the branching threshold is positive and the attaching bridge is closed independently with probability $1-p$. These disjoint events occur infinitely often, giving infinitely many infinite clusters for $p_c<p<1$ and $p_u=1$. The bridge property is essential; a graph with relations need not have it.

**w558-L2 — KEEP within the stated family.** In the spanning 4-regular tree, a finite set $A$ has $4|A|-2(|A|-c)=2|A|+2c$ outgoing edges. For $A_L=\{1,a,\ldots,a^{L-1}\}$, the full graph has $2L+N(N+1)$ outgoing edges; the ratio tends to $2$, so $\phi_E=2$. The normalized conductance is $2/(2N+2)=1/(N+1)$. The indicator Rayleigh quotient is $[2\sum_{k=1}^N(L-k)]/[(2N+2)L]=N/(N+1)-N/(2L)$. The standard tree adjacency has norm $2\sqrt3$, and the other $2N-2$ generator translations each norm one; thus the stated upper bound follows. Both bounds approach one as $N\to\infty$, refuting a generating-set-uniform spectral gap. This does not refute individual nonamenability or C0047.

**w558-C0 — KEEP as a source correction.** Juschenko–Nagnibeda defines $\rho=\|\sum_{s\in S}\lambda(s)\|/|S|$ and explicitly prints $\rho p_c|S|<1$ as the sufficient hypothesis. The September C0047 attempt instead says $p_c<1/\rho$, dropping $|S|$. Since $\rho<1$ and $p_c\le1$ on a nonamenable Cayley graph, the mistaken condition is automatic. This is a live attempt-record correction, not a new parent theorem.

**w558-L3 — KEEP, counterexample to necessity of the sufficient criterion.** For the standard 4-regular tree, $p_c=1/3$ and $p_u=1$. Radial test functions $f_R(v)=3^{-d(o,v)/2}$ on balls of radius $R$ have squared norm $1+4R/3$ and adjacency form $8R/\sqrt3$. Their ratio tends to $2\sqrt3$; the matching parent/three-child bound gives the reverse inequality. Thus $\rho=\sqrt3/2$ and $D\rho p_c=2\sqrt3/3>1$ despite $p_c<p_u$. This tests necessity, not the parent conjecture.

**w558-L4 — KEEP arithmetic, with upper bounds only.** Degree $D=2N+2$ gives $p_c\ge1/(D-1)$. Direct neighbors give $\chi_N\ge1+2Np$, hence $p_c\le(\sqrt{1+16N}-1)/(8N)$. For $N\ge2$, an open length-two edge and a closed adjacent nearest edge make the corresponding $\pm2$ vertex an extra member of the horizontal root cluster, each with probability $p(1-p)$. The two gain indicators are added pointwise, so no independence is used. Substitution yields the printed quartic and an upper-bound root below $1/3$; it is not an exact $p_c$ formula for $N\ge2$.

**w559-source-002 — KEEP as normalization correction.** Its original-paper citation says $\rho(G)kp<1$ and its corroborating source states $\rho p_c|S|<1$. These match when $k=|S|$ and one chooses a parameter $p>p_c$ below the sufficient-condition bound. The old intake condition is missing the degree factor. This review verifies source wording, not the historical theorem's full proof.

**w559-special-001 — KEEP within $C_2*C_3$.** The Cayley graph's $b$-edges form disjoint triangles. Every $a$-edge joins distinct triangle blocks, and free-product normal forms make the contracted graph a 3-regular tree. For a finite vertex set $F$, the induced graph has cyclomatic number equal to its number $t$ of full triangles, so $|E(F)|=|F|-c+t$ and $|\partial_EF|=|F|+2c-2t\ge|F|/3+2c$. A connected $k$-block subtree has $3k$ vertices and $k+2$ boundary edges, proving $h_E=1/3$. This in turn proves positive vertex isoperimetry, since degree is three.

For the branching calculation, condition on entry through an open $a$-edge. Let $K$ count the other two vertices in the triangle connected to the entry by open triangle edges. Enumerating the three internal edges gives $P(K=0)=(1-p)^2$, $P(K=1)=2p(1-p)^2$, and $P(K=2)=3p^2-2p^3$. Each of those $K$ vertices has one fresh outward $a$-edge, independent of all internal edges and of other blocks. Thus $X\mid K\sim\mathrm{Binomial}(K,p)$ and $EX=2p^2+2p^3-2p^4=:M(p)$. The derivative $M'(p)=2p(2+3p-4p^2)>0$ on $(0,1)$, giving a unique threshold root $q$ of $M(q)=1$. The nondegenerate critical branching process dies out, and countability eliminates infinite clusters at or below $q$. For $p>q$, isolate off-ray branch blocks with independently closed $a$-bridges and surviving forward clusters; infinitely many occur, while $p=1$ gives one cluster. Hence $p_c=q$ and $p_u=1$. The supplied 32-configuration run supports the finite algebra but is not used as the proof of the infinite reduction.

**w559-bridge-001 — KEEP as a counterexample to auxiliary implications.** The indicator of one full triangle has adjacency Rayleigh quotient $6/3=2$, so normalized $3\rho p_c=\|A\|q\ge2q$. Direct substitution gives $M(0.63)<1<M(0.64)$, hence $q>0.63$ and $3\rho p_c>1.26$. Also $q>0.5=1/(d-1)$ for $d=3$. Thus nonamenability does not force either proposed bound on this prescribed graph. The example satisfies $p_c<p_u$ and does not refute the parent conjecture.

## Publication and model gates

The w558 and w559 mathematical results have one independent manual referee here and cited prior art. This packet does not certify the authors' or referee's served model, a second-account audit, novelty, or a parent-problem solution. The 2026 bond manuscript is a primary claim with a concrete theorem and long proof, but its public `BenjaminiSchramm.lean` comparator has `sorry` for `full_main`, `critical_laws`, and `cayley_main`. The comparator alone cannot close proof review.

NEXT: Have another account review the source correction and peer special cases; have w563 independently audit my site-tree lemma; audit Theorem 2.6 before retiring the bond target as proven.
