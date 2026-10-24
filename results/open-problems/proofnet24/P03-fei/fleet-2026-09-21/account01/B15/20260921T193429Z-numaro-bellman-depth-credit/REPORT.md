# B15 — a sharp Bellman barrier for the full nonstationary Numaro recursive-tree closure

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-context use entered this mathematics.  
**Role:** FEI spectral remainder proof / unequal Fourier magnitudes.  
**Route:** APPROACH 4, with the aggregate one-sided magnitude-flow reduction from the newest B15 handoff.  
**Claim level:** a rigorous theorem for one much larger explicit recursive Boolean class; no publication-priority claim.

## 0. What changed in this run

The previous B15 handoff proved that the stationary heterogeneous Numaro `C`-spine has

\[
1.4993911747781890
<
\lim_d\frac{\mathcal A(F_d)}{I(F_d)}
<
1.4993911747781891
<\frac32,
\]

and explicitly left open the stronger stress test: **allow arbitrary nonstationary subtrees on different branches and see whether the aggregate-flow ratio crosses \(3/2\).**

This run closes that stress test for the entire recursive closure of the exact 18-variable Numaro seed, including arbitrary recursion on both coordinate classes.

Let \(\mathcal T_N\) be the smallest class containing the exact recovered balanced Numaro seed \(G\) and closed under the following operation: in a fresh copy of \(G\), replace any subset of its 18 dictator inputs by arbitrary members of \(\mathcal T_N\) on mutually disjoint variable blocks; leave all other inputs as fresh dictators. The choices can vary from node to node, from depth to depth, and from branch to branch. Thus this is not a stationary recursion and not a one-parameter spine.

The main theorem is

\[
\boxed{
\sup_{F\in\mathcal T_N}
\frac{\mathcal A(F)}{I(F)}
=
R_N,
}
\]

where the exact seed-defined real number \(R_N\) is rigorously enclosed by

\[
\boxed{
1.4993911747781890
\le R_N
\le
1.4993911747781891
<
1.499392
<
\frac32.
}
\]

So **no arbitrary nonstationary recursive tree built from this Numaro seed can refute**
\[
\mathcal A(f)\le \frac32 I(f).
\]
The earlier stationary `C`-spine was already asymptotically sharp for the entire Numaro recursive closure.

This does **not** prove the universal \(3/2\) inequality and therefore does not prove FEI. It removes a concrete and much larger counterexample mechanism.

---

## 1. The quantity being controlled

Write
\[
p_S=\widehat f(S)^2,
\]
and for a physical coordinate \(i\),
\[
L_i(f)
=
\sum_{T:\widehat f(T\cup\{i\})\ne0}
\widehat f(T\cup\{i\})^2
\log_2^+
\frac{|\widehat f(T)|}
     {|\widehat f(T\cup\{i\})|}.
\]
The aggregate one-sided magnitude flow is
\[
\boxed{
\mathcal A(f)=\sum_i L_i(f)
=
\frac12\sum_Sp_S\sum_{i\in S}
\left[\log_2\frac{p_{S\setminus\{i\}}}{p_S}\right]_+.
}
\]

The inherited restriction estimate is
\[
\Delta_iH
\le
\frac3{\ln2}\operatorname{Inf}_i(f)+2L_i(f).
\]
Consequently a universal inequality
\[
\mathcal A(f)\le \kappa I(f)
\]
would imply full FEI with
\[
C=\frac3{\ln2}+2\kappa.
\]
The focused open target is \(\kappa=3/2\).

---

## 2. Exact seed constants

For the recovered balanced 18-variable Numaro seed, coordinates \(1,\dots,9\) form class \(C\), and coordinates \(10,\dots,18\) form class \(A\). Exact integer Walsh arithmetic gives

\[
c:=\alpha_C=|\widehat G(\{i\})|=\frac{57}{256},
\qquad
a:=\alpha_A=|\widehat G(\{i\})|=\frac1{256}.
\]

For an outer coordinate \(i\), write
\[
u_K=\widehat G(K),
\qquad
v_K=\widehat G(K\cup\{i\}),
\]
and define
\[
M_i(q)
=
\sum_{K:v_K\ne0}
v_K^2\log_2^+\frac{|u_K|}{|v_K|q}.
\]

Within a coordinate class \(j\in\{C,A\}\), define
\[
B_j=\sum_{K:u_Kv_K\ne0}v_K^2,
\qquad
C_j=\sum_{K:u_Kv_K\ne0}v_K^2
       \log_2\frac{|u_K|}{|v_K|},
\qquad
L_j=M_j(1).
\]

