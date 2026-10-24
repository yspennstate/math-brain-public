# Block restriction identity and its exact surviving term

Status: proved below, self-checked, novelty UNVERIFIED. This generalizes the one-coordinate erasure/JS identity already recorded. It is a framework, not a proof of FEI. The parity construction in `ERASURE_SYNERGY_AND_DUALITY_2026-09-18.md` proves that the block conditional term cannot be replaced by average restriction erasure.

All logarithms in entropy quantities are base two. Natural logarithms are written ln.

## 1. Partial Fourier channel

Partition the n physical input coordinates into nonempty A and its complement C. For x in {+1,-1}^A and D subset C define

    v_D(x)=E_y[f(x,y) chi_D(y)],
    q_x(D)=v_D(x)^2.                                    (1)

For every x, q_x is the squared Fourier law of the Boolean restriction f_x on C, hence a probability law. Let

    q(D)=E_x q_x(D).

Expanding v_D in the x characters and using Parseval gives

    q(D)=sum_{E subset A} fhat(E union D)^2.             (2)

Thus q is exactly the C-marginal of the full spectral random subset Z=(Z_A,Z_C).

Let X denote the uniformly random physical assignment on A, and conditionally on X=x draw D with law q_x. Then

    H(q)-E_x H(q_x)=I(X;D).                              (3)

Since H(f)=H(Z_C)+H(Z_A|Z_C), equations (2)-(3) give the exact block identity

    H(f)-E_x H(f_x)
       = H(Z_A|Z_C)+I(X;D).                              (4)

For |A|=1, the first term is B_i and the second is the Jensen--Shannon term from `ERASURE_REDUCTION.md`.

## 2. Dimension-free bound for the channel information

**Theorem.** For every block A,

    I(X;D) <= (2/ln 2) I_A(f),                           (5)

where I_A(f)=sum_{i in A}Inf_i(f).

**Proof.** We first prove the cube logarithmic Sobolev inequality in exactly the normalization needed here. For every nonnegative g on a uniform cube,

    Ent(g^2):=E[g^2 ln(g^2/Eg^2)]
       <= (1/2) sum_i E[(g(x)-g(x^i))^2].                (6)

For one bit, homogeneity reduces (6) to u=t,v=1. After multiplying by two and moving the entropy to the other side, the required quantity is

    F(t)=(t^2+1)ln[(t^2+1)/2]-2t^2 ln t+(t-1)^2.

It satisfies F(1)=0 and

    F'(t)=2t ln[(t^2+1)/(2t^2)]+2(t-1).

For t>=1, F'(t)>=0 is equivalent to

    ln[2t^2/(t^2+1)] <= 1-1/t.

The right side minus the left side vanishes at one and has derivative

    (t-1)^2/[t^2(t^2+1)] >=0.

Thus F(t)>=0 for t>=1; the symmetry F(t)=t^2 F(1/t) handles 0<t<=1, and endpoints follow by continuity. This proves the two-point case. Entropy tensorization (apply the conditional two-point inequality one coordinate at a time and use the entropy chain rule) yields (6) on a product cube.

For q(D)>0 put w_D(x)=q_x(D)/q(D), whose x-mean is one. In natural units,

    (ln 2) I(X;D)=sum_D q(D) Ent_x(w_D).

Apply (6) to g=sqrt(w_D), multiply by q(D), and sum D:

    (ln 2) I(X;D)
      <=(1/2)sum_{i in A}E_x sum_D
            (|v_D(x)|-|v_D(x^i)|)^2
      <=(1/2)sum_{i in A}E_x sum_D
            (v_D(x)-v_D(x^i))^2.                       (7)

Parseval in y makes the inner sum

    E_y[(f(x,y)-f(x^i,y))^2]
       =4 Pr_y[f(x,y)!=f(x^i,y)].

Average x and sum i to obtain (5). Terms with q(D)=0 vanish identically. QED.

Combining (4)-(5),

    H(f)-E_x H(f_x)
       <= H(Z_A|Z_C)+(2/ln2)I_A(f).                     (8)

## 3. Exact block sufficient criterion

Suppose there is a finite K such that every nonconstant Boolean f admits a nonempty physical block A for which

    H(Z_A|Z_C)<=K I_A(f).                               (9)

If A is allowed to be all coordinates, (9) is just FEI itself, so useful versions must impose a genuinely smaller-block rule. Subject to such a rule, (8) supports restriction induction.

Indeed, the exact influence decomposition is

    I(f)=E_x I(f_x)+I_A(f).                              (10)

It follows from Parseval in the same partial expansion, or directly by averaging restriction influences on C and adding the physical influences in A. If every restriction f_x already satisfies H(f_x)<=C I(f_x), then (8)-(10) give H(f)<=C I(f) whenever C>=K+2/ln2. Induction terminates because A is nonempty.

This is a block generalization of the existing coordinate program, not a claim that (9) has been proved with a useful block restriction.

## 4. Why average fiber erasure cannot replace the conditional term

One might hope to strengthen (8) by replacing H(Z_A|Z_C), or by bounding the C-side erasure of q, using the average erasure of the restriction laws q_x plus O(I_A). The semi-bent parity construction proves this impossible.

With one selector input and m data coordinates, its two q_x laws are uniform on even and odd parity respectively. Each has aggregate erasure zero. Their mixture q is uniform on all m bits and has aggregate erasure m, while I_A=1/2 and I(X;D)=1. Hence

    B(q)-E_x B(q_x)=m

with bounded selector influence and bounded channel information. Conditional entropies can exhibit high-order synergy: one latent parity bit is revealed separately by every erased coordinate when the other m-1 are known.

Equation (4) remains valid because it uses full entropy of the restrictions. In this example H(q)-E H(q_x)=1, exactly the channel information. It is the attempted replacement of full restriction entropy by erasure entropy that loses m-1 bits of parity constraint.

## 5. Remaining route

A useful block choice in (9) would need to detect and include enough coordinates from every high-order spectral constraint, while paying each physical influence only once through (10). The existing one-coordinate bent-marker obstruction says arbitrary singleton blocks do not work; the parity synergy obstruction says averaging fiber erasure does not repair larger-block induction.

No selection theorem of this kind is proved here. The precise live possibilities are:

1. prove (9) with a nontrivial universal rule such as a proper block of controlled relative size;
2. build a nonlinear potential that retains parity-type constraints and has an exact non-reuse identity analogous to (10);
3. abandon restriction induction and control the logarithmic edge functional K directly from signed Boolean convolution.

The first option is stated as an obligation, not a conjecture asserted to be true.
