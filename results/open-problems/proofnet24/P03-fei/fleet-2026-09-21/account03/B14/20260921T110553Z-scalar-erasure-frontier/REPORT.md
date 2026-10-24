# B14 — sharp scalar restriction-erasure frontier and hard-core endpoint

**Status:** PARTIAL / PROVED structural theorem. **Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use occurred.  
**Live role:** FEI erasure and selector proof.  
**Fresh mathematical source before the write:** `master` at `7d11b36ab3635253165ed27d4b1c6b63d4d02952`.  
**Owner route:** mass-weighted erasure / existential restriction selector / exact restriction-entropy payment.

This is new mathematics, not a certificate audit or a repeat of the finite FEI atlas. It preserves the refuted arbitrary-prescribed-coordinate payment route. Publication priority is **UNVERIFIED**.

## 1. Starting point and exact question

For one physical coordinate `i`, pair the parent Fourier coefficients as

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}),\qquad
w_T=u_T^2+v_T^2,\qquad q_T=\frac{v_T^2}{w_T}
\]

on nonzero fibres. Put

\[
h(q)=h_2(q),\qquad
j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right),\qquad
\Psi(q)=h(q)+j(q).
\]

The recovered exact restriction identities are

\[
\alpha_i:=\operatorname{Inf}_i(f)=\sum_Tw_Tq_T,
\]

\[
B_i=H(X_i\mid X_{-i})=\sum_Tw_Th(q_T),
\]

\[
\Delta_iH=B_i+JS_i=\sum_Tw_T\Psi(q_T).
\tag{1}
\]

The previous critical-core argument used the pointwise estimate `j(q)<= (2/ln2)q`, giving

\[
\Delta_iH\ge r\alpha_i\quad\Longrightarrow\quad
B_i\ge\left(r-\frac2{\ln2}\right)\alpha_i.
\tag{2}
\]

The exact attempted statement in this run was: **what is the sharp scalar lower payment for `B_i/alpha_i` implied by (1) and `Delta_iH/alpha_i>=r`, without throwing away the fibre distribution?**

## 2. PROVED: the sharp scalar erasure frontier

For `q>0` define

\[
\beta(q)=\frac{h(q)}q,
\qquad
\kappa(q)=\frac{\Psi(q)}q.
\]

For every `r>4`, there is a unique `tau=tau(r) in (0,1/2)` with

\[
\kappa(\tau)=r.
\tag{3}
\]

### Theorem 2.1 — scalar erasure frontier

Let `w_a>=0`, `sum_a w_a=1`, and `q_a in [0,1]`. If

\[
\alpha:=\sum_aw_aq_a>0,
\qquad
\sum_aw_a\Psi(q_a)\ge r\alpha,
\qquad r>4,
\]

then

\[
\boxed{
\sum_aw_ah(q_a)\ge \beta(\tau(r))\,\alpha.
}
\tag{4}
\]

The coefficient `beta(tau(r))` is sharp for this scalar moment problem. Equality in (4), together with equality in the hypothesis, forces every positive-`q` fibre to have `q=tau(r)`; zero fibres may remain.

### Proof

It is enough to prove a global supporting-line inequality for the parametric curve `(kappa(q),beta(q))`.

First work on `0<q<1/2`. Set

\[
P(q)=h(q)-qh'(q),\qquad Q(q)=j(q)-qj'(q).
\]

Since `h(0)=j(0)=0` and both are strictly concave here, `P,Q>0`. Direct differentiation gives

\[
\beta'(q)=-\frac{P(q)}{q^2},
\qquad
\kappa'(q)=-\frac{P(q)+Q(q)}{q^2},
\]

so both functions strictly decrease and the slope of `beta` as a function of `kappa` is

\[
\lambda(q):=\frac{d\beta}{d\kappa}
=\frac{P(q)}{P(q)+Q(q)}\in(0,1).
\tag{5}
\]

We now prove that this curve is strictly convex. Let

\[
y=2\sqrt{q(1-q)}\in(0,1).
\]

A direct calculation yields

\[
j''(q)=\frac{4\,[y-\operatorname{atanh}y]}{(\ln2)y^3}<0.
\tag{6}
\]

Moreover

\[
j'''(q)=\frac{8(1-2q)}{(\ln2)y^5}
\left[3(\operatorname{atanh}y-y)-\frac{y^3}{1-y^2}\right]<0.
\tag{7}
\]

The last sign is elementary from the power series

\[
3(\operatorname{atanh}y-y)
=\sum_{k\ge1}\frac{3}{2k+1}y^{2k+1}
<\sum_{k\ge1}y^{2k+1}
=\frac{y^3}{1-y^2},
\]

where equality occurs only in the first coefficient and the remaining coefficients are strictly smaller.

Now

\[
P'=-qh'',\qquad Q'=-qj'',
\]

and

\[
\frac{Q'}{P'}=\frac{j''}{h''}
=-(\ln2)q(1-q)j''=:R(q).
\]

Because `q<1/2` and both (6),(7) are negative,

\[
R'(q)=-(\ln2)\bigl[(1-2q)j''+q(1-q)j'''\bigr]>0.
\tag{8}
\]

