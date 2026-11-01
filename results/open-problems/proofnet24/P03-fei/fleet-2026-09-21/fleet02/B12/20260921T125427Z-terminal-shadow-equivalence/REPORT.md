# B12 FEI spectral-sample compression — logarithmic shadow gain and exact terminal equivalence

TASK: B12 ACCOUNT: fleet02 RUN: 2026-09-21T12:54:27.763687Z  
CURRENT WORK: exact compression reduction for the full uniform-cube Fourier entropy-influence conjecture  
ROLE: FEI approach 1 — spectral-sample compression / sequential prediction  
EXECUTION: WITHOUT_VERIFIED_BRAIN  
STATUS: FULL FEI REMAINS OPEN. The results below are exact reductions, a martingale/Shapley reformulation, and a no-go for pointwise coding. They do not prove FEI and make no novelty or publication-priority claim.

## Live dependencies and scope

The required 2026-09-21 FEI owner entry was read in order: `TASKS_2026-09-21.md`, the read-once `REPORT.md`, `APPROACHES.md`, and the fresh P03 README. The current task prompt assigns B12 to spectral-sample compression/sequential prediction. The active sprint document was also read; its slot-local read-once numerical subassignment conflicts with this direct current B12 role, so this run did not duplicate the region-2 certificate work already split across the sprint. It did use the sprint's rigorously recovered current unrestricted lower-bound seed as a calibration dependency.

The immediate predecessor is fleet02/B12 `20260921T122750Z-terminal-shadow-selector`, which proved
\[
v_A:=\sum_{B\supseteq A}\frac{p_B}{\binom{|B|}{|A|}},\qquad
R_{\rm seq}:=-\sum_A p_A\log_2 v_A,
\]
and the exact decomposition
\[
H(P)=B_{\rm sh}(P)+R_{\rm seq}(P),\qquad
B_{\rm sh}:=\sum_Ap_A\log_2\frac{v_A}{p_A}.
\]
It left a universal Boolean bound on \(R_{\rm seq}/I\) open.

This run used three new FLEET_RULES moves: **#3 prove something stronger** (identify the exact sharp constant of the terminal inequality, not merely a sufficient one), **#12 find what is conserved** (the total prefix-shadow mass is exactly \(1+I\)), and **#18 say it in another language** (identify \(v_A\) as a Shapley/martingale interaction average).

## 1. A stronger generic shadow bound

Let \(P\) be any probability law on subsets of a finite set, \(p_A=P(S=A)\), \(K=|S|\), and \(I(P)=\mathbb E K\). The definition of \(v_A\) gives, for every level \(a\),
\[
\sum_{|A|=a}v_A
=\sum_{B:|B|\ge a}p_B
  \frac{\binom{|B|}{a}}{\binom{|B|}{a}}
=P(K\ge a).
\]
Therefore
\[
\boxed{\sum_A v_A=1+\mathbb E K=1+I(P).} \tag{1}
\]

Now apply Jensen to the concave logarithm, with terms having \(p_A=0\) omitted:
\[
\begin{aligned}
B_{\rm sh}(P)
&=\sum_{p_A>0}p_A\log_2\frac{v_A}{p_A}\\
&\le
\log_2\left(\sum_{p_A>0}p_A\frac{v_A}{p_A}\right)\\
&=\log_2\left(\sum_{p_A>0}v_A\right)
\le \boxed{\log_2(1+I(P)).} \tag{2}
\end{aligned}
\]
This holds for **every subset law**, with no Booleanity assumption. Since
\(\log_2(1+x)\le(\log_2e)x\), (2) strictly strengthens the earlier generic
\(B_{\rm sh}\le(\log_2e)I\) except infinitesimally near \(I=0\).

Combining (2) with the predecessor's exact identity,
\[
\boxed{H(P)-\log_2(1+I(P))\le R_{\rm seq}(P)\le H(P).} \tag{3}
\]
The upper bound is simply \(v_A\ge p_A\).

The important feature is not the additive improvement at a fixed function. It is that
\[
\frac{B_{\rm sh}}I\le \frac{\log_2(1+I)}I\longrightarrow0
\qquad(I\to\infty). \tag{4}
\]
Thus the terminal quantity asymptotically carries *all* of the spectral entropy on high-influence amplification sequences.

## 2. The terminal-shadow constant is exactly the FEI constant

Define the extended-real sharp constants over nonconstant Boolean functions on uniform cubes,
\[
C_H:=\sup_f\frac{H(f)}{I(f)},\qquad
C_R:=\sup_f\frac{R_{\rm seq}(f)}{I(f)}.
\]

### Theorem
\[
\boxed{C_R=C_H.} \tag{5}
\]

