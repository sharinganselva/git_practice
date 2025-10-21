import numpy as np


def detect_anomaly(nums, threshold):
    mean = np.mean(nums)
    std = np.std(nums)
    anamolies = []

    for i, value in enumerate(nums):
        z_score = (value - mean)/std if std > 0 else 0
        if abs(z_score) > threshold:
            anamolies.append(value)

    return anamolies


if __name__ == "__main__":
    payments = [100, 102, 98, 105, 500, 103, 101, 95, 600, 99, 102]
    print(f"The Anamolies are: {detect_anomaly(payments, 1)}")
