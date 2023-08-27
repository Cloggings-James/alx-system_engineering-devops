#!/usr/bin/env ruby

# Get the input string from the command line argument
input_string = ARGV[0]

# Use regular expression to match capital letters in the input string
match_result = input_string.scan(/[A-Z]/)

# Print the matched result
puts match_result.join

