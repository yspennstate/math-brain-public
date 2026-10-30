# B16 — basiswise q-flip local bound is false; random-basis orbit averaging repairs the singleton obstruction

**Run:** 2026-09-21T11:58:41Z, fleet02/B16  
**Live role:** FEI signed transport proof  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full FEI status:** **OPEN / NOT PROVED**.  
**Fresh scientific master used for the final derivation before delivery:** `55612ab3345e44122472d0d5876d6f8b9c64de6a`.  
**Measurable quantity:** the local size of the signed q-flip transport after the averaging actually allowed by the construction. Before this run the live route had only the proposed pointwise target `L_v=O(n)` plus the exact fleet04 averaged-edge target. After this run the pointwise target is **DISPROVED** by an exponential family, while an exact transitive-orbit average is **PROVED** and gives the correct `O(1/N)` edge scale on the canonical dummy-variable obstruction and on every affine-subcube defect.

The three deliberately different `FLEET_RULES` moves used this run are **#2 ATTACK THE NEGATION FIRST** (try to kill the proposed pointwise q-flip derivative estimate), **#14 FIND THE GROUP ACTING** (average the exact signed transport under the stabilizer of `f`), and **#4 PROVE SOMETHING WEAKER, COMPLETELY** (prove the averaged theorem exactly on transitive disagreement-edge orbits instead of claiming a universal local inequality).

This report preserves every sign in R32. No absolute values are introduced, dual-code multiplicity is unchanged, `2 mod 4` relations remain negative entropy credits, and the terminal response remains a separate exact endpoint quantity. Nothing below revives the killed fixed-basis spectral-entropy shortcut.

---

## 1. Entering exact state

Write `V=F_2^n`, `N=2^n`. At a paid complete-degree prefix `d`, the recovered R32 identity in natural entropy units is

\[
F_d(f):=H_{\rm nat}(f)-R_d(f)
 =\frac8N\sum_{\substack{A\in C_0\setminus D_d\\ f_A=-1}}
 c_A,
\qquad
c_A=(-1)^{|A|/2}I_{|A|,N},
\tag{1.1}
\]

where

\[
C_0=RM(1,n)^\perp,
\qquad
I_{w,N}=\int_0^\infty \frac{\sin^w t\cos^{N-w}t}{t^3}\,dt\ge0.
\tag{1.2}
\]

Thus supports of size `0 mod 4` are positive debits and supports of size `2 mod 4` are genuine negative credits. The half-band theorem carried by the compiler gives, for `d_h=ceil(n/2)`,

\[
R_{d_h}(f)=o(J(f))
\tag{1.3}
\]

uniformly over noncharacters. This is a **net signed endpoint theorem**, not a positive-turnover theorem.

The preceding fleet02/B16 run fixed an anchor `a` and, for each displacement `v` with `|v|>=2`, a pivot `i(v) in supp(v)` and proved that

\[
B_v(a)=\{a,a+e_{i(v)},a+v,a+v+e_{i(v)}\}
\tag{1.4}
\]

forms a basis of `C_0`. With syndrome

\[
z_v(f)=f_{B_v(a)},
\tag{1.5}
\]

every frustrated relation has an odd nonempty set of active (`z_v=-1`) basis q-flips, and each active q-flip contains exactly one genuine physical disagreement edge, denoted `epsilon_v(f)`.

For the exact R32 coefficients, its Aumann--Shapley load is

\[
L_v(f)=1_{\{z_v=-1\}}
\sum_{\substack{A\in C_0\setminus D_d\\ f_A=-1\\a_v(A)=1}}
\frac{c_A}{q_A},
\tag{1.6}
\]

with `q_A` the number of active basis coordinates in the unique expansion of `A`. It obeys

\[
F_d(f)=\frac8N\sum_v L_v(f),
\tag{1.7}
\]

and is exactly the integrated signed derivative of the R32 relation polynomial. The previous run proposed the sufficient local lemma

\[
L_v(f)\le K n
\tag{1.8}
\]

because random q-flip bases have expected physical channel incidence `<4/n` at a fixed edge.

Fleet04/B16 then proved the exact Shapley--plaquette bridge. If `g_v` is the phase quotient dual to `B_v`, `C_v^M` is its signed Shapley plaquette bank, and `Theta_v^M` is the Shapley share of `R_d`, then

