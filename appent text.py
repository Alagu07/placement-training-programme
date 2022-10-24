File file = new File("append.txt");
FileWriter fr = new FileWriter(file, true);
BufferedWriter br = new BufferedWriter(fr);
PrintWriter pr = new PrintWriter(br);
pr.println("data");
pr.close();
br.close();
fr.close();
