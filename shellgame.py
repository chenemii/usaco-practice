def main():
    with open("shell.in") as read:
        n = int(read.readline())

        shell_at_pos = []
        for i in range(3):
            shell_at_pos.append(i)

        counter = [0,0,0]

        for _ in range(n):
            a, b, g = [int(i) - 1 for i in read.readline().split()]
            shell_at_pos[a], shell_at_pos[b] = shell_at_pos[b], shell_at_pos[a]
            counter[shell_at_pos[g]]+=1

        with open("shell.out", "w") as out:
            print(max(counter), file = out)

main()
