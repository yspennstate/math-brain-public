from pathlib import Path
R=Path(__file__).resolve().parents[1]
def change(path,pairs):
 s=path.read_text(encoding='utf-8')
 for old,new in pairs:
  assert old in s,old
  s=s.replace(old,new)
 path.write_text(s,encoding='utf-8')
change(R/'DERIVATION.md',[
('For every d>=2, log2(d-1)<=d, so0<=rho_i<=Inf_i(f). The physical influence telescope therefore gives','The SHARP pointwise bound is log2(d-1)/d<=2/5 for integer d>=2. Equivalently (d-1)^5<=4^d: verify d=2,3,4,5 by the integer comparisons 1<=16,32<=64,243<=256,1024=1024. For d>=5 the induction step multiplies the left side by (d/(d-1))^5<= (5/4)^5<4, since3125<4096. Equality holds only at d=5. Thus0<=rho_i<=(2/5)Inf_i(f), with optimal pointwise constant attained by the actual Boolean character parity_5. The physical influence telescope therefore gives'),
('sum reach*rho_i<=I_root-E I_leaf.','sum reach*rho_i<=(2/5)(I_root-E I_leaf).'),
('<=CE(P_root,R_root)+2I_root-Var(root)-E I_leaf.','<=CE(P_root,R_root)+(7/5)I_root-Var(root)-(2/5)E I_leaf.'),
('gives rateC+2.','gives rateC+7/5. This is an upper bound for the combined accounting convention, not a claim of its optimal global rate.'),
('independently compares them to lifted scalar marginals;','independently compares them to lifted scalar marginals;'),
('The all-dimensional finite-tree theorem is sections1-4,','FROZEN_SHARPENING.json separately fixes63 exact integer certificates for d2..64 before running code/sharp.py; out/SHARP_RESELECTION.json retains the sharp2/5 guard. The original exhaustive checker deliberately retains its weaker valid <=Inf bounds; the sharper bound is supplied by the independent integer inequality and induction above, not by retroactively relabeling those assertions.\n\nThe all-dimensional finite-tree theorem is sections1-4,')])
change(R/'code'/'finalize.py',[
("'out/PERSISTENCE.json']","'out/PERSISTENCE.json','FROZEN_SHARPENING.json','code/sharp.py','code/upgrade.py','out/SHARP_RESELECTION.json']"),
("'code/witness.py','out/EXACT_RESULTS.json'","'code/witness.py','out/SHARP_RESELECTION.json','out/EXACT_RESULTS.json'"),
('log2(|S|-1)/|S|<=Inf_i.','log2(|S|-1)/|S|<=(2/5)Inf_i, with optimal pointwise constant attained by parity_5.'),
('total reselection entropy<=I_root-E I_leaf.','total reselection entropy<=(2/5)(I_root-E I_leaf).'),
('bill<=CE(P_root,R_root)+2I_root-Var_root-E I_leaf.','bill<=CE(P_root,R_root)+(7/5)I_root-Var_root-(2/5)E I_leaf.'),
('mark reselection <=I_root-E I_leaf','mark reselection <=(2/5)(I_root-E I_leaf)'),
('separately paid reselection entropy at most I_root-E I_leaf','separately paid reselection entropy at most (2/5)(I_root-E I_leaf)'),
('conditional rate C+2','conditional rate C+7/5'),
('mark reselection <= original influence','mark reselection <=2/5 of original influence'),
('separate Shannon reselection invoice and original influence payment.','separate Shannon reselection invoice and original influence payment. The sharp pointwise coefficient2/5 is proved by (d-1)^5<=4^d with an integer induction and actual parity_5 equality; code/sharp.py and out/SHARP_RESELECTION.json check63 frozen integer cases. The original exhaustive checker verifies the weaker <=Inf bound, not the sharpened coefficient.'),
('separately owner-paid mark reselection <=(2/5)(I_root-E I_leaf);','separately owner-paid mark reselection <=(2/5)(I_root-E I_leaf) (sharp pointwise coefficient);'),
('rho=sum_{i in S}P(S)log(d-1)/d is separate and <=Inf_i.','rho=sum_{i in S}P(S)log(d-1)/d is separate and <=(2/5)Inf_i, sharp at parity5.'),
('bill <=rootCE+2I_root-Var_root-EI_leaf.','bill <=rootCE+(7/5)I_root-Var_root-(2/5)EI_leaf.')])
for name in ['WORKLOG.md','LEARNED.md']:
 p=R.parents[1]/name;s=p.read_text(encoding='utf-8')
 s+='\n\n2026-10-23 stage21 sharp-pointwise extension: rho_i<=(2/5)Inf_i, exact at actual parity_5. Integer proof (d-1)^5<=4^d for d2..5 then induction using(5/4)^5<4. Frozen63-case exact integer check PASS. Combined conditional bill improves to rootCE+(7/5)I_root-Var_root-(2/5)E I_leaf; this does not claim optimal global rate or price the initial source.\n'
 p.write_text(s,encoding='utf-8')
print('Sharp proof and finalizer upgraded; rerun finalizer to regenerate protocol files and hashes.')
