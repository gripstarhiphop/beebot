import asyncpg, time, random, discord, asyncio
from discord.ext import commands
from sys import platform
from discord.commands import slash_command, Option, permissions


guildIDs = [929594969000390696, 580587544287379456, 340253890643755009, 765005927619231774, 691147057796218905, 389113239159439361, 621423558886817820, 943741853239492688]
banchannels = [1040859151833772083, 1040859197417459763, 1040859197417459763]

class Wordle(commands.Cog):
    """
    Gaming
    """
    def __init__(self, bot):
        self.bot = bot
        if platform.startswith("lin"):
            self.path = "/root/serverkitten/media/"
        else:
            self.path = "./media/"


    @slash_command(name = "wordle", description = "play Wordle, the popular word guessing game!")
    @commands.cooldown(1, 60*60*24, commands.BucketType.user)
    async def wordle(self, ctx: commands.Context):
        if ctx.channel.id in banchannels:
            await ctx.send("This game is restricted in this channel, please try again elsewhere")
            return

        db = await asyncpg.connect(user = 'postgres', password = 'gaming123', database = 'postgres', host = 'localhost')
        result = await db.fetch(f"SELECT coins FROM beelevel WHERE guild_id = '{ctx.guild.id}' AND user_id = '{ctx.author.id}'")
        bal = result[0]['coins']
        result1 = await db.fetch(f"SELECT wins, losses, turns_used, streak FROM wordle WHERE guild_id = '{ctx.author.guild.id}' AND user_id = '{ctx.author.id}'")
        if result1 == []:
            sql = f"INSERT INTO wordle(guild_id, user_id, wins, losses, turns_used, streak) VALUES($1, $2, $3, $4, $5, $6)"
            await db.execute(sql, str(ctx.guild.id), str(ctx.author.id), 0, 0, 0, 0)
            result1 = await db.fetch(f"SELECT wins, losses, turns_used, streak FROM wordle WHERE guild_id = '{ctx.author.guild.id}' AND user_id = '{ctx.author.id}'")
        userwins = result1[0]['wins']
        userlosses = result1[0]['losses']
        userturns = result1[0]['turns_used']
        userstreak = result1[0]['streak']

        
        dictionary = [
        'aback', 'abbey', 'abbot', 'abide', 'abode', 'abort', 'about', 'above', 'abuse', 'abuzz', 'abyss','ached', 'aches', 'acids', 'acorn', 'acres', 'acted', 'actor', 'acute',
        'adage', 'adapt', 'added', 'adder', 'addle', 'adept', 'adieu', 'adios', 'admin', 'admit', 'adobe', 'adopt', 'adore', 'adorn', 'adult', 'aegis', 'aeons', 'aerie', 'affix',
        'afire', 'afoot', 'afoul', 'after', 'again', 'agape', 'agast', 'agave', 'agent', 'aggie', 'agile', 'aging', 'agism', 'aglet', 'aglow', 'agony', 'agora', 'agree', 'agrin', 
        'ahead', 'ahold', 'aided', 'aides', 'adios', 'ailed', 'aimed', 'aimer', 'aired', 'airer', 'aisle', 'alamo', 'alarm', 'alias', 'alibi', 'alien', 'align', 'alike', 'alive',
        'alley', 'allot', 'allow', 'alloy', 'aloft', 'aloha', 'alone', 'along', 'aloof', 'aloud', 'alpha', 'altar', 'alter', 'amass', 'amaze', 'amber', 'amble', 'amend', 'amiga',
        'amigo', 'among', 'amour', 'amped', 'ample', 'amuck', 'amuse', 'angel', 'anger', 'angle', 'anglo', 'angry', 'angst', 'anime', 'ankle', 'annex', 'annoy', 'anole', 'antic', 
        'antsy', 'anvil', 'aorta', 'apart', 'aphid', 'apnea', 'appal', 'apple', 'apply', 'apron', 'aptly', 'arbor', 'arced', 'ardor', 'arena', 'arise', 'argon', 'armed', 'armer', 'armor', 
        'aroma', 'arose', 'array', 'arrow', 'arson', 'artsy', 'ascot', 'ashen', 'ashes', 'aside', 'asked', 'akser', 'askew', 'aspen', 'asset', 'atlas', 'atolls', 'atoms', 'atone', 
        'attic', 'audio', 'audit', 'auger', 'aunts', 'aunty', 'aural', 'avail', 'avast', 'avert', 'avoid', 'avows', 'await', 'awake', 'award', 'aware', 'awash', 'aways', 'awful', 
        'awned', 'awner', 'awoke', 'axels', 'axial', 'axiom', 'axles', 'aztec', 'azure', 'babel', 'babes', 'backs', 'bacon', 'baddy', 'badge', 'badly', 'bagel', 'baggy', 'bails', 
        'baits', 'baked', 'baker', 'bakes', 'balds', 'baldy', 'baled', 'baler', 'bales', 'balks', 'balls', 'bally', 'balms', 'balmy', 'balsa', 'bambi', 'banal', 'bands', 'bangs', 
        'banjo', 'banks', 'barbs', 'barby', 'bards', 'bared', 'barer', 'bares', 'barfs', 'barge', 'barks', 'barky', 'barns', 'baron', 'basal', 'based', 'bases', 'basic', 'basin',
        'basis', 'basks', 'bassy', 'batch', 'bathe', 'baths', 'baton', 'batty', 'bawls', 'bayed', 'bayou', 'bazar', 'beach', 'beads', 'beady', 'beaks', 'beaky', 'beams', 'beans',
        'beard', 'bears', 'beast', 'beats', 'beaut', 'bebop', 'beech', 'beefs', 'beefy', 'beeps', 'beers', 'beets', 'befit', 'began', 'begat', 'begin', 'begot', 'begun', 'beige',
        'being', 'belay', 'belch', 'belle', 'bells', 'belly', 'below', 'belts', 'bench', 'bends', 'bendy', 'bento', 'beret', 'berr', 'berth', 'beryl', 'beset', 'bests', 'bible',
        'bicep', 'bides', 'bidet', 'bigot', 'bijou', 'biked', 'biker', 'bikes', 'bilge', 'bimbo', 'binds', 'bingo', 'biome', 'biped', 'birch', 'birds', 'birrs', 'birth', 'bison',
        'bitch', 'biter', 'bites', 'bitsy', 'bitty', 'blabs', 'black', 'blade', 'blame', 'bland', 'blank', 'blare', 'blast', 'blaze', 'bleak', 'bleed', 'bleep', 'blend', 'bless',
        'blimp', 'blind', 'bling', 'blink', 'blips', 'bliss', 'blitz', 'bloat', 'blobs', 'block', 'blogs', 'bloke', 'blond', 'blood', 'bloom', 'blots', 'blown', 'blows', 'bluer', 
        'blues', 'bluff', 'blunt', 'blurb', 'blurs', 'blurt', 'blush', 'board', 'boars', 'boast', 'boats', 'boded', 'bodes', 'bogey', 'boggy', 'bogus', 'boils', 'boing', 'bolas', 
        'bolds', 'bolts', 'bolus', 'bombs', 'bonds', 'boned', 'boner', 'bones', 'bongo', 'bongs', 'bonks', 'bonus', 'boobs', 'booby', 'booed', 'books', 'booms', 'boons', 'boors', 
        'boost', 'booth', 'boots', 'booty', 'booze', 'bored', 'borer', 'bores', 'bosom', 'bossy', 'botch', 'bough', 'bound', 'bouts', 'bowed', 'bowel', 'bower', 'bowls', 'boxed',
        'boxer', 'boxes', 'bozos', 'brace', 'brags', 'braid', 'brail', 'brain', 'brake', 'brand', 'brash', 'brass', 'brats', 'brave', 'bravo', 'brawl', 'brawn', 'brays', 'braze',
        'bread', 'break', 'breed', 'brews', 'briar', 'bribe', 'brick', 'bride', 'brief', 'brigs', 'brims', 'brine', 'bring', 'brink', 'briny', 'brisk', 'broil', 'broke', 'brood',
        'brook', 'broom', 'broth', 'brown', 'brows', 'bruin', 'brunt', 'brush', 'brute', 'bucks', 'buddy', 'budge', 'buffs', 'buggy', 'bugle', 'build', 'built', 'bulbs', 'bulge',
        'bulks', 'bulky', 'bulls', 'bully', 'bumps', 'bumpy', 'bunch', 'bunks', 'bunny', 'bunts', 'burly', 'burns', 'burnt', 'burps', 'burro', 'burrs', 'burry', 'burst', 'bused',
        'buses', 'bushy', 'busts', 'busty', 'butch', 'butte', 'butts', 'buyer', 'buzzy', 'bylaw', 'bytes', 'cabin', 'cable', 'cacao', 'cache', 'cacti', 'caddy', 'cadet', 'cadre',
        'cafes', 'caged', 'cager', 'cages', 'cagey', 'cajun', 'caked', 'cakes', 'cakey', 'calfs', 'calks', 'calls', 'calms', 'camel', 'cameo', 'camps', 'canal', 'canes', 'canny', 
        'canoe', 'canon', 'caped', 'caper', 'capes', 'caput', 'carbs', 'cards', 'cared', 'carer', 'cares', 'caret', 'cargo', 'carny', 'carol', 'carps', 'carry', 'carts', 'carve', 
        'casas', 'cased', 'cases', 'casks', 'caste', 'casts', 'catch', 'cater', 'catty', 'cauld', 'caulks', 'cause', 'cease', 'cedar', 'ceded', 'ceder', 'cedes', 'celeb', 'cello',
        'cells', 'celts', 'cents','certs', 'chaco', 'chads', 'chafe', 'chaff', 'chaft', 'chain', 'chair', 'chalk', 'champ', 'chant', 'chaos', 'chaps', 'chard', 'charm', 'chars', 'chart',
        'chase', 'chasm', 'chats', 'chaws', 'cheap', 'cheat', 'check', 'cheek', 'cheep', 'cheer', 'chefs', 'chemo', 'chess', 'chest', 'chevy', 'chews', 'chewy', 'chica', 'chick', 'chico',
        'chide', 'chief', 'child', 'chile', 'chili', 'chill', 'chime', 'chimp', 'china', 'chink', 'chino', 'chins', 'chips', 'chirk', 'chirp', 'chirt', 'chits', 'chive', 'chock', 'choco',
        'choir', 'choke', 'cholo', 'chomp', 'chops', 'chord', 'chore', 'chose', 'chows', 'chubs', 'chuck', 'chugs', 'chump', 'chums', 'chunk', 'churn', 'chute', 'cider', 'cigar', 'cinch',
        'circa', 'cists', 'cited', 'citer', 'cites', 'civic', 'civil', 'clack', 'clads', 'claim', 'clamp', 'clams', 'clang', 'clank', 'clans', 'claps', 'clash', 'clasp', 'class', 'claws', 
        'clays', 'clean', 'clear', 'cleat', 'cleft', 'click', 'cliff', 'climb', 'cling', 'clink', 'clips', 'cloak', 'clock', 'clods', 'clogs', 'clomp', 'clone', 'close', 'cloth', 'clots',
        'cloud',  'clout', 'clove', 'clown', 'clubs', 'clubs', 'cluck', 'clued', 'clues', 'clump', 'clung', 'clunk', 'coach', 'coals', 'coast', 'coats', 'cobra', 'cocks', 'cocky', 'cocoa',
        'coded', 'coder', 'codes', 'codex', 'coeds', 'coifs', 'coils', 'coins', 'coked', 'cokes', 'colas', 'colds', 'colon', 'color', 'colts', 'combo', 'combs', 'comet', 'comfy', 'comic',
        'comma', 'comps', 'conch', 'condo', 'coned', 'cones', 'conga', 'congo', 'conky', 'convo', 'cooch', 'cooed', 'cooey', 'cooks', 'cooky', 'coons', 'coops', 'coped', 'coper', 'copes',
        'coral', 'cords', 'cored', 'corer', 'cores', 'corgi', 'corks', 'corky', 'corns', 'corny', 'corps', 'costs', 'couch', 'cough', 'could', 'count', 'coupe', 'court', 'court', 'couth', 
        'coven', 'cover', 'covet', 'cowed', 'cower', 'cowry', 'coyly', 'crabs', 'crack', 'craft', 'cramp', 'crams', 'crane', 'crank', 'crape', 'craps', 'crash', 'crass', 'crate', 'crave',
        'crawl', 'craze', 'crazy', 'cream', 'credo', 'creed', 'creek', 'creep', 'creme', 'crepe', 'crept', 'cress', 'crest', 'crews', 'cribs', 'crick', 'cried', 'crier', 'cries', 'crime',
        'crimp', 'cripe', 'crisp', 'crits', 'croak', 'crocs', 'crops', 'cross', 'crowd', 'crown', 'crows', 'crude', 'cruel', 'crumb', 'crush', 'crust', 'crypt', 'cubby', 'cubed', 'cuber',
        'cubes', 'cubic', 'cubit', 'cuffs', 'culls', 'cully', 'cults', 'culty', 'cumin', 'cupid', 'cuppy', 'curbs', 'curds', 'curdy',  'cured', 'curer', 'cures', 'curio', 'curls', 'curly',
        'curry', 'curse', 'curve', 'curvy', 'cushy', 'cusps', 'cuter', 'cutes', 'cutey', 'cutie', 'cutty', 'cutup', 'cyber', 'cycle', 'cynic', 'cysts', 'czars', 'daces', 'daddy', 'daffy',
        'daily', 'daint', 'dairy', 'daisy', 'dally', 'dames', 'damps', 'dance', 'dandy', 'danks', 'dared', 'darer', 'dares', 'darks', 'darky', 'darns', 'darts', 'dated', 'dater', 'dates',
        'datum', 'daunt', 'dawns', 'dazed', 'dazer', 'dazes', 'deads', 'deals', 'dealt', 'deans', 'dears', ' deary', 'death', 'debag', 'debit', 'debts', 'debug', 'debut', 'decaf', 'decal',
        'decay', 'decks', 'decor', 'decoy', 'decry', 'deeds', 'deems', 'deeps', 'deers', 'defer', 'defog', 'deice', 'deify', 'deign', 'deism', 'deity', 'delay', 'delta', 'delts', 'delve', 
        'demon', 'demos', 'demur', 'denim', 'dense', 'dents', 'depot', 'depth', 'derby', 'derma', 'derth', 'desks', 'deter', 'detox', 'deuce', 'devil', 'dewax', 'dewed', 'dials', 'diary', 
        'dibbs', 'diced', 'dicer', 'dices', 'dicey', 'dicks', 'dicot', 'dikes', 'dimes', 'dimly', 'dined', 'diner', 'dines', 'dinge', 'dingo', 'dings', 'dingy', 'dinks', 'dinky', 'diode',
        'dippy', 'dirge', 'dirks', 'dirts', 'dirty', 'disco', 'discs', 'disks', 'ditch', 'ditto', 'ditzy', 'dived', 'diver', 'dives', 'divot', 'dixie', 'dizzy', 'docks', 'dodge', 'dodgy', 
        'dodos', 'doers', 'doeth', 'doggo', 'doggy', 'dogma', 'doily', 'doing', 'dojos', 'dolls', 'dolly', 'dolts', 'domed', 'domes', 'donor', 'donut', 'dooms', 'doomy', 'doors', 'doozy', 
        'doped', 'doper', 'dopes', 'dopey', 'dorks', 'dorky', 'dorms', 'dosed', 'doses', 'doted', 'doter', 'dotty', 'doubt', 'dough', 'douse', 'dowdy', 'dowed', 'dowel', 'downs', 'downy',
        'dowry', 'dozed', 'dozen', 'dozer', 'dozes', 'drabs', 'draco', 'draft', 'drags', 'drain', 'drake', 'drama', 'drank', 'drape', 'drawl', 'drawn', 'draws', 'dread', 'dream', 'dregs',
        'dress', 'dried', 'drier', 'dries', 'drift', 'drill', 'drink', 'drips', 'drive', 'droid', 'droll', 'drone', 'drool', 'drops', 'drove', 'drown', 'drubs', 'drugs', 'druid', 'drums', 
        'drunk', 'dryad', 'dryer', 'dryly', 'duals', 'ducks', 'ducky', 'ducts', 'dudes', 'duels', 'duets', 'dukes', 'dumbo', 'dumbs', 'dummy', 'dumps', 'dumpy', 'dunce', 'dunes', 'dunks',
        'duped', 'duper', 'dupes', 'dusks', 'dusky', 'dusty', 'dusty', 'dutch', 'duvet', 'dwarf', 'dweeb', 'dwell', 'dwelt', 'dying', 'dykes', 'eager', 'eagle', 'eared', 'earls', 'earns',
        'earth', 'eased', 'easel', 'easer', 'eases', 'easts', 'eaten', 'eater', 'ebbed', 'ebony', 'ecads', 'echos', 'edged', 'edger', 'edges', 'edict', 'edify', 'edits', 'eerie', 'egads',
        'egged', 'egger', 'egret', 'eight', 'eject', 'elate', 'elbow', 'elder', 'elect', 'elfin', 'elite', 'elope', 'elude', 'elves', 'email', 'embed', 'ember', 'emcee', 'emits', 'emote', 
        'empty', 'enact', 'ended', 'ender', 'enema', 'enemy', 'enjoy', 'ensue', 'enter', 'entry', 'envoy', 'epics', 'epoch', 'epoxy', 'equal', 'equip', 'erase', 'erect', 'erode', 'erred',
        'error', 'erupt', 'essay', 'ether', 'ethic', 'ethos', 'ethyl', 'euros', 'evade', 'evens', 'event', 'evict', 'evils', 'evoke', 'exact', 'exalt', 'exams', 'excel', 'execs', 'exert',
        'exile', 'exist', 'exits', 'expel', 'expos', 'exude', 'exult', 'fable', 'faced', 'facer', 'faces', 'facet', 'facts', 'faded', 'fader', 'fades', 'fails', 'fains', 'faint', 'fairy',
        'faith', 'faked', 'faker', 'fakes', 'falls', 'false', 'famed', 'fames', 'fancy', 'fangs', 'fanny', 'farce', 'fared', 'farer', 'farms', 'farts', 'fasts', 'fatal', 'fated', 'fates', 
        'fatly', 'fatso', 'fatty', 'fault', 'fauna', 'favor', 'fawns', 'faxed', 'faxes', 'fazed', 'fazes', 'fears', 'feast', 'feats', 'fecal', 'feces', 'fedex', 'feeds', 'feels', 'feign',
        'feint', 'fella', 'fells', 'felon', 'felts', 'felty', 'femme', 'femur', 'fence', 'fends', 'feral', 'ferns', 'ferry', 'fetch', 'fetus', 'feuds', 'fever', 'fewer', 'fiats', 'fiber',
        'fibre', 'fiefs', 'field', 'fiend', 'fiery', 'fifer', 'fifes', 'fifth', 'fifty', 'fight', 'filch', 'filed', 'filer', 'files', 'filet', 'fills', 'filly', 'films', 'filmy', 'filth',
        'finch', 'finds', 'fined', 'finer', 'fines', 'fired', 'firer', 'fires', 'firms', 'first', 'firth', 'fishy', 'fists', 'fiver', 'fives', 'fixed', 'fixer', 'fixes', 'fizzy', 'fjord',
        'flabs', 'flack', 'flags', 'flail', 'flair', 'flake', 'flaky', 'flame', 'flank', 'flans', 'flaps', 'flare', 'flash', 'flask', 'flats', 'flaws', 'flays', 'fleas', 'fleck', 'flees',
        'fleet', 'flesh', 'flick', 'flies', 'fling', 'flint', 'flips', 'flirt', 'flits', 'float', 'flock', 'flogs', 'flood', 'floor', 'flops', 'floss', 'flour', 'flown', 'flows', 'flubs',
        'flues', 'fluff', 'fluid', 'fluke', 'flume', 'flung', 'flunk', 'flush', 'flute', 'flyer', 'foals', 'foams', 'foamy', 'focal', 'focus', 'fogey', 'foggy', 'foils', 'foist', 'folds', 
        'folks', 'folky', 'folly', 'fonts', 'foods', 'foody', 'fools', 'foots', 'footy', 'foray', 'force', 'fords', 'forge', 'forks', 'forky', 'forms', 'forte', 'forth', 'forts', 'forty',
        'forum', 'fouls', 'found', 'fount', 'fours', 'fowls', 'foxes', 'foyer', 'frack', 'frags', 'frail', 'frame', 'frank', 'frats', 'fraud', 'frays', 'freak', 'freed', 'freer', 'frees',
        'freon', 'fresh', 'frets', 'friar', 'fried', 'frier', 'fries', 'frill', 'frisk', 'fritz', 'frizz', 'frogs', 'frond', 'front', 'frost', 'froth', 'frown', 'froze', 'fruit', 'fryer', 
        'fudge', 'fuels', 'fulls', 'fully', 'fumed', 'fumes', 'funds', 'fungi', 'funks', 'funky', 'funny', 'furls', 'furor', 'furry', 'fused', 'fuses', 'fussy', 'futon', 'fuzed', 'fuzes', 
        'fuzzy', 'gaffe', 'gages', 'gains', 'gaits', 'galls', 'gamed', 'gamer', 'games', 'gamey', 'gamma', 'gangs', 'gapes', 'garbs', 'gasps', 'gaspy', 'gassy', 'gated', 'gater', 'gates',
        'gator', 'gauge', 'gauze', 'gavel', 'gawks', 'gawky', 'gayer', 'gayly', 'gazed', 'gazer', 'gazes', 'gears', 'gecko', 'geeks', 'geeky', 'geese', 'genes', 'genie', 'gents', 'genus',
        'geode', 'germs', 'germy', 'getup', 'ghost', 'ghoul', 'giant', 'giddy', 'gifts', 'gills', 'gilly', 'gimme', 'gimps', 'gimpy', 'gipsy', 'girls', 'girly', 'girth', 'given', 'giver', 
        'gives', 'gizmo', 'glade', 'gland', 'glare', 'glary', 'glass', 'glaze', 'gleam', 'glean', 'glint', 'glitz', 'gloat', 'globe', 'globs', 'gloom', 'glory', 'gloss', 'glove', 'glows',
        'glued', 'gluer', 'glues', 'gluey', 'flute', 'glyph', 'gnarl', 'gnash', 'gnats', 'gnaws', 'gnome', 'goads', 'goals', 'goats', 'godly', 'goers', 'going', 'golds', 'golem', 'golfs',
        'golly', 'goner', 'gongs', 'goods', 'goody', 'gooey', 'goofs', 'goofy', 'gooky', 'goons', 'goony', 'goops', 'goopy', 'goose', 'gored', 'gores', 'gorge', 'goths', 'gouge', 'gourd',
        'gouts', 'gowns', 'grabs', 'grace', 'grade', 'grads', 'graft', 'grail', 'grain', 'grams', 'grands', 'grant', 'grape', 'graph', 'grasp', 'grass', 'grate', 'grave', 'gravy', 'grays',
        'graze', 'great', 'greed', 'greek', 'green', 'greet', 'grids', 'grief', 'grill', 'grime', 'grimy', 'grind', 'grins', 'gripe', 'grips', 'grits', 'groan', 'groin', 'groom', 'grope', 
        'gross', 'group', 'grout', 'grove', 'growl', 'grown', 'grows', 'grubs', 'gruel', 'gruff', 'grump', 'grunt', 'guano', 'guard', 'guava', 'guess', 'guest', 'guide', 'guild', 'guile',
        'guilt', 'guise', 'gulag', 'gulfs', 'gulls', 'gully', 'gulps', 'gumbo', 'gummy', 'guppy', 'gurus', 'gushy', 'gusto', 'gusts', 'gusty', 'gutsy', 'gutty', 'gyros', 'habit', 'hacks', 
        'haiku', 'hails', 'hairs', 'hairy', 'halal', 'halls', 'halos', 'halts', 'halve', 'hands', 'handy', 'hangs', 'happy', 'hardy', 'harem', 'hares', 'harks', 'harms', 'harps', 'harpy', 
        'harsh', 'haste', 'hasty', 'hatch', 'hated', 'hater', 'hates', 'hauls', 'hault', 'haunt', 'haven', 'haves', 'havoc', 'hawks', 'hazed', 'hazer', 'hazes', 'heads', 'heady', 'heals', 
        'heaps', 'heard', 'hears', 'heart', 'heath', 'heats', 'heave', 'heavy', 'hecks', 'hedge', 'heeds', 'heels', 'hefts', 'hefty', 'heils', 'heirs', 'heist', 'helix', 'hello', 'helms', 
        'helps', 'hence', 'henna', 'herbs', 'herby', 'herds', 'hertz', 'hexed', 'hexer', 'hexes', 'hicks', 'hider', 'hides', 'hints', 'hippo', 'hippy', 'hired', 'hiree', 'hirer', 'hires',
        'hissy', 'hitch', 'hives', 'hoard', 'hoary', 'hobby', 'hobos', 'hocus', 'hoist', 'hokey', 'holds', 'holed', 'holes', 'holey', 'holly', 'holts', 'homer', 'homes', 'homey', 'homie', 
        'honed', 'honer', 'hones', 'honey', 'hopes', 'hoppy', 'horde', 'horns', 'horny', 'horse', 'hosed', 'hoser', 'hoses', 'hosts', 'hotel', 'hotly', 'hound', 'hours', 'house', 'hovel',
        'hover', 'howdy', 'howls', 'hubby', 'huffs', 'huffy', 'huggy', 'hulas', 'hulks', 'hulky', 'hulls', 'human', 'humid', 'humor', 'humps', 'humpy', 'hunch', 'hunks', 'hunky', 'hunts', 
        'hurls', 'hurry', 'hurts', 'husks', 'husky', 'hydra', 'hydro', 'hyena', 'hymns', 'hyped', 'hyper', 'hypes', 'hyrax', 'icier', 'icing', 'icons', 'ideal', 'ideas', 'idiom', 'idiot', 
        'idled', 'idler', 'idles', 'idols', 'igloo', 'iliad', 'iller', 'image', 'imbed', 'imbue', 'imply', 'inane', 'incur', 'index', 'indie', 'inept', 'inert', 'infer', 'ingot', 'inked',
        'inker', 'inlet', 'inned', 'inner', 'input', 'intel', 'inter', 'intro', 'ionic', 'irate', 'irked', 'irons', 'irony', 'isles', 'islet', 'issue', 'itchy', 'items', 'ivory', 'jacks', 
        'jaded', 'jades', 'jails', 'jaunt', 'jawed', 'jazzy', 'jeans', 'jeeps', 'jeers', 'jello', 'jelly', 'jerks', 'jerks', 'jerky', 'jests', 'jewel', 'jiffy', 'jiggy', 'jilts', 'jived',
        'jives', 'jocks', 'joins', 'joint', 'joked', 'joker', 'jokes', 'jokey', 'jolly', 'jolts', 'jolty', 'joule', 'joust', 'jowls', 'joyed', 'judge', 'judos', 'juice', 'juicy', 'juked',
        'jukes', 'jumbo', 'jumps', 'jumpy', 'junks', 'junky', 'juror', 'kappa', 'kaput', 'karat', 'karma', 'kayak', 'kazoo', 'kebab', 'keeps', 'kelts', 'keyed', 'khaki', 'kicks', 'kicky', 
        'kiddo', 'kiddy', 'kilns', 'kilos', 'kilts', 'kinds', 'kings', 'kinks', 'kinky', 'kiosk', 'kissy', 'kited', 'kiter', 'kites', 'kitty', 'kiwis', 'klutz', 'knack', 'knave', 'knead',
        'kneel', 'knees', 'knell', 'knife', 'knits', 'knobs', 'knock', 'knots', 'known', 'knows', 'koala', 'kooky', 'kraut', 'kudos', 'kudzu', 'labor', 'laced', 'lacer', 'laces', 'lacey',
        'lacks', 'laden', 'ladle', 'lager', 'lairs', 'laker', 'lakes', 'lambs', 'lamby', 'lamed', 'lamer', 'lames', 'lamps', 'lance', 'lands', 'lanes', 'lanky', 'lapel', 'lapis', 'lapse',
        'lards', 'large', 'larks', 'larva', 'laser', 'lasso', 'lasts', 'latch', 'later', 'latex', 'lathe', 'latte', 'laugh', 'lavas', 'lawns', 'laxly', 'layed', 'layer', 'layup', 'leach', 
        'leads', 'leafy', 'leaks', 'leaky', 'leans', 'leaps', 'leapt', 'learn', 'lease', 'leash', 'least', 'leave', 'ledge', 'leech', 'leeks', 'leers', 'leery', 'lefts', 'lefty', 'legal', 
        'legit', 'lemon', 'lemur', 'lends', 'lense', 'leper', 'levee', 'level', 'lever', 'liars', 'libel', 'libra', 'licks', 'liege', 'lifts', 'liger', 'light', 'liked', 'liken', 'liker',
        'likes', 'lilac', 'limbo', 'limbs', 'limes', 'limey', 'limit', 'limps', 'lined', 'linen', 'liner', 'lines', 'lingo', 'links', 'lints', 'linty', 'linux', 'lions', 'lipid', 'lisps',
        'lists', 'liter', 'lived', 'liven', 'liver', 'lives', 'livid', 'llama', 'loads', 'loafs', 'loams', 'loamy', 'loans', 'lobby', 'lobed', 'lobes', 'lobos', 'local', 'locks', 'lodes', 
        'lodge', 'lofts', 'lofty', 'loggy', 'logic', 'login', 'logos', 'loins', 'lolly', 'loner', 'loofa', 'looks', 'looms', 'loons', 'loony', 'loops', 'loopy', 'loose', 'loots', 'loped', 
        'loper', 'lopes', 'lords', 'lores', 'lorry', 'loser', 'loses', 'lotto', 'lotus', 'louse', 'lousy', 'loved', 'lover', 'loves', 'lovey', 'lower', 'lowly', 'loyal', 'lubed', 'lubes',
        'lucid', 'lucks', 'lucky', 'luged', 'luger', 'luges', 'lulls', 'lumps', 'lumpy', 'lunar', 'lunch', 'lunge', 'lungs', 'lunks', 'lurch', 'lured', 'lurer', 'lures', 'lurks', 'lusts', 
        'lusty', 'lutes', 'lymph', 'lynch', 'lyric', 'macaw', 'maced', 'maces', 'macho', 'macks', 'macro', 'madam', 'madly', 'mafia', 'mages', 'magic', 'magma', 'magus', 'maids', 'mils',
        'maims', 'mains', 'maize', 'major', 'maker', 'makes', 'males', 'malls', 'malts', 'malty', 'mamas', 'mamba', 'mamma', 'maned', 'manes', 'manga', 'mango', 'mania', 'manic', 'manly',
        'manor', 'maple', 'march', 'mares', 'marks', 'marry', 'marsh', 'marts', 'mashy', 'masks', 'mason', 'masts', 'match', 'match', 'mated', 'mater', 'mates', 'matey', 'maths', 'matte', 
        'matts', 'mauls', 'maven', 'maxed', 'maxes', 'mayan', 'maybe', 'mayor', 'mayos', 'mazes', 'meads', 'meals', 'mealy', 'means', 'meant', 'meats', 'meaty', 'medal', 'media', 'medic',
        'meets', 'melds', 'melee', 'melon', 'melts', 'melty', 'memes', 'memos', 'mends', 'menus', 'meows', 'merch', 'mercy', 'merge', 'merit', 'merry', 'mesas', 'meshy', 'messy', 'metal', 
        'meter', 'metro', 'mewed', 'mewls', 'micro', 'midst', 'might', 'miles', 'milks', 'milky', 'mills', 'mimed', 'mimer', 'mimes', 'mimic', 'mince', 'minds', 'mined', 'miner', 'mines', 
        'minor', 'mints', 'minty', 'minus', 'mired', 'mires', 'mirth', 'miser', 'mises', 'missy', 'mists', 'misty', 'mites', 'mitts', 'mixed', 'mixer', 'mixes', 'mixup', 'moans', 'moats', 
        'mocha', 'mocks', 'model', 'modem', 'modes', 'mogul', 'moist', 'mojos', 'molar', 'molds', 'moldy', 'moles', 'molly', 'molts', 'momma', 'mommy', 'money', 'monks', 'month', 'mooch', 
        'moods', 'moody', 'mooed', 'moola', 'moons', 'moony', 'moors', 'moose',  'moped', 'moper', 'mopes', 'mopey', 'moral', 'moray', 'moron', 'morph', 'morse', 'mosey', 'mossy', 'mosts', 
        'motel', 'moths', 'motif', 'motor', 'motto', 'motts', 'moult', 'mound', 'mount', 'mourn', 'mouse', 'mousy', 'mouth', 'moved', 'mover', 'moves', 'movie', 'mowed', 'mower', 'moxie',
        'mucks', 'mucky', 'mucus', 'muddy', 'muggy', 'mulch', 'mulls', 'mummy', 'mumps', 'munch', 'mural', 'murky', 'mused', 'muser', 'muses', 'mushy', 'music', 'musks', 'musky', 'musty',
        'muted', 'muter', 'mutes', 'mutts', 'myrrh', 'myths', 'nacho', 'naggy', 'nails', 'naive', 'naked', 'named', 'namer', 'names', 'nanny', 'narcs', 'nasal', 'nasty', 'natal', 'natty',
        'naval', 'navel', 'nazis', 'nears', 'neats', 'necks', 'needs', 'needy', 'neigh', 'neons', 'nerds', 'nerdy', 'nerve', 'nests', 'never', 'newer', 'newly', 'newts', 'nexus', 'nicer',
        'niche', 'nicks', 'niece', 'nifty', 'night', 'ninja', 'ninny', 'ninth', 'nippy', 'nitro', 'noble', 'nobly', 'nodes', 'noise', 'noisy', 'nomad', 'nonce', 'nooks', 'noose', 'norms',
        'north', 'nosed', 'noses', 'nosey', 'notch', 'noted', 'noter', 'notes', 'nouns', 'novel', 'nudes', 'nudge', 'nuked', 'nukes', 'numbs', 'nurse', 'nutsy', 'nutty', 'nylon', 'nymph',
        'oaken', 'oared', 'oasis', 'oaths', 'obese', 'obeys', 'occur', 'ocean', 'octal', 'octet', 'odder', 'oddly', 'odors', 'offed', 'offer', 'often', 'ogled', 'ogles', 'ogres', 'oiled',
        'oiler', 'oinks', 'olden', 'older', 'oldie', 'olive', 'ombre', 'omega', 'omens', 'omits', 'onery', 'onion', 'onset', 'oozed', 'oozes', 'opals', 'opens', 'opera', 'opium', 'opted',
        'optic', 'orals', 'orbit', 'orcas', 'order', 'organ', 'ortho', 'other', 'otter', 'ought', 'ounce', 'ousts', 'outed', 'outer', 'ovals', 'ovary', 'ovens', 'overs', 'overt', 'ovoid', 
        'owlet', 'owned', 'owner', 'oxide', 'ozone', 'paced', 'pacer', 'paces', 'packs', 'paddy', 'padre', 'pagan', 'paged', 'pager', 'pages', 'pails', 'pains', 'paint', 'pairs', 'paled',
        'paler', 'pales', 'palms', 'palmy', 'palsy', 'panda', 'paned', 'panel', 'panes', 'pangs', 'panic', 'pansy', 'pants', 'panty', 'papal', 'paper', 'parch', 'pared', 'parer', 'pares',
        'parka', 'parks', 'parry', 'parse', 'parts', 'party', 'passe', 'pasta', 'paste', 'pasts', 'pasty', 'patch', 'paths', 'patio', 'patty', 'pause', 'paved', 'paver', 'paves', 'pawed',
        'pawer', 'pawns', 'payed', 'payer', 'peace', 'peach', 'peaks', 'pearl', 'pears', 'peats', 'pecan', 'pecks', 'pedal', 'peeks', 'peels', 'peeps', 'peers', 'peeve', 'pelts', 'penal', 
        'pence', 'penny', 'peppy', 'perch', 'peril', 'perks', 'perky', 'perms', 'perps', 'pesky', 'pesto', 'pests', 'petal', 'petty', 'phage', 'phase', 'phlox', 'phone', 'phony', 'photo',
        'piano', 'picks', 'picky', 'piece', 'piers', 'piety', 'piggy', 'pigmy', 'piker', 'pikes', 'piled', 'piles', 'pills', 'pilot', 'pimps', 'pinch', 'pined', 'pines', 'piney', 'pings',
        'pinks', 'pinky', 'pints', 'pinup', 'pious', 'piped', 'piper', 'pipes', 'pipet', 'pique', 'pitch', 'piths', 'pithy', 'pivot', 'pixel', 'pixie', 'pizza', 'place', 'plaid', 'plain', 
        'plane', 'plank', 'plans', 'plant', 'plate', 'plays', 'plaza', 'plead', 'pleas', 'plebs', 'plied', 'plier', 'plies', 'plops', 'plots', 'plows', 'ploys', 'pluck', 'plugs', 'plumb',
        'plume', 'plump', 'plums', 'plush', 'poach', 'pocky', 'poems', 'poets', 'point', 'poise', 'poked', 'poker', 'pokes', 'pokey', 'polar', 'poled', 'poles', 'polio', 'polka', 'polls',
        'polos', 'polyp', 'ponds', 'pongs', 'pooch', 'pooed', 'poofs', 'poofy', 'pools', 'poops', 'popes', 'poppy', 'porch', 'pored', 'pores', 'porks', 'porky', 'ports', 'posed', 'poser',
        'poses', 'posse', 'posts', 'potty', 'pouch', 'pound', 'pours', 'pouts', 'pouty', 'power', 'prank', 'prawn', 'prays', 'preen', 'preps', 'press', 'preys', 'price', 'prick', 'pricy',
        'pride', 'pried', 'prier', 'pries', 'prime', 'print', 'prior', 'prism', 'privy', 'prize', 'probe', 'promo', 'prone', 'prong', 'proof', 'props', 'prose', 'proud', 'prove', 'prowl',
        'proxy', 'prude', 'prune', 'psalm', 'psych', 'pubic', 'pucks', 'pudgy', 'puffs', 'puffy', 'puggy', 'puked', 'pukes', 'pulls', 'pulps', 'pulpy', 'pulse', 'pumas', 'pumps', 'punch', 
        'punks', 'punky', 'punny', 'punts', 'punty', 'pupae', 'pupil', 'puppy', 'puree', 'purer', 'purge', 'purrs', 'purse', 'pushy', 'pussy', 'putty', 'pygmy', 'pylon', 'pyres', 'pyros',
        'quack', 'quads', 'quaff', 'quail', 'quake', 'quaky', 'quart', 'quash', 'queen', 'queer', 'quell', 'query', 'quest', 'queue', 'quick', 'quids', 'quiet', 'quill', 'quilt', 'quips',
        'quirk', 'quits', 'quota', 'quote', 'rabid', 'raced', 'racer', 'races', 'racks', 'radar', 'radio', 'radon', 'rafts', 'raged', 'rager', 'rages', 'raggy', 'raids', 'rails', 'rains',
        'rainy', 'raise', 'raked', 'raker', 'rakes', 'rally', 'ralph', 'ramen', 'ramps', 'ranch', 'range', 'ranks', 'rants', 'raped', 'raper', 'rapes', 'rapid', 'rared', 'rarer', 'rares',
        'rasps', 'raspy', 'rater', 'rates', 'ratio', 'ratty', 'raved', 'raven', 'raver', 'raves', 'rawer', 'rawly', 'razed', 'razer', 'razes', 'razor', ' reach', 'react', 'reads', 'ready',
        'realm', 'reals', 'reams', 'reaps', 'rearm', 'rears', 'reave', 'rebar', 'rebel' 'rebut', 'rebuy', 'recap', 'recon', 'redry', 'redux', 'reeds', 'reedy', 'reefs', 'reefy', 'reeks', 'reeks',
        'reeky', 'reels', 'refer', 'refix', 'refry', 'regal', 'rehab', 'reign', 'reins', 'relax', 'relay', 'relic', 'remit', 'remix', 'rends', 'renew', 'rents', 'repay', 'repel', 'reply', 'rerun',
        'reset', 'resin', 'rests', 'retro', 'retry', 'reuse', 'revel', 'rhino', 'rhyme', 'ribby', 'rices', 'rider', 'rides', 'ridge', 'riffs', 'rifle', 'rifts', 'right', 'rigid', 'rigor', 'riled',
        'rills', 'rinds', 'rings', 'rinks', 'rinse', 'riots', 'riped', 'ripen', 'riper', 'ripes', 'risen', 'riser', 'rises', 'risks', 'risky', 'rites', 'ritzy', 'rival', 'river', 'rivet', 'roach',
        'roads', 'roams', 'roars', 'roast', 'robed', 'robes', 'robin', 'robot', 'rocks', 'rocky', 'rodeo', 'rogue', 'roils', 'roles', 'rolls', 'roman', 'romeo', 'romps', 'roofs', 'rooks', 'rooms',
        'roomy', 'roost', 'roots', 'roped', 'roper', 'ropes', 'ropey', 'rosed', 'roses', 'roset', 'rotor', 'rouge', 'rough', 'round', 'route', 'roved', 'rover', 'rowdy', 'rower', 'royal', 'rubes',
        'rucks', 'ruddy', 'ruder', 'rugby', 'ruins', 'ruled', 'ruler', 'rules', 'rummy', 'rumor', 'rumps', 'runes', 'rungs', 'runic', 'runny', 'runts', 'rural', 'rushy', 'rusts', 'rusty', 'rutty', 
        'sable', 'sabre', 'sacks', 'sadly', 'safer', 'sagas', 'sager', 'sages', 'saggy', 'sails', 'saint', 'sakes', 'salad', 'sales', 'salon', 'salsa', 'salts', 'salty', 'salve', 'salvo', 'samba',
        'sands', 'sandy', 'sappy', 'sassy', 'sated', 'satin', 'sauce', 'saucy', 'sauna', 'saute', 'saved', 'saver', 'saves', 'savor', 'savoy', 'savvy', 'sawed', 'sawer', 'sayer', 'scabs', 'scald', 
        'scale', 'scall', 'scalp', 'scaly', 'scamp', 'scams', 'scans', 'scape', 'scare', 'scarf', 'scars', 'sary', 'scats', 'scene', 'scent', 'scoff', 'scold', 'scone', 'scoop', 'scoot', 'scope',
        'score', 'scorn', 'scots', 'scour', 'scout', 'scowl', 'scows', 'scram', 'scrap', 'screw', 'scrim', 'scrub', 'scrum', 'scuba', 'scuds', 'scuff', 'scull', 'scums', 'seals', 'seams', 'sears',
        'seats', 'sedan', 'sedge', 'seeds', 'seedy', 'seeks', 'seels', 'seems', 'seeps', 'seize', 'sells', 'semen', 'semis', 'sends', 'sense', 'serfs', 'serif', 'serum', 'serve', 'servo', 'setup',
        'seven', 'sever', 'sewed', 'sewer', 'sexes', 'shack', 'shade', 'shady', 'shaft', 'shags', 'shake', 'shaky', 'shale', 'shall', 'shame', 'shank', 'shape', 'shard', 'share', 'shark', 'sharp', 
        'shave', 'shawl', 'sheaf', 'shear', 'sheds', 'sheen', 'sheep', 'sheer', 'sheet', 'sheik', 'shelf', 'shell', 'shied', 'shies', 'shift', 'shill', 'shine', 'shins', 'shiny', 'ships', 'shire', 
        'shirt', 'shist', 'shoal', 'shock', 'shoed', 'shoer', 'shoes', 'shone', 'shook', 'shoot', 'shops', 'shore', 'shorn', 'short', 'shots', 'shout', 'shove', 'shown', 'shows', 'showy', 'shred',
        'shrew', 'shrub', 'shrug', 'shuck', 'shuns', 'shush', 'shute', 'shuts', 'shyly', 'sicko', 'sicks', 'sided', 'sides', 'siege', 'sieve', 'sifts', 'sighs', 'sight', 'sigil', 'sigma', 'signs', 
        'silks', 'silky', 'sills', 'silly', 'silos', 'silts', 'silty', 'simps', 'since', 'sinew', 'singe', 'sings', 'sinks', 'sinus', 'siren', 'sissy', 'sited', 'sistes', 'sixes', 'sixth', 'sixty', 
        'sized', 'sizer', 'sizes', 'skank', 'skate', 'skeet', 'skein', 'skelp', 'skews', 'skids', 'skied', 'skier', 'skies', 'skiff', 'skill', 'skimp', 'skims', 'skink', 'skins', 'skips', 'skirt', 
        'skits', 'skoal', 'skulk', 'skull', 'skunk', 'slabs', 'slack', 'slags', 'slain', 'slams', 'slang', 'slank', 'slant', 'slaps', 'slash', 'slate', 'slats', 'slave', 'slays', 'sleds', 'sleek',
        'sleep', 'sleet', 'slept', 'slice', 'slick', 'slide', 'slime', 'slims', 'slimy', 'sling', 'slink', 'slips', 'slits', 'slobs', 'slogs', 'slope', 'slops', 'slosh', 'sloth', 'slots', 'slows',
        'slugs', 'slump', 'slums', 'slung', 'slunk', 'slurp', 'slurs', 'slush', 'sluts', 'slyly', 'smack', 'small', 'smart', 'smash', 'smear', 'smell', 'smelt', 'smile', 'smirk', 'smite', 'smith', 
        'smock', 'smogs', 'smoke', 'smoky', 'smush', 'snack', 'snags', 'snail', 'snake', 'snaky', 'snaps', 'snare', 'snark', 'snarl', 'sneak', 'sneer', 'snide', 'sniff', 'snipe', 'snips', 'snobs',
        'snoop', 'snoot', 'snore', 'snort', 'snots', 'snout', 'snows', 'snowy', 'snuck', 'snuff', 'snugs', 'soaks', 'soaps', 'soapy', 'soars', 'sober', 'socks', 'sodas', 'soddy', 'sofas', 'softy',
        'soggy', 'soils', 'solar', 'soles', 'solve', 'sonar', 'songs', 'sonic', 'sooty', 'soppy', 'sores', 'sorry', 'sorts', 'souls', 'sound', 'soups', 'soupy', 'sours', 'south', 'sowed', 'sower',
        'space', 'spade', 'spams', 'spank', 'spans', 'spare', 'spark', 'spars', 'spasm', 'spats', 'spawn', 'speak', 'spear', 'speck', 'specs', 'speed', 'spell', 'spend', 'spent', 'sperm', 'spews', 
        'spice', 'spicy', 'spied', 'spies', 'spike', 'spiky', 'spill', 'spilt', 'spoil', 'spoke', 'spoof', 'spook', 'spool', 'spoon', 'spore', 'sport', 'spots', 'spout', 'spray', 'spree', 'sprig', 
        'spuds', 'spunk', 'spurn', 'spurs', 'spurt', 'squad', 'squat', 'squaw', 'squib', 'squid', 'stabs', 'stack', 'staff', 'stage', 'stags', 'stain', 'stair', 'stake', 'stale', 'stalk', 'stall',
        'stamp', 'stand', 'stank', 'stare', 'stark', 'stars', 'start', 'stash', 'state', 'stats', 'stave', 'stays', 'stead', 'steak', 'steal', 'steam', 'steed', 'steel', 'steep', 'steer', 'stems',
        'steps', 'stern', 'stews', 'stewy', 'stick', 'stiff', 'still', 'stilt', 'sting', 'stink', 'stint', 'stirs', 'stock', 'stoic', 'stoke', 'stole', 'stomp', 'stone', 'stony', 'stood', 'stool',
        'stoop', 'stops', 'store', 'stork', 'storm', 'story', 'stout', 'stove', 'stows', 'strap', 'straw', 'stray', 'strew', 'strip', 'strum', 'strut', 'stubs', 'stuck', 'studs', 'study', 'stuff',
        'stump', 'stung', 'stunk', 'stuns', 'stunt', 'stupe', 'style', 'stymy', 'suave', 'sucks', 'sucky', 'sudsy', 'suede', 'sugar', 'suing', 'suite', 'suits', 'sulks', 'sulky', 'sully', 'sunny',
        'super', 'surfs', 'surge', 'surly', 'sushi', 'swabs', 'swami', 'swamp', 'swang', 'swank', 'swans', 'swaps', 'swarm', 'swath', 'swats', 'sways', 'swear', 'sweat', 'swede', 'sweep', 'sweet',
        'swell', 'swept', 'swift', 'swigs', 'swill', 'swims', 'swine', 'swing', 'swipe', 'swirl', 'swish', 'swiss', 'swoon', 'swoop', 'sword', 'swore', 'sworn', 'swung', 'syncs', 'synth', 'syrup',
        'tabby', 'table', 'taboo', 'tacit', 'tacks', 'tacky', 'tacos', 'taffy', 'tails', 'taint', 'taken', 'taker', 'takes', 'talon', 'tamed', 'tamer', 'tames', 'tango', 'tangs', 'tangy', 'tanks',
        'taped', 'taper', 'tapes', 'tapir', 'tardy', 'tarot', 'tarps', 'tarry', 'tarts', 'tarty', 'tasks', 'taste', 'tasty', 'tatar', 'tater', 'taunt', 'tawny', 'taxed', 'taxer', 'taxes', 'taxis', 
        'taxon', 'teach', 'teams', 'tears', 'teary', 'tease', 'teats', 'techs', 'techy', 'teddy', 'teems', 'teens', 'teeth', 'tempo', 'temps', 'tempt', 'tends', 'tenet', 'tenor', 'tense', 'tenth',
        'tents', 'tepee', 'tepid', 'terms', 'terra', 'terry', 'terse', 'tesla', 'tests', 'testy', 'texts', 'thank', 'thaws', 'theft', 'their', 'theme', 'there', 'these', 'theta', 'thick', 'thief',
        'thigh', 'thine', 'thing', 'think', 'thins', 'third', 'thong', 'thorn', 'those', 'three', 'threw', 'throb', 'throw', 'thrum', 'thuds', 'thugs', 'thumb', 'thump', 'thunk', 'thyme', 'tiara',
        'tibia', 'ticks', 'tidal', 'tided', 'tides', 'tiers', 'tiger', 'tight', 'tikes', 'tikis', 'tilde', 'tiled', 'tiles', 'tilts', 'timed', 'timer', 'times', 'timid', 'tings', 'tints', 'tippy',
        'tipsy', 'tired', 'tires', 'titan', 'tithe', 'title', 'tizzy', 'toads', 'toady', 'toast', 'today', 'togas', 'toils', 'token', 'tolls', 'tombs', 'tomes', 'toned', 'toner', 'tongs', 'tonic', 
        'tools', 'toons', 'tooth', 'toots', 'topaz', 'topic', 'torch', 'torso', 'totem', 'touch', 'tough', 'touts', 'towed', 'towel', 'tower', 'towns', 'toxic', 'toxin', 'toyed', 'toyer', 'trace',
        'track', 'tract', 'trade', 'trail', 'train', 'trait', 'tramp', 'trams', 'trans', 'traps', 'trash', 'trawl', 'trays', 'tread', 'treat', 'trees', 'treks', 'trend', 'triad', 'trial', 'tribe',
        'trick', 'tried', 'tries', 'trike', 'trill', 'trims', 'tripe', 'trips', 'trite', 'troll', 'trope', 'trout', 'trove', 'truce', 'truck', 'truly', 'trump', 'trunk', 'trust', 'truth', 'tsars',
        'tubby', 'tubed', 'tuber', 'tucks', 'tufts', 'tufty', 'tulip', 'tummy', 'tumor', 'tuner', 'tungs', 'turbo', 'turds', 'turfs', 'turns', 'tushy', 'tusks', 'tutor', 'tutus', 'twang', 'tweak',
        'tweed', 'tween', 'tweet', 'twerp', 'twice', 'twigs', 'twine', 'twins', 'twirl', 'twist', 'tying', 'tykes', 'typed', 'types', 'udder', 'ulcer', 'ulnar', 'ultra', 'umber', 'umbra', 'unarm',
        'unary', 'unban', 'unbar', 'unbox', 'uncap', 'uncle', 'uncut', 'under', 'unfed', 'unfit', 'unify', 'union', 'unite', 'units', 'unity', 'unjam', 'unlit', 'unmet', 'untie', 'unwet', 'unzip',
        'upend', 'upped', 'upper', 'upset', 'urban', 'urged', 'urger', 'urges', 'urine', 'usage', 'users', 'usher', 'using', 'usual', 'usurp', 'utter', 'uvula', 'vague', 'valet', 'valid', 'valor',
        'value', 'valve', 'vapid', 'vapor', 'vases', 'vault', 'vaunt', 'veers', 'vegan', 'veils', 'veins', 'veiny', 'veldt', 'venom', 'vents', 'venue', 'venus', 'verbs', 'verge', 'verse', 'vests',
        'vials', 'vibes', 'vices', 'video', 'views', 'vigil', 'vigor', 'villa', 'villi', 'vines', 'vinyl', 'viola', 'viper', 'viral', 'virus', 'visas', 'visit', 'vista', 'vital', 'vivid', 'vixen',
        'vizor', 'vocab', 'vocal', 'vodka', 'vogue', 'voice', 'voids', 'voila', 'voles', 'volts', 'vomit', 'voted', 'voter', 'votes', 'vouch', 'vowed', 'vowel', 'vower', 'vulva', 'vying', 'wacko', 
        'wacks', 'wacky', 'waded', 'wader', 'wades', 'wafer', 'waffs', 'wafts', 'waged', 'wager', 'wages', 'wagon', 'wahoo', 'wails', 'waist', 'waits', 'waive', 'waked', 'waken', 'waker', 'wakes',
        'wales', 'walks', 'walls', 'waltz', 'wands', 'waned', 'wanes', 'wanks', 'wants', 'wards', 'wared', 'wares', 'warms', 'warns', 'warps', 'warts', 'warty', 'washy', 'wasps', 'waspy', 'waste',
        'watch', 'water', 'watts', 'waved', 'waver', 'waves', 'wavey', 'waxed', 'waxer', 'waxes', 'weans', 'wears', 'weary', 'weave', 'webby', 'wedge', 'wedgy', 'weeds', 'weedy', 'weeks', 'weeps',
        'weepy', 'weigh', 'weird', 'welds', 'wells', 'welsh', 'welts', 'wench', 'wests', 'wetly', 'whack', 'whale', ' wharf', 'whats', 'wheat', 'wheel', 'whelk', 'whelp', 'where', 'whets', 'which',
        'whiff', 'whigs', 'while', 'whims', 'whine', 'whiny', 'whips', 'whirl', 'whisk', 'white', 'whizz', 'whole', 'whoop', 'whore', 'whose', 'wicks', 'widen', 'wider', 'wides', 'widow', 'width',
        'wield', 'wilds', 'wiles', 'wills', 'wilts', 'wimps', 'wimpy', 'wince', 'winch', 'winds', 'windy', 'wined', 'wines', 'winey', 'wings', 'wingy', 'winks', 'wiped', 'wiper', 'wipes', 'wired',
        'wirer', 'wires', 'wiser', 'wisps', 'wispy', 'wists', 'witch' 'witty', 'wives', 'woads', 'woken', 'wolfs', 'woman', 'wombs', 'women', 'wonky', 'woods', 'woody', 'wooed', 'woofs', 'wools',
        'wooly', 'woosh', 'woozy', 'words', 'wordy', 'works', 'world', 'worms', 'wormy', 'worry', 'worse', 'worst', 'worth', 'would', 'wound', 'woven', 'wowed', 'wrack', 'wrang', 'wraps', 'wrath',
        'wreak', 'wreck', 'wrens', 'wrest', 'wring', 'wrist', 'write', 'wrong', 'wrote', 'wryly', 'xenon', 'xerox', 'xylem', 'yacht', 'yahoo', 'yanks', 'yarns', 'yawns', 'yearn', 'years', 'yeast',
        'yells', 'yelps', 'yerba', 'yetis', 'yield', 'yikes', 'yodel', 'yogas', 'yogis', 'yoked', 'yokel', 'yokes', 'yolks', 'yolky', 'young', 'yours', 'youth', 'yucca', 'yucky', 'yummy', 'yuppy',
        'yurts', 'zappy', 'zeals', 'zebra', 'zeros', 'zests', 'zesty', 'zilch', 'zincs', 'zings', 'zippy', 'zoned', 'zoner', 'zones', 'zooms', 'zowie',
        ]

        word = random.choice(dictionary)
        playerguesses = [""]
        playergrid = [""]

        
        await ctx.respond(f"Wordle is starting, good luck")
        playerWin = False
        turnCounter = 0


        while playerWin == False and turnCounter < 6:
            def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel and \
                len(msg.content) == 5
            await ctx.send("please make a guess")
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=300)
            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond and forfeited the game!")
                return
            guess = msg.content.lower()
            wordexists = False
            for things in dictionary:
                if guess == things:
                    wordexists = True
            if wordexists == False:
                await ctx.send("That word does not exist in the game dictionary, please try again.")
                continue
            else:
                playerguesses.append(guess)
                playerguesses.append("\n")
                if guess == word:
                    playergrid.append("🟩 🟩 🟩 🟩 🟩")
                    playerWin = True
                else:
                    i = 0
                    for idx, char in enumerate(guess):
                        if char == word[idx]:
                            playergrid.append("🟩")
                        elif char in word:
                            playergrid.append("🟨")
                        else:
                            playergrid.append("⬜")
                playergrid.append("\n")
                
                await ctx.send(f"**Guessed Words**\n{(' '.join(playerguesses))}**Guess Grid**\n{(' '.join(playergrid))}") 
                turnCounter = turnCounter + 1

        if playerWin == True:
            winnings = 1000
            if turnCounter == 1:
                winnings = 800
            elif turnCounter == 2:
                winnings = 600
            elif turnCounter == 3:
                winnings = 400
            elif turnCounter == 4:
                winnings = 200
            else:
                winnings = 100
            winbal = bal + winnings
            userwins = userwins + 1
            userstreak = userstreak + 1
            userturns = userturns + turnCounter + 1

            sql = "UPDATE beelevel SET coins = $1 WHERE guild_id = $2 AND user_id = $3"
            sql1 = "UPDATE wordle SET wins = $1, turns_used = $2, streak = $3  WHERE guild_id = $4 AND user_id = $5"
            await db.execute(sql, winbal, str(ctx.author.guild.id), str(ctx.author.id))
            await db.execute(sql1, userwins, userturns, userstreak, str(ctx.author.guild.id), str(ctx.author.id))
            await ctx.send(f"Congratulations, you have correctly guessed the word `{word}` and won {winnings} coins!  Come back for another word tomorrow")
        else:
            userlosses = userlosses + 1
            userstreak = 0
            userturns = userturns + 6
            sql = "UPDATE wordle SET losses = $1, turns_used = $2, streak = $3  WHERE guild_id = $4 AND user_id = $5"
            await db.execute(sql, userlosses, userturns, userstreak, str(ctx.author.guild.id), str(ctx.author.id))
            await ctx.send(f"You have run out of guesses, the correct word was `{word}`.  Come back tomorrow to try again.")

    @wordle.error
    async def wordle_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            timer = error.retry_after / 3600
            await ctx.respond(f"Please wait {timer:.2f} hours to try again")


def setup(bot: commands.Bot):
    bot.add_cog(Wordle(bot))