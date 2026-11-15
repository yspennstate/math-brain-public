// Independent degree-five exact posterior upgrading, derived from the proof.
// Reuses our own degree-four design; imports no solver source or tables.
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Numerics;

class Degree6Own {
    const int A=89, B=218;
    const ulong S=4294967296UL;
    static int N=96;
    static Stopwatch Clock;
    static ulong FirstDen {get{return checked(108UL*(ulong)N*(ulong)N);}}
    static ulong LaterDen {get{return checked(108UL*(ulong)N*(ulong)N);}}
    static readonly int[][] Perm={new int[]{0,1,2},new int[]{0,2,1},new int[]{1,0,2},new int[]{1,2,0},new int[]{2,0,1},new int[]{2,1,0}};
    struct Orbit {public int X,Y,Z;public Orbit(int x,int y,int z){X=x;Y=y;Z=z;}}
    struct Wide {public ulong Lo,Hi;public Wide(ulong lo,ulong hi){Lo=lo;Hi=hi;}}
    class Table {public int[] Start;public ushort[] Dest;public ulong[] Num;public ulong Den;public bool First;}
    static List<Orbit> Orbits=new List<Orbit>();
    static int[] Map;
    static int Pure;
    static string Stem {get{return "t067_d6_N"+N+"_own_";}}
    static string Local(string name){return Path.Combine("checks",Stem+name);}
    static void Guard(){
        if(Clock.Elapsed.TotalSeconds>480)throw new TimeoutException("Chunk guard; completed depth checkpoints retained");
        if(Process.GetCurrentProcess().PrivateMemorySize64>900000000L)throw new Exception("Own memory guard900MB");
    }
    static int Code(int x,int y,int z){return (x*(N+1)+y)*(N+1)+z;}
    static int Index(int x,int y,int z){
        if(x<0||y<0||z<0||x+y+z!=N)throw new Exception("invalid grid vertex");
        if(x>y){int q=x;x=y;y=q;}if(y>z){int q=y;y=z;z=q;}if(x>y){int q=x;x=y;y=q;}
        int id=Map[Code(x,y,z)];if(id<0)throw new Exception("orbit missing");return id;
    }
    static void Init(){
        Map=new int[(N+1)*(N+1)*(N+1)];for(int j=0;j<Map.Length;j++)Map[j]=-1;
        for(int x=0;x<=N;x++)for(int y=x;y<=N;y++){
            int z=N-x-y;if(z<y)continue;
            Map[Code(x,y,z)]=Orbits.Count;Orbits.Add(new Orbit(x,y,z));
        }
        if(Orbits.Count!=(N==96?817:7))throw new Exception("orbit census");
        Pure=Index(0,0,N);
    }
    static int[] Coords(Orbit o){return new int[]{o.X,o.Y,o.Z};}
    static ulong Likelihood(int k){return 3UL*(ulong)k;}
    static void Contribution(int[] dest,ulong[] num,ref int length,int id,ulong value){
        if(value==0)return;
        for(int j=0;j<length;j++)if(dest[j]==id){num[j]=checked(num[j]+value);return;}
        if(length>=18)throw new Exception("row destination bound");
        dest[length]=id;num[length]=value;length++;
    }
    static Table Build(bool first){
        if(first)throw new Exception("unit ordered table only");
        int count=Orbits.Count,rows=first?count*(count+1)/2:count*count,row=0;
        ulong den=first?FirstDen:LaterDen;
        int[] start=new int[rows+1];
        List<ushort> destinations=new List<ushort>(rows*5);
        List<ulong> numbers=new List<ulong>(rows*5);
        int[] td=new int[18];ulong[] tn=new ulong[18];
        StreamWriter dump=N==6?new StreamWriter(Local(first?"prefix.tsv":"merge.tsv"),false):null;
        try {
            for(int i=0;i<count;i++){
                int[] left=Coords(Orbits[i]);
                for(int j=first?i:0;j<count;j++){
                    start[row]=destinations.Count;
                    int[] right=Coords(Orbits[j]);
                    int size=right[0]==right[2]?1:(right[0]==right[1]||right[1]==right[2]?3:6);
                    ulong factor=(ulong)(36/size);int length=0;
                    for(int k=0;k<6;k++){
                        int r0=right[Perm[k][0]],r1=right[Perm[k][1]],r2=right[Perm[k][2]];
                        bool duplicate=false;
                        for(int earlier=0;earlier<k;earlier++)
                            if(r0==right[Perm[earlier][0]]&&r1==right[Perm[earlier][1]]&&r2==right[Perm[earlier][2]]){duplicate=true;break;}
                        if(duplicate)continue;
                        ulong z0=checked((first?Likelihood(left[0]):3UL*(ulong)left[0])*Likelihood(r0));
                        ulong z1=checked((first?Likelihood(left[1]):3UL*(ulong)left[1])*Likelihood(r1));
                        ulong z2=checked((first?Likelihood(left[2]):3UL*(ulong)left[2])*Likelihood(r2));
                        ulong c=checked(z0+z1+z2);if(c==0)continue;
                        int f0=(int)((ulong)N*z0/c),f1=(int)((ulong)N*z1/c),f2=(int)((ulong)N*z2/c);
                        ulong e0=(ulong)N*z0-(ulong)f0*c,e1=(ulong)N*z1-(ulong)f1*c,e2=(ulong)N*z2-(ulong)f2*c;
                        int m=N-f0-f1-f2;
                        if(m<0||m>2||e0>=c||e1>=c||e2>=c||e0+e1+e2!=(ulong)m*c)throw new Exception("barycentric residual");
                        if(m==0)Contribution(td,tn,ref length,Index(f0,f1,f2),checked(factor*c));
                        if(m==1){
                            Contribution(td,tn,ref length,Index(f0+1,f1,f2),checked(factor*e0));
                            Contribution(td,tn,ref length,Index(f0,f1+1,f2),checked(factor*e1));
                            Contribution(td,tn,ref length,Index(f0,f1,f2+1),checked(factor*e2));
                        }
                        if(m==2){
                            Contribution(td,tn,ref length,Index(f0,f1+1,f2+1),checked(factor*(c-e0)));
                            Contribution(td,tn,ref length,Index(f0+1,f1,f2+1),checked(factor*(c-e1)));
                            Contribution(td,tn,ref length,Index(f0+1,f1+1,f2),checked(factor*(c-e2)));
                        }
                    }
                    ulong sum=0;
                    for(int k=0;k<length;k++){
                        sum=checked(sum+tn[k]);destinations.Add(checked((ushort)td[k]));numbers.Add(tn[k]);
                        if(dump!=null)dump.WriteLine(i+"\t"+j+"\t"+td[k]+"\t"+tn[k]+"\t"+den);
                    }
                    if(sum!=den)throw new Exception("row normalization "+i+","+j);
                    row++;
                }
                if(i%200==0)Guard();
            }
        } finally {if(dump!=null)dump.Dispose();}
        start[row]=destinations.Count;if(row!=rows)throw new Exception("table row count");
        Console.WriteLine((first?"prefix":"merge")+" rows="+rows+" entries="+destinations.Count+" denominator="+den);
        return new Table{Start=start,Dest=destinations.ToArray(),Num=numbers.ToArray(),Den=den,First=first};
    }

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

