# B16 — the hierarchical rare-corner escape for the antipodal EQ family is closed

**Classification:** `ESSENTIAL_STEP_APPLIED`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository controls and mathematical sources were consumed, but no authenticated cognitive-brain retrieval/context entered the proof.

## 0. Live candidate and exact peer gap attacked

Fresh owner control revision `2026-09-22.2` supersedes the older Campaign-C half-band assignment and asks every FEI worker to converge on the all-gate inequality. I bind this run to the stable candidate of account01/B18,

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`, blob
`7ea2c548afc0a5fc62f972f9c64df0578f7e0838`:

\[
C_*=6.5218512,
\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p),
\qquad a_*=0.2682048.
\tag{0.1}
\]

The universal missing statement is `LIMIT-PRIME-GATE-LIFT-v1`: for every composition-prime Boolean gate of every finite arity and every interior product bias,

\[
D_{\Gamma_*}(G;p)\ge0.
\tag{0.2}
\]

The exact other-account result attacked here is account04/B13,

`proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0324Z-arbitrary-bias-eq-boundary/REPORT.md`, blob
`58bc9653da0a1db3514c927bc0a88c78b695e10c`.

For the antipodal two-corner gate

\[
\operatorname{EQ}_d=1_{\{0^d,1^d\}},\qquad d\ge3,
\]
that report proved the exact arbitrary-bias formulas and excluded every fixed-ratio approach to the rare corners. Its explicitly remaining boundary mechanism was **hierarchical degeneration of the bias ratios**: one coordinate can be much larger than all the others, so the normalized direction itself tends to a simplex vertex and the fixed-ray leading term is no longer uniformly separated from zero.

This run closes that exact missing mechanism for every fixed arity `d`.

I also use account04/B17,

`proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`, blob
`d32321447c5f30282f243d9a2907ec719d483c92`,

for the exact all-gate normalization and its retained information credits. No credit-free arity induction is used below.

## 1. Exact source formulas

Let independent inputs have biases

\[
p_i\in(0,1),\qquad q_i=1-p_i,
\]
and put

\[
P=\prod_{i=1}^d p_i,\qquad Q=\prod_{i=1}^d q_i,
\qquad r=P+Q.
\]

Account04/B13 proved

\[
\frac{\operatorname{It}_i(\operatorname{EQ}_d;p)}{V_{p_i}}
=P_{-i}+Q_{-i},
\qquad
P_{-i}=\prod_{j\ne i}p_j,
\quad Q_{-i}=\prod_{j\ne i}q_j,
\tag{1.1}
\]

and therefore

\[
D_*^{\rm EQ}(p)
=
\sum_i(P_{-i}+Q_{-i})
\bigl(\Gamma_*(p_i)+h_2(V_{p_i})\bigr)
-\widetilde H_{\rm EQ}(p)-\Gamma_*(P+Q).
\tag{1.2}
\]

The source potential used by the gate programme is the read-once piecewise-linear-in-log potential. The implementation `continuations/2026-09-22-gate-reformulation/gam.py` has, below its final knot,

\[
\Gamma_{\rm RO}(z)
=z\,[B_0+A\log_2(1/z)]
\tag{1.3}
\]

for fixed constants `B_0,A`; the source endpoint calculation used by account04/B13 identifies

\[
A=2(6.4548-4)=4.9096>0.
\tag{1.4}
\]

Hence in the actual tail of the stable candidate

\[
\Gamma_*(z)=A z\log_2(1/z)+Bz-a_*z^2
\tag{1.5}
\]

for another constant `B`. In particular there is an `epsilon_0>0` for which

\[
\Gamma_*'(z)>0\qquad(0<z<\epsilon_0).
\tag{1.6}
\]

This eventual monotonicity is source-exact for the candidate; it is not inferred merely from a sampled asymptotic.

Finally, the certified read-once theorem proves the all-gate inequality on every AND/OR/NOT read-once gate for the potential

\[
\Gamma_{\rm cert}(z)=\Gamma_{\rm RO}(z)+0.01z(1-z).
\tag{1.7}
\]

The quadratic-lift identity gives, for every gate,

\[
D_{\Gamma_*}=D_{\Gamma_{\rm cert}}+\kappa W,
\qquad
\kappa:=a_*-0.01=0.2582048,
\qquad
W=I/4-r(1-r)\ge0.
\tag{1.8}
\]

Thus every read-once gate satisfies

\[
D_{\Gamma_*}\ge\kappa W.
\tag{1.9}
\]

## 2. Uniform nonhierarchical expansion

Set

\[
s=\sum_{i=1}^d p_i,
\qquad
w_i=p_i/s.
\]

The fixed-ray theorem of account04/B13 has leading term `A s H(w)`. For the present use we need the remainder uniformly when `w` is allowed to move.

### Lemma 2.1 — uniform rare-corner expansion

For fixed `d>=3`, as `s->0`, uniformly over all positive bias vectors with sum `s`,

\[
\boxed{
D_*^{\rm EQ}(p)
=A s H_2(w)+O_d\!\left(s^2\log\frac1s\right),
}
\tag{2.1}
\]
where

\[
H_2(w)=\sum_i w_i\log_2\frac1{w_i}.
\]

### Proof

First,

\[
Q=1-s+O_d(s^2),\qquad P=O_d(s^d),
\qquad 1-(P+Q)=s+O_d(s^2),
\tag{2.2}
\]
and uniformly

\[
Q_{-i}=1+O_d(s),\qquad P_{-i}=O_d(s^{d-1}).
\tag{2.3}
\]

Because the tail (1.5) is exact once `s` is sufficiently small,

\[
\sum_i\Gamma_*(p_i)-\Gamma_*(s)
=A\left[\sum_i p_i\log_2\frac1{p_i}-s\log_2\frac1s\right]+O_d(s^2)
=A sH_2(w)+O_d(s^2).
\tag{2.4}
\]

Changing the output argument from `s` to `1-(P+Q)=s+O_d(s^2)` costs
`O_d(s^2 log(1/s))`, because the derivative of (1.5) is `O(log(1/s))`. Multiplying the input potentials by the factors in (2.3) costs the same order. Hence the entire potential part of (1.2) equals

\[
A sH_2(w)+O_d(s^2\log(1/s)).
\tag{2.5}
\]

For the entropy part, compare the squared biased-Walsh law of `EQ_d` with the product subset law whose independent inclusion probabilities are

\[
v_i=V_{p_i}=4p_i(1-p_i).
\]

The product law has entropy `sum_i h_2(v_i)`. From the exact coefficient formula of account04/B13, the empty spectral mass is `1-4s+O_d(s^2)`, the singleton `i` mass is `4p_i+O_d(sp_i)+O_d(P)`, and the total mass on levels at least two is `O_d(s^2)`. The same statements hold for the product subset law. Therefore their total-variation distance is `O_d(s^2)`. Fannes-Audenaert on the fixed alphabet of size `2^d` gives

\[
\widetilde H_{\rm EQ}(p)
=\sum_i h_2(V_{p_i})+O_d(s^2\log(1/s)).
\tag{2.6}
\]

Using (2.3) once more,

\[
\sum_i(P_{-i}+Q_{-i})h_2(V_{p_i})
=\sum_i h_2(V_{p_i})+O_d(s^2\log(1/s)).
\tag{2.7}
\]

Equations (2.5)--(2.7) prove (2.1). `QED`.

### Consequence

Order the coordinates so that

\[
t=p_1=\max_i p_i,
\qquad
u:=\sum_{i=2}^d p_i.
\tag{2.8}
\]

If along a rare-corner sequence `nu/t` is bounded below by some positive constant, then `H_2(w)` is bounded below by a positive constant depending only on that lower bound and `d`. Therefore (2.1) gives

\[
D_*^{\rm EQ}(p)>0
\tag{2.9}
\]

for all sufficiently small `s` on that sequence.

So an unsafe rare-corner sequence, if it existed, would necessarily have

\[
\boxed{\nu/t\to0.}
\tag{2.10}
\]

That is exactly the hierarchical regime left open by the fixed-ray result.

## 3. The hierarchical regime is paid by the one-corner read-once gate

Assume now (2.10). Let

\[
N_d=1_{\{0^d\}}
\]
be the one-corner NOR gate at the same product bias. It is read-once.
Its output probability is `Q`, and

\[
\frac{\operatorname{It}_i(N_d;p)}{V_{p_i}}=Q_{-i}.
\tag{3.1}
\]

Its Poincare currency has an exact elementary form:

\[
W_N
=\frac{I(N_d;p)}4-Q(1-Q)
=Q\left[s-(1-Q)\right].
\tag{3.2}
\]

Write

\[
Q_R=\prod_{i=2}^d(1-p_i),
\qquad x_R=1-Q_R.
\]

Since `Q=(1-t)Q_R`,

\[
s-(1-Q)=t x_R+(\nu-x_R).
\tag{3.3}
\]

The elementary union bounds

\[
0\le \nu-x_R\le\frac{\nu^2}{2},
\qquad
\nu-\frac{\nu^2}{2}\le x_R\le\nu
\tag{3.4}
\]
show, using `nu/t->0`, that

\[
\boxed{W_N=t\nu\,(1+o(1)).}
\tag{3.5}
\]

By the certified read-once theorem and the extra stable quadratic lift, (1.9) gives

\[
\boxed{
D_*^{N}(p)\ge0.2582048\,W_N.
}
\tag{3.6}
\]

Thus it remains only to prove that adding the second antipodal exceptional corner changes the defect by `o(W_N)` in the unfavorable direction.

## 4. Exact spectral perturbation from NOR to EQ

For each nonempty spectral set `S`, let `a_S` be the biased-Walsh coefficient of the NOR sign function and `b_S` the additional coefficient caused by flipping the all-ones corner. Then

\[
a_S=-2Q\,\varphi_S(0^d),
\qquad
b_S=-2P\,\varphi_S(1^d).
\tag{4.1}
\]

Since

\[
|\varphi_S(0^d)\varphi_S(1^d)|=1,
\]
we have the exact, set-independent cross magnitude

\[
|a_Sb_S|=4PQ.
\tag{4.2}
\]

Also Parseval for the one-point perturbation gives

\[
\sum_S b_S^2=4P.
\tag{4.3}
\]

At the empty coefficient, the change is from `1-2Q` to `1-2Q-2P`, whose squared-mass change has magnitude at most `8P`. Summing (4.2)--(4.3) over the fixed `2^d`-point spectral alphabet yields

\[
\boxed{
\|\mu_{\rm EQ}-\mu_N\|_1
\le (8\,2^d+4)P.
}
\tag{4.4}
\]

Hence, by Fannes-Audenaert,

\[
\boxed{
|\widetilde H_{\rm EQ}-\widetilde H_N|
=O_d\!\left(P\log\frac1P\right).
}
\tag{4.5}
\]

Now put

\[
R=\prod_{i=2}^d p_i,
\qquad P=tR,
\qquad m=d-1\ge2.
\]

AM-GM gives

\[
R\le(\nu/m)^m.
\tag{4.6}
\]

For sufficiently small `nu`, the function `x log(1/x)` is increasing, so

\[
R\log\frac1R
\le (\nu/m)^m\log\frac{m^m}{\nu^m}
=O_d(\nu^m\log(1/\nu)).
\tag{4.7}
\]

Because `nu/t->0`, eventually `t>=nu`, and similarly

\[
R\log\frac1t
\le O_d(\nu^m\log(1/\nu)).
\tag{4.8}
\]

Therefore

\[
\frac{P\log(1/P)}{t\nu}
=
\frac{R}{\nu}\left(\log\frac1t+\log\frac1R\right)
=O_d(\nu^{m-1}\log(1/\nu))\to0.
\tag{4.9}
\]

Combining (3.5), (4.5), and (4.9),

\[
\boxed{
|\widetilde H_{\rm EQ}-\widetilde H_N|=o(W_N).
}
\tag{4.10}
\]

## 5. Defect comparison and closure of the hierarchical escape

Subtract the NOR defect from the EQ defect using (1.2) and (3.1):

\[
\begin{aligned}
D_*^{\rm EQ}-D_*^N
={}&\sum_iP_{-i}\bigl(\Gamma_*(p_i)+h_2(V_{p_i})\bigr)\\
&-(\widetilde H_{\rm EQ}-\widetilde H_N)
-[\Gamma_*(P+Q)-\Gamma_*(Q)].
\end{aligned}
\tag{5.1}
\]

The first line is nonnegative except for the displayed entropy difference. For the output-potential term, symmetry gives

\[
\Gamma_*(P+Q)-\Gamma_*(Q)
=\Gamma_*(1-P-Q)-\Gamma_*(1-Q).
\tag{5.2}
\]

Both arguments tend to zero. Moreover

\[
0\le1-P-Q<1-Q,
\]
so eventual monotonicity (1.6) gives

\[
\Gamma_*(P+Q)-\Gamma_*(Q)\le0.
\tag{5.3}
\]

Thus (5.1) implies

\[
D_*^{\rm EQ}
\ge D_*^N-|\widetilde H_{\rm EQ}-\widetilde H_N|.
\tag{5.4}
\]

Using (3.6) and (4.10),

\[
D_*^{\rm EQ}
\ge [0.2582048-o(1)]W_N>0
\tag{5.5}
\]

for every sufficiently deep point of the hierarchical regime.

This contradicts the existence of an unsafe hierarchical rare-corner sequence.

## 6. Main theorem

### Theorem 6.1 — complete simultaneous rare-corner safety for the antipodal family

Fix any finite `d>=3`. For the stable candidate (0.1), there exists
`epsilon_d>0` such that

\[
\boxed{
0<\sum_i p_i<\epsilon_d
\quad\Longrightarrow\quad
D_{\Gamma_*}(\operatorname{EQ}_d;p)>0.
}
\tag{6.1}
\]

By complement symmetry, there is also an `epsilon_d'>0` such that

