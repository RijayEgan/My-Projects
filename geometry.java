import java.util.Scanner;



public class geometry {
    public static void main(String[] args){
        try (Scanner myObj = new Scanner(System.in)) {
            System.out.println("Hello User! What is your name?");
            System.out.println("Enter Here:");
            String name = myObj.nextLine();
            System.out.println("Hello there " + name);
            System.out.println("What would you like to do " + name);
            System.out.println("1. Area Of Triangle");
            System.out.println("2. Area of Rectangle");
            System.out.println("3. Area of Square");
            int choice = myObj.nextInt();
            if (choice == 1){
                System.out.println("Please enter the Height of the Triangle");
                int heighttriangle = myObj.nextInt();
                System.out.println("Please enter the Base Length");
                int basetriangle = myObj.nextInt();
                int firststeptriangle = (basetriangle * heighttriangle);
                int areaoftriangle = (firststeptriangle / 2);
                System.out.println("Here is the area of your Triangle: " + areaoftriangle);       
            }
            else if(choice == 2){
                System.out.println("Please enter the Height of the Rectangle");
                int heightrectangle = myObj.nextInt();
                System.out.println("Please enter the Base Length");
                int baserectangle = myObj.nextInt();
                int areaofrectangle = (baserectangle*heightrectangle);
                System.out.println("Here is the area of your Rectangle: " + areaofrectangle);
                if (heightrectangle == baserectangle){
                    System.out.println("You could have just used the square option");
                }
            }
            else if(choice == 3){
                System.out.println("Please enter the Height of the Square");
                int heightsquare = myObj.nextInt();
                int areaofsquare = (heightsquare*heightsquare);
                System.out.println("Here is the area of your square: " + areaofsquare);
            }
        }
    }
}
