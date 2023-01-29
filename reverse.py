numbers = [10,9,8,7,6,5,4,3,2,1]

def reverse_list(list_in):
  for i in range(len(list_in)//2):
    list_in[i], list_in[-i-1] = list_in[-i-1], list_in[i]
  return list_in

print(reverse_list(numbers))
