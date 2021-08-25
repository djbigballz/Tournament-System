###############################
# Cameron Denny               #
# Tournament System           #
# 17/01/2021                  #
###############################

import sys
import csv 

def main(): 
    menu()

def menu():
    print("************TOURNAMENT PROGRAM MENU**************") 
    while True: 
        choice = input(""" 
        1: Enter event rankings
        2: Output scores
        3: Output winners
        4: Quit/Log Out
        Please enter your choice: """) 

        if choice == "1":
            enter_rankings()      
        elif choice == "2": 
            output_scores()
        elif choice=="3":
            output_winners()
        elif choice=="4": 
            sys.exit
            break 
        else:
            print("You must only select 1,2,3,4.") 
            print("Please try again")
            menu() 

def enter_rankings(): 
    event_ranking = []

    choice = input("Enter T for Team or I for Individual: ")
    if not(choice in 'TI'):
        print("You must only enter T or I. Please try again.")
        print("--------------------------------------------------") 
        enter_rankings()
    if choice == 'I':
        subject  = "Individual"
        events_data_individual = open('Event_Data_individual.csv', 'w', newline='')
        data_writeri = csv.writer(events_data_individual)
        data_writer = data_writeri
    if choice == 'T':
        subject = 'Team'
        events_data_team = open('Event_Data_team.csv', 'w', newline='')
        data_writert = csv.writer(events_data_team)
        data_writer = data_writert
    for event in range(1,6):
        print(f'Enter the rankings for the event number {event}')
        rank = input(f'Enter the name of {subject} who stood |First|: ')
        event_ranking.append(rank)
        rank = input(f'Enter the name of {subject} who stood |Second|: ')
        event_ranking.append(rank)
        rank = input(f'Enter the name of {subject} who stood |Third|: ')
        print("--------------------------------------------------")
        event_ranking.append(rank)
        data_writer.writerow(event_ranking)
        event_ranking.clear()
    print('You have Entered the Rankings for all the Events...')
    

def output_scores():
    data_indi = open('Event_Data_team.csv', 'r')
    event_counter = 1
    print('\n\n\nTeam Rankings for all the Events are: ')
    for one_event in data_indi:
        print(f'Scores for Event Number {event_counter} are:')

        all_ranks = one_event.split(',')
        all_ranks.reverse()
        for j in all_ranks:
            print(f'{j} = {(all_ranks.index(j) + 1) * 5}')
        event_counter += 1

    data_indi = open('Event_Data_individual.csv', 'r')
    event_counter = 1
    print('\n\n\nIndividual Rankings for all the Events are: ')
    for one_event in data_indi:
        print(f'Scores for Event Number {event_counter} are:')

        all_ranks = one_event.split(',')
        all_ranks.reverse()
        for j in all_ranks:
            print(f'{j} = {(all_ranks.index(j) + 1) * 5}')
        event_counter += 1


def output_winners(): 
    rankings = open('Event_Data_team.csv', 'r')
    ec = 1
    print('Team Winners are: ')
    for r in rankings:
        all_ranks = r.split(',')
        print(f'Winner for Event Number {ec} is {all_ranks[0]}')
        ec += 1
    rankings = open('Event_Data_individual.csv', 'r')
    print('\n\nIndividual Winners are: ')
    for r in rankings:
        all_ranks = r.split(',')
        print(f'Winner for Event Number {ec} is {all_ranks[0]}')
        ec += 1


main()
