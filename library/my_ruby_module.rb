#!/usr/bin/env ruby

require "json"

params = {}

arguments = File.read(ARGV[0])
arguments.split(" ").each do |argument|
  key, value = argument.split("=")

  next unless key && value

  params[key] = value
end

# This is how you fetch parameters
params["name"]

puts ({ change: true, params: params }).to_json
