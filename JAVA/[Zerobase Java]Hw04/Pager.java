public class Pager {
   long totalCount;
   long pageIndex;
   long totalPage;   // 전체 페이지 수
   long pageList = 10;   // 한 페이지에서 보여지는 글의 목록 수
   long rangeSize = 10;   // 한 블럭 당 페이지 수
   int curRange;
   long startPage = 0;
   int endPage = 1;
   int startIndex = 0;
   int prevPage;
   int nextPage;
   
   public Pager(long totalCount) {
      this.totalCount = totalCount;
      this.totalPage = this.totalCount / this.pageList;
      if (this.totalCount % this.pageList > 0) {
         this.totalPage += 1;
      }
      //System.out.println("totalPage is " + this.totalPage);
   }
   
   public String html(long pageIndex) {
      String rtnHtml = "";
      long tempCount = 0;
      
      rtnHtml += "<a href='#'>[처음]</a>\r\n";
      rtnHtml += "<a href='#'>[이전]</a>\r\n\r\n";
      
      if (pageIndex > rangeSize) {
         startPage = rangeSize + 1;
         tempCount = startPage - 1;
         rangeSize = this.totalPage + 1;
      }
      
      for (long i = startPage; i < rangeSize; i++) {
         tempCount++;
         if (pageIndex == tempCount) {
            rtnHtml += "<a href='#' class='on'>"+tempCount+"</a>\r\n";
         }
         else {
            rtnHtml += "<a gref='#'>" + tempCount + "</a>\r\n";
         }
         continue;
      }
      
      rtnHtml += "\r\n<a gref='#'>[다음]</a>\r\n";
      rtnHtml += "<a gref='#'>[마지막]</a>\r\n";
      
      return rtnHtml;
   }
}
