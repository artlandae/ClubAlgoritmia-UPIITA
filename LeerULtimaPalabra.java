public class LeerULtimaPalabra {
    public static void main(String[] args) {
        String entrada=("Hola mundo");
        String vector[] = entrada.split(" ");
        int cantidad=0;
        System.out.println(entrada.length());
        for(int i=(entrada.length()-1);i<=0;i--){
            System.out.println(vector[i]);
            if(vector[i]!=" "){
                System.out.println(vector[i]);
                cantidad+=1;
                continue;
            }
            break;
        }
        System.out.println(cantidad);
        }
    
}