    static Wide Mul64(ulong a,ulong b){
        ulong mask=0xffffffffUL,a0=a&mask,a1=a>>32,b0=b&mask,b1=b>>32;
        ulong p00=a0*b0,p01=a0*b1,p10=a1*b0,p11=a1*b1;
        ulong mid=(p00>>32)+(p01&mask)+(p10&mask);
        return new Wide((mid<<32)|(p00&mask),checked(p11+(p01>>32)+(p10>>32)+(mid>>32)));
    }
    static void AddProduct(ulong[] lo,ulong[] hi,int id,Wide p,ulong multiplier){
        Wide low=Mul64(p.Lo,multiplier),high=Mul64(p.Hi,multiplier);
        if(high.Hi!=0)throw new OverflowException("128-bit multiplication");
        ulong top=checked(low.Hi+high.Lo),old=lo[id],sum=unchecked(old+low.Lo);
        ulong resultTop=checked(hi[id]+top+(sum<old?1UL:0UL));
        lo[id]=sum;hi[id]=resultTop;
    }
    static BigInteger Value(Wide p){return ((BigInteger)p.Hi<<64)+p.Lo;}
    static void WideControls(){
        ulong[] vals={0UL,1UL,S-1,S,ulong.MaxValue};
        ulong[] multipliers={0UL,1UL,FirstDen,checked(2UL*FirstDen)};
        int cases=0,overflow=0;
        foreach(ulong a in vals)foreach(ulong b in vals){
            Wide p=Mul64(a,b);if(Value(p)!=(BigInteger)a*b)throw new Exception("Mul64 control");
            foreach(ulong m in multipliers){
                ulong[] lo={ulong.MaxValue},hi={12345UL};
                BigInteger expected=((BigInteger)12345<<64)+ulong.MaxValue+(BigInteger)a*b*m;
                bool mustOverflow=expected>=(BigInteger.One<<128);
                try {
                    AddProduct(lo,hi,0,p,m);
                    if(mustOverflow||Value(new Wide(lo[0],hi[0]))!=expected)throw new Exception("AddProduct control");
                } catch(OverflowException){if(!mustOverflow)throw;overflow++;}
                cases++;
            }
        }
        File.WriteAllText(Local("wide_controls.json"),"{\"cases\":"+cases+",\"expected_overflows_rejected\":"+overflow+",\"complete\":true}\n");
        Console.WriteLine("wide controls="+cases+" expected overflow rejections="+overflow);
    }
    static ulong[] Stage(ulong[] left,ulong[] right,Table table,out ulong revealed){
        if(table.First&&!Object.ReferenceEquals(left,right))throw new Exception("triangular table requires identical laws");
        int count=Orbits.Count,row=0;ulong[] lo=new ulong[count],hi=new ulong[count];
        for(int i=0;i<count;i++){
            for(int j=table.First?i:0;j<count;j++){
                if(left[i]!=0&&right[j]!=0){
                    Wide p=Mul64(left[i],right[j]);ulong factor=table.First&&i!=j?2UL:1UL;
                    for(int k=table.Start[row];k<table.Start[row+1];k++)
                        AddProduct(lo,hi,table.Dest[k],p,checked(factor*table.Num[k]));
                }
                row++;
            }
            if(i%200==0)Guard();
        }
        BigInteger denominator=(BigInteger)S*table.Den;ulong[] mass=new ulong[count];ulong total=0;
        for(int i=0;i<count;i++){
            mass[i]=(ulong)(Value(new Wide(lo[i],hi[i]))/denominator);
            total=checked(total+mass[i]);
        }
        if(total>S)throw new Exception("mass normalization");
        revealed=S-total;mass[Pure]=checked(mass[Pure]+revealed);return mass;
    }
    static ulong Gcd(ulong a,ulong b){while(b!=0){ulong r=a%b;a=b;b=r;}return a;}
    static string Fraction(ulong a,ulong b){ulong g=Gcd(a,b);return (a/g)+"/"+(b/g);}
    static string Signal(ulong[] mass){
        ulong numerator=0,denominator=checked(3UL*(ulong)N*(ulong)N*S);
        for(int j=0;j<mass.Length;j++){
            Orbit o=Orbits[j];int q=3*(o.X*o.X+o.Y*o.Y+o.Z*o.Z)-N*N;
            if(q<0)throw new Exception("negative squared deviation");
            numerator=checked(numerator+checked(mass[j]*(ulong)q));
        }
        return Fraction(numerator,denominator);
    }
    static string Snapshot(int depth){return Local("depth_"+depth.ToString("D3")+".txt");}
    static void Save(int depth,ulong[] mass,ulong[] revealed){
        string name=Snapshot(depth),part=name+".part";
        using(StreamWriter w=new StreamWriter(part,false)){
            w.WriteLine(depth);w.WriteLine(Signal(mass));foreach(ulong value in mass)w.WriteLine(value);
        }
        File.Move(part,name);
        using(StreamWriter w=new StreamWriter(Local("revealed_"+depth.ToString("D3")+".txt"),false))
            foreach(ulong value in revealed)w.WriteLine(Fraction(value,S));
    }
    static ulong[] Load(out int depth){
        string[] files=Directory.GetFiles("checks",Stem+"depth_*.txt");Array.Sort(files,StringComparer.Ordinal);
        if(files.Length==0){depth=0;ulong[] init=new ulong[Orbits.Count];init[Pure]=S;return init;}
        string[] lines=File.ReadAllLines(files[files.Length-1]);depth=int.Parse(lines[0]);
        if(lines.Length!=Orbits.Count+2)throw new Exception("snapshot length");
        ulong total=0;ulong[] mass=new ulong[Orbits.Count];
        for(int j=0;j<mass.Length;j++){mass[j]=ulong.Parse(lines[j+2]);total=checked(total+mass[j]);}
        if(total!=S||Signal(mass)!=lines[1])throw new Exception("snapshot content");
        Console.WriteLine("resume depth="+depth);return mass;
    }
    static void Main(string[] args){
        if(args.Length!=2)throw new Exception("usage: grid(6|96) end_depth");
        N=int.Parse(args[0]);int until=int.Parse(args[1]);
        if((N!=6&&N!=96)||until<1||until>(N==6?4:26))throw new Exception("unsupported parameters");
        Process.GetCurrentProcess().ProcessorAffinity=(IntPtr)12;
        Clock=Stopwatch.StartNew();Init();WideControls();
        int depth;ulong[] child=Load(out depth);Table edge=EdgeTable(),unit=Build(false);
        if((BigInteger)S*edge.Den>=(BigInteger.One<<64)||(BigInteger)S*S*unit.Den>=(BigInteger.One<<128))throw new Exception("raw accumulation width");
        for(int current=depth+1;current<=until;current++){
            ulong[] revealed=new ulong[4];
            ulong[] physical=EdgeStage(child,edge,out revealed[0]);
            ulong[] pair=Stage(physical,physical,unit,out revealed[1]);
            ulong[] fourth=Stage(pair,pair,unit,out revealed[2]);
            ulong[] sixth=Stage(pair,fourth,unit,out revealed[3]);
            Save(current,sixth,revealed);child=sixth;
            Console.WriteLine("depth="+current+" x="+Signal(child)+" seconds="+Clock.Elapsed.TotalSeconds.ToString("F2"));
            if(Clock.Elapsed.TotalSeconds>420){Console.WriteLine("complete depth checkpoint; chunk budget reached");break;}
        }
    }
}
