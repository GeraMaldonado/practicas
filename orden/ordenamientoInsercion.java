class Insercion{
    public static void main(String[] args){
        int[] lista = {8,3,1,19,14};
        int temp1, temp2;
        for(int element : lista){
            System.out.print(element+" ");
        }
        System.out.println();
        for(int i = 1; i < lista.length; i++){
            for(int j = i; j > 0; j--){
                if(lista[j]<lista[j-1]){
                    temp1 = lista[j];
                    lista[j] = lista[j-1];
                    lista[j-1] = temp1;
                }else{
                    break;
                }
            }
        }
        for(int element : lista){
            System.out.print(element+" ");
        }    
    }
}
