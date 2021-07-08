package myProject;
import java.util.Scanner;

class Employee{
	public String Ename;
	public int Salary;
	
	public Employee(String n,int s) {
		Ename = n;
		Salary=s<20000?20000:s<=40000?s:40000;
	}
	
	public static void search(String name,Employee E[]) {
		for(int i=0;i<E.length;i++) {
			if(name.equals(E[i].Ename)) {
				System.out.println("Employee"+(i+1)+" Name:"+E[i].Ename+" Salary:"+E[i].Salary);
			}
		}
	}
	
}

public class myClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Please input number of your employee:");
		int num = scanner.nextInt();
		
		Employee E[] = new Employee[num];
		for(int i=0;i<E.length;i++) {
			System.out.print("Please input Employee"+(i+1)+"'s name:");
			String n = scanner.next();
			System.out.print("Please input Employee"+(i+1)+"'s Salary:");
			int s = scanner.nextInt();
			E[i]=new Employee(n,s);
		}
		String name;
		do {
			System.out.print("Please input search Ename:");
			name = scanner.next();
			Employee.search(name,E);
		}while(!name.equals("0"));
	}

}