The exact overlap masses are
\[
\boxed{
B_C=\frac{5613}{32768},
\qquad
B_A=\frac{117}{32768}.
}
\]

The smallest positive overlap ratio \(|u_K|/|v_K|\) is exactly \(1/2\) in class \(C\) and exactly \(1\) in class \(A\).

Since every nontrivial recursive child below the root will have all leaf influences at most
\[
c=\frac{57}{256}<\frac12,
\]
the positive part disappears on every such recursive substitution:
\[
\boxed{
M_C(q)=B_C\log_2(1/q)+C_C
\quad(0<q\le c),
}
\]
and
\[
\boxed{
M_A(q)=B_A\log_2(1/q)+C_A
\quad(0<q\le c).
}
\]
For class \(A\), all overlap ratios are at least one, so \(C_A=L_A\).

---

## 3. A four-state recursion valid for arbitrary branch shapes

For a balanced recursive child \(H\), let its physical leaf influences be
\[
p_x=\operatorname{Inf}_x(H),
\]
and define
\[
I(H)=\sum_xp_x,
\qquad
Q(H)=\sum_xp_x^2,
\qquad
E(H)=\sum_xp_x^2\log_2\frac1{p_x},
\qquad
A(H)=\mathcal A(H).
\]

### Lemma 3.1 — singleton magnitude equals influence throughout the closure

For every \(H\in\mathcal T_N\) and every physical leaf \(x\),
\[
\boxed{
|\widehat H(\{x\})|=\operatorname{Inf}_x(H)=p_x.
}
\]

**Proof.**
It holds for a dictator. Suppose \(F=G(H_1,\ldots,H_{18})\) with balanced disjoint children. If \(x\) belongs to child block \(i\), balanced composition gives
\[
|\widehat F(\{x\})|
=
|\widehat G(\{i\})|\,
|\widehat H_i(\{x\})|,
\]
while influence composition gives
\[
\operatorname{Inf}_x(F)
=
\operatorname{Inf}_i(G)\,
\operatorname{Inf}_x(H_i).
\]
For both Numaro coordinate classes
\[
|\widehat G(\{i\})|
=
\operatorname{Inf}_i(G),
\]
so induction proves the claim. \(\square\)

In particular, if \(H\) is nontrivial then its root multiplier is at most \(c\), so every leaf satisfies \(p_x\le c\). This justifies the full-log formulas of Section 2.

Let
\[
\ell_C=\log_2(1/c),
\qquad
\ell_A=\log_2(1/a)=8.
\]

The baseline state of \(G\), with all 18 inputs dictators, is
\[
I_G=9c+9a,
\qquad
Q_G=9c^2+9a^2=\frac{14625}{32768},
\]
\[
E_G=9c^2\ell_C+9a^2\ell_A,
\qquad
A_G=9L_C+9L_A.
\]

Now replace a class-\(j\) dictator leaf of \(G\) by a nontrivial recursive child \(H\), where
\[
\alpha_j=
\begin{cases}
c,&j=C,\\
a,&j=A.
\end{cases}
\]

The change in the four state variables is exactly
\[
\boxed{
\Delta I=\alpha_j(I(H)-1),
}
\]
\[
\boxed{
\Delta Q=\alpha_j^2(Q(H)-1),
}
\]
\[
\boxed{
\Delta E
=
\alpha_j^2
\left(
E(H)+\ell_jQ(H)-\ell_j
\right),
}
\]
and, by the heterogeneous magnitude-flow composition identity,
\[
\boxed{
\Delta A
=
\alpha_j A(H)
+
B_jE(H)+C_jQ(H)-L_j.
}
\]

Crucially, these increments add independently over different replaced branches. No stationarity, common depth, or identical-child assumption remains.

---

## 4. The sharp affine Bellman barrier

Define
\[
\Phi(H)
=
A(H)-R I(H)-xE(H)-yQ(H)-z.
\]

We now choose \(x,y,R,z\) from the class-\(C\) substitution rule.

First set
\[
\boxed{
x=-\frac{B_C}{c(1-c)}.
}
\]
Then set
\[
\boxed{
y
=
-\frac{C_C-xc^2\ell_C}{c(1-c)}.
}
\]

Finally choose \(R\) and \(z\) by the two conditions
\[
\boxed{
\Phi(G)=0
}
\]
and
\[
\boxed{
-L_C+Rc+xc^2\ell_C+yc^2+cz=0.
}
\]

Equivalently,
\[
z=A_G-RI_G-xE_G-yQ_G,
\]
and
\[
R
=
-\frac{
c(A_G-xE_G-yQ_G)-L_C+xc^2\ell_C+yc^2
}{
c(1-I_G)
}.
\]

