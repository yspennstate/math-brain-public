# One paid root increment covers every subsequent history

Full FEI is open. The new certificate concerns one nine-bit Boolean function, with every adaptive physical restriction policy allowed. The all-dimensional implication below is a conditional accounting lemma, not a proof that its admission hypothesis always holds.

## Exact reference and entropy increment

Let b,c be Boolean signs on the same uniform data cube, h a balanced Boolean sign on a disjoint uniform encoder cube, A=(b+c)/2, D=(b-c)/2, delta=E D^2=P(b!=c), G(s,y)=A(y)+sD(y), and F(x,y)=A(y)+h(x)D(y). Write T0=(H(b)+H(c))/2 and Q=B_s(G). All entropies are in bits.

Balance gives hhat(empty)=0. Thus A's coefficients occupy encoder set empty and D's coefficients occupy nonempty encoder sets, without collision. Replacing the selector sector of G by the normalized squared spectrum of h gives the exact identity

    H(F)=H(G)+delta H(h)=T0+Q+JS_s(G)+delta H(h).       (1)

For each data Fourier index put u=Ahat(T), v=Dhat(T), q=u^2+v^2. Omit q=0. Its JS contribution is q phi(z)/ln(2), where z=2uv/q and

    phi(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2.

The even function phi satisfies phi(z)<=1-sqrt(1-z^2) for |z|<=1. On [0,1), the derivative of the difference is z/sqrt(1-z^2)-atanh(z); its derivative is (1-z^2)^(-3/2)-(1-z^2)^(-1)>=0, and both the difference and its first derivative vanish at zero. Continuity handles z=1. Therefore the packet is at most 2min(u^2,v^2)/ln(2). Summing gives JS_s(G)<=2delta/ln(2). Also ln(2)>2/3: its atanh series has first term 2/3 and positive remaining terms. In particular

    H(F)-T0 <= Q+delta(H(h)+2/ln(2)).                 (2)

For h=Maj3, its four occupied Fourier coefficients have squared mass 1/4, so H(h)=2. Hence H(F)-T0<=Q+5delta (strict if delta>0). Every denominator is positive where used; zero packets and delta=0 are treated without division by delta.

Fresh encoder inputs and balance are necessary for (1). For b=1,c=y on one bit, G has entropy 2. A constant encoder h=1 gives F=1 and entropy 0, contradicting (1) if balance is dropped. Taking h=y on that same data coordinate gives F=y and entropy 0, contradicting (1) if freshness is dropped. These are exact Boolean counterexamples to the weakened hypotheses, not counterexamples to FEI.

## The original account, never renewed

At any physical query i on an actual Boolean function g,

    H(g)=B_i(g)+(H(g_+)+H(g_-))/2+JS_i(g), JS_i(g)>=0.   (3)

Indeed the paired parent spectrum is the mean of the two child spectra; entropy concavity gives JS>=0. Fourier amplitudes restrict as a_child(T)=a_parent(T)+epsilon*a_parent(T+i). Conditioning the squared parent spectrum is a different operation.

For any finite adaptive restriction tree, let W be its reach-weighted executed erasure bill and L its expected COMPLETE terminal spectral entropy. Iterating (3) yields W+L<=H(F). This covers arbitrary stopping leaves, all query orders, data/encoder interleavings, and adaptive selection. No coordinate can be queried twice on one path. A randomized policy follows by averaging fixed policies.

Fix an original quota K I0, I0=(I(b)+I(c))/2, and S=K I0-T0. If Q+delta(H(h)+2/ln(2))<=S, then every such history obeys

    S-W+(T0-L)=K I0-W-L>=0.                         (4)

For a prefix v, the potential W_prefix+sum_reach H(g_v) never increases. Its expected decrease is the actual reach-weighted JS. Thus (4) books each executed cost once, releases exactly the original terminal debt, and preserves the opposite sibling even when continuing only one child. It never credits K I(child)-H(child) as a new bank. This is an entropy accounting consequence of a paid root admission; it does not assert that admission is universal. Nonnegativity holds for the expected global account, not necessarily separately for every conditional child with a prescribed allocation.

## The neutral AND3 edit

On six data bits b(y)=1 iff the first three bits are zero; c equals b except c(0)=-1. Both have influence 3/4, delta=1/64, and h is Maj3 on three fresh bits. K=4 gives original quota 3. Exact rational logarithm intervals give

| Quantity | Strict enclosing interval, bits |
| --- | --- |
| T0 | (2333719,2333720)/10^6 |
| S | (666280,666281)/10^6 |
| H(F)-T0 | (110484,110485)/10^6 |
| Q+5delta | (124387,124388)/10^6 |
| S-(Q+5delta) | (541893,541894)/10^6 |
| H(F) | (2444203,2444204)/10^6 |
| 3-H(F) | (555796,555797)/10^6 |

Thus every adaptive physical history, with its complete actual terminal spectra, is paid from this SAME original quota with margin >555796/10^6. An independent character-sum calculation reproduces every one of the root's 512 Fourier coefficients and all nine influences. The checker enumerates all 3^9=19683 labeled restrictions and all 9*3^8=59049 node/query pairs, independently verifying signed phase transport, Parseval, influence telescoping, and (3) with rigorous JS signs. There are 10191 positive-JS and 48858 zero-JS pairs. Equal truth tables are cached, but labeled restrictions are not removed by symmetry.

For direct continuation of the saved NEXT, all 30 ordered distinct data-coordinate pairs are queried before resolving all three encoder bits. Both first-query outcomes and all four complete data-restricted terminal pairs are retained. Every such whole-tree bill plus full terminals leaves more than 670974/10^6 of the original quota. The arbitrary-history result also covers choosing a different second query in each first-query branch; the 30 explicit policies are diagnostics, not an exhaustive enumeration of adaptive trees.

## First unpaid universal step

The actual-reference fixture is closed at every history length, so another depth sweep would repeat paid work. The unproved universal implication is that one can supply, for every Boolean source, an admissible incoming complete reference and a phase-compatible continuation whose initial and subsequent excess cross-entropies are paid by one genuinely unused ancestor account. Replacing terminal H by cross-entropy against arbitrary Q adds D(p_leaf||Q_leaf); (3) does not pay that sum. Nor is Q+delta(H(h)+2/ln(2))<=S known for arbitrary cores. Claiming either from this fixture would reinsert FEI into the admission step. No universal constant improves.
