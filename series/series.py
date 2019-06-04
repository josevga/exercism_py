def slices(series, length):
    if not series or length <= 0 or length > len(series):
        raise ValueError("Error: wrong length")
    return [series[i:i + length] for i in range(0, len(series) - length + 1)]
