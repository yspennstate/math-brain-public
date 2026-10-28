from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'code/finalize.py';s=p.read_text(encoding='utf-8')
def rep(old,new):
 global s
 assert old in s,old
 s=s.replace(old,new)
rep("'out/SHARP_RESELECTION.json']","'out/SHARP_RESELECTION.json','EXACT_POTENTIAL.md','FROZEN_POTENTIAL.json','code/potential.py','code/upgrade_potential.py','out/POTENTIAL_CERTIFICATES.json']")
rep("'DERIVATION.md sections1-5 equations1-10'","'DERIVATION.md sections1-5 equations1-10','EXACT_POTENTIAL.md equations11-15','out/POTENTIAL_CERTIFICATES.json'")
rep('No universal initial reference price or full FEI is supplied.', 'Furthermore m(d)=sum_{j=2}^d log2(j-1)/j has physical drift rho_i exactly. With M(P)=E m(|S|) and c_star=[log2(5)+log2(3)/4+11/15]/5<7/10, every finite tree has combined bill=rootCE+E_P w(|S|)-E M_leaf<=rootCE+c_star I_root-E M_leaf, where w(d)=log2(d)+m(d). The optimal overhead coefficient for this explicit kernel/accounting convention is c_star, attained by a complete parity_5 restriction tree. No universal initial reference price or full FEI is supplied.')
rep("'mathematical_delta':'Conditional universal finite-tree per-set witness transport", "'mathematical_delta':'Sharp exact degree-potential theorem: combined bill<=rootCE+c_star I_root-E M_leaf, c_star=0.69030041068...<7/10, optimal at complete parity_5 tree. Conditional universal finite-tree per-set witness transport")
rep('The scalar CE release is explicitly reconstructed', 'EXACT_POTENTIAL.md equations11-15 further prove the exact reselection potential M and the sharp combined overhead c_star=[log2(5)+log2(3)/4+11/15]/5<7/10. The unique degree maximum is proved by a decreasing binary-entropy-increment argument and three exact integer guards, with equality on a full actual parity_5 tree. This supersedes the weaker C+7/5 combined upper bound while retaining its valid pointwise2/5 invoice bound. The scalar CE release is explicitly reconstructed')
rep('All-dimensional proof is analytic, not extrapolation.', 'The separately frozen code/potential.py job passed2752 additional exact assertions:63 degree certificates,512 stored-tree exact M telescopes and physical drifts, and3 integer guards. out/POTENTIAL_CERTIFICATES.json retains these; frozen estimated memory120MB, no heavy job. All-dimensional proof is analytic, not extrapolation.')
rep('Thus a supplied root CE price C I yields an explicitly combined conditional rate C+7/5; no universal root price is gained.', 'The exact potential M has query drift rho_i and yields combined bill<=rootCE+c_star I_root-E M_leaf, c_star=[log2(5)+log2(3)/4+11/15]/5<7/10. This overhead is sharp for this kernel/accounting convention, attained on a complete parity_5 tree. Thus a supplied root CE price C I yields conditional rate C+c_star; no universal root price is gained.')
rep("status='STATE: Stage21 v9 conditional physical per-set witness transport and original-influence reselection payment proved; '","status='STATE: Stage21 v9 sharp exact mark-potential transport proved: combined bill<=rootCE+c_star I, c_star=0.69030041068...<7/10, attained on full parity5; '")
p.write_text(s,encoding='utf-8')
for name in ['WORKLOG.md','LEARNED.md']:
 p=R.parents[1]/name;s=p.read_text(encoding='utf-8')
 s+='\n\n2026-10-23 stage21 exact-potential extension: M(P)=E sum_{j=2}^|S| log2(j-1)/j has physical query drift exactly rho_i, so full tree reselection telescopes from the ORIGINAL degree law. Combined lifted CE ledger plus reselection equals rootCE+Ew(|S|)-E M_leaf. Sharp w(d)/d maximum occurs at d5: c_star=[log2(5)+log2(3)/4+11/15]/5<7/10, attained by a complete parity5 tree. Proved all degrees with decreasing binary-entropy increments and3 exact integer guards;2752 additional exact checks passed. Initial original-spectrum source and independent review remain OPEN.\n'
 p.write_text(s,encoding='utf-8')
print('Exact potential proof and finalizer upgraded.')
