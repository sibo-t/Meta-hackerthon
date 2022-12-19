
def convert_txt_input_to_int_list(txt):
    input_list = []
    f = open(txt, "r")
    for x in f:
        input_list.append(int(x))
    f.close()
    return input_list

def compare_first_two_nums(the_list):
    """Compare the 1st and second value in the list,
    append to the last list if second greater than 1st

    Args:
        the_list (list): Integer input from the file

    Return:
        (list):List of all the possible ride strategies
    """
    scary_ride_strategies = []
    temp = 0
    prev = 0
    fun_sum = 0
    while (len(the_list)!=0):
        temp = the_list.pop(0)
        if temp>prev and len(the_list)>0:
            fun_sum+=10

        elif temp>prev and len(the_list)==0:
            fun_sum+=10
            scary_ride_strategies.append(fun_sum)

        else:
            scary_ride_strategies.append(fun_sum)
            fun_sum = 10

        prev = temp
        


    return scary_ride_strategies


if __name__ == "__main__":
    the_input = convert_txt_input_to_int_list("rollercoasters_medium_sample_input.txt")
    fun_strategies = compare_first_two_nums(the_input)
    the_max_fun = max(fun_strategies)
    f = open("outsample.txt", "w")
    f.write(str(the_max_fun))
    f.close()