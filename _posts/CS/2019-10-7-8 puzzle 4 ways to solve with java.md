---
layout: post
title: 8 puzzle 4 ways to solve
categories: [CS, JAVA]
tags: [java]
---
example: from       
2 | 3 |&nbsp;&nbsp;&nbsp;&nbsp;|       
1 | 8 | 5 |         
7 | 4 | 6 |   
to        
1 | 2 | 3 |       
8 |&nbsp;&nbsp;&nbsp;&nbsp;| 4 |         
7 | 6 | 5 | 
<!-- more -->   
```java
public class EightHuanfang {
	/**
	 * 输入中0表示该位置无小卡片
	 * @param Zing
	 */
	public static void main(String[] Zing) {
		int[][] input = { {2,3,0},{1,8,5},{7,4,6}};
		int[][] result = { {1,2,3},{8,0,4},{7,6,5}};
		BreadthFirst(input,result);
		DepthFirst(input,result);
		HillClimbing(input,result);
		BestFirstSearch(input,result);
		}
	/**
	 * 广度优先搜索
	 * 1队列实现，先放入根节点，
	 * 2看队首符不符合，符合就结束
	 * 3把根节点的叶子放进去，扔掉队首
	 * 4返回2
	 * 搜索成功返回true，否则返回false
	 * @return
	 */
	public static boolean BreadthFirst(int[][] input,int[][] result) {
		boolean ending = false;//ending=false：无解，ending=true：可解
		long startTime=System.currentTimeMillis();   //获取开始时间
		
		int[][] input0 = new int[3][3];
		input0 = shuzufuzhi(input);
		int[][] result0 = new int[3][3];
		result0 = shuzufuzhi(result);
		/**List里面可以装数组！！！
		 * int[][]数组也是对象！！！
		 */
		ArrayList<int[][]> list= new ArrayList<>();//队列
		/**下面这个visit很关键！！！不然就死循环了
		 */
		ArrayList<int[][]> visit= new ArrayList<>();//存储访问过的节点!!!
		list.add(input0);
		visit.add(input0);
		for(int i = 0;;i ++) {
			if(list.size() == 0) {//队列中没有元素，搜索失败
				ending = false;
				break;
			}
			if(0 == qifahanshu(list.get(0),result0)) {//成功搜索到元素
				ending = true;
				break;
			}else {
				ArrayList<int[][]> temp = new ArrayList<>();
				temp= move(shuzufuzhi(list.get(0)));
				list.remove(0);
				for(int j = 0;j < temp.size();j ++) {
					if(!visittest(visit,temp.get(j))) {
						list.add(temp.get(j));
						visit.add(temp.get(j));
					}
				}
			}
		}
		if(ending == false) {
			System.out.println("不可达");
		}else {
			System.out.println("可达");
		}
		long endTime=System.currentTimeMillis(); //获取结束时间
		System.out.println("Breadth-First: "+(endTime-startTime)+"ms ");
		return ending;
	}
	/**
	 * 深度优先搜索
	 * 1.首先将根节点放入队列中。
2.从队列中取出第一个节点，并检验它是否为目标。
如果找到目标，则结束搜寻并回传结果。
否则将它某一个尚未检验过的直接子节点加入队列中。
3.重复步骤2。
4.如果不存在未检测过的直接子节点。
将上一级节点加入队列中。
重复步骤2。
5.重复步骤4。
6.若队列为空，表示整张图都检查过了——亦即图中没有欲搜寻的目标。结束搜寻并回传“找不到目标”。
	 * @param input
	 * @param result
	 * @return
	 */
    public static boolean DepthFirst(int[][] input,int[][] result) {
    	boolean ending = false;
        long startTime=System.currentTimeMillis();   //获取开始时间
		
		int[][] input0 = new int[3][3];
		input0 = shuzufuzhi(input);
		int[][] result0 = new int[3][3];
		result0 = shuzufuzhi(result);
		ArrayList<int[][]> visit= new ArrayList<>();//存储访问过的节点
		node zuzong = new node(null,shuzufuzhi(input0));//别忘了在根节点上面添加一个无用节点！
		node root = new node(zuzong,shuzufuzhi(input0));
		ArrayList<node> nodes= new ArrayList<>();//深搜中的队列
		nodes.add(root);
		for(int i = 0;;i ++) {
			if(nodes.size() == 0) {
				ending = false;
				break;
			}
			
			if(nodes.get(0) == null) {
				ending = false;
				break;
			}
			
			node tempnode = nodes.get(0);//队列的头节点是tempnode
			nodes.remove(0);
			
			if(0 == qifahanshu(tempnode.getdata(),result0)) {
				ending = true;
				break;
			}
			
			if(tempnode.visit == false) {//该节点没有被访问过的情形
				
				tempnode.visit = true;
				
				if(tempnode.create == false) {//向节点中添加生成的叶子节点
					ArrayList<int[][]> temp = new ArrayList<>();
					temp= move(shuzufuzhi(tempnode.getdata()));//temp中装着tempnode生成的节点
					for(int k = 0;k < temp.size();k ++) {
						if(visittest(visit,temp.get(k)) == false) {
							visit.add(shuzufuzhi(temp.get(k)));
							node child = new node(tempnode,shuzufuzhi(temp.get(k)));
							tempnode.addchild(child);
						}
					}
					tempnode.create = true;
				}
				if(tempnode.getchildren().size() == 0) {
					
					nodes.add(tempnode.getparent());//没孩子就添加父母
				}else {
					nodes.add(tempnode.getchildren().get(0));//有孩子就添加最左边的孩子
				}
				
			}else {//该节点被访问过的情形
				for(int j = 0;j < tempnode.getchildren().size();j ++) {
					if(tempnode.getchildren().get(j).visit == false) {//还有孩子没被访问
						nodes.add(tempnode.getchildren().get(j));
						break;
					}
					if(j == tempnode.getchildren().size() - 1) {
						nodes.add(tempnode.getparent());
					}
				}
			}
				
		}
    	
		long endTime=System.currentTimeMillis(); //获取结束时间
		System.out.println("DepthFirst: "+(endTime-startTime)+"ms ");		
    	return ending;
    	}
    /**
     * 爬山法，把启发测度有大到小压人堆栈
     * @param input
     * @param result
     * @return
     */
    public static boolean HillClimbing(int[][] input,int[][] result) {
    	boolean ending = false;//ending=false：无解，ending=true：可解
		long startTime=System.currentTimeMillis();   //获取开始时间
		
		int[][] input0 = new int[3][3];
		input0 = shuzufuzhi(input);
		int[][] result0 = new int[3][3];
		result0 = shuzufuzhi(result);
		/**List里面可以装数组！！！
		 * int[][]数组也是对象！！！
		 */
		ArrayList<int[][]> list= new ArrayList<>();//栈，list的最后边是栈顶
		/**下面这个visit很关键！！！不然就死循环了
		 */
		ArrayList<int[][]> visit= new ArrayList<>();//存储访问过的节点!!!
		list.add(input0);
		visit.add(input0);
		for(int i = 0;;i ++) {
			if(list.size() == 0) {//队列中没有元素，搜索失败
				ending = false;
				break;
			}
			if(0 == qifahanshu(list.get(list.size() - 1),result0)) {//成功搜索到元素
				ending = true;
				break;
			}else {
				ArrayList<int[][]> temp = new ArrayList<>();
				temp= move(shuzufuzhi(list.get(list.size() - 1)));
				list.remove(list.size() - 1);
				ArrayList<int[][]> sort = new ArrayList<>();//用于按照启发测度排序
				for(int j = 0;j < temp.size();j ++) {
					if(!visittest(visit,temp.get(j))) {
						sort.add(temp.get(j));
						visit.add(temp.get(j));
					}
				}
				sort(sort,result0);
				for(int j = 0;j < sort.size();j ++) {
					list.add(sort.get(sort.size() - 1 - j));
				}
			}
		}
		long endTime=System.currentTimeMillis(); //获取结束时间
		System.out.println("HillClimbing: "+(endTime-startTime)+"ms ");
		return ending;
		
	}
    /**
     * 弄个堆，每次去取启发函数数值最小的
     * @param input
     * @param result
     * @return
     */
    public static boolean BestFirstSearch(int[][] input,int[][] result) {
		boolean ending = false;
		long startTime=System.currentTimeMillis(); 
    	int[][] input0 = shuzufuzhi(input);
    	int[][] result0 = shuzufuzhi(result);
		
		ArrayList<int[][]> list = new ArrayList<>();//堆
		ArrayList<Integer> intlist = new ArrayList<>();//和list对应的存储权值的arraylist
		ArrayList<int[][]> visit = new ArrayList<>();
		list.add(shuzufuzhi(input0));
		intlist.add(qifahanshu(list.get(0),result0));
		visit.add(shuzufuzhi(input0));
		for(int i = 0;;i ++) {
			
			if(list.size() == 0) {
				ending = false;
				break;
			}
			
			int minindex = 0;
			int min = 999999;
			for(int h = 0;h < intlist.size();h ++) {
				if((int)intlist.get(h) < min) {
					minindex = h;
					min = intlist.get(h);
				}
			}
			if((int)intlist.get(minindex) == 0) {
				ending = true;
				break;
			}
			ArrayList<int[][]> temp = new ArrayList<>();
			temp= move(shuzufuzhi(list.get(minindex)));
			list.remove(minindex);
			intlist.remove(minindex);
			for(int j = 0;j < temp.size();j ++) {
				if(!visittest(visit,temp.get(j))) {
					list.add(temp.get(j));
					intlist.add(qifahanshu(temp.get(j),result0));
					visit.add(temp.get(j));
				}
			}
			
			
			
		}
		 
		
    	long endTime=System.currentTimeMillis(); //获取结束时间
		System.out.println("BestFirstSearch: "+(endTime-startTime)+"ms ");
		return ending;
	}
    /**
     * 为防止数组赋值中的同地址引用而创建的新建对象数组复制方式
     * @param input
     * @return
     */
    public static int[][] shuzufuzhi(int[][] input){
    	int[][] ending = new int[3][3];
    	for(int i = 0;i < 3;i ++) {
    		for(int j = 0;j < 3;j ++) {
    			ending[i][j] = input[i][j];
    		}
    	}
    	return ending;
    }
    /**
     * 启发函数
     * 用于计算input和result的数组之间有多少个数字在对应位置上不一样
     * @param input
     * @param result
     * @return
     */
    public static int qifahanshu(int[][] input,int[][] result){
    	int ending = 0;
    	for(int i = 0;i < 3;i ++) {
    		for(int j = 0;j < 3;j ++) {
    			if(input[i][j] != result[i][j]) {
    				ending = ending + 1;
    			}
    		}
    	}
    	return ending;
    }
    /**
     * 把输入的数组进行一次操作，即把非0元素移到0的位置
     * 返回一个ArrayList中装着两个/多个新的数组
     * @param input
     * @return
     */
    public static ArrayList<int[][]> move(int[][] input){
    	int[][] input0 = new int[3][3];
    	ArrayList<int[][]> ending = new ArrayList<>();
    	int i0 = 0;//输入数组中0元素的横坐标
    	int j0 = 0;//输入数组中0元素的纵坐标
    	input0 = shuzufuzhi(input);
    	for(int i = 0;i < 3;i ++) {
    		for(int j = 0;j < 3;j ++) {
    			if(input0[i][j] == 0) {
    				i0 = i;
    				j0 = j;
    				break;
    			}
    		}
    	}
    	
    	if((j0 == 1)&&(i0 == 1)) {//0在中间的时候
    		int[][] temp = new int[3][3];
    		temp= shuzufuzhi(input0);
    		temp[1][1] = temp[0][1];
    		temp[0][1] = 0;
    		ending.add(temp);
    		temp= shuzufuzhi(input0);
    		temp[1][1] = temp[1][0];
    		temp[1][0] = 0;
    		ending.add(temp);
    		temp= shuzufuzhi(input0);
    		temp[1][1] = temp[1][2];
    		temp[1][2] = 0;
    		ending.add(temp);
    		temp= shuzufuzhi(input0);
    		temp[1][1] = temp[2][1];
    		temp[2][1] = 0;
    		ending.add(temp);
    	}else {
    		if(i0 == 1) {//当0位于中间行(除中心点)时
    			int[][] temp = new int[3][3];
        		temp= shuzufuzhi(input0);
        		temp[1][j0] = temp[0][j0];
        		temp[0][j0] = 0;
        		ending.add(temp);
        		temp= shuzufuzhi(input0);
        		temp[1][j0] = temp[2][j0];
        		temp[2][j0] = 0;
        		ending.add(temp);
        		if(j0 == 0) {//(1,0)
        			temp= shuzufuzhi(input0);
            		temp[1][0] = temp[1][1];
            		temp[1][1] = 0;
            		ending.add(temp);
        		}else {//(1,2)
        			temp= shuzufuzhi(input0);
            		temp[1][2] = temp[1][1];
            		temp[1][1] = 0;
            		ending.add(temp);
        		}
    		}else {
    			if(j0 == 1) {//当0位于中间列(除中心点)时
    				int[][] temp = new int[3][3];
            		temp= shuzufuzhi(input0);
            		temp[i0][1] = temp[i0][0];
            		temp[i0][0] = 0;
            		ending.add(temp);
            		temp= shuzufuzhi(input0);
            		temp[i0][1] = temp[i0][2];
            		temp[i0][2] = 0;
            		ending.add(temp);
            		if(i0 == 0) {//(0,1)
            			temp= shuzufuzhi(input0);
                		temp[0][1] = temp[1][1];
                		temp[1][1] = 0;
                		ending.add(temp);
            		}else {//(2,1)
            			temp= shuzufuzhi(input0);
                		temp[2][1] = temp[1][1];
                		temp[1][1] = 0;
                		ending.add(temp);
            		}
    			}else {
    				if((i0 == 0)&&(j0 == 0)) {//0在(0,0)
    					int[][] temp = new int[3][3];
                		temp= shuzufuzhi(input0);
                		temp[0][0] = temp[0][1];
                		temp[0][1] = 0;
                		ending.add(temp);
                		temp= shuzufuzhi(input0);
                		temp[0][0] = temp[1][0];
                		temp[1][0] = 0;
                		ending.add(temp);
    				}else {
    					if((i0 == 0)&&(j0 == 2)) {//0在(0,2)
    						int[][] temp = new int[3][3];
                    		temp= shuzufuzhi(input0);
                    		temp[0][2] = temp[0][1];
                    		temp[0][1] = 0;
                    		ending.add(temp);
                    		temp= shuzufuzhi(input0);
                    		temp[0][2] = temp[1][2];
                    		temp[1][2] = 0;
                    		ending.add(temp);
    					}else {
    						if((i0 == 2)&&(j0 == 0)) {//0在(2,0)
    							int[][] temp = new int[3][3];
                        		temp= shuzufuzhi(input0);
                        		temp[2][0] = temp[1][0];
                        		temp[1][0] = 0;
                        		ending.add(temp);
                        		temp= shuzufuzhi(input0);
                        		temp[2][0] = temp[2][1];
                        		temp[2][1] = 0;
                        		ending.add(temp);
    						}else {//0在(2,2)
    							int[][] temp = new int[3][3];
                        		temp= shuzufuzhi(input0);
                        		temp[2][2] = temp[1][2];
                        		temp[1][2] = 0;
                        		ending.add(temp);
                        		temp= shuzufuzhi(input0);
                        		temp[2][2] = temp[2][1];
                        		temp[2][1] = 0;
                        		ending.add(temp);
    						}
    					}
    				}
    			}
    		}
    	}
    	return ending;
    }
    /**
     * 选择排序
     * 按照启发测度从小大大排序
     * @param arr
     */
    public static void sort(ArrayList<int[][]> list,int[][] result) {
    	int[] arr = new int[list.size()];
    	for(int i = 0;i < list.size();i ++) {
    		arr[i] = qifahanshu(list.get(i),result);
    	}
        for (int x = 0; x < arr.length - 1; x++) {
            for (int y = x + 1; y < arr.length; y++) {
                if (arr[x] > arr[y]) {
                    int temp = arr[x];
                    int[][] temp0 = list.get(x);
                    arr[x] = arr[y];
                    list.add(x, list.get(y));
                    list.remove(x + 1);
                    arr[y] = temp;
                    list.remove(y);
                    list.add(y,temp0);
                }
            }
        }
    }
    /**
     * 基于内容判断，而非地址
     * 用来判断某元素是否在list中
     * true表示数组在list中
     * false表示富足不再list中
     * @param input
     * @return
     */
    public static boolean visittest(ArrayList<int[][]> input,int[][] shuzu) {
    	boolean ending = false;
    	int[][] temp = new int[3][3];
    	for(int i = 0;i < input.size();i ++) {
    		temp = input.get(i);
    		if(qifahanshu(temp,shuzu) == 0) {
    			ending = true;
    			break;
    		}
    	}
    	return ending;
    }
    /**
     * 测试中用于输出数组
     * @param input
     */
    public static void showtest(int[][] input) {
    	int[][] input0 = new int[3][3];
    	input0 = shuzufuzhi(input);
    	for(int i = 0;i < 3;i ++) {
    		for(int j = 0;j < 3;j ++) {
    			System.out.print(input0[i][j] + ",");
    		}
    		System.out.println("");
    	}
    	System.out.println("");
    }
}
/**
 * 树上的节点
 * @author ZingsGF
 *
 */
class node{
	private node parrent = null;
	private ArrayList<node> children = new ArrayList<>();
	private int[][] data = new int[3][3];
	public boolean visit = false;//该节点是否被访问过
	public boolean create = false;//该节点是否生成过子节点
	node(node parrent,int[][] data) {
		this.parrent = parrent;
		this.data = data;
	}
	public ArrayList<node> getchildren() {
		return this.children;
	}
	public void addchild(node child) {
		children.add(child);
	}
	public int[][] getdata() {
		return data;
	}
	public node getparent(){
		return this.parrent;
	}
}
```
