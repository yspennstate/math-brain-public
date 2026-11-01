# P0072 — stochastic extinction of every internal non-geodesic edge on two-terminal suspension graphs

Status: **new restricted theorem / PROVED CANDIDATE after self-review; full canonical P0072 remains OPEN; publication novelty UNVERIFIED**.

This note continues the exact loop-erased spanning-forest route already established in this own root. The only imported mathematical dependency is the exact identity proved in `research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T063200Z__P0072_spanning_forest_dual_and_suspension_ODE.md`:

\[
\frac{p_e(c)}{c_e}
 =R_{s,t}(c)\,\Pr_{\mathbb F_{s,t}^{c}}(u,v\text{ lie in different full forest components}),
\tag{1}
\]

for an internal edge \(e=uv\), where \(p_e(c)\) is the probability that the next loop-erased ant uses \(e\), and \(\mathbb F_{s,t}^{c}\) is the weighted spanning two-forest law with exactly two components separating the terminals. The same prior note proved, for every interior vertex \(i\) adjacent to both terminals,

\[
\frac{p_{si}(c)}{c_{si}}+\frac{p_{it}(c)}{c_{it}}=R_{s,t}(c).
\tag{2}
\]

No deterministic mean-ODE convergence theorem is used below; the proof is directly stochastic.

## 1. Graph and process

Let \(G\) be a finite **two-terminal suspension graph**. Thus there are terminals \(s,t\), a finite nonempty interior vertex set \(I\), both terminal edges \(si,it\) for every \(i\in I\), and an arbitrary finite internal graph \(H=(I,E_H)\). Every \(s-i-t\) path has length two, hence every edge of \(E_H\) is non-geodesic.

Run the loop-erased reinforcement process with initial edge weights equal to positive integers; in particular this includes the source normalization in which every edge initially has weight one. Let \(W_e(n)\) be the raw weight after \(n\) ants. Each loop-erased path is simple, so every edge is reinforced at most once by one ant.

For terminal edges write

\[
L_i(n)=W_{si}(n),\qquad R_i(n)=W_{it}(n).
\]

Every reinforced \(s\)-to-\(t\) path uses exactly one edge incident to \(s\) and exactly one edge incident to \(t\). Therefore the two terminal totals are equal for all \(n\):

\[
S_n:=\sum_{i\in I}L_i(n)=\sum_{i\in I}R_i(n)=S_0+n.
\tag{3}
\]

Normalize by this common scale:

\[
l_i(n)=\frac{L_i(n)}{S_n},\qquad
r_i(n)=\frac{R_i(n)}{S_n},\qquad
h_e(n)=\frac{W_e(n)}{S_n}\quad(e\in E_H).
\tag{4}
\]

Thus \(\sum_i l_i=\sum_i r_i=1\). Let

\[
D_n:=\|l(n)-r(n)\|_1.
\tag{5}
\]

Let \(\mathcal R_n\) denote the effective resistance between \(s,t\) in the raw conductance network \(W(n)\), and let

\[
\rho_n:=S_n\mathcal R_n
\tag{6}
\]

be the effective resistance in the normalized network \((l,r,h)\).

## 2. The theorem

### Theorem

For the loop-erased ant process on every finite two-terminal suspension graph, with positive integer initial weights, almost surely

\[
\boxed{D_n\longrightarrow0}
\tag{7}
\]

and, for every internal edge \(e\in E_H\),

\[
\boxed{h_e(n)=\frac{W_e(n)}{S_n}\longrightarrow0.}
\tag{8}
\]

Consequently every non-geodesic internal edge has sublinear raw growth:

\[
\boxed{W_e(n)=o(n)\qquad(e\in E_H)\quad\text{a.s.}}
\tag{9}
\]

This proves the canonical source conclusion for the **loop-erased rule on the entire suspension class**, but not for arbitrary finite graphs and not for the source's second reinforcement rule. It therefore remains a restricted theorem relative to P0072.

## 3. B13: an exact stochastic Lyapunov identity

The first issue left open by the preceding mean-ODE theorem was stochastic convergence to a boundary face. The useful monotone quantity is not an ODE Lyapunov function but the accumulated **excess effective resistance**.

Fix any interior vertex \(i\). Define

\[
A_i(n):=H_{L_i(n)-1}+H_{R_i(n)-1},
\tag{10}
\]

where \(H_m=\sum_{j=1}^m1/j\) and \(H_0=0\). If the next ant reinforces \(si\), the first summand increases by \(1/L_i(n)\); otherwise it does not change, and similarly on the \(t\)-side. By (2),

