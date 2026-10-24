TASK: B16 ACCOUNT: account02 RUN: 2026-09-21T17:32:38.347735+00:00 — FEI signed transport: original-coordinate incidence characterizes the arbitrary-q-flip Radon frame obstruction up to universal constants.

MODEL: GPT-5.6 Sol
THINKING LEVEL: UNKNOWN / NOT_EXPOSED; requested=maximum actually supported
THINKING USAGE: NOT_EXPOSED; provider reasoning tokens/time unavailable
EXECUTION: WITHOUT_VERIFIED_BRAIN
FULL FEI STATUS: OPEN / NOT PROVED

# 0. What moved

The freshest compatible B18 source theorem had reduced a large part of the arbitrary-q-flip source problem to the following frame condition. For nonzero translations `u in F_2^n`, write

\[
I_u(f)=\Pr_x[f(x)\ne f(x+u)],\qquad
E_u(f)=I_u(f)(1-I_u(f)).
\]

B18 proved an arbitrary-pivot central Radon square `S_u` satisfying

\[
\mathcal S_u(f)\le \frac1{40}E_u(f)^2,
\]

and showed that a fully refunded compiler step would be paid if its nonnegative post-current pivot weights `lambda_u` obeyed a dimension-free frame bound

\[
\sum_{u\ne0}\lambda_u E_u(f)^2\lesssim I(f).
\]

That left an analytic-looking all-translation obligation. This run removes that source-side analytic ambiguity. Define the **original-coordinate incidence** of a nonnegative pivot frame by

\[
d_i(\lambda)=\sum_{u:u_i=1}\lambda_u,
\qquad
D(\lambda)=\max_i d_i(\lambda).
\]

I prove

\[
\boxed{
\sum_{u\ne0}\lambda_u E_u(f)^2
\le \frac4{27}D(\lambda)J(f),
}
\]
where `J(f)=sum_i min(I_i(f),1-I_i(f))` is the folded physical influence. Consequently

\[
\boxed{
\sum_{u\ne0}\lambda_u\mathcal S_u(f)
\le \frac1{270}D(\lambda)J(f).
}
\]

For a **fixed** frame `lambda`, this criterion is also necessary up to a universal constant: if

\[
A_*(\lambda)=\sup_{f:J(f)>0}
\frac{\sum_u\lambda_uE_u(f)^2}{J(f)},
\]
then for every `n>=2`,

\[
\boxed{
\frac1{16}D(\lambda)
\le A_*(\lambda)
\le \frac4{27}D(\lambda).
}
\]

Thus B18's arbitrary-pivot frame obstruction is, up to constants, **exactly an original-coordinate incidence problem**. No spectral fourth moment, all-translation capacity sum, or Hamming length estimate is needed once the compiler has legitimately reached nonnegative Radon weights.

This does **not** prove FEI. The remaining universal obligation is now sharply combinatorial and signed: derive the actual `lambda` from the account04 parity-current/double-resolvent compiler *after* its signed cancellations, and prove `D(lambda)=O(1)` (or an averaged version) without replacing the signed R32/R16/current ledger by absolute values.

# 1. Route and continuity

The three deliberately different FLEET_RULES moves were:

- **#2 ATTACK THE NEGATION FIRST:** ask whether an arbitrary all-q-flip frame can be paid without any coordinate-incidence control; the two-coordinate parity-switch family gives the exact obstruction.
- **#12 FIND WHAT IS CONSERVED:** fold by a cube character and keep the physical coordinate path metric. This reveals `D(lambda)` as the invariant that survives arbitrary q-flip directions.
- **#27 SWAP THE QUANTIFIERS:** instead of bounding one complicated compiler frame, characterize which fixed nonnegative pivot frames admit a uniform bound for *every* Boolean function.

Fresh owner control was read from `yspennstate/math-research-brain` main `38ff83fd75cfdf405faeb342648dc72ba2b08d4f`, OWNER CONTROL revision `2026-09-21.1`, including the natural-language OWNER MESSAGE. The live owner message keeps seven FEI workers/account and explicitly asks for creative FEI work rather than audits. Fresh `yspennstate/math-open-problems` master entering the scientific work was `5c9ba3bd107e843efa16109b57d7ea1907629ac4`.

The required current FEI state was read, including:

- `proofnet24/P03-fei/README.md`;
- `continuations/2026-09-21-readonce-certificate/TASKS_2026-09-21.md`;
- the corresponding `REPORT.md` and `APPROACHES.md`;
- account02/B18's fresh arbitrary-q-flip dependent-triple/Radon-frame theorem;
- account04/B16's fresh parity-current Walsh-frame theorem;
- the entering account02/B16 active-entropy Laplacian result.

