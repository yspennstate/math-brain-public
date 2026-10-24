from hashlib import sha256
P=577; DEN=100; TNUM=16
NUMS=[-47,-51,-69,-101,-94,-112,-61,-55,-109,-107,-41,-55,-98,-68,-50,-113,0,-57,-120,-62,-68,-44,-47,-52,15,-127,-139,-41,-94,-53,-48,-46,-72,-93,-14,-87,-42,-66,-62,-130,-102,-130,-70,-85,-108,-62,-53,-22,-79,-57,-122,-82,-36,-87,-105,-76,-103,-73,-76,-130,-86,-65,-119,4,-59,-93,-112,-75,-88,-137,-99,-108,-14,-143,-113,-85,-87,-43,-10,-60,-99,-123,-61,-76,-104,-71,-89,-47,-138,-56,-98,-142,-10,-100,-160,-110,-60,-10,-73,16,-134,-51,-30,-62,-72,-113,-77,-8,-87,-100,-120,-73,-73,-55,-62,-106,-107,-64,-133,-44,-40,-18,-61,-88,-101,-91,-101,-76,-55,-104,-68,5,-82,-101,-110,-155,-53,-31,-107,-114,-131,-63,-78,-105,-131,-65,-48,-95,-85,-81,-16,-102,-91,-2,-146,-62,-131,-44,-39,-65,-81,26,-150,-96,-113,-26,-79,-164,11,-86,-100,7,-24,-63,-108,-128,-50,-78,-72,-149,-77,-70,-73,-72,-45,-91,-74,-107,-81,-34,-67,-136,-107,-42,1,-113,-76,-91,-90,-74,-135,-78,-75,-51,-98,-80,-87,-41,-95,-100,-32,-89,-78,-88,-164,-54,-89,-72,-9,-191,-12,-42,-48,-108,-122,-91,-106,-75,-84,-76,-70,-68,1,-176,-124,-73,-118,-75,-82,-120,-61,-72,-69,-27,-59,-75,-65,-73,-1,-51,-64,-111,-97,-80,-20,-100,-94,-77,-97,-94,-44,-69,-98,-84,-67,-60,-129,-71,-62,-58,-111,-53,-53,-59,-93,-56,-2,-17,-59,-120,-94,-1,-144,-104,-111,-115,-96,-110,-73,-167,-61,-100,-117,-69,-47,-90,-23,-27,-47,-77,-113,-92,-119,-15,-61,-78,-67,-39,-59,-85,-81,-100]

def legendre(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
QR={a*a%P for a in range(1,P)}
V=sorted(x for x in range(P) if x in QR and (x-1)%P in QR)
n=len(V); assert n==(P-5)//4==143
idx={x:i for i,x in enumerate(V)}
A=[[0]*n for _ in range(n)]; edges=0
for i,x in enumerate(V):
  for j in range(i+1,n):
    if (x-V[j])%P in QR:
      A[i][j]=A[j][i]=1; edges+=1

def inv(x):return pow(x,-1,P)
def orbit(x):
    seen=set(); stack=[x]
    while stack:
      y=stack.pop()
      if y in seen:continue
      seen.add(y);stack.extend(((1-y)%P,inv(y)))
    return seen
cell=[None]*n; ovs=[]; unseen=set(V)
while unseen:
  x=min(unseen); O=orbit(x); assert O<=set(V); a=len(ovs); ovs.append(O)
  for y in O:cell[idx[y]]=a
  unseen-=O
assert len(ovs)==25 and sorted(map(len,ovs))==[2,3]+[6]*23
# Exact p=577 self-check of deg_H(x)=(p-15+S_p(x))/8.
degs=[sum(row) for row in A]
for i,x in enumerate(V):
  S=sum(legendre(u*(u-1)*(u-x),P) for u in range(P))
  num=P-15+S
  assert num%8==0 and degs[i]==num//8
for O in ovs:
  assert len({degs[idx[x]] for x in O})==1
# Exceptional anharmonic orbits: size 2 solves x^2-x+1=0; size 3 is {-1,1/2,2}.
small=sorted((len(O),O) for O in ovs if len(O)<6)
assert [k for k,O in small]==[2,3]
assert all((x*x-x+1)%P==0 for x in small[0][1])
assert small[1][1]=={(-1)%P,pow(2,-1,P),2}

needed=set()
for i in range(n):
  for j in range(i+1,n):
    if not A[i][j]:
      a,b=cell[i],cell[j]
      if a>b:a,b=b,a
      needed.add((a,b))
keys=sorted(needed)
assert len(keys)==len(NUMS)==312
YNUM=dict(zip(keys,NUMS))
# K=100*(16I-B), Bii=1, Bedge=1, and Bnonedge=YNUM[cell-pair]/100.
K=[[0]*n for _ in range(n)]
for i in range(n):
  K[i][i]=DEN*(TNUM-1)
  for j in range(i+1,n):
    if A[i][j]: val=-DEN
    else:
      a,b=cell[i],cell[j]
      if a>b:a,b=b,a
      val=-YNUM[(a,b)]
    K[i][j]=K[j][i]=val
# Exact fraction-free elimination. Successive pivots are leading principal minors.
M=[row[:] for row in K]; prev=1; piv=[]
for k in range(n-1):
  pivot=M[k][k]
  assert pivot>0
  piv.append(pivot)
  for i in range(k+1,n):
    mik=M[i][k]
    for j in range(k+1,n):
      num=M[i][j]*pivot-mik*M[k][j]
      assert num%prev==0
      M[i][j]=num//prev
  prev=pivot
last=M[n-1][n-1]
assert last>0
piv.append(last)
# Sylvester: K positive definite, hence lambda_max(B)<16.
# Exact source threshold: 16 < (2/3)sqrt(577).
gap_num=4*P-9*TNUM*TNUM
assert gap_num==4 and gap_num>0
payload='\n'.join(map(str,piv)).encode()
print('P04-I0101-P577-EXACT-S3-CELL-DUAL-CERTIFICATE=PASS')
print('p=577 n=143 edges=%d s3_orbits=%d nonedge_cell_variables=%d'%(edges,len(ovs),len(YNUM)))
print('orbit_sizes='+','.join(map(str,sorted(map(len,ovs)))))
print('t=16 threshold_squared_gap=(4p-9t^2)/9=%d/9'%gap_num)
print('legendre_degree_identity_checked=%d'%n)
print('positive_leading_principal_minors=%d'%len(piv))
print('last_minor_digits=%d'%len(str(last)))
print('pivot_sha256='+sha256(payload).hexdigest())
