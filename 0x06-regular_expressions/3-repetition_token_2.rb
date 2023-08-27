#!/usr/bin/env ruby

# Get the input string from the command line argument
input_string = ARGV[0]

# Use regular expression to find occurrences of 'hbtn' with at least two 't's
match_result = input_string.scan(/hbt+n/)

# Print the matched result
puts match_result.join

