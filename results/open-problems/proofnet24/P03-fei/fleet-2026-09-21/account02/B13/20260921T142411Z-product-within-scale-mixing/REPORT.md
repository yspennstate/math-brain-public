TASK: B13 ACCOUNT: account02 RUN: 2026-09-21T14:24:11.725662Z — product-block decomposition of the fixed-scale residual and a strict Boolean non-tensorization witness

**STATUS: PARTIAL. Full uniform-cube FEI remains OPEN.**  
**EXECUTION: WITHOUT_VERIFIED_BRAIN.** No retrieved brain context was consumed.  
**ROLE:** FEI approach 2/13 — Boolean block-influence/correlation profiles and two-sided Booleanity constraints.  
**MODEL:** GPT-5.6 Sol (self-report). Maximum reasoning was requested; configured selector and provider thinking counters are not exposed.

## 0. Fresh control/dependencies and research moves

The governing control was resolved fresh from `yspennstate/math-research-brain` main. OWNER CONTROL revision is `2026-09-21.1`; the direct owner order `FEI-SEVEN-TASKS-2026-09-21` supersedes the stale provisional B13 benchmark row in `roles.json`. No later B13/account02 stop was present at entry. The FEI files were read in the required order: `TASKS_2026-09-21.md`, certified read-once `REPORT.md`, `APPROACHES.md`, then the fresh P03 README and `FLEET_RULES.md`.

Immediate scientific dependencies used here are the prior B13 prefix/Beta run, which isolated
\[
H(f)\le (5+\log_2 e)I(f)+C_{\rm within}(f),
\]
and the account01/B13 random-order decomposition. I also read B12's current death-chain selector formulation. Its selector term is the next-coordinate information in a random reveal; the result below identifies and pays the *coarse block-label part* of the fixed-scale version under exact disjoint products. This does not overlap B14's existential selector or B16's signed transport route.

The three fresh `FLEET_RULES` moves were:

- **#12 find what is conserved:** the tilted-prefix partition of unity below is exactly one and is what prevents a factor-count loss;
- **#18 say it in another language:** rewrite the Beta/noise residual as a communication channel `next coordinate -> (block label, within-block coordinate)`;
- **#20 find why the algorithm fails:** naive tensorization of `C_within` is false even for `Maj_3 x Maj_3`; the corrected block-label charge is globally bounded once by the entropy of the vector of factor spectral sizes.

A fresh literature query found the recent 2026 plateaued-function paper and the 2026 stopping-binary-tree paper, but no full FEI proof and no located statement of the product identity below. I make no novelty or priority claim without a paper-level comparison.

## 1. Setup: the fixed-scale residual

For a Boolean function with spectral law
\[
p_B=\widehat f(B)^2,
\]
write, for a prefix `A`, `a=|A|`,
\[
E_A(s)=\sum_{B\supseteq A}p_B s^{|B|-a},\qquad
R_A(s)=E_A'(s).
\]
At fixed `s`, conditioned on continuation from `A`, the joint branch law is
\[
\Pr(N=i,T=B\mid A,s)
=\frac{p_B s^{|B|-a-1}}{R_A(s)}
\quad(i\in B\setminus A).
\]
Let
\[
I_{A,s}=I(N;T\mid A,s).
\]
The residual isolated in the predecessor is
\[
C_{\rm within}(f)
=\sum_A\int_0^1 (1-s)^{|A|}R_A(s)I_{A,s}\,ds.\tag{1}
\]

A basic conservation law, valid for every subset law and every `s in [0,1]`, is
\[
\boxed{\sum_A(1-s)^{|A|}E_A(s)=1.}\tag{2}
\]
Indeed a fixed terminal `B` contributes
\[
p_B\sum_{A\subseteq B}(1-s)^{|A|}s^{|B|-|A|}=p_B.
\]
This identity will remove all other factors exactly when a within-factor term is summed.

## 2. Main theorem: exact disjoint-product decomposition

Let `f_j` be Boolean functions on pairwise disjoint coordinate blocks and
\[
F=\prod_{j=1}^m f_j.
\]
Its spectral sample is the disjoint union of independent samples `S_j` from the factor spectral laws. Put
\[
K_j=|S_j|,\qquad \mathbf K=(K_1,\ldots,K_m).
\]

### Theorem

