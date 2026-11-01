# B12 FEI creative attempt: actual restriction refunds force Palm-code savings

**Status:** **PARTIAL. Full uniform-cube Friedgut–Kalai Fourier entropy–influence remains OPEN / NOT PROVED.**

**Route:** APPROACH 1, spectral-sample compression / sequential prediction. This run does not audit FEI and does not rerun the settled read-once certificate. It uses two fresh compatible peer results to attack one explicit missing implication in the joint state: turn **actual physical restriction refunds** into a rigorously non-overcounted saving in the **Palm insertion code**.

**Execution label:** `WITHOUT_VERIFIED_BRAIN`. The authorized GitHub control/handoff files were consumed, but no authenticated mathematical-brain retrieval engine or receiver-context result was used.

**Scientific master at the substantive refresh:** `01e6df6be1cd3ffd582b9c8153253ea9bfd40ce1` before this run's own commits. The required `TASKS_2026-09-21.md`, `REPORT.md`, and `APPROACHES.md` were read first from the then-current master lineage. The corrected unrestricted lower bound `> 6.521845710923...` is retained; nothing here makes a sharp-constant claim.

## 1. Exact peer interfaces consumed

The sequential-code input is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B12/20260921T191537Z-palm-insertion-information/REPORT.md`

blob `e3be1fc4acbfa40d56f8490da4a93997f87ed30a`.

For a Boolean function with spectral sample `S`, write

\[
p_i:=\Pr(i\in S)=\operatorname{Inf}_i(f),\qquad I=\sum_i p_i,
\qquad q_{ij}:=\Pr(i,j\in S).
\]

That report constructs the uniform-prefix insertion edge law. If `L` is the inserted coordinate and `P` the predecessor prefix, its exact KL saving is

\[
D_{\rm seq}=I\,I_2(L;P).
\tag{1.1}
\]

It also proves the **self-witness** data-processing bound

\[
\boxed{
D_{\rm seq}\ge \sum_i p_i\log_2\frac1{1-\beta_i},
\qquad
\beta_i:=\Pr(i\in P)=\frac1{2I}\sum_{j\ne i}q_{ij}.
}
\tag{1.2}
\]

The associated exact code identity gives

\[
H(S)\le H(K)+I H(\pi)-\mathbb E\log_2(K!)-D_{\rm seq},
\qquad
K=|S|,\quad \pi_i=p_i/I.
\tag{1.3}
\]

The actual-refund input is

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B14/20260921T184113Z-posterior-crossing-budget/REPORT.md`

blob `c974b249c6cc513019bd0e58e7711ad808c80844`.

On a centered physical-restriction-critical core, let

\[
R=\frac{H(S)}{I},\qquad
\mathfrak j(p)=1-h_2\!\left(\frac12+\sqrt{p(1-p)}\right),
\qquad
\Psi(p)=h_2(p)+\mathfrak j(p),
\]

and

\[
D:=\sum_i\Psi(p_i)-RI
   =\operatorname{TC}(S)+\sum_i\mathfrak j(p_i).
\tag{1.4}
\]

For a pair `i != j`, let `c_ij` be the probability, over a uniformly random restriction of all other physical variables, that the residual `(i,j)` face is non-affine. The B14 pair-refund theorem is

\[
\boxed{
R c_{ij}\ge \Psi(p_i)+\Psi(p_j)-D.
}
\tag{1.5}
\]

The right side may be negative; below it is replaced by its positive part.

The missing bridge was that (1.5) is a physical two-face statement whereas (1.2) needs spectral co-inclusion `q_ij`. The next lemma supplies that bridge exactly.

## 2. New exact two-face identity

### Lemma 2.1 — non-affine faces inject one quarter of their mass into spectral co-inclusion

For distinct `i,j`, let `a_ij` be the probability that the random residual `(i,j)` face is **affine parity in both coordinates** (the checkerboard face, up to output sign). Then

\[
\boxed{
q_{ij}=a_{ij}+\frac14 c_{ij}.
}
\tag{2.1}
\]

In particular,

\[
\boxed{q_{ij}\ge \frac14 c_{ij}.}
\tag{2.2}
\]

### Proof

Fix all variables except `i,j`. Encode the resulting two-bit Boolean truth table over `\mathbb F_2` as

\[
F(x_i,x_j)=\alpha+b x_i+c x_j+d x_i x_j.
\]

