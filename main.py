def insertion_sort(input_list):
  for i in range(1, len(input_list)):
    j = i-1
    nxt_element = input_list[i]

    # computes current element with the next one 
    while(input_list[j] > nxt_element) and (j >= 0):
      input_list[j+1] = input_list[j]
      j=j-1

    input_list[j+1] = nxt_element

list = [19, 20 ,3 , 53, 55,323, 90, 8]
insertion_sort(list)
print(f"here is the list: {list}")
