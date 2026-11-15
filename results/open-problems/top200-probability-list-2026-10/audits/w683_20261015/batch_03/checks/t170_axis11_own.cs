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
    static string Name(int d, int n) { return Path.Combine(Dir,"t170_d"+d+"_face_after_"+n+".bin"); }
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
        File.WriteAllText(Path.Combine(Dir,"t170_d"+d+"_stage_"+n+".txt"),report+Environment.NewLine);
        Console.WriteLine(report);
        return root;
    }
    static void Main(string[] args) {
        if(args.Length!=3)throw new Exception("usage: d start_stage end_stage");
        int d=int.Parse(args[0]), start=int.Parse(args[1]), end=int.Parse(args[2]);
        if(d!=17 || start<1 || end>11 || start>end)throw new Exception("arguments");
        System.Diagnostics.Process.GetCurrentProcess().ProcessorAffinity=(IntPtr)12;
        string folder="~/brain_workers/w676/T170/inputs";
        string[] lines=File.ReadAllLines(Path.Combine(folder,"axis6_d17_69092f0747019beb.txt"));
        string[] hs=lines[0].Split(new char[]{' '},StringSplitOptions.RemoveEmptyEntries);
        if(int.Parse(hs[0])!=d || int.Parse(hs[1])!=40 || int.Parse(hs[4])!=1)throw new Exception("input header");
        int[] s=Array.ConvertAll(lines[2].Split(new char[]{' '},StringSplitOptions.RemoveEmptyEntries),int.Parse);
        if(s.Length!=10001)throw new Exception("rates");
        ulong[] gammas=Array.ConvertAll(lines[1].Split(new char[]{' '},StringSplitOptions.RemoveEmptyEntries),ulong.Parse);
        string[] extension=File.ReadAllLines(Path.Combine(folder,"axisn_exact_d17_m11_46704de27b8ab538.txt"));
        ulong[] extra=Array.ConvertAll(extension[1].Split(new char[]{' '},StringSplitOptions.RemoveEmptyEntries),ulong.Parse);
        if(gammas.Length!=6 || extra.Length!=6 || extra[0]!=gammas[5] || extension[2]!=lines[2])throw new Exception("extension disagreement");
        ulong[] fullGamma=new ulong[11]; Array.Copy(gammas,fullGamma,6);
        for(int k=1;k<6;k++)fullGamma[k+5]=extra[k];
        Directory.CreateDirectory(Dir);
        for(int n=start;n<=end;n++) {
            ulong[] prior=n==1?null:LoadFace(d,n-1,TailSize(Caps[n-1]));
            Solve(d,n,s,fullGamma[n-1],prior);
        }
    }
}
