class GameHistory:
    def __init__(self):
        self.records = []

    def add_record(self, word, won, attempts_remaining):
        record = {
            "word": word,
            "result": "Won" if won else "Lost",
            "attempts_remaining": attempts_remaining
        }
        self.records.append(record)

    def show_summary(self):
        print("\n--- Game History ---")
        for i, record in enumerate(self.records, start=1):
            print(f"Game {i}: Word = {record['word']}, Result = {record['result']}, Attempts left = {record['attempts_remaining']}")