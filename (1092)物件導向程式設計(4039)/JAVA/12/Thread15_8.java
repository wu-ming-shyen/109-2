package Thread;
class D{
	private static int sum = 0;
	public synchronized static void add(int n) {
		int temp = sum;
		temp += n;
		try {
			Thread.sleep((int)(1000*Math.random()));
		}catch(InterruptedException e) {}
		sum = temp;
		System.out.println("sum = "+sum);
	}
}
class E extends Thread{
	public void run() {
		for(int i = 1;i<=3;i++) {
			D.add(100);
		}
	}
}
public class Thread15_8 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		E _1 = new E();
		E _2 = new E();
		_1.start();
		_2.start();
	}

}