The companion exact checker encloses these quantities as
\[
x\in[-0.9896852684475007,-0.9896852684475006],
\]
\[
y\in[-1.4631188449282932,-1.4631188449282931],
\]
\[
\boxed{
R\in[1.4993911747781890,1.4993911747781891],
}
\]
\[
z\in[-0.0275004000253346,-0.0275004000253345].
\]

In particular
\[
x<0,\qquad y<0,\qquad z<0.
\]

### Lemma 4.1 — class \(C\) is exactly neutral for \(\Phi\)

If a class-\(C\) dictator leaf is replaced by a nontrivial child \(H\), then
\[
\boxed{
\Delta\Phi=c\,\Phi(H).
}
\]

**Proof.**
Insert the four increments from Section 3. The coefficients of \(E(H)\) and \(Q(H)\) vanish exactly by the definitions of \(x\) and \(y\), while the constant term vanishes by the defining relation for \(R,z\). What remains is
\[
c\bigl(A(H)-RI(H)-xE(H)-yQ(H)-z\bigr).
\]
\(\square\)

This is the hidden reason all fixed \(k\)-branch `C`-spines with \(kc>1\) converge to the same \(1.499391174778\ldots\) ratio: the entire class-\(C\) recursion is a Bellman coboundary.

---

## 5. Class \(A\) is strictly dissipative

For a class-\(A\) replacement, the same calculation gives
\[
\Delta\Phi
=
a\Phi(H)
+
\eta_E E(H)
+
\eta_Q Q(H)
+
\eta_0,
\]
where
\[
\eta_E
=
B_A+x\,a(1-a),
\]
\[
\eta_Q
=
C_A-xa^2\ell_A+y\,a(1-a),
\]
\[
\eta_0
=
-L_A+Ra+xa^2\ell_A+ya^2+az.
\]

The rational interval certificate proves
\[
\boxed{
\eta_E< -0.0002803000404985<0,
}
\]
\[
\boxed{
\eta_Q>0.0032092247288020>0,
}
\]
and
\[
\eta_0<-0.0031749593779249.
\]

We also have a simple recursive \(Q\)-bound.

### Lemma 5.1 — \(Q(H)\le Q_G<1\) throughout \(\mathcal T_N\)

For every \(H\in\mathcal T_N\),
\[
\boxed{
Q(H)\le Q_G=\frac{14625}{32768}<1.
}
\]

**Proof.**
It is true for \(G\). For a parent obtained by substituting nontrivial children \(H_j\) into a fresh \(G\),
\[
Q(\text{parent})
=
Q_G+
\sum_j\alpha_j^2(Q(H_j)-1).
\]
By induction \(Q(H_j)\le Q_G<1\), so every summand is nonpositive. \(\square\)

Since \(E(H)\ge0\), Lemma 5.1 implies
\[
\eta_EE(H)+\eta_QQ(H)+\eta_0
\le
\eta_QQ_G+\eta_0.
\]
The exact interval checker gives the strict uniform margin
\[
\boxed{
\eta_QQ_G+\eta_0
<
-0.0017426195445896.
}
\]

Therefore every recursive class-\(A\) substitution is strictly dissipative:
\[
\boxed{
\Delta\Phi<a\,\Phi(H).
}
\]

---

## 6. The nonstationary closure theorem

### Theorem 6.1

For every \(F\in\mathcal T_N\),
\[
\boxed{
\Phi(F)\le0.
}
\]
Consequently
\[
\boxed{
\frac{\mathcal A(F)}{I(F)}
<
R
<
1.499392
<
\frac32.
}
\]

**Proof.**
For the baseline seed \(G\), \(\Phi(G)=0\) by construction.

Take a fresh parent \(G\) and replace any collection of its dictator inputs by arbitrary nontrivial children \(H_j\in\mathcal T_N\). The state increments are additive. Class-\(C\) replacements contribute exactly
\[
c\Phi(H_j)\le0
\]
by Lemma 4.1 and induction. Class-\(A\) replacements contribute strictly less than
\[
a\Phi(H_j)\le0
\]
by Section 5. Thus the parent has \(\Phi\le0\).

Finally,
\[
\Phi(F)\le0
\quad\Longrightarrow\quad
A(F)\le RI(F)+xE(F)+yQ(F)+z.
\]
Because \(x,y,z<0\), \(E(F)\ge0\), and \(Q(F)>0\),
\[
A(F)<RI(F).
\]
Divide by \(I(F)>0\). \(\square\)

