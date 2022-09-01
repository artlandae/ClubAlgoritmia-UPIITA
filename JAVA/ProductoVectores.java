package JAVA;
import java.util.Arrays;
import java.util.Scanner;
class ProductoVector{
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in); 
        
        System.out.println("El tamaño de los vectores a y b : ");
        int cantidad = entrada.nextInt();
        int[] a=new int[cantidad];   
        for (int i=0; i<=cantidad-1;i++){
            System.out.println();
            a[i]=entrada.nextInt();
        }
        int[] b=new int[cantidad];   
        for (int i=0; i<=cantidad-1;i++){
            b[i]=entrada.nextInt();
        }
        int[] producto=new int[cantidad];   
        for (int i=0; i<=cantidad-1;i++){
            producto[i]=a[i]*b[i];
        }

        System.out.println( Arrays.stream(producto).sum());


        
    }

}
