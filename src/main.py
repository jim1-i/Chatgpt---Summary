import argparse
from backend import summarize_text
from utils import read_txt_file, write_txt_file

def main():
    parser = argparse.ArgumentParser(description="Summarize the main idea of a text file using ChatGPT.")
    parser.add_argument("--file", required=True, help="Path to the input .txt file.")
    parser.add_argument("--output", help="Optional path to save the summary output.")
    args = parser.parse_args()

    content = read_txt_file(args.file)
    summary = summarize_text(content)
    print("Summary:\n", summary)

    if args.output:
        write_txt_file(args.output, summary)
        print(f"Summary saved to: {args.output}")

if __name__ == "__main__":
    main()
