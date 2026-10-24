# B18 FEI proof integration — sharp projection-density floor and spendable phase credit

**Status:** **PARTIAL / PROVED universal information-theoretic implication. Full unrestricted FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context was available in this run.  
**Role:** account03/B18, FEI proof integration.  
**Publication priority:** UNVERIFIED; no novelty claim.

## 0. Exact target and fresh inputs

This run attacks the explicit open interface left by the newest compatible B18 work:

> Global total correlation `T` is not itself spendable at a fixed physical descent scale `q`; only
> `K_q=T-(n/q)\bar T_q` may be subtracted from recombination. Convert a certified global dependence/phase bank into a **scale-specific `K_q` payment without double counting projected total correlation**.

The source-exact inputs used are:

1. `account02/B18/20260921T153436Z-kl-projection-han-packet-integration/REPORT.md`, Git blob `6578efff5ab37f00bede1ee135468cefe20a697e`, which proves
   \[
   K_q=T-{n\over q}\bar T_q
   =(n-q)\left(\operatorname{avg}_{r\ge q}m_r-\operatorname{avg}_{r<q}m_r\right),
   \]
   with `m_0=0`, `m_r` nondecreasing, and `T=\sum_{r=0}^{n-1}m_r`, and also the exact restriction toll
   \[
   \Gamma_q={\mathcal R_q-K_q\over I}.
   \]
2. `account02/B18/20260921T160323Z-joint-phase-packing/REPORT.md`, Git blob `f057794796a6780f46099de3b312126fb1520437`, which proves `T>=t/ln 2`, `t>=Theta(A)`, and the scalar-hard-core two-bank inequality.
3. `account04/B18/20260921T154013Z-scalar-frontier-stability/PHASE_DEFECT_EXACT.md`, Git blob `27f7ef1b604e2a93ef3ecf6d3e57290745a5ed38`, which supplies the exact scalar tangent/phase slack constants used by that two-bank inequality.

The fresh scientific master seen immediately before this derivation was `a38e0151f3e453895c19f752085c255230364412`; newer concurrent B13/B15/B17 work was checked for compatibility. In particular, the fresh B15 magnitude-gradient theorem is an orthogonal positive-recombination/degree constraint and does not alter the KL accounting below.

The route is APPROACHES 6/13 with FLEET_RULES moves: **count the same dependence bank at two scales**, **prove the sharp scalar sequence inequality first**, and **stress the strongest tempting upgrade on an exact extremal law**.

---

## 1. Setup: total-correlation slopes and the exact spendable credit

Let `X=(X_1,...,X_n)` have any probability law on `{0,1}^n`; Booleanity is not needed in Sections 1–2. Let

\[
T=D_{\mathrm{KL},2}(\mu\|\textstyle\prod_i\mu_i)
\]

be total correlation in bits. For a uniformly random `q`-subset `B`, let `\bar T_q` be the average total correlation of `X_B`, and define

\[
K_q:=T-{n\over q}\bar T_q,
\qquad 1\le q\le n-1.
\tag{1.1}
\]

The inherited slope representation is

\[
m_r:=\mathbb E_{i,B:\,|B|=r,\ i\notin B} I(X_i;X_B),
\qquad 0\le r\le n-1,
\tag{1.2}
\]

with

\[
0=m_0\le m_1\le\cdots\le m_{n-1},
\qquad
T=\sum_{r=0}^{n-1}m_r.
\tag{1.3}
\]

Writing

\[
E_q={1\over q}\sum_{r=0}^{q-1}m_r,
\qquad
L_q={1\over n-q}\sum_{r=q}^{n-1}m_r,
\]

the inherited identity is

\[
K_q=(n-q)(L_q-E_q).
\tag{1.4}
\]

The missing issue was that `T` and `K_q` had no quantitative lower comparison, so a global phase/KL certificate could not safely enter `UNPAID_q=\mathcal R_q-K_q`.

---

## 2. PROVED: sharp universal projection-density floor

### Theorem B18-KL-DENSITY-FLOOR

For every probability law on `{0,1}^n`, `n>=2`, and every `1<=q<=n-1`,

\[
\boxed{
K_q\ge a_{n,q}T,
\qquad
a_{n,q}:={n-q\over q(n-1)}.
}
\tag{2.1}
\]

Equivalently,

\[
\boxed{
{n\over q}\bar T_q
\le
\left(1-{n-q\over q(n-1)}\right)T.
}
\tag{2.2}
\]

The coefficient is sharp among all probability laws.

### Proof

Because the slope sequence is nondecreasing and `m_0=0`,

\[
E_q
={1\over q}\sum_{r=1}^{q-1}m_r
\le {q-1\over q}m_{q-1}
\le {q-1\over q}L_q.
\tag{2.3}
\]

