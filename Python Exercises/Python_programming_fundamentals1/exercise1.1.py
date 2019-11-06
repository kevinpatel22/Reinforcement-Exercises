documentary = 'Man on wire'
comedy = 'Hangover'
dramedy = 'La La Land'
drama = 'Lincoln'
print('Choose your options\n 1. Documentaries\n 2. Dramas and/or\n 3. Comeedies?')
print('Answer')
interest = input().lower()
if interest == '1':
    print('We recommend you watch "{}".'.format(documentary))
elif interest == '2 and 3':
    print('We recommend you watch "{}".'.format(dramedy))
elif interest == '2':
    print('We recommend you watch "{}".'.format(drama))
elif interest == '3':
    print('We recommend you watch "{}".'.format(comedy))
