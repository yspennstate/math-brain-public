# B16 FEI — binary Ward stopping and exact selector-energy dissipation

**Date:** 21 September 2026  
**Fleet scope:** `fleet03 / B16`  
**Execution label:** **WITHOUT_VERIFIED_BRAIN**  
**Live role:** FEI signed transport proof; current sprint subrole: martingale/Shapley stopping without a false local charge  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact algebraic lemmas for the signed R32 selector plus a precise remaining universal square-function bridge. No publication-priority claim.

## 0. Entering state and route change

This run began from the live 21 September FEI state, not from an older handoff. The owner entry files `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md` were read in that order. The current correction is retained: the read-once bound `H <= 6.4573 I` is a subclass theorem, Numaro's recovered balanced monotone seed already exceeds the old proposed general constant, and unrestricted FEI is still open.

The signed route entering this run has three compatible exact pieces.

1. R32 keeps the exact signed relation sum
   \[
   H_{\rm nat}(f)-R_d(f)
   =\frac8N\sum_{\substack{A\in C_0\setminus D_d\\f_A=-1}}
   (-1)^{|A|/2}I_{|A|,N},
   \]
   with `0 mod 4` debits, `2 mod 4` negative credits, original Reed--Muller dual-code multiplicity, the R16 moment-refund bank, and the terminal response all retained.
2. The weight-four q-flip basis/Aumann--Shapley representation writes each frustrated relation as an odd parity game on the *actually negative* q-flip syndrome coordinates. If a relation has `q` such coordinates and signed coefficient `c`, ordinary fine Shapley assigns `c/q` to each one. The previous proposed **basiswise pointwise** `L_v=O(n)` bound is refuted by an exponential singleton-syndrome family, so this run does not revive it.
3. The newer block-coupled selector is exact for every signed parity monomial: at a partition of the q-flip players into blocks, if `q_odd` blocks have odd relation occupancy, each such block receives `c/q_odd` and every even-occupancy block receives zero. Signs are untouched. Dummy refinements are exactly invariant under this coupled selector, while ordinary fine-player Shapley can move mass between clone orbits through third-and-higher curvature.

The natural question is therefore not whether a single q-flip can always have a small local charge. It cannot. The question attacked here is:

> **Can one refine a coarse signed selector to the fine q-flip selector through an exact stopping process whose redistribution has dimension-free quadratic variation, even though absolute turnover can grow with dimension?**

The answer is **yes, relation by relation**. This is a genuinely different route from a pointwise local-charge bound. The remaining obstacle is an aggregate cross-relation square-function inequality; that part is still open.

Dependencies used explicitly:

- fleet03/B16 signed T-join/R32 disintegration: `fleet-2026-09-21/fleet03/B16/20260921T095730Z-signed-tjoin-transport/REPORT.md`;
- fleet02/B16 q-flip syndrome/Aumann--Shapley transport: `fleet-2026-09-21/fleet02/B16/20260921T103156Z-qflip-syndrome-transport/REPORT.md`;
- fleet02/B16 singleton obstruction/orbit averaging: `fleet-2026-09-21/fleet02/B16/20260921T115841Z-orbit-averaged-qflip-cancellation/REPORT.md`;
- fleet03/B16 dummy Ward identity: `fleet-2026-09-21/fleet03/B16/20260921T115308Z-shapley-dummy-ward/REPORT.md`;
- fleet04/B16 coupled q-flip selector: `continuations/2026-09-21-three-hour-sprint/fleet04/B16/20260921T121543Z-coupled-qflip-selector/REPORT.md`.

No FEI certificate audit or settled exhaustive sweep was repeated.

---

## 1. Binary refinement of one signed frustrated relation

Fix one signed parity monomial from the exact R32 polynomial after choosing a valid q-flip basis. Write

\[
Q_R(S)=c\,\frac{1-(-1)^{|S\cap R|}}2,
\tag{1.1}
\]

