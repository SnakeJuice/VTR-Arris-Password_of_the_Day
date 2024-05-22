from datetime import datetime

def GenArrisPasswords():
    seed = [0]*10
    seedten = [0]*10
    seedeight = [0]*8
    list1 = [0]*8
    list2 = [0]*8
    list3 = [0]*10
    list4 = [0]*10
    list5 = [0]*10

    date = datetime.now()
    myseed = "vtr2014"

    myseed2 = myseed * 3
    for i in range(10):
        seed[i] = ord(myseed2[i])

    seedten = seed.copy()
    for i in range(8):
        seedeight[i] = seedten[i]

    table1 = [
      [15, 15, 24, 20, 24],
      [13, 14, 27, 32, 10],
      [29, 14, 32, 29, 24],
      [23, 32, 24, 29, 29],
      [14, 29, 10, 21, 29],
      [34, 27, 16, 23, 30],
      [14, 22, 24, 17, 13]
    ]

    table2 = [
      [0, 1, 2, 9, 3, 4, 5, 6, 7, 8],
      [1, 4, 3, 9, 0, 7, 8, 2, 5, 6],
      [7, 2, 8, 9, 4, 1, 6, 0, 3, 5],
      [6, 3, 5, 9, 1, 8, 2, 7, 4, 0],
      [4, 7, 0, 9, 5, 2, 3, 1, 8, 6],
      [5, 6, 1, 9, 8, 0, 4, 3, 2, 7]
    ]

    alphanum = [
      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
      'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    year = date.year % 100
    month = date.month
    day_of_month = date.day
    day_of_week = date.weekday()

    for i in range(5):
        list1[i] = table1[day_of_week][i]

    list1[5] = day_of_month
    list1[6] = ((year + month) - day_of_month + 36) % 36 if ((year + month) - day_of_month) < 0 else ((year + month) - day_of_month) % 36
    list1[7] = (((3 + ((year + month) % 12)) * day_of_month) % 37) % 36

    for i in range(8):
        list2[i] = seedeight[i] % 36

    for i in range(8):
        list3[i] = ((list1[i] + list2[i]) % 36)

    list3[8] = sum(list3[:8]) % 36
    num8 = list3[8] % 6
    list3[9] = round(num8 ** 2)

    for i in range(10):
        list4[i] = list3[table2[num8][i]]

    for i in range(10):
        list5[i] = (seedten[i] + list4[i]) % 36

    password_of_the_day = [alphanum[i] for i in list5]
    
    print("\nuser: technician")
    print("pass: ", ''.join(password_of_the_day) )

    return ''.join(password_of_the_day)

GenArrisPasswords()