import argparse

def parse_args():
    desc = "Scaloni Greedy"
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument("filename", help="filename of sample")
    
    return parser.parse_args()
