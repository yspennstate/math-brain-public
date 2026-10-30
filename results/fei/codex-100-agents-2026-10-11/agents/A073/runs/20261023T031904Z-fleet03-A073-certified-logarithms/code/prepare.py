from pathlib import Path
R=Path(__file__).resolve().parents[1];R.joinpath('out').mkdir(parents=True,exist_ok=True)
old=R.parent/'20261023T025235Z-fleet03-A073-certified-logarithms'
s=(old/'code/physical.py').read_text(encoding='utf-8')
shape='''def shape_reference(blocks,order,bits):
 qs=[]
 for block in blocks:
  labels=list(block);q=pointq(labels);alive=True
  for a,y in zip(order,bits):
   if a not in labels:continue
   k=len(labels);labels.remove(a)
   if not alive or not y or k<=2:
    alive=alive and bool(y)
    q=pointq(labels) if alive and len(labels)==1 else {0:F(1)}
    continue
   d=F(1,1<<k);full=sum(1<<j for j in [a]+labels)
   c=q[0];ordinary=q[1<<labels[0]];b=q[full]
   cnew=(c+ordinary)*(1-4*d)**2/(1-4*d+8*d*d)
   anew=4*ordinary;bnew=2*(ordinary+b)
   z=cnew+((1<<len(labels))-2)*anew+bnew
   q={sum(1<<labels[j] for j in range(len(labels)) if mask>>j&1):anew/z for mask in range(1,1<<len(labels))}
   q[0]=cnew/z;q[sum(1<<j for j in labels)]=bnew/z
  if alive and len(labels)>=2:
   full=sum(1<<a for a in labels);u=F(1,1<<len(labels));v=F(1,1<<len(block))
   assert q[full]/q[1<<labels[0]]==1+(1-v)/(7*u)
  qs.append(q)
 return tensor(qs)

'''
s=s.replace('def main():',shape+'def main():')
s=s.replace('[(2,),(3,),(4,),(2,3),(3,3)]','[(2,),(3,),(4,),(2,3),(3,3),(5,)]')
s=s.replace('for k in range(2)','for k in range(3)')
s=s.replace('predicted=quotient(cp,cq,assignment,core.p)','predicted=shape_reference(blocks,order,bits)')
s=s.replace('every distinct data prefix of length0 or1','every ordered distinct data prefix of length0,1,2')
s=s.replace('Two unreset incoming data queries are explicitly excluded.','Sequential unreset prefixes are certified by the three-mass recurrence, not cumulative erasure.')
s=s.replace('failed cumulative-prefix hypothesis falsified in less than60s; preserved in TRANSPORT_OBJECTION.json; repaired application has one incoming data query only','stage18 pilot45 cases595 checks completed in1.50s; this frozen domain adds one width5 root and length2 prefixes, no automatic escalation')
s=s.replace('physical transport objection saved','three-mass recurrence objection saved')
(R/'code/check.py').write_text(s,encoding='utf-8')
print('prepared fixed width<=6 core / <=9 lifted-variable domain')