\[
D_v:=\frac8N L_v
 =H_{\rm nat}(g_v)-\mathcal C_v^M-\Theta_v^M.
\tag{1.9}
\]

Routing `D_v` through `epsilon_v(f)` and then averaging over valid q-flip bases gives the exact residual edge load

\[
\overline D_e=
\mathbb E_{\mathcal B}\sum_{v:\epsilon_v(f)=e}D_v,
\tag{1.10}
\]

whose desired universal target is `overline D_e <= 2K/N`. Fleet04 also showed that paying the raw positive dual-generator entropy separately loses a factor `Theta(n)` per edge; signed plaquette/terminal cancellation is essential.

Fleet01/B16 sharpened the warning: after subtracting only the constant baseline, the random-order raw dual-generator displacement kernel has fixed low Walsh multipliers

\[
A_{n,r}=\frac{4n}{(r+1)(r+2)}+O_r(1),
\tag{1.11}
\]

and the two-variable parity-switch with dummy variables realizes the bad singleton mode. Its handoff asks whether the *combined signed* plaquette + terminal + retained refund ledger cancels that mode.

This run attacks exactly that point.

---

## 2. The proposed pointwise `L_v=O(n)` lemma is false by an exponential factor

Use the ordered-first-pivot q-flip basis from fleet04. Fix an integer `c>=2`, and for every `n>=c` choose a dual basis generator `g_u` whose pivot has rank `r=n-c+1` in the coordinate order. Fleet04 proved that `g_u` is a one-subcube defect of codimension `c`: up to translation and affine gauge,

\[
g_u(x)=1-2\,1_A(x),
\qquad |A|/N=2^{-c},
\tag{2.1}
\]

where `A` is an affine coordinate subcube. It depends on only `c` coordinates and has `n-c` dummy coordinates.

Because `g_u` is **the phase dual to one basis relation**, its q-flip syndrome in that defining basis is exactly singleton:

\[
z_u(g_u)=-1,
\qquad z_v(g_u)=+1\quad(v\ne u).
\tag{2.2}
\]

Therefore `M={u}` and (1.7) has only one summand:

\[
\boxed{
\frac8N L_u(g_u)=F_d(g_u)=H_{\rm nat}(g_u)-R_d(g_u).
}
\tag{2.3}
\]

At the half-band, (1.3) applies because `g_u` is a noncharacter. Its folded influence is a positive constant depending only on `c` (computed in section 4), so `R_{d_h}(g_u)=o(1)` as `n->infinity`. Its entropy is likewise a positive constant depending only on `c`. Hence

\[
\boxed{
L_u(g_u)=\frac N8\bigl(H_{c,\rm nat}+o(1)\bigr)=\Theta_c(N).
}
\tag{2.4}
\]

### Theorem 2.1 — `B16-POINTWISE-QFLIP-BOUND-OBSTRUCTION`

For every fixed `c>=2`, the ordered q-flip basis contains Boolean functions and an active basis coordinate for which the exact signed Aumann--Shapley R32 load is `Theta(2^n)`. Consequently there is no dimension-independent `K` such that

\[
L_v(f)\le Kn
\]

for every Boolean `f`, every valid q-flip basis and every active q-flip coordinate.

The failure is exponential, not a constant-factor miss.

This also kills any attempt to demand `O(1/N)` signed edge payment **basis by basis**: for the singleton-syndrome function the unique active q-flip routes all of (2.3) through one physical disagreement edge in its defining basis.

This is not a counterexample to FEI and not a counterexample to the random-basis route. It says the averaging over bases was not merely a convenient way to count channels: it is mathematically necessary.

---

## 3. Equivariant random q-flip bases

Let `mu` be the following q-flip basis law:

1. choose the anchor `a` uniformly from `V`;
2. choose a uniformly random total order of the `n` physical coordinates;
3. for every `v`, use as pivot the first coordinate of `supp(v)` in that order.

For a fixed `v`, this pivot is uniform on `supp(v)`, so this is a coupled version of the random-pivot law used in the previous `4/n` incidence calculation. More importantly, `mu` is equivariant under translations of `V` and permutations of the original coordinates.

For a sampled basis `mathcal B`, route each active q-flip to its unique disagreement edge and put

\[
\Lambda_e^{\mathcal B}(f)
 :=\sum_{v:\epsilon_v(f)=e}\frac8N L_v(f),
\tag{3.1}
\]

so that, **for every basis separately**, signs included,

