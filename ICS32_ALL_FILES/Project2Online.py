###Joshua Pascascio ID: 52192782
### Heran Patel: 62984531

import socket
import ICS32_common_func
import connectfour
import socketMethods
from collections import namedtuple

display = ICS32_common_func.display_screen
take_turn = ICS32_common_func.take_a_turn
make_Move = ICS32_common_func.read_move

def print_winner(response:str) -> None:
    """Outputs the winner of the online game in a cheeky fashion depending on the final input
    from the connect four server"""
    if response == 'WINNER_YELLOW':
        print("The yellow token has won")
        print("You have lost to a UC Irvine computer server")
    else:
        print("The red token has won")
        print("You have beaten the UC Irvine computer, for now ...")
def play_game(socketStructure):
    """Main game structure of the online game, red is user player, server is yellow, takes servers input and parses it into
    format that can be used take_turn and exchanges turns accordingly"""
    game_Winner = ICS32_common_func.NONE
    starting_game = connectfour.new_game()
    response = None
    while(game_Winner == ICS32_common_func.NONE):
        try:
            ai_Move = None
            if starting_game.turn == ICS32_common_func.YELLOW:
                for i in range(2):
                    response = socketMethods.recv_message(socketStructure)
                    print(response)
                    if type(response) == str:
                        ai_Move = response.split()
                        if (ai_Move[0] == 'DROP' or ai_Move[0] == 'POP'):
                            ai_Move[1] = int(ai_Move[1]) - 1
                            game_Winner, starting_game = take_turn(starting_game, ai_Move)
                            display(starting_game)
                continue
            if starting_game.turn == ICS32_common_func.RED:
                user_Inputs = make_Move()
                action = user_Inputs[0].upper()
                send_string = action + " " + str(user_Inputs[1] + 1)
                socketMethods.send_message(socketStructure, send_string)
                response = socketMethods.recv_message(socketStructure)
                if response == 'INVALID':
                    print(response)
                    response = socketMethods.recv_message(socketStructure)
                    print(response)
                    continue
                game_Winner,starting_game = take_turn(starting_game, user_Inputs)
                display(starting_game)
                print(response)
        except:
            print("I will figure it out later")
            ##raise ServerError
    socketMethods.close(socketStructure)
    print_winner(response)

def try_Reconnect():
    choice = input("Would you like to try to connect again, possibly another server?  ")
    while choice.lower().strip() != "yes" and choice.lower().strip() != "no":
        choice = input("I'm sorry I didn't understand, say that again:  ")
    if choice.lower().strip() == "no":
        return
    elif choice.lower().strip() == "yes":
        interact()
class ServerError(Exception):
    pass
def interact():
    """Core interface that implements the play game function, will connect to the server and
    if valid, will send valid inputs to start a connect four game with the server and print the winner"""
    try:
        serverSockets = socketMethods.establish_connection()
        if serverSockets == None:
            return
        userName = input("Please create a user name:  ")
        user_Chars = userName.split()
        check_user = ""
        for e in user_Chars:
            check_user += e
        while userName != check_user:
            print("User Name must not contain spaces!")
            userName = input("Please create a user name:  ")
            user_Chars = userName.split()
            check_user = ""
            for e in user_Chars:
                check_user += e
        hello_string = 'I32CFSP_HELLO ' + userName
        socketMethods.send_message(serverSockets, hello_string)
        response = socketMethods.recv_message(serverSockets)
        right_Server_Check = "WELCOME " + userName
        if response.startswith(right_Server_Check) == False:
            raise ServerError
        print(response)
        socketMethods.send_message(serverSockets, 'AI_GAME')
        response = socketMethods.recv_message(serverSockets)
        print(response)
        play_game(serverSockets)
    except ConnectionError:
        print("There was a connection error")
        return try_Reconnect()
    except ConnectionRefusedError:
        print("There was a connection error")
        print("It appears the server does not want you to connect to it")
        return try_Reconnect()
    except ConnectionAbortedError:
        print("The connection was aborted, you may have been disconnected from the server or internet")
        return try_Reconnect()
    except ConnectionResetError:
        print("The connection was reset")
        return try_Reconnect()
    except TimeoutError:
        print("The connection has timed out")
        return try_Reconnect()
    except socket.gaierror:
        print("You entered eiter an invalid or non-existent host or port Number please try again")
        interact()
    
if __name__ == '__main__':
    interact()
