Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum; authenticated runtime reasoning-effort telemetry and a binding model/effort selector are not exposed.

# C0130 — a spatial-periodic transfer-resolvent theorem beyond the i.i.d. branch

Target: `C0130`, Elena Kosygina and Martin P. W. Zerner, *Excited random walks: results, methods, open problems*, Problem 3.12.

This note continues the all-finite-depth i.i.d. signed-resolvent theorem from

`research7_2026-09-17/R7-05/artifacts/2026-09-18/2026-09-18T140250Z__C0130_all_finite_depth_signed_resolvent_theorem.md`.

That theorem saturates the frozen metric `M_closed` over the `(IID)+(BD)+(WEL)` branch. The remaining source scope is the separate `(SE)+(POS_1)` branch. Here I do not claim to solve that branch. I prove an exact transfer-semigroup and finite-defect reduction for a genuinely non-i.i.d. source-valid subclass: finite-depth positive cookie environments periodic in the **spatial coordinate** and randomized over their spatial phase. This is not the different model usually called “periodic cookies”, where the cookie stack is periodic in visit number and identical at each site.

Methods in this research step: **B3 / B19 / B30**.

## 1. The source-valid spatial-periodic subclass

Fix an integer spatial period `L>=1`. For each phase `a in Z/LZ`, fix a finite-depth stack

\[
\omega_a=(p_{a,1},\ldots,p_{a,M_a},1/2,1/2,\ldots),
\qquad p_{a,i}\in[1/2,1].
\]

Set

\[
\alpha_{a,i}=2p_{a,i}-1\in[0,1],
\qquad
\delta_a=\sum_{i=1}^{M_a}\alpha_{a,i},
\qquad
\bar\delta=\frac1L\sum_{a=0}^{L-1}\delta_a.
\]

Choose a phase `Theta` uniformly from `Z/LZ`, and put the stack at spatial site `x` equal to `omega_{Theta+x}`. The law of the environment is stationary under spatial shift. It is also ergodic: spatial shift acts transitively on the finite orbit of the `L` phases, so a shift-invariant subset of that orbit is empty or the entire orbit. Since all cookies are nonnegative, this is a subclass of `(SE)+(POS_1)`.

Assume

\[
\boxed{\bar\delta>1.}\tag{1.1}
\]

