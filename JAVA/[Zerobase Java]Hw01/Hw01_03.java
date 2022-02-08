/*
다음 글은 “제19대 대통령 취임사”의 영문 문장이다.(자료제공)
문장의 각 영문 알파벳 별 출현 빈도의 개수를 구하고, 전체알파벳 중 몇 % 비율로 나오는지를 구하는 프로그램을 아래 조건에
맞게 작성하시오.
(배점: 40점)
[조건]
• 우린 아직 배열을 배우지 않았습니다.
• 전체 문자열의 길이는 String.length()
함수를 이용
• 문자열(String)에서 특정 자리의 문자를 가져오는 String.charAt(index)
함수를 이용
• 대소문자는 구분하지 않습니다.
• 출력 형식을 아래 결과 이미지 형식에 맞출 것(포맷일치)
 */
public class javaStudy {
	public static void main(String[] args)
	{
		String speech = "";
	      speech += "My fellow Koreans,";
	      speech += "\n";
	      speech += "I am grateful to you all. I bow my head in deep appreciation for the choice of you, the people.";
	      speech += "Today, serving as President in the 19th presidential term of the Republic of Korea, I take the first step toward a new Korea.";
	      speech += "My shoulders are now burdened with heavy mandates entrusted to me by the people, and my heart is burning with enthusiasm to create the kind of country that we have never been able to live in";
	      speech += "before. My head is now filled with blueprints for ushering in a new world characterized by unity and coexistence.";
	      speech += "\n";
	      speech += "The new Republic of Korea we are trying to build is the nation that those who came before us have consistently aspired to in the face of countless frustrations and defeats.";
	      speech += "It is the nation that our young people have longed for so ardently, in spite of many sacrifices and dedicated efforts.";
	      speech += "To build such a Republic of Korea, I declare before history and the people with a fearful but humble mind that I will faithfully fulfill my responsibilities and missions as President.";
	      speech += "\n";
	      speech += "I offer my gratitude and sympathy from deep in my heart to the other presidential contenders. There is no winner or loser in this election. We are all partners who are required to lead the new Republic of Korea together. Now is the time to leave behind the heat of competition and move forward together hand in hand.";
	      speech += "\n";
	      speech += "My fellow Koreans,";
	      speech += "\n";
	      speech += "We have gone through unprecedented political upheavals over the past few months. Politics was in disarray but our people were great.";
	      speech += "Even with the impeachment and arrest of the sitting President, our people paved a way forward for the Republic of Korea. They never got discouraged but instead turned the crisis into an opportunity,";
	      speech += "eventually opening the way to a new world today. The greatness of the Republic of Korea is the greatness of the people.";
	      speech += "\n";
	      speech += "During this presidential election, our people made history again. A new President was elected through even support from all across the country. Starting today, I will become a president for everyone. Even those who did not support me are my people, and I will serve them all alike.";
	      speech += "\n";
	      speech += "I dare to make a promise. This date—May 10, 2017—will go down in history as the beginning of the genuine unity of the people.";
	      speech += "\n";
	      speech += "My fellow Koreans,";
	      speech += "\n";
	      speech += "Over the past several troubling months, many people asked whether this country can indeed be called a country. From this very question, I will make a new start as President. From today, I will become a president dedicated to building a country worthy of being called a country.";
	      speech += "\n";
	      speech += "I will boldly break from the malpractices of old days. As President, I will take the lead in starting anew.";
	      speech += "\n";
	      speech += "First and foremost, I will strive to get rid of authoritarian practices in the presidency. When preparations are completed, I am going to leave Cheong Wa Dae to usher in an era of the presidential office in Gwanghwamun Square. There, my aides and I will put our heads together and have discussions. I will frequently engage in communication with the people. On key issues, I myself will hold press briefings.";
	      speech += "\n";
	      speech += "On my way home, I will drop by markets to talk freely with citizens I encounter. Large public forums will be occasionally held at Gwanghwamun Square.";
	      speech += "\n";
	      speech += "The President's imperial power will be shared as much as possible. I will make sure that agencies that have great authority remain completely independent from politics. There will be a system to keep these agencies in check so that none of them will be able to wield absolute power. ";
	      speech += "\n";
	      speech += "I will perform my duties with humility. I will become a president who is at eye level with the people.";
	      speech += "\n";
	      speech += "I will endeavor to address the security crisis promptly. For the sake of peace on the Korean Peninsula, I will crisscross the globe. If needed, I will immediately fly to Washington. I will also visit Beijing and Tokyo and even Pyongyang under the right circumstances.";
	      speech += "\n";
	      speech += "I remain committed to doing all I can for the establishment of peace on the Korean Peninsula. The ROK-U.S. alliance will be further strengthened. In the meantime, I will have serious discussions with the United States and China for the resolution of issues related to THAAD.";
	      speech += "\n";
	      speech += "Strong security is made possible by strong defense capabilities. The Government will also strive to further enhance independent defense capabilities. It will also lay the foundation for the resolution of the North Korean nuclear problem. The Government will endeavor to establish peace in Northeast Asia, thus setting a milestone in alleviating tensions on the Korean Peninsula.";
	      speech += "\n";
	      speech += "I will make efforts to change the landscape of politics characterized by division and conflicts. Confrontations between conservatives and progressives must come to an end. As President, I will take the lead in engaging in dialogues. Opposition parties are partners in the administration of state affairs. Discussions will be held on a regular basis, and I will take time to have meetings.";
	      speech += "\n";
	      speech += "Officials will be appointed regardless of where they are from. Competence and the need to put the right person in the right place will become the overriding criteria. I am ready to appoint capable individuals regardless of whether or not they support me.";
	      speech += "\n";
	      speech += "Both here and abroad, the economy is going through a difficult time. Ordinary people’s livelihoods are under threat. As I promised during my campaign, I will tend to the employment issue first. At the same time, I will take the initiative in reforming conglomerates. Under the Moon Jae-in Administration, the cozy relationship between political and business circles will completely disappear.";
	      speech += "\n";
	      speech += "I will strive to resolve conflicts between regions, social classes and generations and seek ways to solve the problems faced by irregular workers. I will help create a world without discrimination.";
	      speech += "\n";
	      speech += "I repeat. The Administration led by Moon Jae-in and the Democratic Party of Korea will promote equal opportunities. The process will be fair, and the result will be just.";
	      speech += "\n";
	      speech += "My fellow Koreans,";
	      speech += "\n";
	      speech += "This presidential election was held in the aftermath of the impeachment of the former President. The unfortunate history of the presidency still continues. On the occasion of this election, this unfortunate history must end.";
	      speech += "\n";
	      speech += "I will set a new example as the President of the Republic of Korea. I will make my utmost efforts to become a president who will be viewed as a success by the public and by history. By doing so, I will repay your support.";
	      speech += "\n";
	      speech += "I will become a clean president. I take office empty-handed, and I will leave office the same way. Someday, I will return home and become an ordinary citizen and friendly neighbor. I will continue to be a person all of you can be proud of. ";
	      speech += "\n";
	      speech += "I will become an honest president who keeps promises. I will meticulously honor the pledges I made during the campaign. Genuine political progress will be possible only when the president takes the initiative in engaging in trustworthy politics. I will not talk big about doing the impossible. I will admit to the wrong I did. I will not cover up unfavorable public opinion with lies.";
	      speech += "\n";
	      speech += "I will be a fair president. I will explore ways to ceate a world without privileges and foul play. I will endeavor to create a world where those who follow common sense will benefit. I will not overlook the pain of our neighbors. I will always be vigilant with a great sense of caring so that there will be no one left behind. I will become a president who comforts people in sorrow.";
	      speech += "\n";
	      speech += "I will be a president who communicates with others. I will exert my authority in a humble and modest manner; I will build a country stronger than it has ever been. I will not be a president who is domineering and authoritative but one who communicates and promotes dialogue.";
	      speech += "\n";
	      speech += "I will stay close to the people, working near Gwanghwamun. I will become a president who remains warmhearted and friendly to the people.";
	      speech += "\n";
	      speech += "My fellow Koreans,";
	      speech += "\n";
	      speech += "The Republic of Korea starts anew today, on May 10, 2017. A great history of building a decent nation begins. I ask you all to join me on this journey. I will fully dedicate myself to it.";
		int speechLength=speech.length();
		int a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0,l=0,m=0,n=0,o=0,p=0,q=0,r=0,s=0,t=0,u=0,v=0,w=0,x=0,y=0,z=0;
		for(int loop = 0;loop<speechLength;loop++)
		{
			char now = speech.charAt(loop);
			if(now =='a') a++;
			else if(now=='b') b++;
			else if(now=='c') c++;
			else if(now=='d') d++;
			else if(now=='e') e++;
			else if(now=='f') f++;
			else if(now=='g') g++;
			else if(now=='h') h++;
			else if(now=='i') i++;
			else if(now=='j') j++;
			else if(now=='k') k++;
			else if(now=='l') l++;
			else if(now=='m') m++;
			else if(now=='n') n++;
			else if(now=='o') o++;
			else if(now=='p') p++;
			else if(now=='q') q++;
			else if(now=='r') r++;
			else if(now=='s') s++;
			else if(now=='t') t++;
			else if(now=='u') u++;
			else if(now=='v') v++;
			else if(now=='w') w++;
			else if(now=='x') x++;
			else if(now=='y') y++;
			else if(now=='z') z++;
		}
		System.out.printf("A: %-5d개, %-4.2f%c\n", a, (a/(float)speechLength)*100, '\u0025');
		System.out.printf("B: %-5d개, %-4.2f%c\n", b, (b/(float)speechLength)*100, '\u0025');
		System.out.printf("C: %-5d개, %-4.2f%c\n", c, (c/(float)speechLength)*100, '\u0025');
		System.out.printf("D: %-5d개, %-4.2f%c\n", d, (d/(float)speechLength)*100, '\u0025');
		System.out.printf("E: %-5d개, %-4.2f%c\n", e, (e/(float)speechLength)*100, '\u0025');
		System.out.printf("F: %-5d개, %-4.2f%c\n", f, (f/(float)speechLength)*100, '\u0025');
		System.out.printf("G: %-5d개, %-4.2f%c\n", g, (g/(float)speechLength)*100, '\u0025');
		System.out.printf("H: %-5d개, %-4.2f%c\n", h, (h/(float)speechLength)*100, '\u0025');
		System.out.printf("I: %-5d개, %-4.2f%c\n", i, (i/(float)speechLength)*100, '\u0025');
		System.out.printf("J: %-5d개, %-4.2f%c\n", j, (j/(float)speechLength)*100, '\u0025');
		System.out.printf("K: %-5d개, %-4.2f%c\n", k, (k/(float)speechLength)*100, '\u0025');
		System.out.printf("L: %-5d개, %-4.2f%c\n", l, (l/(float)speechLength)*100, '\u0025');
		System.out.printf("M: %-5d개, %-4.2f%c\n", m, (m/(float)speechLength)*100, '\u0025');
		System.out.printf("N: %-5d개, %-4.2f%c\n", n, (n/(float)speechLength)*100, '\u0025');
		System.out.printf("O: %-5d개, %-4.2f%c\n", o, (o/(float)speechLength)*100, '\u0025');
		System.out.printf("P: %-5d개, %-4.2f%c\n", p, (p/(float)speechLength)*100, '\u0025');
		System.out.printf("Q: %-5d개, %-4.2f%c\n", q, (q/(float)speechLength)*100, '\u0025');
		System.out.printf("R: %-5d개, %-4.2f%c\n", r, (r/(float)speechLength)*100, '\u0025');
		System.out.printf("S: %-5d개, %-4.2f%c\n", s, (s/(float)speechLength)*100, '\u0025');
		System.out.printf("T: %-5d개, %-4.2f%c\n", t, (t/(float)speechLength)*100, '\u0025');
		System.out.printf("U: %-5d개, %-4.2f%c\n", u, (u/(float)speechLength)*100, '\u0025');
		System.out.printf("V: %-5d개, %-4.2f%c\n", v, (v/(float)speechLength)*100, '\u0025');
		System.out.printf("W: %-5d개, %-4.2f%c\n", w, (w/(float)speechLength)*100, '\u0025');
		System.out.printf("X: %-5d개, %-4.2f%c\n", x, (x/(float)speechLength)*100, '\u0025');
		System.out.printf("Y: %-5d개, %-4.2f%c\n", y, (y/(float)speechLength)*100, '\u0025');
		System.out.printf("Z: %-5d개, %-4.2f%c\n", z, (z/(float)speechLength)*100, '\u0025');
	}

}
