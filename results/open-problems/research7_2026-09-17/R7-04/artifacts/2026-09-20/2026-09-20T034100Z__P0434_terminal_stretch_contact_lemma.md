# P0434: terminal-stretch invariance inside stabilized finite-support cells, and a contact obstruction

## Scope

Source: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1* (2020), Section 8, Conjecture 8.1, arXiv:1907.10792.

This note is **PROVED PARTIAL** relative to Conjecture 8.1. It proves a structural lemma for arbitrary finite-support laws and exactly identifies why the most naive terminal-mass transport induction fails at M-SERPT record contacts. It does **not** prove or refute the source conjecture.

The SOAP mean-response theorem used below is Theorem 5.5 of Scully--Harchol-Balter--Scheller-Wolf, *SOAP: One Clean Analysis of All Age-Based Scheduling Policies* (2018). We use FCFS tie-breaking, as in the P0434 source and the existing R7-04 calculations.

## 1. Finite-support terminal-stretch family

Fix positive support points

\[
0<x_1<\cdots <x_{k-1}=b
\]

with masses `p_1,...,p_{k-1}>0`, and a terminal mass `r>0`, with

\[
\sum_{i=1}^{k-1}p_i+r=1.
\]

For a tail length `d>0`, let

\[
X_d\in\{x_1,\ldots,x_{k-1},b+d\}.
\]

Keep the arrival rate `lambda` fixed and restrict attention to the stable part of parameter space

\[
\rho(d)=\lambda E[X_d]<1.
\]

Write

\[
\mu:=E[X_d\wedge b]
=\sum_{i=1}^{k-1}p_i x_i+rb,
\]

which is independent of `d`, and

\[
M_2(d):=E[X_d^2]
=\sum_{i=1}^{k-1}p_i x_i^2+r(b+d)^2,
\qquad
\beta:=1-\lambda\mu.
\]

The terminal atom is the only part of the law that moves.

## 2. Why only finitely many M-SERPT contacts occur

On a support interval whose surviving mass is `S_j>r`, the SERPT rank has the form

\[
s_j(a;d)=A_j-a+\frac r{S_j}d.
\]

Its candidate record value at the left endpoint of that support interval is therefore an affine function

\[
L_j(d)=c_j+\alpha_j d,
\qquad
\alpha_j=\frac r{S_j}<1.
\]

At the terminal support point `b`, the residual candidate is simply

\[
L_k(d)=d,
\]

with slope one. M-SERPT is the increasing record envelope of these finitely many affine candidates. Hence its combinatorial record pattern can change only at finitely many pairwise affine contacts. On every open component of the complement of those contact values, the complete ordering of the M-SERPT record candidates is fixed.

Because all prefix slopes are strictly below one, whenever a stable parameter interval reaches sufficiently far to the right, the terminal record `d` dominates every preterminal M-SERPT record.

## 3. Gittins prefix stabilization

For attained age `a<b`, the finite-support Gittins rank is the minimum over finitely many stopping candidates. Every candidate whose stopping endpoint is at or before `b` is independent of `d`. The only candidates that actually use the terminal atom are affine increasing functions of `d`, with positive coefficient.

Consequently there is a finite threshold `d_G` such that for every `d>d_G` for which the queue remains stable, the entire Gittins rank function on `[0,b)` is independent of `d`: every minimizing preterminal stopping rule stops no later than `b`.

Let

\[
H_G:=\sup_{0\le a<b}r_G(a)
\]

for this stabilized prefix rank. If additionally `d>H_G`, then the terminal jump is strictly worse than every preterminal Gittins rank.

## 4. Terminal-stabilized cells

Call an open stable interval `I` of tail lengths **terminal-stabilized** if throughout `I`:

1. the M-SERPT affine record ordering is fixed;
2. the terminal record `d` strictly dominates every preterminal M-SERPT record;
3. the Gittins rank on `[0,b)` is independent of `d`;
4. `d>H_G`, so the terminal Gittins jump strictly dominates every preterminal Gittins rank.

These conditions are deliberately local in `d`; no claim is made that a fixed `lambda` leaves a nonempty far-tail interval before the stability boundary.

## 5. Main structural theorem

### Theorem 5.1 (terminal-stretch invariance and positive slack derivative)

On every terminal-stabilized cell `I`, define

\[
D(d):=E[T_{MS}(X_d)]-E[T_G(X_d)]
\]

and

\[
F(d):=2E[T_G(X_d)]-E[T_{MS}(X_d)]
=E[T_G(X_d)]-D(d).
\]

Then for every `d in I`,

