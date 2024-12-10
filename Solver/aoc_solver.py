from gpt_scraper import GPTScraper
from aoc_scraper import AdventOfCodeScraper

YEAR = 2024

DAY = 9

PART = 2

# Advent of Code Cookie header value, required
with open('cookie.txt', "r", encoding='utf-8') as fp:
    SESSION_COOKIE = fp.read().strip()

# Firefox profile path with logged ChatGPT account
# Use None for default account
PROFILE_PATH = r""

# Do not change this
PROMPT = """

Please provide the full Python script to solve this puzzle,
having an input file called input.txt as puzzle input.
Please answer with only the Python script.
Please make sure your python script begins with a comment and ends with a comment
"""


def _extract_code(s):
    # Find the first occurrence of #
    first_hash = s.index("#")
    # Find the last occurrence of #
    last_hash = s.rindex("#")
    # Extract everything between them
    return s[first_hash:last_hash]


def _get_puzzle_input(aoc_scraper: AdventOfCodeScraper) -> None:
    try:
        text = aoc_scraper.get_puzzle_input(YEAR, DAY)
    except Exception as e:
        return
    with open("input.txt", "w", encoding="utf-8") as fp:
        fp.write(text)


def get_solution_code(aoc_scraper: AdventOfCodeScraper) -> None:
    """Ask GPT for code solution"""
    gpt_scraper = GPTScraper(profile_path=PROFILE_PATH)
    try:
        gpt_scraper.start()

        question = ""
        if PART == 1:
            question = aoc_scraper.get_puzzle_instructions(YEAR, DAY, PART)
        elif PART == 2:
            question = aoc_scraper.get_puzzle_instructions(YEAR, DAY, 1)
            question += "\n" + aoc_scraper.get_puzzle_instructions(YEAR, DAY, PART)

        question += PROMPT

        gpt_scraper.send_message(question)

        gpt_scraper.wait_completion()

        messages = list(gpt_scraper.get_messages())
        if not messages:
            return None

        return _extract_code(messages[-1].text)
    except KeyboardInterrupt:
        return
    finally:
        gpt_scraper.quit()


def _main() -> str:

    aoc_scraper = AdventOfCodeScraper(SESSION_COOKIE)

    # Save puzzle input file
    _get_puzzle_input(aoc_scraper)

    # Ask ChatGPT for solution code
    return get_solution_code(aoc_scraper)


if __name__ == "__main__":
    # Exec solution code
    try:
        code = _main()
        print(code)
        exec(code)
    except Exception as e:
        print(f"Error: {e}")