where `R` is the set of negative q-flip coordinates occurring in this relation. Since the relation is frustrated, `m:=|R|` is odd and positive. The coefficient `c` is allowed to have either sign; in R32 its sign includes the `(-1)^{|A|/2}` factor, so negative entropy credits remain negative.

Choose **any nested binary hierarchy of blocks**

\[
\mathcal P_0\prec\mathcal P_1\prec\cdots\prec\mathcal P_L,
\tag{1.2}
\]

with one root block at level zero and singleton q-flip blocks at the final level. Every refinement step splits some blocks into two children. The hierarchy may be chosen from the actual ordered-min q-flip coordinates, so this introduces no synthetic replacement of the original coordinate geometry.

For level `ell`, let

\[
q_\ell=\#\{B\in\mathcal P_\ell: |B\cap R|\equiv1\pmod2\}.
\tag{1.3}
\]

The inherited exact block-parity selector gives the block charge

\[
\Phi_\ell(B)=
\begin{cases}
 c/q_\ell,&|B\cap R|\text{ odd},\\
 0,&|B\cap R|\text{ even}.
\end{cases}
\tag{1.4}
\]

At the root `q_0=1`; at the singleton level `q_L=m`, and (1.4) becomes the ordinary fine Shapley allocation `c/m` on every q-flip of `R`.

### Theorem 1.1 — `P03-B16-ODD-BLOCK-BIRTH-LAW` — **PROVED**

If `b_ell` is the number of even parent blocks at level `ell` that split into two odd children, then

\[
\boxed{q_{\ell+1}=q_\ell+2b_\ell.}
\tag{1.5}
\]

In particular every `q_ell` is positive and odd and the sequence is nondecreasing.

#### Proof

An odd parent has total odd occupancy. Under a binary split, exactly one child is odd and one is even, so it contributes one odd block both before and after refinement. An even parent has either two even children or two odd children. Only the latter case changes the count, and it adds two. Summing over parents gives (1.5). `square`

This elementary parity law is the stopping variable for the rest of the run.

---

## 2. Exact Ward selector-energy dissipation

Define the quadratic selector energy at level `ell` by

\[
\mathcal E_\ell(R,c)
:=\sum_{B\in\mathcal P_\ell}\Phi_\ell(B)^2.
\tag{2.1}
\]

### Theorem 2.1 — `P03-B16-WARD-SELECTOR-ENERGY` — **PROVED**

For every signed coefficient `c`,

\[
\boxed{\mathcal E_\ell(R,c)=\frac{c^2}{q_\ell}.}
\tag{2.2}
\]

If `q=q_ell` and `q'=q_{ell+1}=q+2b_ell`, then