There is a nonnegative block-mixing term `C_mix` such that
\[
\boxed{
C_{\rm within}(F)
=\sum_{j=1}^m C_{\rm within}(f_j)+C_{\rm mix}(f_1,\ldots,f_m),
}\tag{3}
\]
and
\[
\boxed{0\le C_{\rm mix}\le H(\mathbf K).}\tag{4}
\]
Because the factor spectral samples are independent,
\[
H(\mathbf K)=\sum_j H(K_j).\tag{5}
\]
For Boolean factors the size-entropy payment from the predecessor gives
\[
H(K_j)\le 3 I(f_j),
\]
therefore
\[
\boxed{C_{\rm mix}\le 3I(F).}\tag{6}
\]
If every factor is balanced, then `p_empty=0`, so the sharper positive-size argument gives `H(K_j)<=I(f_j)` and hence
\[
\boxed{C_{\rm mix}\le I(F)\qquad\text{for balanced factors}.}\tag{7}
\]
Crucially, (6) is paid **once for the whole product**, not once per binary composition depth and not as `I log m`.

### Proof of the exact identity

Write a prefix as `A=(A_1,...,A_m)` and abbreviate
\[
E_j=E^{(j)}_{A_j}(s),\qquad R_j=(E^{(j)}_{A_j})'(s).
\]
Independence gives
\[
E_A(s)=\prod_jE_j,
\qquad
R_A(s)=\sum_\ell R_\ell\prod_{j\ne\ell}E_j.\tag{8}
\]
Let `L` be the block containing the next coordinate `N`. At fixed `(A,s)`,
\[
\Pr(L=\ell)=
\lambda_\ell:=
\frac{R_\ell\prod_{j\ne\ell}E_j}{R_A}.\tag{9}
\]
Conditioned on `L=ell`, factor `ell` has its derivative/size-biased branch law, while every other factor has the ordinary `s`-tilted law. Hence `N_ell` is conditionally independent of all terminal factor sets except `T_ell`, and the mutual-information chain rule gives
\[
I_{A,s}
=I(L;T_1,\ldots,T_m\mid A,s)
+\sum_\ell\lambda_\ell I^{(\ell)}_{A_\ell,s}.\tag{10}
\]
Moreover the conditional law of `L` given the full terminal sets depends on them only through the remaining block sizes:
\[
\Pr(L=\ell\mid T_1,\ldots,T_m,A,s)
=\frac{|T_\ell|-|A_\ell|}{\sum_j(|T_j|-|A_j|)}.
\]
Thus
\[
I(L;T_1,\ldots,T_m\mid A,s)
=I(L;\mathbf K\mid A,s).\tag{11}
\]
Multiply (10) by `(1-s)^|A| R_A` and sum over all prefixes. For a fixed `ell`, its internal term becomes
\[
\sum_{A_\ell}\int(1-s)^{|A_\ell|}R_\ell I^{(\ell)}_{A_\ell,s}
\prod_{j\ne\ell}
\left[\sum_{A_j}(1-s)^{|A_j|}E^{(j)}_{A_j}(s)\right]ds.
\]
Every bracket is one by (2). The result is exactly `C_within(f_ell)`. The leftover term is
\[
C_{\rm mix}:=
\sum_A\int_0^1(1-s)^{|A|}R_A(s)
I(L;\mathbf K\mid A,s)\,ds\ge0,
\]
which proves (3).

### Proof of the global payment (4)

Use the predecessor's Beta augmentation: before each continuation step, the fixed scale `tau=s` is sampled from the Beta law determined by the total number of unrevealed coordinates. Given the terminal size vector `K` and the current prefix `A`, `tau` depends only on the total remaining count, while the next block label `L` is chosen in proportion to the per-block remaining counts. Therefore
\[
L\perp\!\!\!\perp \tau\mid(\mathbf K,A,\text{continue}).
\]
Consequently
\[
I(L;\mathbf K\mid \tau,A,\text{continue})
\le I(L;\mathbf K\mid A,\text{continue}).\tag{12}
\]
(The identity behind this is `I(L;K)=I(L;tau)+I(L;K|tau)` because `I(L;tau|K)=0`.)

Now expose a uniformly random ordering of the terminal spectral set. At each continuation step record first the block label and then the exact coordinate. The vector `K` is determined by the resulting sequence of block labels together with termination. Chain rule for `I(K; transcript)=H(K)` shows that the sum of all block-label information increments is at most `H(K)`. Grouping ordered histories with the same unordered prefix does not change those increments: conditional on the unordered prefix and terminal set, the past ordering is uniform and carries no additional information about `K`. Combining this chain-rule bound with (12) proves (4).

