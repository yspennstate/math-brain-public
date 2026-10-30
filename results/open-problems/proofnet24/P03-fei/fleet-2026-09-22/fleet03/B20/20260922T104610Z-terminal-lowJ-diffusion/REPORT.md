# fleet03/B20 — low-J terminal-core diffusion and near-character branch reduction

**Classification:** `ESSENTIAL_STEP_APPLIED / TERMINAL_EXCEPTIONAL_BRANCH_NARROWED / FULL_FEI_OPEN`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, state `FEI-20260922T1000Z-v1`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Model self-report:** GPT-5.6 Sol. Maximum actually supported reasoning requested; configured effort and provider usage were not exposed.

## 1. Scope and source pins

The live owner order superseded this slot's older MOC4 assignment. The present task is to remove a small-influence or degeneracy branch of the candidate-independent physical stopping theorem without invoking dimension-dependent continuity of Fourier entropy.

The proof below uses the exact minimum-dimensional all-block critical core and co-singleton phase-support tax from

- `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`.

For the mechanism calibration in Section 5 it also applies the robust-row trigger-surplus theorem from

- `yspennstate/math-open-problems@fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`, `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`.

The current correction inbox was empty at the pre-publication sweep. The named partner for this new all-team assignment is `fleet04/B20`; no completed fleet04/B20 FEI artifact under the new all-team order was visible at the compatibility sweep, so no partner theorem is fabricated or attributed here. Its pre-order POS3 outputs are scientifically incompatible with this FEI task and are not consumed.

## 2. Imported exact critical-core endpoint

Let `g` be the centered, essential, minimum-dimensional ratio core selected in the all-block terminal reduction. Write

\[
q_i=\operatorname{Inf}_i(g)\le \frac12,
\qquad
\mathcal J=\sum_i q_i>0,
\]
\[
\mathfrak j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right),
\qquad
\mathcal P=\sum_i\mathfrak j(q_i),
\qquad
\mathcal F=H-\mathcal P.
\]

The source proves the scalar phase cap

\[
\boxed{\mathcal P\le c_0\mathcal J,\qquad c_0:=\frac{2}{\ln2},}
\tag{2.1}
\]

and, by revealing all coordinates except `j`, the exact co-singleton phase-support tax

\[
\boxed{
\mathcal P\ge h_2(q_j)+q_j\mathfrak j'(q_j)
\quad\text{for every essential coordinate }j.
}
\tag{2.2}
\]

No Fourier-entropy continuity statement is used below.

## 3. New theorem: low-total-influence terminal cores are necessarily diffuse

### Theorem 3.1 — quantitative finite-heavy exclusion

Assume `0<\mathcal J<1`. Every coordinate of the minimum-dimensional all-block critical core satisfies

\[
\boxed{
\frac{q_j}{\mathcal J}
\le
\frac{c_0}{\log_2(1/\mathcal J)}
\qquad(c_0=2/\ln2).
}
\tag{3.1}
\]

Equivalently, for every `delta>0`,

\[
\boxed{
\mathcal J<2^{-c_0/\delta}
\quad\Longrightarrow\quad
q_j<\delta\mathcal J\ \text{for every }j.
}
\tag{3.2}
\]

Consequently, along any sequence of such critical cores with `\mathcal J_m\to0`,

\[
\boxed{
\max_j\frac{q_{m,j}}{\mathcal J_m}\longrightarrow0.
}
\tag{3.3}
\]

Thus a low-`J` obstruction cannot retain a coordinate carrying a fixed positive fraction of the total folded influence.

### Proof

The function `\mathfrak j` is increasing on `[0,1/2]`, hence `\mathfrak j'(q)\ge0` in the interior (with the endpoint derivative understood by its one-sided limit). Combining (2.1) and (2.2) gives

\[
h_2(q_j)\le c_0\mathcal J.
\tag{3.4}
\]

For `0<q\le1/2`,

\[
h_2(q)
=q\log_2\frac1q+(1-q)\log_2\frac1{1-q}
\ge q\log_2\frac1q.
\tag{3.5}
\]

Also `q_j\le\mathcal J`, so

\[
q_j\log_2\frac1{\mathcal J}
\le q_j\log_2\frac1{q_j}
\le h_2(q_j)
\le c_0\mathcal J.
\]

Division by the positive denominator proves (3.1), and (3.2)--(3.3) follow immediately. QED.

### Corollary 3.2 — dimension must diverge

If `n` is the number of essential coordinates, then

\[
\mathcal J\le n\max_jq_j,
\]
so Theorem 3.1 implies

\[
\boxed{
n\ge\frac1{c_0}\log_2\frac1{\mathcal J}.}
\tag{3.6}
\]

Hence there is no bounded-essential-dimension low-`J` critical sequence. This is exactly the point at which a naive fixed-dimensional entropy-continuity argument would be invalid: any genuinely unresolved low-`J` sequence is forced into growing dimension.

## 4. Exact character/constant endpoint: the remaining branch is near-character

The centering operation in the source is multiplication by a character chosen so that the ordinary influence of the centered representative is exactly

\[
I(g)=\sum_iq_i=\mathcal J.
\]

Uniform-cube Poincare gives

\[
\operatorname{Var}(g)\le\mathcal J.
\tag{4.1}
\]