Hence

\[
L_q-E_q\ge {L_q\over q}.
\tag{2.4}
\]

Also

\[
T=qE_q+(n-q)L_q
\le(q-1)L_q+(n-q)L_q
=(n-1)L_q,
\tag{2.5}
\]

so

\[
L_q\ge {T\over n-1}.
\tag{2.6}
\]

Insert (2.4)–(2.6) into (1.4):

\[
K_q
=(n-q)(L_q-E_q)
\ge {n-q\over q}L_q
\ge {n-q\over q(n-1)}T.
\]

This proves (2.1). ∎

### Sharpness and decisive refutation of a stronger general-law factor

Let `X_1=...=X_n=Z` for one unbiased Bernoulli bit `Z`. Then

\[
T=n-1,
\qquad
m_0=0,
\qquad
m_r=1\quad(1\le r\le n-1).
\]

For every `q`,

\[
K_q={n-q\over q}
={n-q\over q(n-1)}T.
\tag{2.7}
\]

Thus (2.1) is exact. In particular, the tempting stronger claim that a fixed positive fraction of `T` survives as `K_q` **uniformly for all q** is REFUTED for general laws: at `q=n-1`, the sharp fraction is `1/(n-1)^2`.

This does not refute a stronger **Boolean-spectral** inequality; it identifies exactly where additional Boolean structure would have to enter.

---

## 3. PROVED: global phase/KL certificates now become legal fixed-q credits

For a Boolean spectral law, let `t` and `A=(A_i)` be the inherited matched-product Hellinger/phase quantities from the joint phase-packing theorem. That theorem gives

\[
T\ge {t\over\ln2},
\qquad
t\ge\Theta(A),
\tag{3.1}
\]

where `Theta(A)` is the unique nonnegative solution of

\[
\sum_i(A_i-s)_+^2=4s.
\tag{3.2}
\]

Combining (2.1) and (3.1) gives the exact safe scale conversion

\[
\boxed{
K_q
\ge
{n-q\over q(n-1)\ln2}\,t
\ge
{n-q\over q(n-1)\ln2}\,\Theta(A).
}
\tag{3.3}
\]

This is the missing legal interface: it spends only a guaranteed portion of the actual `K_q`, never the reserved projected correlation `(n/q)\bar T_q`.

If `m` coordinates satisfy `A_i>=a`, the inherited equal-tranche formula

\[
\Theta(A)\ge {\bigl(\sqrt{1+ma}-1\bigr)^2\over m}
\]

gives

\[
\boxed{
K_q\ge
{n-q\over q(n-1)\ln2}
{\bigl(\sqrt{1+ma}-1\bigr)^2\over m}.
}
\tag{3.4}
\]

No phase/KL bank is counted twice in (3.3)–(3.4).

---

## 4. PROVED: direct insertion into the exact FEI descent toll

For a physical-restriction maximal Boolean core, the inherited B18 restriction identity is

\[
\Gamma_q={\mathcal R_q-K_q\over I},
\tag{4.1}
\]

where `\mathcal R_q` is the correctly rescaled average recombination cost. Therefore Theorem 2.1 yields

\[
\boxed{
\Gamma_q
\le
{\mathcal R_q\over I}
-{n-q\over q(n-1)}{T\over I}.
}
\tag{4.2}
\]

Using phase packing,

\[
\boxed{
\Gamma_q
\le
{\mathcal R_q\over I}
-{n-q\over q(n-1)\ln2}{\Theta(A)\over I}.
}
\tag{4.3}
\]

Equivalently, restriction maximality (`\Gamma_q>=0`) forces the new universal structural lower bound

\[
\boxed{
\mathcal R_q
\ge K_q
\ge {n-q\over q(n-1)}T.
}
\tag{4.4}
\]

So any high-dependence hard core must regenerate at least this much recombination at every fixed scale. The global dependence bank is no longer disconnected from `UNPAID_q`; what remains is to compare the **positive** recombination term to this guaranteed contraction.

---

## 5. PROVED: scalar-slack versus scale-specific KL credit

Now use the scalar hard-core setting of the exact phase-defect theorem. Put

\[
s:=B-bI,
\qquad
P_i:=p_i\delta_i,
\qquad
C_r:=2\left(K_r+{1\over d_r}\right),
\tag{5.1}
\]

where the inherited two-bank theorem is

\[
\sum_i(P_i-2\sqrt t)_+^2\le C_rs.
\tag{5.2}
\]

From (2.1) and `T>=t/ln2`,

\[
t\le \Lambda_{n,q}K_q,
\qquad
\Lambda_{n,q}:={q(n-1)\ln2\over n-q}.
\tag{5.3}
\]

Since increasing the threshold can only decrease a positive part, (5.2) gives the direct scale-specific form

