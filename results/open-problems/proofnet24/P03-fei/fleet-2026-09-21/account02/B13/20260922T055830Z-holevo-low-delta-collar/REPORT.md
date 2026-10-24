# account02/B13 — two-channel Holevo collar for the minimum all-gate critical core

**Run:** `20260922T055830Z-b13-fei-small-delta-joint-credit`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated GitHub controls and scientific artifacts were consumed, but no separately verified native research-brain receiver/context was used).  
**Model self-report:** `GPT-5.6 Sol`.  
**Reasoning requested:** maximum actually supported.  
**Reasoning configured:** `UNKNOWN` (the exposed scheduler schema has no model/reasoning selector).  
**Reasoning known/exposed usage:** `UNKNOWN / NOT_EXPOSED`.

## 0. Compact conditional universal argument and first missing implication

The live account01/B18 candidate is

\[
C^\dagger=6.521851214,\qquad
C_0=6.4548,\qquad
a^\dagger=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u).
\]

For a Boolean gate \(G\) at product bias \(p\), put

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
  [\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

The source gate reformulation gives the exact conditional chain:

1. prove \(D_{\Gamma^\dagger}(P;p)\ge0\) for every composition-prime Boolean gate \(P\) and every interior product bias;
2. use the exact nonnegative composition cocycle to get the same inequality for every Boolean gate;
3. apply the gate equivalence to obtain
   \[
   H(f)\le C^\dagger I(f)
   \]
   for every uniform-cube Boolean \(f\).

Full FEI is therefore reduced to the fixed all-gate inequality, but step 1 is still open.

The latest A-lead report I read completely is

`account01/B18/20260922T050337Z-complementary-mux-address-tube/REPORT.md`
(blob `ce379eac385c9f388d2a72f5c10f3a0f6611fca9`).

It closes the complementary-data MUX in the source-valid tube
\[
|t-1/2|\le q^2/8192
\]
and leaves unequal-data MUX and general biased prime gates open.  I also use the A-lead source-tail theorem

`account01/B18/20260922T0325Z-addressing-star-cdagger/REPORT.md`
(blob `6deb28dc6f2e8f36da01fdc7ac24f600f7553a5c`),

which proves for \(0<u\le1/2\), \(\ell=\log_2(1/u)\),

\[
\boxed{\Gamma^\dagger(u)>
u(4.9096\,\ell+2.22)+a^\dagger u(1-u).}
\tag{0.1}
\]

The named completed **other-account** result consumed substantively is

`account04/B13/20260922T051245Z-biased-joint-credit-collar/REPORT.md`
(blob `e77494a14411182d0f20429a349ccfef3d561253`).

It extends my preceding unbiased joint-credit theorem to arbitrary pivot bias and proves: for balanced children, if
\[
u=\min(t,1-t)\le2^{-15},\qquad \delta\ge1/4,
\]
then the exact local gluing term is positive.  Hence a negative balanced-child gluing node in that rare-bias collar must have \(\delta<1/4\).

**First missing implication attacked here.**  The low-disagreement sector
\[
0<\delta<1/4
\]
was not covered by that result.  The main theorem below pays a source-valid rare-bias subregion of exactly this sector, for arbitrary actual Boolean child pairs, by changing category from a lower bound on the joint credit to an upper bound on the two exact entropy costs.

## 1. Last three B13 reports: target-level versus mechanism-level movement

The last three substantive B13 reports are:

1. `20260922T032411Z-gate-block-critical-core`: exact all-block gate restriction cocycle and minimum-essential-arity critical core for the fixed common potential; it localized the universal obstruction to composition-prime gates but did not pay a general local block.
2. `20260922T035349Z-character-tube-prime-defect`: a genuine Boolean character-tube payment and a composition-prime near-dictator family showing that primitivity alone gives no fixed Hamming/spectral gap.
3. `20260922T045511Z-joint-credit-critical-core`: at an unbiased pivot, an exact signed-overlap convexity theorem for
   \(H(B\mid S)+I(S;J)\), giving the balanced-child quarter-influence exclusion \(\delta<1/4\) at a negative central gluing node.

### FULL-PROBLEM CHANGE

**Before:** the fixed \(C^\dagger,\Gamma^\dagger\) all-gate inequality was open, with balanced-child negative gluing still possible in the low-disagreement \(\delta<1/4\) sector at arbitrary bias.

**After:** the full all-gate inequality, and hence full FEI, remain **OPEN**.  However any minimum-essential-arity, bias-minimizing counterexample now obeys an explicit two-sided rare-bias collar at every balanced-child pivot:

\[
\boxed{
\begin{array}{ll}
\delta\ge1/4 &\Longrightarrow\quad u>2^{-15}
\quad\text{(account04/B13)},\\[1ex]
0<\delta\le1/4 &\Longrightarrow\quad
u>2^{-10}\delta^9
\quad\text{(this report).}
\end{array}}
\tag{1.1}
\]

The case \(\delta=0\) is impossible for an essential pivot.  Thus a balanced-child coordinate of a true minimum counterexample cannot approach a product-bias boundary unless its normalized physical disagreement collapses quantitatively.

### MECHANISM CHANGE

The preceding three mechanisms were: physical-block cocycles, signed Boolean Hamming tubes, and an unbiased convex lower bound on the joint information credit.  This run instead:

* **changes category** to a two-pure-state lift of the child spectral laws and uses a Holevo/data-processing upper bound on the branch-spectrum Jensen-Shannon cost;
* rewrites the exact local gluing term as a **sum of two entropy costs**, so the troublesome \(h_2(V_t\delta)\) terms cancel before estimating;
* compactifies the bias cube and chooses a **global bias minimizer** inside the minimum-essential-arity gate, giving a derivative-free secant constraint at every physical pivot.

No affine rebasing, global phase/rank/\(\ell_1\) payment, sign-free realizability relaxation, ordinary derivative-depth payment, or fixed-relative near-subcube shortcut is used.

## 2. A bias-minimizing minimum-essential-arity critical core

This is a small but exact strengthening of the earlier critical-core reduction.

Assume \(D_{\Gamma^\dagger}<0\) somewhere.  Choose a violating Boolean gate \(G\) with minimum essential arity \(k\).  The fixed source candidate has its continuous boundary extension, and the physical restriction cocycle gives on a face \(p_j=b\)

\[
D_{\Gamma^\dagger}(G;p)=D_{\Gamma^\dagger}(G_b;p_{-j}),
\qquad b\in\{0,1\},
\tag{2.1}
\]

after deleting inessential inputs.  By minimum essential arity, every proper physical restriction has nonnegative slack for every residual bias.

Now minimize \(D_{\Gamma^\dagger}(G;\cdot)\) over the closed bias cube.  Since a negative value exists while every boundary face is nonnegative, a global minimizer \(p^*\) is interior and has

\[
D_*:=D_{\Gamma^\dagger}(G;p^*)<0.
\tag{2.2}
\]

Fix a physical pivot \(j\), set \(t=p_j^*\), \(q=1-t\), and write

\[
d_b=D_{\Gamma^\dagger}(G_b;p^*_{-j})\ge0.
\]

Let \(\mathcal L_j(t)\) be the exact local gluing term in the one-coordinate cocycle.  Then

\[
D_*=q d_0+t d_1+\mathcal L_j(t),
\tag{2.3}
\]
so immediately
\[
\boxed{\mathcal L_j(t)<0\quad\text{for every physical pivot }j.}
\tag{2.4}
\]

The global-minimum property also gives \(D_*\le d_0,d_1\).  Hence

\[
\mathcal L_j(t)\le -t(d_1-d_0),
\qquad
\mathcal L_j(t)\le q(d_1-d_0),
\]
and therefore, with \(u=\min(t,q)\),

\[
\boxed{
\mathcal L_j(t)\le -u\,|d_1-d_0|.
}
\tag{2.5}
\]

This is derivative-free and survives piecewise-linear knots of the source potential.  At a point where the one-dimensional section is twice differentiable one additionally has

\[
\mathcal L_j'(t)=d_0-d_1,\qquad
\mathcal L_j''(t)\ge0,
\tag{2.6}
\]

but no smoothness is required below.

The exact composition cocycle from the prior core reduction still permits \(G\) to be chosen composition-prime.  Thus the properties “composition-prime”, “minimum essential arity”, “interior global bias minimizer”, and “every physical pivot has negative local gluing” can be imposed simultaneously.

## 3. Exact two-channel form of the local gluing term

Let \(f_b=(-1)^{G_b}\), \(b\in\{0,1\}\), be the two actual Boolean children on the common residual product space.  Expand them in the residual biased orthonormal Fourier basis,

\[
f_0=\sum_S a_S\chi_S,\qquad
f_1=\sum_S b_S\chi_S.
\]

Write

\[
\delta=\Pr(f_0\ne f_1).
\]

Booleanity gives the exact signed overlap

\[
\boxed{
\sum_S a_Sb_S=\mathbb E[f_0f_1]=1-2\delta.
}
\tag{3.1}
\]

Let

\[
P_S=a_S^2,\qquad Q_S=b_S^2.
\]

If \(B\in\{0,1\}\) is the physical branch with
\(\Pr(B=1)=t\), and \(S\) is the child spectral atom, then

\[
I(B;S)=\operatorname{JS}_t(P,Q).
\tag{3.2}
\]

The parent Fourier pair over residual atom \(S\) is

\[
\alpha_S=q a_S+t b_S,\qquad
\beta_S=\sqrt{tq}\,(b_S-a_S),
\tag{3.3}
\]

and

\[
\alpha_S^2+\beta_S^2=q a_S^2+t b_S^2.
\tag{3.4}
\]

Let \(J\) be the parent spectral indicator of whether the pivot coordinate is present.  Then

\[
\Pr(J=1)=\sum_S\beta_S^2
=tq\|f_1-f_0\|_2^2
=4tq\,\delta
=V_t\delta.
\tag{3.5}
\]

Therefore

\[
H(B\mid S)=h_2(t)-I(B;S),
\tag{3.6}
\]
\[
I(S;J)=h_2(V_t\delta)-H(J\mid S).
\tag{3.7}
\]

The exact account04/B17 local cocycle, written using its
\(\mathcal R_{\Gamma,j}+\mathcal C_j\), now simplifies **without an inequality** to

\[
\boxed{
\begin{aligned}
\mathcal L_{\Gamma,j}
={}&
q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(qr_0+tr_1)\\
&+\delta[\Gamma(t)+h_2(V_t)]
-I(B;S)-H(J\mid S).
\end{aligned}}
\tag{3.8}
\]

This cancellation is the reason to upper-bound the two actual costs rather than lower-bound \(\mathcal C_j\): the two global binary entropies \(h_2(t)\) and \(h_2(V_t\delta)\) disappear before any estimate.

## 4. New theorem: a signed Boolean Holevo bound for the branch-spectrum cost

Define the Bhattacharyya overlap of the two **actual child spectral laws**

\[
\operatorname{BC}(P,Q)=\sum_S |a_Sb_S|.
\]

The signed Boolean identity (3.1) gives

\[
\boxed{\operatorname{BC}(P,Q)\ge |1-2\delta|.}
\tag{4.1}
\]

This is where Boolean sign compatibility enters; the proof is not a statement about arbitrary unrelated probability laws.

Now form two pure states in the span of the spectral labels,

\[
|\psi_0\rangle=\sum_S |a_S|\,|S\rangle,
\qquad
|\psi_1\rangle=\sum_S |b_S|\,|S\rangle.
\]

Their overlap is \(\operatorname{BC}(P,Q)\).  Measuring in the \(|S\rangle\) basis produces exactly the classical channel \(B\mapsto S\) with output laws \(P,Q\).  By data processing for relative entropy (equivalently the binary pure-state Holevo bound),

\[
I(B;S)
\le
S\!\left(q|\psi_0\rangle\!\langle\psi_0|
+t|\psi_1\rangle\!\langle\psi_1|\right).
\tag{4.2}
\]

The mixture has rank at most two.  Its smaller eigenvalue is

\[
\lambda_{\rm BC}
=
\frac{1-\sqrt{1-4tq(1-\operatorname{BC}^2)}}2.
\]

Since \(h_2\) is increasing on \([0,1/2]\), (4.1) yields the dimension-free bound

\[
\boxed{
I(B;S)
\le
\chi_t(\delta):=
h_2\!\left(
\frac{1-\sqrt{1-4V_t\delta(1-\delta)}}2
\right).
}
\tag{4.3}
\]

The second channel has the trivial but exact entropy cap

\[
\boxed{
H(J\mid S)\le H(J)=h_2(V_t\delta).
}
\tag{4.4}
\]

Combining (3.8), (4.3), and (4.4) proves for **arbitrary actual Boolean child pairs**

\[
\boxed{
\begin{aligned}
\mathcal L_{\Gamma,j}\ge{}&
q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(qr_0+tr_1)\\
&+\delta[\Gamma(t)+h_2(V_t)]
-\chi_t(\delta)-h_2(V_t\delta).
\end{aligned}}
\tag{4.5}
\]

No concavity of \(\Gamma\) is assumed.  The only remaining child-output object is exactly the source potential Jensen term.

For balanced children \(r_0=r_1=1/2\), symmetry gives zero Jensen term, hence

\[
\boxed{
\mathcal L_{\Gamma,j}\ge
\delta[\Gamma(t)+h_2(V_t)]
-\chi_t(\delta)-h_2(V_t\delta).
}
\tag{4.6}
\]

This is the input to the low-disagreement collar.

## 5. New low-disagreement rare-bias collar

### Theorem 5.1

For the live \(\Gamma^\dagger\), suppose a physical pivot has balanced Boolean children and

\[
0<\delta\le\frac14.
\]

Put \(u=\min(t,1-t)\).  If

\[
\boxed{
u\le 2^{-10}\delta^9,
}
\tag{5.1}
\]

then

\[
\boxed{
\mathcal L_{\Gamma^\dagger,j}>0.
}
\tag{5.2}
\]

Consequently a negative balanced-child gluing node with \(0<\delta\le1/4\) must satisfy

\[
\boxed{
u>2^{-10}\delta^9.
}
\tag{5.3}
\]

### Proof

By symmetry assume \(t=u\le1/2\), and put

\[
V=4u(1-u),\qquad
\ell=\log_2(1/u),\qquad
d=\log_2(1/\delta).
\]

From (5.1), \(u\le2^{-10}\), so \(V\le1/256\).

Set

\[
x=4V\delta(1-\delta),\qquad
\lambda=\frac{1-\sqrt{1-x}}2.
\]

Because \(4\delta(1-\delta)\le1\), \(x\le V\le1/256\).  Using
\(\sqrt{1-x}\ge1-x\),

\[
\lambda
=
\frac{x}{2(1+\sqrt{1-x})}
\le
\frac{128}{511}x
=
\frac{512}{511}V\delta(1-\delta).
\tag{5.4}
\]

Write

\[
\kappa={512\over511}.
\]

The standard binary-entropy bounds

\[
z\log_2(1/z)\le h_2(z)
\le z\log_2(e/z)
\tag{5.5}
\]

give from (4.6),

\[
\begin{aligned}
{\mathcal L_{\Gamma^\dagger,j}\over\delta}
>{}&
\Gamma^\dagger(u)
+V\log_2(1/V)
-V\log_2{e\over V\delta}\\
&-\kappa V(1-\delta)
 \log_2{e\over V\delta(1-\delta)}.
\end{aligned}
\tag{5.6}
\]

The source-tail theorem (0.1) allows us to discard its positive quadratic term and retain

\[
\Gamma^\dagger(u)>u(4.9096\,\ell+2.22).
\tag{5.7}
\]

Also

\[
V\le4u,\qquad
\log_2(1/V)\le\ell-1,
\]
\[
\log_2 e<\frac32,\qquad
\log_2{1\over1-\delta}
\le\log_2{4\over3}<\frac12.
\]

Applying these only in the adverse direction to (5.6) gives

\[
{\mathcal L_{\Gamma^\dagger,j}\over\delta u}
>
A\ell-Bd+C,
\tag{5.8}
\]
where the constants are exactly

\[
A=4.9096-4\kappa
={576007\over638750}>0,
\]
\[
B=4+4\kappa={4092\over511},
\]
\[
C=2.22-6-4\kappa
=-{198979\over25550}.
\tag{5.9}
\]

Condition (5.1) is precisely

\[
\ell\ge10+9d.
\]

Therefore

\[
\begin{aligned}
A\ell-Bd+C
&\ge(9A-B)d+(10A+C)\\
&=
{69063\over638750}\,d
+
{157119\over127750}
>0.
\end{aligned}
\tag{5.10}
\]

This proves (5.2).  QED.

The exponent \(9\) and factor \(2^{-10}\) are deliberately conservative.  No claim is made that they are sharp.

## 6. Combined critical-core collar using the other-account theorem

Account04/B13's completed theorem gives, for the same balanced-child local gluing problem,

\[
\delta\ge1/4,\quad
u\le2^{-15}
\quad\Longrightarrow\quad
\mathcal L_{\Gamma^\dagger,j}>0.
\tag{6.1}
\]

Theorem 5.1 gives the complementary low-disagreement branch

\[
0<\delta\le1/4,\quad
u\le2^{-10}\delta^9
\quad\Longrightarrow\quad
\mathcal L_{\Gamma^\dagger,j}>0.
\tag{6.2}
\]

Insert these into the bias-minimizing critical core of Section 2, where every pivot has \(\mathcal L_j<0\).  Every balanced-child pivot of such a counterexample must therefore obey exactly the piecewise exclusion (1.1).

This is a property of the **same** minimum-essential-arity, composition-prime, physical-restriction critical core that the all-gate induction uses.  It is not an every-function shell statement.

## 7. Tensor and gauge quantifiers

The theorem was checked against the quantifiers that invalidated earlier B13 shortcuts.

### Common disjoint tensor factor

Replace both children by \(f_0h,f_1h\) on an additional disjoint Boolean block.  Then

* physical disagreement remains \(\delta\);
* the square spectra become \(P\otimes R,Q\otimes R\);
* \(\operatorname{BC}(P\otimes R,Q\otimes R)=\operatorname{BC}(P,Q)\);
* \(I(B;S)\) is unchanged because the extra spectral factor is independent of \(B\);
* \(H(J\mid S)\) is unchanged.

Thus (4.5) has **zero common-tensor tax**.  The tensor operation is used only as a consistency test; it is not asserted to be a free operation inside the physical restriction tree.

### Common character multiplication

Multiplying both children by the same residual character translates both spectra by the same permutation.  Hence \(P,Q\), their Bhattacharyya overlap, both information costs, and the bound are unchanged.  Again this is invariance of the theorem, not permission to recenter a physical child for free.

### Affine input changes

No arbitrary affine rebasing is used or claimed invariant.  At biased product measure it is not a free physical operation, consistent with the earlier B13 gauge obstruction.

## 8. Relation to the A lead and what remains unpaid

The A lead's newest report closes a complementary-data MUX tube around balanced address bias.  The theorem here is not another MUX-specific tube: it applies to arbitrary actual Boolean child pairs, but only when the **child output measures are equal and balanced** and the pivot lies in the stated rare-bias/disagreement collar.

The exact remaining universal implication is therefore narrower but still substantial:

* intermediate pivot biases for balanced children;
* unequal child output measures, where
  \[
  q\Gamma^\dagger(r_0)+t\Gamma^\dagger(r_1)
  -\Gamma^\dagger(qr_0+tr_1)
  \]
  must be retained with its true sign;
* the possibility that every pivot of a minimum critical core lies in those unpaid regions.

A useful next attack is to combine the derivative-free secant property (2.5) with the two-channel lower envelope (4.5), rather than attempting another sign-free profile or an affine recentering.

No universal FEI constant is claimed by this report.

## 9. Deliberate out-of-the-box moves used

Following the current fleet rules, this run used three different moves rather than repeating the previous local convexity proof.

* **Move 1 — CHANGE THE CATEGORY.**  The child spectral laws were lifted to two pure states.  Holevo/data processing turns the branch-spectrum Jensen-Shannon cost into a rank-two entropy depending only on the actual signed Boolean overlap.
* **Move 12 — FIND WHAT IS CONSERVED.**  The conserved quantity is
  \(\sum_S a_Sb_S=1-2\delta\), which lower-bounds the pure-state overlap after absolute-amplitude lifting and keeps Boolean orientation in the argument.
* **Move 29 — ADD THE POINTS AT INFINITY.**  The open product-bias cube was compactified using the physical boundary restriction identity.  A false candidate therefore has an interior global bias minimizer with the secant constraint (2.5).

All three moves produced formulas used in the proof; none is only a proposed direction.

## 10. Executed self-check

`verify_holevo_collar.py` is a standard-library self-check, not the proof.  It exhausts every ordered pair of Boolean children through three residual variables at five pivot biases

\[
t\in\{1/2,1/4,1/8,1/16,1/256\}.
\]

It performs 329,060 child-pair/bias checks of:

* the exact signed overlap;
* the Bhattacharyya domination (4.1);
* the Holevo upper bound (4.3);
* the parent two-channel mass identity (3.4);
* \(H(J\mid S)\le h_2(V_t\delta)\).

It also checks the exact rational positivity in (5.9)-(5.10).  The archived execution reports `PASS`; the largest numerical excesses are at floating roundoff scale.  The analytic theorem does not depend on the finite census.

## 11. Status

**Proved this run**

1. the bias-minimizing minimum-essential-arity secant core (2.5);
2. the exact two-channel local identity (3.8);
3. the arbitrary-bias signed Boolean Holevo bound (4.3);
4. the all-child lower envelope (4.5);
5. the low-disagreement rare-bias collar (5.1)-(5.3);
6. the combined piecewise balanced-child collar (1.1) after applying the completed account04/B13 theorem.

**Not proved**

* the all-prime-gate inequality for \(\Gamma^\dagger\);
* local gluing for all intermediate biases or unequal child output measures;
* full uniform-cube FEI.

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**
