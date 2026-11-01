from pathlib import Path
s=r'''

## 3. Exact critical dynamics in the smallest target case d=4, k=2

Here r=d-k+1=3 and q denotes initial vacancy density (occupied density is 1-q). The core message recursion on the infinite 4-regular tree is

  x_0=q,
  x_{t+1}=q P(Bin(3,x_t)>=2)=q(3x_t^2-2x_t^3),
  h_0(q)=q,
  h_t(q)=q P(Bin(4,x_{t-1})>=3)
        =q(4x_{t-1}^3-3x_{t-1}^4), t>=1.               (B1)

Justification of the message recursion, including its relation to peeling. On any graph define directed messages b^0_{u->v}=Z_u and

  b^{j+1}_{u->v}=Z_u 1{sum_{w in N(u)\{v}} b^j_{w->u}>=r-1}.

They decrease in j. Let a^0_v=Z_v and a^j_v=Z_v 1{sum_{u in N(v)}b^{j-1}_{u->v}>=r} for j>=1. We prove a^j equals the true j-round vacancy indicator by induction. This is immediate at j=0,1. If v survives the true jth round, then it was initially vacant and has at least r neighbours u with a^{j-1}_u=1. For j>=2 the latter have r incoming messages at time j-2, so after excluding v they have at least r-1 and b^{j-1}_{u->v}=1. This gives a^j_v=1.

Conversely if a^j_v=1, then a^{j-1}_v=1 by monotonicity, and there are at least r neighbours u with b^{j-1}_{u->v}=1. For j=2, the initially vacant v supplies one extra support to each such u in addition to its r-1 other initially vacant neighbours, hence a^1_u=1. For j>=3, excluding u from v's at least r incoming messages at time j-1 leaves at least r-1 messages; by monotonicity they are also present at time j-3. Thus b^{j-2}_{v->u}=1. Together with the r-1 supports at time j-2 supplied by b^{j-1}_{u->v}=1, this gives a^{j-1}_u=1. In either case v has at least r true surviving neighbours at round j-1 and itself survived that round, so survives round j. This completes the induction. On the infinite tree the r-1 forward subtrees for a directed edge are independent, giving (B1).

The critical values are q*=8/9, x*=3/4, p*=1/9: q*(3x*^2-2x*^3)=x*, and the derivative in x is 1. Write z_t=x_t-x* at q=q*. Then z_0=5/36 and the following identity is exact:

  z_{t+1}=z_t-(4/3)z_t^2-(16/9)z_t^3.                  (B2)

Let a=4/3, b=16/9, alpha=36/5 and B=1152/569. For 0<z<=5/36,

  1-a z-b z^2 >= 569/729>0,
  a <= 1/[z(1-a z-b z^2)]-1/z
       = (a+b z)/(1-a z-b z^2) <= B.                   (B3)

The first inequality evaluates the decreasing quadratic at 5/36. For the last bound increase the numerator to a+b(5/36)=128/81 and decrease the denominator to 569/729, giving 1152/569. Therefore z_t stays positive, decreases, and telescoping (B3) proves

  1/(alpha+B t) <= z_t <= 1/(alpha+a t).                (B4)

Its limit is zero (a positive limit would force the decrement in (B2) to stay positive). The reciprocal increments in (B3) converge to a, so their averages converge to a; consequently

  t z_t -> 3/4,
  t^2 (x_t-x_{t+1}) -> 3/4.                            (B5)

The root-density expansion is also exact:

  h_t(q*)-21/32
    =(3/2)z_{t-1}-z_{t-1}^2-(40/9)z_{t-1}^3-(8/3)z_{t-1}^4.

Combined with (B5) it gives

  t[h_t(q*)-21/32] -> 9/8.                             (B6)

The asymptotic core density 21/32 is positive. This is fully compatible with finite random graphs having a critical probability of complete occupation of order one: a finite stochastic bottleneck decides which branch is reached after many rounds, and fixed-round limits do not commute with final stabilization.

### 3.1 The scale obstruction, stated precisely

For a perturbed vacancy density q=q*+eta, at x=x* the message-map drift is exactly

  T_q(x*)-x*=(27/32)eta.                                (B7)

More generally, the exact perturbation polynomial is

  T_{q*+eta}(x*+z)-(x*+z)
    =-(4/3)z^2-(16/9)z^3
      +eta[(27/32)+(9/8)z-(3/2)z^2-2z^3].              (B8)

In the n^-1/2 critical window, (B7) has scale n^-1/2. At criticality the residual deterministic message decrement is

  D_t=x_t-x_{t+1} >= (4/3)/(alpha+B t)^2.               (B9)

If one tries to approximate the saddle-node drift to error at most C n^-1/2 using the critical t-step tree recursion, (B9) forces

  t >= [sqrt((4/3)/C) n^(1/4)-alpha]/B.

This is a rigorous lower bound on the depth required by THAT drift-approximation strategy, not a claimed lower bound on the actual finite-graph stabilization time. Equivalently, for t=o(n^(1/4)) the critical deterministic residual dominates n^-1/2.

A tree radius-t ball in a d-regular graph has S_t vertices, so S_t<=n is necessary for any such ball to exist. For fixed d>=3 this forces t=O(log n). Thus the tree-ball conditional-mean argument underlying Theorem A cannot be applied at depths of order n^(1/4): none of those balls is a tree. No uniform-in-t extension of (A2), (A5), or (A7) has been invoked. We have identified a genuine limitation of the selected local approach, rather than incorrectly equating a fixed-round limit with the final event.

### 3.2 Checked and unproved portions

CriticalRecursion.lean checks the rational polynomial identities (B2), the root expansion, and (B8) by `ring`, plus the rational constants in (B3) by `decide +kernel`. It imports only Mathlib.Tactic.Ring. The command `lake env lean ~/brain_workers/TRIO_1011/op/E0089/CriticalRecursion.lean`, run from ~/lean_verify with a one-hour subprocess timeout, exited 0; second_lean_check.txt records the result. These are kernel-checked algebraic statements, not a Lean formalization of Theorem A or the asymptotic argument.

The inequalities, induction, and asymptotics (B3)-(B6) have complete handwritten proofs above. The exact identities were additionally evaluated in Python with rational arithmetic, and the recursion/bounds were checked numerically through 100000 iterations with 40-digit Decimal arithmetic; details are in second_experiments.py and second_experiments.json. Numerics do not replace the proof.
'''
p=Path('SECOND_ATTEMPT.md');p.write_text(p.read_text(encoding='utf8')+s,encoding='utf8')