\[
\sum_{e\in\mathcal D_f}\Lambda_e^{\mathcal B}(f)=F_d(f).
\tag{3.2}
\]

Use fleet04's terminal Shapley share to define on the same routed q-flips

\[
T_e^{\mathcal B}(f)
 :=\sum_{v:\epsilon_v(f)=e}\Theta_v^M.
\tag{3.3}
\]

Shapley efficiency gives, again for every basis,

\[
\sum_{e\in\mathcal D_f}T_e^{\mathcal B}(f)=R_d(f).
\tag{3.4}
\]

No positivity of either quantity is assumed.

---

## 4. Exact orbit-averaged signed transport theorem

Let `G` be a subgroup of the physical cube isometry group generated by translations and coordinate permutations. Suppose

* `f(gx)=f(x)` for every `g in G` (or, equivalently for the transport quantities, `f` is fixed up to the harmless global/affine gauge already allowed by the compiler); and
* `G` acts transitively on the undirected physical disagreement edges `mathcal D_f`.

A complete-degree Reed--Muller prefix is invariant under these cube isometries. Hence `C_0`, `D_d`, the cardinality-dependent R32 coefficient `c_A`, `F_d`, and therefore `R_d=H_nat-F_d` are invariant. The law `mu` is equivariant as well. Acting by `g` maps every basis relation, active syndrome coordinate, dual phase, Shapley share and routed disagreement edge to the corresponding object for the transformed basis. Thus the expectations of (3.1) and (3.3) are constant on the unique edge orbit.

Summing over that orbit and using (3.2)--(3.4) determines the constants exactly.

### Theorem 4.1 — `B16-ORBIT-AVERAGED-SIGNED-TRANSPORT`

Under the hypotheses above, every disagreement edge `e` satisfies

\[
\boxed{
\mathbb E_{\mathcal B\sim\mu}\Lambda_e^{\mathcal B}(f)
 =\frac{F_d(f)}{|\mathcal D_f|}
 =\frac{H_{\rm nat}(f)-R_d(f)}{|\mathcal D_f|},
}
\tag{4.1}
\]

and

\[
\boxed{
\mathbb E_{\mathcal B\sim\mu}T_e^{\mathcal B}(f)
 =\frac{R_d(f)}{|\mathcal D_f|}.
}
\tag{4.2}
\]

Consequently the combined residual-plus-terminal Shapley ledger is

\[
\boxed{
\mathbb E_{\mathcal B}
\bigl(\Lambda_e^{\mathcal B}+T_e^{\mathcal B}\bigr)
 =\frac{H_{\rm nat}(f)}{|\mathcal D_f|}.
}
\tag{4.3}
\]

The theorem is an equality of signed quantities. It does not positive-part the plaquette bank, the R32 relation weights or the terminal response.

### Why this is a genuine advance over the `4/n` incidence estimate

The earlier incidence theorem counts how many possible q-flip channels geometrically touch one physical edge and yields `<4/n` in expectation. Theorem 4.1 instead averages the **actual exact signed Aumann--Shapley charges** after all high-weight relation multiplicities and cancellations have been assigned. On a transitive orbit the entire integrated transport collapses to a scalar forced by the global signed R32 identity. Thus a huge basiswise charge such as (2.4) is allowed, provided the group average redistributes/cancels it correctly.

---

## 5. Affine-subcube defects: exact `O(1/N)` average and a universal class constant `<4`

Apply Theorem 4.1 to

\[
f_{c,n}=1-2\,1_A,
\qquad q:=|A|/N=2^{-c},
\qquad c\ge2,
\tag{5.1}
\]

where `A` is an affine coordinate subcube of codimension `c`.

### 5.1 Exact Fourier entropy

The squared Fourier spectrum has

\[
p_0=(1-2q)^2
\tag{5.2}
\]

at the empty character and

\[
p_1=4q^2
\tag{5.3}
\]

at each of the `2^c-1` nonzero characters in the annihilator of the free subspace. Therefore in bits

\[
H_c
=-p_0\log_2p_0-(2^c-1)p_1\log_2p_1.
\tag{5.4}
\]

Equivalently, with

\[
\epsilon=1-p_0=4q(1-q),
\tag{5.5}
\]

the nonzero spectral law conditional on being nonempty is uniform, so

\[
\boxed{H_c=h_2(\epsilon)+\epsilon\log_2(2^c-1).}
\tag{5.6}
\]

