package Thread;

class B implements Runnable
{
	private String id;
	public B(String str) {
		id = str;
	}
	public void run() {
		for(int i = 0;i<5;i++) {
			try {
				Thread.sleep(1000);
				System.out.println(id+" is running");
			} catch (InterruptedException e) {}
			
		}
	}
}
public class Thread15_3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		B dog = new B("dog");
		B cat = new B("cat");
		Thread t1 = new Thread(dog);
		Thread t2 = new Thread(cat);
		t1.start();
		t2.start();
	}

}
