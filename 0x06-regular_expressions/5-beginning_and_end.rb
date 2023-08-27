#!/usr/bin/env ruby

# Get the input string from the command line argument
input_string = ARGV[0]

# Use regular expression to match a string starting with 'h', ending with 'n', and having any single character in between
match_result = input_string.scan(/^h.n$/)

# Print the matched result
puts match_result.join

