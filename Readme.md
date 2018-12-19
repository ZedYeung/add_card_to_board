This program add a Trello card with labels and a comment to the X column of board Y.  

(ps: X and Y are index rather than ID. With ID, you could directly use Official API)

# Dependency
In requirement.txt  
[py-trello](https://github.com/sarumont/py-trello)


# Prepare
[Generate api_key and api_secret](https://trello.com/1/appKey/generate)  
Store in .config.json file
```
{
  "api_key": "",
  "api_secret": "",
  "token": "",
  "token_secret": ""
}
```

# Usage
python add_card_to_board.py -n "test" -c "test" --board_idx 3 --list_idx 1 --labels 1 3 5

labels: list of label id