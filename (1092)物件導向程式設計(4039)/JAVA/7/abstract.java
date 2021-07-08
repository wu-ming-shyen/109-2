package myProject;

import java.util.Scanner;

abstract class Shape {
	
	protected String color;
	
	public void setColor(String str) {
		color = str;
	}
	
	public abstract void show();
	
}

class R extends Shape {
	
	protected int width,height;
	
	public R(int w,int h) {
		width = w;
		height = h;
	}
	
	public void show() {
		System.out.println("color = "+color+",	"+"area = "+width*height);
	}
	
}


class C extends Shape {
	
	protected double radius;
	
	public C(double r) {
		radius = r;
	}
	
	public void show() {
		System.out.println("color = "+color+",	"+"area = "+3.14*radius*radius);
	}
	
}


class T  extends Shape {
	
	protected int bottom,height;
	
	public T(int b,int h) {
		bottom = b;
		height = h;
	}
	
	public void show() {
		System.out.println("color = "+color+",	"+"area = "+bottom*height/2);
	}
	
}


public class myClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		
		R r = new R(5,10);
		r.setColor("Yellow");
		r.show();
		
		C c = new C(2.0);
		c.setColor("Green");
		c.show();
		
	}

}
