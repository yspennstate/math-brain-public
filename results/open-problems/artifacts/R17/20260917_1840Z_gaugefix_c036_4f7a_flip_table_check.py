#!/usr/bin/env python3
import hashlib, os, sys
import numpy as np
p=sys.argv[1] if len(sys.argv)>1 else 'r17_h8_flip.bin'
N=6419109*30
assert os.path.getsize(p)==N*4
arr=np.memmap(p,dtype='<u4',mode='r')
assert len(arr)==N
hin=hashlib.sha256(); hstrip=hashlib.sha256(); flips=0
chunk=5_000_000
with open(p,'rb') as f:
    while True:
        b=f.read(16<<20)
        if not b: break
        hin.update(b)
for i in range(0,N,chunk):
    a=arr[i:i+chunk]
    flips += int(np.count_nonzero(a & np.uint32(0x80000000)))
    stripped=np.asarray(a & np.uint32(0x7fffffff),dtype='<u4')
    hstrip.update(stripped.tobytes())
orig='c6d12e75e87b7c6b00a95f0c7f3580fa1cdee4996ce690a2f922f7eaeea1fbd1'
flipsha='8578dfef79ef62c36386537e19140053bd44581cb7966b51b71419900f5b2906'
assert hstrip.hexdigest()==orig
assert hin.hexdigest()==flipsha
print('R17 C036 flip-table exact hash check')
print('entries =',N)
print('bytes =',N*4)
print('flip_marked_transitions =',flips)
print('flip_table_sha256 =',hin.hexdigest())
print('stripped_table_sha256 =',hstrip.hexdigest())
print('expected_original_canonical_sha256 =',orig)
print('EXACT_FLIP_TABLE_HASH_CHECK_PASS')
