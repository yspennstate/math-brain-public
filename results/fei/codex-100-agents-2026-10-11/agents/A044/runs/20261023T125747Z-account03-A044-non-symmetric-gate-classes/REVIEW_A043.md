# A044 independent review of A043 singleton import and depth theorem

Source claim: A043-SINGLETON-IMPORT-BOUNDARY-AND-DEPTH@1.
Statement SHA256: 0f4a98356a94028224020188918ef2d3caef8cc3aff708df442d04cf3814f2f6.
Source run: A043/runs/20261023T123418Z-account03-A043-prime-gate-decomposition.
PROOF.md and CLAIMS.json hashes are pinned in out/SOURCE_RECEIPTS.json.

Outcome: HOLDS for the original mathematical statement. This is an
independent analytic reconstruction by A044, not a formal verification
or registry adoption. Source certificate counts were not rerun or used
as our own counts; our separate implementation has its own frozen domain.

The composition partition is exact: an outer singleton scale enters the
final high sector precisely when its selected child label is high, and
a child singleton scale enters it precisely when the outer label is high.
The remaining coefficient-product rounding is the nonnegative high carry.
These yield the source's T_out,T_in and its exact J_hi recurrence.

At an actual Boolean coordinate, d=E D^2>=t=|E D| and t<=2^-j.
For j>=1, j2^-j<=1/2, hence P_i j<=v_i d/2=I_i/2.
Substitution proves T_out<=ln4 sum a_i M_i/2. For T_in, use
J_1(child)<=ln4 I(child)/2 and
sum b_i Var(child)=2Delta_g-R_g. Combining the two gives EXACTLY
the source's bound

T<=ln4 Delta_F-(ln4/2)[R_g+sum_i((a_i-b_i)Delta_i+a_i R_i)].

Every bracket term is nonnegative. The stated outer-import equality
control uses a fair parity child and fair literal at the actual fair
AND2 root law; its imports have the displayed values.

For the Maj3 tower, Maj3=(x+y+z-xyz)/2 is balanced and prime: its
two-coordinate cofactors have three distinct rows. Each occupied
coefficient at a gate has magnitude 1/2, so unique disjoint expansion
keeps every nonzero final coefficient dyadic. Thus all mantissas,
rounding carries, normalizers and ordinary KL terms vanish. Expected
occupied-node count satisfies k_d=1+(3/2)k_(d-1), while singleton
mass is (3/4)^d and its scale is d. Hence
J_all/ln4=2Delta, J_1/ln4=d(3/4)^d, and the weighted prime-high
source is Delta/2. Subtraction gives exactly
T_total/ln4=(3/2)Delta-d(3/4)^d and the depth-four excess 49/64.
The generating recursion in the source is the same derivation encoded
as a probability-generating polynomial, not an extrapolation.

The source does NOT claim the coefficient ln4 can be renewed at all
depths, and does NOT pay prime J_hi. The new A044 theorem in PROOF.md
supplies a different all-depth bound 4Delta using the ACTUAL lost
singleton entropy and its imported mantissa refund. This extends the
reviewed source; it is not a repair, a refutation, or a change of its
original one-boundary constant. The universal prime-scale gap remains.

The separate A041 paid-sector joint telescope and A042 activation
singleton-bill theorem were read as dependencies/controls. This review
does not independently certify their entire claims or their certificate
counts. No shared source file or global claim status is modified.