### Proof

Because \(v_A\ge p_A\), \(R_{\rm seq}(f)\le H(f)\), so \(C_R\le C_H\).

For the reverse inequality, fix any nonconstant Boolean \(f\). Introduce one fresh uniform bit \(z\) and form the balanced lift
\[
g(x,z)=z\,f(x).
\]
Its spectrum is exactly the spectrum of \(f\) shifted by the new coordinate:
\[
\widehat g(A\cup\{z\})=\widehat f(A),\qquad
\widehat g(B)=0\quad(z\notin B).
\]
Hence
\[
H(g)=H(f)=:h,\qquad I(g)=I(f)+1=:i>1. \tag{6}
\]

Starting from a dictator \(F_0\), recursively substitute independent copies of \(F_r\) into every input of the balanced seed \(g\):
\[
F_{r+1}=g(F_r^{(1)},\ldots,F_r^{(m)}),
\]
with all input blocks disjoint. The standard balanced spectral factorization, also proved in the current sprint dependency, gives
\[
I(F_r)=i^r,\qquad
H(F_r)=h\,\frac{i^r-1}{i-1}. \tag{7}
\]
Applying (3) to each finite Boolean \(F_r\),
\[
\frac{R_{\rm seq}(F_r)}{I(F_r)}
\ge
\frac{h}{i-1}(1-i^{-r})
-\frac{\log_2(1+i^r)}{i^r}. \tag{8}
\]
The final term tends to zero. Therefore
\[
C_R\ge \lim_{r\to\infty}\frac{R_{\rm seq}(F_r)}{I(F_r)}
\ge \frac{h}{i-1}
=\frac{H(f)}{I(f)}.
\]
Since \(f\) was arbitrary, \(C_R\ge C_H\), proving (5). \(\square\)

### Consequence

The predecessor report described a terminal bound \(R_{\rm seq}\le C_R I\) as a sufficient route that would combine with the linear shadow bound and therefore discussed targets such as “Hod minus \(\log_2e\).” Equation (5) shows that this is **not the sharp calibration**. A universal terminal-shadow inequality with constant \(C\) is, after balanced amplification, equivalent to FEI with the **same optimal constant** \(C\).

The sprint's independently reconstructed Numaro balanced \(18\)-variable seed has
\[
\frac{H(g)}{I(g)-1}>6.521845710923046575.
\]
By exactly the same amplification and (5),
\[
\boxed{C_R=C_H>6.521845710923046575.} \tag{9}
\]
Thus any attempt to prove the terminal inequality with constant near \(5\) is impossible. The earlier fleet02 addressing calibration \(R/I\to4\) remains correct but is not extremal for the terminal constant.

Full FEI is still OPEN: (5) is an exact reformulation, not the missing universal upper bound.

## 3. Input-side meaning of the shadow: Shapley interactions of a bounded martingale

The new reduction is only useful if \(v_A\) can be attacked using Boolean structure rather than as an arbitrary subset law. There is an exact input-side representation.

For a Boolean \(f\), let
\[
V(T):=\left\|\mathbb E[f\mid x_T]\right\|_2^2
=\sum_{B\subseteq T}p_B. \tag{10}
\]
For nonempty \(A\) and \(T\cap A=\varnothing\), define the mixed finite difference
\[
\Delta_A V(T)
:=\sum_{C\subseteq A}(-1)^{|A|-|C|}V(T\cup C)
=\sum_{D\subseteq T}p_{A\cup D}. \tag{11}
\]
Let \(\pi\) be a uniformly random permutation of all coordinates and let
\[
P_A(\pi):=\{j\notin A:\ j\text{ appears before every element of }A\}.
\]
For a fixed \(D\subseteq A^c\), all elements of \(D\) precede all elements of \(A\) with probability
\[
\frac{|D|!\,|A|!}{(|A|+|D|)!}
=\frac1{\binom{|A|+|D|}{|A|}}.
\]
Averaging (11) therefore gives the exact identity
\[
\boxed{
v_A=\mathbb E_\pi\,\Delta_A V(P_A(\pi)).
} \tag{12}
\]

If \(D_A\) denotes the normalized iterated discrete derivative, Fourier orthogonality gives the equivalent norm form
\[
\Delta_A V(T)
=
\left\|D_A\,\mathbb E[f\mid x_{T\cup A}]\right\|_2^2. \tag{13}
\]
Thus
\[
\boxed{
v_A=
\mathbb E_\pi
\left\|D_A\,\mathbb E[f\mid x_{A\cup P_A(\pi)}]\right\|_2^2.
} \tag{14}
\]

