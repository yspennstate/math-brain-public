# B12 / A056 — joint outer–child payment on the tensor no-go family

Run: `20261013T192205Z-account01-B12-gu-joint-tensor-payment`  
Attempt: `A056-GU-JOINT-TENSOR-06`  
Stable gap: `GU-JOINT-OUTER-CHILD-PAYMENT`  
Status: **PROVED BY CONTRIBUTOR, PENDING INDEPENDENT REVIEW; UNIVERSAL GU AND FULL FEI OPEN**

## Result

The preceding B12 run proved—and A094 independently accepted—that no finite
constant can pay the one-child endpoint reserve solely from the child's
variance or source influence.  This run restores the omitted outer physical
budget on exactly that obstruction family.

Let `u` be the four-bit Boolean slice with truth-table index `22338`, let `v`
be four-bit full parity (index `38505`), and set

\[
U_k=u^{\otimes k},\qquad V_k=v^{\otimes k}.
\]

Let `d_{8k}` be the point defect on `8k` bits and define the genuine Boolean
function on `12k` physical bits by

\[
F_k(x,z)=
\begin{cases}
U_k(z),&d_{8k}(x)=-1,\\
V_k(z),&d_{8k}(x)=+1.
\end{cases}
\]

Then, for every `k>=1`,

\[
\boxed{H(F_k)\le\frac{1728}{595}I(F_k)<3I(F_k).}
\]

Therefore

\[
U(F_k)\le\frac{1728}{595}I(F_k),
\]

and the complete endpoint-centered biased-child reserve satisfies

\[
\boxed{
\overline\Theta_k(-1+2^{1-8k})
\le\frac{1728}{595}I(F_k).}
\]

This is a dimension-, depth-, bias-, and collision-ratio-independent joint
payment on the exact family where every child-only constant fails.

## Proof

Write `n=8k`, `r=2^-n`, `q=1-r`, and

\[
\mu=-1+2r,\qquad \delta=1-\mu^2=4r(1-r).
\]

For the two-slice outer gate, the activation energy is

\[
\beta_k=\Pr[U_k\ne V_k]=\frac{1-8^{-k}}2\le\frac12.
\]

The Fourier spectrum of `F_k=a+d_n b` splits into the empty-selector sector
and the nonempty-selector sector.  The latter has total squared mass

\[
m=\delta\beta_k\le2r=2^{1-8k}.
\]

The empty sector contains at most `2^(4k)` atoms and the nonempty sector
fewer than `2^(12k)` atoms.  Conditional entropy maximization within the two
sectors yields

\[
H(F_k)\le h_2(m)+4k(1-m)+12km
=4k+h_2(m)+8km.
\]

Since `h_2(m)<=1<=k` and

\[
8km\le16k2^{-8k}\le k/16,
\]

we get

\[
H(F_k)\le\frac{81}{16}k.                                  \tag{1}
\]

Exact Walsh arithmetic gives

\[
\langle u,v\rangle=\frac18,\qquad I(u)=\frac74,
\qquad I(v)=4.
\]

The physical influence ledger is exactly

\[
I(F_k)=qI(U_k)+rI(V_k)+\beta_k I(d_{8k}).                    \tag{2}
\]

Tensor additivity gives `I(U_k)=7k/4`, and `q>=255/256`; hence

\[
I(F_k)\ge\frac{1785}{1024}k.                               \tag{3}
\]

Dividing (1) by (3) gives the claimed constant

\[
\frac{81/16}{1785/1024}=\frac{1728}{595}<3.
\]

The upper-set potential obeys `U<=H` termwise.  Moreover, the exact
biased-child cocycle gives

\[
\overline\Theta_k(\mu)
=U(F_k)-\beta_kU(d_{8k})-qU(U_k)-rU(V_k)le U(F_k).
\]

This proves the joint terminal-reserve payment.

The full proof is archived in `JOINT_TENSOR_PAYMENT.tex`.

## Why this matters