\[
\mathbb E[A_i(n+1)-A_i(n)\mid\mathcal F_n]
=\frac{p_{si}(n)}{L_i(n)}+\frac{p_{it}(n)}{R_i(n)}
=\mathcal R_n.
\tag{11}
\]

### 3.1 Deterministic lower bound on resistance

For any unit \(s\)-to-\(t\) flow \(f\), Cauchy--Schwarz on the terminal cut at \(s\) gives

\[
\sum_i\frac{f_{si}^2}{L_i}
\ge\frac{(\sum_i f_{si})^2}{\sum_iL_i}
=\frac1{S_n}.
\tag{12}
\]

The disjoint terminal cut at \(t\) contributes another \(1/S_n\), and internal energy is nonnegative. Thomson's principle therefore gives

\[
\boxed{\mathcal R_n\ge\frac2{S_n}},
\qquad
\boxed{\rho_n\ge2}.
\tag{13}
\]

### 3.2 Summability of the excess

Since \(L_i(n),R_i(n)\le S_n\),

\[
A_i(n)\le2H_{S_n-1}.
\tag{14}
\]

Taking expectations in (11) and summing,

\[
\mathbb E A_i(n)
=A_i(0)+\mathbb E\sum_{k=0}^{n-1}\mathcal R_k.
\tag{15}
\]

Also, because \(S_k=S_0+k\),

\[
\sum_{k=0}^{n-1}\frac2{S_k}
=2(H_{S_n-1}-H_{S_0-1}).
\tag{16}
\]

Combining (14)--(16) gives the uniform bound

\[
\mathbb E\sum_{k=0}^{n-1}\left(\mathcal R_k-\frac2{S_k}\right)
\le 2H_{S_0-1}-A_i(0).
\tag{17}
\]

Every summand is nonnegative by (13). Monotone convergence therefore implies

\[
\boxed{
\sum_{n=0}^{\infty}\left(\mathcal R_n-\frac2{S_n}\right)<\infty
\quad\text{a.s.}
}
\tag{18}
\]

or, using (6),

\[
\boxed{
\sum_{n=0}^{\infty}\frac{\rho_n-2}{S_n}<\infty
\quad\text{a.s.}
}
\tag{19}
\]

This is an exact stochastic statement, not an ODE approximation.

## 4. Excess resistance controls terminal imbalance

We now turn (19) into \(D_n\to0\).

Fix a normalized state \((l,r,h)\) and let \(f\) be its unit energy-minimizing flow. Write \(a_i\) for the flow on \(si\), \(b_i\) for the flow on \(it\), and \(g_e\) for the oriented internal flows. Then \(\sum_i a_i=\sum_i b_i=1\).

The left terminal energy has the exact decomposition

\[
\sum_i\frac{a_i^2}{l_i}
=1+\sum_i\frac{(a_i-l_i)^2}{l_i},
\tag{20}
\]

and similarly

\[
\sum_i\frac{b_i^2}{r_i}
=1+\sum_i\frac{(b_i-r_i)^2}{r_i}.
\tag{21}
\]

Set

\[
E_s'=\sum_i\frac{(a_i-l_i)^2}{l_i},\qquad
E_t'=\sum_i\frac{(b_i-r_i)^2}{r_i},\qquad
E_H=\sum_{e\in E_H}\frac{g_e^2}{h_e}.
\tag{22}
\]

Then

\[
\rho-2=E_s'+E_t'+E_H.
\tag{23}
\]

Because \(\sum_i l_i=\sum_i r_i=1\), Cauchy--Schwarz gives

