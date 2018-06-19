poll = {
    'paul': 'already take poll',
    'damon': 'not yet',
    'stefen': 'already take poll',
    'vanessa': 'not yet'
    }
include = ['vanessa', 'paul']
for key in poll.keys():
    if key in include:
        print(key.title() + ", thank you for taking the poll.")
    else:
        print(key.title() + ", please take the poll soon.")

if 'Edward' not in poll.keys():
    print("Edward, please take the poll soon.")
