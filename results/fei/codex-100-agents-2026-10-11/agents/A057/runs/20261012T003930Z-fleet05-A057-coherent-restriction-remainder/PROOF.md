# Scoped payment of the capped recentered gate bank

All entropy quantities in this proof are in **bits**. Set
`c=1/ln(2)` and `c0=2/(e ln(2))`. Let u be any finite Boolean sign core,
let r>=1, p=2^(-r), and let A_r be the indicator of one point on r fresh
uniform control bits. Put `F=1+A_r(u-1)`, `a0=1-Eu`.

Take any finite adaptive tree querying only core coordinates, then at every
core leaf query all control coordinates. Initially consider a complete core
tree, so each core leaf is +/-1. At each core node v let `m=E u_v`,
`beta=hat u_v({i_v})`, `t=beta^2`, `v0=1-m^2`, `d=Inf_i(u_v)`,
and let w_v be its reach probability. Every core node is represented by the
same fresh activation outer and its actual, potentially biased, core child.
Use the A056 v2 positive-sector envelope, recomputing the induced outer law.
The capped gate charge is

`C_v=min{M_v(v0), (t/v0) M_v(v0)+p t log2(v0/t)}`,

with C_v=0 at t=0 or v0=0. Here the source formula is
`B_i(F_v)=p [B_i(u_v)-Phi(m^2,t)] + M_v(t)`,
where `Phi(s,t)=(s+t)h2(t/(s+t))`.
The subtraction is retained throughout. At control-tail nodes represent the
remaining point defect by literal inners; their capped charge is the actual
queried erasure entropy. No balancing auxiliary or changed Boolean family is
introduced.

**Theorem.** For the complete physical tree just specified, the total expected
capped gate charge, including the control suffix, satisfies

`sum_v w_v C_v + expected control-tail erasure
 <= (4+c0) p I(u)+5 r p a0 <= (4+c0) I(F)`.

More precisely the prefix is bounded by
`[4p(1-p)+c p^2+c0 p] Pi_I(u)+2r p^2 V_drop`,
where Pi_I is consumed core influence and
`V_drop=Var(u)-E Var(u_leaf)=sum_v w_v beta_v^2`.
This prefix formula remains valid for a partial adaptive core tree. It does
not provide a certified entropy bound for its still-activated core leaves.

## Proof

### 1. Actual shifted empty-control row

For the activation outer, in the uniform physical Fourier basis of the
unchanged control bits, A coefficients are `1-p` at the empty set and `-p`
at every nonempty control set; B coefficients are p everywhere. Recenter at
the actual core mean m. The empty coefficient is `C=1-p+pm`, and every
nonempty coefficient is `-p(1-m)`. Their exact multiplicities give

`M_v(s)=Phi(C^2,p^2 s)+p(1-p) Phi((1-m)^2,s)`.

This is the same M(s) as A056's biased-output erasure, since expanding the
control literals changes no basis. The empty-control row has not been
confused with the empty-core subtraction. Parseval gives
`C^2+p^2 v0=1-2p(1-p)(1-m)<=1`. Booleanity also gives
`t<=v0` and `|beta|<=d`.

### 2. A scalar envelope

For nonnegative amplitudes s,t,
`Phi(s^2,t^2)<=2st` in bits. To prove it, by homogeneity and symmetry assume
the ratio z=t/s lies in (0,1]. The natural-log expression divided by 2z is
`G(z)=[(1+z^2)ln(1+z^2)-z^2 ln(z^2)]/(2z)`.
Its derivative has the sign of
`(z^2-1)ln(1+z^2)-z^2 ln(z^2)`.
For x=z^2 in [0,1], `ln(1+x)<=x` and `-ln x>=1-x`, so this expression is
at least `-(1-x)x+x(1-x)=0`. Hence G(z)<=G(1)=ln2, proving the bit-unit
bound. Zero amplitudes follow by continuity.

The logarithmic sum bound also gives
`Phi(A,B)<=B log2(e(A+B)/B)` for B>0.
Apply these two bounds to M(v0), multiply by theta=t/v0, and keep the
envelope's own logarithm:

`theta M(v0)+p t log2(v0/t)
 <= p^2 t[2r+c+log2(1/v0)]
    +2p(1-p)(1-m)t/sqrt(v0)+p t log2(v0/t)`.

