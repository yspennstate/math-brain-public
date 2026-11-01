# Independent scoped reconstruction: A055 stage19 all-block guard

Source: A055/runs/20261023T112023Z-fleet03-A055-extremal-obstruction-referee/PROOF.md,
Sections1--3; read in UTF-8 this stage. Reviewer A005 supplied no repair.

Reconstruct the entropy guard by sampling one actual original assignment
u, then the child Fourier label S under its squared spectrum. Conditional
on u, P(S nonempty)=q_u=4 delta_u(1-delta_u). Encode the indicator first,
then at most d bits for a nonempty label: H(child)<=h2(q_u)+d q_u.
Original reaches give E delta_u=delta, so E q_u<=4p. Jensen gives
E h2(q_u)<=h2(E q_u)<=h2(4p) because k>=3 makes4p<=1/2.
The elementary -(1-x)ln(1-x)<=x and ln2>1/2 give
h2(4p)<=4p(k-2)+8p=4kp. Thus E H(child)<=4p(d+k).
The bound is simultaneous across blocks because it holds for each block
with the SAME upper bound4p(n+k); no union bound is needed.

Positive optimized deficit is at most H pointwise. Also optimized a<=I,
and averaging full physical children leaves exactly I(root)-I_A.
Therefore 0<=N_A*<=B and -B<=S_A*<=K I(root), exactly as stated.
At k=ceil(sqrt(t)) and n=O(t+k), B->0. This conclusion follows without
minimality or a premise about the number of original partitions.

For the paid pair, optimization can only LOWER the explicit reset bank.
Thus its already-negative SAME-bank reserve remains negative, and
N_A*>=-S_A*>D(root). Dividing by the consumed ratio limit gives the
relative-scale lower bound in Section3. No sign is reversed by taking
positive parts. No terminal is omitted.

Verdict: Sections1--3 all-block guard and its conditional application to
the previously reviewed paid-pair embedding HOLD without repair.
The new independent review does not recertify the finite huge-parameter
numbers in Section4 or rerun A055's census. Those are excluded explicitly.
