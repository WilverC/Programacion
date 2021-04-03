
public class Cadenas{
    public static void main(String args[]){
        int aNumber = 9;
        double aDouble = 9.5;
        String text = "Hi";
        String blank = " ";
        String astring = "there";
        String hithere = text + blank + astring;
        
        System.out.println(text);
        System.out.println(text + blank + astring);
        System.out.println("Hi" + " " + "there");
        System.out.println(hithere);
        System.out.println("My numbers " + aNumber + ", " + aDouble);
    }
}