The accepted no-go had left open whether the cap-ratio explosion reflected a
real FEI obstruction or only an invalid allocation of the physical budget.
This theorem decides that question for the entire parametric family: it is an
allocation obstruction.  The child-only normalized reserve diverges, yet the
full Boolean functions satisfy FEI with one constant below three because the
outer tensor retains linear influence.

The mechanism is explicitly joint:

- the rare activation sector costs at most one binary bit plus `8km` bits;
- the outer data block contributes at least `(1785/1024)k` physical influence;
- neither contribution is recharged by depth;
- the exponentially growing cap-ratio never appears after the complete
  physical ledger is used.

This does not prove universal GU.  It isolates the useful structural repair:
terminal reserve must be compared with the total physical composition, not
with the child channel alone.

## Direct diagnostics

The deterministic checker reconstructs the exact base identities and the
rational constant proof.  It also directly evaluates `H`, `U`, the terminal
reserve, and the one-scale GU quantity `G` for `k=1,2,3,4`.

| `k` | `H/I` | `U/I` | reserve / `I` | `G/I` |
|---:|---:|---:|---:|---:|
| 1 | 1.9247119625 | 0.6559862478 | 2.3505e-2 | 0.7965637345 |
| 2 | 1.9003068227 | 0.6272707778 | 3.3822e-4 | 0.7422823451 |
| 3 | 1.9002150771 | 0.6269226490 | 6.1689e-6 | 0.7408952865 |
| 4 | 1.9002147328 | 0.6269165606 | 1.2913e-7 | 0.7408570091 |

The finite `G/I` values are diagnostics only; no all-`k` GU claim is inferred
from them.  The all-`k` FEI, `U`, and joint-reserve bounds are analytic.

Reproduction:

```bash
python3 check_joint_tensor_payment.py
```

No randomness or seed is used.

## Previous and new status

- Previous, independently accepted: no finite `C` pays the reserve by
  `C beta(1-mu^2)` or `C beta I(h)`.
- New, pending review: on the same all-depth Boolean family, the complete
  joint budget pays both FEI and the terminal reserve with
  `C=1728/595<3`.
- Interpretation: the tensor cap-ratio explosion is a certified child-only
  allocation failure, not an FEI counterfamily.
- Universal GU: **OPEN**.
- Full FEI: **OPEN**.

## Scope and next unpaid step

The proof uses the fixed base slice `u` with `I(u)=7/4`, full-parity slice
`v`, and the `8k`-bit point-defect activation.  It does not cover arbitrary
slice pairs, arbitrary activation laws, overlapping physical inputs, or a
universal signed GU ledger.

The next step is to replace the support-size bound by a compositional sector
entropy bound in terms of outer influence or endpoint `U`, with constants
that do not require a fixed positive influence density.  That candidate must
then be tested on shared-coordinate activation/source overlap.

## Sources and review

Relied-on immutable evidence:

- B12 tensor no-go core: `math-open-problems@b631276522c94b64f7f54e2014822e4c6e05463f`.
- B12 tensor no-go finalized receipt: `math-open-problems@ef67e8cd5c8e81b3eb4ffb13ce2a786bb52bddc3`.
- A094 independent acceptance: `math-open-problems@88270c6634d96ee594a03845900a2445b019294a`.
- A094 delivery receipt: `math-open-problems@a12cb4f9554bc3473b037f83b78a9f3ff85d62f2`.
- Exact biased-child cocycle receipt: `math-open-problems@335e5c6488f95c0f53b3ce3bcac275bada17e0e6`.
- Owner GU order blob: `7c5e21945adef435e6b587909603dd96794a1ebe`.
- B12 compact assignment blob: `40935ac651643a17815d0addf664ec4c1c0313cc`.
- Concurrent B01 fixed-bias tower result inspected for scope:
  `math-open-problems@bdd18f98e73739debb566afac8a55356af5ff370`;
  it neither proves nor conflicts with the joint tensor payment here.

No independent review of the new joint theorem is observed.  Route to A091
and A090; A094 reviewed the predecessor and may also audit the new allocation
claim if recusal rules permit.
