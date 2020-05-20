#!/usr/bin/ruby
# Перевод из нормализованной модели RGB в десятичное представление
# или шестандцатиричное.
#
# Input example:
# ./nrgb2hex.rb 0.5 0.3
# Output example:
# #0804D
#
# Input example2:
# ./nrgb2hex.rb 0.5 0.3 -d
# Output example2:
# 0 128 77

nums = ARGV.select { |x| x.match /\d+/}
flag = ARGV - nums
puts '#' + nums.map { |x| (x.to_f * 255).round.to_s(16).size > 1 ? (x.to_f * 255).round.to_s(16) : (x.to_f * 255).round.to_s(16).insert(0, '0') }.join('').upcase if (flag.empty? || flag[0] == "-h")  && !nums.empty?
puts nums.map { |x| (x.to_f * 255).round.to_s }.join(' ').upcase if !flag.empty? && !nums.empty? && flag[0] == "-d"
