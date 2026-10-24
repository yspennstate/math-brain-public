# Solo FEI continuation: Shannon barrier for every singleton-corrected NAND potential

## Outcome

Full Friedgut--Kalai Fourier entropy--influence remains **OPEN**. The previous continuation produced a logarithmic potential contracting under arbitrary unequal disjoint NAND. This continuation proves that neither that potential nor any fixed retuning of its singleton correction can satisfy a dimension-free one-coordinate Shannon-restriction recursion.

For every fixed real c, let

    W_c(A)=U(A)+cQ_A,

where U is the complement-invariant indicator logarithmic-edge functional and Q_A is the singleton Fourier-square mass. An explicit bent function with a one-point marker has restrictions A_0,A_1 and selector influence 2^(-m) such that

    [W_c(A)-(W_c(A_0)+W_c(A_1))/2]/2^(-m)
      =[1/4+1/(2ln2)+o(1)]m.                            (1)

Thus no fixed c and C give

    W_c(A)<=average(W_c(A_0),W_c(A_1))+C Inf_selector

for all indicators and coordinates. This is a proof-method obstruction, not a counterexample to FEI and not evidence that W_c/I is unbounded.

All work in this continuation was done by the primary assistant. Subagents, delegated tasks, other-model calls, commissioned audits and outside contacts: zero. Actual model and reasoning-level metadata are not exposed and are therefore UNVERIFIED.

The freshly read master head at the start was `499676351e82d5a372c79f9f3afe22e951e585d2`; the newest prior solo commit was `6e25bb8885585972be64b72dabbd6b5c9813c78e`. The current root exclusion register, latest P03 fleet handoff, solo README and NEXT_STEPS, erasure reduction, unequal-NAND proof and newest report were read first. The original P03 finite-dimensional metric 6 remains a prior reported fact only; its exhausted enumeration was not resumed.

## 1. Why this extension mattered

The prior potential

    V(A)=U(A)+(2/ln2)Q_A

satisfies an exact contraction under disjoint NAND products. If it also obeyed a restriction inequality with a constant charge to the split-coordinate influence, it could be combined with Boolean-preserving Shannon induction and would move beyond read-once composition. The bent-marker family shows that this bridge is impossible in that form.

The result is stronger than failure for the coefficient 2/ln2: the leading defect in (1) is independent of every fixed singleton coefficient c. Hence retuning Q cannot repair the route.

## 2. Exact construction

Let m be positive and even, N=2^m, epsilon=N^(-1/2), and delta=N^(-1). Define

    g(x)=(-1)^(x_1x_2+...+x_(m-1)x_m).

Its Walsh coefficients are s_S epsilon with s_S in {+1,-1}. Tensoring `(1,1,1,-1)/2` gives

    s_empty=s_{i}=+1,
    n_+=(N+sqrt N)/2,   n_-=(N-sqrt N)/2,

and exactly N/4 sign-changing spectral edges in each coordinate direction.

Flip only g(0) to obtain g'. Then

    ghat'_S=s_S epsilon-2delta.

Let F have selector restrictions g,g', and set A=(1-F)/2 and A_j=(1-g_j)/2. The restrictions differ at one of N physical points, so the selector influence is exactly delta.

## 3. Exact potential formulas

With h(x)=-x log_2 x, put

    q=epsilon^2/4,
    x_+=epsilon^2(1-2epsilon)^2/4,
    x_-=epsilon^2(1+2epsilon)^2/4.

Then

    W_c(A_0)=m h(q)+cmq,

    W_c(A_1)=(mN/4)x_+log_2(x_-/x_+)+m h(x_+)+cmx_+.

For the selector function put

    z_+=epsilon^2(1-epsilon)^2/4,
    z_-=epsilon^2(1+epsilon)^2/4,
    y=epsilon^4/4.

Its data-layer and selector-layer internal costs are

    K_data=(mN/4)z_+log_2(z_-/z_+),

    K_sel=y[(n_+-1)log_2(z_+/y)+n_-log_2(z_-/y)].

Therefore

    W_c(A)=K_data+K_sel+m h(z_+)+h(y)+c(mz_++y).        (2)

These formulas are exact for every positive even m. Their complete derivation is in `SHANNON_POTENTIAL_BARRIER_2026-09-18.md`.

## 4. Asymptotic proof

Using

    log_2[((1+t)/(1-t))^2]
      =[4/ln2](t+t^3/3+O(t^5)),

the data-edge difference between (2) and the average restriction potential is

    [m epsilon^2/(2ln2)]+O(m epsilon^3).

The selector-layer edges contribute

    m epsilon^2/4+O(m epsilon^4+epsilon^4).

Taylor expansion of h at q shows that the remaining data-singleton entropy defect is O(m^2 epsilon^4). The Q defect is exactly

    (mz_++y)-[mq+mx_+]/2=(1-m)epsilon^4/4.

Thus the contribution of every fixed c is lower order. Since epsilon^2=delta, summing proves (1).

## 5. Exact checks

Executed from the solo folder:

    python check_shannon_potential_barrier.py
    python -m py_compile check_shannon_potential_barrier.py

The script returned PASS. It uses exact rational Walsh transforms and 160-bit outward rational logarithm intervals for m=2,4,6,8,10,12. It independently evaluates the truth tables and verifies all closed formulas for the actual NAND potential c=2/ln2. At m=12 the selector influence is exactly 1/4096 and the defect/influence interval is rigorously positive and approximately 11.382.

Finite checks do not prove the asymptotic theorem; the all-m algebra does. This is a self-check, not an independent audit.

## 6. Failed route and exact boundary

Attempted extension:

    disjoint NAND contraction
      -> one-coordinate Shannon recursion
      -> induction on arbitrary Boolean functions.

The second arrow fails by (1). The failure comes from two sources that survive restriction averaging:

- a data-layer scale imbalance contributing `m delta/(2ln2)`;
- many selector-layer small-to-large edges contributing `m delta/4`.

Singleton entropy or Q corrections contribute only lower-order terms and cannot cancel them with a fixed coefficient.

What survives is precisely the disjoint-product theorem: once seed potentials are controlled, arbitrary unequal NAND does not amplify their normalized value. No seed-independent bound is obtained.

## 7. Literature and novelty limits

Fresh primary-source searches included:

- `site:arxiv.org Fourier entropy influence conjecture 2026 restriction bent function`
- `site:arxiv.org "Fourier entropy" "bent" influence`
- `site:arxiv.org "Fourier Entropy-Influence" 2026`

They reopened González--MacManus--Pereyra, arXiv:2606.00246, whose restriction-induction framework is acknowledged prior art, and O'Donnell--Tan, arXiv:1304.1347, whose disjoint composition theorem already covers read-once formulas. The searches did not verify novelty of (1). No novelty claim is made.

## 8. Exact remaining obligation

The full target remains

    K(f)=sum_edges min(p_S,p_T)|log_2(p_S/p_T)|
       <=C sum_S |S|p_S

under the signed Boolean convolution identities. The new obstruction rules out one local route from composition to induction. It does not rule out an aggregate non-reusing scale allocation, a favorable-coordinate theorem, or a proper-block selection result.

## 9. Measured execution

The supplied run start was 2026-09-18T03:58:17Z and the first sampled shell clock was 03:58:35Z. This report checkpoint is 04:04:19Z: 6 minutes 2 seconds from supplied start and 5 minutes 44 seconds between sampled shell clocks. This includes retrieval, derivation, exact checking, literature search and writing; it is not a claim of continuous model compute. GitHub delivery time is not included.

Intervals between continuations are not counted as research time. Neither the schedule nor this report establishes an hour of work or ten continuous hours.
