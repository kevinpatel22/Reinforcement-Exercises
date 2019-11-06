ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]


def winner():
    votes = {}
    for ballot in ballots:
        for medal, voter in ballot.items():
            if voter not in votes:
                votes.update({voter: 0})
            if medal == 'gold':
                votes[voter] += 3
            elif medal == 'silver':
                votes[voter] += 2
            elif medal == 'bronze':
                votes[voter] += 1
    return (f'Winner is {max(votes, key=votes.get)}')

print(winner())



