import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  # Convert seconds into minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"  # Format as MM:SS
        print(timer, end="\r")  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("Time up!")  # Display when the timer finishes

# Example usage
countdown_seconds = int(input("Enter the countdown time in seconds: "))
countdown_timer(countdown_seconds)
