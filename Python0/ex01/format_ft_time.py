import time

epoch_time = time.time()

formatted_date = time.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {epoch_time} or {epoch_time:.2e} in scientific notation")
print(formatted_date)
