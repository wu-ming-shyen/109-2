package myPackage;

public class myClass  {  
	public static void Divide(int a[],int n) {
		if(n<2) {return;}
		int m = n/2;
		int l[] = new int[m];
		int r[] = new int[n-m];
		for(int i=0;i<m;i++) {
			l[i] = a[i];
		}
		for(int i=m;i<n;i++) {
			r[i-m] = a[i];
		}
		Divide(l,l.length);
		Divide(r,r.length);
		Merge(a,l,r,l.length,r.length);
	}
	public static void Merge(int a[],int l[],int r[],int ln,int rn) {
		int i=0,j=0,k=0;
		while(i<ln && j<rn) {
			a[k++]=l[i]<r[j]?l[i++]:r[j++];
		}
		while(i<ln) {
			a[k++]=l[i++];
		}
		while(j<ln) {
			a[k++]=r[j++];
		}
		
	}
	public static void show(int a[]) {
		for(int i=0;i<a.length;i++) {
			System.out.print(a[i]+" ");
		}
	}
	public static void main(String args[]){
		int a[] = {5,8,4,2,3,6,1,7,9};
		Divide(a,a.length);
		show(a);
	}
}