\[
\|a-l\|_1\le\sqrt{E_s'},
\qquad
\|b-r\|_1\le\sqrt{E_t'}.
\tag{24}
\]

Flow conservation at the interior vertices says that \(a-b\) is the incidence divergence of the internal flow. Hence

\[
\|a-b\|_1\le2\sum_{e\in E_H}|g_e|.
\tag{25}
\]

Since an internal edge is reinforced at most once per ant,

\[
h_e(n)=\frac{W_e(n)}{S_n}
\le \max\left\{1,\frac{W_e(0)}{S_0}\right\}.
\tag{26}
\]

Thus there is a deterministic finite constant

\[
M_H:=\sum_{e\in E_H}\max\left\{1,\frac{W_e(0)}{S_0}\right\}
\tag{27}
\]

such that \(\sum_e h_e(n)\le M_H\) for all \(n\). Another Cauchy--Schwarz inequality gives

\[
\sum_e|g_e|
\le\sqrt{\left(\sum_eh_e\right)E_H}
\le\sqrt{M_HE_H}.
\tag{28}
\]

Combining (24), (25), (28),

\[
D=\|l-r\|_1
\le\sqrt{E_s'}+\sqrt{E_t'}+2\sqrt{M_HE_H}.
\tag{29}
\]

Cauchy--Schwarz once more yields

\[
\boxed{
D^2\le(2+4M_H)(E_s'+E_t'+E_H)
=(2+4M_H)(\rho-2).
}
\tag{30}
\]

Together with (19),

\[
\boxed{
\sum_{n=0}^{\infty}\frac{D_n^2}{S_n}<\infty
\quad\text{a.s.}
}
\tag{31}
\]

Finally, one ant changes each normalized terminal vector by at most \(|I|/(S_n+1)\) in \(\ell^1\), so

\[
|D_{n+1}-D_n|\le\frac{2|I|}{S_n+1}.
\tag{32}
\]

We use the elementary excursion lemma: if \(z_n\ge0\), \(|z_{n+1}-z_n|\le C/S_n\), \(S_n=S_0+n\), and \(\sum z_n^2/S_n<\infty\), then \(z_n\to0\). Indeed, if \(\limsup z_n>\varepsilon\), either \(z_n\ge\varepsilon/2\) eventually, which contradicts divergence of \(\sum1/S_n\), or there are infinitely many disjoint excursions from \(\varepsilon/2\) to \(\varepsilon\). Every sufficiently late such excursion needs a fixed positive amount of \(\sum1/S_n\) because of the increment bound, and while traversing it \(z_n\ge\varepsilon/2\), again contradicting summability.

Applying the lemma to (31)--(32) proves

\[
\boxed{D_n\to0\quad\text{a.s.}}
\tag{33}
\]

This is the first half of the theorem.

## 5. B27: swap the quantifiers and prove one uniform edge contraction inequality

The remaining task is to exclude positive normalized mass on **every** internal edge simultaneously. Instead of studying the many boundary faces one by one, we prove a statewise inequality that works for every internal edge whenever \(D\) is small.

### 5.1 Exact internal-forest factorization

Fix a normalized state. Consider an internal spanning forest \(F\subseteq H\). For an internal component \(C\) define

\[
L(C)=\sum_{i\in C}l_i,
\qquad
R(C)=\sum_{i\in C}r_i,
\qquad
M(C)=L(C)+R(C).
\tag{34}
\]

In a spanning two-forest separating \(s,t\), every internal component must attach to exactly one terminal by exactly one terminal edge. Summing over the possible attachment vertex and terminal therefore shows that the total two-forest weight lying above \(F\) is

\[
\left(\prod_{f\in F}h_f\right)
\prod_{C\in\operatorname{Comp}(F)}M(C).
\tag{35}
\]

This is a bijective factorization: choosing for each component one terminal side and one incident terminal edge produces exactly one full separating two-forest, and every such two-forest arises uniquely this way.

Fix an internal edge \(e=uv\). If \(u,v\) lie in distinct internal components \(C,D\) of \(F\), the total weight among the configurations above \(F\) in which \(u,v\) lie on opposite full terminal sides is

\[
\left(\prod_{f\in F}h_f\right)
\bigl[L(C)R(D)+R(C)L(D)\bigr]
\prod_{B\neq C,D}M(B).
\tag{36}
\]

Put

\[
a=M(C),\qquad b=M(D),\qquad
d_C=L(C)-R(C),\qquad d_D=L(D)-R(D).
\tag{37}
\]

Then

\[
L(C)R(D)+R(C)L(D)=\frac{ab-d_Cd_D}{2}.
\tag{38}
\]

Moreover

\[
|d_C|\le\min(a,D),\qquad |d_D|\le\min(b,D),
\tag{39}
\]

where \(D=\|l-r\|_1\).

### 5.2 Pair each separating forest with the forest obtained by adding e

The map

\[
F\longmapsto F+e
\tag{40}
\]

is a bijection between internal forests not containing \(e\) in which \(u,v\) are in distinct components and internal forests containing \(e\): the inverse removes \(e\). For the pair \(F,F+e\), the two denominator contributions from (35), after removing the common positive factor, are

\[
ab\qquad\text{and}\qquad h_e(a+b).
\tag{41}
\]

All internal forests not belonging to one of these pairs add nonnegative weight to the denominator and nothing to the numerator in (36). Therefore the full two-forest separation probability is bounded by the largest paired ratio

\[
\frac{(ab-d_Cd_D)/2}{ab+h_e(a+b)}.
\tag{42}
\]

Now

\[
\min(a,D)\min(b,D)\le D\sqrt{ab},
\tag{43}
\]

because \(\min(a,D)\le\sqrt{aD}\) and similarly for \(b\). Put \(x=\sqrt{ab}\). Since the component masses sum to two, \(a+b\le2\), hence \(x\le1\), while \(a+b\ge2x\). Thus

\[
\frac{ab/2}{ab+h_e(a+b)}
\le\frac{x}{2(x+2h_e)}
\le\frac1{2(1+2h_e)},
\tag{44}
\]

and

\[
\frac{D\sqrt{ab}/2}{ab+h_e(a+b)}
\le\frac{D}{2(x+2h_e)}
\le\frac{D}{4h_e}.
\tag{45}
\]

Consequently

\[
\boxed{
\Pr_{\mathbb F_{s,t}}(u,v\text{ lie on opposite full sides})
\le
\frac1{2(1+2h_e)}+\frac{D}{4h_e}.
}
\tag{46}
\]

At \(D=0\), this recovers and quantitatively strengthens the strict balanced-manifold inequality from the preceding run.

### 5.3 A direct upper bound on normalized resistance

Ignore all internal edges and retain only the parallel length-two branches \(s-i-t\). Their total conductance is

\[
C_0=\sum_i\frac{l_ir_i}{l_i+r_i}.
\tag{47}
\]

Write

\[
m_i=\frac{l_i+r_i}{2},\qquad
\delta_i=\frac{l_i-r_i}{2}.
\tag{48}
\]

Then

\[
\frac{l_ir_i}{l_i+r_i}
=\frac{m_i}{2}-\frac{\delta_i^2}{2m_i}.
\tag{49}
\]

Because \(|\delta_i|\le m_i\),

\[
\sum_i\frac{\delta_i^2}{m_i}
\le\sum_i|\delta_i|=\frac D2.
\tag{50}
\]

Since \(\sum_i m_i=1\),

\[
C_0\ge\frac12-\frac D4.
\tag{51}
\]

Adding internal conductances can only decrease effective resistance, so whenever \(D<2\),

\[
\boxed{
\rho\le\frac{2}{1-D/2}.
}
\tag{52}
\]

### 5.4 Uniform negative drift above every positive internal scale

Combining the exact duality (1) in normalized variables, (46), and (52) yields

\[
\boxed{
\frac{p_e}{h_e}
\le
\frac1{1-D/2}
\left(
\frac1{1+2h_e}+\frac{D}{2h_e}
\right).
}
\tag{53}
\]

Fix \(\varepsilon>0\). The right side is decreasing in \(h_e\) and increasing in \(D\). Solving the strict inequality at \(h_e=\varepsilon\) gives

\[
\frac1{1-D/2}
\left(
\frac1{1+2\varepsilon}+\frac{D}{2\varepsilon}
\right)<1
\quad\Longleftrightarrow\quad
D<\frac{4\varepsilon^2}{(1+\varepsilon)(1+2\varepsilon)}.
\tag{54}
\]

By (33), for every \(\varepsilon>0\) there is an almost-sure finite random time after which (54) holds. Hence there exists \(q_\varepsilon<1\) such that eventually, uniformly over all states with \(h_e\ge\varepsilon\),

\[
\boxed{p_e\le q_\varepsilon h_e.}
\tag{55}
\]

This is the desired boundary-repulsion estimate. It is stronger than saying that each bad boundary equilibrium is unstable: it gives one explicit inward inequality on the entire strip \(h_e\ge\varepsilon\) once the terminal imbalance is small.

## 6. B21: stochastic-approximation noise becomes a convergent martingale tail

The normalized internal coordinate obeys the exact recursion

\[
h_e(n+1)-h_e(n)
=\frac{I_e(n+1)-h_e(n)}{S_n+1},
\tag{56}
\]

where \(I_e(n+1)\in\{0,1\}\) records whether ant \(n+1\) uses \(e\). With

\[
\xi_e(n+1)=I_e(n+1)-p_e(n),
\tag{57}
\]

this is

\[
h_e(n+1)-h_e(n)
=\frac{p_e(n)-h_e(n)}{S_n+1}
+\frac{\xi_e(n+1)}{S_n+1}.
\tag{58}
\]

The last term is a bounded martingale difference. Therefore

\[
M_e(n):=\sum_{k=0}^{n-1}\frac{\xi_e(k+1)}{S_k+1}
\tag{59}
\]

converges almost surely, since

\[
\sum_k\mathbb E\left[
\left.
\frac{\xi_e(k+1)^2}{(S_k+1)^2}
\right|\mathcal F_k\right]
\le\sum_k\frac1{(S_k+1)^2}<\infty.
\tag{60}
\]

This is exactly the useful part of the classical stochastic-approximation viewpoint. General unstable-equilibrium theorems require hypotheses on instability and noise along a possibly nonisolated boundary set; no such black box is needed here because (55) and the convergent martingale tail give a direct pathwise argument.

Suppose, toward contradiction, that \(\limsup h_e(n)>0\). Choose \(\varepsilon>0\) such that \(\limsup h_e>2\varepsilon\), and go beyond the random time at which (55) holds.

If \(h_e(n)\ge\varepsilon\) eventually, then from (58),

\[
\sum\frac{p_e-h_e}{S_n+1}
\le-(1-q_\varepsilon)\varepsilon\sum\frac1{S_n+1}=-\infty,
\tag{61}
\]

while \(M_e(n)\) converges. This contradicts \(0\le h_e(n)\le\sup_nh_e(n)<\infty\).

Hence \(h_e<\varepsilon\) infinitely often. Since \(\limsup h_e>2\varepsilon\), there must be infinitely many upcrossings from the level \(\varepsilon\) to \(2\varepsilon\). For a sufficiently late upcrossing, take the last crossing of \(\varepsilon\) before the first subsequent hit of \(2\varepsilon\). Throughout that excursion the drift term in (58) is nonpositive by (55). The one-step overshoot of the lower level is at most \(1/(S_n+1)=o(1)\). Therefore the net increase of asymptotically at least \(\varepsilon\) would have to come from a martingale increment \(M_e(m)-M_e(n)\). But convergence of \(M_e\) implies

\[
\sup_{m\ge n}|M_e(m)-M_e(n)|\longrightarrow0.
\tag{62}
\]

This is impossible. Hence \(\limsup h_e\le2\varepsilon\). Since \(\varepsilon>0\) was arbitrary,

\[
\boxed{h_e(n)\to0\quad\text{a.s.}}
\tag{63}
\]

There are finitely many internal edges, so (63) holds simultaneously for all \(e\in E_H\). Equations (3)--(4) then give \(W_e(n)=o(n)\), completing the theorem. ∎

## 7. What this theorem does and does not establish

The previous own-root theorem was deterministic: the mean ODE converges to the geodesic face on all suspension graphs. The present theorem removes the exact stochastic gluing gap for the loop-erased process on that class. It supplies three genuinely stochastic ingredients:

1. exact a.s. summability of normalized excess resistance, (19);
2. a quantitative terminal-balance theorem \(D_n\to0\), (33);
3. an explicit uniform drift barrier (53)--(55) plus convergent-noise upcrossing argument, proving every internal normalized weight tends to zero.

The argument does **not** prove that the individual terminal vectors \(l(n)\) and \(r(n)\) converge coordinatewise to a common random limit, so it does not claim the stronger parent convergence theorem on the whole suspension class. It proves exactly what is needed for the canonical source's loop-erased **non-geodesic sublinearity** conclusion on this class.

The full P0072 source remains open in this work because:

- an arbitrary finite graph need not have a direct length-two branch through every interior vertex;
- the exact terminal-pair identity (2) and direct conductance lower barrier used above are special to the suspension geometry;
- the source also asks for the uniform-geodesic reinforcement rule, to which the spanning-tree/two-forest identity (1) does not automatically transfer.

Those are source-scope gaps, not gaps in the suspension theorem.

## 8. Method outcomes

- **B13 — find what only increases / a monovariant:** successful. The hidden object is accumulated excess resistance; harmonic-number compensators prove the exact summability (19), which forces stochastic terminal balance.
- **B27 — swap the quantifiers:** successful. Rather than exclude one bad boundary face at a time, (53) yields one explicit inequality for every internal edge and every state above a fixed positive internal scale.
- **B21 — import a technique from an analogous field:** partially successful and then simplified. Classical stochastic approximation suggests unstable-boundary exclusion, but the present boundary is nonisolated. The only needed imported structure is square-summable martingale noise; the final nonconvergence argument is elementary and self-contained.

No finite checker is appropriate for this theorem-sized claim. The complete proof is written above; independent audits have not yet been performed.