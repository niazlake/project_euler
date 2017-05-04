import time

start = time.time()

g = range(100,1000)

last_list =[]
for i in g:
    for j in g:
        large = i*j
        string_main = str(large)
        if len(string_main) != 5:
            if int(string_main[0:3]) == int(string_main[5]+string_main[4]+string_main[3]):
                last_list.append(large)
        else:
            if int(string_main[0:1]) == int(string_main[4]+string_main[3]):
                last_list.append(large)
finish = time.time() - start
print("time:", finish, "result:", max(last_list))
