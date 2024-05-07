seconds = int(input())

days = seconds // (24 * 3600)
seconds %= (24 * 3600)
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(f"{days}\n{hours}\n{minutes}\n{seconds}")