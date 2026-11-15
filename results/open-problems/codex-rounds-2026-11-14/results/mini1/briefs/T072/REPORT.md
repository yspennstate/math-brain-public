VERDICT: PROVED an explicit finite-n bound and sharp leading degree cutoff for the planted-clique low-degree likelihood-ratio norm.

The full planted clique conjecture remains open. This is a self-contained restricted-model theorem; no claim of novelty over the established low-degree literature is made.

Let Q=G(n,1/2), let P plant a uniform k-subset, and let L_{≤D} be the degree-D projection of dP/dQ in the signed edge variables. Define

\[
A=\max_{0<p\le1/2}\frac{H_2(p)}{\sqrt{2p}},\qquad
C_*=4/A^2,\qquad q=(k^2/n)2^{A\sqrt D}.
\]

PROOF.md proves, for every integer n≥2, 0≤k≤n, D≥0,

\[
0\le\|L_{\le D}\|_2^2-1\le e^q-1-q\le q^2e^q/2.
\]

For fixed ε∈(0,1/2), k=⌊n^{1/2−ε}⌋, and any fixed δ∈(0,1), the squared norm tends to one when D≤(1−δ)C_*ε²(log₂n)² and diverges when D≥(1+δ)C_*ε²(log₂n)². The constant is characterized exactly by

\[
C_*=8p_*/H_2(p_*)^2,
\quad (1+p_*)\ln(1-p_*)=p_*\ln p_*,
\quad 1/5<p_*<1/4.
\]

No decimal optimization or unverified numerical constant is used. The proof gives every counting and entropy estimate and tracks integer rounding. The degree threshold has matching leading coefficient with fixed multiplicative slack; behavior in the critical window is not determined.

The implication is vanishing normalized mean separation for degree-D polynomials below the cutoff. It also rules out constant distinguishing advantage for acceptance functions that are themselves degree-D polynomials with values in [0,1]. It does not establish lower bounds for all polynomial thresholds, general polynomial-time algorithms, or recovery. Divergence above the cutoff alone does not prove strong detection.

Audit: the exact norm was re-derived using the hypergeometric overlap of two planted sets. Exact hand calculations for (n,k)=(4,2) and (5,3) agree degree by degree. At full degree, ordinary edge-count and triangle-count second moments supply a third check. The cutoff constant was derived both from an upper entropy envelope and from optimizing a lower fixed-density graph contribution. Details and endpoint checks are in LOG.md, Section 8.

Literature search: no qualifying post-status resolution was verified within the ten-minute search. Opened Dmitriy Kunisky and Songtao Mao, [arXiv:2609.24780v1](https://arxiv.org/abs/2609.24780), including its full HTML and PDF. Its Theorem 1.12 improves runtime at fixed square-root-scale signal. It predates the supplied November cutoff and does not settle the target regime. Opened Riddhi Ghosal, Isaac M Hair, Aayush Jain, Amit Sahai, [arXiv:2611.11701](https://arxiv.org/abs/2611.11701); its abstract assumes planted-clique hardness for a cryptographic application. Neither is used as an unproved ingredient of PROOF.md. The search cannot certify absence of other work.

Commands and computation: there was no numerical program or experiment. All mathematical checks are symbolic or exact hand arithmetic, recorded in LOG.md. Inspection used `pwd`, `rg --files ...`, and `cat ...`; files were edited with the patch tool. The initial orientation command `OMP_NUM_THREADS=1 nice -n 15 python3 ~/.claude/dreaming/brain.py recall "planted clique low degree lower bound"` printed `nice: setpriority: Operation not permitted`; the sandbox also denied `ps`. No numerical program was launched after that failure.

What failed: an initial plan to stop at the September runtime improvement did not meet the date/scope requirement. That decision was corrected in LOG.md before the theorem was developed, and the provisional SOLVED_ELSEWHERE.md was removed. Attempts to infer threshold-test hardness or recovery from the norm calculation do not follow from the proved inequalities and are expressly excluded.

Next worker: first compare the explicit constant and finite bound with the existing low-degree literature before claiming a new result. A concrete mathematical continuation is to locate the critical window around C_*ε²(log₂n)², retaining the v! factor and the non-isolation correction. These terms are lower order for the theorem here but cannot be discarded in that window.

Task: “push this problem forward by one checkable piece.” Received 2026-11-14, approximately 20:51 local machine time; the exact request timestamp was not supplied.
