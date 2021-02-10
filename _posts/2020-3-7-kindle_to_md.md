---
layout: post
title: kindle的txt格式笔记转md格式(JAVA)
--- 
<!-- more --> 
需要先将html的pc端导出笔记复制为txt格式。        
```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class kindle_formater {
    public static void main(String[] Zing) {
        String path = "D:\\Workplace\\Idea\\docs\\article.txt";
        ArrayList<String> strs = read(path);
        writeFile("D:\\Workplace\\Idea\\docs\\article.md", strs);
    }

    public static ArrayList<String> read(String path) {
        FileInputStream fis = null;
        InputStreamReader isr = null;
        BufferedReader br = null;
        ArrayList<String> ending = new ArrayList<String>();
        ending.add("---");
        ending.add("layout: post");
        ending.add("title: name");
        ending.add("---");
        ending.add("<!-- more -->");
        try {
            fis = new FileInputStream(path);
            isr = new InputStreamReader(fis, "UTF-8");
            br = new BufferedReader(isr);
            String line;
            while ((line = br.readLine()) != null)//去除所有非英文
            {
                if (line.contains("标注 (粉色)")) {
                    ;
                } else {
                    if (!line.contains("标注 (黄色)")) {
                        line = line.replace(" ", "");
                        if(line.contains("[")&&line.contains("]")){
                            String[] temp = line.split("\\[");
                            System.out.println(temp.length);
                            for(int temp_i = 0;temp_i < temp.length;temp_i ++){
                                if(temp_i != 0){
                                    while(true){
                                        String str = temp[temp_i].charAt(0) +"";
                                        try{
                                            Integer.parseInt(str);
                                            temp[temp_i] = removeCharAt(temp[temp_i],0);
                                        } catch (Exception ex){
                                            try{
                                                temp[temp_i] = removeCharAt(temp[temp_i],0);
                                            } catch (Exception ex1){

                                            }finally {
                                                break;
                                            }
                                        }
                                    }
                                }
                            }
                            line = "";
                            for(int temp_i = 0;temp_i < temp.length;temp_i ++){
                                line = line + temp[temp_i];
                            }
                        }
                        ending.add("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + line +  "               ");
                    }
                }
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            try {
                br.close(); // 关闭最后一个类，会将所有的底层流都关闭
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
        return ending;
    }

    public static void writeFile(String path, ArrayList<String> lines) {
        FileOutputStream fos = null;
        OutputStreamWriter osw = null;
        BufferedWriter bw = null;
        try {
            fos = new FileOutputStream(path); // 节点类
            osw = new OutputStreamWriter(fos, "UTF-8"); // 转化类
            bw = new BufferedWriter(osw); // 装饰类
            for (int i = 0; i < lines.size(); i++) {
                bw.write(lines.get(i));
                System.out.print(lines.get(i) + "\n");
                bw.newLine();
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            try {
                bw.close(); // 关闭最后一个类，会将所有的底层流都关闭
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
    }
    public static String removeCharAt(String s, int pos) {
        return s.substring(0, pos) + s.substring(pos + 1);// 使用substring()方法截取0-pos之间的字符串+pos之后的字符串，相当于将要把要删除的字符串删除
    }
}

```