package myProject;

class CCircle{
	private static double pi = 3.14;
	private double radius;
	
	public CCircle() {
		System.out.print("CCircle() constructor called ");
	}
	public void setRadius(double r) {
		radius = r;
		System.out.println("radius="+radius);
	}
	public void show() {
		System.out.println("area="+pi*radius*radius);
	}
}

class CCoin extends CCircle{
	private int value;
	
	public CCoin() {
		System.out.println("CCoin() constructor called ");
	}
	public void setValue(int t) {
		value = t;
		System.out.println("value="+value);
	}
}


public class myExtend {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CCoin coin = new CCoin();
		coin.setRadius(2.0);
		coin.show();
		coin.setValue(5);
	}

}
