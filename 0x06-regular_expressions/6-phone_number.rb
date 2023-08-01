#!/usr/bin/env ruby

# Get the input string from the command line argument
input_string = ARGV[0]

# Use regular expression to match a 10-digit phone number
match_result = input_string.scan(/^\d{10}$/)

# Print the matched result
puts match_result.join

