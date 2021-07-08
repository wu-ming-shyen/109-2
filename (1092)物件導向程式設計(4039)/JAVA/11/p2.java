package myProject;

public class p2 {

	public static void o(int a,int b) throws ArithmeticException
	{
		int c = a/b;
		System.out.println(a+"/"+b+"="+c);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try
		{
			o(4,0);
		}
		catch(ArithmeticException e)
		{
			System.out.println(e+" throwed");
		}
	}

}
