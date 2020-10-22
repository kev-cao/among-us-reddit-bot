import random


def build_reply(username):
    reply = """
. 　　　。　　　　•　 　ﾟ　　。 　　.

　　　.　　　 　　.　　　　　。　　 。　. 　

.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•

{0}

　　'　　　 {1} 　 　　。

 ﾟ　　　.　　　.&nbsp;&nbsp;&nbsp;&nbsp; , 　   　     　.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     ."""

    description = "\n\n&nbsp;\n\n---------------------------------\n\nYou can summon this bot using `/u/username is sus`.\n\nIf you're interested in the source code, [you can find it here.](https://github.com/defCoding/among-us-reddit-bot)"

    username = f'/u/{username}'

    # Randomly choose if the user is an imposter.
    if random.randrange(2) == 0:
        line1 = f'{username} was not an Impostor.'
        line2 = f'2 Impostors remain'
    else:
        line1 = f'{username} was an Impostor.'
        line2 = f'1 Impostor remains'

    # Add proper spacing for line1.
    line_width = 45
    padding = '&nbsp;' * ((line_width - len(line1)) // 2)

    line1 = f'&nbsp;ﾟ{padding + line1 + "&nbsp;" * 5}。   .'

    return reply.format(line1, line2) + description

if __name__ == '__main__':
    print(build_reply('Luclid'))
