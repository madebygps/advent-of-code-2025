with open("ranges.csv", "r") as f:
    ranges = f.read().strip().split(",")

total_sum = 0

for r in ranges:
    # could use split, but map splits and converts to int in one go
    start, end = map(int, r.split("-"))
    for i in range(start, end + 1):
        s = str(i)
        # invalid id has to be made of ONLY repeated patterns, upper limit is half the length
        for possible_pattern_lengths in range(1, len(s) // 2 + 1):
            # pattern has to fit exactly into entire id
            if len(s) % possible_pattern_lengths == 0:
                # grab the potential pattern
                potential_pattern = s[:possible_pattern_lengths]
                # repeat the potential pattern enough times to match length of s
                potential_repetition = potential_pattern * (len(s) // possible_pattern_lengths)
                # compare and if it matches, we have an invalid id
                if s == potential_repetition:
                    total_sum += i
                    break

print(f"Total matching numbers found: {total_sum}")
