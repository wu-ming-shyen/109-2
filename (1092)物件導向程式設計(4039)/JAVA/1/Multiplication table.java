package B10856012;

public class test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		for(int i=1;i<10;i++) {//Set Multiplicand
			for(int j=1;j<10;j++) {//Set Multiplier
				int ans = i*j;//i*j=ans
				if(ans%2 == 0)System.out.println(i+"*"+j+"="+ans);//ans is Even?
			}
		}
	}

}