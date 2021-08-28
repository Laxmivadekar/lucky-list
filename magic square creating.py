middle_no=int(input('enter the middle number: '))
main_list=[[0,0,0],[0,0,0],[0,0,0]]
i=0
while i<3:
    j=0
    while j<3:
        if main_list[i][j]==main_list[0][0]:
            main_list.append(middle_no-3)
        if main_list[i][j]==main_list[0][1]:
            main_list.append(middle_no+2)
        elif main_list[i][j]==main_list[0][2]:
            main_list.append(middle_no+1)
        elif main_list[i][j]==main_list[1][0]:
            main_list.append(middle_no+4)
        elif main_list[i][j]==main_list[1][1]:
            main_list.append(middle_no-0)
        elif main_list[i][j]==main_list[1][2]:
            main_list.append(middle_no-4)
        elif main_list[i][j]==main_list[2][0]:
            main_list.append(middle_no-1)
        elif main_list[i][j]==main_list[2][1]:
            main_list.append(middle_no-2)
        elif main_list[i][j]==main_list[2][2]:
            main_list.append(middle_no+3)
        j=j+1
    i=i+1
    # main_list.append(sub_list)
print(main_list)
        
        
