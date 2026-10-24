# account01/B14 — A066 parity-lift audit of Fourier-degree entropy variation

**Date:** 2026-10-11  
**Primary packet:** `A066` — Semigroup dissipation  
**Claim version:** `A066-PARITY-LIFT-SEMI-v1`  
**Gap:** `G-A066-SEMI-VARIATION`  
**Status:** `AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW`  
**Full Fourier Entropy–Influence conjecture:** `OPEN`

## 1. Exact mathematical movement

The prior A066 work defined the normalized Fourier-degree damping law

\[
p_t(S)=\frac{\widehat f(S)^2e^{-2t|S|}}
{\sum_T\widehat f(T)^2e^{-2t|T|}}
\]

and the corrected total downward entropy variation

\[
\mathcal V_-(f)=H(P_\infty)+\int_0^\infty[-H'(P_t)]_+\,dt.
\tag{1.1}
\]

It proved that monotone entropy dissipation is false for genuine Boolean
functions and left the campaign's parity lift as the next exact falsifier.
This run closes that test at its correct scope.

> **PROVED.** The parity lift preserves the complete squared Fourier law,
> rounds every occupied degree upward to an even integer, and increases
> influence by at most a factor two.  Nevertheless, for every `r>=3` there
> is a genuine Boolean parity lift with `H'(P_t)|_{t=0}>0`.  Thus even-only
> Fourier support (equivalently the parity-erasure condition used in X001)
> does not restore semigroup entropy monotonicity.

There are also two positive controls.

> **PROVED.** Parity-lifted ordinary addressing and parity-lifted one-point
> defects have monotone entropy curves, hence `V_-=H`, and each satisfies
> `V_-/I<4` (with the exact addressing ratio `4a/(a+3)`).

The universal inequality `V_-<=C I` remains **OPEN**.  More strongly, its
restriction to the parity-lift/even-support class is already full-FEI-hard
up to a factor two.  This is a boundary theorem, not a solution.

## 2. Sources, versions, and one availability limitation

| Source | Verified version |
|---|---|
| `CURRENT_STATUS.md` | blob `74f6ae761739455083804505ba0e0fd7aaf2f3e2` |
| `STREAM_PACKET_INDEX.json` | blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704` |
| `assignments/B14.json` | blob `c1457da582b357efb51b39eb3bda0cff56437219` |
| `EXECUTION_PROTOCOL.json` | blob `457358ff62cbf1141a72096bcabdf95bf18c1be2` |
| `PACKET_STATUS.json` | blob `66a78ef3249a89d481a47320f990dc2aec002ccb` |
| `CLAIM_REGISTRY.json` | blob `bef50513c8309b0e601aec42470bc09162f26ea8` |
| `OBSTRUCTION_REGISTRY.json` | blob `d9c8b8632d019aa9e4d5c7394001d116fd21d94e` |
| supplement `COUNTEREXAMPLES.md`, X001 | blob `4c393aa5507b67198127bae61f71f1a7fdb328ac` |
| supplement `SEED_LEMMAS.md` | blob `c575d18146a9a9d2bdee006dc3856947565442bc` |
| prior local A066 semigroup report | `runs/B14/20261011T201026Z-account01-B14-semigroup-entropy-variation/REPORT.md` |

The later reported A066 B05-payment folder
`20261011T211852Z-account01-B14-A066-b05-semigroup-payment` was not present
in this run's filesystem and its authorized repository path returned 404.
Accordingly, this proof does not rely on that unavailable report.  It uses
the fully read earlier semigroup derivation and the original X001 parity-lift
statement.

No external novelty claim is made and no primary theorem beyond these
elementary Fourier calculations is invoked.

## 3. Exact parity-lift transform

Let `g:{-1,1}^n->{-1,1}` and

\[
F(x,z)=g(x_1z,\ldots,x_nz).
\tag{3.1}
\]

Expanding `g` gives

\[
F(x,z)=\sum_{|S|\text{ even}}\widehat g(S)\chi_S(x)
+\sum_{|S|\text{ odd}}\widehat g(S)\chi_S(x)z.
\tag{3.2}
\]

Therefore the occupied-set map

\[
\lambda(S)=S\quad(|S|\text{ even}),\qquad
\lambda(S)=S\cup\{z\}\quad(|S|\text{ odd})
\tag{3.3}
\]

is injective and preserves every Fourier coefficient.  If `S` is sampled
from the squared Fourier law of `g`, the lifted degree is

\[
L=|S|+\mathbf1_{\{|S|\text{ odd}\}}.
\tag{3.4}
\]

Thus

\[
H(F)=H(g),\qquad
I(F)=I(g)+q,\quad q=\Pr(|S|\text{ odd}).
\tag{3.5}
\]

Since `1_{|S| odd}<=|S|`, `q<=I(g)` and

\[
\boxed{I(F)\le2I(g).}
\tag{3.6}
\]

Every occupied set of `F` has even cardinality, so its aggregate local
erasure `B` is zero, exactly as in X001.

## 4. Full-FEI hardness of the restricted variation target

The signed identity underlying (1.1) gives `V_-(F)>=H(F)`.  Hence, if

\[
\mathcal V_-(F)\le C I(F)
\tag{4.1}
\]

were proved for every parity lift (or every genuine Boolean function with
even Fourier support), then (3.5)--(3.6) would imply for every Boolean `g`

\[
H(g)=H(F)\le \mathcal V_-(F)\le C I(F)\le2C I(g).
\tag{4.2}
\]

So (4.1) on this restricted class already implies full FEI, with at most a
factor-two loss.  This prevents treating parity erasure as an easy endpoint
for the semigroup route.

## 5. Monotonicity still fails inside the parity-lift class

Let `N=2^r`, let

\[
g_r(x)=1-2\mathbf1_{\{x=0\}},\qquad
h_r(x)=\chi_{[r]}(x)g_r(x),
\tag{5.1}
\]

and parity-lift `h_r`.  Its squared spectrum has one heavy atom at
`A=[r]`, with

\[
a=(1-2/N)^2,
\tag{5.2}
\]

and `N-1` atoms of equal mass

\[
b=4/N^2.
\tag{5.3}
\]

The heavy lifted degree is `e_A=r+1_{r odd}`.  Since

\[
\sum_{S\subseteq[r]}\bigl(|S|+\mathbf1_{\{|S|\text{ odd}\}}\bigr)
=\frac{N(r+1)}2,
\tag{5.4}
\]

the mean lifted degree `bar e` over `S!=A` satisfies

\[
e_A-\bar e=
\begin{cases}
\dfrac{N(r-1)}{2(N-1)},&r\text{ even},\\[5pt]
\dfrac{N(r+1)}{2(N-1)},&r\text{ odd}.
\end{cases}
\tag{5.5}
\]

With `c=1-a=(N-1)b`, the two-group covariance identity and the exact
semigroup derivative give, in natural units,

\[
\boxed{
H_F'(0)=2ac(e_A-\bar e)\ln(a/b)>0
}\qquad(r\ge3).
\tag{5.6}
\]

This is an all-dimension analytic counterfamily to monotone dissipation
inside the genuine Boolean even-support class.  It is not a counterfamily
to FEI: its influence is order `r`.

## 6. Two positive parity-lift controls

### 6.1 Uniform spectral laws and addressing

For a base law uniform on its occupied atoms, `ln p` is constant.  The
normalized degree-damping identity reduces to

\[
H'(t)=-4t\operatorname{Var}_t(L)\le0.
\tag{6.1}
\]

Ordinary addressing on `a` address bits has a uniform squared spectrum,
`H=2a`, and original degree `1+Bin(a,1/2)`.  For `a>=1`, the probability
that this degree is odd equals `1/2`.  Its parity lift therefore has

\[
\boxed{
\mathcal V_-=2a,\qquad I=\frac{a+3}{2},\qquad
\frac{\mathcal V_-}{I}=\frac{4a}{a+3}<4.
}
\tag{6.2}
\]

Thus whole-set addressing remains correctly calibrated after parity lifting.

### 6.2 One-point defects

For the unshifted `g_r`, the unique mass `a` is at lifted degree zero and
every excited atom has the same base mass `b`.  At every `t`, if `A_t` and
`C_t` are the ground and total excited probabilities and `mu_t` is the
conditional excited mean degree, then

\[
\operatorname{Cov}_t(L,\ln p)
=A_tC_t\mu_t(\ln b-\ln a)\le0.
\tag{6.3}
\]

Hence `H'(t)<=0` and `V_-=H(g_r)`.  Moreover

\[
I(F_r)=\frac{2(r+1)}{2^r}.
\tag{6.4}
\]

Putting `delta=2^{1-r}`, the excited entropy is at most
`4 delta (r-1)`, while the heavy-atom entropy is at most
`2 delta/ln 2`.  Since `2/ln2<8`,

\[
\boxed{\mathcal V_-(F_r)/I(F_r)<4.}
\tag{6.5}
\]

This pays the rare point-defect logarithm once.  It does not claim the
unavailable later B05-payment theorem or a universal rare-restriction bound.

## 7. Mandatory obstruction checks

- **Parity-zero erasure:** addressed exactly by Sections 3--5.  The class is
  full-FEI-hard and still contains positive entropy production.
- **Rare defects:** the parity-lifted point defect has `V_-=H` and ratio
  below four.  No inference is made for every sparse activated family.
- **Whole-set addressing:** exact ratio `4a/(a+3)`; no label is paid per
  coordinate.
- **Near tensors:** the prior subadditivity
  `V_-(p tensor q)<=V_-(p)+V_-(q)` remains valid.  The present argument does
  not use overlapping-product subadditivity.
- **Shared-variable interference:** parity lifting is a physical shared
  substitution, but its Fourier action is computed exactly in (3.2); no
  unsupported product rule is used.
- **Weighted threshold controls:** not used; this run asserts no physical-TC
  or pivotal-credit inequality.
- **Fixed Rényi orders below one:** not used; the quantity remains Shannon
  entropy along a scale parameter.
- **Boolean realizability:** every analytic witness is an explicit Boolean
  truth table.  Non-Boolean prefix laws play no role.

## 8. Deterministic verification

`CHECK.py` uses an integer Walsh transform and exact rational influence.
There is no random seed.

It exhausts every Boolean truth table modulo global output sign through four
variables, applies the physical parity lift, and checks coefficient mapping,
entropy preservation, exact influence increment, the factor-two bound, and
even support.  It also verifies point/shifted-defect formulas for
`2<=r<=10` and addressing for `1<=a<=3`.

| Measurement | Result |
|---|---:|
| Boolean source tables exhausted | 32,906 |
| Lifted 3-bit sources with `H'(0)>0` | 8 of 128 |
| Lifted 4-bit sources with `H'(0)>0` | 13,496 of 32,768 |
| Programmatic assertions | 164,599 |
| Assertion failures | 0 |
| Random seeds | none |

The derivative census is numerical.  The all-`r` positive sign in (5.6)
and the monotonicity assertions in Section 6 are analytic proofs.

## 9. Status and handoff

This run gives a checkable A066 boundary theorem and completes the parity-lift
stress test for the proposed semigroup variation target.  It does **not**
establish the universal payment, satisfy independent review, or solve FEI.

Route the package to A088 and A094 for independent reconstruction.  The
next mathematical action is A067: identify a Boolean-specific analytic
regime stronger than even spectral support, since parity erasure alone is
now proved insufficient both for FEI reduction and for pointwise entropy
dissipation.

Exposed runtime identity: Codex based on GPT-5.  No separate reasoning-effort
selector or allowance meter was exposed.
