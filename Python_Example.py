import requests
import json
import argparse

def main(pin):
    res = requests.get(f"https://anticheat.site/api/pins/{pin}")

    if res.status_code == 200:
        data = json.loads(res.text)
        print(f"\ndata for pin {pin}\n")
        print(f"Game: {data['pin_type']}")
        print(f"Scan Time: {data['scantime']}")
        print(f"Pin: {data['pin']}")
        print(f"Country: {data['country']}")
        print(f"Sentence: {data['result']}")
        print("Detections:")
        print("\n".join([f"\t{detecc}" for detecc in json.loads(data["detects"].replace("'", "\""))]))
        print("Warnings:")
        print("\n".join([f"\t{warning}" for warning in json.loads(data["warnings"].replace("'", "\""))]))
        #print("Suspicious Files:") # jean forgot to add suspicious, so remove the # when the api updates again.
        #print("\n".join([f"\t{file}" for file in json.loads(data["suspicious"].replace("'", "\""))]))
        print("Exec List:")
        print("\n".join([f"\t{file}" for file in json.loads(data["execlist"].replace("'", "\""))]))
    else:
        print(f"Invalid pin or data | {res.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check PIN data")
    parser.add_argument("pin", help="Your 6 digit pin")
    args = parser.parse_args()
    main(args.pin)
