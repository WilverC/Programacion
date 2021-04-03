import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Exceptions_uno {
	public static void main(String[] args) throws FileNotFoundException {
		File file = new File("example.txt");
		Scanner readFile = new Scanner(file);
	}
}