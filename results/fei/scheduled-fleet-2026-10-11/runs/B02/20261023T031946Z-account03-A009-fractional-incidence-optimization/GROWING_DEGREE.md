# Pay the inherited dense transfer for growing deleted degree

Let4<=a<=b, let H be ANY labelled bipartite deletion graph with maximum degree at most d,0<=d<=a/2, and set G=K_(a,b) minus H. All original surviving positive edge primes, both endpoint orders, actual rarity1/4 and one fixed lambda=1/b are retained. Let C be the complete original nonempty-conditioned all-partition queue cost under the actual Boolean squared spectrum. Write I for the actual physical influence. No vertex is isolated. Independently reconstructed A006's dense transfer is

    C < (91/8) I +2J log2 b,                            (1)

where J is the physical boundary influence of the exceptional event E: both active sides are nonempty and every active cross-pair lies in H. The following payment applies to the SAME J and reference:

    C/I < 91/8 + [2 b^2 2^(2d-b)]/[1-2^(-(b-d))].      (2)

In particular C<22I whenever d<=a/4, uniformly over ALL deleted graphs and every dimension. More generally C<15I in the exact parameter regime a^2 4^d<=2^a. This permits d to grow to approximately a/2-log2 a; no asymptotic approximation is used in the stated hypothesis. These are complete coding-mechanism bounds, not new FEI class novelty or optimal-weight assertions.

## Count physical exceptional configurations without squaring edge count

For a configuration in E let nonempty active sets X,Y satisfy X cross Y subset H. Anchor it at the FIRST active left vertex i. There are at most a anchors and at most2^d-1 possible nonempty Y within N_H(i). For each fixed Y choose y in Y: every possible X lies in N_H(y), which has at most d vertices, and must contain i. There are at most2^(d-1) such X. The first-anchor condition only reduces this number. Thus, for d>=1,

    e=|E|<=a(2^d-1)2^(d-1)<=a2^(2d-1).                (3)

For d=0,E is empty and J=0. This count uses BOTH degree bounds; a one-sided degree assumption cannot bound the number of X choices. There are no invented spectral laws: e counts actual uniform Boolean inputs. Since each point has at most n=a+b incident boundary edges,

    J <=2n e 2^(-n) <= an2^(2d-a-b).                   (4)

The factor two converts undirected cube boundary edges to physical flip probabilities. The Dirichlet energy of the actual perturbation f_G-f_complete=-2*1_E is exactly J, as in A006's transfer; no energy budget is renewed.

If all other left bits are zero and at least one of a vertex's surviving right neighbors is one, that vertex is pivotal. Its surviving degree is at least b-d. Therefore

    I>=2a2^-a[1-2^(-(b-d))]>0.                         (5)

Every denominator is positive, since b-d>=b/2>=2. Combining(4),(5), n<=2b and log2 b<=b gives

    J log2 b/I <= [b^2 2^(2d-b)]/[1-2^(-(b-d))].       (6)

Both sides of G have at least half their possible surviving neighbors, so the hypotheses of(1) hold. Substitute(6) ONCE into(1) to obtain(2). This keeps the original D=(1+1/(4b))^|G|-1, actual singleton-label sums, original nonempty root rarity, generic forests, rank/count/subset factors and posterior output ambiguity from the inherited complete transfer.

## Two dimension-independent regimes

If d<=a/4, then b-d>=3 and b^2 2^(2d-b)<=b^2 2^(-b/2)<=9/2. For the last inequality square both positive sides: b^4/2^b<=81/4. Check b=4,5,6, then advance by two using(b+2)^2<=2b^2 for b>=5 (the difference is b^2-4b-4>=1). Both parity subsequences are covered, with b=4 isolated. Hence

    C/I <91/8+72/7=1213/56<22.                        (7)

If a^2 4^d<=2^a, then b^2 2^(2d-b)<=(b/a)^2 2^(a-b)<=1. Put h=b-a>=0. Since a>=4, the last ratio is at most(1+h/4)^2 2^-h; it starts at one and has successive ratio at most25/32. Also b-d>=2, so the denominator in(6) is at least3/4. Thus

    C/I <91/8+8/3=337/24<15.                          (8)

No bound is inferred from finite enumeration. Exact finite cases validate the physical count, original queue premise, factors in the Dirichlet identity, the two parity inductions and endpoint d=0; the written inequalities prove every parameter case.

## Exact remaining line

This pays the growing-degree bill only in the stated regimes. HALF_DENSITY_OBSTRUCTION.md shows that Jlog b itself cannot be paid universally by I even with half-density and the same natural prime reference. Full FEI remains OPEN. Beyond these regimes the shortest route is to replace the coarse joint-J logarithm by sector-sensitive actual occupation or component-compatible reference mass, retaining the SAME reference and its complete output ambiguity; another universal claim Jlog b<=KI would be false.
