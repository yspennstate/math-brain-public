# Single owned separator reserve for three events

Let U,V,W be point indicators on disjoint fresh blocks of widths R,T,L>=1, and X a fresh fair bit. Let A=X(U OR V) OR WUV and F=1+A(g-1), with an independent balanced Boolean core g. Write p=EW, q=EU, r=EV, beta=q+r-qr, and eta=pqr. The root separator X has controller children A0=WUV, A1=U OR V; A0 is contained in A1, and the difference D=A1-A0 is an indicator of density e=beta-eta. Root density is pi=(beta+eta)/2 and root queried influence d_X=e/2.

Query X first. In its zero branch, resolve the point WUV; in its one branch, resolve the two-event union U OR V by the previous exposure rule. Stop when the controller is fixed, retaining one core terminal with expected entropy pi H(g) and influence pi I(g). All descendant control queries are K=4-good, since the conditional core is still balanced, a=1. This assertion is independent of whether the X root is good or bad.

Define J(B)=I(1-2B)/2. The exact control influence decomposition is

    J(A)=d_X+Jrem,
    Jrem=[J(A0)+J(A1)]/2,
    J(A0)=(L+R+T)eta,
    J(A1)=R q(1-r)+T r(1-q).

These are owned physical-coordinate contributions, not raw event boundaries. Terminal probability is pi, never beta+eta, and both overlapping events lead to the same g, not separate copies.

The separator's odd-face charge is c_X=I(F0F1)/2. Since F0F1=1+D(g-1), balance gives exactly

    c_X=e I(g)/2+J(D)/2.

In this point-block family the exact expression is J(D)=R q(1-r)+T r(1-q)+(L+R+T)eta=J(A1)+J(A0)=2Jrem: their boundary edges are disjoint. Also e/2<=pi. Thus c_X=Jrem+e I(g)/2<=Jrem+pi I(g), and Q_bad for this stopping tree is either c_X or zero. In particular Q_bad<=I(F)-d_X<=I(F), uniformly in L,R,T and core dimension. The actual face currency is counted once at X. No reserve may be reposted below X.

Reserve ownership: choose K=5+2/ln2. Every nonseparator control coordinate receives K times its physical influence. Reserve one unit of that rate for the separator, leaving exactly 4+2/ln2 for its own descendant erasure/recombination cost. Each terminal-core coordinate receives (C0+1) times its expected physical influence when H(g)<=C0 I(g); reserve one unit for the separator's data contribution, leaving C0 for terminal entropy. The separator's own influence gets rate K. Debit the root face from these marked reserves once. Descendants see the reduced capacities, so the same child slack is never spent again.

The localized node bound B_X<=4d_X+c_X holds whether X is good or bad: for a bad node, B_X<=c_X+c d_X<=c_X+4d_X; for a good node omit c_X. JS<=2c d_X. Descendant cost is at most (4+2c)Jrem. Therefore

    H(F)<=K J(A)+(C0+1)pi I(g),
    H(F)<=max(K,C0+1) I(F).

This is a single-separator scoped ownership lemma, not permission to charge child influence at every depth. The separator reserve is removed before recursion. For a balanced bent/point-flip selector core with an additional balancing sign, H(g)/I(g)<3, yielding H(F)<8I(F) for independent unbounded L,R,T and even bent dimension k>=4. The whole rare event may have vanishing probability and influence as R,T grow.

The root logarithmic mismatch bill Jminor<=B_X, and the full source allowance satisfies Delta H<=Jminor+3c mu. For the requested complete retained-KL account, all descendant Jminor<=4d. Thus J_tree+terminal<=[4J(A)+Jrem]+(C0+1)pi I(g)<=5J(A)+(C0+1)pi I(g); adding 3c sum mu<=3c J(A) gives full sufficient ledger <=(5+3c)J(A)+(C0+1)pi I(g)<10I(F) for C0<3. Terminal entropy is included.

Remaining universal line: for several nested/shared separators, the sum of these marked one-unit reserves must stay bounded per physical coordinate. The present proof handles one separator only; automatically opening this reserve at every ancestor would reintroduce exactly the prohibited reuse.
