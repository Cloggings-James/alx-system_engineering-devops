#!/usr/bin/env ruby

# Read the log file content from the command line argument
log_content = ARGV[0]

# Use regular expressions to extract the required information
matches = log_content.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# Format the extracted information as [SENDER],[RECEIVER],[FLAGS]
formatted_output = matches.map { |match| "#{match[0]},#{match[1]},#{match[2]}" }

# Print the formatted output
puts formatted_output.join("\n")

