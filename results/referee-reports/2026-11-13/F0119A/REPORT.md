RESOLVED_IN_LITERATURE

Task: “Open problem F0119” — 2026-11-13 08:43 Asia/Tbilisi, the first directly observed session clock; the prompt timestamp was unavailable.

For every integer \(b\ge2\), the answer for the specified three-state channel is

\[
\boxed{\text{reconstruction is solvable}\quad\Longleftrightarrow\quad
       b(1-3\epsilon)^2>1,\qquad 0\le\epsilon\le\tfrac12.}
\]

There is non-reconstruction at equality. This is Theorem 1.1, PDF page 3,
of OpenAI, *The exact reconstruction threshold for the three-state symmetric
channel*, dated September 25, 2026; its proof is assembled on page 33.
[Primary manuscript and verification package](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026).

The resolving reference is a public preprint. This audit did not establish
journal acceptance or a complete independent review of its analytic proof.
The status above means that the full statement and a proof are present in
public literature; it does not claim a new theorem of this project. The
exact-arithmetic certificates needed for its regular-tree argument were
independently replayed here and passed. Under the requested literature-stop
rule, no new proof search or population dynamics was undertaken.

The channel and the complete parameter region
-------------------------------------------

Mossel's equation (8), Section 5, PDF page 7, uses an off-diagonal parameter
\(\delta\), equal to the question's \(\epsilon\). Thus

\[
 M=(1-3\epsilon)I+\epsilon J,\quad
 M_{ii}=1-2\epsilon,\quad M_{ij}=\epsilon\ (i\ne j),\quad
 \lambda=\lambda_2=1-3\epsilon.
\]

