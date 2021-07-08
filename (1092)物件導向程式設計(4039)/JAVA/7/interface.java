package myProject;

import java.util.Scanner;

interface myShape{
	double PI = 3.14;
	void area();
}

interface myColor{
	void setColor(String str);
}

class R implements myShape,myColor {
	
	protected int width,height;
	protected String color;
	
	public R(int w,int h) {
		width = w;
		height = h;
	}
	
	public void area() {
		System.out.println("area = "+width*height);
	}
	
	public void setColor(String str) {
		color = str;
		System.out.println("color = "+color);
	}
	
}


class C implements myShape,myColor {
	
	protected double radius;
	protected String color;
	
	public C(double r) {
		radius = r;
	}
	
	public void area() {
		System.out.println("area = "+3.14*radius*radius);
	}
	
	public void setColor(String str) {
		color = str;
		System.out.println("color = "+color);
	}
	
}


class T  implements myShape,myColor {
	
	protected int bottom,height;
	protected String color;
	
	public T(int b,int h) {
		bottom = b;
		height = h;
	}
	
	public void area() {
		System.out.println("area = "+bottom*height/2);
	}
	
	public void setColor(String str) {
		color = str;
		System.out.println("color = "+color);
	}
	
}


public class myClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		
		R r = new R(5,10);
		r.setColor("Blue");
		r.area();
		
		C c = new C(2.0);
		c.setColor("Gray");
		c.area();
		
	}

}
