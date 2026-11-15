// Independent exact count-supremum dynamic program from the T170 proof.
// Compile with csc /out:checks\t170_axis_own.exe checks\t170_axis_own.cs
using System;
using System.IO;
using System.Collections.Generic;

class AxisAudit {
    const ulong Scale = 1099511627776UL;
    static readonly int[][] Caps = {
        new int[] {1000},
        new int[] {10000,1000},
        new int[] {1000,100,10},
        new int[] {1000,100,10,10},
        new int[] {1000,100,100,10,1},
        new int[] {1000,100,10,10,1,1},
        new int[] {1000,100,10,10,1,1,1},
        new int[] {1000,100,10,10,1,1,1,1},
        new int[] {1000,100,10,10,1,1,1,1,1},
        new int[] {1000,100,10,10,1,1,1,1,1,1},
        new int[] {1000,100,10,10,1,1,1,1,1,1,1}
    };
    static string Dir = "checks";
    static string Name(int d, int n) { return Path.Combine(Dir,"t170_discrete_d"+d+"_face_after_"+n+".bin"); }
    static int[] Strides(int[] caps) {
        int[] step = new int[caps.Length];
        int x=1;
        for(int k=caps.Length-1;k>=1;k--) {step[k]=x; x=checked(x*(caps[k]+1));}
        return step;
    }
    static int TailSize(int[] caps) {
        int x=1;
        for(int k=1;k<caps.Length;k++) x=checked(x*(caps[k]+1));
        return x;
    }
    static ulong[] LoadFace(int d,int n,int expected) {
        using(var f=new BinaryReader(File.OpenRead(Name(d,n)))) {
            if(f.ReadInt32()!=d || f.ReadInt32()!=n || f.ReadInt32()!=expected) throw new Exception("face header");
            ulong[] v=new ulong[expected];
            for(int i=0;i<expected;i++)v[i]=f.ReadUInt64();
            if(f.BaseStream.Position!=f.BaseStream.Length)throw new Exception("face trailing data");
            return v;
        }
    }
    static void SaveFace(int d,int n,ulong[] a) {
        using(var f=new BinaryWriter(File.Create(Name(d,n)))) {
            f.Write(d);f.Write(n);f.Write(a.Length);
            foreach(ulong x in a)f.Write(x);
        }
    }
    static ulong Solve(int d,int n,int[] s,ulong gamma,ulong[] priorFace) {
        int[] cap=Caps[n-1], step=Strides(cap);
        int size=TailSize(cap);
        if(n>1 && priorFace.Length!=size)throw new Exception("prior face size");
        ulong[] upperC0=new ulong[size], atC0=new ulong[size];
        int[] c=new int[n];
        var validIndices=new List<int>();
        var tails=new List<int[]>();
        for(int idx=size-1;idx>=0;idx--) {
            int q=idx;
            int[] tail=new int[n]; tail[0]=1;
            bool good=true;
            for(int k=1;k<n;k++) {
                tail[k]=q/step[k]; q%=step[k];
                if(tail[k]>0 && tail[k-1]==0)good=false;
            }
            if(good) {validIndices.Add(idx);tails.Add(tail);}
        }
        int[] nextCap=n<11?Caps[n]:null;
        int[] nextStep=n<11?Strides(nextCap):null;
        ulong[] faceForNext=n<11?new ulong[TailSize(nextCap)]:null;
        long valid=0, boundary=0;
        for(int first=cap[0];first>=1;first--) {
            if(first%20==0)Guard();
            c[0]=first;
            for(int vi=0;vi<validIndices.Count;vi++) {
                int idx=validIndices[vi];
                for(int k=1;k<n;k++)c[k]=tails[vi][k];
                valid++;
                bool isFace=first==cap[0];
                ulong answer=isFace?gamma:ulong.MaxValue;
                if(n>1) {
                    for(int k=1;k<n;k++) {
                        if(c[k]==cap[k]) {
                            isFace=true;
                            if(priorFace[idx]==0)throw new Exception("empty tail face");
                            if(priorFace[idx]<answer)answer=priorFace[idx];
                        }
                    }
                }
                if(isFace) boundary++;
                else {
                    ulong numerator=Scale;
                    ulong total=(ulong)c[n-1];
                    for(int k=0;k<n;k++) {
                        ulong rate=(ulong)s[c[k]];
                        if(k>0 && c[k-1]>c[k])rate+=(ulong)(c[k-1]-c[k]);
                        total=checked(total+rate);
                        if(rate==0)continue;
                        ulong child=k==0?upperC0[idx]:atC0[idx+step[k]];
                        if(child==0)throw new Exception("uncomputed child at stage "+n+" state "+first+"/"+idx+" k="+k);
                        numerator=checked(numerator+checked(rate*child));
                    }
                    if(total==0)throw new Exception("zero denominator");
                    answer=checked((numerator+total-1)/total);
                }
                // Suppressing slab 0 is valid at every state with c1>0,
                // not only when a later coordinate reaches its box face.
                if(n>1 && c[1]>0) {
                    if(priorFace[idx]==0)throw new Exception("empty available tail bound");
                    if(priorFace[idx]<answer)answer=priorFace[idx];
                }
                atC0[idx]=answer;
                if(n<11 && first<=nextCap[1]) {
                    bool inSubset=true;
                    int mapped=first*nextStep[1];
                    for(int k=1;k<n;k++) {
                        if(c[k]>nextCap[k+1]) {inSubset=false;break;}
                        mapped+=c[k]*nextStep[k+1];
                    }
                    if(inSubset)faceForNext[mapped]=answer;
                }
            }
            ulong[] swap=upperC0;upperC0=atC0;atC0=swap;
        }
        ulong root=upperC0[0];
        if(n<11)SaveFace(d,n,faceForNext);
        string report="d="+d+" n="+n+" root_units="+root+" valid="+valid+" face="+boundary+" size="+size;
        File.WriteAllText(Path.Combine(Dir,"t170_discrete_d"+d+"_stage_"+n+".txt"),report+Environment.NewLine);
        Console.WriteLine(report);
        return root;
    }
    static System.Diagnostics.Stopwatch Clock;
    static void Guard() {
        if(Clock.Elapsed.TotalSeconds>480)throw new TimeoutException("Completed stage faces retained; chunk480s guard");
        if(System.Diagnostics.Process.GetCurrentProcess().PrivateMemorySize64>900000000L)throw new Exception("Memory guard900MB");
    }
    static int DigitalSum(int n) {
        int result=0;
        while(n>0) {
            int h=1,bits=0;while(h<=n/2){h*=2;bits++;}
            result+=bits*(h/2)+(n-h);n-=h;
        }
        return result;
    }
    static void FiniteBoundary(int[] rates) {
        int[] f=new int[10001];long checks=0;int minSlack=int.MaxValue;
        for(int n=0;n<=10000;n++) {
            f[n]=DigitalSum(n);
            if(rates[n]!=30*n-2*f[n])throw new Exception("Independent digital-block sum/rate mismatch");
        }
        for(int n=2;n<=10000;n++)for(int b=1;b<=n/2;b++) {
            int slack=f[n]-f[n-b]-f[b]-b;
            if(slack<0)throw new Exception("Hypercube split inequality");
            if(slack<minSlack)minSlack=slack;checks++;
        }
        if(checks!=25000000L)throw new Exception("Incomplete finite split coverage");
        File.WriteAllText(Path.Combine(Dir,"t170_d16_boundary_own.json"),
          "{\"complete\":true,\"checked_splits\":"+checks+",\"minimum_slack\":"+minSlack+",\"f10000\":"+f[10000]+",\"rate10000\":"+rates[10000]+"}\n");
        Console.WriteLine("Finite split PASS checks="+checks+" f10000="+f[10000]+" rate10000="+rates[10000]);
    }
    static void Main(string[] args) {
        if(args.Length!=2)throw new Exception("usage: start_stage end_stage");
        int d=16,start=int.Parse(args[0]),end=int.Parse(args[1]);
        if(start<1||end>11||start>end)throw new Exception("arguments");
        System.Diagnostics.Process.GetCurrentProcess().ProcessorAffinity=(IntPtr)12;
        Clock=System.Diagnostics.Stopwatch.StartNew();
        string[] lines=File.ReadAllLines(Path.Combine(Dir,"t170_d16_discrete_inputs_own.txt"));
        if(lines.Length!=3||lines[0]!="16 40 11 10000 1")throw new Exception("Own input header");
        ulong[] gammas=Array.ConvertAll(lines[1].Split(' '),ulong.Parse);
        int[] rates=Array.ConvertAll(lines[2].Split(' '),int.Parse);
        if(gammas.Length!=11||rates.Length!=10001)throw new Exception("Own input dimensions");
        FiniteBoundary(rates);
        for(int n=start;n<=end;n++) {
            ulong[] prior=n==1?null:LoadFace(d,n-1,TailSize(Caps[n-1]));
            Solve(d,n,rates,gammas[n-1],prior);
            Console.WriteLine("complete_stage="+n+" seconds="+Clock.Elapsed.TotalSeconds.ToString("F2"));
            if(Clock.Elapsed.TotalSeconds>420){Console.WriteLine("Complete-stage checkpoint; resume next stage");break;}
        }
    }
}
