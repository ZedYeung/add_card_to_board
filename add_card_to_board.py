from trello import TrelloClient
import json
import argparse


def add_card_to_board(board_idx, list_idx, name, comment, labels):
    boards = client.list_boards()
    board = boards[board_idx]

    if not labels:
        labels = board.get_labels(fields="all", limit=50)

    lists = board.get_lists(list_filter="all")
    list_ = lists[list_idx]

    card = list_.add_card(name, desc=None, labels=labels, due="null", source=None,
                          position="bottom", assign=None)
    card.comment(comment)

    return card


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="add trello card to board",
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--board_idx', type=int, help="board index", required=True)
    parser.add_argument('--list_idx', type=int, help="list index", required=True)
    parser.add_argument('-n', '--name', help="card name", default="new")
    parser.add_argument('-c', '--comment', help="comment for the card", default="")
    parser.add_argument('-l', '--labels', nargs='*', help='card labels')

    # get args
    args = parser.parse_args()

    board_idx = args.board_idx
    list_idx = args.list_idx
    name = args.name
    comment = args.comment
    labels = args.labels

    with open("./.config.json") as f:
        config = json.load(f)

    api_key = config['api_key']
    api_secret = config['api_secret']
    token = config['token']
    token_secret = config['token_secret']

    client = TrelloClient(
        api_key=api_key,
        api_secret=api_secret,
        token=token,
        token_secret=token_secret
    )

    card = add_card_to_board(board_idx, list_idx, name, comment, labels)
    print("Add card {} with comment {} in board {} list {}".format(
        name, comment, board_idx, list_idx))
