package myProject;

class Caaa{
	protected int num;
	
	public void show() {
		System.out.println("Caaa_num"+num);
	}
}

class Cbbb extends Caaa{
	int num = 10;
	
	public void show() {
		super.num = 20;
		System.out.println("Cbbb_num"+num);
		super.show();
	}
}


public class myExtend {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Cbbb b = new Cbbb();
		b.show();
	}

}
