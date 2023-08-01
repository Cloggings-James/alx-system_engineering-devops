#!/usr/bin/env ruby

# Get the input string from the command line argument
input_string = ARGV[0]

# Use regular expression to find occurrences of 'hbtn' with at least two 't's (without square brackets)
match_result = input_string.scan(/hb+t+n/)

# Print the matched result
puts match_result.join

