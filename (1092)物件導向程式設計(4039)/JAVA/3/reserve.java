package array;

import java.util.Arrays;
import java.util.Scanner;

public class reserve {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		int rank[]=new int[5];
		int sort[]=new int[5];
		for(int i=0;i<rank.length;i++) {
			rank[i]=(int)(Math.random()*1000)+1;
			System.out.println(rank[i]);
		}
		System.out.println();
		sort = Sort(rank);
		for(int i=0;i<rank.length;i++) {
			System.out.println(sort[i]);
		}
		*/
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Please input a string: ");
		String myString = scanner.next();
		
		System.out.println(myString);
		System.out.println(ReString(myString,myString.length()-1));
		
	}
	/*
	public static int[] Sort(int arr[]){
		Arrays.sort(arr);
		return arr;
	}
	*/
	
	public static String ReString(String str,int index) {
		if(index==0) {
			return str.charAt(0)+"";
		}
		char letter = str.charAt(index);
		return letter + ReString(str,index-1);
	}
	
}
