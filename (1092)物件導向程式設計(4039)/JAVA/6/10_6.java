package myProject;

class CCircle{
	protected static double pi = 3.14;
	protected double radius;
	/*
	public CCircle() {
		System.out.print("CCircle() constructor called ");
	}
	public CCircle(double r) {
		radius = r;
		System.out.print("CCircle(double r) constructor called ");
	}
	public void setRadius(double r) {
		radius = r;
		System.out.println("radius="+radius);
	}
	*/
	public void show() {
		System.out.println("area="+pi*radius*radius);
	}
}

class CCoin extends CCircle{
	private int value;
	/*
	public CCoin() {
		System.out.println("CCoin() constructor called ");
	}
	*/
	public CCoin(double r,int v) {
		radius = r;
		value = v;
		System.out.println("CCoin(double r,int v) constructor called ");
	}
	public void setValue(int t) {
		value = t;
		System.out.println("value="+value);
	}
	public void show() {
		System.out.println("radius="+radius+", value="+value);
	}
}


public class myExtend {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//CCoin coin1 = new CCoin();
		CCoin coin = new CCoin(2.0,10);
		//coin1.show();
		coin.show();
	}

}