This proof permits arbitrary branch-dependent choices. In particular it covers:

- different depths on different branches;
- changing the number of recursive \(C\) branches at every node;
- arbitrary recursion on the rare \(A\) branches;
- mixtures of all of these in one tree.

So the earlier stationary `C`-spine was not hiding a nonstationary recursive counterexample.

---

## 7. Sharpness inside the recursive closure

The constant \(R\) is not merely an upper certificate for \(\mathcal T_N\).

Take the pure class-\(C\) spine in which all nine \(C\) inputs recurse and all nine \(A\) inputs terminate at dictators. Every recursive replacement is class \(C\), so the Bellman identity is exact:
\[
\Phi(F_d)=0
\]
at every depth.

For this sequence,
\[
I_{d+1}=9c\,I_d+9a,
\qquad
9c=\frac{513}{256}>1,
\]
so \(I_d\to\infty\). Meanwhile
\[
Q_{d+1}=9c^2Q_d+9a^2,
\qquad
9c^2<1,
\]
and the corresponding \(E_d\) recurrence is also contractive, hence \(Q_d,E_d\) remain bounded. Therefore
\[
\frac{A(F_d)}{I(F_d)}
=
R+\frac{xE_d+yQ_d+z}{I_d}
\longrightarrow R.
\]

Thus
\[
\boxed{
\sup_{F\in\mathcal T_N}\frac{\mathcal A(F)}{I(F)}
=R.
}
\]

The previous numerical/C-spine limit is therefore explained by an exact affine conservation law, not by accidental stationarity.

---

## 8. Consequence for the full FEI strategy

This closes the explicit counterexample search requested by the previous B15 handoff **within the whole recursive Numaro-tree mechanism**.

The important structural lesson is that the near-\(3/2\) number is controlled by a tiny Bellman state
\[
(I,Q,E,A).
\]
The two auxiliary terms
\[
Q=\sum_x\operatorname{Inf}_x(f)^2,
\qquad
E=\sum_x\operatorname{Inf}_x(f)^2
        \log_2\frac1{\operatorname{Inf}_x(f)}
\]
are exactly what convert the branchwise logarithmic corrections into an affine potential.

This suggests a sharper universal target than trying to prove \(\mathcal A\le 3I/2\) naked: seek constants/potentials for which the same compensated quantity
\[
\mathcal A-RI-xE-yQ
\]
is monotone or superharmonic under a suitable universal restriction/composition operation. The Numaro closure shows that an \(E,Q\) correction is not cosmetic: it is precisely the boundary term that explains the residual \(0.0006088\ldots\) gap to \(3/2\).

However, nothing here establishes such a universal Bellman inequality. An arbitrary Boolean function need not be a Numaro recursive composition, need not satisfy singleton-magnitude \(=\) influence, and need not have the two seed overlap kernels above. Full FEI therefore remains OPEN.

The next B15 target should move outside fixed-seed recursion: either

1. derive a seed-independent inequality that dominates the overlap kernel \(M_i(q)\) by a universal \(I,Q,E\) Bellman increment; or
2. construct a genuinely different balanced outer seed whose exact overlap kernel violates every \(R<3/2\) Bellman certificate.

That is now more informative than deeper nonstationary recursion of the same Numaro seed, which Theorem 6.1 completely controls.

---

## 9. Current literature context

A fresh 21 September 2026 primary-source check still finds the unrestricted uniform-cube FEI conjecture open in the relevant current papers.

- González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), develop a restriction/stopping-tree framework and explicitly identify a missing general restriction inequality whose validity would imply full FEI.
- Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for plateaued Boolean functions with sharp class constant \(4\), and for partially bent functions with sharp class constant \(2\); this does not cover arbitrary unequal-magnitude spectra.
- The current repository correction is also essential: Hod's \(\beta(1/2)=6.4547837\ldots\) remains a read-once lower-bound/sharpness candidate, but it is **not** the universal sharp FEI constant because the recovered external Numaro 18-variable seed already exceeds it.

No novelty or publication-priority claim is made for the Bellman identity in this report without a broader prior-art search.

---

## 10. Reproducibility

`check_numaro_bellman_closure.py` is standard-library only. It:

1. reconstructs the exact recovered Numaro truth table and refuses a hash mismatch;
2. computes the integer Walsh transform;
3. verifies both coordinate classes;
4. certifies \(c,a,B_C,B_A,Q_G\) exactly;
5. encloses every logarithmic constant with rational arithmetic;
6. constructs \(x,y,R,z\);
7. verifies \(x,y,z<0\) and \(R<1.499392<3/2\);
8. proves the class-\(A\) residual margin is negative after the universal \(Q\le Q_G\) bound.

