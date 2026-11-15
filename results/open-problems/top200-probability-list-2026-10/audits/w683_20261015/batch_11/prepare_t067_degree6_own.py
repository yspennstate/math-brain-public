"""Adapt only OUR own exact evaluator; do not read an author's executable code."""
from pathlib import Path
from datetime import datetime
from hashlib import sha256
import json
root=Path(__file__).resolve().parent
assert not (root/'checks/t067_degree6_own.cs').exists()
sources={}
for claim in ['T067-UNIVERSAL-FUSION-001','T067-DEGREE6-UPPER-001','T067-DEGREE6-001']:
    p=Path('~/brain_workers/w682/proofs')/(claim+'_v1.md')
    raw=p.read_bytes(); sources[claim]={'path':str(p),'sha256':sha256(raw).hexdigest()}
    (root/'checks'/('frozen_'+claim+'_v1.md')).write_bytes(raw)
s=(root/'checks/t067_degree5_own.cs').read_text(encoding='utf-8')
s=s.replace('Degree5Own','Degree6Own').replace('const int A=161, B=360;','const int A=89, B=218;')
s=s.replace('108UL*(ulong)(B*N)*(ulong)(B*N)','108UL*(ulong)N*(ulong)N')
s=s.replace('108UL*(ulong)B*(ulong)N*(ulong)N','108UL*(ulong)N*(ulong)N')
s=s.replace('"t067_d5_N"','"t067_d6_N"')
s=s.replace('static ulong Likelihood(int k){return checked((ulong)(B-A)*(ulong)N+3UL*(ulong)A*(ulong)k);}', 'static ulong Likelihood(int k){return 3UL*(ulong)k;}')
s=s.replace('static Table Build(bool first){','static Table Build(bool first){\n        if(first)throw new Exception("unit ordered table only");')
s=s.replace('if(c==0)throw new Exception("zero tuple density");','if(c==0)continue;')
edge_code=r'''
    static Table EdgeTable(){
        ulong den=3UL*(ulong)B;
        int[] start=new int[Orbits.Count+1];
        List<ushort> destinations=new List<ushort>();List<ulong> numbers=new List<ulong>();
        StreamWriter dump=N==6?new StreamWriter(Local("edge.tsv"),false):null;
        try {
            for(int i=0;i<Orbits.Count;i++){
                start[i]=destinations.Count;int[] k=Coords(Orbits[i]);
                ulong[] u=new ulong[3],r=new ulong[3];int[] f=new int[3];
                for(int t=0;t<3;t++){
                    u[t]=checked((ulong)(B-A)*(ulong)N+3UL*(ulong)A*(ulong)k[t]);
                    f[t]=(int)(u[t]/den);r[t]=u[t]-(ulong)f[t]*den;
                }
                int missing=N-f[0]-f[1]-f[2],len=0;int[] dest=new int[18];ulong[] num=new ulong[18];
                if(missing<0||missing>2||r[0]+r[1]+r[2]!=(ulong)missing*den)throw new Exception("edge barycenter");
                if(missing==0)Contribution(dest,num,ref len,Index(f[0],f[1],f[2]),den);
                for(int t=0;t<3;t++){
                    int[] q=(int[])f.Clone();ulong w=0;
                    if(missing==1){q[t]++;w=r[t];}
                    if(missing==2){for(int j=0;j<3;j++)if(j!=t)q[j]++;w=den-r[t];}
                    if(w!=0)Contribution(dest,num,ref len,Index(q[0],q[1],q[2]),w);
                }
                ulong total=0;
                for(int j=0;j<len;j++){
                    total=checked(total+num[j]);destinations.Add((ushort)dest[j]);numbers.Add(num[j]);
                    if(dump!=null)dump.WriteLine(i+"\t"+dest[j]+"\t"+num[j]+"\t"+den);
                }
                if(total!=den)throw new Exception("edge row normalization");
            }
        } finally {if(dump!=null)dump.Dispose();}
        start[Orbits.Count]=destinations.Count;
        Console.WriteLine("edge rows="+Orbits.Count+" entries="+destinations.Count+" denominator="+den);
        return new Table{Start=start,Dest=destinations.ToArray(),Num=numbers.ToArray(),Den=den,First=false};
    }
    static ulong[] EdgeStage(ulong[] mass,Table edge,out ulong revealed){
        ulong[] raw=new ulong[Orbits.Count];ulong totalRaw=0;
        for(int i=0;i<mass.Length;i++)for(int j=edge.Start[i];j<edge.Start[i+1];j++)
            raw[edge.Dest[j]]=checked(raw[edge.Dest[j]]+checked(mass[i]*edge.Num[j]));
        ulong[] output=new ulong[mass.Length];ulong total=0;
        for(int j=0;j<mass.Length;j++){
            totalRaw=checked(totalRaw+raw[j]);output[j]=raw[j]/edge.Den;total=checked(total+output[j]);
        }
        if(totalRaw!=checked(S*edge.Den)||total>S)throw new Exception("edge mass normalization");
        revealed=S-total;output[Pure]=checked(output[Pure]+revealed);return output;
    }
'''
s=s.replace('    static Wide Mul64(',edge_code+'\n    static Wide Mul64(')
s=s.replace('(N==6?4:25)','(N==6?4:26)')
s=s.replace('Table first=Build(true),later=Build(false);','Table edge=EdgeTable(),unit=Build(false);\n        if((BigInteger)S*edge.Den>=(BigInteger.One<<64)||(BigInteger)S*S*unit.Den>=(BigInteger.One<<128))throw new Exception("raw accumulation width");')
old='''            ulong[] pair=Stage(child,child,first,out revealed[0]);
            ulong[] triple=Stage(pair,child,later,out revealed[1]);
            ulong[] fourth=Stage(triple,child,later,out revealed[2]);
            ulong[] fifth=Stage(fourth,child,later,out revealed[3]);
            Save(current,fifth,revealed);child=fifth;'''
new='''            ulong[] physical=EdgeStage(child,edge,out revealed[0]);
            ulong[] pair=Stage(physical,physical,unit,out revealed[1]);
            ulong[] fourth=Stage(pair,pair,unit,out revealed[2]);
            ulong[] sixth=Stage(pair,fourth,unit,out revealed[3]);
            Save(current,sixth,revealed);child=sixth;'''
assert old in s;s=s.replace(old,new)
assert 'Table first=Build(true)' not in s and 'zero tuple density' not in s
p=root/'checks/t067_degree6_own.cs';p.write_text(s,encoding='utf-8')
receipt={'at':datetime.now().astimezone().isoformat(),'sources':sources,'evaluator_sha256':sha256(p.read_bytes()).hexdigest(),'based_on':'own frozen degree5 evaluator only','changes':'physical edge once, exact ordered unit fusion, skip null outcomes, fresh independent group laws2+4','next':'compile checked+, N6 four depths then N96 depth26; no author code imported'}
(root/'checks/t067_degree6_preparation_own.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print('Independent degree6 native source and frozen proof bindings prepared.')
