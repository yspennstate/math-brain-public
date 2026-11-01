# Independent review of A061 fixed-root prefix obstruction

Verdict: HOLDS unchanged. The direct exact audit completed with 30,547 primary
assertions PASS; its certificate is out/A061_AUDIT.json.
No new repair is supplied and A064 is not a contributor to the source version.

I reconstructed the field calculation using additive character orthogonality.
For the exceptional relation x=ab, the Fourier sum over x fixes its character
to chi(gamma ab); summing b vanishes unless its coefficient is zero. At gamma=0
this leaves the single coefficient selected by the nontrivial additive psi(a).
At gamma!=0 it leaves a unique a, with magnitude q^-2. Subtracting twice the
exceptional indicator from psi gives one coefficient 1-2/q and (q-1)q^2
coefficients of magnitude 2/q^2, with no empty coefficient. This independently
establishes the support sizes and H_2=5; no floating extrapolation is used.

The inner bent carrier is a four-atom uniform spectrum with a parity shear.
Its two physical mask influences and every sheared core influence are 1/2.
The selector children have disjoint core spectral supports (empty versus the
balanced field core), so the actual selector erasure credit at the uniform
reference is zero. Keeping the fair extension on the complement of BOTH
supports gives prediction (1/(2q),1-1/(2q)). On positive child atoms the
normalized inherited reference has constant density, giving K_G=2l-1 and
K_H=3l-H_l+log r. These calculations use the whole normalized reference;
discarding its source-zero part would change r and invalidate the proof.

The fresh independent bent pair has a positive uniform four-atom spectrum.
Its common physical ordinary kernel is the core kernel on each of those atoms,
including the zero-row extension. Thus ordinary history, actual prediction,
signed E, O and K are exactly preserved; the later protected pivot has E=O=0.
The full product KL after that pivot is 3l in the G branch and 3l-H_l in H.
Consequently BOTH signed debits are positive: l+1 and -log r. Their mean is
B_l=(l+1-log r)/2. Resetting all children and stopping attains that bill,
whereas any later inherited-only continuation cannot increase its funding
need. The full entropy at that stopping cut is 2+H_l/2. The claimed lower
bound does not apply to every prescribed continuation or every order.

For the supplied SAME original S=6l+4-H_l/2, the already booked K=3l-1-H_l/2
is strictly below S/2. Since r>=7/8 and 8^4<2*7^4, B_l<l/2+5/8.
Since H_l<=3l, S/8>=9l/16+1/2; the latter exceeds l/2+5/8 for l>2,
and equality at l=2 is harmless because the previous inequality is strict.
Hence B_l<S/8 and S-omega-K-B_l>S/8 whenever omega<=S/4. This accounts for
the old debit, initial KL, and new reserve without changing the owner.

The direct audit uses the ACTUAL 11-bit Boolean truth table at l=2, an
independently inherited A064 integer FWHT plus physical-edge influence check,
and actual normalized kernel transport. It compares full root H,I,K, both
physical predictions, both erasure credits, all four terminal product KL and H,
the exact required reserve and old-quarter remainder. Four proper influence-1/2
ordinary queries after actual product installation check the continuation claim.
Only own code is executed. Source statement/proof hashes and exact counts are
saved separately; the source payload is preserved with this review appended.
