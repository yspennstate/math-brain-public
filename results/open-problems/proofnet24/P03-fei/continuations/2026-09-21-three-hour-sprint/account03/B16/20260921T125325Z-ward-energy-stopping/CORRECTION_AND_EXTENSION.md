# B16 correction and extension — the aggregate Ward operator has an exponential generic mode

**Scope:** additive correction/extension to this run's immutable `REPORT.md`.  
**Execution label:** **WITHOUT_VERIFIED_BRAIN**.  
**Full FEI:** **OPEN / NOT PROVED**.

## 1. Narrow correction to REPORT.md §6

The relationwise results `P03-B16-ODD-BLOCK-BIRTH-LAW`, `P03-B16-WARD-SELECTOR-ENERGY`, and `P03-B16-WARD-PYTHAGORAS` do **not** depend on this correction and remain unchanged.

One sentence in §6 of `REPORT.md` was too broad. The account04 refinement-defect theorem that was cited there proves the third-and-higher-curvature description for its **clone-pair refinement**. It does not, by itself, prove that an arbitrary binary block refinement of the whole R32 polynomial is exactly the same higher-curvature operator. For a general hierarchy, that identification is therefore **OPEN** and must be derived before the inherited plaquette/noisy-square bank can be applied.

The valid statement at present is only: relation by relation, the block selector admits the exact energy and orthogonality identities proved in §§1–3; summing different relations creates cross terms which are not controlled by those identities alone.

## 2. Attack the aggregate square-function shortcut directly

There is a very tempting continuation after the relationwise Pythagorean theorem: sum the squared relation coefficients and hope that the map from signed relation coefficients to fine q-flip Shapley loads has a dimension-free Hilbert-space norm. That shortcut is false even before one asks about physical edge routing.

Fix an active q-flip set `M` with odd cardinality parameter left arbitrary; write `m=|M|`. Consider the abstract signed parity polynomial containing one coefficient `c_R` for every odd nonempty subset `R subseteq M`. Its fine Shapley load on player `v` is

\[
 (T_m c)_v
 =\sum_{\substack{R\subseteq M\\ |R|\ {m odd}\\v\in R}}
 \frac{c_R}{|R|}.
\tag{2.1}
\]

Thus the matrix of `T_m` is

\[
 (T_m)_{v,R}=\frac{1_{\{v\in R\}}}{|R|}.
\tag{2.2}
\]

This is exactly the linear aggregation operator produced by the `c/q` fine parity selector when one forgets the special R32 coefficient restrictions. It preserves coefficient signs; no absolute value has been inserted.

### Theorem 2.1 — `P03-B16-GENERIC-WARD-OPERATOR-OBSTRUCTION` — **PROVED**

For every `m>=1`,

\[
\boxed{
 \|T_m\|_{\ell_2(\{R:|R|\ {m odd}\})\to\ell_2(M)}^2
 =\frac{2^{m-1}}{m}.
}
\tag{2.3}
\]

Consequently no dimension-independent generic `l2` estimate can aggregate the relationwise Ward energies. The norm itself grows as

\[
\boxed{\|T_m\|=\sqrt{2^{m-1}/m}.}
\tag{2.4}
\]

#### Proof

By permutation symmetry of `M`, `T_mT_m^*` has one diagonal entry `a_m` and one off-diagonal entry `b_m>=0`. Hence it has the constant vector as an eigenvector, with eigenvalue equal to the common row sum, and the orthogonal complement has eigenvalue `a_m-b_m`. Since `b_m>=0`, the constant eigenvalue is the largest.

The row sum can be computed without evaluating `a_m` or `b_m` separately. For the all-ones vector `1_M`,

\[
 (T_m^*1_M)_R
 =\sum_{v\in M}\frac{1_{\{v\in R\}}}{|R|}=1
\]

for every odd nonempty `R`. Therefore

\[
 \langle 1_M,T_mT_m^*1_M\rangle
 =\|T_m^*1_M\|_2^2
 =\#\{R\subseteq M:|R|\text{ odd}\}
 =2^{m-1}.
\]

Dividing by `\|1_M\|_2^2=m` gives the constant-mode eigenvalue `2^{m-1}/m`, which is the spectral radius. This proves (2.3)–(2.4). `square`

Equivalently, direct row counting gives

\[
 a_m=\sum_{\substack{k\le m\\k\ {m odd}}}
 \binom{m-1}{k-1}\frac1{k^2},
 \qquad
 b_m=\sum_{\substack{k\le m\\k\ {m odd}}}
 \binom{m-2}{k-2}\frac1{k^2},
\]

and

\[
 a_m+(m-1)b_m
 =\sum_{k\ {m odd}}\binom{m-1}{k-1}\frac1k
 =\frac1m\sum_{k\ {m odd}}\binom mk
 =\frac{2^{m-1}}m.
\]

### Exact scale examples

\[
\begin{array}{c|c|c}
 m & \|T_m\|^2 & \|T_m\|\\ \hline
 1 & 1 & 1\\
 3 & 4/3 & 1.154700\ldots\\
 5 & 16/5 & 1.788854\ldots\\
 9 & 256/9 & 16/3\\
 17 & 65536/17 & 62.089\ldots\\
 33 & 2^{32}/33 & 11408\ldots
\end{array}
\]

The exponential growth is not a constant-factor defect.

## 3. Exact scope of the obstruction

This theorem is **not** a counterexample to FEI and is **not** an assertion that the actual R32 coefficient vector realizes the bad constant mode. The genuine R32 vector is highly structured:

- coefficients are radial in the original relation weight through `(-1)^{|A|/2}I_{|A|,N}` or their Borel versions;
- only `C_0\setminus D_d` appears at the retained prefix;
- one q-flip basis identifies relations with binary coefficient subsets, but original relation weight is not arbitrary in those coordinates;
- R16 retains moment/high-resolvent refunds;
- `2 mod 4` terms are negative credits rather than independent positive masses;
- the terminal response is separately retained.

What (2.3) **does** rigorously refute is the generic continuation

> “relationwise Pythagoras plus a dimension-free `l2` operator estimate, with no use of the special R32 coefficient structure, closes the aggregate square-function step.”

That continuation is **REFUTED**. Any successful Ward-stopping proof must eliminate or pay the exponentially dangerous representation modes using the actual signed R32 structure.

## 4. Sharpened next attack

The constant player mode in Theorem 2.1 is the first exact target. It is also conceptually compatible with two positive results already in the fleet:

1. the account03 dummy-coordinate Ward identity cancels a dangerous low-frequency mode on monomial-defect families; and
2. the account02 equivariant random-basis theorem forces exact signed redistribution on transitive disagreement-edge orbits.

The next calculation should therefore **not** be another arbitrary-coefficient norm bound. It should project the genuine R32 coefficient vector, at a fixed Borel time or retained prefix, onto the constant and next permutation-isotypic components of the q-flip player representation and compute those components using the original relation-weight signs and multiplicities.

A useful outcome would be one of the following.

- **PROVED route:** the dangerous constant/low modes are exactly a Ward/terminal or R16 moment term already retained, leaving only a mean-zero component that the fractional noisy-square bank can pay.
- **REFUTED route:** an admissible Boolean phase and genuine R32 coefficient vector has an unbounded surviving low-mode ratio after all retained refunds, killing the Ward-stopping mechanism.

Until that structured projection is proved, the aggregate signed square-function bridge and unrestricted FEI remain **OPEN**.
