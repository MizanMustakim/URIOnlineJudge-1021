N = float(input())
banknotes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print("NOTAS:")
for note in banknotes:
    note_number = ""
    if 0 <= N <= 1000000.00:
        note_number = int(N / note)
        N -= note_number * note
    print("{} nota(s) de R$ {:.2f}".format(note_number, note))
print("MOEDAS:")
for coin in coins:
    coin_number = ""
    if 0 <= N <= 1000000.00:
        coin_number = int(N / coin)
        N -= coin_number * coin
    print("{} moeda(s) de R$ {:.2f}".format(coin_number, coin))