Since `g` is Boolean, choose the closer constant sign `s\in\{\pm1\}` and write

\[
\varepsilon:=\Pr[g\ne s]\le\frac12.
\]

Then exactly

\[
\operatorname{Var}(g)=4\varepsilon(1-\varepsilon).
\]

For `\mathcal J<1`, (4.1) therefore yields

\[
\boxed{
\varepsilon
\le
\frac{1-\sqrt{1-\mathcal J}}2.
}
\tag{4.2}
\]

In particular `\varepsilon\to0` as `\mathcal J\to0`.

Combining Sections 3 and 4 gives a source-valid classification of the low-total-influence exceptional branch:

> Any unresolved minimum-dimensional terminal countersequence with `\mathcal J\to0` must simultaneously be (i) Hamming-near a character after exact character centering, (ii) supported on a number of essential coordinates diverging at least logarithmically in `1/\mathcal J`, and (iii) diffuse in normalized influence, with every fixed coordinate share tending to zero.

This eliminates the bounded-dimensional and finite-heavy degeneracy branches without ever asserting continuity of Fourier entropy across growing dimension.

## 5. Application of the robust-row theorem: why that theorem alone does not kill the residual branch

The current B20 input bundle includes fleet04/B12's exact robust-row theorem. For an exact subcube derivative row (`eta=0`) with trigger set `F_i`, it states

\[
\boxed{
\sum_{k\in F_i}\sigma_k(K)
\ge [K+\mathfrak j'(q_i)]q_i,
\qquad
\sigma_k(K)=h_2(q_k)-Kq_k.
}
\tag{5.1}
\]

A canonical near-character calibration shows why (5.1) cannot by itself remove the remaining diffuse low-`J` regime.

Let `f_d` be `+1` on the `d`-cube except at one point, where it is `-1`. Then, for every active coordinate,

\[
q=2^{1-d},
\qquad
\mathcal J=d\,2^{1-d},
\qquad
\frac q{\mathcal J}=\frac1d\to0.
\tag{5.2}
\]

Each derivative support is exactly one point of a `(d-1)`-cube, hence an exact subcube row with `|F_i|=d-1`. Therefore the two sides of (5.1) are

\[
(d-1)[h_2(q)-Kq]
\quad\text{and}\quad
[K+\mathfrak j'(q)]q.
\tag{5.3}
\]

As `d\to\infty`,

\[
\frac{h_2(q)}q=(d-1)+\frac1{\ln2}+o(1),
\qquad
\mathfrak j'(q)\to\frac2{\ln2},
\]
so the ratio of the left side of (5.3) to the right side grows quadratically in `d`. The robust trigger-surplus inequality becomes increasingly slack rather than contradictory.

This is a mechanism-level counterfamily, **not an FEI counterexample**. It shows that a proof of the residual low-`J` branch must exploit a nonlocal/nonreused structure beyond the local robust-row surplus demand.

The same family has exact Fourier spectrum

\[
\widehat f_d(\varnothing)=1-2^{1-d},
\qquad
|\widehat f_d(S)|=2^{1-d}\quad(S\ne\varnothing).
\]

Thus

\[
H(f_d)=
-(1-2^{1-d})^2\log_2(1-2^{1-d})^2
+(2^d-1)2^{2-2d}(2d-2),
\tag{5.4}
\]

and

\[
\boxed{
\frac{H(f_d)}{\mathcal J(f_d)}\to4,
\qquad
\frac{\mathcal F(f_d)}{\mathcal J(f_d)}
\to4-\frac2{\ln2}<2.
}
\tag{5.5}
\]

So this explicit diffuse near-character family is target-safe for the `K>2` terminal ratio reduction, while demonstrating that the residual structural regime is genuinely nonempty and that the logarithmic diffusion scale in (3.1) is of the correct order (`q/J=1/d` while `\log_2(1/J)=d-O(\log d)`).

## 6. Exact change in the proof state

**Before this run:** the all-block terminal reduction left a small-influence/nonrobust exceptional sector, and the robust-row theorem explicitly suggested treating it by a different mechanism.

**After this run:** the `J\to0` portion of that sector is split rigorously into:

1. **eliminated:** bounded-dimensional low-`J` sequences;
2. **eliminated:** low-`J` sequences with any coordinate carrying a fixed positive fraction of total folded influence;
3. **remaining:** growing-dimensional, normalized-influence-diffuse, near-character sequences.

The one-point-defect family proves that branch (3) is not empty and that the current robust trigger-surplus theorem alone does not remove it. It is nonetheless safely below the current terminal critical ratio threshold in that calibration.

## 7. First unpaid implication and handoff

The next useful target for `fleet01/B19` is therefore narrower than generic terminal closure:

> **LOWJ-DIFFUSE-TERMINAL-TO-KL:** On a minimum-dimensional all-block critical core with `J` small and `max_i q_i/J = O(1/log(1/J))`, convert the near-character rare defect into a nonreused occurrence-KL or conditional-support payment strong enough to bound `F/J`, without a Fannes term depending on ambient spectral support.

The exact constraints available to that step are (3.1), (4.2), all-block terminality, the co-pair identities, and the current correction that fixed-depth KL projections do not suffice. A successful proof must therefore be multiscale/nonlocal or exploit additional common-source Boolean structure.

**Full uniform-cube FEI remains OPEN / NOT PROVED.**
