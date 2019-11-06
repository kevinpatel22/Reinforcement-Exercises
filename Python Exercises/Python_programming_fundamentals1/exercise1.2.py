documentary = 'Man on wire'
comedy = 'Hangover'
dramedy = 'La La Land'
drama = 'Lincoln'
print('Rate your appreciation on a scale from one to five:\n 1. Documentaries\n 2. Dramas\n 3. Comeedies')
print('Rate documentaries!')
interest_doc = int(input())
print('Rate dramas!')
interest_dram = int(input())
print('Rate comedies!')
interest_com = int(input())
if interest_doc >= 4 or interest_doc > interest_dram and interest_doc > interest_com:
    print('We recommend you watch "{}".'.format(documentary))
elif interest_doc <= 3 and interest_dram >= 4 and nterest_com >= 4:
    print('We recommend you watch "{}".'.format(dramedy))
elif interest_dram >= 4 or interest_dram > interest_doc and interest_dram > interest_com:
    print('We recommend you watch "{}".'.format(drama))
elif interest_com >= 4 or interest_com > interest_doc and interest_com > interest_dram:
    print('We recommend you watch "{}".'.format(comedy))