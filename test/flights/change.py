file1 = open("testfile.csv","w") 
with open("flights_input.csv") as f:
    count = 0.00
    list1 = []
    dict1 = {}
    list_onomata = ["sched_dep_time","act_dep_time","sched_arr_time","flight","act_arr_time"]
    for line in f:
        line1 = line.split(",")
        count1 = line1[0]
        if float(count) == float(count1):
            if line1[1] in list_onomata:
	        dict1[line1[1]] = line1[2]
            list1.append([line1[1],line1[2]])
        else:
              list1 = []
              if count != 0:
                  file1.write(count+","+dict1["flight"]+","+dict1["sched_dep_time"]+","+dict1["act_dep_time"]+","+dict1["sched_arr_time"]+","+dict1["act_arr_time"]+"\n")
              dict1={}
              count = count1
              if line1[1] in list_onomata:
	        dict1[line1[1]] = line1[2]
              list1.append([line1[1],line1[2]])

file1.close()
      
        
