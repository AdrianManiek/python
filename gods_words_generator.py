import random
import sys
import termios
import tty


WORDS = [
    "computer", "crazy town", "Monika Lewinsky", "python", "God",
    "Nick Nolte", "flower", "Bible", "Clint Eastwood", "CIA",
    "Morgan Freeman", "America", "sun", "discord", "Adam and Eve",
    "wall", "earth", "wife", "fedora", "KDE", "Lisboa", "win",
    "vinyls", "comunism", "blood", "clock", "coffee",
    "capitalism", "beaver", "swim", "adult", "meat", "money",
    "alien", "death", "parrot", "strawberry", "pleasure",
    "riddle", "fun"
]


def wait_for_enter(read_char):
    """Wait until Enter is pressed."""
    while True:
        if read_char(1) in ("\n", "\r"):
            return


def draw_words(words, read_char, choose_word, write, flush):
    """
    Pure application logic.
    No terminal, no randomness, no side effects.
    """
    available = list(words)

    write("Press Enter to draw next word. Ctrl+C to stop.\n")
    write("Drawn words: ")
    flush()

    try:
        while available:
            wait_for_enter(read_char)
            chosen = choose_word(available)
            available.remove(chosen)

            write(chosen + ", ")
            flush()

    except KeyboardInterrupt:
        write("\n\nInterrupted by user (Ctrl+C).")

    write("\nNo more input words available.\n")
    write("Done.\n")
    flush()


def main():
    """
    Terminal-specific layer.
    This is the ONLY place that touches termios / tty.
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        # disable Enter echo, but keep Ctrl+C working
        tty.setcbreak(fd)

        draw_words(
            words=WORDS,
            read_char=sys.stdin.read,
            choose_word=random.choice,
            write=sys.stdout.write,
            flush=sys.stdout.flush
        )

    finally:
        # always restore terminal state
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


if __name__ == "__main__":
    main()
