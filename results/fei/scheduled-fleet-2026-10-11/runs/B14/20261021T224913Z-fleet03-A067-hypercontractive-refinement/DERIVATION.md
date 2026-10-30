# The post-core flag has an actual terminal owner

All Fourier transforms use the uniform cube and all entropies are in bits.
This is a payment for A088's physical post-core family, not a universal FEI proof.

## 1. Exact family and retained terminals

For every integer m>=2 let Y have 2m bits, w one bit and z a sign, and put

    b(Y)=(-1)^(sum_j Y_(2j-1)Y_(2j)),
    G(w,Y,z)=b(Y)+1{w=0,Y=0}(z-1),
    c(w,Y)=b(Y)-2*1{w=0,Y=0}.

The z terminals are the actual Boolean signs b and c, each reached with probability 1/2.
The base b is independent of w. Both terminals remain in every entropy account below.
The all-zero point and all its Y-neighbors have b=+1; flipping that point changes a
nonpivotal edge to a pivotal edge in each of the 2m+1 core directions.
Write N=2^(2m), A=2^-m, delta=1/(2N). Direct physical edge counting gives

    I(b)=m, I(c)=m+(4m+2)delta,
    I_X(G)=[I(b)+I(c)]/2=m+(2m+1)delta,
    I_z(G)=delta, I(G)=I_X(G)+delta.

The two-bit bent Walsh coefficients are (1/2,1/2,1/2,-1/2).
Tensoring gives N coefficients sigma A. Since b(0)=sum beta_T=1,
the positive and negative multiplicities are (N+2^m)/2 and (N-2^m)/2.
Thus H(b)=2m=2I(b). This child has zero surplus at C=2.

## 2. One signed account, with the entire channel paid

Let T be the full core Fourier label (including w), V the z occupancy, and
Hbar=[H(b)+H(c)]/2. The core marginal is the mean of the two actual terminal spectra.
Consequently JS=H(T)-Hbar is their Jensen-Shannon divergence, B=H(V|T), and

    D_z=H(G)-Hbar=B+JS.

The unused actual C=2 child bank is

    S_2=[2I(b)-H(b)]/2+[2I(c)-H(c)]/2=2I_X-Hbar.

The exact cancellation is

    S_2-D_z=2I_X-H(G).                                      (1)

There is no new root quota, omission of the channel, deletion of w, or erased terminal.
The result below proves more than the affordability of B alone:

    B+JS < S_2-delta/4, for EVERY m>=2.                       (2)

In particular H(c)<=2I(c), both children are legitimately certified at the same C,
and H(G)<2I(G)-(9/4)delta. The nonnegative JS and B show from (2) that S_2>0;
as the b bank is zero, the entire payment comes from the weighted c bank.

## 3. The infinite range m>=4

The four cells are the two Fourier occupancies of w and z. In cell (0,0),
coefficients are sigma A-delta, and in the other three cells every coefficient
has absolute value delta. Each cell has N labels. The three small cells have
mass delta/2 each, hence the large cell has mass 1-3delta/2. Conditional entropy
inside every cell is at most log2 N=2m, regardless of its signs or nonuniformity.
The entropy chain rule therefore gives

    H(G)<=2m+eta(1-3delta/2)+3eta(delta/2)
         <=2m+(3delta/2)log2(e)+3delta(m+1),                 (3)

where eta(t)=-t log2 t. The second line uses -x ln x<=1-x for x in (0,1].
There is no asymptotic approximation. Here 0<3delta/2<1, so all logarithms
and denominators used are valid. Also ln2>2/3: the positive atanh expansion
2*(1/3+(1/3)^3/3+...) is strictly greater than 2/3. Hence log2(e)<3/2.
Subtracting (3) from 2I_X=2m+(4m+2)delta gives

    S_2-D_z >=delta[m-1-(3/2)log2(e)]
             >delta(m-13/4)>=3delta/4, m>=4.              (4)

This proves (2) on the whole infinite range. The finite check below supplies
the two boundary dimensions; no numerical extrapolation is used.

## 4. Boundary certificates m=2,3

The exact probability/multiplicity groups for G are

    ((A-delta)^2,(N+2^m)/2), ((A+delta)^2,(N-2^m)/2),
    (delta^2,3N).

For c replace delta by 2delta in the first two amplitudes and append (4delta^2,N).
For T replace those two G probabilities by their sum with delta^2 and append
(2delta^2,N). All three group laws normalize exactly. These formulas retain
all actual labels, including the small informative w rows.

The checker certifies by rational log intervals that

    [2I_X-H(G)]/delta > 1/4, m=2,
    [2I_X-H(G)]/delta > 5/4, m=3.

The interval centers are about 0.2617164 and 1.274424; the inequalities, not the
centers, are the certificates. Each log uses exact range reduction into [1,2],
z=(x-1)/(x+1), the first 28 terms of 2 sum z^(2k+1)/(2k+1), and positive tail
at most 2z^57/[57(1-z^2)]. Division by the positive ln2 interval is outward.
No floating sign is trusted. Independent literal truth tables, integer Walsh
transforms and physical edges reconstruct m=2,3,4 and BOTH terminals.

The separately frozen excluded-boundary guard reconstructs m=1 from all sixteen
physical values and certifies 2I_X-H(G)<0. Thus m>=2 is essential to this exact
no-query-allowance statement; the proof has not discarded an unnecessary hypothesis.

## 5. Same-price spectators, scope and first unpaid line

For any C>=2, S_C=S_2+(C-2)I_X, so the same payment remains valid. If an
independent Boolean spectator q has a genuinely available certification H(q)<=C I(q),
tensoring every actual function with q adds exactly C I(q)-H(q)>=0 to the child
bank, and leaves B, JS and D_z unchanged. Its entire Fourier entropy is retained.
No surplus from q is needed for (2), and no bank is refreshed at a descendant.

This resolves the actual payment on the A088 obstruction, including the channel,
although B/Inf_z diverges. It does not refute A088's local-price obstruction or
A096's loss-only bank threshold five: the latter discards informative core labels
and has different actual terminals. No arbitrary post-core four-branch bank follows.
The unsupported universal line is that inherited, already debited banks retain a
positive version of (1) after a further mixed core/control exposure for arbitrary
Boolean cores. Our proof uses the explicit flat bent base and the nonpivotal
incident edges; it does not claim those hypotheses hold for general cores.

Checks that could fail: Fourier sign multiplicities; physical edge sign at the
edited point; exact terminal normalization; entropy interval direction; cancellation
of the same Hbar; small-m boundary; and accidental reuse of a spectator bank.
The two spectrum/edge implementations and rational intervals test the first six.
The proof retains the spectator in full and needs none of its surplus, addressing
the seventh directly. The analytic proof plus exact boundary certificates is the
rung claimed; a Lean algebra check, if successful, certifies only (1), not (3).
