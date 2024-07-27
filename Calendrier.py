import calendar
while True:
    yes_no=['yes','no']
    y=int(input(" a3tini l3am ltheb alih : "))
    m=int(input(" a3tini 9adeh mn chhar theb twarih : "))
    
    for i in range(m):
        print (calendar.month(y,i+1))
        
    Try_again = input('Theb t3awed ? :').lower()
    
    while Try_again not in yes_no:
    	 Try_again = input('Theb t3awed ?(yes/no) :').lower()
    if Try_again != 'yes':
        break