Stochasticity gives \(0\le\epsilon\le1/2\), or \(-1/2\le\lambda\le1\).
Ferromagnetic means \(\lambda>0\), \(\epsilon<1/3\);
antiferromagnetic means \(\lambda<0\), \(\epsilon>1/3\).
The independent channel has \(\epsilon=1/3\); proper three-colourings have
\(\epsilon=1/2\), \(\lambda=-1/2\). The survey assumes ergodicity, excluding
\(\epsilon=0\). That endpoint extends the answer trivially because all
descendants then equal the root.
[Mossel 2004, Sections 2–5](https://arxiv.org/abs/math/0406446).

Put \(\epsilon_+(b)=(1-b^{-1/2})/3\) and
\(\epsilon_-(b)=(1+b^{-1/2})/3\). The entire region is:

| Branching | Solvable region in \(\epsilon\) | Unsolvable region in \(\epsilon\) |
|---|---|---|
| \(b=2,3,4\) | \([0,\epsilon_+(b))\) | \([\epsilon_+(b),1/2]\) |
| \(b\ge5\) | \([0,\epsilon_+(b))\cup(\epsilon_-(b),1/2]\) | \([\epsilon_+(b),\epsilon_-(b)]\) |

In particular, every antiferromagnetic channel is non-reconstructible for
\(b=2,3,4\). For \(b\ge5\), negative-side reconstruction occurs exactly for
\(-1/2\le\lambda<-b^{-1/2}\). At \(b=4\), the colouring endpoint is a
non-reconstructible equality.

These numerical boundaries evaluate the theorem; they are not simulations.

| \(b\) | Positive \(\lambda\) boundary | \(\epsilon_+(b)\) | Negative-side reconstruction in \(\epsilon\) |
|---:|---:|---:|---|
| 2 | 0.707106781187 | 0.097631072938 | empty |
| 3 | 0.577350269190 | 0.140883243603 | empty |
| 4 | 0.500000000000 | 0.166666666667 | empty; \(\epsilon=1/2\) is critical |
| 5 | 0.447213595500 | 0.184262134833 | \((0.482404531833\ldots,1/2]\) |
| 6 | 0.408248290464 | 0.197250569845 | \((0.469416096821\ldots,1/2]\) |

All positive boundaries are excluded from the solvable region. Use the
exact radical expressions when interpreting endpoints.

Proof that the cited theorem answers the original problem
-------------------------------------------------------

Mossel's Definition 2.1, PDF pages 2–3, asks whether two boundary laws
conditioned on different root states have nonzero limiting total variation
distance. Proposition 2.1, page 3, gives equivalent uniform-prior,
mutual-information, and optimal-success formulations. The resolving
paper's matrix (1.1), page 3, has diagonal \((1+2\lambda)/3\) and
off-diagonal \((1-\lambda)/3\). Substitution gives exactly Mossel's matrix.

To check definitions directly, write \(P_n^i\) for the boundary law given
root \(i\), \(P_n=(P_n^1+P_n^2+P_n^3)/3\), and \(p_n\) for the root
posterior under the uniform prior. Bayes' formula gives

\[
 A_n:=\mathbb E\|p_n-(1/3,1/3,1/3)\|_{\rm TV}
       =\frac13\sum_i\|P_n^i-P_n\|_{\rm TV}.
\]

Permutation symmetry makes every summand equal to \(A_n\), and all
distinct-root distances equal to a common \(d_n\). Triangle inequality
and convexity give \(d_n/2\le A_n\le2d_n/3\). Thus one tends to zero
exactly when the other does. The limits exist by information degradation.
The regular tree is deterministic, with no survival conditioning.
Forgetting sibling order does not change its posterior: the resolving
paper proves this in Lemma 2.1, page 6. Consequently its Theorem 1.1
applies to precisely the experiment in the question, and substitution
proves the boxed classification, including equality.

The proof dependencies in that reference are:

| Assertion | Exact location in the 2026 manuscript |
|---|---|
| Reconstruction for \(b\lambda^2>1\), either sign | Proposition 2.7, p. 11 |
| Non-reconstruction for \(0\le\lambda\le b^{-1/2}\), every \(b\ge2\) | Proposition 3.3, pp. 17–18; Section 3, pp. 12–18; radial inequality Lemma A.1, pp. 34–39 |
| At negative equality, a nonuniform symmetric fixed point must have \(\mu:=\mathbb E|\zeta|^2>1/20\) | Proposition 4.1, pp. 19–23; pair inequalities Lemma 4.2, pp. 19–20 |
| No such fixed point at \(\lambda=-b^{-1/2}\), integer \(b\ge5\) | Proposition 5.1, p. 23, regular range \(0<|\lambda|\le0.448\); Lemma 5.4, p. 26; Appendix B, pp. 39–46 |
| Four-child colouring has a dominating finite experiment with \(\mu<1/20\) | Section 6, pp. 27–32; stopping depth 162, p. 32; Proposition 6.3, pp. 32–33; arithmetic bounds, Appendix C, pp. 46–48 |
| Smaller degrees and weaker negative channels follow by degradation | Proposition 2.8, pp. 11–12; Proposition 6.3, pp. 32–33 |
| Complete assembly | Section 7, Table 1 and proof, p. 33 |

The positive argument compares an entropy functional's radial defect
with fixed-point identities. The negative argument combines the local
gap with a certified global inequality. The colouring case uses a finite
experiment dominating the true observation, with rounding losses replaced
by fully informative messages. It is an exact upper bound, not Monte Carlo.

Earlier results and the former gap
---------------------------------

Sly's *Reconstruction for the Potts model*, Ann. Probab. 39 (2011),
1365–1406, has preprint arXiv:0811.1208. The supplied arXiv:0905.3797
instead identifies an unrelated quantum-physics paper. Sly's Theorem 1.1,
saved PDF page 4, proves three-state KS sharpness for both signs, including
equality, for sufficiently large \(b\ge d_{\min}\). It supplies no numerical
cutoff establishing the small-degree cases.
[Sly's primary preprint](https://arxiv.org/abs/0811.1208).

His Section 1.5, equation (1.1), PDF page 6, uses
\[
 x_n=\mathbb E_1[p_{n,1}-1/3]
     =\mathbb E\sum_i(p_{n,i}-1/3)^2
\]
and, under the moment and concentration estimates in the argument,
\[
 x_{n+1}=b\lambda^2x_n-
        \frac34b(b-1)\lambda^4x_n^2+o(x_n^2).
\]
The negative second-order coefficient explains local attraction at KS.
It does not prove that fully informative initial data enter the small
region; Sly explicitly identifies this obstacle for small degrees on
page 7. The 2026 argument supplies global bounds.

The survey's known non-reconstruction criteria remain as stated:
\(b|\lambda|\le1\), or
\[
 \frac{b(1-3\epsilon)^2}{1-\epsilon}
       =\frac{3b\lambda^2}{2+\lambda}\le1.
\]
The latter is Mossel–Peres Proposition 1.3, saved PDF pages 4 and 11,
settling the interval
\[
 \left[\frac{1-\sqrt{1+24b}}{6b},
       \frac{1+\sqrt{1+24b}}{6b}\right]\cap[-1/2,1].
\]
It already covers the entire negative side for \(b=2\).
Bhatnagar–Maneva Theorem 12, PDF pages 17–18, covers three-colourings
at \(b=3\); degradation extends that to every weaker negative channel.
Neither settles four-child colouring equality. Full and census
reconstruction now have the same classification for this three-state
channel: full impossibility suffices below and at KS; the classical
census estimator suffices above KS.

[LITERATURE.md](LITERATURE.md) records the other requested authors,
theorems, pages, source versions, and the distinctions between
reconstruction, Gibbs uniqueness, mixing, and cavity predictions.

Checks performed and their limits
--------------------------------

The original survey is saved in [sources/mossel2004.txt](sources/mossel2004.txt).
Sections 2–5 were read, including subsections 5.1–5.2 on PDF page 10.
Source texts have PDF-page delimiters; `data/*.metadata.json` records URLs,
timestamps, page counts, and SHA-256 hashes. PDFs were extracted from RAM
through `pdftotext`; no PDF, image, scan, or screenshot was saved.
The resolving PDF was checked against pinned commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a` and is byte-identical to the
initial download from `main`.

The three certificate source hashes match Appendix D, PDF page 49.
[code/check_literature.py](code/check_literature.py) replayed the subset
needed for regular trees:

| Check | Outcome |
|---|---|
| Symbolic integer-polynomial pair checks, `pair.py` | Silent success, assertions enabled |
| Integer-interval case 0 | 414080 visited boxes; exit 0 |
| Integer-interval case 1 | 756096 visited boxes; exit 0 |
| Four-child colouring upper recursion, `grid -1` | Exactly `-1 162`; exit 0 |

C++ builds used Apple clang 17.0.0, C++17, `-O2`, `-UNDEBUG`,
`-fsanitize=undefined`, and `-fno-sanitize-recover=undefined`. No run
reported sanitizer errors. Python was 3.13. The final audit's maximum
recorded child RSS was 153206784 bytes, about 153 MB. Runs were sequential,
inherited nice 10, and used single-thread library settings. The
Poisson-only interval case 2 and grid cases 0–26 were not rerun; this is
not the package's complete 37-record regular-and-Poisson replay.
Commands and logs are in
[data/literature_checks/summary.json](data/literature_checks/summary.json).

[code/audit_parameters.py](code/audit_parameters.py) checked the channel
on two mean-zero eigenvectors, both forms of the revealing-colour ratio,
and an independent quadratic expansion of the KS condition, at 101
rational parameters and every \(b=2,\ldots,6\). The radical endpoints
were also checked at 60-digit precision; see [data/thresholds.csv](data/thresholds.csv).

The analytic proof remains attributed to the preprint. Certificate success
establishes its finite algebraic assertions, not an independent end-to-end
formalisation of its probability arguments. No population dynamics, new
range claim, push, or publication was produced.
