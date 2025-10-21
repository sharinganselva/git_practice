from datetime import datetime
import os


def find_gaps(log_file, gap_threshold=10):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_location = base_path+log_file
    print(f"file_location = {file_location}")
    prev_timestamp = None
    gaps = []
    with open(file_location, "r") as f:
        for line in f:
            # print(line)
            # print(line.split(" ")[0])
            # print(line.split(" ")[1].split(",")[0])
            time_string = line.split(
                " ")[0] + " " + line.split(" ")[1].split(",")[0]
            timestamp = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
            if prev_timestamp is not None:
                time_diff = (timestamp - prev_timestamp).total_seconds()
                # print(time_diff)
                if time_diff > 10:
                    gaps.append((timestamp, prev_timestamp))
                    print(f"Gap found at {timestamp} and {prev_timestamp}")

            prev_timestamp = timestamp
            return gaps


if __name__ == "__main__":
    log_file = "/logs/sample_logs.log"
    gaps = find_gaps(log_file, 10)
    if len(gaps) == 0:
        print("There are no gaps found")
