import java.util.Scanner;
public class Comments{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		int number = 0; 
		
        do{
		    System.out.println("Enter a number: ");
		    number = input.nextInt();
		}
		while(number != 9);
		
        System.out.println("You got 9!");
	}
}