The script SHA-256 is

`608c2f3d4c64000cb003d750dcacd07c18947939955083fd69016a67b4192fa2`

and the recorded output SHA-256 is

`2081f3bd1274a9164fe5e39992d678577406072ff33575b4a12a6c242ca8b283`.

The checker is a self-check of the structured theorem, not an independent audit and not evidence that full FEI is proved.

---

## 11. Joint-account D-interface: valuation-depth-filtered KL credits do **not** retain a sign

This run also consumes the named peer result

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260921T170301Z-valuation-tail-majorization/REPORT.md`

at blob `7633ed3dca15ea17d4c17af94e621f4ab3745691`, specifically its all-cost valuation majorization and depth-tail bounds

\[
\mathbb E(r_a-m+1)_+
\le
2\sum_{k=m}^n q_k^\downarrow.
\]

The current joint interface D asks whether those paid valuation tails can be combined with the **negative relative-entropy credits** in the product-shadow identity to pay the actual mesh remainder \(D\). A natural next maneuver would be to spend the \(m\)-th valuation tail only on packets with \(r_a\ge m\), and simultaneously discard the corresponding depth-filtered part of the global product KL credit as if it remained nonnegative.

That maneuver is invalid already on four bits.

Let
\[
f(x)=+1\quad\text{for }x\in\{1,2,4\}\subset\mathbb F_2^4,
\qquad
f(x)=-1\quad\text{otherwise}.
\]
Its unnormalized Walsh vector is exactly
\[
(-10,2,2,-2,2,-2,-2,-6,6,2,2,-2,2,-2,-2,-6).
\]

There are three magnitude packets:
\[
|W|=10:\quad |A|=1,\ r=0,
\]
\[
|W|=2:\quad |A|=12,\ r=2,
\]
\[
|W|=6:\quad |A|=3,\ r=0.
\]

All four spectral marginals are
\[
q_i=\frac38.
\]
Let \(\nu\) be the product law with those marginals. For the depth-two packet, every spectral atom has mass
\[
\mu(S)=\frac1{64},
\]
and its Hamming-level counts are
\[
3\text{ atoms at level }1,\qquad
6\text{ at level }2,\qquad
3\text{ at level }3.
\]
Hence the contribution of **only the \(r=2\) packet** to the product relative entropy is

\[
\begin{aligned}
K_{r=2}
&=
\sum_{S:r(S)=2}
\mu(S)\log_2\frac{\mu(S)}{\nu(S)}\\
&=
\frac3{16}
\log_2\frac{1/64}{(3/8)^2(5/8)^2}\\
&=
\boxed{
\frac3{16}\log_2\frac{64}{225}
}
<0.
\end{aligned}
\]

Numerically,
\[
K_{r=2}=-0.340083973353194\ldots.
\]

Thus:
\[
\boxed{
\text{the global KL credit is nonnegative, but a valuation-depth-filtered KL credit can be negative.}
}
\]

This gives a precise incompatibility between the account02 valuation-tail theorem and the simplest depth-by-depth credit-spending strategy. The tail bound is valid, and the full KL credit is valid, but **their packetwise/depthwise matching does not preserve the sign that makes KL useful**.

Equivalently, a packet-dependent escort parameter \(\theta=\theta(r_a)\) cannot be justified merely by saying “KL is nonnegative”; once the KL summands are reweighted by valuation depth, nonnegativity is lost. Any successful use of the account02 tail theorem with the negative information credits must therefore keep a globally normalized information projection, or prove a new monotonicity/transport statement that controls the cross-depth transfer.

This is not a new FEI counterexample. It is a counterexample to a concrete proposed way of combining the two strongest current arithmetic inputs.

The exact checker `check_depth_filtered_credit.py` has SHA-256

`8af8721b9d850beba80f4be4c9fd00282501c028ba11e01f1280a5a25b0b8e02`

and its recorded output has SHA-256

`e2e386138550b15128ad74374d7ab7a4fb8a541275148d1ba03f445376f8ad1e`.

**Next recipient / missing implication.** This should be handed to the other B15 arithmetic workers: retain account02's weighted valuation-tail payment, but do not slice the KL credit by \(r_a\). The next viable object is a *single globally normalized tilted reference law* whose tilt contains the valuation cost while preserving one genuine KL divergence. The exact task is to choose such a global tilt so that its partition term is \(O(J)\); if that cannot be done, produce a Boolean family showing the partition term still diverges after every admissible global valuation tilt.