### 5.2 Exact influence and edge orbit

For each of the `c` fixed coordinates, the function changes on a fraction `2q` of inputs; all other coordinates are dummy. Since `2q<=1/2`, folded and ordinary influence coincide:

\[
\boxed{J(f_{c,n})=I(f_{c,n})=2cq.}
\tag{5.7}
\]

The number of undirected disagreement edges is

\[
\boxed{|\mathcal D_f|=c2^{n-c}=\frac{N J(f)}2.}
\tag{5.8}
\]

Translations along the free coordinates together with permutations of the `c` fixed coordinates act transitively on these disagreement edges, so Theorem 4.1 applies.

### 5.3 A simple analytic entropy bound

Use

\[
h_2(x)\le x\log_2(e/x),\qquad 0<x<1.
\tag{5.9}
\]

Because `epsilon<=4q` and `x log(e/x)` is increasing on `(0,1]`,

\[
h_2(\epsilon)
 \le4q\log_2\frac e{4q}
 =4q(c-2+\log_2 e)
 <4qc.
\tag{5.10}
\]

Also

\[
\epsilon\log_2(2^c-1)<4qc.
\tag{5.11}
\]

Hence

\[
\boxed{H_c<8cq=4J(f_{c,n}).}
\tag{5.12}
\]

Put

\[
K_c:=\frac{H_c}{J(f_{c,n})}<4.
\tag{5.13}
\]

In fact `K_c -> 4` from below as `c->infinity`.

### Corollary 5.1 — exact averaged edge scale

For every disagreement edge of the affine-subcube defect,

\[
\boxed{
\mathbb E_{\mathcal B}\Lambda_e^{\mathcal B}
 =\frac2N\left(K_c\ln2-\frac{R_d(f)}{J(f)}\right).
}
\tag{5.14}
\]

At the half-band,

\[
\boxed{
\mathbb E_{\mathcal B}\Lambda_e^{\mathcal B}
 =\frac{2K_c\ln2+o(1)}N
 <\frac{8\ln2+o(1)}N,
}
\tag{5.15}
\]

while the terminal share is separately

\[
\boxed{
\mathbb E_{\mathcal B}T_e^{\mathcal B}
 =\frac2N\frac{R_{d_h}(f)}{J(f)}
 =o(1/N).
}
\tag{5.16}
\]

This is exactly the normalized local scale demanded by the fleet04 closure target, for an infinite family with arbitrarily many dummy variables.

---

## 6. The fleet01 bad singleton mode is cancelled in the complete signed average

Take `c=2`. Up to translation and affine gauge the subcube defect is the two-variable parity-switch/quadratic phase used as the dummy-variable obstruction by fleet01:

\[
f(x)=(-1)^{x_1x_2},
\tag{6.1}
\]

with `n-2` dummy coordinates. Its exact values are

\[
H_2(f)=2,
\qquad J(f)=1,
\qquad |\mathcal D_f|=N/2.
\tag{6.2}
\]

Therefore Theorem 4.1 gives, without asymptotics for the combined ledger,

\[
\boxed{
\mathbb E_{\mathcal B}
(\Lambda_e^{\mathcal B}+T_e^{\mathcal B})
 =\frac{4\ln2}{N}
}
\tag{6.3}
\]

for every disagreement edge. At the half-band,

\[
\boxed{
\mathbb E_{\mathcal B}\Lambda_e^{\mathcal B}
 =\frac{4\ln2+o(1)}N,
\qquad
\mathbb E_{\mathcal B}T_e^{\mathcal B}=o(1/N).
}
\tag{6.4}
\]

This directly answers the calibration question left by fleet01's low-mode computation. The raw generator-entropy singleton multiplier grows linearly in `n`, but after complete signed basis averaging the true R32 residual is `O(1/N)` per disagreement edge, and the terminal band is too small at the half-band to supply the leading cancellation. Thus the `Theta(n)` singleton growth must be cancelled by the signed plaquette/refund part of the complete ledger rather than paid as a positive error.

This does **not** prove the analogous cancellation for an arbitrary Boolean function; it proves that the most explicit dummy-variable obstruction is a bookkeeping artefact of separating the positive baseline from its signed curvature bank.

---

## 7. Exact self-checks

The companion checker `check_orbit_averaged_qflip_transport.py` does not certify FEI; it checks the finite algebra used above.