Since `P(0)=Q(0)=0`, the ratio `Q/P` is the `P'`-weighted average of the strictly increasing function `R` on `[0,q]`. Hence `Q/P` strictly increases, and therefore `lambda=1/(1+Q/P)` strictly decreases with `q`. Since `kappa` also decreases with `q`, the slope `d beta/d kappa` strictly increases with `kappa`: `beta` is a strictly convex function of `kappa` on the half-curve `0<q<=1/2`.

Fix `tau=tau(r)` and set

\[
\lambda=\lambda(\tau),\qquad b=\beta(\tau),\qquad d=\lambda r-b.
\]

Strict convexity gives the tangent inequality

\[
\beta(q)\ge b+\lambda\bigl(\kappa(q)-r\bigr)
\qquad(0<q\le1/2).
\tag{9}
\]

We also need the tangent to lie below the origin. For this, put

\[
x=1-2q,\qquad y=2\sqrt{q(1-q)},\qquad
A(z)=\frac{\operatorname{atanh}z}{z}.
\]

Then

\[
\frac{j'(q)}{h'(q)}=\frac{A(y)}{A(x)}.
\]

The power series for `A` has positive coefficients, so `A` is strictly increasing. As `q` increases on `(0,1/2)`, `y` increases and `x` decreases; hence `j'/h'` strictly increases. With `h(0)=j(0)=0`, the usual weighted-average argument gives that `j/h` strictly increases. Therefore

\[
Pj-hQ=q(hj'-h'j)>0,
\]

which is exactly

\[
\lambda>\frac{h}{h+j}=\frac\beta\kappa.
\]

At `q=tau` this yields `d=lambda r-b>0`.

Finally take `q>1/2` and write `q'=1-q`, `a=q'/q in (0,1)`. Symmetry of `h` and `Psi` gives

\[
\beta(q)=a\beta(q'),\qquad\kappa(q)=a\kappa(q').
\]

From (9), `beta(q')-lambda kappa(q')>=-d`. Multiplication by `a in(0,1)` cannot move a number below the negative threshold `-d`: if the number is negative it moves toward zero, and if positive it stays nonnegative. Thus (9) holds for all `q in (0,1]`.

Now size-bias the fibres by

\[
\rho_a=\frac{w_aq_a}{\alpha}.
\]

Then

\[
\mathbb E_\rho\kappa(Q)
=\frac{\sum_aw_a\Psi(q_a)}\alpha\ge r,
\qquad
\mathbb E_\rho\beta(Q)
=\frac{\sum_aw_ah(q_a)}\alpha.
\]

Taking expectations in (9) proves (4). Strict convexity and the strict extension away from `tau` give the equality statement. QED.

## 3. Exact consequence for a restriction-critical FEI core

Let `g` be the recovered physical restriction descendant maximizing

\[
r(g)=H(g)/I(g).
\]

For every relevant coordinate the inherited criticality theorem gives

\[
\Delta_iH(g)\ge r(g)\alpha_i(g).
\]

Applying Theorem 2.1 fibrewise gives the sharper all-coordinate payment

\[
\boxed{
B_i(g)\ge b(r(g))\alpha_i(g),
\qquad
b(r):=\beta(\tau(r)).
}
\tag{10}
\]

For `r>4`, `b(r)` is increasing. This strictly improves the earlier scalar consequence `B_i/alpha_i>=max(r/2,r-2/ln2)` except at limiting regimes where the bounds approach each other.

At the Hod-scale calibration `r_0=6.4547837`, the current-run high-precision calculation gives

\[
\tau(r_0)=0.1805540237871973049\ldots,
\]

\[
\boxed{b(r_0)=3.7733168718839303550\ldots}
\tag{11}
\]

versus the previous bound

\[
r_0-2/\ln2=3.5693936182220731853\ldots.
\]

The gain is

\[
0.2039232536618571698\ldots.
\]

The tangent parameters are

\[
\lambda=0.8686428210743078427\ldots,
\qquad
d=1.8335846507085283969\ldots.
\]

Summing (10) over coordinates sharpens the necessary dual-total-correlation shape of the same core. Since

\[
\operatorname{DTC}(X)=H(g)-\sum_iB_i(g),
\]

one gets at `r=r_0`

\[
\boxed{
\operatorname{DTC}(X)\le
2.6814668281160696450\ldots\,I(g)
=0.4154231888693760\ldots\,H(g).
}
\tag{12}
\]