\[
\boxed{
\sum_i\left(P_i-2\sqrt{\Lambda_{n,q}K_q}\right)_+^2
\le C_rs.
}
\tag{5.4}
\]

Thus the phase discrepancy is now paid by **the actually spendable q-scale KL credit** or by scalar tangent slack, with no appeal to the full `T` as an independent debit.

### Equal-tranche consequence

If a set `J` of `m` coordinates satisfies `P_i>=d>0`, then (5.4) implies

\[
\boxed{
K_q\ge
{n-q\over4q(n-1)\ln2}
\left(d-\sqrt{C_rs/m}\right)_+^2.
}
\tag{5.5}
\]

Proof: from (5.4),

\[
m\left(d-2\sqrt{\Lambda_{n,q}K_q}\right)_+^2\le C_rs,
\]

and solve for `K_q`; if the positive part has already vanished, the resulting lower bound is even stronger. ∎

This is an explicit three-way hard-core constraint: many discrepant coordinates force either scalar slack `s`, spendable projection KL `K_q`, or both.

---

## 6. Numerical calibration on the inherited n=20 stress profile

The joint phase-packing report used the symmetric marginal stress profile

\[
n=20,\qquad p_i=0.01,
\]

and certified from its phase surrogate

\[
T\ge0.0579604858411688\ldots\text{ bits}.
\]

Theorem 2.1 converts that same already-certified global payment into the following legal fixed-scale credits:

| q | sharp general-law fraction `a_{20,q}` | certified `K_q` floor (bits) |
|---:|---:|---:|
| 1 | 1 | 0.0579604858411688 |
| 2 | 0.4736842105263158 | 0.0274549669773957 |
| 3 | 0.2982456140350877 | 0.0172864606894714 |
| 5 | 0.1578947368421053 | 0.00915165565913192 |
| 10 | 0.0526315789473684 | 0.00305055188637731 |
| 19 | 0.00277008310249308 | 0.000160555362440911 |

The q=2 point is particularly concrete: **at least 47.3684% of total correlation is spendable as the two-coordinate Han/KL contraction for every law**, not merely for this profile.

These numbers do not close FEI; the inherited positive recombination term is still too weakly controlled in the diffuse rare-coordinate regime.

---

## 7. Verification and dead-route ledger

The accompanying standard-library checker performs two independent sanity layers:

1. random probability laws on `{0,1}^n` for `2<=n<=6`, recomputing `T`, every `\bar T_q`, `K_q`, and the floor directly from subset marginals;
2. the exact common-bit family, which attains equality for every `n,q` and therefore stress-tests the claimed sharp coefficient.

The analytic proof in Section 2 is the theorem; finite/random checks are implementation evidence only.

### PROVED in this run

- `K_q >= [(n-q)/(q(n-1))] T` for every finite binary law.
- The coefficient is sharp for general laws, attained by a common latent bit.
- Global phase/Hellinger payment therefore yields the legal fixed-q credit (3.3), and the exact FEI descent toll improves to (4.2)–(4.3).
- In the scalar hard-core regime the previous Hellinger/slack theorem upgrades to the direct `K_q`/slack inequality (5.4) and equal-tranche bound (5.5).

### REFUTED / dead route

- A q-independent positive fraction `K_q>=cT` for all projection dimensions is false for general laws; the common-bit law forces the fraction down to `1/(n-1)^2` at `q=n-1`.
- Therefore the next proof cannot simply claim that “most total correlation is always lost under every projection.” One must either choose the descent scale strategically or use specifically Boolean-spectral structure to beat the sharp general-law floor.

### OPEN

- Full unrestricted FEI.
- A stronger Boolean-spectral lower bound on `K_q/T` than (2.1), if one exists.
- A matching upper control on `\mathcal R_q` in terms of the same dependence/phase quantities sufficient to make `\mathcal R_q-K_q` summably small.
- Closing the diffuse phase-balanced rare-coordinate regime.

## 8. Next attack

The next B18 integration should **not** rederive global total correlation or another one-coordinate phase bound. The new bottleneck is now explicit:

> At a strategically chosen small q (especially q=2 or q=3, where (2.1) retains a constant fraction of `T`), prove that the recombination cost `\mathcal R_q` is bounded by the same phase/magnitude-gradient resource plus a strictly smaller residual. Equivalently, seek a Boolean-specific improvement to the general-law slope floor by exploiting the signed xor/curl constraints.

The fresh B15 magnitude-gradient inequality is a promising positive-side input because it charges one-sided Fourier magnitude tails to higher spectral degree. A useful next synthesis is to express the q=2 recombination remainder through those degree-gradient terms and compare it directly against the guaranteed `K_2 >= (n-2)T/[2(n-1)]` credit.

**Full FEI remains OPEN / NOT PROVED.**
