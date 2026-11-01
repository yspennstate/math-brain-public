from pathlib import Path
import json
with Path('ATTEMPT.md').open('a',encoding='utf8') as out:out.write('''

## Reduction M (proved using Thorisson's shift-coupling theorem)

Let mu be any centered continuous real-path law, and W centered two-sided Wiener law. Let I_R be the Borel sets A of C_0(R) such that theta_t^{-1}A=A for every real t, where theta_t x(s)=x(t+s)-x(t). In the distributional sense allowing an extension, mu admits a finite real random shift to W if and only if

    mu(A)=0 for every A in I_R with W(A)=0.

Necessity is elementary: for a pathwise finite shift R and invariant A, 1_A(theta_R x)=1_A(x), so the probabilities of every invariant event are unchanged by the random shift.

For sufficiency first observe that W is ergodic under the real recentering group: any real-invariant event is in particular invariant under the integer shift, whose ergodicity was proved in Corollary F. Thus W(A) is 0 or 1 for A in I_R. The null-set condition, applied also to complements, implies that mu and W agree on I_R.

To apply the cited ordinary-time shift-coupling criterion to a recentering action, encode a centered path x as the continuous E-valued trajectory Z_x(t)=theta_t x, with E=C_0(R). The map (t,x)->theta_t x is continuous for the compact-open topologies, so x->Z_x is measurable into C(R,E). Its image O consists exactly of trajectories Z satisfying Z(t)=theta_t Z(0) for every t. The equalities at rational t suffice by continuity, so O is Borel; O is invariant under ordinary translation of the parameter t. The encoding is one-to-one with measurable inverse Z->Z(0), and obeys Z_{theta_s x}(t)=Z_x(t+s).

An invariant Borel event H of these E-valued trajectories pulls back to an event in I_R. Conversely, for A in I_R the event O intersection {Z:Z(0) in A} is Borel and invariant under ordinary time translation, with pullback A. Hence the two encoded process laws agree on their invariant sigma field. Thorisson's continuous-path shift-coupling criterion, reproduced as Pitman–Tang Theorem 5.9 on p.19, gives a finite random ordinary time shift of Z_mu with law Z_W. Evaluating at time zero gives theta_R x with law W. This proves sufficiency. QED.

This is a genuine full-path reformulation of the remaining gap, not a solution: the source assumptions have not been proved to exclude every Wiener-null real-shift-invariant event. Replacing I_R by the larger integer-invariant sigma field would add a stronger condition and is not justified for a question permitting arbitrary real shifts. The filling lemma's integer correction is used only after full domination by W has been obtained.
''')
p=Path('CLAIMS.jsonl')
c=dict(problem_id='P0030',claim='A centered continuous path law admits a finite real random shift to two-sided Wiener law on an extension iff it assigns zero probability to every real-recentering-invariant Borel event that is Wiener-null.',status='proved',proof_location='ATTEMPT.md, Reduction M',remaining_gap='No proof that arbitrary source FBM+BBM with decomposability or an independent cut agrees with Wiener law on all such invariant events.',checks=['Necessity from pathwise shift invariance.','Wiener ergodicity implies the null-set condition is equivalent to equality of invariant-event laws.','Centered-window trajectory encoding converts recentering to ordinary time shifts; cited Thorisson criterion applied with its stated full-invariant-sigma-field hypothesis.','Real-invariant and integer-invariant sigma fields explicitly distinguished; auxiliary-randomness scope stated.'])
p.write_text(p.read_text(encoding='utf8')+json.dumps(c,ensure_ascii=False)+'\n',encoding='utf8')
print('saved exact invariant-event reduction')