\[
\boxed{D'(d)=0}
\tag{5.1}
\]

and

\[
\boxed{
F'(d)
=
 r\left[
 \frac{\lambda}{2\beta}
 \left(
 \frac{2r(b+d)}{1-\rho(d)}
 +
 \frac{\lambda rM_2(d)}{(1-\rho(d))^2}
 \right)
 +\frac1\beta
 \right]
>0.
}
\tag{5.2}
\]

Thus, inside each stabilized open cell, outward motion of the terminal support point leaves the **additive M-SERPT penalty exactly invariant** and makes the factor-two slack strictly larger. The hardest point of such a cell is its left one-sided boundary.

### Proof

We use the SOAP Theorem 5.5 decomposition into waiting work and residence work.

#### Step 1: all nonterminal M-SERPT tagged responses are constant on the cell

For a tagged size `x_i<=b`, its M-SERPT worst-future record is one of the finitely many preterminal record levels. On a cell with fixed record ordering, every comparison of a new or old job's M-SERPT rank against this tagged threshold has the same truth value throughout the cell.

The terminal record is strictly larger than the threshold. Because M-SERPT is an increasing envelope, once a terminal job reaches age `b` it stays at the terminal plateau and never recycles into a better rank. Hence every new-work cutoff and every old-work interval relevant to the nonterminal tagged job ends at a fixed prefix support boundary, independent of `d`.

Therefore every SOAP work moment and every residence denominator for every nonterminal M-SERPT tagged size is independent of `d` on `I`.

#### Step 2: all nonterminal Gittins tagged responses are constant on the cell

The Gittins prefix rank itself is fixed on `[0,b)`. A nonterminal tagged job therefore has a fixed worst-future rank `R<=H_G`.

For a terminal competing job, the rank jumps at age `b` above `R` and then decreases along the deterministic terminal tail. Its eventual recycled segment below `R` has a length determined only by `R`, not by the total tail length `d`, because `d>H_G>=R`. Thus all new-work cutoffs, old-work intervals, old-work squared moments, and residence denominators seen by a nonterminal Gittins tagged job are independent of `d`.

Hence every nonterminal Gittins tagged response is independent of `d` on `I`.

#### Step 3: the terminal tagged job has the same waiting term under both policies

For the terminal tagged job, the worst future rank at arrival is the terminal rank `d` under both policies. Under FCFS tie-breaking, a newly arriving competing job contributes new `d`-work only until it first **reaches** rank `d`. By terminal dominance this first happens at age `b`, so

\[
E[X_{new}[d]]=E[X_d\wedge b]=\mu.
\]

For old work, equality at the terminal jump is retained under FCFS tie-breaking, and the total squared old-work contribution at threshold `d` is `E[X_d^2]=M_2(d)`. The 0-old load is the full load `rho(d)`. Therefore both policies have the same terminal waiting term

\[
\boxed{
W_\infty(d)
=
\frac{\lambda M_2(d)}
{2(1-\rho(d))\beta}.
}
\tag{5.3}
\]

Differentiating exactly gives

\[
\boxed{
W_\infty'(d)
=
\frac{r\lambda}{2\beta}
\left(
\frac{2(b+d)}{1-\rho(d)}
+
\frac{\lambda M_2(d)}{(1-\rho(d))^2}
\right).
}
\tag{5.4}
\]

#### Step 4: the terminal residence derivatives agree

For M-SERPT, once the terminal record is the strict maximum, the terminal tagged job's worst-future rank is `d` throughout its full service trajectory. Its new-work load is therefore the fixed prefix load `lambda mu`, so

\[
R'_{MS,\,term}(d)=\frac1\beta.
\tag{5.5}
\]

For Gittins, parametrize the terminal tail by the residual `y=b+d-a`. For `y>H_G`, every preterminal rank is better than `y`, and a new competing terminal job first reaches rank `y` at age `b`; therefore the new-work mean is again `mu`. Increasing `d` adds exactly one new unit of tail at residual above `H_G`, so the SOAP residence integral gives

\[
R'_{G,\,term}(d)=\frac1\beta.
\tag{5.6}
\]

The waiting derivative (5.4) is common as well. Thus the derivatives of the two conditional terminal response times are identical.

#### Step 5: average over masses

All nonterminal conditional responses have zero derivative, and the terminal responses have equal derivative. Hence

\[
D'(d)=0.
\]

Moreover only the terminal Gittins conditional response varies with `d`, so

\[
E[T_G]'=r\left(W_\infty'(d)+\frac1\beta\right),
\]

which is exactly (5.2). Every factor is positive under stability. This proves the theorem. `square`

## 6. Consequence: far-tail rays reduce to finitely many contact checks

For a fixed finite-support prefix, the M-SERPT record candidates are a finite affine family. Therefore there are only finitely many record-contact parameters. After Gittins prefix stabilization, every open stable component between contacts satisfies Theorem 5.1 once terminal dominance holds.

Hence continuous optimization in the terminal support location disappears: each such component is controlled by its left one-sided boundary. The remaining obstruction is not motion **inside** a rank cell; it is what happens **at M-SERPT record contacts**.

