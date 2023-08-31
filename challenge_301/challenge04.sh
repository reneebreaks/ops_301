#!/bin/bash

#ostype = $OSTYPE

while true; do
    clear
    echo "Hello human. I am a simple program, I can only perform a few simple tasks. Please choose one: "
    echo "1. Say Hello to the World"
    echo "2. Ping your machine"
    echo "3. Check your IP address"
    echo "4. Exit"
    read choice
    

    if [[ $choice == 1 ]]; then
        echo "Hello, World!"
        read -p "Press Enter to continue"
    elif [[ $choice == 2 ]]; then
        ping -c 3 localhost
        read -p "Press Enter to continue"
    elif [[ $choice == 3 ]]; then
       
        while true; do
            clear
            echo "What is your operating system?: " ostype
            echo "1. Linux"
            echo "2. MacOS"
            echo "3. Windows"
            echo "4. Return to main menu"
            read ostype

       
            if [[ "$ostype" == 1 ]]; then
                ip a
                read -p "Press Enter to continue"
            elif [[ "$ostype" == 2 ]]; then
                ifconfig
                read -p "Press Enter to continue"
            elif [[ "$ostype" == 3 ]]; then
                ip a
                read -p "Press Enter to continue"
            elif [[ $ostype == 4 ]]; then
                echo "Exiting."
                break 
            else
                echo "Invalid choice"
                read -p "Press Enter to continue"
            fi
        done

    
       
    elif [[ $choice == 4 ]]; then
        echo "See ya later!"
        exit 0
    else
        echo "Invalid choice"
        read -p "Press Enter to continue"
    fi
done  

#End