import sys
import time
# import shutil


def ft_tqdm(lst: range):
    """
    My version of tqdm progress bar.

    Args:
        lst (range): range of numbers to iterate over
    """

    # Set variables
    total = len(lst)
    start_time = time.time()

    # Get terminal size (width)
    # terminal_width, _ = shutil.get_terminal_size(fallback=(100, 20))
    # bar_length = terminal_width - 20

    for i, item in enumerate(lst):

        # Calculate the percentage of completion
        percent = (i + 1) / total
        bar_length = 160 - len(f"{i + 1}/{total}")
        filled_length = int(bar_length * percent)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)

        # Calculate the time remaining
        elapsed_time = time.time() - start_time
        if percent > 0:
            remaining_time = elapsed_time / percent - elapsed_time
        else:
            remaining_time = 0

        # Print the progress bar
        if i % 20 == 0 or i == total - 1:
            n = i
            if n == total - 1:
                n += 1
            sys.stdout.write(
                f"\r{percent:.0%}|{bar}| {n}/{total} "
                f"[{int(elapsed_time // 60):02}:{int(elapsed_time % 60):02}<"
                f"{int(remaining_time // 60):02}"
                f":{int(remaining_time % 60):02}, "
                f"{(i + 1) / elapsed_time if elapsed_time > 0 else 0:.2f}it/s]"
            )
            sys.stdout.flush()
        yield item

    # Print a newline after the progress bar
    print()


if __name__ == "__main__":
    for _ in ft_tqdm(range(100)):
        time.sleep(0.1)
