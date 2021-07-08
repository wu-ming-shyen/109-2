package B10856012;
import java.util.Scanner;//include Scanner class
public class GCD_LCM {
	public static int gcd(int m, int n) {return n == 0 ? m : gcd(n, m % n);}
    public static int lcm(int m, int n) { return m * n / gcd(m, n);}
	public static void main(String[] args) {
		int a=0,b=0;
		Scanner scanner = new Scanner(System.in);
		System.out.println("Input two number");
		a = scanner.nextInt();
		b = scanner.nextInt();
		System.out.printf("GCD of = %d \n", gcd(10, 4));
        System.out.printf("LCM of = %d", lcm(10, 4));
		
	}
}