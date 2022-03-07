public class main {

   public static void main(String[] args) {
      // TODO Auto-generated method stub
      long totalCount = 127;
      long pageIndex = 7;
      
      Pager pager = new Pager(totalCount);
      System.out.println(pager.html(pageIndex));
   }

}
