"""
Creator - MakeTheMaker
COMBAT SIMULATOR - Simulates fight between you and computer
"""

from tkinter import *
import random


# main_menu WINDOW
class Userinterface:
    def __init__(self):
        # creates main_menu window
        self.__main_menu = Tk()
        # attributes for main_menu window
        self.__main_menu.title("COMBAT SIMULATOR - MAIN MENU")
        self.__main_menu.geometry("820x650")
        self.__main_menu.configure(background="#8A0707")

        # Variable to detect which button is pressed
        self.__var = IntVar()
        self.__var.set(1)
        # self.__marauder, self.__duelist, self.__shadow = your character
        # choice for the game
        # self.__exit = exit button for exiting the program
        self.__canvas = Canvas(self.__main_menu, width=450, height=190,
                               highlightthickness=0, relief='ridge')
        self.__title = Label(self.__main_menu, text="ULTIMATE FIGHTING GAME",
                             font=("Algerian", 30, "bold", "underline"),
                             pady=20,
                             bg="#8A0707",
                             fg="white")
        self.__character_label = Label(self.__main_menu,
                                       text="Choose your character:",
                                       font=("Algerian", 10, "bold"), pady=10,
                                       bg="#8A0707",
                                       fg="white")
        self.__marauder = Radiobutton(self.__main_menu, text="Marauder",
                                      command=self.change_image,
                                      variable=self.__var, value=1,
                                      indicator=0,
                                      font=("Algerian", 10, "bold"), pady=10,
                                      bg="#8A0707", fg="black", width=10,
                                      relief=RAISED, borderwidth=5)
        self.__duelist = Radiobutton(self.__main_menu, text="Duelist",
                                     command=self.change_image,
                                     variable=self.__var, value=2, indicator=0,
                                     font=("Algerian", 10, "bold"), pady=10,
                                     bg="#8A0707", fg="black", width=10,
                                     relief=RAISED, borderwidth=5)
        self.__shadow = Radiobutton(self.__main_menu, text="Shadow",
                                    command=self.change_image,
                                    variable=self.__var, value=3, indicator=0,
                                    font=("Algerian", 10, "bold"), pady=10,
                                    bg="#8A0707", fg="black", width=10,
                                    relief=RAISED, borderwidth=5)
        self.__fight_button = Button(self.__main_menu, command=self.fight,
                                     text="FIGHT!",
                                     font=("Algerian", 20, "bold"), pady=20,
                                     bg="#8A0707", fg="black", relief=RAISED,
                                     borderwidth=5)
        self.__exit = Button(self.__main_menu, text="Exit", command=exit)

        # adds image to main menu window
        self.__img = PhotoImage(file="marauder.png")
        self.__canvas.create_image(0, 0, anchor=NW, image=self.__img)

        # Component placement on gui
        self.__exit.pack(fill=X, side=BOTTOM)
        self.__title.pack()
        self.__canvas.pack(pady=20)
        self.__character_label.pack()
        self.__marauder.pack()
        self.__duelist.pack()
        self.__shadow.pack()
        self.__fight_button.pack()
        self.__main_menu.mainloop()

    def fight(self):
        """
        Your character selection which carries over to gameplay class.
        Checks which character you chose.
        Closes main_menu window and opens gameplay window.
        """
        global character_class
        selection = self.__var.get()
        if selection == 1:
            character_class = "marauder"
            self.__main_menu.destroy()
            Gameplay()
        elif selection == 2:
            character_class = "duelist"
            self.__main_menu.destroy()
            Gameplay()
        elif selection == 3:
            character_class = "shadow"
            self.__main_menu.destroy()
            Gameplay()

    def change_image(self):
        """
        Changes the image in the main menu according to radiobutton selection
        """
        selection = self.__var.get()
        if selection == 1:
            self.__img = PhotoImage(file="marauder.png")
            self.__canvas.create_image(0, 0, anchor=NW, image=self.__img)
        elif selection == 2:
            self.__img = PhotoImage(file="duelist.png")
            self.__canvas.create_image(0, 0, anchor=NW, image=self.__img)
        elif selection == 3:
            self.__img = PhotoImage(file="shadow.png")
            self.__canvas.create_image(0, 0, anchor=NW, image=self.__img)

    def start(self):
        """
        Starts the mainloop.
        """
        self.__main_menu.mainloop()


