package B10856012;

import java.lang.reflect.Array;
import java.util.*;

class student implements Comparable<student>{
	protected String name;
	protected int score;
	protected int rank;
	public student(String n, int s) {
		this.name = n;
		this.score = s;
	}
	public int compareTo(student o) {
		return Integer.compare(this.score,o.score);
	}
	public static void setRank(student a[]) {
		int r = 1;
		a[0].rank = r;
		int length = Array.getLength(a);
		for(int i = 1;i < length;i++) {
			a[i].rank = a[i].score!=a[i-1].score ? ++r : r;
		}
	}
	public static int search(student a[], int f) {
        int l = 0; 
        int r = Array.getLength(a) - 1; 

        while(l <= r) { 
            int m = (l+r) / 2; 
            if(a[m].rank < f) 
                l = m+1; 
            else if(a[m].rank > f) 
                r = m - 1; 
            else {
            	while(a[m-1].rank == f) {
            		m--;
            	}
            	return m;
            }
        } 

        return -1; 
    }
	public static void allFind(student a[],int f) {
		int length = Array.getLength(a);
		if(f >= 0) {
			do {
				student.showSearch(a[f]);
			}while(f < length-1 && a[++f].rank == 25);
		}
		else {
			System.out.printf("沒有這個名次!");
		}
	}
	public static void show(student a[]) {
		for(int i = 0;i < a.length;i++) {
			System.out.print(String.format("%-4s",a[i].name));
			System.out.printf("%3d ",a[i].score);
			System.out.printf("%3d\n",a[i].rank);
		}
		System.out.printf("-----------\n");
	}
	public static void showSearch(student o) {
		System.out.printf("學生學號:%-4s",o.name);
		System.out.printf("學生分數:%d ",o.score);
		System.out.printf("學生排名:%d\n",o.rank);
		System.out.printf("-----------------------------------\n");
	}
	
}

public class mainClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		student students[] = new student[50];
		int length = Array.getLength(students);
		for(int i = 0;i < length;i++) {
			students[i] = new student("S"+(i+1),(int)(Math.random()*100));
		}
		Arrays.sort(students,Collections.reverseOrder());
		student.setRank(students);
		student.show(students);
		int find = student.search(students, 25);
		student.allFind(students,find);
	}

}