There are two cases.

If `d=0`, the face is affine. The two coordinates are simultaneously pivotal at a vertex iff `b=c=1`. Thus an affine checkerboard face contributes conditional joint-pivotality probability `1`, while every other affine face contributes `0`.

If `d=1`, the face is non-affine. The discrete derivatives are

\[
\partial_iF=b+x_j,\qquad \partial_jF=c+x_i.
\]

They are simultaneously `1` at exactly one of the four vertices. Hence every non-affine face contributes conditional joint-pivotality probability exactly `1/4`.

Averaging over the outside restriction gives

\[
\Pr(i,j\in\operatorname{Sens}_f(X))=a_{ij}+c_{ij}/4.
\]

The standard Parseval derivative identity, also used in the Palm-insertion handoff, gives

\[
\Pr(i,j\in\operatorname{Sens}_f(X))
=\sum_{A\ni i,j}\widehat f(A)^2
=q_{ij}.
\]

This proves (2.1) and (2.2). QED.

This is stronger than merely comparing two expectations: it identifies the exact missing piece. The non-affine refund geometry contributes a forced `1/4` to the two-coordinate spectral Palm statistic, while affine parity faces contribute an additional nonnegative term.

## 3. New theorem: actual crossing refunds force a non-overcounted Palm KL saving

Define

\[
[x]_+:=\max\{x,0\}
\]

and, for each relevant coordinate `i`,

\[
\boxed{
b_i:=\frac{1}{8RI}
\sum_{j\ne i}
[\Psi(p_i)+\Psi(p_j)-D]_+.
}
\tag{3.1}
\]

### Theorem 3.1 — crossing-to-Palm bridge

On every centered restriction-critical core to which (1.5) applies,

\[
\boxed{
0\le b_i\le \beta_i<1
}
\tag{3.2}
\]

and therefore

\[
\boxed{
D_{\rm seq}
\ge
\sum_i p_i\log_2\frac1{1-b_i}.
}
\tag{3.3}
\]

Consequently,

\[
\boxed{
D_{\rm seq}
\ge
\frac{1}{8RI\ln2}
\sum_{i<j}(p_i+p_j)
[\Psi(p_i)+\Psi(p_j)-D]_+.
}
\tag{3.4}
\]

### Proof

From the B14 pair-refund theorem (1.5),

\[
c_{ij}\ge \frac{[\Psi(p_i)+\Psi(p_j)-D]_+}{R}.
\]

Lemma 2.1 then yields

\[
q_{ij}\ge
\frac{[\Psi(p_i)+\Psi(p_j)-D]_+}{4R}.
\tag{3.5}
\]

Insert (3.5) into the exact Palm predecessor occupancy from (1.2):

\[
\beta_i
=\frac1{2I}\sum_{j\ne i}q_{ij}
\ge b_i.
\tag{3.6}
\]

Moreover, whenever `p_i>0`, the event `L=i` has probability `p_i/I` and forces `i notin P`, so

\[
\beta_i\le 1-p_i/I<1.
\]

The function `x -> -log_2(1-x)` is increasing on `[0,1)`. Applying the inherited self-witness bound (1.2) and (3.6) gives (3.3).

Finally use

\[
-\log_2(1-x)\ge \frac{x}{\ln2}
\]

and substitute (3.1). The ordered-pair sum groups as

\[
\sum_i p_i\sum_{j\ne i}A_{ij}
=\sum_{i<j}(p_i+p_j)A_{ij}
\]

for the symmetric quantity
`A_ij=[Psi(p_i)+Psi(p_j)-D]_+`, proving (3.4). QED.

## 4. Why this avoids the pairwise-overcounting failure

The fresh fleet03/B12 handoff explicitly refuted the tempting bound obtained by **adding a separate binary KL term for every pair**: selector-of-parities functions make many coordinates repeat essentially the same latent cluster bit, so the apparent pairwise information can exceed the true insertion mutual information.

Theorem 3.1 does **not** make that false summation. All pairwise physical refunds first pass through the exact probability

\[
\beta_i=\Pr(i\in P),
\]

and only then incur one self-witness log-loss for label `i`. Thus repeated pair evidence can raise the occupancy of one prefix coordinate only up to probability one; it cannot be charged as arbitrarily many independent KL bits. The linearized formula (3.4) is safe because its summed lower bound is inherited from the genuine occupancy `b_i<=beta_i<1`, not from adding the false pairwise KL terms.