################ GAMEPLAY WINDOW ################

class Gameplay:
    def __init__(self):
        # parameter to define if you win/lose
        self.__winlose = 0
        # Defines modifiers for player chosen class
        # self.__amodifier = attack a(punch) modifier
        # self.__bmodifier = attack b(kick) modifier
        # self.__cmodifier = attack c(headbutt) modifier
        # health = current health
        # basehp = base health
        if character_class == "shadow":
            self.__amodifier = 1.4
            self.__bmodifier = 0.45
            self.__cmodifier = 0.2
            self.__health = 100
            self.__basehp = 100
        elif character_class == "duelist":
            self.__amodifier = 0.7
            self.__bmodifier = 1.4
            self.__cmodifier = 1.1
            self.__health = 150
            self.__basehp = 150
        elif character_class == "marauder":
            self.__amodifier = 0.4
            self.__bmodifier = 0.4
            self.__cmodifier = 1.8
            self.__health = 200
            self.__basehp = 200

        # enemy modifiers
        # self.__enemy_health = enemy health depends on your health
        # self.__emodifier = enemy damage modifier
        # self.__ebasehp = enemy base health
        self.__enemy_health = int(round(self.__health * 1.25))
        self.__emodifier = 1.32
        self.__ebasehp = self.__enemy_health

        # Creates userinterface for the fight window
        self.__fightwindow = Tk()
        # attributes for the fight window
        self.__fightwindow.title("COMBAT SIMULATOR - Fight")
        self.__fightwindow.geometry("820x900")
        self.__fightwindow.configure(background="#c2b280")
        self.__canvas1 = Canvas(self.__fightwindow, width=450, height=190,
                                highlightthickness=0, relief='ridge')
        self.__canvas2 = Canvas(self.__fightwindow, width=450, height=190,
                                highlightthickness=0, relief='ridge')
        # self.__player = player name
        # self.__health_display = shows your (current health / max health)
        # self.__enemy = enemy name
        # self.__enemy_health_display = shows enemy's (current health / max health)
        # self.__punch = punch attack selection goes to punch method
        # self.__kick = kick attack selection goes to kick method
        # self.__headbutt = headbutt attack selection goes to headbutt method
        # self.__restart = by pressing button goes to main main_menu
        # self.__exit = by pressing button exits the program
        # self.__enemymove = tells enemy movement, damage and hit
        # self.__playermove = tells damage inflicted and did it hit
        # self.__winner = tells the winner of the fight
        self.__player = Label(self.__fightwindow, text=f"{character_class}",
                              font=("Algerian", 24, "bold"), bg="#c2b280")
        self.__health_display = Label(self.__fightwindow, text=(
                "Health: " + str(self.__health) + "/" + str(self.__basehp)),
                                      font=("Courier", 18), bg="#c2b280")
        self.__enemy = Label(self.__fightwindow, text="Daresso",
                             font=("Algerian", 24, "bold"), bg="#c2b280")
        self.__enemy_health_display = Label(self.__fightwindow, bg="#c2b280",
                text=("Health: " + str(self.__enemy_health) + "/" +
                str(self.__ebasehp)), font=("Courier", 18, "bold"))
        self.__punch = Button(self.__fightwindow, text="Punch", width=10,
                              command=self.punch)
        self.__kick = Button(self.__fightwindow, text="Kick", width=10,
                             command=self.kick)
        self.__headbutt = Button(self.__fightwindow, text="Headbutt", width=10,
                                 command=self.headbutt)
        self.__restart = Button(self.__fightwindow, text="Restart",
                                command=self.restart)
        self.__exit = Button(self.__fightwindow, text="Exit", command=exit)
        self.__enemymove = Label(self.__fightwindow, text="",
                                 font=("Courier", 14),
                                 bg="#c2b280", fg="black")
        self.__playermove = Label(self.__fightwindow, text="",
                                  font=("Courier", 14),
                                  bg="#c2b280", fg="black")
        self.__winner = Label(self.__fightwindow, text="",
                              font=("Courier", 14, "bold"),
                              bg="#c2b280", fg="black")

        # adds images to main menu window
        self.__img1 = PhotoImage(file=f"{character_class}.png")
        self.__img2 = PhotoImage(file="enemy.png")
        self.__canvas1.create_image(0, 0, anchor=NW, image=self.__img1)
        self.__canvas2.create_image(0, 0, anchor=NW, image=self.__img2)

        self.__exit.pack(fill=X, side=BOTTOM)
        self.__player.pack(pady=10, padx=100, fill=X)
        self.__canvas1.pack(pady=10)
        self.__health_display.pack()
        self.__punch.pack(pady=5)
        self.__kick.pack(pady=5)
        self.__headbutt.pack(pady=5)
        self.__playermove.pack()
        self.__enemy.pack(pady=10, padx=20, fill=X)
        self.__canvas2.pack(pady=10)
        self.__enemy_health_display.pack()
        self.__enemymove.pack()
        self.__restart.pack(fill=X, side=BOTTOM)
        self.__winner.pack(side=BOTTOM)
        self.__fightwindow.mainloop()

    def player_win(self):
        """
        If enemy health is 0 or under
        the method configures victory text to self.__winner label
        """
        if self.__enemy_health <= 0:
            self.__enemy_health_display.configure(
                text="Health: 0" + "/" + str(self.__ebasehp))
            self.__winlose = 1
            self.__winner.configure(text="Fatality! Flawless victory!",
                                    font=("Algerian", 30, "bold"))

    def enemy_win(self):
        """
        If player health is 0 or under
        the method configures lost text to self.__winner label
        """
        if self.__health <= 0:
            self.__health_display.configure(
                text="Health: 0" + "/" + str(self.__basehp))
            self.__winlose = 1
            self.__winner.configure(text="Fatality! You lose!",
                                    font=("Algerian", 30, "bold"))

    def enemy_attack(self):
        """
        First in this method we use random functions check which attack
        enemy uses number between 0-13(enemy_attack) and does
        it miss(miss_check) number between 0-13.If attack hits random
        function(dmgdealt) calculates how much damage is dealt.
        Changes attributes depending on how much damage is done,
        how much hp is lost and which move was used.
        """
        if self.__winlose != 1:

            miss_check = random.randint(0, 13)
            enemy_attack = random.randint(0, 13)

            if enemy_attack >= 5:
                if miss_check >= 11:
                    self.__enemymove.configure(text="Enemy attack missed")
                else:
                    # calculates how much damage is done
                    dmgdealt = int(
                        round(random.randint(10, 20) * self.__emodifier))
                    # takes damage done away from health
                    self.__health -= dmgdealt
                    # new configures for labels
                    self.__health_display.configure(
                        text="Health: " + str(
                            int(round(self.__health))) + "/" + str(
                            self.__basehp))
                    self.__enemymove.configure(
                        text="Daresso used: Punch(Damage dealt: " + (
                            str(f'{dmgdealt:.0f}')) + ")")

            elif enemy_attack >= 10:
                if miss_check >= 10:
                    self.__enemymove.configure(text="Enemy attack missed")
                else:
                    # calculates how much damage is done
                    dmgdealt = int(
                        round(random.randint(14, 26) * self.__emodifier))
                    # takes damage done away from health
                    self.__health -= dmgdealt
                    # new configures for labels
                    self.__health_display.configure(
                        text="Health: " + str(self.__health) + "/" + str(
                            self.__basehp))
                    self.__enemymove.configure(
                        text="Daresso used: Kick(Damage dealt: " + (
                            str(f'{dmgdealt:.0f}')) + ")")

            elif enemy_attack <= 4:
                chance = 1
                damage = 0
                # loop keeps adding damage as long as chance is under 7
                while chance < 7:
                    # calculates how much damage is done
                    dmgdealt = random.randint(2, 7) * self.__emodifier
                    # sums up damage done
                    damage += int(round(dmgdealt))
                    self.__health -= dmgdealt
                    # randomizes new number between 0-11 to chance
                    chance = int(round(random.randint(0, 11)))
                    self.__health_display.configure(text="Health: " + str(
                        int(round(self.__health))) + "/" + str(
                        self.__basehp))

                self.__enemymove.configure(
                    text="Daresso used: headbutt(Damage dealt: " + (
                        str(damage)) + ")")

    def punch(self):
        """
        Players punch attack, first random function is used
        to test if it hits(miss_check). If punch hits punch damage is
        calculated and attributes are configured accordingly.
        """
        if self.__winlose != 1:
            miss_check = random.randint(0, 13)
            if miss_check >= 11:
                self.__playermove.configure(text="Your attack missed!")
            else:
                # calculates how much damage you do
                dmgdealt = int(
                    round(random.randint(9, 21) * self.__amodifier))
                # damage done is taken from enemy health
                self.__enemy_health -= dmgdealt
                # labels are reconfigured
                self.__enemy_health_display.configure(
                    text="Health: " + str(int(round(self.__enemy_health))) +
                         "/" + str(self.__ebasehp))
                self.__playermove.configure(
                    text="Damage dealt to enemy: " + str(f'{dmgdealt:.0f}'))
            # method self.player_win() checks if enemy health is 0 or under
            # otherwise self.enemy_attack() is called which is enemy's hit
            # method self.enemy_win() checks if player health
            # is 0 or under after enemy's hit
            self.player_win()
            self.enemy_attack()
            self.enemy_win()

    def kick(self):
        """
        Players kick attack, first random function is used
        to test if it hits(miss_check). If kick hits kick damage is
        calculated and attributes are configured accordingly.
        """
        if self.__winlose != 1:
            miss_check = random.randint(0, 13)
            if miss_check >= 10:
                self.__playermove.configure(text="Your attack missed!")
            else:
                # calculates how much damage you do
                dmgdealt = int(
                    round(random.randint(14, 26) * self.__bmodifier))
                # damage done is taken from enemy health
                self.__enemy_health -= dmgdealt
                # labels are reconfigured
                self.__enemy_health_display.configure(text="Health: " + str(
                    int(round(self.__enemy_health))) + "/" + str(
                    self.__ebasehp))
                self.__playermove.configure(
                    text="Damage dealt to enemy: " + str(f'{dmgdealt:.0f}'))
            # method self.player_win() checks if enemy health is 0 or under
            # otherwise self.enemy_attack() is called which is enemy's hit
            # method self.enemy_win() checks if player health
            # is 0 or under after enemy's hit
            self.player_win()
            self.enemy_attack()
            self.enemy_win()

    def headbutt(self):
        """
        Players headbutt attack, Headbutt can't miss. It loops as long as
        chance is under 7. It keeps adding damage to hit as long as loop
        continues. Configures attributes accordingly after that.
        """
        if self.__winlose != 1:
            chance = 1
            damage = 0
            while chance < 7:
                # calculates how much damage is done
                dmgdealt = random.randint(2, 7) * self.__cmodifier
                # sums up damage dealt
                damage += dmgdealt
                # damage dealt is taken from enemy hp
                self.__enemy_health -= dmgdealt
                # randomizes new number between 0-11 to chance
                chance = int(round(random.randint(0, 11)))
                # labels are reconfigured
                self.__enemy_health_display.configure(
                    text="Health: " + str(
                        int(round(self.__enemy_health))) + "/" + str(
                        self.__ebasehp))

            self.__playermove.configure(
                text="Damage dealt to enemy: " + str(f'{dmgdealt:.0f}'))
            # method self.player_win() checks if enemy health is 0 or under
            # otherwise self.enemy_attack() is called which is enemy's hit
            # method self.enemy_win() checks if player health
            # is 0 or under after enemy's hit
            self.player_win()
            self.enemy_attack()
            self.enemy_win()

    def restart(self):
        """
        Shutdowns fight window and goes back to main menu
        """
        self.__fightwindow.destroy()
        Userinterface()


def main():
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
