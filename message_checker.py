import re


class MessageChecker:
    """
    Class to handle checking of messages.
    """

    checker_start_string = "checker"

    # --- TOP LEVEL METHODS -----------------------------------------------------------------------------------------

    def __init__(self, config):
        """
        Constructor.
        :param config: YAML config.
        """
        # The config["illegal_regexes"] object is a dictionary whose keys are names for the rules and whose
        # values are regex strings.
        # This reads those in and compiles each regex.
        self.illegal_regexes = \
            [(illegal, re.compile(config["illegal_regexes"][illegal], re.I)) for illegal in config["illegal_regexes"]]

        self.illegal_checkers = [
            self.checker_basic_regex
        ]

    def validate_message(self, message):
        """
        Validates a message based on the `self.illegal_checkers` list.
        :param message: The message to validate.
        :return: The name of the rule broken (if any), and None if none were.
        """
        print(f"Validating message: {message}")

        for checker in self.illegal_checkers:
            print(f"\tUsing checker: {checker.__name__}")

            rule_broken = checker(message)  # noqa
            if rule_broken is not None:
                return rule_broken

        return None

    # --- ILLEGAL MESSAGE CHECKERS ----------------------------------------------------------------------------------

    def checker_basic_regex(self, message):
        """
        Checks messages against basic regex rules.
        :param message: The message to check.
        :return: The name of the rule broken, or None otherwise.
        """
        for regex in self.illegal_regexes:
            # regex[1] contains the actual regex Pattern
            if regex[1].search(message) is not None:
                return regex[0]  # The name of the rule
        return None

