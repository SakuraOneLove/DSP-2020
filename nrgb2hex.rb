#!/usr/bin/ruby

nums = ARGV.select { |x| x.match /\d+/}
flag = ARGV - nums
puts '#' + nums.map { |x| (x.to_f * 255).round.to_s(16) }.join('').upcase if (flag.empty? || (flag[0] == "-h" unless flag.empty?)) && !nums.empty?
puts nums.map { |x| (x.to_f * 255).round.to_s }.join(' ').upcase unless flag.empty? && nums.empty && (flag[0] == "-d" unless flag.empty?)
