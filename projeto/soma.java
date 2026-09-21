import java.util.Scanner;

public class soma {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        double num1 = scanner.nextDouble();

        System.out.print("Digite o segundo número: ");
        double num2 = scanner.nextDouble();

        double resultado = num1 + num2;

        System.out.printf("A soma de %.2f e %.2f é: %.2f\n", num1, num2, resultado);

        scanner.close();
    }
}
