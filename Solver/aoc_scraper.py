"""Advent of Code scraper"""

import bs4
import requests

BASE_URL = "https://adventofcode.com"


class AdventOfCodeScraper:
    """Advent Of Code Scraper"""

    def __init__(self, session_cookie: str):
        """Give the constructor your Cookie header value for Advent Of Code page"""
        session_cookie = session_cookie.replace("session=", "")
        self.session_cookie = {"session": session_cookie}

    def get_puzzle_instructions(self, year: int, day: int, part: int) -> str | None:
        """Returns puzzle text for given year and day, part argument is either 1 or 2"""

        if part not in {1, 2}:
            return None

        url = f"{BASE_URL}/{year}/day/{day}"

        res = requests.get(url, cookies=self.session_cookie, timeout=10)
        if res.status_code != 200:
            raise RuntimeError(f"Request error: {res.content}")

        soup = bs4.BeautifulSoup(res.text, "html.parser")
        return soup.find_all("article")[part - 1].get_text()

    def get_puzzle_input(self, year: int, day: int) -> str | None:
        """Returns puzzle input text given year and day"""
        url = f"{BASE_URL}/{year}/day/{day}/input"

        res = requests.get(url, cookies=self.session_cookie, timeout=10)
        if res.status_code != 200:
            raise RuntimeError(f"Request error: {res.content}")
        return res.text.strip()