This is the concrete resolution of the immediate fleet03 obstruction: **physical pair information can be aggregated, but it must be aggregated as occupancy/refund mass before taking logarithmic information cost.**

## 5. A new explicit entropy upper bound on a critical core

Combining (1.3) with Theorem 3.1 gives

\[
\boxed{
H(S)
\le
H(K)+I H(\pi)-\mathbb E\log_2(K!)
-
\sum_i p_i\log_2\frac1{1-b_i}.
}
\tag{5.1}
\]

A weaker completely scalar form is

\[
\boxed{
H(S)
\le
H(K)+I H(\pi)-\mathbb E\log_2(K!)
-
\frac{1}{8RI\ln2}
\sum_{i<j}(p_i+p_j)
[\Psi(p_i)+\Psi(p_j)-D]_+.
}
\tag{5.2}
\]

where `R=H/I` and `D=sum_i Psi(p_i)-RI` on the critical core.

Equation (5.2) is a genuine coupling of the two previously separate proof engines:

- `D` is the **actual restriction/refund bank** (total correlation plus recombination credit);
- the positive pair deficits force non-affine physical faces;
- non-affine faces force spectral co-inclusion;
- co-inclusion forces predecessor occupancy in the Palm insertion process;
- predecessor occupancy forces a **real sequential KL saving**.

No mock predictor, no scalar-only surrogate, and no independent addition of redundant pair information is used.

## 6. What remains — a sharply reduced dichotomy

This still does **not** prove FEI. The unresolved scalar/structural dichotomy is now explicit.

If many pairs satisfy

\[
\Psi(p_i)+\Psi(p_j)>D,
\tag{6.1}
\]

then (5.1)-(5.2) force a quantitative Palm-code rebate. The harder regime is when

\[
D\ge \Psi(p_i)+\Psi(p_j)
\tag{6.2}
\]

for most pairs. In that regime the pair bridge is silent, but `D` itself is already a large global dependence/recombination bank because

\[
RI=\sum_i\Psi(p_i)-D.
\tag{6.3}
\]

The next missing implication is therefore no longer “sum pairwise information somehow.” It is:

> **BANK-OR-CODE TARGET.** Show, with a dimension-free constant, that either the global bank `D` itself removes enough of `sum Psi(p_i)` to bound `R`, or the positive pair deficits in (6.1) are numerous/heavy enough that the Palm rebate in (5.1) removes the diffuse influence-profile entropy `I H(pi)`.

The obstruction is also clear: a proof cannot count the same latent cluster many times. Any continuation should keep the occupancy saturation `beta_i` or an actual block-valued observation of the prefix, rather than revert to a raw sum of pairwise KL terms.

A promising next step is to optimize the **block self-witness** `1_{P cap B != empty}` over disjoint blocks selected from the positive-deficit graph. Disjointness would preserve nonreuse, while the current theorem is the singleton endpoint of that construction.

## 7. Finite self-check

`verify_face_identity.py` performs an exact integer-Walsh / rational exhaustive check modulo global output sign through `n=4`. It verifies for every Boolean function and every coordinate pair that

\[
q_{ij}=\Pr(i,j\in\operatorname{Sens}(X))
      =a_{ij}+c_{ij}/4.
\]

Counts checked:

- `n=2`: 8 functions modulo sign, 8 function-pairs;
- `n=3`: 128 functions modulo sign, 384 function-pairs;
- `n=4`: 32,768 functions modulo sign, 196,608 function-pairs.

All passed exactly. This is only a sanity check; Lemma 2.1 and Theorem 3.1 are proved analytically above.

## 8. Classification

- **PROVED:** exact two-face identity `q_ij = a_ij + c_ij/4`.
- **PROVED:** actual B14 crossing refunds imply the Palm predecessor lower bound `beta_i >= b_i`.
- **PROVED:** the non-overcounted sequential KL saving (3.3) and scalar consequence (3.4).
- **PROVED:** combined entropy upper bounds (5.1)-(5.2) on the centered restriction-critical core interface.
- **NOT CLAIMED:** that (5.1) is already bounded by `C I`; this is the remaining bank-or-code problem.
- **OPEN:** full FEI.

No novelty or publication-priority claim is made for these private continuation lemmas.