The numerical correction in `TASKS_2026-09-21.md` is retained: the unrestricted FEI constant is already known to exceed `6.521845710923046575`; the older `6.4547837` unrestricted target is obsolete. Nothing below depends on trying to prove the refuted smaller target.

# 2. Setup and a folded translation metric

Let

\[
G=\mathbb F_2^n,\qquad f:G\to\{\pm1\}.
\]

For every translation `u in G`, define

\[
I_u(f)=\Pr_x[f(x)\ne f(x+u)]
\]
and its folded version

\[
j_u(f)=\min\{I_u(f),1-I_u(f)\}.
\]

For a physical coordinate `e_i`, abbreviate `j_i=j_{e_i}` and

\[
J(f)=\sum_i j_i.
\]

B18's source capacity is

\[
E_u=I_u(1-I_u)=j_u(1-j_u).
\tag{2.1}
\]

The key elementary fact is that `j_u` is controlled by the **original-coordinate support** of `u`, even though `u` is an arbitrary q-flip direction.

## Lemma 2.1 — folded path inequality

For every Boolean `f` and every `u`,

\[
\boxed{
 j_u(f)\le \sum_{i:u_i=1}j_i(f).
}
\tag{2.2}
\]

### Proof

Let

\[
A=\{i:I_{e_i}(f)>1/2\}
\]
and put `g=f chi_A`, where `chi_A` is the cube character with label `A`. Multiplication by a character either preserves or complements every translation disagreement indicator. Hence

\[
j_u(g)=j_u(f)
\]
for every `u`, while by construction

\[
I_{e_i}(g)=j_i(f)
\]
for every physical coordinate.

Write the support of `u` as `i_1,...,i_m` and let `s_r=e_{i_1}+...+e_{i_r}`. Pointwise,

\[
1_{\{g(x)\ne g(x+u)\}}
\le
\sum_{r=1}^m
1_{\{g(x+s_{r-1})\ne g(x+s_r)\}}.
\]

Averaging and using translation invariance gives

\[
I_u(g)\le\sum_{r=1}^m I_{e_{i_r}}(g)
=\sum_{i:u_i=1}j_i(f).
\]
Finally `j_u(f)=j_u(g)<=I_u(g)`. QED.

This is exactly where original-coordinate geometry re-enters. No arbitrary Hamming path in a changed representation is used.

# 3. The sharp scalar refund

For `0<=j<=1/2`,

\[
E^2=j^2(1-j)^2
=j\,[j(1-j)^2].
\]
The scalar function `j(1-j)^2` has derivative `(1-j)(1-3j)` and therefore maximum `4/27` at `j=1/3`. Hence

\[
\boxed{
E_u(f)^2\le \frac4{27}j_u(f).
}
\tag{3.1}
\]

The constant `4/27` is sharp for this scalar reduction. No claim is made that a Boolean translation must realize equality simultaneously with every other part of the frame.

Combining (3.1) and Lemma 2.1 gives the main theorem immediately.

# 4. PROVED: coordinate-incidence frame theorem

Let `lambda_u>=0` be arbitrary weights on `G\setminus{0}` and define

\[
\mathcal F_\lambda(f)=\sum_{u\ne0}\lambda_uE_u(f)^2,
\]

\[
d_i(\lambda)=\sum_{u:u_i=1}\lambda_u,
\qquad
D(\lambda)=\max_i d_i(\lambda).
\]

## Theorem B16-QFLIP-FRAME-INCIDENCE

For every Boolean `f`,

\[
\boxed{
\mathcal F_\lambda(f)
\le\frac4{27}\sum_i d_i(\lambda)j_i(f)
\le\frac4{27}D(\lambda)J(f).
}
\tag{4.1}
\]

### Proof

By (3.1) and (2.2),

\[
\begin{aligned}
\mathcal F_\lambda(f)
&\le \frac4{27}\sum_u\lambda_u j_u(f)\\
&\le \frac4{27}\sum_u\lambda_u\sum_{i:u_i=1}j_i(f)\\
&=\frac4{27}\sum_i j_i(f)\sum_{u:u_i=1}\lambda_u.
\end{aligned}
\]
This is the first inequality; the second follows from `d_i<=D`. QED.

### Immediate B18 source payment

For every arbitrary-q-flip quotient basis, B18 proves

\[
\mathcal S_u(f)\le E_u(f)^2/40.
\]
Therefore

\[
\boxed{
\sum_u\lambda_u\mathcal S_u(f)
\le\frac{D(\lambda)}{270}J(f).
}
\tag{4.2}
\]

