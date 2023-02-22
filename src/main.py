class BotSubject:
    name = "Simple Subject"

    def __init__(self) -> None:
        self.utterances = [
            "I want something",
            "Let's go",
        ]
        self.start = False
        self.slots = [
            {
                "question": "Please select (A, B, C)",
                "options": ("A", "B", "C"),
            },
            {
                "question": "Please select (1, 2, 3)",
                "options": ("1", "2", "3"),
            },
        ]
        self.wait_slot_response = False
        self.slot_i = -1
        self.results = []
        self.confirmation = "You select {}"
        self.wait_confirmation = False
        self.end = "Bye!"

    def __call__(self, text) -> str:
        if self.start or text in self.utterances:
            self.start = True

            if self.wait_slot_response:
                if text in self.slots[self.slot_i]["options"]:
                    self.results.append(text)
                else:
                    return self.slots[self.slot_i]["question"]
            
            self.slot_i += 1
            
            if self.slot_i < len(self.slots):
                self.wait_slot_response = True
                return self.slots[self.slot_i]["question"]
            
            self.wait_slot_response = False
            
            if not self.wait_confirmation:
                self.wait_confirmation = True
                return self.confirmation.format(self.results)
            else:
                if text == "yes":
                    ...
                    return self.end
                else:
                    self.results = []
                    self.slot_i = -1
                    self.wait_confirmation = False
                    return self.__call__("")


if __name__ == "__main__":
    bot_subject = BotSubject()

    while True:
        text = input("> ")
        print("bot >", bot_subject(text))