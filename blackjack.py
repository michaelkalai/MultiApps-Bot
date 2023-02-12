import discord
from discord.ext import commands
import random


class Blackjack(discord.ui.View):
    def __init__(self, bet, player):
        super().__init__()
        self.player = player
        self.bet = bet
        self.player_score = 0
        self.bot = "Myriad"
        self.bot_score = random.randint(17, 22)
        self.card_types = [":clubs:", ":spades:", ":hearts:", ":diamonds:"]
        self.hand = []
        self.aces = []
        self.winner = None

    def emb(self, message=""):
        display = ""
        for card in self.hand:
            display += card
            if card != self.hand[-1]:
                display += "\n"

        embed = discord.Embed(color=0xFF5733)
        embed.add_field(name="Blackjack", value="First to 21 wins")
        embed.add_field(name="Your Hand", value=display)
        embed.add_field(message)

        return embed

    def con_num_to_card(self, num):
        if num == 11:
            return "Jack"
        elif num == 12:
            return "Queen"
        elif num == 13:
            return "King"
        return num

    def check_ace(self):
        for ace in self.aces:
            if self.points > 21:
                if ace[1] == 11:
                    self.points -= 10
                    ace[1] = 1

    def add_points(self, num):
        if num == 11 or num == 12 or num == 13:
            self.player_score += 10
        elif num == 1:
            self.player_score += 11
        else:
            self.player_score += num

    def deal_card(self):
        num = random.randint(1, 13)
        card_type = self.card_types[random.randint(0, 3)],
        card_num = self.con_num_to_card(num)
        card = card_type + str(card_num)
        if card_num == 1:
            self.aces.append([card, 11])
        self.add_points(num)
        self.check_ace()
        self.hand.append(card)
        return card

    def check_for_bust(self, user):
        if self.player == user and self.player_score > 21:
            return True
        elif self.bot == user and self.bot_score > 21:
            return True
        return False

    def game_over(self):
        if self.check_for_bust(self.player):
            return self.bot
        elif self.check_for_bust(self.bot):
            return self.player
        elif self.bot_score > self.player_score:
            return self.bot
        else:
            return self.player

    @discord.ui.button(label="Hold", style=discord.ButtonStyle.grey)
    async def menu1(self, interaction: discord.Interaction,
                    button: discord.ui.Button):
        print(interaction.user)
        await interaction.response.send_message("You chose to Hold")

    @discord.ui.button(label="Hit", style=discord.ButtonStyle.grey)
    async def menu2(self, interaction: discord.Interaction,
                    button: discord.ui.Button):
        if self.player_score < 21:
            self.deal_card()
        elif self.player_score > 21:
            button.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.edit_message(
                embed=self.emb("You Have Reached 21 cards"),
                message_id=interaction.message.id)
        else:
            button.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.edit_message(
                embed=self.emb("You Have Reached 21 cards"),
                message_id=interaction.message.id)

            await interaction.response.send_message()

        # await interaction.response.send_message("You chose to Hit")
        # await interaction.followup.send_message("Mop")