Thus a compiler inequality of the legitimate form

\[
\operatorname{UNPAID}(f)
\le \Lambda\sum_u\lambda_u\mathcal S_u(f)
\]
with `D(lambda)<=D_0` would imply

\[
\operatorname{UNPAID}(f)
\le \frac{\Lambda D_0}{270}J(f).
\tag{4.3}
\]

This is a dimension-independent FEI payment at exactly the B18 frame stage.

Crucially, (4.1)--(4.3) are **not** permission to take absolute values in R32 or in the parity-current. The theorem starts only after the signed relation coefficients have been aggregated and the legitimate Hilbert/current step has produced nonnegative Radon-square weights. Negative entropy credits, dual-code multiplicity, R16 odd refunds, KL refunds and the exact terminal band remain untouched.

# 5. PROVED: the incidence condition is necessary up to constants for a fixed frame

The upper theorem is not merely a loose sufficient device. The two-variable Boolean parity switch detects coordinate concentration exactly.

Fix distinct coordinates `i,j` and let

\[
f_{ij}(x)=(-1)^{x_ix_j}
\]
in `{0,1}` coordinate notation. Its physical folded influences are

\[
j_i=j_j=1/2,
\qquad j_k=0\ (k\notin\{i,j\}),
\]
so

\[
J(f_{ij})=1.
\tag{5.1}
\]

For a translation `u`,

\[
f_{ij}(x)f_{ij}(x+u)
=(-1)^{x_i u_j+x_j u_i+u_i u_j}.
\tag{5.2}
\]
If `u_i=u_j=0`, this derivative is constant and `E_u=0`. Otherwise it is balanced, so

\[
I_u=1/2,\qquad E_u=1/4,\qquad E_u^2=1/16.
\tag{5.3}
\]
Therefore

\[
\boxed{
\mathcal F_\lambda(f_{ij})
=\frac1{16}
\sum_{u:\,u_i=1\ \mathrm{or}\ u_j=1}\lambda_u.
}
\tag{5.4}
\]

Define the optimal fixed-frame constant

\[
A_*(\lambda)=
\sup_{f:J(f)>0}\frac{\mathcal F_\lambda(f)}{J(f)}.
\]
Choose `i` with `d_i(lambda)=D(lambda)` and any `j!=i`. Since the pair-load in (5.4) is at least `d_i`, equations (5.1)--(5.4) imply

\[
A_*(\lambda)\ge D(\lambda)/16.
\]
Together with Theorem 4.1:

## Corollary B16-QFLIP-FRAME-EQUIVALENCE

For every fixed nonnegative pivot frame in dimension `n>=2`,

\[
\boxed{
\frac1{16}D(\lambda)
\le A_*(\lambda)
\le\frac4{27}D(\lambda).
}
\tag{5.5}
\]

So, up to a factor `64/27<2.371`, uniform arbitrary-q-flip source payment is equivalent to bounded original-coordinate incidence.

For an **f-dependent** compiler frame `lambda=lambda(f)`, the upper theorem remains valid pointwise. The lower theorem should not be over-read as a universal equivalence for such adaptive frames; it instead gives the exact diagnostic that any claimed adaptive compiler must pass on every parity-switch input.

# 6. Random-basis / averaged-frame corollary

Let `lambda^omega` be any random nonnegative pivot frame, possibly coming from a random q-flip basis. For a fixed Boolean input set

\[
\bar\lambda_u=\mathbb E_\omega\lambda_u^\omega.
\]
Then linearity gives

\[
\mathbb E_\omega\sum_u\lambda_u^\omega E_u(f)^2
=
\sum_u\bar\lambda_uE_u(f)^2.
\]
Therefore

\[
\boxed{
\mathbb E_\omega\sum_u\lambda_u^\omega E_u(f)^2
\le\frac4{27}
\left[
\max_i\mathbb E_\omega\sum_{u:u_i=1}\lambda_u^\omega
\right]J(f).
}
\tag{6.1}
\]

The same replacement in (4.2) yields an averaged central-Radon payment with factor `1/270`. Thus a proof does **not** need one basis whose every coordinate load is simultaneously small; an expected coordinate-incidence bound is enough. This matches the earlier orbit-averaging philosophy while keeping the actual original Boolean function fixed.

# 7. Why this is useful for the fresh parity-current theorem

Account04/B16 has now converted the odd relation ledger into an exact signed minimum-current object. Its current energy kills the singleton relation layer, retains the `2 mod 4` signs before squaring, and admits a double-resolvent/Walsh-frame representation. The fresh B18 theorem says every resulting q-flip pivot has a genuine physical dependent-triple/Radon source square.

