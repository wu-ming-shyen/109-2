package myProject;

public class p1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try
		{
			int arr[] = new int[5];
			arr[5] = 5;
		}
		catch(ArrayIndexOutOfBoundsException e)
		{
			System.out.println("index out of bound!");
		}
		finally
		{
			System.out.println("this line is always executed!");
		}
		System.out.println("end of main()");
	}

}
