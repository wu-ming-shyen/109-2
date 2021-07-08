package myPackage;

import java.util.Scanner;

class Employee {
	
	int Salary;
	String Ename;
	
	void setMM(int sal) {
		if(sal<20000) {
			this.Salary = 20000;
		}
		else if(sal<40000) {
			this.Salary = sal;
		}
		else {
			this.Salary = 40000;
		}
	}
	
}

public class myObject {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner myObj = new Scanner(System.in);  // Create a Scanner object
		Employee employee1 = new Employee();
		Employee employee2 = new Employee();
		
		System.out.print("Enter employee1 name:");
		employee1.Ename = myObj.nextLine();  // Read user input employee1's name
		System.out.print("Enter employee2 name:");
		employee2.Ename = myObj.nextLine();  // Read user input employee2's name
		System.out.print("Enter employee1 salary:");
		int eSalary1 = Integer.parseInt(myObj.nextLine());// Read user input employee1's salary
		System.out.print("Enter employee2 salary:");
		int eSalary2 = Integer.parseInt(myObj.nextLine());// Read user input employee2's salary
		
		employee1.setMM(eSalary1);
		employee2.setMM(eSalary2);
		
		System.out.print(employee1.Ename+" and "+
				employee2.Ename+" average salary is "+
				(employee1.Salary+employee2.Salary)/2);
	}

}
