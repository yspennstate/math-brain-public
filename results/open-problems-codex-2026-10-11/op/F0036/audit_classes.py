from pathlib import Path
p=Path('PROOF.md'); t=p.read_text(encoding='utf8')
a=t.index('By the special-point structure, choose'); b=t.index('For some epsilon>0,',a)
t=t[:a]+'''By Proposition 2.6(iii), choose incoming l in W^l and r in W^r which separate at z. Their ordering just after the meeting is l<r, by the left/right ordering constraint, so l belongs to the left outgoing class and r to the right outgoing class. By Theorem 1.11(a),(b), their extended representatives in these classes agree strongly with these true web paths near z. Theorem 1.12(b) therefore supplies the local outer bounds for eta_1 and eta_2 using these same incoming l,r. '''+t[b:]
t=t.replace('using their outgoing restrictions if necessary','without any assumption about a deterministic starting point at z')
p.write_text(t,encoding='utf8')