Finally, for one Boolean factor let `V=P(K>0)=1-p_empty`. Then
\[
H(K)=h_2(V)+V H(K\mid K>0).
\]
Among positive-integer laws of mean `m=I/V`, the geometric law maximizes entropy, so by a one-line KL comparison
\[
H(K\mid K>0)\le m h_2(1/m)\le m.
\]
Thus the second term is at most `I`. Also
\[
h_2(V)\le V\bigl(\log_2(1/V)+\log_2e\bigr)\le2I
\]
by the Boolean edge-isoperimetric payment already used for continuation entropy. Hence `H(K)<=3I`. If `V=1` the binary-entropy term vanishes and `H(K)<=I`, proving (6)-(7).

## 3. Rigorous Boolean obstruction: `C_within` does not tensorize

A tempting lemma would be
\[
C_{\rm within}(fg)=C_{\rm within}(f)+C_{\rm within}(g)
\]
for disjoint Boolean products. Equation (3) shows this is false whenever the block label carries terminal-size information.

Take `f=g=Maj_3`. Its spectral law puts mass `1/4` on each of the three singleton sets and on the full three-set, so `K in {1,3}` with probabilities `3/4,1/4`. For `F=Maj_3 x Maj_3`, at the root and every fixed `s in (0,1)`, symmetry gives marginal `P(L=1)=1/2`. But on the positive-probability event `(K_1,K_2)=(3,1)`,
\[
P(L=1\mid K_1=3,K_2=1)=3/4.
\]
Therefore
\[
I(L;\mathbf K\mid A=\varnothing,s)>0
\]
on an interval of positive `s`-measure, hence
\[
\boxed{C_{\rm mix}(Maj_3,Maj_3)>0.}\tag{13}
\]
This is a genuine Boolean counterexample to exact tensorization, not a relaxed-law obstruction.

The numerical self-check gives
\[
C_{\rm within}(Maj_3)=1.1887218755408673,
\]
\[
C_{\rm within}(Maj_3\times Maj_3)=3.0652083501106455,
\]
and therefore
\[
C_{\rm mix}=0.687764599028911.
\]
The rigorous theorem only needs positivity and the entropy bound; these floating values are diagnostic, not proof of (13).

## 4. Verification

`verify_product_mixing.py` was executed on the exact archived code. It performed 2,304 all-prefix pointwise fixed-scale checks on `Maj_3` and a three-bit one-point-defect factor over a nine-point scale grid. Results:

- maximum fixed-scale factorization discrepancy: `8.215650382226158e-15`;
- maximum discrepancy between `I(L; terminal sets)` and `I(L; size vector)`: `1.5543122344752192e-15`;
- maximum partition-of-unity discrepancy: `0.0`;
- `Maj_3 x Maj_3`: numerical `C_mix=0.687764599028911 <= H(K_1,K_2)=1.6225562489182657`;
- defect3 x defect3: numerical `C_mix=1.0065798501956704 <= H(K_1,K_2)=3.2451124978365318`.

The checker is a self-check of the algebra and quadrature diagnostics. The theorem above is the proof.

## 5. What this changes, and the next target

The new information is not another constant for a structured class. It identifies a previously hidden source of residual entropy and proves that, under arbitrary many disjoint product blocks, this source **cannot accumulate as a depth or factor-count loss**. The full fixed-scale residual splits into factor-internal residuals plus one coarse block-identification term, and the latter costs at most the entropy of the vector of spectral sizes, hence at most `3I` universally (`I` for balanced factors).

So disjoint products cannot manufacture an unbounded `C_within/I` ratio merely by interleaving many otherwise controlled blocks. Any full-FEI obstruction in this framework has to live in the factor-internal fixed-scale selector information or in non-product coupling between blocks.

The next nonduplicative target is the **weakly coupled block extension**: for a general Boolean spectral law partitioned into blocks, compare its `s`-tilted branch law with the product of its block marginals. The exact-product proof says the error term should be a tilted block total-correlation / signed-correlation defect. A viable bridge would bound the integral of that defect by Boolean block influences or the simultaneous `f^2=1` phase constraints. The `Maj_3 x Maj_3` witness is now the mandatory test: any proposed theorem that simply declares the within-scale residual additive is false.

Full FEI is not proved here.
