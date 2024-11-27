import argparse
import re


def convert_to_srt(input_file, output_file):
    """
    Converts a text file with timestamped lines (containing \n characters) to SRT subtitle format.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output SRT file.
    """
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        content = infile.read()

        # Split content by \n and process each line
        lines = content.split("\\n")
        subtitle_index = 1

        for line in lines:
            # Match timestamp and text using regex
            match = re.match(
                r"\[(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})\]\s+(.*)",
                line.strip(),
            )
            if match:
                start_time, end_time, text = match.groups()

                # Write subtitle index
                outfile.write(f"{subtitle_index}\n")
                # Write timestamps in SRT format
                outfile.write(
                    f"{start_time.replace('.', ',')} --> {end_time.replace('.', ',')}\n"
                )
                # Write subtitle text
                outfile.write(f"{text}\n\n")

                subtitle_index += 1


def main():
    """
    Main function to parse CLI arguments and run the conversion.
    """
    parser = argparse.ArgumentParser(
        description="Convert a timestamped text file to SRT subtitle format."
    )
    parser.add_argument("input", help="Path to the input text file.")
    parser.add_argument("output", help="Path to the output SRT file.")

    args = parser.parse_args()

    # Run the conversion
    convert_to_srt(args.input, args.output)
    print(f"Subtitle file '{args.output}' has been created successfully.")


if __name__ == "__main__":
    main()
