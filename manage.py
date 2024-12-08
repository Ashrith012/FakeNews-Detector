def max_alternating_string_worth(binary_string, worths):
    n = len(binary_string)
    max_worth_removed = 0
    prev_char = None
    max_alternating_worth = 0
    
    # Two arrays to store worth of current alternating string ending with '0' or '1'
    dp0 = [0] * n  # Max worth if ending with '0'
    dp1 = [0] * n  # Max worth if ending with '1'

    for i in range(n):
        worth = worths[i]
        
        if binary_string[i] == '0':
            # Current worth for an alternating string ending with '0'
            dp0[i] = (dp1[i - 1] if i > 0 else 0) + worth
            dp1[i] = dp1[i - 1] if i > 0 else 0  # Carry forward previous value
        else:  # binary_string[i] == '1'
            dp1[i] = (dp0[i - 1] if i > 0 else 0) + worth
            dp0[i] = dp0[i - 1] if i > 0 else 0  # Carry forward previous value
    
    max_alternating_worth = max(dp0[-1], dp1[-1])
    total_worth = sum(worths)
    max_worth_removed = total_worth - max_alternating_worth

    return max_worth_removed


# Input handling
binary_string = input().strip()
worths = list(map(int, input().strip().split()))

# Function call and result
result = max_alternating_string_worth(binary_string, worths)
print(result)
