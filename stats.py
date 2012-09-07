#!/usr/bin/env python

import sys
import time
import curses
import curses.wrapper

procs = ["first", "second", "third", "fourth"]

def main(stdscr):
    stdscr.border(0)
    stdscr.nodelay(1)
    curses.curs_set(0)
    start = int(time.time())
    while True:
        stdscr.addstr(1, 2, "Elapsed: " + str(int(time.time())))
        for idx, proc in enumerate(procs):
            stdscr.addstr(idx + 3, 2, proc)
        stdscr.refresh()
        c = stdscr.getch()
        if c == ord('q'):
            sys.exit(0)
        curses.napms(1000)

if __name__ == "__main__":
    curses.wrapper(main)