\[
\boxed{
\mathcal E_\ell-\mathcal E_{\ell+1}
=c^2\left(\frac1q-\frac1{q'}\right)
=\frac{2b_\ell c^2}{q q'}\ge0.
}
\tag{2.3}
\]

Consequently the full coarse-to-fine refinement has the exact path-independent identity

\[
\boxed{
\sum_{\ell=0}^{L-1}
(\mathcal E_\ell-\mathcal E_{\ell+1})
=c^2\left(1-\frac1m\right),
\qquad
\mathcal E_L=\frac{c^2}{m}.
}
\tag{2.4}
\]

#### Proof

Exactly `q_ell` blocks carry the common signed charge `c/q_ell`; squaring gives (2.2). Equation (2.3) is substitution of (1.5), and (2.4) telescopes from `q_0=1` to `q_L=m`. `square`

### Interpretation

The pointwise singleton obstruction is a **concentration** phenomenon: at the coarsest scale all signed mass `c` can sit in one channel, with energy `c^2`. Fine Shapley spreads the same signed total across `m` participating q-flips and has energy `c^2/m`. The complete redistribution costs exactly the missing energy `c^2(1-1/m)` and no dimension factor.

This statement does **not** take the absolute value of `c` in the linear R32 ledger. A negative `2 mod 4` relation stays negative at every level. The square appears only in the auxiliary redistribution energy, where the goal is to interface with the already existing quadratic/fractional noisy-square bank rather than pay signed mass by total variation.

---

## 3. An orthogonal Ward lift and stopping identity

The scalar energy telescope can be lifted to an exact orthogonal decomposition.

For every odd block `B`, repeatedly descend to its unique odd child. This process ends at a unique singleton `r(B) in R`. Define

\[
S_\ell:=\{r(B): B\in\mathcal P_\ell,\ |B\cap R|\text{ odd}\}.
\tag{3.1}
\]

An old odd block retains its representative in its unique odd child, while an even parent that births two odd children contributes two new representatives. Hence

\[
S_0\subseteq S_1\subseteq\cdots\subseteq S_L=R,
\qquad |S_\ell|=q_\ell.
\tag{3.2}
\]

Define a vector on the **actual participating q-flip leaves**

\[
w_\ell:=\frac{c}{q_\ell}\,1_{S_\ell}\in\mathbb R^R,
\qquad
\delta_\ell:=w_{\ell+1}-w_\ell.
\tag{3.3}
\]

This is an analysis lift of the block charges; it does not replace the physical q-flip-to-disagreement-edge map.

### Theorem 3.1 — `P03-B16-WARD-PYTHAGORAS` — **PROVED**

For `k>=ell`,

\[
\langle w_\ell,w_k\rangle=\frac{c^2}{q_k}=\|w_k\|_2^2.
\tag{3.4}
\]

Therefore the increments are pairwise orthogonal and orthogonal to the terminal fine allocation:

\[
\boxed{
\langle\delta_\ell,\delta_j\rangle=0\ (\ell\ne j),
\qquad
\langle\delta_\ell,w_L\rangle=0.
}
\tag{3.5}
\]

Moreover

\[
\boxed{
\|\delta_\ell\|_2^2
=c^2\left(\frac1{q_\ell}-\frac1{q_{\ell+1}}\right),
\qquad
c^2=\|w_L\|_2^2+\sum_{\ell<L}\|\delta_\ell\|_2^2.
}
\tag{3.6}
\]

Every redistribution increment has zero signed total,

\[
\boxed{\sum_{v\in R}\delta_\ell(v)=0,}
\tag{3.7}
\]

while every `w_ell` has total signed mass `c`.

#### Proof

Nestedness (3.2) gives, for `k>=ell`,

\[
\langle w_\ell,w_k\rangle
=|S_\ell|\frac{c}{q_\ell}\frac{c}{q_k}
=\frac{c^2}{q_k}.
\]

Subtracting this identity at adjacent levels proves both orthogonality statements. The norm formula follows from

\[
\|w_{\ell+1}-w_\ell\|_2^2
=\|w_\ell\|_2^2-\|w_{\ell+1}\|_2^2.
\]

Summation gives (3.6). Finally both `w_ell` and `w_{ell+1}` sum to `c`, proving (3.7). `square`

### Stopping version

At **any** stopping level `tau`, not only at singleton resolution,

\[
\boxed{
 c^2=\frac{c^2}{q_\tau}
 +\sum_{\ell<\tau}\|\delta_\ell\|_2^2.
}
\tag{3.8}
\]

Thus stopping once `q_tau>=K` leaves residual norm at most `|c|/sqrt(K)` while all earlier selector changes are an orthogonal zero-mass transport with total squared norm at most `c^2`.

This is the precise half-order scale sought by the current Shapley route. It matches the *shape* of the inherited fractional noisy-square bank (which carries a square-function/half-order weight), but no identification of the two objects is assumed here.

---

## 4. Why total-variation payment is the wrong continuation

The same exact algebra gives a decisive dead route.

For `q'=q+2b`, the lifted increment has

\[
\frac12\|\delta_\ell\|_1
=|c|\left(1-\frac q{q'}\right)
=\frac{2b|c|}{q'}.
\tag{4.1}
\]

If one pays the refinement by absolute turnover, these costs accumulate. A sequential slow refinement `1,3,5,...,m` gives

\[
\frac1{|c|}\sum_\ell\frac12\|\delta_\ell\|_1
=\sum_{j=0}^{(m-3)/2}\frac2{2j+3}
=2H_m-H_{(m-1)/2}-2
=\log m+O(1).
\tag{4.2}
\]

So an `L1`/positive-turnover proof can lose a logarithm of the participating relation size; with exponentially many q-flip coordinates this is again a dimension loss. This is exactly the sort of loss the signed compiler warns against.

By contrast the quadratic variation is always

\[
c^2(1-1/m)<c^2,
\tag{4.3}
\]

independent of the number of refinement stages.

This run therefore **REFUTES as a viable dimension-free mechanism** the shortcut “pay every Shapley refinement by absolute selector turnover.” It does not refute FEI or any signed square-function payment.

Concrete unit-coefficient values from the checker for the slow refinement are:

| final odd count `m` | one-way `L1` turnover | quadratic variation `1-1/m` |
|---:|---:|---:|
| 3 | 0.6666667 | 0.6666667 |
| 5 | 1.0666667 | 0.8000000 |
| 17 | 2.1612479 | 0.9411765 |
| 65 | 3.4600558 | 0.9846154 |
| 257 | 4.8233249 | 0.9961089 |
| 1025 | 6.2037860 | 0.9990244 |

The contrast is the main quantitative output of this run: absolute turnover keeps growing, whereas the signed Ward redistribution has a bounded orthogonal energy budget.

---

## 5. Pointwise Borel compatibility

The exact Borel R32 corridor writes each relation with a real scale-dependent coefficient

\[
c_A(s)=2N(-1)^{|A|/2}
\sin^{|A|}(s/N)\cos^{N-|A|}(s/N).
\tag{5.1}
\]

Nothing in Theorems 1.1--3.1 assumes positivity or a fixed coefficient. Therefore the same hierarchy gives, **for every Borel time `s` separately**,

\[
\mathcal E_{A,\ell}(s)=\frac{c_A(s)^2}{q_{A,\ell}},
\tag{5.2}
\]

and

\[
\sum_{\ell<L}\|\delta_{A,\ell}(s)\|_2^2
=c_A(s)^2\left(1-\frac1{q_A}\right).
\tag{5.3}
\]

The linear selector mass at every level is still exactly `c_A(s)`, so the sign of the Borel relation, including negative-credit phases, is retained before the final `s^{-3}` integration.

**Important limitation:** (5.3) is quadratic while R32 is a signed linear integral. This run does **not** interchange them and does not claim that the R16 bank automatically pays (5.3). The point is to expose an exact square-function object whose payment would avoid the known `L1` turnover loss.

---

## 6. Exact remaining universal implication

The new relationwise theorem removes one obstruction but not the cross-relation one.

Let `P_ell` denote the signed block-coupled selector applied to the **whole** R32 relation polynomial at refinement level `ell`. By linearity it is the sum of the per-relation block charges above. Passing from `P_ell` to `P_{ell+1}` is exactly a higher-curvature redistribution: fleet04's refinement-defect theorem already shows that first- and second-order terms do not create the ordinary-versus-coupled orbit defect, and all movement is carried by third-and-higher mixed plaquette curvature.

The next theorem needed is therefore a genuine aggregate square-function estimate, schematically

\[
\boxed{
\text{signed aggregate refinement square function}
\ \lesssim\ 
\text{retained R16/noisy-square moment bank},
}
\tag{6.1}
\]

with the exact q-flip hierarchy, physical disagreement-edge map, and Borel/R32 coefficients. The relationwise orthogonality in (3.5) is **not** enough by itself because increments belonging to different relations can have nonzero cross inner products. Taking `sum_A |c_A|` or `sum_A |delta_A|` would destroy the R32 negative credits and is forbidden.

A successful proof of (6.1), together with a stopping rule for the fine residual and the already separate terminal-band payment, would convert the current signed Shapley mechanism into an integrated transport payment without the false basiswise `L_v=O(n)` lemma.

This is **CONDITIONAL / OPEN**. It is the exact point at which this run stops.

---

## 7. Attempted refutation and finite checks

A standard-library checker attacks the identities in two ways.

1. It exhausts **every odd subset** of a dyadic leaf set through height four: `2 + 8 + 128 + 32768 = 32906` odd subsets. For each one it constructs every `q_ell`, the parity-descendant representative sets, all lifted increments, and verifies with exact rational arithmetic:
   - odd/nondecreasing parity counts and the `+2b` birth law;
   - nested representative sets;
   - the exact norm decrement;
   - zero signed mass of every increment;
   - pairwise increment orthogonality;
   - terminal orthogonality;
   - the Pythagorean identity.
2. With deterministic seed `20260921`, it checks another **6000** random odd subsets at heights `5,6,8`. The largest observed one-level odd-count jumps were `20,42,94`, respectively. No identity failed.

The checker returned `PASS`. This is falsification evidence only; the proofs above are the universal argument.

Files in this run:

- `check_ward_energy.py` — exact standard-library checker;
- `check_output.json` — current-run counts and turnover values.

---

## 8. Status ledger

**PROVED in this run**

- `P03-B16-ODD-BLOCK-BIRTH-LAW`: binary refinement changes the number of odd relation blocks by exactly `+2b`.
- `P03-B16-WARD-SELECTOR-ENERGY`: the block-coupled parity selector has exact energy `c^2/q`, with dimension-free telescoping dissipation `c^2(1-1/m)`.
- `P03-B16-WARD-PYTHAGORAS`: the parity-descendant Ward lift has pairwise orthogonal zero-mass refinement increments and terminal residual norm `|c|/sqrt(m)`.
- The same identities hold pointwise for every real Borel coefficient `c_A(s)`.

**REFUTED / dead continuation**

- Paying each refinement by absolute `L1` turnover is not dimension-free in general; the slow refinement accumulates `log m+O(1)`, and balanced/random hierarchies can also accumulate with depth. This route is not used further.
- The previously killed basiswise pointwise q-flip local bound remains killed; nothing here revives it.

**PRESERVED / not spent**

- signed `0 mod 4` debit / `2 mod 4` negative-credit cancellation;
- original-coordinate q-flip/disagreement-edge geometry;
- exact dual-code multiplicity;
- R16 odd-moment/high-resolvent refunds;
- terminal response and its separate terminal-band payment.

**OPEN**

- the aggregate cross-relation square-function estimate (6.1);
- the final stopping-to-physical-edge payment after that estimate;
- unrestricted FEI itself.

**FULL FEI:** **OPEN / NOT PROVED**.

---

## 9. Next attack

Do not spend the next run on another parity-subset checker. The next move is to compute the exact operator taking one binary block refinement of the *whole signed R32 polynomial* to its higher-curvature defect, in Harsanyi/plaquette coordinates, and compare its coefficient square function with the inherited midpoint fractional noisy-square bank. The decisive calculation is whether the fleet04 `1/sqrt(8s)` refinement coefficient and the present exact `c^2(1/q-1/q')` energy decrement are two coordinate descriptions of the same half-order operator after summing the dual-code multiplicities.

If they are, the R16/noisy-square bank becomes a plausible actual payment. If an admissible Boolean phase makes that aggregate square function exceed the available bank by an unbounded factor, this Ward-stopping route is decisively dead and B16 should switch mechanisms rather than repeat it.