Since `t/sqrt(v0)<=|beta|`, `1-m<=2`, and `|beta|<=d`, the middle term
is at most `4p(1-p)d`. The remaining variance logs combine exactly:

`p^2 t log2(1/v0)+p t log2(v0/t)
 =p t log2(1/t)+p(1-p)t log2(v0)`.

The last summand is nonpositive, because v0<=1. Crucially it was combined
before taking an absolute value or making a local payment. Therefore

`C_v<=4p(1-p)d+p^2(2r+c)t+p t log2(1/t)`.

The retained rarity term obeys `t log2(1/t)<=c0 |beta|<=c0 d`.
This does not replace any logarithmic remainder by O(t).

### 3. Nonreuse of the two resources

The physical mean martingale satisfies
`Var(u_v)-[Var(u_v+)+Var(u_v-)]/2=beta_v^2`.
Consequently `sum_v w_v t_v=V_drop<=Var(u)`, while the physical influence
telescope gives `sum_v w_v d_v=Pi_I(u)`.
Also `t_v<=d_v`, so summing the preceding bound yields the precise prefix
formula in the theorem. For a complete core tree Pi_I=I(u), and
`Var(u)=a0(2-a0)<=2a0`. Thus

`prefix <= [4p(1-p)+c p^2+c0 p] I(u)+4r p^2 a0
        <= (4+c0)p I(u)+2 r p a0`,

since p<=1/2 and c<4. Core consumed influence is exactly p I(u). The
separate control influence r p a0 has not been queried during this prefix;
it is a labelled terminal reserve. The prefix price uses at most twice this
reserve, rather than repeatedly reopening it at successive core depths.

### 4. Complete control suffix

At a complete core leaf, F is constant +1 when u_leaf=+1 and is an r-bit
point defect when u_leaf=-1. The latter event has probability a0/2.
For a point defect on s bits put delta=2^(1-s). Its queried influence is
delta, and its erasure is

`Phi((1-delta)^2,delta^2)+2delta(1-delta)`.

For s=1 this is zero. For s>=2 write l=s-1. The logarithmic sum bound gives
its ratio to delta at most
`2(1-delta)+delta(2l+c)<=3`, because `2l/2^l<=1` and c<2.
Thus every suffix query costs at most 3 times its own influence.
The expected suffix influence is exactly `(a0/2) r 2^(1-r)=r p a0`.
Its charge is at most `3r p a0`. Prefix and suffix together give the theorem.
Since `c0>1`, the larger coefficient is 4+c0, which exceeds 5. One elementary
check is e<11/4 and ln2<7/10, yielding e ln2<77/40<2.

## Terminal and inner costs are still explicit

On the full core-first tree, the exact erasure charge is

`B_tree(F)=p [B_tree(u)-sum_core w_v Phi(m_v^2,t_v)]
          +sum_core w_v M_v(t_v)+expected B_tree(point-defect suffix)`.

The exact entropy-decrement ledger has the corresponding nonempty inner
decrements and the outer JS terms. The sum of the inner nonempty decrements
is bounded above by p H(u), **which remains unpaid for arbitrary u**.
For a partial tree, keep the actual terminal entropy E H(F_leaf). A056's
once-per-query outer-JS bound costs at most (2/ln2)I(F); it does not eliminate
the arbitrary core term or justify FEI. The new result pays the requested
capped gate envelope, not the complete inner plus terminal functional.

## Sparse-bent application and comparison

Take the actual core selecting a k-bit quadratic bent sign b and its flip at
zero, k>=4 even. Then `I(u)=k/2+(k+1)2^(-k)` and
`E u=2^(-k/2)-2^(-k)`. The theorem includes the original B05 activation r=2k,
and either marker-first or marker-last core order. In particular the bad
selector's local logarithm creates no divergence of the capped gate-tree bank.
This stage does not reprove the already known H<=8I for these activations.
A027's partial-core entropy transport controls a different signed aggregate;
the present bound controls the larger positive capped gate envelope itself
and names its one-time influence/variance resources.

## First unsupported universal line

A dimension-independent payment of the nonempty inner-decrement sum plus
actual terminal entropy for a universal physical selection policy remains
unproved. Beyond fresh point controls, the other-output erasure need not have
the two multiplicity classes above; the negative variance-log combination
can no longer be assumed. Overlapping controls require a common ownership
account for their control reserves. No uniform K for all Boolean functions
or unbounded Boolean H/I family follows.
