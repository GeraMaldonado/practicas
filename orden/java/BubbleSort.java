class BubbleSort{
    public static void main(String[] args){
        int[] list = {8,3,1,19,14};
        int temp;
        for(int k : list){
            System.out.print(k+" ");
        }
        System.out.println();
        for(int i=5; i>0; i--){
            for(int j=0; j<(i-1); j++){
                if(list[j]>list[j+1]){
                    temp = list[j];
                    list[j] = list[j+1];
                    list[j+1] = temp;
                }
            }
        }
        for(int k : list){
            System.out.print(k+" ");
        }
    }
}