It exhaustively averages over **all anchors and all coordinate orders** for the affine-subcube defects

\[
(n,c)=(3,2),(3,3),(4,2),(4,3),(4,4),(5,2).
\]

For every basis it reconstructs the exact dual q-flip phases recursively, identifies active syndromes and their unique routed disagreement edges, computes the entropy set-function on every subset of active duals, evaluates the Shapley marginals directly, and then averages routed loads. In every case all physical disagreement edges receive `H_2/|D|` up to floating roundoff; the largest observed edge spread is `2.22e-16` bits.

It also checks 28 defining-basis singleton-syndrome cases for `2<=n<=8`, and evaluates the exact analytic ratios through `c=32`. Selected values are

\[
\begin{array}{c|rrrrrrr}
c&2&3&4&5&8&16&32\\ \hline
H_c/J&2.000000&2.955890&3.402476&3.623740&3.842783&3.930271&3.965168.
\end{array}
\tag{7.1}
\]

The checker status is `PASS`. These finite tests support the implementation and catch normalization mistakes; the proofs in sections 2--6 are analytic and do not rely on exhaustiveness.

---

## 8. What failed and what remains

### DISPROVED this run

The previous sufficient lemma

\[
L_v=O(n)\quad\text{pointwise in the basis and active q-flip}
\]

is false. Fixed-codimension dual generators give `L_v=Theta(2^n)`. Any route that tries to bound every individual Aumann--Shapley q-flip charge, or every basiswise routed edge load, should be retired.

### PROVED this run

1. Exact signed residual and terminal loads, averaged over the equivariant uniform anchor/order q-flip bases, are forced to be `F_d/|D|` and `R_d/|D|` on every transitive disagreement-edge orbit.
2. Affine-subcube defects have `H_2<4J` and therefore their exact half-band averaged residual edge load is `<(8 ln 2+o(1))/N`.
3. The two-variable parity-switch with arbitrarily many dummy variables has exact joint averaged edge load `4 ln 2/N` and half-band residual `4 ln2/N+o(1/N)`. Thus fleet01's linear singleton-mode growth cancels in the complete signed basis average; the terminal term is asymptotically too small to be that leading cancellation.

### Still OPEN

For a general Boolean function the disagreement edges need not form one stabilizer orbit, and Theorem 4.1 gives no direct comparison between different edge orbits. Full FEI would follow from the fleet04 target

\[
\overline D_e\le\frac{2K}{N}
\tag{8.1}
\]

for every disagreement edge, but no such universal signed inequality is proved here.

The next exact target is therefore sharper than the now-dead pointwise bound:

> Compute the fixed-`r` displacement-Walsh multipliers of the **basis-averaged signed plaquette bank** (with the inherited terminal/R16 refunds kept in their exact places). The `r=1` multiplier is forced by section 6 to cancel the raw `Theta(n)` singleton term on the parity-switch family. Prove the analogous cancellation for every fixed `r`, then use fleet01's exact q-flip Radon/noisy-square `L2` identity to pay the high-frequency remainder.

A failure of that complete signed multiplier cancellation on an explicit Boolean family would decisively retire the random-order q-flip basis route. An absolute-value estimate is not an acceptable substitute.

---

## 9. Fresh literature check and scope

A fresh primary-source search during this run did not reveal a proof of unrestricted uniform-cube FEI. The current 2026 papers found remain class/route evidence rather than closure: Potapov's September 18 paper proves the conjecture for plateaued functions (sharp class constant 4) and partially bent functions (constant 2), while González--MacManus--Pereyra's May 29 paper proves further classes and a stopping-tree reduction. Han's 2025 general estimate includes the additional `sum_i I_i log(1/I_i)` term rather than a dimension-free pure-influence FEI bound. No publication-priority or novelty claim is made for the orbit-averaged formulation above merely because this search found no match.

The repository's 21 September continuation also records a certified read-once bound `6.4573`, with sharp read-once value numerically `6.4547837...`; that is a subclass theorem, not full FEI. The newer September 20 spectral-lattice, centroid/carry, erasure, affine-stopping and restriction results remain part of the live state and are not superseded by this report.

**Final status:** substantial signed-transport progress and one dead local lemma removed; unrestricted FEI remains **OPEN / NOT PROVED**. Work was performed **WITHOUT_VERIFIED_BRAIN**.