This is exactly the structural reduction suggested by the earlier three-point calculations, but it now holds for arbitrary finite support.

## 7. The stronger global monotonicity conjecture is false

A tempting next claim would be that

\[
F(d)=2E[T_G]-E[T_{MS}]
\]

is globally nondecreasing as the terminal atom moves outward. That would permit a direct support-merging/transport induction. It is false because M-SERPT can change discontinuously at a record tie under FCFS tie-breaking.

### Exact four-point obstruction

Take

\[
X_d\in\left\{1,\frac52,\frac72,\frac72+d\right\},
\]

with masses

\[
\left(\frac13,\frac1{12},\frac12,\frac1{12}\right)
\]

and arrival rate

\[
\lambda=\frac1{10}.
\]

The four SERPT start values whose running maximum determines M-SERPT are

\[
\frac{d+31}{12},\qquad
\frac{d+19}{8},\qquad
\frac{d+7}{7},\qquad
d.
\tag{7.1}
\]

The first two satisfy

\[
\frac{d+19}{8}-\frac{d+31}{12}
=\frac{d-5}{24}.
\tag{7.2}
\]

Thus `d=5` is an exact M-SERPT record contact. At that parameter

\[
E[X]=3,
\qquad
\rho=\frac3{10}<1.
\]

The exact SOAP evaluator gives

\[
E[T_G]=\frac{52145}{13706},
\qquad
E[T_{MS}]=\frac{57497}{14952},
\]

hence

\[
D(5)=\frac{961}{23496},
\qquad
F(5)=\frac{619013}{164472}.
\tag{7.3}
\]

Immediately to the right of the contact, the new M-SERPT topology is a terminal-stabilized open cell. Its additive penalty is

\[
D(5+)=\frac{1553}{11748}.
\tag{7.4}
\]

For example the exact evaluator returns this same value at both `d=26/5` and `d=6`, as predicted by Theorem 5.1. The preterminal Gittins lower envelope is unchanged across the contact, so its mean response is continuous there. Therefore

\[
F(5+)=E[T_G](5)-D(5+)
=\frac{301999}{82236},
\]

and

\[
\boxed{
F(5)-F(5+)
=D(5+)-D(5)
=\frac{65}{712}>0.
}
\tag{7.5}
\]

So the factor-two slack jumps **downward** when `d` crosses this M-SERPT record contact. This refutes global terminal-stretch monotonicity as a proof route. It is **not** a counterexample to the factor-two conjecture: both one-sided slacks here are strongly positive.

The mechanism is tie-sensitive. At the exact record contact the first two M-SERPT plateau levels agree, so FCFS tie-breaking avoids the strict priority change that appears immediately after the contact.

## 8. New minimal four-atom bottleneck

The continuous part of terminal transport is now solved on stabilized cells. The missing finite-support induction lemma is a **contact-jump inequality**.

A sufficient form would be: at every one-sided M-SERPT record contact `d_c`,

\[
F(d_c+)\ge0
\quad\text{whenever}\quad
F(d_c)\ge0,
\tag{8.1}
\]

or more quantitatively, if

\[
J_c:=D(d_c+)-D(d_c)\ge0,
\]

prove that the pre-contact Gittins slack pays for the jump,

\[
J_c\le F(d_c).
\tag{8.2}
\]

The exact example above shows that the stronger inequality `J_c<=0` is impossible. Therefore the next proof must charge a positive M-SERPT contact jump against already-existing Gittins waiting/residence slack.

This is the useful handoff to P01-B: its finite-support reduction says that finite-support closure is enough for a broad record-regular source class, while Theorem 5.1 removes the continuous terminal-location degrees of freedom. What remains is discrete contact bookkeeping.

## 9. Self-check

The exact checker stored beside this note does four things:

1. symbolically verifies (5.4);
2. reproduces the published SOAP two-point `{2,14}` Gittins example at `lambda=1/20`, obtaining conditional responses `7/3` and `533/27` and overall mean `298/27`;
3. evaluates the four-point contact example entirely in exact rational arithmetic;
4. verifies the contact equation, the open-cell invariance at two distinct post-contact rational parameters, and the exact slack drop `65/712`.

The archived execution ends with `ALL_EXACT_CHECKS_PASS`. This is a self-check, not an independent audit.

## 10. Status

- Full source endpoint: **OPEN / PARTIAL**.
- Fixed source interval: `[2,5]`; `W_MS=3 -> 3`.
- Previous theorem `#supp_+(X)<=3`: retained **PROVED PARTIAL**.
- New arbitrary finite-support terminal-stabilized-cell invariance: **PROVED PARTIAL**.
- Naive global terminal-stretch monotonicity: **REFUTED AS A ROUTE**, by the exact four-point record-contact example; this does not refute Conjecture 8.1.
- New bottleneck: prove a contact-jump charge such as (8.2), then iterate over the finite contact set.