For \(|A|=1\), (12) is exactly the Shapley value of the variance game \(V\): reveal coordinates in random order and measure the squared-martingale increment when coordinate \(i\) is reached. For higher \(A\), it is the corresponding positive mixed Shapley interaction.

Combining with the terminal identity yields the exact Boolean compression target
\[
R_{\rm seq}(f)
=
\mathbb E_{S\sim p}\left[
-\log_2
\mathbb E_\pi
\left\|D_S\mathbb E[f\mid x_{S\cup P_S(\pi)}]\right\|_2^2
\right]. \tag{15}
\]
This formulation preserves the bounded martingale \(\mathbb E[f\mid x_T]\in[-1,1]\), unlike the earlier projected-spectral-law route that lost the cross-block selector information. By (5), proving (15) \(\le C I(f)\) universally is exactly FEI at constant \(C\).

## 4. A pointwise coding bridge is impossible

A tempting next step would be to seek a pointwise lower bound
\[
v_A\ge 2^{-C|A|}
\quad\text{for every Fourier-supported }A. \tag{16}
\]
This is false for genuine Boolean functions for every fixed \(C\).

Take \(n\)-bit AND (the sign convention changes coefficient signs but not their squares). Every nonempty Fourier coefficient has magnitude \(2^{1-n}\), so for every nonempty \(B\),
\[
p_B=4^{1-n}.
\]
For a singleton \(A=\{i\}\),
\[
\begin{aligned}
v_{\{i\}}
&=4^{1-n}\sum_{k=1}^n\frac{\binom{n-1}{k-1}}k\\
&=4^{1-n}\frac{2^n-1}{n}, \tag{17}
\end{aligned}
\]
using \(\binom{n-1}{k-1}/k=\binom nk/n\). Therefore
\[
-\log_2 v_{\{i\}}
=
n-2+\log_2 n-\log_2(1-2^{-n})
\longrightarrow\infty, \tag{18}
\]
while \(|A|=1\).

The terminal theorem must therefore be **mass-weighted**. The bad singleton atoms in AND have probability \(4^{1-n}\), so (18) does not threaten the average \(R_{\rm seq}\). This rules out a whole class of coefficientwise prefix-code proofs and focuses the next step on an averaged martingale/Shapley inequality.

## 5. Executed finite self-check

`verify_terminal_shadow_equivalence.py` is a bounded exact-arithmetic self-check of the algebraic identities, not a proof substitute. On a rational full-support law on \(2^{[4]}\) it verifies with `fractions.Fraction`:

- all five level-shadow identities and \(\sum_Av_A=1+I\);
- all 16 prefix recurrences \(\sum_{i\notin A}v_{A\cup i}=(|A|+1)(v_A-p_A)\);
- all 360 permutation/mixed-difference instances underlying (12);
- the AND singleton formula (17) for every \(2\le n\le12\).

The run returned `PASS`. The Jensen comparison is also evaluated numerically as a sanity check; the universal proof is the displayed algebra above.

## 6. What changed and next attack

**Before:** the terminal remainder was a useful sufficient target, but its apparent sharp constant was miscalibrated by adding the linear shadow estimate. The cross-block resource needed by a sequential proof was qualitative.

**After:** the shadow gain is only logarithmic in total influence, the sharp terminal constant is **exactly** the sharp FEI constant under balanced amplification, and each terminal shadow \(v_A\) is an averaged positive Shapley/martingale interaction. A pointwise coefficientwise code is rigorously dead.

The next B12 attack is therefore precise: use the bounded-martingale structure in (14) to prove an *averaged* lower-tail inequality for the random mixed interaction
\[
\Delta_S V(P_S(\pi)),
\]
strong enough to control its logarithmic mean by \(C\,\mathbb E|S|\). The natural first tests are (i) a good-\(\pi\)/bad-\(\pi\) truncation using bounded martingale square-function energy and (ii) an entropy/Carleson packing inequality over the random-order interaction tree. Either must survive AND's tiny individual atoms and addressing's selector transfer. No claim is made yet that such an inequality holds.

## Ledger

- **PROVED (algebraically):** total uniform-prefix shadow mass \(\sum_Av_A=1+I\).
- **PROVED (algebraically):** \(B_{\rm sh}\le\log_2(1+I)\) for every subset law.
- **PROVED (algebraically):** the sharp Boolean terminal-shadow constant equals the sharp FEI constant.
- **PROVED (algebraically):** exact Shapley/martingale representation (12)--(15).
- **DISPROVED:** any dimension-free pointwise bound \(v_A\ge2^{-C|A|}\) on all supported Fourier atoms.
- **OPEN:** a universal averaged upper bound \(R_{\rm seq}(f)\le C I(f)\), equivalently full FEI.
