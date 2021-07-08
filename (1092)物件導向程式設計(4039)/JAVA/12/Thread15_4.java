package Thread;
class C extends Thread
{
	private String id;
	public C(String str) {
		id = str;
	}
	public void run() {
		for(int i = 0;i<5;i++) {
			try {
				sleep((long)(1000*Math.random()));
				System.out.println(id+" is running");
			} catch (InterruptedException e) {}
			
		}
	}
}
public class Thread15_4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		C dog = new C("dog");
		C cat = new C("cat");
		dog.start();
		cat.start();
	}

}
