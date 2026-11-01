# Saved analytic result: actual B05 children pay the selector debt at K=4

This is a scoped transport test, not an all-function FEI theorem. All entropy is in bits.
Use the original B05 family: even k>=4, r=2k, delta=2^-k, p=2^-r,
b(x)=(-1)^(x1*x2+...+x(k-1)*xk), b' the sign flip at x=0,
A the all-zero event on r controls, G=1+A(b-1), H=1+A(b'-1),
and f the fair physical selector of G,H. Both signs and both means are retained.
The source gives mu_b=sqrt(delta), mu_b'=sqrt(delta)-2delta,
I(b)=k/2, I(b')=k/2+2k delta, and selector influence d=p delta.

For any u with 0<=mu=Eu<=1, put c=1-mu and F=1+A(u-1).
Its empty coefficient is 1-pc; the empty-data, nonempty-control coefficients
have magnitude pc; every nonempty-data coefficient is p uhat(T), repeated 2^r times.
Writing h(t)=-t log2(t), the exact entropy is

H(F)=p[H(u)-h(mu^2)]+2rp[(1-mu^2)+(1-p)c^2]
      +p(1-p)h(c^2)+h((1-pc)^2).

Since h(t)<=(1-t)/ln2 on [0,1], h(c^2)<=(2mu-mu^2)/ln2,
and h((1-pc)^2)<=2pc/ln2, the last two terms are at most 2p/ln2.
Also (1-mu^2)+c^2=2c. Therefore

H(F)<=p H(u)+4rp c+2p/ln2,
I(F)=p[I(u)+rc],
D_4(F)>=p[4I(u)-H(u)-2/ln2].

For both b,b', the dimensional entropy bound H(u)<=k and I(u)>=k/2
give the PROVED child reserve D_4(G),D_4(H)>=p(k-2/ln2)>=p(k-3).
The latter uses ln2>2/3, supplied by the first term of its atanh series.
This nonnegativity is not an induction assumption.

The baseline physical split identity gives Delta_y H=B_y+JS_y.
Conditioning reduces entropy: B_y<=h2(d); the baseline scalar bound gives
JS_y<=(2/ln2)d. Since h2(d)<=d log2(1/d)+d/ln2,

Delta_y H-4d<=d(3k+3/ln2-4)<=p delta(3k+1/2).

For k>=4, delta(3k+1/2) decreases in k, and its value at k=4 is 25/32<1.
Hence actual average child reserve exceeds the selector deficit:

(D_4(G)+D_4(H))/2-(Delta_y H-4d)
 >=p[k-3-delta(3k+1/2)]>0.

By B06 R2 this is exactly D_4(f)>0. It compensates a selector whose
local entropy/influence ratio grows at least k-O(1), without pretending
that the bad selector step alone is linearly paid. Terminal child entropy
has been included through the ACTUAL child deficits. No dimension bound
for arbitrary cores is asserted.

Nonreuse: replace each child deficit by its complete subtree expansion
before summing payments. An internal deficit then disappears from the ledger;
only terminal deficits and signed node increments remain, each with its
physical reach probability. Keeping a paid internal child deficit as a new
terminal reserve would double count the same descendant terms. For parity
on m variables, D_K=Km and sum over internal node weights of D_K is
K*m*(m+1)/2: an explicit Boolean overcount if internal reserves are added.
