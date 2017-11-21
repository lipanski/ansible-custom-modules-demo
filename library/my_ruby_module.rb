#!/usr/bin/env ruby

require "json"

result = { changed: true }

args_file = ARGV[0]
data = File.read(args_file)
args = data.split(" ")

puts result.to_json
#exit 0
