import generate_data as gd
import filter_data as fd
import analys_data as ad

#gd.generate_data(2005)
#fd.filter_date("month",12)
#fd.filter_data_gt("pool_betting_duty",417000)
#ad.general_betting_stakes('generalbettingstakes')

#ad.column_year('generalbettingstakes',2005)

#filter_data('candidate',"Martin O'Malley")
#filter_candidate("Martin O'Malley")
#filter_party("Republican")
#filter_st_abbr("CA")
#filter_state("California")
#filter_votes_gt(10000)
#filter_votes_ls(5000)


#gd.read_data()
#analys_tests
#ad.total_receipt(2000)
#ad.total_receipt_years([2011,2012,2013])
#ad.column_year('pool_betting_duty', 2000)
###ad.column_full('pool_betting_duty')
#ad.column_multiple_years('pool_betting_duty',[2011,2012,2013])
#ad.annual_receipt('pool_betting_duty')


def start():
    flag_main = True
    while flag_main:
        print("""Comands:
        1-filter,
        2-analyse 
        3-read_data
        4-gen_data
        5-exit
         """)
        a = int(input("Enter command:"))
        if a == 2:
            print(""" Analyze
                        1 - Total receipt of a specific year
                        2 - Total receipt of range of years
                        3 - full data of certain duty
                        4 - Receipt of a duty in a certain year
                        5 - Receipt of a duty in a range of years
                        6 - Total sum of receipts of a duty
                        7-  Total Betting 
                        8-  Total Gaming
                        8 - quit

                        """)
            b = int(input("Enter command: "))
            if b == 1:
                c = int((input("Enter year: ")))
                ad.total_receipt(c)
            if b == 2:
                u = int(input("enter number of years you want to compare: "))
                years = [int(input("Enter year")) for i in range(u)]
                ad.total_receipt_years(years)
            if b == 3:
                print(""" Analyze
                        1 - general_betting_duty
                        2 - pool_betting_duty
                        3 - gaming_duty
                        4 - amusement_machine_licence
                        5 - bingo
                        6 - machine_games_duty
                        7 - lottery_duty
                                        """)
                j = int(input("enter command: "))
                if j == 1:
                    ad.column_full("general_betting_duty")
                if j == 2:
                    ad.column_full("pool_betting_duty")
                if j == 3:
                    ad.column_full("gaming_duty")
                if j == 4:
                    ad.column_full("amusement_machine_licence")
                if j == 5:
                    ad.column_full("bingo")
                if j == 6:
                    ad.column_full("machine_games_duty")
                if j == 7:
                    ad.column_full("lottery_duty")
            if b == 4:
                yy = int(input("enter year: "))
                print(""" Analyze
                        1 - general_betting_duty
                        2 - pool_betting_duty
                        3 - gaming_duty
                        4 - amusement_machine_licence
                        5 - bingo
                        6 - machine_games_duty
                        7 - lottery_duty
                                                       """)
                j = int(input("enter command: "))
                if j == 1:
                    ad.column_year("general_betting_duty", yy)
                if j == 2:
                    ad.column_year("pool_betting_duty", yy)
                if j == 3:
                    ad.column_year("gaming_duty", yy)
                if j == 4:
                    ad.column_year("amusement_machine_licence", yy)
                if j == 5:
                    ad.column_year("bingo", yy)
                if j == 6:
                    ad.column_year("machine_games_duty", yy)
                if j == 7:
                    ad.column_year("lottery_duty", yy)
            if b == 5:
                u = int(input("enter number of years you want to compare: "))
                years = [int(input("Enter year: ")) for i in range(u)]
                print(""" Analyze
                        1 - general_betting_duty
                        2 - pool_betting_duty
                        3 - gaming_duty
                        4 - amusement_machine_licence
                        5 - bingo
                        6 - machine_games_duty
                        7 - lottery_duty
                                                                       """)
                j = int(input("enter command: "))
                if j == 1:
                    ad.column_multiple_years("general_betting_duty", years)
                if j == 2:
                    ad.column_multiple_years("pool_betting_duty", years)
                if j == 3:
                    ad.column_multiple_years("gaming_duty", years)
                if j == 4:
                    ad.column_multiple_years("amusement_machine_licence", years)
                if j == 5:
                    ad.column_multiple_years("bingo", years)
                if j == 6:
                    ad.column_multiple_years("machine_games_duty", years)
                if j == 7:
                    ad.column_multiple_years("lottery_duty", years)
            if b == 6:
                print(""" Analyze
                        1 - general_betting_duty
                        2 - pool_betting_duty
                        3 - gaming_duty
                        4 - amusement_machine_licence
                        5 - bingo
                        6 - machine_games_duty
                        7 - lottery_duty
                                                                                       """)
                j = int(input("enter command: "))
                if j == 1:
                    ad.annual_receipt("general_betting_duty")
                if j == 2:
                    ad.annual_receipt("pool_betting_duty")
                if j == 3:
                    ad.annual_receipt("gaming_duty")
                if j == 4:
                    ad.annual_receipt("amusement_machine_licence")
                if j == 5:
                    ad.annual_receipt("bingo")
                if j == 6:
                    ad.annual_receipt("machine_games_duty")
                if j == 7:
                    ad.annual_receipt("lottery_duty")
            if b == 7:
                ad.annual_betting()
            if b == 8:
                ad.annual_gaming()
        elif a == 1:
            print(""" Filter
            1 - Year
            2 - Year >
            3 - Year <
            4 - Month
            5 - Month >
            6 - Month <
            7 - Date
            8 - Other fields
            9 - quit
            
            """)

            b = int(input("Enter command:"))

            if b == 1:
                c = int((input("Enter year:")))
                fd.filter_date("year", c)
            if b == 2:
                c = int((input("Enter year:")))
                fd.filter_date_gt("year", c)
            if b == 3:
                c = input("Enter year:")
                fd.filter_date_ls("year", c)
            if b == 4:
                c = int((input("Enter month:")))
                fd.filter_date("month", c)
            if b == 5:
                c = int((input("Enter month:")))
                fd.filter_date_gt("month", c)
            if b == 6:
                c = input("Enter month:")
                fd.filter_date_ls("month", c)
            if b == 7:
                c = input("Enter date:(yyyy-mm)")
                fullDate = "%s-01" %c
                print(fullDate)
                fd.filter_data("date", fullDate)
            if b == 8:

                print(""" operation
                         1 - =
                         2 - >
                         3 - <
                              """)
                op = int(input("Enter operation: "))
                val = int(input("Enter Value: "))
                print(""" Field
                        1 - general_betting_duty
                        2 - pool_betting_duty
                        3 - gaming_duty
                        4 - amusement_machine_licence
                        5 - bingo
                        6 - machine_games_duty
                        7 - lottery_duty
                                                       """)
                j = int(input("enter command"))
                s = ""
                if j == 1:
                    s = "general_betting_duty"
                if j == 2:
                    s = "pool_betting_duty"
                if j == 3:
                    s = "gaming_duty"
                if j == 4:
                    s = "amusement_machine_licence"
                if j == 5:
                    s = "bingo"
                if j == 6:
                    s = "machine_games_duty"
                if j == 7:
                    s = "lottery_duty"
                if op == 1:
                    fd.filter_data(s, val)
                if op == 2:
                    fd.filter_data_gt(s, val)
                if op == 3:
                    fd.filter_data_ls(s, val)
            if b == 15:
                break
            if (b < 1 or b > 15):
                print("Error number")
                flag_main = True

        elif a == 3:
            gd.read_data()
        elif a == 4:
            c = int(input("Enter start year: "))
            gd.generate_data(c)
        elif a == 5:
            break

start()
