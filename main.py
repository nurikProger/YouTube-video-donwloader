from pytube import YouTube


def download_crispiest(url):
	# Creating a YouTube object
	yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)

	# Filtering streams & selecting the highest resolution
	yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
	yt.download()

def on_progress(chunk, file_handler, bytes_remaining):
    percent = round((1 - bytes_remaining / chunk.filesize) * 100, 2)
    value = percent
    if percent < 10:
        percent = "  " + str(percent)
    elif percent < 100:
        percent = " " + str(percent)
    else:
        percent = str(percent)
    if len(percent) != 6:
        percent = percent + " "
    width = 40
    cell = int(value / 2.5)
    spaces = width - cell
    total = round(chunk.filesize / 1024 ** 2, 2)
    done = round((chunk.filesize - bytes_remaining) / (1024 ** 2), 2)
    if len(str(done)) > len(str(total)):
        done = str(done) + " " * (len(str(total)) - len(str(done)))
    print("|" + ("█" * cell) + (" " * spaces) + "|" + " {} %".format(percent) + "      {}/{} MB".format(done, total),
          end="\r")


def on_complete(steam, file_dir):
    print()
    print("\nSuccessfully saved as {}".format(file_dir))


if __name__ == "__main__":
	url = input("Input video url:\n")
	print('\nDownloading...\n')
	download_crispiest(url)