Before this run, joining those results still appeared to require a new Fourier estimate for

\[
\sum_r\lambda_rE_{u_r}^2
\]
over an arbitrary family of q-flip pivots. Theorem 4.1 shows that no such all-translation Fourier estimate is needed. At the source side it is enough to establish

\[
\boxed{
\max_i\sum_{r:\,(u_r)_i=1}\lambda_r=O(1).
}
\tag{7.1}
\]

for the **actual post-current weights**. This is an original-coordinate combinatorial incidence statement. It is also the correct scale: Corollary 5.5 shows that fixed frames with unbounded coordinate incidence cannot satisfy a dimension-free universal B18 frame bound.

The next proof task is therefore concrete. One must express the account04 double-resolvent current-to-Radon map with its exact nonnegative weights `lambda_r`, retain the signed aggregation that precedes that map, and prove (7.1), likely by charging first coordinate separation / R16 moment refunds before the current is squared. Any route that instead replaces pre-current signed coefficients by `|b_R|` is still invalid.

# 8. Exact self-check

`check_qflip_frame_incidence.py` was executed natively in exact integer arithmetic.

It exhaustively checked the cross-multiplied inequality

\[
27\sum_u\lambda_u d_u^2(N-d_u)^2
\le
4D(\lambda)J_{\rm num}N^3
\]
for every Boolean truth table in dimensions `n=2,3,4` under one deterministic strictly positive integer pivot-weight family. Here `d_u` is the translation disagreement count, `I_u=d_u/N`, and `J=J_num/N`. It also checked every coordinate-pair parity-switch identity (5.4) in those dimensions.

Results:

- `65,808` Boolean truth tables checked;
- `10` parity-switch coordinate-pair witnesses checked;
- status `PASS`;
- largest observed `F_lambda/(D J)` under the tested weight family was about `0.0883152`, below the proved `4/27 ~= 0.148148` envelope.

The exhaustive computation is a self-check only. The theorem is proved symbolically in Sections 2--6.

Artifact identities:

- checker SHA-256 `e92e4b0176e99556585086a7b2565bc52be4d28e9028add62411bc778c608103`;
- checker Git blob `410f73ed35180e4d80c36d1029fc44839bbb2227`;
- output SHA-256 `97292c55e2f118329ba2c8b0b0ae3baf81a1d37811ce09982d9175446cad3b27`;
- output Git blob `dac20123776df56a6d7ca3da4607c6c4774980b5`.

# 9. Literature/status check

Fresh public searches on 2026-09-21 found:

- Vladimir N. Potapov, arXiv:2609.21563, submitted 2026-09-18 and updated 2026-09-21, proving FEI for Boolean plateaued functions with sharp class constant 4 and for partially bent functions with sharp class constant 2;
- Maria Jose Gonzalez, Paul MacManus, Maria Cristina Pereyra, arXiv:2606.00246, submitted 2026-05-29, proving additional structured/stopping-tree cases and explicitly presenting the unrestricted FEI statement as a conjecture;
- the older O'Donnell--Tan composition theorem remains a structured composition result, not an unrestricted proof.

These checks support treating full FEI as open in the inspected literature. They do **not** establish novelty or publication priority for the incidence theorem above, and no such claim is made.

# 10. Ledger

**PROVED in this run**

1. `B16-FOLDED-QFLIP-PATH`: `j_u <= sum_{i in supp u} j_i` in original cube coordinates.
2. `B16-QFLIP-FRAME-INCIDENCE`: `sum lambda_u E_u^2 <= (4/27) D(lambda) J`.
3. `B16-QFLIP-RADON-INCIDENCE`: using the inherited B18 source theorem, `sum lambda_u S_u <= D(lambda)J/270`.
4. `B16-QFLIP-FRAME-EQUIVALENCE`: for a fixed nonnegative frame, its best universal `E_u^2` frame constant lies in `[D/16,4D/27]`.
5. Expected coordinate incidence is sufficient for random-basis frames; no simultaneous sparse basis is required.

**PRESERVED / NOT SPENT**

- R32 negative `2 mod 4` entropy credits;
- relation/code multiplicity;
- account04 signed parity-current cancellations;
- R16 odd-moment refunds;
- KL/restriction refunds;
- exact terminal-band payment.

**OPEN universal obligation**

Identify the actual nonnegative q-flip Radon weights produced *after* the signed parity-current/double-resolvent aggregation and prove their original-coordinate incidence `D(lambda)=O(1)` (or the averaged counterpart). This is now the exact source-frame bottleneck. Full FEI remains OPEN / NOT PROVED.