The preceding erasure bound gave `DTC<= (2/ln2)I`, i.e. about `0.4470 H` at this calibration.

## 4. PROVED endpoint structure: uniform-activity hard-core spectral law

The equality case exposes a new structural endpoint for the selector route.

Suppose the same Boolean function saturates (10) at every relevant coordinate with the same `r>4`, and also has `Delta_iH=r alpha_i` there. Put `tau=tau(r)` and

\[
\theta=\frac{\tau}{1-\tau}\in(0,1).
\]

The equality statement of Theorem 2.1 says that every Fourier pair obeys

\[
q_i(T)=\frac{p_{T\cup\{i\}}}{p_T+p_{T\cup\{i\}}}\in\{0,\tau\}.
\]

Hence whenever the upper coefficient is nonzero,

\[
\frac{p_{T\cup\{i\}}}{p_T}=\theta.
\tag{13}
\]

Therefore the nonzero Fourier support `F={S:p_S>0}` is downward closed, and path multiplication in (13) gives

\[
\boxed{
p_S=p_\varnothing\,\theta^{|S|}\quad(S\in F).}
\tag{14}
\]

Thus the exact all-coordinate scalar endpoint is a **uniform-activity hard-core measure on a downward-closed family**. If the support is the full subset cube, (14) is the product Bernoulli(`tau`) law; the already recovered exact product-spectrum rigidity then rules out a nondegenerate Boolean endpoint with `tau<1/2`. Hence any high-ratio exact endpoint would have to use a proper down-set support.

This does not yet rule out the proper-down-set case and is not promoted to full FEI.

## 5. Attempted refutation and numbers

Two targeted computations were performed to attack, not establish, the theorem.

1. `scalar_frontier.py` discretizes `q in (0,1)`, including `q>1/2`, and solves the linear program
   \[
   \min \mathbb E\beta(Q)\quad\text{s.t.}\quad
   \mathbb E\kappa(Q)\ge6.4547837.
   \]
   The solver returned objective `3.7733168718839325`, mean `kappa=6.454783700000004`, with all displayed mass at `q=0.18055402378719732`. The gap from the analytic value (11) was `2.1e-15`. This is only a refutation attempt; the proof is the calculus argument above.
2. `check_hardcore_endpoint.py` exhaustively searches Boolean functions through four variables for a nonconstant Fourier law having a downward-closed support and one common geometric activity ratio `0<theta<1` as in (14). The current-run targeted enumeration found **zero** such examples for `n=1,2,3,4`. This finite check is not a universal proof and is not an FEI sweep.

## 6. Dead route / what this does not prove

The scalar frontier by itself does **not** close FEI. Summing `B_i>=b(r)alpha_i` only gives

\[
\sum_iB_i\ge b(r)I,
\]

while the general entropy inequality `sum_i B_i<=H=rI` leaves a positive gap because `b(r)<r`. Likewise, (11) does not improve the already recovered marginal cap `alpha_i<=tau(r)` into a contradiction: at the scalar level the same `tau` is precisely the extremal fibre parameter.

So the following shortcut is **REFUTED AS A CLOSURE STEP**: “the sharper one-coordinate erasure coefficient alone proves FEI.” It does not.

The old arbitrary-prescribed-coordinate upper-payment proposal remains refuted and is not revived here. A structured endpoint or a finite search is not full closure.

## 7. Next attack

The theorem points to a sharper stability target than raw pivotal-set isoperimetry.

The exact endpoint says that near equality must look, in the size-biased fibre law, like `q_i(T)` concentrated near `tau(r)`, with the remaining outside-fibre mass pushed toward `q=0`. Simultaneous equality across coordinates becomes the hard-core down-set law (14). The next B14 attack should therefore prove a **quantitative stability / Booleanity rebate** of one of these two forms:

- either scalar slack in (10) controls distance from the `{0,tau}` conditional-posterior pattern, and the accumulated slack pays the FEI defect; or
- a Boolean Fourier law whose every coordinate is close to that hard-core conditional structure must either be close to the full-product endpoint (already rigid) or have a proper-block selector `B_A<=K I_A` with dimension-free `K`.

This directly connects the mass-weighted erasure route to the newest block-selector and product-phase work without replacing either by a weaker finite statement.

## 8. Literature scope

A bounded current primary-literature search was made before any priority statement. González--MacManus--Pereyra, arXiv:2606.00246 (2026), use the restriction entropy decrement / stopping-tree route and state that a suitable coordinate inequality would imply full FEI. Potapov, arXiv:2609.21563 (18 September 2026), proves FEI only for plateaued and partially bent classes. Han, arXiv:2312.08271, gives the known influence-plus-log-profile upper bound. I did not locate this exact scalar convex-frontier / hard-core endpoint statement in that bounded search, but a search miss is not evidence of novelty. **Publication priority: UNVERIFIED. Full FEI: OPEN.**
