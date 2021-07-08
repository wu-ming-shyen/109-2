package Thread;

class A extends Thread
{
	private String id;
	public A(String str) {
		id = str;
	}
	public void run() {
		for(int i = 0;i<5;i++) {
			try {
				sleep(1000);
				System.out.println(id+" is running");
			} catch (InterruptedException e) {}
			
		}
	}
}
public class Thread15_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		A dog = new A("dog");
		A cat = new A("cat");
		dog.start();
		cat.start();
	}

}