\[
\boxed{
0<\sum_i(1-p_i)<\epsilon_d'
\quad\Longrightarrow\quad
D_{\Gamma_*}(\operatorname{EQ}_d;p)>0.
}
\tag{6.2}
\]

### Proof

If (6.1) failed, take an unsafe sequence with `s->0`, order it as in (2.8), and pass to a subsequence. Either `nu/t` is bounded below, in which case Lemma 2.1 makes the defect positive, or `nu/t->0`, in which case (5.5) makes the defect positive. Both are contradictions. Equation (6.2) follows from the global complement symmetry already used in the source gate formulation. `QED`.

The theorem is stronger than the fixed-ray result exactly where needed: it permits arbitrary changing bias ratios and therefore includes super-polynomial and iterated-scale hierarchies.

## 7. Exact old/new implication and remaining gap

**Old missing implication:** account04/B13 excluded every fixed rare-corner ray but explicitly left hierarchical regimes in which the direction itself degenerates as the corner is approached.

**New proved inference:** those hierarchical regimes are safe. The dominant-corner gate is a read-once NOR with stable-candidate reserve asymptotic to `0.2582048 t nu`; the second antipodal corner perturbs spectral entropy only by `o(t nu)`, while its source and output-potential corrections are nonnegative in the deep tail. Together with the uniform nonhierarchical expansion, this proves a full rare-corner neighborhood theorem for every fixed `EQ_d`.

