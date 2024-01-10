import asyncpg, time, random, discord, asyncio
from discord.ext import commands
from sys import platform
from discord.commands import slash_command, Option, permissions


guildIDs = [929594969000390696, 580587544287379456, 340253890643755009, 765005927619231774, 691147057796218905, 389113239159439361, 621423558886817820, 943741853239492688, 1040888019906994186]
currency_name = "BeeBucks"
banchannels = [1040859151833772083, 1040859197417459763, 1040859197417459763]

class Casino(commands.Cog):
    """
    Gaming
    """
    def __init__(self, bot):
        self.bot = bot
        if platform.startswith("lin"):
            self.path = "/root/serverkitten/media/"
        else:
            self.path = "./media/"

    @slash_command(name = "blackjack", description = "lets you play a hand of blackjack")
    async def blackjack(self, ctx: commands.Context, wager: Option(int, "Bet Size", required = True, min_value = 1)):
        if ctx.channel.id in banchannels:
            await ctx.send("This game is restricted in this channel, please try again elsewhere")
            return
        
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")
        bal = result[0]['coins']
        result1 = await db.fetch(f"SELECT bj_wins, bj_losses FROM gamblingstats WHERE guild_id = '{ctx.author.guild.id}' AND user_id = '{ctx.author.id}'")
        if result1 == []:
            sql = f"INSERT INTO gamblingstats(guild_id, user_id, bj_wins, bj_losses, ban_win_streak, best_coinflip, coinswon, coinslost) VALUES($1, $2, $3, $4, $5, $6, $7, $8)"
            await db.execute(sql, str(ctx.guild.id), str(ctx.author.id), 0, 0, 0, 0, 0, 0)
            result1 = await db.fetch(f"SELECT bj_wins, bj_losses FROM gamblingstats WHERE guild_id = '{ctx.author.guild.id}' AND user_id = '{ctx.author.id}'")
            
        if result == []:
            await ctx.respond("You are not entered into the system, please send a message then try again.")
            return
        
            
        elif wager > bal:
            await ctx.respond("Your bet is greater than your coin balance, please bet an amount you actually have and try again")
            return
        else:
            def cardCheck(card:str=None):
                if card == None:
                    return 0
                elif "A" in card:
                    return 1
                elif "2" in card:
                    return 2
                elif "3" in card:
                    return 3
                elif "4" in card:
                    return 4
                elif "5" in card:
                    return 5
                elif "6" in card:
                    return 6
                elif "7" in card:
                    return 7
                elif "8" in card:
                    return 8
                elif "9" in card:
                    return 9
                elif "10" in card:
                    return 10
                elif "J" in card:
                    return 10
                elif "Q" in card:
                    return 10
                elif "K" in card:
                    return 10

            deck = ["A♠️","2♠️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️",
                    "A♥️","2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️",
                    "A♦️","2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️",
                    "A♣️","2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️"]

            playerAceCount = 0
            dealerAceCount = 0
            playerWon = False
            playerBlkJk = False
            playerBust = False
            dealerBlkJk = False
            dealerBust = False
            playerPass = False
            dealerPass = False
            playerCards = []
            dealerCards = []
            playerDealOne = random.choice(deck)
            # playerDealOne = deck[0]
            playerCards.append(playerDealOne)
            deck.remove(playerDealOne)
            playerScore = cardCheck(playerDealOne)
            if cardCheck(playerDealOne) == 1:
                playerAceCount = 1
            playerDealTwo  = random.choice(deck)
            playerCards.append(playerDealTwo)
            playerScore = playerScore + cardCheck(playerDealTwo)
            if cardCheck(playerDealTwo) == 1:
                playerAceCount = playerAceCount + 1
            deck.remove(playerDealTwo)
            if playerAceCount == 0:
                await ctx.respond(f"Your cards are {playerDealOne} and {playerDealTwo}, your current score is {playerScore}")
                await asyncio.sleep(2)
            elif playerAceCount == 1:
                await ctx.respond(f"Your cards are {playerDealOne} and {playerDealTwo}, your current score is {playerScore} or {playerScore + 10}")
                await asyncio.sleep(2)
                if playerScore == 11:
                    playerBlkJk = True
                    playerScore = 21
            dealerDealFU = random.choice(deck)
            dealerCards.append(dealerDealFU)
            deck.remove(dealerDealFU)
            dealerScore = cardCheck(dealerDealFU)                
            if cardCheck(dealerDealFU) == 1:
                dealerAceCount = 1
            dealerDealFD  = random.choice(deck)
            dealerCards.append(dealerDealFD)
            deck.remove(dealerDealFD)
            dealerScore = dealerScore + cardCheck(dealerDealFD)
            if cardCheck(dealerDealFD) == 1:
                dealerAceCount = dealerAceCount + 1
            if cardCheck(dealerDealFU) == 1:
                await ctx.send(f"The dealer's face up card is {dealerDealFU}, and their current score is {cardCheck(dealerDealFU)} or {cardCheck(dealerDealFU) + 10}")
                await asyncio.sleep(2)
            else:
                await ctx.send(f"The dealer's face up card is {dealerDealFU} and their current score is {cardCheck(dealerDealFU)}")
                await asyncio.sleep(2)
            if dealerScore == 11 and dealerAceCount == 1:
                dealerBlkJk = True
                dealerScore = 21
            if playerBlkJk == True and dealerBlkJk == True:
                await ctx.send("Both you and the dealer hit natural Blackjacks, all bets are cancelled")
                return

            if playerBlkJk == False and dealerBlkJk == False:
                while playerBlkJk == False and playerBust == False and playerPass == False:
                    def check(msg):
                        return msg.author == ctx.author and msg.channel == ctx.channel and \
                        len(msg.content) <= 32
                    await ctx.send("would you like to hit or stand?")
                    try:
                        msg = await self.bot.wait_for("message", check=check, timeout=30)
                    except asyncio.TimeoutError:
                        await ctx.send("You took too long to respond and forfeited the game!")
                        return

                    if msg.content.lower() == 'stand':
                        await ctx.send(f"you have chosen to stand on your cards {(' '.join(playerCards))} and action is now on the dealer")
                        await asyncio.sleep(2)
                        playerPass = True
                    elif msg.content.lower() == 'hit':
                        playerHitCard = random.choice(deck)
                        if cardCheck(playerHitCard) == 1:
                            playerAceCount = playerAceCount + 1
                        playerCards.append(playerHitCard)
                        deck.remove(playerHitCard)
                        await ctx.send(f"you have been dealt the {playerHitCard}")
                        playerScore = playerScore + cardCheck(playerHitCard)
                        if playerAceCount == 1:
                            await ctx.send(f"You now have the cards {(' '.join(playerCards))} and have a score of {playerScore} or {playerScore + 10}")
                        else:
                            await ctx.send(f"You now have the cards {(' '.join(playerCards))} and have a score of {playerScore}")
                            await asyncio.sleep(2)
                        if playerScore > 21:
                            playerBust = True
                        elif playerScore == 21:
                            playerBlkJk = True
                        elif playerAceCount == 1:
                            if playerScore + 10 == 21:
                                playerBlkJk = True
                                playerScore = 21
                        else:
                            continue
                    else:
                        await ctx.send("that is not hit or pass, please try again")
                        continue

            if playerBust == False:    
                if dealerAceCount == 0:
                    await ctx.send(f"The dealer's cards are {dealerDealFU} and {dealerDealFD} giving him a score of {dealerScore}")
                else:
                    await ctx.send(f"The dealer's cards are {dealerDealFU} and {dealerDealFD} giving him a score of {dealerScore} or {dealerScore + 10}")
                await asyncio.sleep(2)

            if playerBlkJk == False and dealerBlkJk == False and playerBust == False:
                while dealerBlkJk == False and dealerBust == False and dealerPass == False:
                    if dealerScore > 16:
                        dealerPass = True
                    elif dealerAceCount == 1 and dealerScore > 6:
                        dealerPass = True
                    else:
                        dealerHitCard = random.choice(deck)
                        if cardCheck(dealerHitCard) == 1:
                            dealerAceCount = dealerAceCount + 1
                        dealerCards.append(dealerHitCard)
                        deck.remove(dealerHitCard)
                        dealerScore = dealerScore + cardCheck(dealerHitCard)
                        await ctx.send(f"The dealer has received the {dealerHitCard}")
                        if dealerAceCount != 1:
                            await ctx.send(f"The dealer now has the cards {(' '.join(dealerCards))} and a score of {dealerScore}")
                        else:
                            await ctx.send(f"The dealer now has the cards {(' '.join(dealerCards))} giving him a score of {dealerScore} or {dealerScore + 10}")
                        await asyncio.sleep(2)

                    if dealerScore > 21:
                        dealerBust = True
                    elif dealerScore == 21:
                        dealerBlkJk = True
                    elif dealerScore > playerScore:
                        dealerPass = True
                    elif dealerAceCount == 1:
                        if dealerScore + 10 == 21:
                            dealerBlkJk = True
                            dealerScore = 21
                        elif dealerScore + 10 > playerScore and dealerScore + 10 < 21:
                            dealerPass = True
                    else:
                        continue

            if playerBlkJk == True or dealerBust == True or playerScore > dealerScore or (playerAceCount == 1 and playerScore + 10 > dealerScore and playerScore + 10 < 21):
                playerWon = True

            elif (playerScore == dealerScore) or (playerAceCount == 1 and playerScore + 10 == dealerScore) or (dealerAceCount == 1 and dealerScore + 10 == playerScore):
                await ctx.send("You and the dealer have the same hand score, all bets are cancelled.")
                return
            if playerBust == True or dealerBlkJk == True:
                playerWon = False
            if dealerAceCount == 1 and dealerScore + 10 > playerScore and dealerScore + 10 < 21:
                playerWon = False

            db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')

            balance = result[0]['coins']
            win_count = result1[0]['bj_wins']
            loss_count = result1[0]['bj_losses']

            if playerWon:
                winbal = balance + wager
                win_count = win_count + 1
                sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
                sql1 = "UPDATE gamblingstats SET bj_wins = $1 WHERE guild_id = $2 AND user_id = $3"
                await db.execute(sql, winbal, str(ctx.author.guild.id), str(ctx.author.id))
                await db.execute(sql1, win_count, str(ctx.author.guild.id), str(ctx.author.id))

                if playerBlkJk == True:
                    await ctx.send(f"Congratulations, you hit Blackjack and won {wager} {currency_name}, and now have a total of {winbal} {currency_name}!")
                elif dealerBust == True:
                    await ctx.send(f"The dealer busted and you won {wager} {currency_name}, and now have a total of {winbal} {currency_name}!")
                else:
                    await ctx.send(f"Congratulations, you made a higher value hand than the dealer and won {wager} {currency_name}, and now have a total of {winbal} {currency_name}!")
            else:
                lossbal = balance - wager
                loss_count = loss_count + 1
                sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
                sql1 = "UPDATE gamblingstats SET bj_losses = $1 WHERE guild_id = $2 AND user_id = $3"
                await db.execute(sql, lossbal, str(ctx.author.guild.id), str(ctx.author.id))
                await db.execute(sql1, loss_count, str(ctx.author.guild.id), str(ctx.author.id))
                if playerBust == True:
                    await ctx.send(f"Sorry, you busted and lost {wager} {currency_name}, and now have a total of {lossbal} {currency_name}.")
                elif dealerBlkJk == True:
                    await ctx.send(f"Sorry, the dealer hit Blackjack and you lost {wager} {currency_name}, and now have a total of {lossbal} {currency_name}.")
                else:
                    await ctx.send(f"Sorry, you have lost the hand and lost {wager} {currency_name}, and now have a total of {lossbal} {currency_name}.")



    # roulette that gives coins for winning and takes them away for losing
    @slash_command(name = "roulette", description = f"Correctly guess a 6 sided die roll to win {currency_name}.  Costs 25 {currency_name} to play")
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def roulette(self, ctx: commands.Context, guess: Option(int, "any number from 1-6", required = True), min_value = 1, max_value = 6):

        if ctx.channel.id in banchannels:
            await ctx.send("This game is restricted in this channel, please try again elsewhere")
            return
        isWinner = False

        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")
        if result == []:
            await ctx.respond("You are not entered into the system, please send a message then try again.")
            return
        balance = result[0]['coins']
        result1 = await db.fetch(f"SELECT coinswon, coinslost FROM gamblingstats WHERE guild_id = '{ctx.author.guild.id}' AND user_id = '{ctx.author.id}'")
        if result1 == []:
            sql = f"INSERT INTO gamblingstats(guild_id, user_id, bj_wins, bj_losses, ban_win_streak, best_coinflip, coinswon, coinslost) VALUES($1, $2, $3, $4, $5, $6, $7, $8)"
            await db.execute(sql, str(ctx.guild.id), str(ctx.author.id), 0, 0, 0, 0, 0, 0)
            result1 = await db.fetch(f"SELECT coinswon, coinslost FROM gamblingstats WHERE guild_id = '{ctx.author.guild.id}' AND user_id = '{ctx.author.id}'")

        if balance < 25:
            await ctx.respond(f"You don't have the {currency_name} to play this")
            return

        else:
            randNum = random.randrange(1, 7)

            randCoins = random.randrange(140, 161)
            if guess == randNum:
                await ctx.respond(f"you guessed the number correctly, congratulations!  You've won {randCoins} {currency_name}")
                isWinner = True
            else:
                await ctx.respond(f"Your guess was incorrect, the winning number was `{randNum}`")

            if isWinner:
                new_balance = balance + randCoins
                coinswon_new = result1[0]['coinswon'] + randCoins
                sql = "UPDATE gamblestats SET coinswon = $1 WHERE guild_id = $2 AND user_id = $3"
                await db.execute(sql, coinswon_new, str(ctx.author.guild.id), str(ctx.author.id))
            else:
                new_balance = balance - 25
                coinslost_new = result1[0]['coinslost'] + 25
                sql = "UPDATE gamblestats SET coinslost = $1 WHERE guild_id = $2 AND user_id = $3"
                await db.execute(sql, coinslost_new, str(ctx.author.guild.id), str(ctx.author.id))
            sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql, new_balance, str(ctx.author.guild.id), str(ctx.author.id))


    @roulette.error
    async def roulette_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(f'Please wait {error.retry_after:.2f} seconds and then try again')

            
    @slash_command(name = "d20", description = f"Correctly guess a 20 sided die roll to win {currency_name}.  Costs 100 {currency_name} to play")
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def d20(self, ctx: commands.Context, guess: Option(int, "any number from 1-20", required = True), min_value = 1, max_value = 20):

        if ctx.channel.id in banchannels:
            await ctx.send("This game is restricted in this channel, please try again elsewhere")
            return
        isWinner = False
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")
        if result == []:
            await ctx.respond("You are not entered into the system, please send a message then try again.")
            return

        balance = result[0]['coins']
        if balance < 100:
            await ctx.respond(f"You don't have the {currency_name} to play this")
            return
        result1 = await db.fetch(f"SELECT coinswon, coinslost FROM gamblingstats WHERE guild_id = '{ctx.author.guild.id}' AND user_id = '{ctx.author.id}'")
        if result1 == []:
            sql = f"INSERT INTO gamblingstats(guild_id, user_id, bj_wins, bj_losses, ban_win_streak, best_coinflip, coinswon, coinslost) VALUES($1, $2, $3, $4, $5, $6, $7, $8)"
            await db.execute(sql, str(ctx.guild.id), str(ctx.author.id), 0, 0, 0, 0, 0, 0)
            result1 = await db.fetch(f"SELECT coinswon, coinslost FROM gamblingstats WHERE guild_id = '{ctx.author.guild.id}' AND user_id = '{ctx.author.id}'")


        randCoins = random.randrange(2450, 2550)
        randNum = random.randrange(1, 21)
        if guess == randNum:
            await ctx.respond(f"you guessed the number correctly, congratulations!  You've won {randCoins} {currency_name}")
            isWinner = True
        else:
            await ctx.respond(f"Your guess was incorrect, the winning number was `{randNum}`")

        if isWinner:
            new_balance = balance + randCoins
            coinswon_new = result1[0]['coinswon'] + randCoins
            sql = "UPDATE gamblestats SET coinswon = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql, coinswon_new, str(ctx.author.guild.id), str(ctx.author.id))

        else:
            new_balance = balance - 100
            coinslost_new = result1[0]['coinslost'] + 100
            sql = "UPDATE gamblestats SET coinslost = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql, coinslost_new, str(ctx.author.guild.id), str(ctx.author.id))
        sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
        await db.execute(sql, new_balance, str(ctx.author.guild.id), str(ctx.author.id))

    @d20.error
    async def d20_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(f'Please wait {error.retry_after:.2f} seconds and then try again')


    @slash_command(name = "coinflip", description = f"Correctly call consecutive coin flips to win {currency_name}!")
    @commands.cooldown(1, 10800, commands.BucketType.user)
    async def coinflip(self, ctx):

        if ctx.channel.id in banchannels:
            await ctx.send("This game is restricted in this channel, please try again elsewhere")
            return
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")
        if result == []:
            await ctx.respond("You are not entered into the system, please send a message then try again.")
            return
        result1 = await db.fetch(f"SELECT best_coinflip, coinswon FROM gamblingstats WHERE guild_id = '{ctx.author.guild.id}' AND user_id = '{ctx.author.id}'")
        if result1 == []:
            sql = f"INSERT INTO gamblingstats(guild_id, user_id, bj_wins, bj_losses, ban_win_streak, best_coinflip, coinswon, coinslost) VALUES($1, $2, $3, $4, $5, $6, $7, $8)"
            await db.execute(sql, str(ctx.guild.id), str(ctx.author.id), 0, 0, 0, 0, 0, 0)
            result1 = await db.fetch(f"SELECT best_coinflip, coinswon FROM gamblingstats WHERE guild_id = '{ctx.author.guild.id}' AND user_id = '{ctx.author.id}'")
        winCounter = 0
        call = 0
        hasLost = False
        firstmessage = True
        while not hasLost:
            def check(msg):
                return (msg.author == ctx.author) and msg.channel == ctx.channel and \
                (msg.content.lower() == 'heads' or msg.content.lower() == 'tails') or (msg.content.lower() == 'exit')
            if firstmessage == True:
                await ctx.respond("Please call heads or tails")
                firstmessage = False
            else:
                await ctx.send("Please call heads or tails")
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond and forfeited the game")
                hasLost = True
            if msg.content == 'exit':
                await ctx.send("You have successfully exited the game")
                hasLost = True
            flip = random.randrange(1,3)
            #bugtesting value don't uncomment
            #flip = 1
            if msg.content.lower() == 'heads':
                call = 1
            elif msg.content.lower() == 'tails':
                call = 2
            else:
                continue
            if flip == call:
                winCounter = winCounter + 1
                await asyncio.sleep(1)
                await ctx.send(f"Great guess, you have called {winCounter} flips correctly so far!")
            else:
                await asyncio.sleep(1)
                if flip == 1:
                    flipString = 'heads'
                else:
                    flipString = 'tails'
                await ctx.send(f"That guess was incorrect, {flipString} was the correct call")
                hasLost = True
            await asyncio.sleep(2)

        if winCounter == 0:
            await ctx.send("Unlucky guess, you've lost the game!")
        else:
            winnings = 50*(winCounter)+2**winCounter

            balance = result[0]['coins']
            new_balance = balance + winnings
            coinswon_new = result1[0]['coinswon'] + winnings
            sql = "UPDATE gamblingstats SET coinswon = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql, coinswon_new, str(ctx.author.guild.id), str(ctx.author.id))
        
            sql1 = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql1, new_balance, str(ctx.author.guild.id), str(ctx.author.id))

            await ctx.send(f"Congratulations, you have won `{winnings}` {currency_name} and now have `{new_balance}` {currency_name} total!")
        if winCounter > result1[0]['best_coinflip']:
            await ctx.send(f"You've set a new personal coinflip record of {winCounter}!")
            sql = "UPDATE gamblingstats SET best_coinflip = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql, winCounter, str(ctx.author.guild.id), str(ctx.author.id))

    @coinflip.error
    async def coinflip_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            timer = error.retry_after / 3600
            await ctx.respond(f"Please wait {timer:.2f} hours to play again")


    @slash_command(name = "russianroulette", description = "Don't lose", guild_ids = guildIDs)
    # @commands.cooldown(1, 60, commands.BucketType.guild)
    async def russianroulette(self, ctx: commands.Context, guess: Option(int, "any number from 1-6", required = True, min_value = 1, max_value = 6)):
        
        if ctx.channel.id in banchannels:
            await ctx.send("This game is restricted in this channel, please try again elsewhere")
            return
        guild = ctx.guild
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        result = await db.fetch(f"SELECT ban_win_streak FROM gamblingstats WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")
        if result == []:
            sql = f"INSERT INTO gamblingstats(guild_id, user_id, bj_wins, bj_losses, ban_win_streak, best_coinflip, coinswon, coinslost) VALUES($1, $2, $3, $4, $5, $6, $7, $8)"
            await db.execute(sql, str(ctx.guild.id), str(ctx.author.id), 0, 0, 0, 0, 0, 0)
            result = await db.fetch(f"SELECT ban_win_streak FROM gamblingstats WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")

        randNum = random.randrange(1, 7)
        # testing value, only uncomment for bugfixing
        # randNum = 1
        await ctx.respond("Spinning the chamber, cross your fingers")
        await asyncio.sleep(2)

        if guess == randNum:
            await ctx.send("Uh oh, you guessed the wrong number!  Kicking in 5...")
            await asyncio.sleep(1)
            await ctx.send("4...")
            await asyncio.sleep(1)
            await ctx.send("3...")
            await asyncio.sleep(1)
            await ctx.send("2...")
            await asyncio.sleep(1)
            await ctx.send("1...")
            await asyncio.sleep(1)
            await ctx.send(f"{ctx.author} got shot and is now dead.")
            reason = "losing at russian roulette"
            message = str(f"Hey idiot, you got kicked from a server for {reason}!  If you want to rejoin, dm the owners and grovel at their feet, they may take pity on you!")
            await ctx.author.send(message)
            member = ctx.author
            await ctx.author.kick(reason = reason)
            sql = f"UPDATE gamblingstats SET ban_win_streak = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql, 0, str(ctx.author.guild.id), str(ctx.author.id))
        else:
            streak = result[0]['ban_win_streak'] + 1
            await ctx.send(f"Phew, you have survived and your win streak advanced to {streak}!")
            
            sql = f"UPDATE gamblingstats SET ban_win_streak = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql, streak, str(ctx.author.guild.id), str(ctx.author.id))
            roles1 = [discord.utils.get(guild.roles, name="Roulette Survivor"), discord.utils.get(guild.roles, name="Roulette Amateur"), discord.utils.get(guild.roles, name="Roulette Pro"), discord.utils.get(guild.roles, name="Roulette Expert"), discord.utils.get(guild.roles, name="Roulette Master")]
            roles3 = [discord.utils.get(guild.roles, name="Roulette Amateur"), discord.utils.get(guild.roles, name="Roulette Pro"), discord.utils.get(guild.roles, name="Roulette Expert"), discord.utils.get(guild.roles, name="Roulette Master")]
            roles6 = [discord.utils.get(guild.roles, name="Roulette Pro"), discord.utils.get(guild.roles, name="Roulette Expert"), discord.utils.get(guild.roles, name="Roulette Master")]
            roles10 = [discord.utils.get(guild.roles, name="Roulette Expert"), discord.utils.get(guild.roles, name="Roulette Master")]
            if streak == 1:
                guild = ctx.guild
                member = ctx.author
                for role in roles1:
                    if role in member.roles:
                        return
                role = discord.utils.get(guild.roles, name="Roulette Survivor")
                if role is None:
                    rolecolor = int("0xb08d57", 16)
                    await guild.create_role(name="Roulette Survivor", colour=rolecolor)
                    role = discord.utils.get(guild.roles, name="Roulette Survivor")
                
                if role not in member.roles:
                    await member.add_roles(role)
            elif streak == 3:
                guild = ctx.guild
                member = ctx.author
                for role in roles3:
                    if role in member.roles:
                        return
                oldrole = discord.utils.get(guild.roles, name="Roulette Survivor")
                if oldrole in member.roles:
                    await member.remove_roles(oldrole)
                role = discord.utils.get(guild.roles, name="Roulette Amateur")
                if role is None:
                    rolecolor = int("0xaaa9ad", 16)
                    await guild.create_role(name="Roulette Amateur", colour=rolecolor)
                    role = discord.utils.get(guild.roles, name="Roulette Amateur")
                member = ctx.author
                if role not in member.roles:
                    await member.add_roles(role)
            elif streak == 6:
                guild = ctx.guild
                member = ctx.author
                for role in roles6:
                    if role in member.roles:
                        return
                oldrole = discord.utils.get(guild.roles, name="Roulette Amateur")
                if oldrole in member.roles:
                    await member.remove_roles(oldrole)
                role = discord.utils.get(guild.roles, name="Roulette Pro")
                if role is None:
                    rolecolor = int("0xd4af37", 16)
                    await guild.create_role(name="Roulette Pro", colour=rolecolor)
                    role = discord.utils.get(guild.roles, name="Roulette Pro")
                member = ctx.author
                if role not in member.roles:
                    await member.add_roles(role)
            elif streak == 10:
                guild = ctx.guild
                member = ctx.author
                for role in roles10:
                    if role in member.roles:
                        return
                oldrole = discord.utils.get(guild.roles, name="Roulette Pro")
                if oldrole in member.roles:
                    await member.remove_roles(oldrole)
                role = discord.utils.get(guild.roles, name="Roulette Expert")
                if role is None:
                    rolecolor = int("0x267166", 16)
                    await guild.create_role(name="Roulette Expert", colour=rolecolor)
                    role = discord.utils.get(guild.roles, name="Roulette Expert")
                member = ctx.author
                if role not in member.roles:
                    await member.add_roles(role)
            elif streak == 15:
                guild = ctx.guild
                member = ctx.author
                if discord.utils.get(guild.roles, name="Roulette Master") in member.roles:
                    return
                oldrole = discord.utils.get(guild.roles, name="Roulette Expert")
                if oldrole in member.roles:
                    await member.remove_roles(oldrole)
                role = discord.utils.get(guild.roles, name="Roulette Master")
                if role is None:
                    rolecolor = int("0x313c7e", 16)
                    await guild.create_role(name="Roulette Master", colour=rolecolor)
                    role = discord.utils.get(guild.roles, name="Roulette Master")
                member = ctx.author
                if role not in member.roles:
                    await member.add_roles(role)

    # @russianroulette.error
    # async def russianroulette_error(self,ctx,error):
    #     if isinstance(error, commands.CommandOnCooldown):
    #         await ctx.respond(f'Please wait {error.retry_after:.2f} seconds and then try again')


    @slash_command(name = "bossroulette", description = "Don't lose")
    async def bossroulette(self, ctx: commands.Context, guess: Option(int, "any number from 1-6", required = True, min_value = 1, max_value = 6), member: Option(discord.Member, "Discord Member", required = True)):
        if ctx.channel.id in banchannels:
            await ctx.send("This game is restricted in this channel, please try again elsewhere")
            return
        guild = ctx.guild
        if ctx.author.id != 784001588816773142:
            await ctx.respond("Nice try kid")
            return
        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        result = await db.fetch(f"SELECT ban_win_streak FROM gamblingstats WHERE guild_id = '{ctx.guild.id}' AND user_id = '{member.id}'")
        if result == []:
            sql = f"INSERT INTO gamblingstats(guild_id, user_id, bj_wins, bj_losses, ban_win_streak, best_coinflip, coinswon, coinslost) VALUES($1, $2, $3, $4, $5, $6, $7, $8)"
            await db.execute(sql, str(ctx.guild.id), str(ctx.author.id), 0, 0, 0, 0, 0, 0)

        randNum = random.randrange(1, 7)
        # testing value, only uncomment for bugfixing
        # randNum = 1
        await ctx.respond(f"You've been forced to play roulette {member.mention}, good luck!  The chamber is spinning")
        await asyncio.sleep(2)

        if guess == randNum:
            await ctx.send("Uh oh, you guessed the wrong number!  Kicking in 5...")
            await asyncio.sleep(1)
            await ctx.send("4...")
            await asyncio.sleep(1)
            await ctx.send("3...")
            await asyncio.sleep(1)
            await ctx.send("2...")
            await asyncio.sleep(1)
            await ctx.send("1...")
            await asyncio.sleep(1)
            await ctx.send(f"{member} got shot and is now dead.")
            reason = "losing at russian roulette"
            message = str(f"Hey idiot, you got kicked from a server for {reason}!  If you want to rejoin, dm the owners and grovel at their feet, they may take pity on you!")
            await member.send(message)
            await member.kick(reason = reason)
            sql = f"UPDATE gamblingstats SET ban_win_streak = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql, 0, str(ctx.author.guild.id), str(member.id))
        else:
            result1 = await db.fetch(f"SELECT ban_win_streak FROM gamblingstats WHERE guild_id = '{ctx.guild.id}' AND user_id = '{member.id}'")
            streak = result1[0]['ban_win_streak'] + 1
            await ctx.send(f"Phew, you have survived and your win streak advanced to {streak}!")
            
            sql = f"UPDATE gamblingstats SET ban_win_streak = $1 WHERE guild_id = $2 AND user_id = $3"
            await db.execute(sql, streak, str(ctx.author.guild.id), str(member.id))
            roles1 = [discord.utils.get(guild.roles, name="Roulette Survivor"), discord.utils.get(guild.roles, name="Roulette Amateur"), discord.utils.get(guild.roles, name="Roulette Pro"), discord.utils.get(guild.roles, name="Roulette Expert"), discord.utils.get(guild.roles, name="Roulette Master")]
            roles3 = [discord.utils.get(guild.roles, name="Roulette Amateur"), discord.utils.get(guild.roles, name="Roulette Pro"), discord.utils.get(guild.roles, name="Roulette Expert"), discord.utils.get(guild.roles, name="Roulette Master")]
            roles6 = [discord.utils.get(guild.roles, name="Roulette Pro"), discord.utils.get(guild.roles, name="Roulette Expert"), discord.utils.get(guild.roles, name="Roulette Master")]
            roles10 = [discord.utils.get(guild.roles, name="Roulette Expert"), discord.utils.get(guild.roles, name="Roulette Master")]
            if streak == 1:
                guild = ctx.guild
                for role in roles1:
                    if role in member.roles:
                        return
                role = discord.utils.get(guild.roles, name="Roulette Survivor")
                if role is None:
                    rolecolor = int("0xb08d57", 16)
                    await guild.create_role(name="Roulette Survivor", colour=rolecolor)
                    role = discord.utils.get(guild.roles, name="Roulette Survivor")
                
                if role not in member.roles:
                    await member.add_roles(role)
            elif streak == 3:
                guild = ctx.guild
                member = ctx.author
                for role in roles3:
                    if role in member.roles:
                        return
                oldrole = discord.utils.get(guild.roles, name="Roulette Survivor")
                if oldrole in member.roles:
                    await member.remove_roles(oldrole)
                role = discord.utils.get(guild.roles, name="Roulette Amateur")
                if role is None:
                    rolecolor = int("0xaaa9ad", 16)
                    await guild.create_role(name="Roulette Amateur", colour=rolecolor)
                    role = discord.utils.get(guild.roles, name="Roulette Amateur")
                member = ctx.author
                if role not in member.roles:
                    await member.add_roles(role)
            elif streak == 6:
                guild = ctx.guild
                member = ctx.author
                for role in roles6:
                    if role in member.roles:
                        return
                oldrole = discord.utils.get(guild.roles, name="Roulette Amateur")
                if oldrole in member.roles:
                    await member.remove_roles(oldrole)
                role = discord.utils.get(guild.roles, name="Roulette Pro")
                if role is None:
                    rolecolor = int("0xd4af37", 16)
                    await guild.create_role(name="Roulette Pro", colour=rolecolor)
                    role = discord.utils.get(guild.roles, name="Roulette Pro")
                member = ctx.author
                if role not in member.roles:
                    await member.add_roles(role)
            elif streak == 10:
                guild = ctx.guild
                member = ctx.author
                for role in roles10:
                    if role in member.roles:
                        return
                oldrole = discord.utils.get(guild.roles, name="Roulette Pro")
                if oldrole in member.roles:
                    await member.remove_roles(oldrole)
                role = discord.utils.get(guild.roles, name="Roulette Expert")
                if role is None:
                    rolecolor = int("0x267166", 16)
                    await guild.create_role(name="Roulette Expert", colour=rolecolor)
                    role = discord.utils.get(guild.roles, name="Roulette Expert")
                member = ctx.author
                if role not in member.roles:
                    await member.add_roles(role)
            elif streak == 15:
                guild = ctx.guild
                member = ctx.author
                if discord.utils.get(guild.roles, name="Roulette Master") in member.roles:
                    return
                oldrole = discord.utils.get(guild.roles, name="Roulette Expert")
                if oldrole in member.roles:
                    await member.remove_roles(oldrole)
                role = discord.utils.get(guild.roles, name="Roulette Master")
                if role is None:
                    rolecolor = int("0x313c7e", 16)
                    await guild.create_role(name="Roulette Master", colour=rolecolor)
                    role = discord.utils.get(guild.roles, name="Roulette Master")
                member = ctx.author
                if role not in member.roles:
                    await member.add_roles(role)


def setup(bot: commands.Bot):
    bot.add_cog(Casino(bot))