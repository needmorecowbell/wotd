## Word of the Day

A small script for getting Merriam Webster's Word of the Day

## Requirements

- python3


## Setup

Clone this reposiitory and run: `pip3 install -r requirements.txt`

## Operation

```
python3 wotd.py
```

## Example output:

```
$ python3 wotd.py
Word of the Day: oaf
        1 : a stupid person : boob
        2 : a big clumsy slow-witted person
```

## Tips

I've put this script in `/usr/bin/`, added a shebang, renamed it wotd, and gave myself executable permissions on the file. In this way I can call `wotd` from anywhere in the terminal, including scripts. I use this to populate my work computer's ssh server motd so I can see a new word each day when I ssh in.


## Contributions

- Please contribute! If there's an error let me know -- even better if you can fix it :)
- Thank you Merriam Webster