The source theorem then places this positive stationary-ergodic environment in the right-transient regime (apart from the source's separately excluded degenerate environment).

## 2. Forward branching representation phase by phase

At a site of phase `a`, let `S_{a,k}` be the number of successes before the `k`-th failure in the independent coin-toss sequence with probabilities `p_{a,1},p_{a,2},...`, with `S_{a,0}=0`. Let

\[
P_a(k,j)=\Pr(S_{a,k}=j).
\]

The standard coin-toss construction gives the forward branching recursion along positive spatial sites:

\[
U_{n+1}=S_{a+n,U_n}
\]

when the current positive site has phase `a+n`. In particular, if the origin has phase `theta`, then after the first right step the positive half-line starts at phase `theta+1`, and

\[
P_{0,\theta}(X_n\ne0\ \forall n\ge1)
=p_{\theta,1}\,s(\theta+1,1),
\tag{2.1}
\]

where

\[
s(a,k)=\Pr_{(a,k)}(U_n>0\ \forall n\ge0).
\tag{2.2}
\]

For completeness, (2.1) can be obtained by first stopping at `{0,N}`. Under the coin-toss construction, starting from `1`, the event of reaching `N` before `0` is equivalent to the recursively defined forward counts remaining positive through the first `N-1` positive sites. Letting `N->infinity` in the right-transient regime gives (2.1). Thus the phase-averaged escape probability is

\[
\boxed{
 p_{\rm esc}
 =\frac1L\sum_{\theta=0}^{L-1}p_{\theta,1}s(\theta+1,1).
}
\tag{2.3}
\]

The problem is therefore to compute a finite set of phase-dependent survival values.

## 3. B3 — strengthen the i.i.d. algebra to a finite spatial orbit

Put

\[
T(z)=\frac1{2-z}
\]

and, for every phase,

\[
\boxed{
B_a(z)=\prod_{i=1}^{M_a}\big((1-\alpha_{a,i})+\alpha_{a,i}z\big).
}
\tag{3.1}
\]

Because `alpha_{a,i} in [0,1]`, every `B_a` is an honest probability generating function. As in the i.i.d. theorem, for every `k>=M_a`,

\[
\boxed{
\sum_{j\ge0}P_a(k,j)z^j=T(z)^kB_a(z).
}
\tag{3.2}
\]

Define the auxiliary phase kernel for every `k>=0` by

\[
\widetilde Q_a(k;z)=T(z)^kB_a(z).
\tag{3.3}
\]

Lift phase into the state. On

\[
\mathcal E=(\mathbb Z/L\mathbb Z)\times\mathbb Z_{\ge0}
\]

define

\[
\mathsf Q((a,k),(a+1,j))=[z^j]\widetilde Q_a(k;z),
\tag{3.4}
\]

and define the true lifted kernel analogously with `P_a(k,j)`. Phase indices are always modulo `L`.

### Lemma 3.1 — finite lifted defect

Let

\[
\mathcal B=\{(a,k):1\le k<M_a\}.
\tag{3.5}
\]

Then `R=Q-K` has nonzero rows only in the finite set `B`. More sharply, the row belonging to `(a,k)` can have a nonzero discrepancy only in columns `(a+1,j)` with

\[
0\le j\le M_a-k.
\tag{3.6}
\]

#### Proof

For each fixed phase `a`, repeat the one-cookie recursion from the all-finite-depth theorem. If `r` is the current cookie and `N=M_a-r+1`, the difference between the true pgf and the algebraic tail pgf vanishes for `k>=N` and is a polynomial of degree at most `N-k` for `k<N`. At `r=1`, this says exactly that the true and auxiliary phase-a rows agree for `k>=M_a`, while their difference for `k<M_a` is a polynomial of degree at most `M_a-k`. Lifting merely attaches the deterministic next phase `a+1`; it does not change row or column support. QED.

This is the first key point: spatial non-i.i.d. structure does **not** destroy finite-rank localization if phase is carried as part of the state.

## 4. B19 — exact transfer-semigroup algorithm

For `n>=0`, start the auxiliary chain from `(a,k)`. Its terminal phase after `n` steps is deterministically `a+n`. Define

\[
F_{a,k}^{(n)}(z)
=\sum_{j\ge0}\mathsf Q^n((a,k),(a+n,j))z^j.
\]

### Theorem 4.1 — exact n-step transfer formula

For every `a,k,n`,

\[
\boxed{
F_{a,k}^{(n)}(z)
=T^n(z)^k
\prod_{m=0}^{n-1}
B_{a+m}\!\left(T^{n-1-m}(z)\right).
}
\tag{4.1}
\]

#### Proof

The statement is trivial at `n=0`. Assume it for `n`. One more step uses phase `a+n`. Conditional on the current population `J`, the next generating function is `T(z)^J B_{a+n}(z)`. Hence

\[
F_{a,k}^{(n+1)}(z)
=B_{a+n}(z)F_{a,k}^{(n)}(T(z)).
\]

Substituting the induction hypothesis gives

\[
B_{a+n}(z)T^{n+1}(z)^k
\prod_{m=0}^{n-1}B_{a+m}(T^{n-m}(z)),
\]

which is exactly (4.1) with `n+1`. QED.

Now conjugate the parabolic Möbius map to translation:

\[
u=\frac1{1-z},
\qquad
T^n(z)=1-\frac1{u+n}.
\tag{4.2}
\]

Write

\[
\Pi_{a,n}(u)
=\prod_{m=0}^{n-1}
B_{a+m}\!\left(1-\frac1{u+n-1-m}\right).
\tag{4.3}
\]

For each phase let

\[
\mathcal C_a(v)=v^{M_a}B_a\!\left(1-\frac1v\right)
=\prod_{r=1}^{M_a}(v-\rho_{a,r}).
\tag{4.4}
\]

The same coefficient comparison as in the i.i.d. theorem gives

\[
\boxed{\sum_{r=1}^{M_a}\rho_{a,r}=\delta_a.}
\tag{4.5}
\]

For a complete spatial period, `n=qL`, reverse the product index and group the denominators by their residue modulo `L`. If

\[
b_h=a-1-h\pmod L,
\]

then

\[
\boxed{
\Pi_{a,qL}(u)
=
\prod_{h=0}^{L-1}
\prod_{r=1}^{M_{b_h}}
\frac{
\left((u+h-\rho_{b_h,r})/L\right)_q
}{
\left((u+h)/L\right)_q
}.
}
\tag{4.6}
\]

Indeed the factors with reverse index `j=h+Lt` have phase `b_h`, and

\[
B_{b_h}\!\left(1-\frac1{u+h+Lt}\right)
=
\prod_r
\frac{u+h+Lt-\rho_{b_h,r}}{u+h+Lt}.
\]

Multiplication over `t=0,...,q-1` is exactly (4.6).

Using the gamma-ratio asymptotic in every factor of (4.6),

\[
\Pi_{a,qL}(u)
=O(q^{-\bar\delta}),
\tag{4.7}
\]

uniformly for `u` in a compact neighborhood of `1`. More strongly, for every fixed derivative order `r`,

\[
\boxed{
\partial_u^r\Pi_{a,qL}(u)=O_r(q^{-\bar\delta}).
}
\tag{4.8}
\]

The reason no logarithmic loss appears is phasewise balance: every numerator Pochhammer has one denominator Pochhammer with the same `u/L` derivative coefficient, so the leading `log q` terms cancel. If `n=qL+s`, `0<=s<L`, only a fixed number of extra factors is present, and the same estimate holds with a constant depending on `s`.

Consequently, under `bar(delta)>1`, every fixed low-population Green entry of the auxiliary lifted chain is absolutely summable:

\[
\boxed{
G(x,y)=\sum_{n\ge0}\mathsf Q^n(x,y)<\infty
\quad\text{whenever the population coordinate of }y\text{ is fixed.}
}
\tag{4.9}
\]

Moreover every such entry is explicit: split the sum into the `L` residue classes of `n`, use (4.6), and take only finitely many derivatives at `u=1` to extract the desired coefficient of `z`. Each residue-class series is generalized hypergeometric (its successive-term ratio is rational in `q`). Thus the spatial-periodic auxiliary low-state Green block is a finite family of convergent special-function values and derivatives, not an infinite-dimensional numerical solve.

## 5. B30 — the new gluing obstruction is a finite zero-class matrix

The homogeneous i.i.d. auxiliary process had one algebraic zero state. The lifted spatial-periodic chain has the finite zero set

\[
\mathcal Z=\{(a,0):a\in\mathbb Z/L\mathbb Z\}.
\tag{5.1}
\]

This is the only genuinely new gluing feature introduced by spatial phase.

Let `G_ZZ` be the `L x L` Green block on `Z`, and let `G_{xZ}` be the row vector of Green entries from `x` to the zero set. Since all low-state Green entries are finite by (4.9), standard first-entrance decomposition on the finite set `Z` gives

\[
G_{xZ}=H_{xZ}G_{ZZ},
\tag{5.2}
\]

where `H_{xZ}` is the vector of first-entrance probabilities into `Z` for the auxiliary Markov chain. The embedded return kernel on `Z` has spectral radius below one because the total expected number of visits to every zero state is finite, so

\[
G_{ZZ}=(I-F_Z)^{-1}
\]

and is invertible.

Therefore the auxiliary probability of ever entering `Z` is

\[
\boxed{
h(x)=G_{xZ}G_{ZZ}^{-1}\mathbf 1,
\qquad
s^*(x)=1-h(x).
}
\tag{5.3}
\]

For a positive boundary state `b in B`, define the Green function killed on first entrance to `Z` by the Schur complement

\[
\boxed{
U(x,b)=G(x,b)-G_{xZ}G_{ZZ}^{-1}G_{Zb}.
}
\tag{5.4}
\]

Then `U(z,b)=0` for `z in Z`, and on positive states

\[
(I-\mathsf Q)U_{\cdot b}=e_b.
\tag{5.5}
\]

Thus all infinite-dimensional auxiliary information needed by the ERW is contained in the finite blocks `G_ZZ`, `G_ZB`, and `G_BB`, each explicitly given by the residue-class hypergeometric series of Section 4.

For the true chain, let `R=Q-K` and let `R_B` be its finite boundary matrix from Lemma 3.1. If `x=s|_B` is the true boundary survival vector, then the same resolvent identity as in the i.i.d. case gives

\[
\boxed{
s=s^*-UR_Bx,}
\tag{5.6}
\]

and hence the finite boundary system

\[
\boxed{
(I+U_BR_B)x=s^*_B.
}
\tag{5.7}
\]

Equation (5.7) is the exact spatial-periodic gluing problem. Under the standard transient forward-branching uniqueness property (bounded survival solution, zero on `Z`, tending to one as population tends to infinity), the matrix in (5.7) is nonsingular by the same optional-stopping argument used in the i.i.d. all-depth theorem, and then

\[
\boxed{
x=(I+U_BR_B)^{-1}s^*_B.}
\tag{5.8}
\]

I deliberately separate the algebra proved here from that last probabilistic uniqueness input. The source's positive stationary-ergodic transience theorem and the standard forward-process representation strongly point to the required uniqueness in this periodic subclass, but this note does not silently promote it to a new full-source theorem without rechecking the exact forward-divergence hypothesis in the non-i.i.d. setting.

Combining (2.3) and (5.8), when that standard uniqueness hypothesis is invoked, gives the completely explicit phase-averaged escape formula

\[
\boxed{
 p_{\rm esc}
 =\frac1L\sum_{\theta=0}^{L-1}
 p_{\theta,1}\,
 e_{(\theta+1,1)}^\mathsf T
 (I+U_BR_B)^{-1}s^*_B.
}
\tag{5.9}
\]

Every entry of the finite matrix in (5.9) is an explicitly convergent residue-class hypergeometric value/derivative determined by the finitely many phase stacks.

## 6. Exact failure of the naive one-period skeleton idea

A tempting shortcut is to sample the chain every `L` sites and hope the one-period true kernel differs from the one-period auxiliary kernel in only finitely many starting rows. That is false.

For two consecutive phases,

\[
K_0K_1-Q_0Q_1
=-R_0Q_1-Q_0R_1+R_0R_1.
\]

Although `R_1` has finite row support, the term `Q_0R_1` does not: from arbitrarily large initial population, `Q_0` has positive probability to enter the low rows on which `R_1` acts. Hence period-skeletonization spreads the defect to infinitely many starting rows. Carrying phase as a state, rather than collapsing a period, is what preserves finite-rank localization. This is the precise B30 gluing obstruction.

## 7. Relation to known literature checked on 2026-09-18

This note does **not** claim that branching-process methods for non-i.i.d. environments are new. Nicholas Travers, *Excited Random Walk in a Markovian Environment* (EJP 23 (2018), article 43; arXiv:1611.01681), explicitly develops forward and backward branching processes for spatial Markovian cookie environments and proves qualitative transience/speed/limit-law results for a large Markovian class. The 2016 Kozma–Orenshtein–Shinkar paper titled *Excited random walk with periodic cookies* concerns periodicity in the **visit index** of an identically piled stack, not the spatial-periodic finite orbit treated here.

A bounded search dated 2026-09-18 did not locate an explicit never-return formula for Kosygina–Zerner Problem 3.12 in the spatial-periodic or Markovian literature, nor the finite-rank hypergeometric transfer resolvent above. This is negative evidence only and does not certify novelty.

## 8. What moved and what remains

The frozen metric itself moved earlier in this same cumulative run through the all-finite-depth i.i.d. theorem:

\[
\boxed{M_{\rm closed}:2\to\infty\text{ (all finite i.i.d. depths).}}
\]

This spatial-periodic theorem does not redefine that metric. It advances source scope instead: the same finite-defect mechanism survives a genuinely non-i.i.d. stationary-ergodic finite orbit after phase lifting, and the auxiliary Green kernel remains explicitly computable.

The full source Problem 3.12 is still **PARTIAL**. The remaining hard step is no longer “another finite cookie depth.” It is to pass from a finite spatial orbit to the general `(SE)+(POS_1)` environment, where the phase variable is infinite and the scalar Pochhammer product becomes a random/noncommutative transfer product. The nearest concrete next target is a finite-state uniformly ergodic spatial Markov chain, exactly the qualitative class studied by Travers.

Suggested next nonrepeating methods: **B1 / B12 / B28** — change the transfer product to a finite-dimensional operator cocycle, identify the conserved Perron projection controlling its `n^{-delta}` decay, and first prove the resolvent formula for typical finite-state Markov environments before attempting arbitrary stationary ergodic stacks.