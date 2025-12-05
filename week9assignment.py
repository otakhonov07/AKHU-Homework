def process_logs(logs, min_level):
    levels = ["INFO", "WARNING", "ERROR"]
    min_index = levels.index(min_level)
    result = []

    for line in logs:
        if line.strip() == "":
            continue

        if "[" not in line or "]" not in line or " - " not in line:
            continue

        start = line.index("[") + 1
        end = line.index("]")
        level = line[start:end]

        if level not in levels:
            continue

        if levels.index(level) < min_index:
            continue

        time_part = line[11:16]
        parts = line.split(" - ", 1)  

        if len(parts) < 2:
            continue

        message = parts[1]
        summary = f"{level} ({time_part}): {message}"
        result.append(summary)

    return result