#!/usr/bin/env python

import curses
import curses.wrapper

procs = ["first", "second", "third", "fourth"]

def main(stdscr):
    stdscr.border(0)
    for idx, proc in enumerate(procs):
        stdscr.addstr(idx + 1, 2, proc)
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
