from random import randint
game_running = True
game_results = []

def cl_zombie_attack():
    return randint(zombie['attack_min'], zombie['attack_max'])


def game_ends(winner_name):
    print(f'{winner_name} won the game')



while game_running == True:
    counter = 0
    new_round = True
    player = {'name': 'MedOne', 'attack': 13, 'heal': 20, 'health': 100}
    zombie = {'name': 'Zombie Level 1', 'attack_min': 10, 'attack_max': 20, 'health': 100}
    print('---' * 7)
    print('Enter Player name')
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(zombie['name'] + ' has ' + str(zombie['health']) + ' health')

    while new_round == True:
        counter = counter + 1
            

        player_won = False
        zombie_won = False
        print('---' * 7)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit')
        print('4) Show results')

        player_choice = input()
        

        if player_choice == '1':
            zombie['health'] = zombie['health'] - player['attack']
            if zombie['health'] <= 0:
                player_won = True
            else: 
                
                player['health'] = player['health'] - cl_zombie_attack()
                if player['health'] <= 0:
                    zombie_won = True
            
            
        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']
            zombie_attack = randint(zombie['attack_min'], zombie['attack_max'])
            player['health'] = player['health'] - zombie_attack
            if player['health'] <= 0:
                zombie_won = True
            
        elif player_choice == '3':
            new_round = False
            game_running = False

        elif player_choice == '4':
            for p_stats in game_results:
                print(p_stats)
            #print(game_results)


        else:
            print('Invalid Input')

        if player_won == False and zombie_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print(zombie['name'] + ' has ' + str(zombie['health']) + ' left')

        elif player_won:
            game_ends(player['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter} 
            game_results.append(round_result)
            
            #print(round_result)           

        elif zombie_won:
            game_ends(zombie['name'])
            round_result = {'name': zombie['name'],
                            'health': zombie['health'], 'rounds': counter}
            game_results.append(round_result)
            
            #print(round_result)

        if player_won == True or zombie_won == True:
            new_round = False