**What remains:** this is not `LIMIT-PRIME-GATE-LIFT-v1`. It does not control the compact interior of the antipodal gate, mixed boundary faces, or unrelated composition-prime gate classes. The universal all-gate inequality and full FEI remain open.

**Classification:** `ESSENTIAL_STEP_APPLIED`, because it closes the exact named hierarchical boundary gap of a live adversarial gate family for the fixed universal candidate rather than replacing it by another sufficient condition.

## 8. Source and scope notes

The stable candidate source is account01/B18 blob `7ea2c548afc0a5fc62f972f9c64df0578f7e0838`. The exact arbitrary-bias antipodal formulas and fixed-ray theorem consumed are account04/B13 blob `58bc9653da0a1db3514c927bc0a88c78b695e10c`. The exact restriction/credit cocycle consumed is account04/B17 blob `d32321447c5f30282f243d9a2907ec719d483c92`. The certified read-once theorem used for (3.6) is `continuations/2026-09-21-readonce-certificate/REPORT.md`, blob `ecc3bedeb9acf676056bdfaad6240fc9c89083b4`; the source potential implementation used for the exact tail form is `continuations/2026-09-22-gate-reformulation/gam.py`, blob `7c31af84556be47c214fc94df283b2267b0149ce`.

No external novelty/priority claim is made. Scoped privacy review: this report contains only FEI mathematics, repository-relative source identifiers and sanitized logical provenance; no credentials, scheduler identifiers, machine paths, unrelated private data, benchmark gold, email/Drive content, public-posting action, paid/remote compute, workflow dispatch, notification changes, or permission changes.
