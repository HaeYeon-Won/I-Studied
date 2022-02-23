import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
/*
 문제
그림에 보이는 웹브라우저 화면은 자바의 환경 정보를 html의 테이블 구조로 출력한 화면입니다. 아래 조건에
맞게 property.html 파일을 만드는 코드를 작성하세요.
[조건]
자바의 시스템 속성과 파일 저장 코드는 샘플 코드를 참조해 주세요.
출력결과의 파일은 웹브라우저로 확인해서 정상적으로 표시되어야 합니다.
html파일을 작성할 때 테이블에 라인이 표시되도록 head 태그에 style태그 추가(샘플 코드 참조)
*/
public class main {

	public static void main(String[] args) {
		  String html = "";

	        //Table생성용 CSS
	        html += "<head>";
	        html +=     "<meta charset='UTF-8'/>";
	        html +=     "<style>";
	        html +=         "table { border-collapse: collapse; width: 100%; }";
	        html +=         "th, td { border: solid 1px #000; }";
	        html +=     "</style>";
	        html += "</head>";
	        
	        html += "<body>";
	        
	        html += "<div style =\"width:100%; height:50px; line-height:50px;\">";
	        html +=     "<span style=\"font-size:25px; font-weight:bold;\">자바 환경정보</span>";
	        html += "</div>";

	        //Table
	        html += "<table>";
	        html +=     "<thead>";
	        html +=         "<th>키</th>";
	        html +=         "<th></th>";
	        html +=     "</thead>";
	        html +=     "<tbody>";

	        //Table Body 내용 (JAVA 환경 정보)
	        for(Object k : System.getProperties().keySet()){
	            String key = k.toString();
	            String value = System.getProperty(key);
	            html += "<tr>";
	            html +=     "<td>" + key + "</td>";
	            html +=     "<td>" + value + "</td>";     
	            html += "</tr>";
	        }
	        
	        html +=     "</tbody>";
	        html += "</table>";
	        html += "</body>";

	        //파일 생성, 저장
	        try {
	            File file = new File("property.html");
	            BufferedWriter writer = new BufferedWriter(new FileWriter(file));
	            writer.write(html);
	            writer.close();
	        } catch (IOException e) {
	            e.printStackTrace();
	        } finally {
	           System.out.println("create complete. . ."); 
	        }

	    

	}

}
