from hashlib import sha256
P=421; DEN=1000; TNUM=13
YNUM={(0, 0): 125, (0, 1): 67, (0, 2): -550, (0, 3): -689, (0, 4): -982, (0, 5): -1963, (0, 6): -479, (0, 7): -1851, (0, 8): -868, (0, 9): -33, (0, 10): -1355, (0, 11): -256, (0, 12): -1080, (0, 13): -819, (0, 14): -679, (0, 15): -776, (0, 16): -1379, (0, 17): -1217, (1, 1): -1404, (1, 2): 394, (1, 3): -1824, (1, 4): -1354, (1, 6): -1005, (1, 7): -882, (1, 8): -504, (1, 9): -995, (1, 10): -1074, (1, 11): -334, (1, 12): -993, (1, 13): -388, (1, 14): -463, (1, 15): -646, (1, 16): -1147, (1, 17): -625, (2, 2): -1702, (2, 3): -121, (2, 4): -549, (2, 5): 978, (2, 6): -1365, (2, 7): -398, (2, 8): -792, (2, 9): -737, (2, 10): -1245, (2, 11): 244, (2, 12): -417, (2, 13): -682, (2, 14): 457, (2, 15): -621, (2, 16): -716, (2, 17): -1406, (3, 3): -1400, (3, 4): -250, (3, 6): -701, (3, 7): -585, (3, 8): -1269, (3, 9): -840, (3, 10): -1407, (3, 11): 254, (3, 12): -657, (3, 13): -1626, (3, 14): -651, (3, 15): -806, (3, 16): -678, (3, 17): -853, (4, 4): 108, (4, 5): -1400, (4, 6): -732, (4, 7): 179, (4, 8): -849, (4, 9): -554, (4, 10): -831, (4, 11): 264, (4, 12): -2601, (4, 13): -380, (4, 14): -603, (4, 15): -524, (4, 16): -1280, (4, 17): -1281, (5, 5): -2, (5, 7): -820, (5, 8): -1364, (5, 9): -575, (5, 10): 834, (5, 11): 532, (5, 12): 329, (5, 13): -1522, (5, 14): -997, (5, 15): -1286, (5, 16): -583, (6, 6): -1243, (6, 7): -577, (6, 8): -948, (6, 9): -1045, (6, 10): -65, (6, 11): -753, (6, 12): -999, (6, 13): -2068, (6, 14): -1049, (6, 15): -459, (6, 16): -618, (6, 17): -794, (7, 7): -307, (7, 8): -1127, (7, 9): 2, (7, 10): -16, (7, 11): -1815, (7, 12): -857, (7, 13): -1589, (7, 14): -1801, (7, 15): -1904, (7, 16): -645, (7, 17): 279, (8, 8): -615, (8, 9): -302, (8, 10): -217, (8, 11): -208, (8, 12): 237, (8, 13): -1155, (8, 14): -470, (8, 15): -1934, (8, 16): -1094, (8, 17): -1301, (9, 9): -458, (9, 10): -686, (9, 11): 895, (9, 12): -1321, (9, 13): 1423, (9, 14): -1480, (9, 15): -1363, (9, 16): -528, (9, 17): -843, (10, 10): -1046, (10, 11): 566, (10, 12): -915, (10, 13): 188, (10, 14): 275, (10, 15): -558, (10, 16): -329, (10, 17): -1261, (11, 11): -5502, (11, 12): 467, (11, 13): -803, (11, 14): -2073, (11, 15): 567, (11, 16): -104, (11, 17): 565, (12, 12): 7, (12, 13): 161, (12, 14): -1050, (12, 15): -3391, (12, 16): -727, (12, 17): -1492, (13, 13): -410, (13, 14): -1105, (13, 15): -291, (13, 16): -1161, (13, 17): -1205, (14, 14): -420, (14, 15): 429, (14, 16): -1129, (14, 17): -21, (15, 15): -828, (15, 16): 160, (15, 17): -1884, (16, 16): -150, (16, 17): -1792, (17, 17): 1301}

def legendre(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
QR={a*a%P for a in range(1,P)}
V=sorted(x for x in range(P) if x in QR and (x-1)%P in QR)
n=len(V); assert n==(P-5)//4==104
idx={x:i for i,x in enumerate(V)}
A=[[0]*n for _ in range(n)]; edges=0
for i,x in enumerate(V):
  for j in range(i+1,n):
    if (x-V[j])%P in QR:
      A[i][j]=A[j][i]=1; edges+=1
# S3 vertex orbits ordered by least unseen element.
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
assert len(ovs)==18 and sorted(map(len,ovs))==[2]+[6]*17
# Exact p=421 self-check of the general degree identity used in the report:
# deg_H(x) = (p-15+S_p(x))/8, S_p(x)=sum_u chi(u(u-1)(u-x)).
degs=[sum(row) for row in A]
for i,x in enumerate(V):
  S=sum(legendre(u*(u-1)*(u-x),P) for u in range(P))
  num=P-15+S
  assert num%8==0 and degs[i]==num//8
for O in ovs:
  vals={degs[idx[x]] for x in O}
  assert len(vals)==1
# For p=421 (1 mod 3, 5 mod 8), the unique exceptional orbit is size 2.
small=[O for O in ovs if len(O)<6]
assert len(small)==1 and len(small[0])==2
assert all((x*x-x+1)%P==0 for x in small[0])

# Check certificate dictionary exactly matches all cell pairs containing at least one nonedge.
needed=set()
for i in range(n):
  for j in range(i+1,n):
    if not A[i][j]:
      a,b=cell[i],cell[j]
      if a>b:a,b=b,a
      needed.add((a,b))
assert needed==set(YNUM), (len(needed),len(YNUM),needed-set(YNUM),set(YNUM)-needed)
# Integer K=1000*(13 I-B), with Bii=1, Bedge=1, Bnonedge=YNUM[cell pair]/1000.
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
# Bareiss on integer symmetric matrix: diagonal pivot after stage k is det(K[:k+1,:k+1]).
M=[row[:] for row in K]
prev=1; piv=[]
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
  for i in range(k+1,n):
    for j in range(k+1,n):
      assert M[i][j]==M[j][i]
last=M[n-1][n-1]
assert last>0
piv.append(last)
# Sylvester => K positive definite => 13 I-B positive definite.
# Exact threshold: 13 < (2/3)*sqrt(421), square both positive sides.
gap_num=4*P-9*TNUM*TNUM
assert gap_num==163 and gap_num>0
payload='\n'.join(map(str,piv)).encode()
print('P04-I0101-P421-EXACT-S3-CELL-DUAL-CERTIFICATE=PASS')
print('p=421 n=104 edges=%d s3_orbits=%d nonedge_cell_variables=%d'%(edges,len(ovs),len(YNUM)))
print('t=13 threshold_squared_gap=(4p-9t^2)/9=%d/9'%gap_num)
print('legendre_degree_identity_checked=%d'%n)
print('positive_leading_principal_minors=%d'%len(piv))
print('last_minor_digits=%d'%len(str(last)))
print('pivot_sha256='+sha256(payload).hexdigest())
