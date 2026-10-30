# B10 / A047 — analytic lower-q collar for the two-bit half-tax candidate

**Claim version:** `B10-A047-HALF-TAX-LOWER-Q-v1`  
**Status:** PROVED analytically; independent A092/A090 review pending.  
**Full FEI:** OPEN.

## Result

For the frozen two-bit AND-class candidate
[
J_Ale M_A+rac12Delta_A,
]
the margin
[
D(p,q):=M_A+rac12Delta_A-J_A
]
is strictly positive for every
[
oxed{pin[1/64,49/100],qquad qin[0,1/100].}
]
More explicitly,
[
oxed{D(p,q)>
rac{5,027,251}{19,592,160,000}
>2.56	imes10^{-4}.}
]

This closes the entire lower-(q) collar adjacent to the compact-core certificate. It is an analytic continuum result, not a finite grid or floating certificate.

## Frozen formulas

Write (h=h_2) and
[
s=4q(1-q),qquad c=4q^2,qquad
z=rac{cp(1-p)}{1-sp}.
]
The exact quantities are
[
M_A=(1-sp)h(z)+sp,h(p),qquad
J_A=h(sp)-p,h(s),
]
and
[
Delta_A=plog_2rac{1-p}{p}.
]

## Proof

Since entropy is nonnegative,
[
M_Age sp,h(p).
]
For fixed (p), define
[
Phi_p(t)=h(pt)-p h(t).
]
Then (Phi_p(0)=0) and
[
Phi_p'(t)
=plog_2rac{1-pt}{p(1-t)}.
]
The ratio ((1-pt)/(1-t)) is increasing in (t). Hence
[
J_A=Phi_p(s)
le pslog_2rac{1-ps}{p(1-s)}.
]
Let
[
L_p=log_2rac{1-p}{p}.
]
Using
[
h(p)-log_2(1/p)=-(1-p)L_p,
]
we obtain
[
D(p,q)ge
pleft[
left(rac12-s(1-p)ight)L_p
-slog_2rac{1-ps}{1-s}
ight].
]
Now
[
rac{1-ps}{1-s}
=1+rac{s(1-p)}{1-s},
]
so (log_2(1+x)le x/ln2) gives
[
slog_2rac{1-ps}{1-s}
lerac{s^2}{(1-s)ln2}.
]
On the stated rectangle,
[
sle s_0=4cdotrac1{100}cdotrac{99}{100}
=rac{99}{2500},
]
and
[
L_pgelog_2rac{51}{49}
=rac{ln(1+2/49)}{ln2}
gerac{2}{51ln2}.
]
Therefore
[
rac{D(p,q)}p
gerac1{ln2}left[
left(rac12-sight)rac2{51}
-rac{s^2}{1-s}
ight].
]
The bracket is strictly decreasing in (s), and at (s=s_0) equals exactly
[
left(rac12-rac{99}{2500}ight)rac2{51}
-rac{(99/2500)^2}{1-99/2500}
=
rac{5,027,251}{306,127,500}>0.
]
Since (1/ln2>1) and (pge1/64),
[
D(p,q)>
rac1{64}rac{5,027,251}{306,127,500}
=
rac{5,027,251}{19,592,160,000}.
]

All endpoint cases are included. At (q=0), (s=c=z=0), so the original formulas are well defined with (h(0)=0), and the same positive bound follows for (ple49/100).

## Coverage delta

Together with the existing compact-core certificate, the candidate is now proved on
[
pin[1/64,49/100],qquad qin[0,99/100].
]
The later balanced-transition certificate extends (p) to (1/2) away from the remaining equality collars. This run does not import that later local artifact as remote evidence; it records the analytic collar independently.

## Scope

This proves only the displayed two-bit AND-class inequality on the stated continuum region. It does not establish higher arity, global nonreuse, or full FEI.

## Next unpaid step

Apply the same derivative-integral method to the upper collar (qin[99/100,1]). The (c=4q^2) term is no longer small, so the useful lower bound must retain ((1-sp)h(z)) instead of discarding it. The rare-(p) strip (p<1/64) and the equality collars at (p=1/2) remain separate obligations.
